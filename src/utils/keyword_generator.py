import asyncio
import httpx
from datetime import datetime, timedelta
from typing import List, Dict, Any
from loguru import logger

from utils.config_loader import load_config
from utils.notifier import FeishuNotifier


class KeywordGenerator:
    """自动关键词生成器"""

    def __init__(self, config=None):
        self.config = config or load_config()
        self.app_id = self.config.bots["feishu"].app_id
        self.app_secret = self.config.bots["feishu"].app_secret
        
        # Bitable configs
        self.kb_base_token = self.config.keyword_table.base_token
        self.kb_table_id = self.config.keyword_table.table_id
        self.ticket_app_token = self.config.feishu_ticket.app_token
        
        # Generator configs
        gen_cfg = getattr(self.config.keyword_table, "generator", {})
        self.history_days = gen_cfg.get("history_days", 7)
        self.min_cluster_size = gen_cfg.get("min_cluster_size", 2)
        self.ticket_table_ids = gen_cfg.get("ticket_table_ids", [])
        if not self.ticket_table_ids:
            # Fallback to config values if omitted
            self.ticket_table_ids = [
                self.config.feishu_ticket.bug_table_id,
                self.config.feishu_ticket.feature_table_id
            ]

        # LLM
        from anthropic import Anthropic
        client_kwargs = {"api_key": self.config.llm.api_key}
        if self.config.llm.base_url:
            client_kwargs["base_url"] = self.config.llm.base_url
        self.llm_client = Anthropic(**client_kwargs)

    async def _get_tenant_access_token(self) -> str:
        """获取飞书 token"""
        url = "https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal"
        async with httpx.AsyncClient() as client:
            resp = await client.post(url, json={
                "app_id": self.app_id,
                "app_secret": self.app_secret
            }, timeout=10.0)
            data = resp.json()
            if data.get("code") == 0:
                return data.get("tenant_access_token")
            raise Exception(f"获取 Token 失败: {data}")

    async def fetch_recent_tickets(self) -> List[Dict]:
        """获取最近提交的工单"""
        token = await self._get_tenant_access_token()
        cutoff_date = datetime.now() - timedelta(days=self.history_days)
        cutoff_timestamp = int(cutoff_date.timestamp() * 1000)
        
        all_tickets = []
        async with httpx.AsyncClient() as client:
            headers = {"Authorization": f"Bearer {token}"}
            for table_id in self.ticket_table_ids:
                if not table_id:
                    continue
                url = f"https://open.feishu.cn/open-apis/bitable/v1/apps/{self.ticket_app_token}/tables/{table_id}/records"
                
                # Using search API instead of list to allow dynamic fetching
                # Simple loop to fetch all and filter by timestamp (since default Bitable filters are complex)
                page_token = ""
                has_more = True
                
                logger.info(f"正在拉取表格 {table_id} 的历史工单数据...")
                while has_more:
                    params = {"page_size": 100}
                    if page_token:
                        params["page_token"] = page_token
                        
                    resp = await client.get(url, headers=headers, params=params, timeout=30.0)
                    data = resp.json()
                    
                    if data.get("code") != 0:
                        logger.error(f"拉取表格 {table_id} 错误: {data.get('msg')}")
                        break
                        
                    items = data.get("data", {}).get("items", [])
                    has_more = data.get("data", {}).get("has_more", False)
                    page_token = data.get("data", {}).get("page_token", "")
                    
                    for item in items:
                        # Extract timestamps or use internal modified time if actual fields missing
                        fields = item.get("fields", {})
                        # fallback logic since created_time might not be perfectly mapped in some tables
                        created_at = item.get("created_time")
                        if not created_at:
                            continue
                            
                        # Keep recent ones
                        if int(created_at) >= cutoff_timestamp:
                            title = fields.get("标题", "")
                            description = fields.get("问题描述", "") or fields.get("问题现状", "") or fields.get("附加信息", "")
                            all_tickets.append({
                                "id": item.get("record_id"),
                                "title": title,
                                "description": description,
                                "type": fields.get("类型", "未知")
                            })
                            
        logger.info(f"共发现 {len(all_tickets)} 个距今 {self.history_days} 天内的工单记录。")
        return all_tickets

    async def analyze_and_generate(self, tickets: List[Dict]) -> List[Dict]:
        """使用 LLM 聚合并生成关键词配置"""
        if len(tickets) < self.min_cluster_size:
            logger.info("近期工单数量不足以形成热点聚类。")
            return []
            
        tickets_text = ""
        for i, t in enumerate(tickets):
            tickets_text += f"【编号{i}】\n标题：{t['title']}\n描述：{t['description'][:50]}\n类型：{t['type']}\n\n"
            
        prompt = f"""你是负责知识库建设和用户支持的数据分析专家。
我为你提供了一批最近提交的技术支持工单记录。请完成以下任务：
1. 找出这里面重复出现2次及以上的【高度相似/相同的业务咨询或报错现象】。
2. 为每个具有代表性的高频问题集，提炼出 3-5 个用户可能输入的**短小触发关键词**（例如：“导入报错、导出Excel失败”）。多个关键词需用顿号（、）隔开。
3. 根据问题集的类型，提供一个简明的回复文本样例（尽量包含问题的原因或大致解决方案，或者提醒查看相关文档）。

近期工单列表：
{tickets_text}

请严格按如下 JSON 数组格式返回结果（如果没有任何聚集出的高频问题，则返回空数组 []）：
[
  {{
    "keywords": "关键词1、关键词2、关键词3",
    "reply_content": "关于导入报错的解决方案是：请检查...",
    "issue_summary": "提取问题摘要",
    "frequency": 2
  }}
]
"""
        logger.info("开始请求 LLM 分析近期高频问题...")
        try:
            client_kwargs = {
                "model": self.config.llm.model,
                "max_tokens": 2048,
                "temperature": 0.2,
                "messages": [{"role": "user", "content": prompt}]
            }
            response = self.llm_client.messages.create(**client_kwargs)
            res_content = self._extract_text_from_response(response.content)
            
            # 解析 JSON 结果
            import json
            import re
            
            # Extract JSON block
            json_str = res_content
            json_match = re.search(r'\[[\s\S]*\]', res_content)
            if json_match:
                json_str = json_match.group(0)
                
            clusters = json.loads(json_str)
            logger.info(f"LLM 挖掘出 {len(clusters)} 个潜在高频关键词集。")
            
            # 过滤条数不满足要求的
            valid_clusters = [c for c in clusters if c.get("frequency", 0) >= self.min_cluster_size]
            return valid_clusters
            
        except Exception as e:
            logger.error(f"提取高频关键词失败: {e}")
            return []

    def _extract_text_from_response(self, content_blocks) -> str:
        """从 LLM 兼容返回值"""
        text_parts = []
        for block in content_blocks:
            block_type = getattr(block, 'type', None)
            if block_type == 'text':
                text_parts.append(block.text)
            elif hasattr(block, 'text'):
                text_parts.append(block.text)
            else:
                text_parts.append(str(block))
        return "\n".join(text_parts)

    async def write_to_bitable(self, clusters: List[Dict]) -> int:
        """将生成的草稿写入关键词飞书表格"""
        if not clusters:
            return 0
            
        token = await self._get_tenant_access_token()
        url = f"https://open.feishu.cn/open-apis/bitable/v1/apps/{self.kb_base_token}/tables/{self.kb_table_id}/records/batch_create"
        
        records = []
        for c in clusters:
            records.append({
                "fields": {
                    "关键词": c.get("keywords", ""),
                    "回复内容": c.get("reply_content", "") + f"\n\n[AI 自动分析近期发现，频率 {c.get('frequency', 0)} 次]",
                    "添加状态": "草稿/待确认"  # 故意设为非“已完成”，需要人工审核
                }
            })
            
        async with httpx.AsyncClient() as client:
            resp = await client.post(url, headers={"Authorization": f"Bearer {token}"}, json={"records": records})
            data = resp.json()
            if data.get("code") == 0:
                logger.info(f"成功将 {len(clusters)} 条关键词草稿写入飞书多维表格。")
                return len(clusters)
            else:
                logger.error(f"写入关键词飞书表失败: {data}")
                return 0

    async def execute(self):
        """执行完整流程"""
        logger.info("=== 启动关键词自动推导与生成 ===")
        try:
            tickets = await self.fetch_recent_tickets()
            if not tickets:
                logger.info("无满足时间条件的工单需要分析。")
                return
                
            clusters = await self.analyze_and_generate(tickets)
            if clusters:
                written_count = await self.write_to_bitable(clusters)
                
                # 发送 webhook 通知
                feishu_cfg = self.config.bots.get("feishu", {})
                webhook_url = feishu_cfg.get("webhook_url") if isinstance(feishu_cfg, dict) else getattr(feishu_cfg, "webhook_url", None)
                
                notifier = FeishuNotifier(webhook_url=webhook_url)
                await notifier.send_card(
                    title="💡 智能关键词发现报告",
                    content={
                        "状态": f"成功写入 {written_count} 个关键词草稿",
                        "摘要": "、".join([c.get("keywords", "") for c in clusters][:3]) + " 等",
                        "下一步": "请管理员前往关键词配置（多维表格）审核发布"
                    },
                    status="green"
                )
            else:
                logger.info("本次分析未发现符合阈值的高频共性问题。")
        except Exception as e:
            logger.error(f"关键词自动推导发生异常: {e}")

async def main():
    generator = KeywordGenerator()
    await generator.execute()

if __name__ == "__main__":
    asyncio.run(main())
