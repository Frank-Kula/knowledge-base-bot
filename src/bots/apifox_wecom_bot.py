"""
Apifox 定制版企微机器人处理器 (基于特定收发消息API)
"""

import asyncio
import time
from typing import Dict, Optional
from loguru import logger
import httpx


class ApifoxWeComBot:
    """Apifox 定制版企微机器人"""

    def __init__(self, config, kb, classifier, template_mgr):
        self.config = config
        self.kb = kb
        self.classifier = classifier
        self.template_mgr = template_mgr
        
        self.wecom_config = config.bots.get("apifox_wecom", {})
        self.access_key = self.wecom_config.get("access_key")
        self.access_secret = self.wecom_config.get("access_secret")
        self.api_base_url = self.wecom_config.get("api_base_url", "").rstrip("/")
        
        # Token 缓存管理
        self._access_token: Optional[str] = None
        self._token_expire_time: float = 0
        
        # 对话管理器
        from bots.conversation_manager import ConversationManager
        self.conversation_mgr = ConversationManager(config)

    async def _get_access_token(self) -> str:
        """获取并缓存 Access Token"""
        current_time = time.time()
        # 预留 5 分钟 (300秒) 的提前刷新窗口
        if self._access_token and current_time < (self._token_expire_time - 300):
            return self._access_token
            
        logger.info("正在请求新的企微 Access Token...")
        try:
            auth_url = f"{self.api_base_url}/robotapi/client/auth"
            data = {
                "accessKey": self.access_key,
                "accessSecret": self.access_secret
            }
            
            async with httpx.AsyncClient() as client:
                response = await client.post(auth_url, json=data, timeout=10.0)
                response.raise_for_status()
                result = response.json()
                
                # 假设返回结构 {"token": "xxx", "expireMinutes": 1440}
                self._access_token = result.get("token")
                expire_minutes = result.get("expireMinutes", 1440)
                self._token_expire_time = current_time + (expire_minutes * 60)
                
                logger.info(f"成功获取企微 Token，有效期至 {time.ctime(self._token_expire_time)}")
                return self._access_token
                
        except Exception as e:
            logger.error(f"获取企微 Access Token 失败: {e}")
            raise Exception("Auth Failed")

    async def handle_message(self, message_data: Dict):
        """
        处理企微推送的消息 (Webhook JSON Payload)
        """
        try:
            # 解析特定 API 协议的消息格式
            chat_user = message_data.get("chatUser", "")
            robot_key = message_data.get("robotKey", "")
            content = message_data.get("content", "")
            sender_name = message_data.get("senderName", "未知用户")
            is_group_chat = message_data.get("isGroupChat", 0)

            logger.info(f"[定制版企微] 收到消息 - 发件人: {sender_name}, 群组: {is_group_chat}, 内容: {content}")

            # 上下文信息，需要传给发送端
            context_meta = {
                "chatUser": chat_user,
                "robotKey": robot_key
            }

            # 检查是否是命令
            if content.startswith("/"):
                await self._handle_command(chat_user, sender_name, content, context_meta)
                return

            # 使用 chatUser 作为会话标识
            if self.conversation_mgr.is_conversation_active(chat_user):
                await self._handle_conversation(chat_user, sender_name, content, context_meta)
            else:
                await self._handle_new_question(chat_user, sender_name, content, context_meta)

        except Exception as e:
            logger.error(f"[定制版企微] 处理消息失败: {e}")

    async def _handle_new_question(self, user_id: str, user_name: str, question: str, context_meta: Dict):
        try:
            await self.send_message(
                f"收到您的问题：{question}\n\n让我先收集一些信息，以便更好地帮助您。",
                context_meta
            )
            first_q = self.conversation_mgr.start_conversation(user_id)
            await self.send_message(first_q["message"], context_meta)
        except Exception as e:
            logger.error(f"处理新问题失败: {e}")

    async def _handle_conversation(self, user_id: str, user_name: str, response: str, context_meta: Dict):
        try:
            result = self.conversation_mgr.process_response(user_id, response)
            if result["status"] == "collecting":
                await self.send_message(result["message"], context_meta)
            elif result["status"] == "completed":
                await self._analyze_and_classify(user_id, user_name, result["collected_data"], context_meta)
        except Exception as e:
            logger.error(f"处理对话失败: {e}")

    async def _analyze_and_classify(self, user_id: str, user_name: str, collected_data: Dict, context_meta: Dict):
        try:
            await self.send_message("感谢您的信息！我正在分析您的问题...", context_meta)

            question = collected_data.get("description", "")
            context = await self.kb.search_with_context(question)
            
            classification = await self.classifier.classify(
                question=question,
                context=context,
                additional_info=collected_data
            )
            
            logger.info(f"分类结果: {classification}")

            ticket_type = classification["type"]
            template_content = self.template_mgr.render_template(
                ticket_type,
                title=question[:50],
                submitter=user_name,
                confidence=int(classification["confidence"] * 100),
                reason=classification["reason"],
                suggested_answer=classification["suggested_answer"],
                **collected_data
            )

            await self.send_message(
                f"分析完成！\n\n"
                f"问题类型：{self._translate_type(ticket_type)}\n"
                f"置信度：{int(classification['confidence'] * 100)}%\n"
                f"判断理由：{classification['reason']}\n\n"
                f"正在生成工单模板...",
                context_meta
            )
            
            await self.send_message(f"```\n{template_content}\n```", context_meta)

            # 创建飞书工单并通知
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
                    f"工单已创建！\n查看链接：{result['url']}\n\n我们将尽快处理，感谢您的反馈！",
                    context_meta
                )
            else:
                await self.send_message(
                    f"工单创建失败：{result.get('error', '未知错误')}\n请联系管理员处理。",
                    context_meta
                )

            self.conversation_mgr.cancel_conversation(user_id)

        except Exception as e:
            logger.error(f"分析分类失败: {e}")
            await self.send_message(f"处理过程中出现错误：{str(e)}", context_meta)

    async def _handle_command(self, user_id: str, user_name: str, command: str, context_meta: Dict):
        if command == "/cancel":
            self.conversation_mgr.cancel_conversation(user_id)
            await self.send_message("已取消当前对话", context_meta)
        elif command == "/help":
            help_text = "使用帮助：\n1. 直接发送问题，我会引导您收集信息\n2. /cancel - 取消当前对话\n3. /help - 显示帮助"
            await self.send_message(help_text, context_meta)
        else:
            await self.send_message(f"未知命令：{command}", context_meta)

    def _translate_type(self, ticket_type: str) -> str:
        type_map = {
            "bug": "缺陷/Bug",
            "feature": "功能需求",
            "usage": "使用问题",
            "unknown": "未知类型"
        }
        return type_map.get(ticket_type, "其他")

    async def send_message(self, content: str, context_meta: Dict = None):
        """
        调用定制版 API 发送消息
        """
        if not context_meta or "chatUser" not in context_meta or "robotKey" not in context_meta:
            logger.error("[定制版企微] 发送消息失败：缺少 context_meta (chatUser/robotKey)")
            return

        try:
            token = await self._get_access_token()
            send_url = f"{self.api_base_url}/wxworkapi/message/exchange"
            
            headers = {
                "token": token
            }
            
            # 构造新的发送 Payload
            import uuid
            data = {
                "type": "robot.msg.send",
                "messageId": str(uuid.uuid4()).replace("-", ""),
                "content": content,
                "friends": [context_meta["chatUser"]],
                "robotKey": context_meta["robotKey"]
            }

            async with httpx.AsyncClient() as client:
                response = await client.post(
                    send_url,
                    json=data,
                    headers=headers,
                    timeout=10.0
                )
                response.raise_for_status()

            logger.info(f"[定制版企微] 发送消息成功: {content[:50]}...")

        except Exception as e:
            logger.error(f"[定制版企微] 发送消息失败: {e}")
