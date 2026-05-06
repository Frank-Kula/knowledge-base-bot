"""
企微消息桥接模块
通过 WebSocket 或 Webhook 接收企微消息，统一处理后转发
"""

import asyncio
import json
from typing import Dict, Optional
from datetime import datetime
from loguru import logger
from pathlib import Path
from dotenv import load_dotenv

# 加载环境变量
load_dotenv(Path(__file__).parent.parent.parent / '.env')

try:
    from src.integrations.lark_cli_wrapper import LarkCliWrapper
    from src.utils.config_loader import load_config
except ImportError:
    import sys
    sys.path.insert(0, str(Path(__file__).parent.parent.parent))
    from src.integrations.lark_cli_wrapper import LarkCliWrapper
    from src.utils.config_loader import load_config


class WeComBridge:
    """企微消息桥接"""

    # 来源标识
    PLATFORM_NAME = "WeCom"

    def __init__(self, config_path: str = "config/config.yaml"):
        """
        初始化桥接

        Args:
            config_path: 配置文件路径
        """
        self.config = load_config(config_path)
        self.lark_cli = LarkCliWrapper(self.config)

        # 企微配置
        wecom_config = getattr(self.config.bots, 'wecom', {})
        self.webhook_url = getattr(wecom_config, 'webhook_url', '')
        self.enabled = getattr(wecom_config, 'enabled', False)

        # 记录已处理的消息
        self.processed_messages: set = set()
        self.processed_file = Path("data/.wecom_processed.json")

        self._load_processed()
        logger.info(f"企微桥接已初始化, enabled={self.enabled}")

    def _load_processed(self):
        """加载已处理记录"""
        if self.processed_file.exists():
            try:
                with open(self.processed_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    for msg_id in data.keys():
                        self.processed_messages.add(msg_id)
                logger.info(f"企微加载已处理记录: {len(self.processed_messages)} 条")
            except Exception as e:
                logger.warning(f"加载企微已处理记录失败: {e}")

    def _save_processed(self):
        """保存已处理记录"""
        try:
            self.processed_file.parent.mkdir(parents=True, exist_ok=True)
            data = {msg_id: datetime.now().isoformat() for msg_id in self.processed_messages}
            with open(self.processed_file, 'w', encoding='utf-8') as f:
                json.dump(data, f)
        except Exception as e:
            logger.warning(f"保存企微已处理记录失败: {e}")

    def normalize_message(self, raw_message: Dict) -> Dict:
        """
        标准化企微消息格式

        Args:
            raw_message: 原始企微消息

        Returns:
            标准化后的消息
        """
        #企微消息格式
        # - FromUserName: 发送者信息
        # - Content: 消息内容
        # - CreateTime: 创建时间
        # - MsgId: 消息ID

        msg_id = raw_message.get("MsgId", raw_message.get("msg_id", ""))
        sender_info = raw_message.get("FromUserName", {})
        content = raw_message.get("Content", raw_message.get("content", ""))
        create_time = raw_message.get("CreateTime", raw_message.get("create_time", ""))

        # 标准化时间格式
        if isinstance(create_time, int):
            create_time = datetime.fromtimestamp(create_time).strftime("%Y-%m-%dT%H:%M:%S+08:00")

        normalized = {
            "message_id": msg_id,
            "content": content,
            "sender": {
                "id": sender_info.get("id", sender_info.get("UserId", "")),
                "name": sender_info.get("name", sender_info.get("Name", "未知用户"))
            },
            "create_time": create_time,
            "chat_id": raw_message.get("chat_id", "wecom_default"),
            "platform": self.PLATFORM_NAME,
            "raw": raw_message  # 保留原始数据
        }

        return normalized

    def analyze_message(self, message: Dict) -> Dict:
        """
        分析企微消息（复用关键词分析逻辑）

        Args:
            message: 标准化后的消息

        Returns:
            分析结果
        """
        # 复用 bug_keyword_watcher 的关键词列表
        BUG_KEYWORDS = [
            "报错", "崩溃", "白屏", "闪退", "打不开",
            "无法使用", "加载失败", "请求失败", "接口错误",
            "数据丢失", "保存失败", "导入失败", "导出失败",
            "卡死", "死机", "无响应", "超时"
        ]

        FEATURE_KEYWORDS = [
            "希望能", "建议", "想要", "需要",
            "能不能", "可以不", "是否有", "为什么没有"
        ]

        content = message.get("content", "")

        bug_keywords_found = [kw for kw in BUG_KEYWORDS if kw in content]
        feature_keywords_found = [kw for kw in FEATURE_KEYWORDS if kw in content]

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

    def process_message(self, raw_message: Dict) -> Optional[Dict]:
        """
        处理企微消息（统一入口）

        Args:
            raw_message: 原始企微消息

        Returns:
            处理结果
        """
        # 标准化消息
        message = self.normalize_message(raw_message)
        msg_id = message["message_id"]

        # 检查是否已处理
        if msg_id in self.processed_messages:
            logger.debug(f"企微消息已处理: {msg_id}")
            return None

        # 分析消息
        analysis = self.analyze_message(message)

        # 只处理 BUG 和需求
        if analysis["type"] == "unknown":
            logger.debug(f"企微消息未匹配关键词: {msg_id}")
            return None

        # 记录已处理
        self.processed_messages.add(msg_id)
        self._save_processed()

        # 创建工单
        result = self._create_ticket(message, analysis)

        if result.get("success"):
            logger.info(f"企微工单创建成功: {result['record_id']}")
            return result
        else:
            logger.error(f"企微工单创建失败: {result}")
            return None

    def _create_ticket(self, message: Dict, analysis: Dict) -> Dict:
        """
        创建飞书工单

        Args:
            message: 标准化消息
            analysis: 分析结果

        Returns:
            创建结果
        """
        content = message.get("content", "")
        sender_name = message.get("sender", {}).get("name", "未知用户")
        create_time = message.get("create_time", "")
        platform = message.get("platform", self.PLATFORM_NAME)

        # 构建工单数据（来源平台写入补充信息）
        ticket_data = {
            "标题": f"[{platform}] {content[:50]}",
            "类型": "缺陷" if analysis["type"] == "bug" else "需求",
            "环境": "待确认",
            "状态": "待处理",
            "补充信息": f"""
原始消息: {content[:200]}
来源平台: {platform}
发送者: {sender_name}
发现关键词: {', '.join(analysis['keywords'])}
置信度: {analysis['confidence']:.1%}
发现时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
消息 ID: {message['message_id']}
"""
        }

        # 企微消息的上下文（如果有）
        if message.get("raw", {}).get("context"):
            context_markdown = self._format_wecom_context(message["raw"]["context"])
            ticket_data["场景还原"] = context_markdown

        # 创建记录
        result = self.lark_cli.create_record(
            table_id=self.lark_cli.bug_table_id,
            fields=ticket_data
        )

        return result

    def _format_wecom_context(self, context: list) -> str:
        """
        格式化企微上下文为 Markdown

        Args:
            context: 上下文消息列表

        Returns:
            Markdown 格式
        """
        if not context:
            return ""

        lines = []
        for msg in context:
            sender = msg.get("sender", {}).get("name", "匿名")
            content = msg.get("content", "")
            time = msg.get("time", "")

            lines.append(f"- **{sender}** ({time})")
            lines.append(f"  {content}")
            lines.append("")

        return "\n".join(lines)

    def send_message(self, content: str) -> bool:
        """
        发送企微消息（通过 Webhook）

        Args:
            content: 消息内容

        Returns:
            是否成功
        """
        if not self.webhook_url:
            logger.warning("企微 Webhook URL 未配置")
            return False

        try:
            import httpx

            data = {
                "msgtype": "text",
                "text": {"content": content}
            }

            with httpx.Client() as client:
                response = client.post(self.webhook_url, json=data, timeout=10.0)
                response.raise_for_status()

            logger.info(f"企微消息发送成功")
            return True

        except Exception as e:
            logger.error(f"企微消息发送失败: {e}")
            return False


def main():
    """测试企微桥接"""
    import argparse

    parser = argparse.ArgumentParser(description="企微消息桥接")
    parser.add_argument("--test", action="store_true", help="测试消息处理")
    parser.add_argument("--config", default="config/config.yaml", help="配置文件路径")

    args = parser.parse_args()

    from dotenv import load_dotenv
    load_dotenv()

    bridge = WeComBridge(args.config)

    if args.test:
        # 测试消息
        test_msg = {
            "MsgId": "test_wecom_001",
            "FromUserName": {"UserId": "user001", "Name": "测试用户"},
            "Content": "Apifox 打开就报错了，提示连接失败",
            "CreateTime": int(datetime.now().timestamp())
        }

        print("\n=== 测试企微消息处理 ===")
        print(f"原始消息: {test_msg}")

        normalized = bridge.normalize_message(test_msg)
        print(f"\n标准化后: {json.dumps(normalized, indent=2, ensure_ascii=False)}")

        analysis = bridge.analyze_message(normalized)
        print(f"\n分析结果: {json.dumps(analysis, indent=2, ensure_ascii=False)}")

        result = bridge.process_message(test_msg)
        print(f"\n处理结果: {json.dumps(result, indent=2, ensure_ascii=False) if result else '未创建工单'}")


if __name__ == "__main__":
    main()