"""
对话管理器
处理信息收集流程
"""

from typing import Dict, List, Optional
from loguru import logger
from datetime import datetime, timedelta


class ConversationManager:
    """对话管理器"""

    def __init__(self, config):
        self.config = config
        # 存储用户对话状态
        # 格式：{user_id: {"state": "collecting", "current_field": 0, "collected_data": {}, "started_at": timestamp}}
        self.conversations: Dict[str, Dict] = {}
        # 信息收集字段配置
        self.fields = config.info_collection.required_fields

    def start_conversation(self, user_id: str) -> Dict:
        """
        开始新的对话

        Args:
            user_id: 用户ID

        Returns:
            初始问题
        """
        self.conversations[user_id] = {
            "state": "collecting",
            "current_field": 0,
            "collected_data": {},
            "started_at": datetime.now()
        }

        first_question = self.fields[0]
        return {
            "message": first_question["question"],
            "field_name": first_question["name"],
            "required": first_question["required"]
        }

    def process_response(
        self,
        user_id: str,
        response: str
    ) -> Dict:
        """
        处理用户回答

        Args:
            user_id: 用户ID
            response: 用户回答

        Returns:
            下一个问题或完成状态
        """
        if user_id not in self.conversations:
            # 新对话
            return self.start_conversation(user_id)

        conversation = self.conversations[user_id]

        # 检查是否超时（30分钟）
        if datetime.now() - conversation["started_at"] > timedelta(minutes=30):
            # 超时，重新开始
            logger.info(f"用户 {user_id} 对话超时，重新开始")
            return self.start_conversation(user_id)

        # 保存回答
        current_field_idx = conversation["current_field"]
        current_field = self.fields[current_field_idx]
        conversation["collected_data"][current_field["name"]] = response

        # 检查是否还有下一个问题
        next_field_idx = current_field_idx + 1
        if next_field_idx < len(self.fields):
            # 有下一个问题
            conversation["current_field"] = next_field_idx
            next_field = self.fields[next_field_idx]
            return {
                "status": "collecting",
                "message": next_field["question"],
                "field_name": next_field["name"],
                "required": next_field["required"]
            }
        else:
            # 收集完成
            conversation["state"] = "completed"
            return {
                "status": "completed",
                "collected_data": conversation["collected_data"]
            }

    def get_collected_data(self, user_id: str) -> Optional[Dict]:
        """
        获取已收集的数据

        Args:
            user_id: 用户ID

        Returns:
            已收集的数据，如果对话不存在返回 None
        """
        conversation = self.conversations.get(user_id)
        if conversation:
            return conversation.get("collected_data")
        return None

    def is_conversation_active(self, user_id: str) -> bool:
        """
        检查对话是否活跃

        Args:
            user_id: 用户ID

        Returns:
            是否活跃
        """
        conversation = self.conversations.get(user_id)
        if not conversation:
            return False

        # 检查是否超时
        if datetime.now() - conversation["started_at"] > timedelta(minutes=30):
            # 清理过期对话
            del self.conversations[user_id]
            return False

        return conversation["state"] == "collecting"

    def cancel_conversation(self, user_id: str):
        """
        取消对话

        Args:
            user_id: 用户ID
        """
        if user_id in self.conversations:
            del self.conversations[user_id]
            logger.info(f"用户 {user_id} 对话已取消")

    def cleanup_expired_conversations(self):
        """清理过期对话"""
        expired_users = []
        for user_id, conversation in self.conversations.items():
            if datetime.now() - conversation["started_at"] > timedelta(minutes=30):
                expired_users.append(user_id)

        for user_id in expired_users:
            del self.conversations[user_id]
            logger.info(f"清理过期对话: {user_id}")

    def get_conversation_summary(self, user_id: str) -> str:
        """
        获取对话摘要

        Args:
            user_id: 用户ID

        Returns:
            对话摘要文本
        """
        data = self.get_collected_data(user_id)
        if not data:
            return "暂无收集信息"

        summary_parts = []
        for key, value in data.items():
            # 将字段名转换为可读格式
            field_name_map = {
                "version": "版本",
                "environment": "环境",
                "specific_case": "特定情况",
                "error_details": "错误详情"
            }
            readable_name = field_name_map.get(key, key)
            summary_parts.append(f"- {readable_name}: {value}")

        return "\n".join(summary_parts)
