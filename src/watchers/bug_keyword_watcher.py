"""
BUG 关键词实时扫描器
定时扫描飞书群消息中的关键词，自动创建工单
"""

import subprocess
import json
import time
import schedule
from datetime import datetime, timedelta
from typing import Dict, List, Optional
from loguru import logger
from pathlib import Path

# 导入 lark-cli 封装
try:
    from src.integrations.lark_cli_wrapper import LarkCliWrapper
    from src.utils.config_loader import load_config
except ImportError:
    # 设置路径
    import sys
    sys.path.insert(0, str(Path(__file__).parent.parent.parent))
    from src.integrations.lark_cli_wrapper import LarkCliWrapper
    from src.utils.config_loader import load_config


class BugKeywordWatcher:
    """BUG 关键词扫描器"""

    # BUG 关键词列表
    BUG_KEYWORDS = [
        "报错", "崩溃", "白屏", "闪退", "打不开",
        "无法使用", "加载失败", "请求失败", "接口错误",
        "数据丢失", "保存失败", "导入失败", "导出失败",
        "卡死", "死机", "无响应", "超时"
    ]

    # 需求关键词列表
    FEATURE_KEYWORDS = [
        "希望能", "建议", "想要", "需要",
        "能不能", "可以不", "是否有", "为什么没有"
    ]

    def __init__(self, config_path: str = "config/config.yaml"):
        """
        初始化扫描器

        Args:
            config_path: 配置文件路径
        """
        self.config = load_config(config_path)
        self.lark_cli = LarkCliWrapper(self.config)

        # 监控的群 ID（可配置）
        self.watch_chat_ids = [
            "oc_9181c1f2869b0ec0af937f5c6f9a82aa",  # bot 测试群
            # 添加更多需要监控的群
        ]

        # 扫描间隔（分钟）
        self.scan_interval = 5

        # 记录已处理的消息 ID（避免重复）
        self.processed_messages: set = set()
        self.processed_file = Path("data/.processed_messages.json")

        # 加载已处理记录
        self._load_processed()

        logger.info(f"BUG 关键词扫描器已初始化，关键词: {len(self.BUG_KEYWORDS)} 个")

    def _load_processed(self):
        """加载已处理的消息记录"""
        if self.processed_file.exists():
            try:
                with open(self.processed_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    # 只保留最近 24 小时的记录
                    cutoff = datetime.now() - timedelta(hours=24)
                    for msg_id, timestamp in data.items():
                        if datetime.fromisoformat(timestamp) > cutoff:
                            self.processed_messages.add(msg_id)
                logger.info(f"加载已处理记录: {len(self.processed_messages)} 条")
            except Exception as e:
                logger.warning(f"加载已处理记录失败: {e}")

    def _save_processed(self):
        """保存已处理的消息记录"""
        try:
            self.processed_file.parent.mkdir(parents=True, exist_ok=True)
            data = {
                msg_id: datetime.now().isoformat()
                for msg_id in self.processed_messages
            }
            with open(self.processed_file, 'w', encoding='utf-8') as f:
                json.dump(data, f)
        except Exception as e:
            logger.warning(f"保存已处理记录失败: {e}")

    def search_messages(
        self,
        keyword: str,
        start_time: Optional[datetime] = None,
        end_time: Optional[datetime] = None,
        include_attachment: bool = True
    ) -> List[Dict]:
        """
        搜索飞书消息 - 使用 LarkCliWrapper

        Args:
            keyword: 搜索关键词
            start_time: 开始时间
            end_time: 结束时间
            include_attachment: 是否只搜索带附件的消息

        Returns:
            消息列表
        """
        try:
            # 使用 LarkCliWrapper 的搜索方法（已处理 Windows 路径问题）
            start_time_str = start_time.strftime("%Y-%m-%dT%H:%M:%S+08:00") if start_time else None
            end_time_str = end_time.strftime("%Y-%m-%dT%H:%M:%S+08:00") if end_time else None

            result = self.lark_cli.search_messages(
                query=keyword,
                start_time=start_time_str,
                end_time=end_time_str,
                limit=20
            )

            if result.get("success"):
                messages = result.get("messages", [])
                logger.info(f"搜索 '{keyword}' 找到 {len(messages)} 条消息")
                return messages
            else:
                logger.error(f"搜索失败: {result.get('error')}")
                return []

        except Exception as e:
            logger.error(f"搜索异常: {e}")
            return []

    def analyze_message(self, message: Dict) -> Dict:
        """
        分析消息判断是否为 BUG

        Args:
            message: 消息数据

        Returns:
            分析结果 {type: bug/feature/unknown, confidence: float, keywords: list}
        """
        content = message.get("content", "")
        content_lower = content.lower()

        # 检查 BUG 关键词
        bug_keywords_found = []
        for keyword in self.BUG_KEYWORDS:
            if keyword in content:
                bug_keywords_found.append(keyword)

        # 检查需求关键词
        feature_keywords_found = []
        for keyword in self.FEATURE_KEYWORDS:
            if keyword in content:
                feature_keywords_found.append(keyword)

        # 判断类型
        if bug_keywords_found:
            return {
                "type": "bug",
                "confidence": 0.8 + 0.1 * len(bug_keywords_found),
                "keywords": bug_keywords_found,
                "reason": f"包含 BUG 关键词: {', '.join(bug_keywords_found)}"
            }
        elif feature_keywords_found:
            return {
                "type": "feature",
                "confidence": 0.7 + 0.1 * len(feature_keywords_found),
                "keywords": feature_keywords_found,
                "reason": f"包含需求关键词: {', '.join(feature_keywords_found)}"
            }
        else:
            return {
                "type": "unknown",
                "confidence": 0.3,
                "keywords": [],
                "reason": "未匹配关键词"
            }

    def get_context_messages(self, chat_id: str, create_time: str, context_size: int = 20) -> List[Dict]:
        """
        获取消息上下文（前后各 context_size/2 条）

        Args:
            chat_id: 群 ID
            create_time: 消息时间
            context_size: 总消息数量

        Returns:
            上下文消息列表
        """
        try:
            from datetime import datetime, timedelta

            # 解析消息时间
            msg_time = datetime.fromisoformat(create_time.replace('+08:00', '+0800'))

            # 获取该消息前后的历史（前后各取一半）
            before_time = msg_time - timedelta(minutes=5)
            after_time = msg_time + timedelta(minutes=5)

            result = self.lark_cli.get_chat_messages(
                chat_id=chat_id,
                start_time=before_time.strftime("%Y-%m-%dT%H:%M:%S+08:00"),
                end_time=after_time.strftime("%Y-%m-%dT%H:%M:%S+08:00"),
                page_size=context_size,
                sort="asc"
            )

            if result.get("success"):
                return result.get("messages", [])
            else:
                logger.warning(f"获取上下文失败: {result.get('error')}")
                return []

        except Exception as e:
            logger.error(f"获取上下文异常: {e}")
            return []

    def format_context_markdown(self, messages: List[Dict], target_msg_id: str) -> str:
        """
        格式化上下文为 Markdown

        Args:
            messages: 消息列表
            target_msg_id: 目标消息 ID（高亮显示）

        Returns:
            Markdown 格式的对话内容
        """
        if not messages:
            return ""

        lines = []
        for msg in messages:
            sender = msg.get("sender", {})
            sender_name = sender.get("name", sender.get("id", "匿名"))
            content = msg.get("content", "")
            msg_id = msg.get("message_id", "")
            create_time = msg.get("create_time", "")

            # 高亮目标消息
            if msg_id == target_msg_id:
                lines.append(f"### ⚠️ **[命中消息] {sender_name}** ({create_time[:16]})")
                lines.append(f"**{content}**")
                lines.append("")
            else:
                lines.append(f"- **{sender_name}** ({create_time[:16]})")
                lines.append(f"  {content}")
                lines.append("")

        return "\n".join(lines)

    def process_found_message(self, message: Dict, analysis: Dict) -> Optional[Dict]:
        """
        处理发现的消息（创建工单）

        Args:
            message: 消息数据
            analysis: 分析结果

        Returns:
            创建结果
        """
        message_id = message.get("message_id")
        if message_id in self.processed_messages:
            logger.debug(f"消息已处理: {message_id}")
            return None

        # 记录已处理
        self.processed_messages.add(message_id)
        self._save_processed()

        try:
            # 提取消息信息
            content = message.get("content", "")
            sender_id = message.get("sender", {}).get("id", "")
            chat_id = message.get("chat_id", "")
            create_time = message.get("create_time", "")

            # 获取上下文消息
            context_messages = self.get_context_messages(chat_id, create_time)
            context_markdown = self.format_context_markdown(context_messages, message_id)

            # 准备工单数据
            ticket_data = {
                "标题": f"[关键词扫描] {content[:50]}",
                "类型": "缺陷" if analysis["type"] == "bug" else "需求",
                "环境": "待确认",
                "状态": "待处理",
                "场景还原": context_markdown if context_markdown else "无上下文",
                "补充信息": f"""
原始消息: {content[:200]}
发现关键词: {', '.join(analysis['keywords'])}
置信度: {analysis['confidence']:.1%}
发现时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
消息 ID: {message_id}
群 ID: {chat_id}
"""
            }

            # 创建记录
            result = self.lark_cli.create_record(
                table_id=self.lark_cli.bug_table_id,
                fields=ticket_data
            )

            if result.get("success"):
                logger.info(f"工单创建成功: {result['record_id']} - 关键词: {analysis['keywords']}")
                return result
            else:
                logger.error(f"工单创建失败: {result}")
                return None

        except Exception as e:
            logger.error(f"处理消息异常: {e}")
            return None

    def scan_once(self) -> Dict:
        """
        执行一次扫描

        Returns:
            扫描结果统计
        """
        logger.info("开始扫描...")

        # 时间范围：最近 scan_interval 分钟
        start_time = datetime.now() - timedelta(minutes=self.scan_interval + 1)

        stats = {
            "scanned": 0,
            "bugs_found": 0,
            "features_found": 0,
            "tickets_created": 0,
            "scan_time": datetime.now().isoformat()
        }

        # 扫描 BUG 关键词
        for keyword in self.BUG_KEYWORDS[:5]:  # 每次扫描前 5 个关键词
            messages = self.search_messages(
                keyword=keyword,
                start_time=start_time,
                include_attachment=False
            )

            for message in messages:
                stats["scanned"] += 1
                analysis = self.analyze_message(message)

                if analysis["type"] == "bug":
                    stats["bugs_found"] += 1
                    result = self.process_found_message(message, analysis)
                    if result:
                        stats["tickets_created"] += 1

        # 扫描需求关键词
        for keyword in self.FEATURE_KEYWORDS[:3]:
            messages = self.search_messages(
                keyword=keyword,
                start_time=start_time,
                include_attachment=False
            )

            for message in messages:
                stats["scanned"] += 1
                analysis = self.analyze_message(message)

                if analysis["type"] == "feature":
                    stats["features_found"] += 1
                    result = self.process_found_message(message, analysis)
                    if result:
                        stats["tickets_created"] += 1

        logger.info(f"扫描完成: 扫描 {stats['scanned']} 条, 发现 BUG {stats['bugs_found']} 个, 需求 {stats['features_found']} 个, 创建工单 {stats['tickets_created']} 个")

        return stats

    def run(self, interval_minutes: int = 5):
        """
        运行定时扫描

        Args:
            interval_minutes: 扫描间隔（分钟）
        """
        self.scan_interval = interval_minutes

        logger.info(f"启动定时扫描，间隔: {interval_minutes} 分钟")

        # 立即执行一次
        self.scan_once()

        # 设置定时任务
        schedule.every(interval_minutes).minutes.do(self.scan_once)

        # 运行循环
        while True:
            schedule.run_pending()
            time.sleep(30)


def main():
    """主函数"""
    import argparse

    parser = argparse.ArgumentParser(description="BUG 关键词扫描器")
    parser.add_argument("--interval", type=int, default=5, help="扫描间隔（分钟）")
    parser.add_argument("--once", action="store_true", help="只执行一次扫描")
    parser.add_argument("--config", default="config/config.yaml", help="配置文件路径")

    args = parser.parse_args()

    # 加载环境变量
    from dotenv import load_dotenv
    load_dotenv()

    watcher = BugKeywordWatcher(args.config)

    if args.once:
        # 单次扫描
        result = watcher.scan_once()
        print(json.dumps(result, indent=2))
    else:
        # 定时扫描
        watcher.run(args.interval)


if __name__ == "__main__":
    main()