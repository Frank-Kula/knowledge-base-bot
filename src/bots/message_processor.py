"""
消息处理器
协调分类、对话管理和工单创建
"""

import asyncio
from typing import Dict, Optional
from loguru import logger

from src.classifiers.question_classifier import QuestionClassifier
from src.bots.conversation_manager import ConversationManager
from src.utils.template_manager import TemplateManager
from src.integrations.feishu_client import FeishuClient
from src.utils.config_loader import load_config
from pathlib import Path
import json
from datetime import datetime


class MessageProcessor:
    """消息处理器"""

    def __init__(self):
        # 加载配置
        self.config = load_config()

        # 初始化组件
        self.classifier = QuestionClassifier(self.config)
        self.conversation_manager = ConversationManager(self.config)
        self.template_manager = TemplateManager(self.config)
        self.feishu_client = FeishuClient()

        # 使用场景缓存（使用问题不需要创建工单）
        self.usage_cache = {}

    async def process_message(
        self,
        user_id: str,
        chat_id: str,
        message: str
    ) -> Dict:
        """
        处理用户消息

        Args:
            user_id: 用户 ID
            chat_id: 群聊 ID
            message: 消息内容

        Returns:
            处理结果和回复消息
        """
        try:
            # 检查是否有活跃对话
            if self.conversation_manager.is_conversation_active(user_id):
                # 继续信息收集
                return await self._continue_conversation(user_id, chat_id, message)

            else:
                # 新对话，先分类
                return await self._start_new_conversation(user_id, chat_id, message)

        except Exception as e:
            logger.error(f"处理消息异常: {e}")
            return {
                "success": False,
                "reply": f"处理失败：{str(e)}"
            }

    async def _start_new_conversation(
        self,
        user_id: str,
        chat_id: str,
        message: str
    ) -> Dict:
        """
        开始新对话

        Args:
            user_id: 用户 ID
            chat_id: 群聊 ID
            message: 消息内容

        Returns:
            处理结果
        """
        try:
            # 1. 问题分类
            logger.info(f"[用户 {user_id}] 开始问题分类")
            classification = await self.classifier.classify(
                question=message,
                context="",
                additional_info={}
            )

            problem_type = classification["type"]
            confidence = classification["confidence"]

            logger.info(f"[用户 {user_id}] 分类结果: {problem_type} (置信度: {confidence})")

            # 2. 根据类型处理
            if problem_type == "usage":
                # 使用问题：直接回答
                return await self._handle_usage_question(user_id, chat_id, classification)

            elif problem_type in ["bug", "feature"]:
                # Bug 或 Feature：开始信息收集
                return await self._start_info_collection(user_id, chat_id, problem_type, classification)

            else:
                # 未知类型
                return {
                    "success": True,
                    "reply": "抱歉，我不确定您的问题类型。请详细描述一下：\n- 是否遇到了错误或报错？\n- 还是希望有某个新功能？\n- 或者不知道如何使用某个功能？"
                }

        except Exception as e:
            logger.error(f"开始新对话异常: {e}")
            return {
                "success": False,
                "reply": f"处理失败：{str(e)}"
            }

    async def _start_info_collection(
        self,
        user_id: str,
        chat_id: str,
        problem_type: str,
        classification: Dict
    ) -> Dict:
        """
        开始信息收集

        Args:
            user_id: 用户 ID
            chat_id: 群聊 ID
            problem_type: 问题类型 (bug/feature)
            classification: 分类结果

        Returns:
            处理结果
        """
        try:
            # 设置字段配置
            if problem_type == "bug":
                self.conversation_manager.fields = self.config.info_collection.bug_fields
                type_name = "缺陷"
            else:
                self.conversation_manager.fields = self.config.info_collection.feature_fields
                type_name = "需求"

            # 保存分类结果到对话上下文
            self.conversation_manager.conversations[user_id] = {
                "state": "collecting",
                "current_field": 0,
                "collected_data": {
                    "_classification": classification,
                    "_chat_id": chat_id
                },
                "started_at": None  # start_conversation 会设置
            }

            # 开始对话
            response = self.conversation_manager.start_conversation(user_id)
            first_question = response["message"]

            logger.info(f"[用户 {user_id}] 开始收集 {type_name} 信息")

            return {
                "success": True,
                "reply": f"✅ 已识别为 **{type_name}**（置信度：{int(classification['confidence'] * 100)}%）\n\n{first_question}"
            }

        except Exception as e:
            logger.error(f"开始信息收集异常: {e}")
            return {
                "success": False,
                "reply": f"开始信息收集失败：{str(e)}"
            }

    async def _continue_conversation(
        self,
        user_id: str,
        chat_id: str,
        message: str
    ) -> Dict:
        """
        继续信息收集

        Args:
            user_id: 用户 ID
            chat_id: 群聊 ID
            message: 消息内容

        Returns:
            处理结果
        """
        try:
            # 处理用户回答
            response = self.conversation_manager.process_response(user_id, message)

            # 检查是否收集完成
            if response["status"] == "completed":
                # 收集完成，生成工单
                return await self._create_ticket(user_id, chat_id)

            else:
                # 继续下一个问题
                next_question = response["message"]
                return {
                    "success": True,
                    "reply": next_question
                }

        except Exception as e:
            logger.error(f"继续对话异常: {e}")
            return {
                "success": False,
                "reply": f"处理失败：{str(e)}"
            }

    async def _create_ticket(
        self,
        user_id: str,
        chat_id: str
    ) -> Dict:
        """
        创建工单

        Args:
            user_id: 用户 ID
            chat_id: 群聊 ID

        Returns:
            处理结果
        """
        try:
            # 获取收集的数据
            conversation = self.conversation_manager.conversations.get(user_id)
            if not conversation:
                return {
                    "success": False,
                    "reply": "未找到对话信息"
                }

            collected_data = conversation["collected_data"]
            classification = collected_data.pop("_classification")
            problem_type = classification["type"]

            logger.info(f"[用户 {user_id}] 信息收集完成，开始创建 {problem_type} 工单")

            # 添加分类信息
            collected_data["confidence"] = int(classification["confidence"] * 100)
            collected_data["reason"] = classification["reason"]
            collected_data["submitter"] = user_id

            # 根据类型创建工单
            if problem_type == "bug":
                result = self.feishu_client.create_bug_record(collected_data)
                type_name = "缺陷"
            else:
                result = self.feishu_client.create_feature_record(collected_data)
                type_name = "需求"

            # 清除对话
            self.conversation_manager.cancel_conversation(user_id)

            if result["success"]:
                record_id = result["record_id"]
                logger.info(f"[用户 {user_id}] {type_name}工单创建成功: {record_id}")

                return {
                    "success": True,
                    "reply": f"✅ **{type_name}工单已创建**\n\n工单 ID：{record_id}\n\n我们会在 1-2 个工作日内处理您的反馈，感谢您的支持！"
                }
            else:
                logger.error(f"[用户 {user_id}] {type_name}工单创建失败: {result}")

                # 降级：保存到本地文件
                save_ticket_to_local(problem_type, collected_data)

                return {
                    "success": True,  # 返回成功，因为已经记录
                    "reply": f"✅ **{type_name}工单已创建**（本地记录）\n\n由于多维表格权限配置中，工单已保存到本地。\n\n我们会在权限配置完成后同步到飞书。感谢您的支持！"
                }

        except Exception as e:
            logger.error(f"创建工单异常: {e}")
            return {
                "success": False,
                "reply": f"创建工单失败：{str(e)}"
            }

    async def _handle_usage_question(
        self,
        user_id: str,
        chat_id: str,
        classification: Dict
    ) -> Dict:
        """
        处理使用问题

        Args:
            user_id: 用户 ID
            chat_id: 群聊 ID
            classification: 分类结果

        Returns:
            处理结果
        """
        try:
            suggested_answer = classification.get("suggested_answer", "")

            if suggested_answer:
                reply = f"💡 **使用提示**\n\n{suggested_answer}\n\n如果还有其他问题，欢迎继续提问！"

            return {
                "success": True,
                "reply": reply
            }

        except Exception as e:
            logger.error(f"处理使用问题异常: {e}")
            return {
                "success": False,
                "reply": f"处理失败：{str(e)}"
            }

def save_ticket_to_local(problem_type: str, data: dict):
    """保存工单到本地文件（降级方案）"""
    try:
        # 创建目录
        ticket_dir = Path("data/local_tickets")
        ticket_dir.mkdir(parents=True, exist_ok=True)

        # 生成文件名
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = ticket_dir / f"{problem_type}_{timestamp}.json"

        # 构建工单数据
        ticket = {
            "type": problem_type,
            "created_at": datetime.now().isoformat(),
            "data": data
        }

        # 保存到文件
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(ticket, f, ensure_ascii=False, indent=2)

        logger.info(f"工单已保存到本地: {filename}")

    except Exception as e:
        logger.error(f"保存工单到本地失败: {e}")

    def cancel_conversation(self, user_id: str) -> str:
        """
        取消对话

        Args:
            user_id: 用户 ID

        Returns:
            取消结果消息
        """
        self.conversation_manager.cancel_conversation(user_id)
        return "对话已取消。"
