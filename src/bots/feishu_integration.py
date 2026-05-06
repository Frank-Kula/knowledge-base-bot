"""
飞书集成模块
创建工单、发送消息到飞书
使用 lark-cli 封装实现
"""

from typing import Dict
from loguru import logger

from src.integrations.lark_cli_wrapper import LarkCliWrapper


class FeishuIntegration:
    """飞书集成"""

    def __init__(self, config):
        self.config = config
        self.lark_cli = LarkCliWrapper(config)
        logger.info("飞书集成已初始化（lark-cli 模式）")

    async def create_ticket(
        self,
        ticket_type: str,
        title: str,
        data: Dict
    ) -> Dict:
        """
        创建飞书工单

        Args:
            ticket_type: 工单类型 (bug/feature/usage)
            title: 标题
            data: 工单数据

        Returns:
            创建结果
        """
        try:
            if ticket_type == "bug":
                fields = self._build_bug_fields(title, data)
                table_id = self.lark_cli.bug_table_id
            elif ticket_type == "feature":
                fields = self._build_feature_fields(title, data)
                table_id = self.lark_cli.feature_table_id
            else:
                fields = self._build_usage_fields(title, data)
                table_id = self.lark_cli.bug_table_id

            result = self.lark_cli.create_record(table_id, fields)

            if result.get("success"):
                logger.info(f"飞书工单创建成功: {result.get('record_id')}")
            else:
                logger.error(f"飞书工单创建失败: {result}")

            return result

        except Exception as e:
            logger.error(f"创建飞书工单异常: {e}")
            return {"success": False, "error": str(e)}

    def _build_bug_fields(self, title: str, data: Dict) -> Dict:
        """构建 Bug 表字段"""
        field_mappings = self.config.feishu_ticket.bug_field_mappings

        fields = {}
        fields[field_mappings["title"]] = title
        fields[field_mappings["type"]] = "缺陷"

        # 解析环境+版本
        env_version = data.get("environment_version", "")
        if env_version:
            parts = env_version.replace("，", ",").replace("：", ":").split(",")
            if len(parts) >= 2:
                fields[field_mappings["environment"]] = parts[0].strip()
                fields[field_mappings["version"]] = parts[1].strip()
            else:
                fields[field_mappings["environment"]] = env_version

        # 复现步骤
        fields[field_mappings["steps"]] = data.get("steps", "")

        # 解析现状及预期
        status_expected = data.get("status_expected", "")
        if status_expected:
            parts = status_expected.replace("现状：", "现状:").replace("预期：", "预期:").split("预期:")
            if len(parts) >= 2:
                fields[field_mappings["actual"]] = parts[0].replace("现状:", "").strip()
                fields[field_mappings["expected"]] = parts[1].strip()
            else:
                fields[field_mappings["actual"]] = status_expected

        # 提交人（如果有有效的飞书 open_id）
        submitter_open_id = data.get("submitter_open_id", "")
        if submitter_open_id and "submitter" in field_mappings:
            fields[field_mappings["submitter"]] = [{"id": submitter_open_id}]

        return fields

    def _build_feature_fields(self, title: str, data: Dict) -> Dict:
        """构建需求表字段"""
        field_mappings = self.config.feishu_ticket.feature_field_mappings

        fields = {}
        fields[field_mappings["title"]] = title
        fields[field_mappings["type"]] = "需求"

        # 提交人（如果有有效的飞书 open_id）
        submitter_open_id = data.get("submitter_open_id", "")
        if submitter_open_id and "submitter" in field_mappings:
            fields[field_mappings["submitter"]] = [{"id": submitter_open_id}]

        return fields

    def _build_usage_fields(self, title: str, data: Dict) -> Dict:
        """构建使用问题字段"""
        field_mappings = self.config.feishu_ticket.bug_field_mappings

        fields = {}
        fields[field_mappings["title"]] = title
        fields[field_mappings["type"]] = "使用咨询"

        # 提交人（如果有有效的飞书 open_id）
        submitter_open_id = data.get("submitter_open_id", "")
        if submitter_open_id and "submitter" in field_mappings:
            fields[field_mappings["submitter"]] = [{"id": submitter_open_id}]

        return fields

    async def send_message(self, receive_id: str, content: str, receive_id_type: str = "chat_id") -> bool:
        """
        发送飞书消息

        Args:
            receive_id: 接收者ID（群ID或用户ID）
            content: 消息内容
            receive_id_type: ID类型 (chat_id/open_id/user_id)

        Returns:
            是否成功
        """
        result = self.lark_cli.send_message(receive_id, content, receive_id_type)
        return result.get("success", False)