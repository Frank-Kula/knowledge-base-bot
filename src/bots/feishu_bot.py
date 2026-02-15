"""
飞书机器人处理器
"""

from typing import Dict
from loguru import logger
from lark_oapi.api.im.v1 import *


class FeishuBot:
    """飞书机器人"""

    def __init__(self, config, kb, classifier, template_mgr):
        self.config = config
        self.kb = kb
        self.classifier = classifier
        self.template_mgr = template_mgr
        self.app_id = config.bots.feishu.app_id
        # 对话管理器
        from bots.conversation_manager import ConversationManager
        self.conversation_mgr = ConversationManager(config)

    async def handle_message(self, event: Dict):
        """
        处理飞书消息

        Args:
            event: 消息事件
        """
        try:
            # 解析消息
            chat_id = event.get("chat_id", "")
            user_id = event.get("sender", {}).get("sender_id", {}).get("user_id", "")
            content = event.get("content", {})

            # 解析消息内容
            if isinstance(content, str):
                import json
                content = json.loads(content)

            message_type = content.get("message_type", "")
            text_content = content.get(text_type := "text", "")

            logger.info(f"收到飞书消息 - 用户: {user_id}, 内容: {text_content}")

            # 检查是否是命令
            if text_content.startswith("/"):
                await self._handle_command(chat_id, user_id, text_content)
                return

            # 检查是否有活跃的对话
            conversation_key = f"{chat_id}_{user_id}"
            if self.conversation_mgr.is_conversation_active(conversation_key):
                await self._handle_conversation(chat_id, user_id, text_content)
            else:
                # 新问题
                await self._handle_new_question(chat_id, user_id, text_content)

        except Exception as e:
            logger.error(f"处理飞书消息失败: {e}")

    async def _handle_new_question(
        self,
        chat_id: str,
        user_id: str,
        question: str
    ):
        """处理新问题"""
        try:
            conversation_key = f"{chat_id}_{user_id}"

            # 发送确认消息
            await self.send_message(
                chat_id,
                f"收到您的问题：{question}\n\n让我先收集一些信息，以便更好地帮助您。"
            )

            # 启动信息收集
            first_q = self.conversation_mgr.start_conversation(conversation_key)
            await self.send_message(chat_id, first_q["message"])

        except Exception as e:
            logger.error(f"处理新问题失败: {e}")

    async def _handle_conversation(
        self,
        chat_id: str,
        user_id: str,
        response: str
    ):
        """处理对话中的回答"""
        try:
            conversation_key = f"{chat_id}_{user_id}"
            result = self.conversation_mgr.process_response(conversation_key, response)

            if result["status"] == "collecting":
                await self.send_message(chat_id, result["message"])
            elif result["status"] == "completed":
                await self._analyze_and_classify(
                    chat_id,
                    user_id,
                    result["collected_data"]
                )

        except Exception as e:
            logger.error(f"处理对话失败: {e}")

    async def _analyze_and_classify(
        self,
        chat_id: str,
        user_id: str,
        collected_data: Dict
    ):
        """分析并分类问题"""
        # 类似企微机器人的实现
        # 这里省略具体实现，参考 wecom_bot.py
        pass

    async def _handle_command(
        self,
        chat_id: str,
        user_id: str,
        command: str
    ):
        """处理命令"""
        if command == "/cancel":
            conversation_key = f"{chat_id}_{user_id}"
            self.conversation_mgr.cancel_conversation(conversation_key)
            await self.send_message(chat_id, "已取消当前对话")

        elif command == "/help":
            help_text = """
使用帮助：
1. 直接发送问题，我会引导您收集信息
2. /cancel - 取消当前对话
3. /help - 显示帮助
            """
            await self.send_message(chat_id, help_text)

    async def send_message(self, chat_id: str, content: str):
        """
        发送飞书消息

        Args:
            chat_id: 群ID
            content: 消息内容
        """
        try:
            # 使用飞书 SDK 发送消息
            # 这里需要实现具体的发送逻辑
            logger.info(f"发送飞书消息到 {chat_id}: {content[:50]}...")

        except Exception as e:
            logger.error(f"发送飞书消息失败: {e}")
