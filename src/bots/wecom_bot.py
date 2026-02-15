"""
企微机器人处理器
"""

import asyncio
import json
from typing import Dict
from loguru import logger
import httpx


class WeComBot:
    """企微机器人"""

    def __init__(self, config, kb, classifier, template_mgr):
        self.config = config
        self.kb = kb
        self.classifier = classifier
        self.template_mgr = template_mgr
        self.webhook_url = config.bots.wecom.webhook_url
        # 对话管理器
        from bots.conversation_manager import ConversationManager
        self.conversation_mgr = ConversationManager(config)

    async def handle_message(self, message_data: Dict):
        """
        处理企微消息

        Args:
            message_data: 消息数据
        """
        try:
            # 解析消息
            user_id = message_data.get("FromUserName", {})
            user_name = user_id.get("name", "未知用户")
            content = message_data.get("Content", "")

            logger.info(f"收到企微消息 - 用户: {user_name}, 内容: {content}")

            # 检查是否是命令
            if content.startswith("/"):
                await self._handle_command(user_id, user_name, content)
                return

            # 检查是否有活跃的对话
            if self.conversation_mgr.is_conversation_active(user_id):
                await self._handle_conversation(user_id, user_name, content)
            else:
                # 新问题，开始处理
                await self._handle_new_question(user_id, user_name, content)

        except Exception as e:
            logger.error(f"处理企微消息失败: {e}")

    async def _handle_new_question(
        self,
        user_id: str,
        user_name: str,
        question: str
    ):
        """
        处理新问题

        Args:
            user_id: 用户ID
            user_name: 用户名称
            question: 问题内容
        """
        try:
            # 发送确认消息
            await self.send_message(
                f"收到您的问题：{question}\n\n让我先收集一些信息，以便更好地帮助您。"
            )

            # 启动信息收集流程
            first_q = self.conversation_mgr.start_conversation(user_id)
            await self.send_message(first_q["message"])

        except Exception as e:
            logger.error(f"处理新问题失败: {e}")

    async def _handle_conversation(
        self,
        user_id: str,
        user_name: str,
        response: str
    ):
        """
        处理对话中的回答

        Args:
            user_id: 用户ID
            user_name: 用户名称
            response: 用户回答
        """
        try:
            # 处理回答
            result = self.conversation_mgr.process_response(user_id, response)

            if result["status"] == "collecting":
                # 继续收集
                await self.send_message(result["message"])
            elif result["status"] == "completed":
                # 收集完成，开始分析
                await self._analyze_and_classify(
                    user_id,
                    user_name,
                    result["collected_data"]
                )

        except Exception as e:
            logger.error(f"处理对话失败: {e}")

    async def _analyze_and_classify(
        self,
        user_id: str,
        user_name: str,
        collected_data: Dict
    ):
        """
        分析并分类问题

        Args:
            user_id: 用户ID
            user_name: 用户名称
            collected_data: 收集的数据
        """
        try:
            await self.send_message("感谢您的信息！我正在分析您的问题...")

            # 获取用户原始问题（这里简化处理，实际应该保存）
            question = collected_data.get("description", "")

            # 检索知识库
            context = await self.kb.search_with_context(question)

            # 分类问题
            classification = await self.classifier.classify(
                question=question,
                context=context,
                additional_info=collected_data
            )

            logger.info(f"分类结果: {classification}")

            # 生成模板
            ticket_type = classification["type"]
            template_content = self.template_mgr.render_template(
                ticket_type,
                title=question[:50],  # 截取标题
                submitter=user_name,
                confidence=int(classification["confidence"] * 100),
                reason=classification["reason"],
                suggested_answer=classification["suggested_answer"],
                **collected_data
            )

            # 发送分类结果和模板
            await self.send_message(
                f"分析完成！\n\n"
                f"问题类型：{self._translate_type(ticket_type)}\n"
                f"置信度：{int(classification['confidence'] * 100)}%\n"
                f"判断理由：{classification['reason']}\n\n"
                f"正在生成工单模板..."
            )

            # 发送模板
            await self.send_message(f"```\n{template_content}\n```")

            # 创建飞书工单
            from bots.feishu_integration import FeishuIntegration
            feishu = FeishuIntegration(self.config)
            result = await feishu.create_ticket(
                ticket_type=ticket_type,
                title=question[:50],
                data={
                    "submitter": user_name,
                    **collected_data
                }
            )

            if result["success"]:
                await self.send_message(
                    f"工单已创建！\n"
                    f"查看链接：{result['url']}\n\n"
                    f"我们将尽快处理，感谢您的反馈！"
                )
            else:
                await self.send_message(
                    f"工单创建失败：{result.get('error', '未知错误')}\n"
                    f"请联系管理员处理。"
                )

            # 清理对话
            self.conversation_mgr.cancel_conversation(user_id)

        except Exception as e:
            logger.error(f"分析分类失败: {e}")
            await self.send_message(f"处理过程中出现错误：{str(e)}")

    async def _handle_command(
        self,
        user_id: str,
        user_name: str,
        command: str
    ):
        """
        处理命令

        Args:
            user_id: 用户ID
            user_name: 用户名称
            command: 命令
        """
        if command == "/cancel":
            self.conversation_mgr.cancel_conversation(user_id)
            await self.send_message("已取消当前对话")

        elif command == "/help":
            help_text = """
使用帮助：
1. 直接发送问题，我会引导您收集信息
2. /cancel - 取消当前对话
3. /help - 显示帮助
            """
            await self.send_message(help_text)

        else:
            await self.send_message(f"未知命令：{command}")

    def _translate_type(self, ticket_type: str) -> str:
        """翻译工单类型"""
        type_map = {
            "bug": "缺陷/Bug",
            "feature": "功能需求",
            "usage": "使用问题",
            "unknown": "未知类型"
        }
        return type_map.get(ticket_type, "其他")

    async def send_message(self, content: str):
        """
        发送企微消息

        Args:
            content: 消息内容
        """
        try:
            # 发送文本消息
            data = {
                "msgtype": "text",
                "text": {
                    "content": content
                }
            }

            async with httpx.AsyncClient() as client:
                response = await client.post(
                    self.webhook_url,
                    json=data,
                    timeout=10.0
                )
                response.raise_for_status()

            logger.info(f"发送企微消息成功: {content[:50]}...")

        except Exception as e:
            logger.error(f"发送企微消息失败: {e}")
