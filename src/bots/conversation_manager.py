"""
对话管理器
处理信息收集流程
"""

from typing import Dict, List, Optional
from loguru import logger
from datetime import datetime, timedelta
from dataclasses import dataclass


@dataclass
class FieldQuestion:
    """字段问题"""
    name: str
    question: str
    required: bool = True
    example: str = ""
    hint: str = ""


class ConversationManager:
    """对话管理器"""

    def __init__(self, config):
        self.config = config
        # 存储用户对话状态
        # 格式：{user_id: {"state": "collecting", "current_field": 0, "collected_data": {}, "started_at": timestamp, "initial_question": ""}}
        self.conversations: Dict[str, Dict] = {}

        # 加载信息收集字段配置
        self.bug_fields = self._load_fields(config.info_collection.bug_fields)
        self.feature_fields = self._load_fields(config.info_collection.feature_fields)

        # 默认使用 bug 字段
        self.fields = self.bug_fields

        logger.info(f"已加载 {len(self.bug_fields)} 个 Bug 收集字段, {len(self.feature_fields)} 个需求收集字段")

    def _load_fields(self, field_configs: List) -> List:
        """加载字段配置"""
        fields = []
        for f in field_configs:
            fields.append(FieldQuestion(
                name=f.name,
                question=f.question,
                required=f.required,
                example=f.example if hasattr(f, 'example') else "",
                hint=f.hint if hasattr(f, 'hint') else ""
            ))
        return fields

    def start_conversation(self, user_id: str, initial_question: str = "") -> Dict:
        """
        开始新的对话

        Args:
            user_id: 用户ID
            initial_question: 用户初始问题（用于提取标题）

        Returns:
            初始问题
        """
        self.conversations[user_id] = {
            "state": "collecting",
            "collected_data": {
                "title": initial_question[:100] if initial_question else "未提供标题"
            },
            "history": [{"role": "user", "content": initial_question}] if initial_question else [],
            "started_at": datetime.now(),
            "initial_question": initial_question,
            "progress_message_id": None
        }

        # 返回第一个问题（用于兼容）
        first_question = self.fields[0]
        return {
            "message": first_question.question,
            "field_name": first_question.name,
            "required": first_question.required
        }

    def add_to_history(self, user_id: str, role: str, content: str):
        """记录对话历史"""
        if user_id in self.conversations:
            self.conversations[user_id]["history"].append({"role": role, "content": content})

    def update_extracted_data(self, user_id: str, extracted_data: Dict):
        """合并 LLM 提取到的数据"""
        if user_id in self.conversations:
            # 只有当提取到的信息不是 "未提及" 时才覆盖现有数据
            for key, value in extracted_data.items():
                if value and value != "未提及":
                    self.conversations[user_id]["collected_data"][key] = value

    def set_confirming(self, user_id: str):
        """进入确认阶段"""
        if user_id in self.conversations:
            self.conversations[user_id]["state"] = "confirming"

    def get_progress_message_id(self, user_id: str) -> Optional[str]:
        """获取进度卡片的消息 ID"""
        return self.conversations.get(user_id, {}).get("progress_message_id")

    def set_progress_message_id(self, user_id: str, message_id: str):
        """记录进度卡片的消息 ID"""
        if user_id in self.conversations:
            self.conversations[user_id]["progress_message_id"] = message_id


    def get_all_questions(self) -> str:
        """
        获取所有问题的一次性展示文本

        Returns:
            所有问题拼接成的文本
        """
        questions = []
        for i, field in enumerate(self.fields, 1):
            question_text = field.question
            questions.append(question_text)
        return "\n\n".join(questions)

    def process_response(
        self,
        user_id: str,
        response: str
    ) -> Dict:
        """
        处理用户回答（无序批量模式，不再按顺序逐字段处理）

        Args:
            user_id: 用户ID
            response: 用户回答

        Returns:
            当前状态信息
        """
        if user_id not in self.conversations:
            return self.start_conversation(user_id, response)

        conversation = self.conversations[user_id]

        # 检查是否超时（30分钟）
        if datetime.now() - conversation["started_at"] > timedelta(minutes=30):
            logger.info(f"用户 {user_id} 对话超时，重新开始")
            return self.start_conversation(user_id, conversation.get("initial_question", ""))

        # 记录用户回复到历史（用于后续LLM提取）
        conversation["history"].append({"role": "user", "content": response})

        # 返回当前状态（实际数据提取由 feishu_bot 调用 classifier.extract_info 完成）
        return {
            "status": "collecting",
            "collected_data": conversation["collected_data"]
        }

    def _parse_response(self, response: str) -> List[str]:
        """
        解析用户回复，提取各个答案

        支持格式：
        1. 数字编号：1. xxx 2. xxx 3. xxx
        2. 换行分隔：每行一个答案

        Args:
            response: 用户回复文本

        Returns:
            答案列表
        """
        import re

        # 尝试匹配数字编号格式
        numbered_pattern = r'[1-9][\.、．]\s*(.+?)(?=(?:[1-9][\.、．])|$)'
        numbered_matches = re.findall(numbered_pattern, response, re.DOTALL)

        if numbered_matches:
            return [m.strip() for m in numbered_matches]

        # 尝试按换行分割
        lines = [line.strip() for line in response.split('\n') if line.strip()]

        # 过滤掉纯数字行
        lines = [line for line in lines if not line.isdigit()]

        return lines

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
