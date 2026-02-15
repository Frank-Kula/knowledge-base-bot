"""
飞书集成模块
创建工单、发送到多维表格
"""

from typing import Dict, List
from loguru import logger
from lark_oapi.api.bitable.v1 import *
from lark_oapi import JSON


class FeishuIntegration:
    """飞书集成"""

    def __init__(self, config):
        self.config = config
        self.base_url = config.feishu_ticket.base_url
        self.app_id = config.bots.feishu.app_id
        self.app_secret = config.bots.feishu.app_secret
        self.spreadsheet_token = config.feishu_ticket.spreadsheet_token
        self.app_token = config.feishu_ticket.app_token
        self.table_id = config.feishu_ticket.table_id

        # 获取 tenant_access_token
        self.tenant_access_token = None
        # self._refresh_tenant_token()

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
            # 映射字段
            field_mappings = self.config.feishu_ticket.field_mappings
            fields = {}

            # 基础字段
            fields[field_mappings["title"]] = title
            fields[field_mappings["type"]] = self._translate_type(ticket_type)
            fields[field_mappings["submitter"]] = data.get("submitter", "未知用户")

            # 环境信息
            if ticket_type == "bug":
                fields[field_mappings["version"]] = data.get("version", "")
                fields[field_mappings["environment"]] = data.get("environment", "")
                fields[field_mappings["description"]] = data.get("description", "")
                fields[field_mappings["steps"]] = data.get("steps", "")
                fields[field_mappings["expected"]] = data.get("expected", "")
                fields[field_mappings["actual"]] = data.get("actual", "")

            elif ticket_type == "feature":
                fields[field_mappings["description"]] = data.get("background", "")
                fields[field_mappings["expected"]] = data.get("expected", "")

            # 优先级
            priority = self._calculate_priority(ticket_type, data)
            fields[field_mappings["priority"]] = priority

            # 创建记录
            result = await self._create_record(fields)

            if result.success():
                record_id = result.data.record.record_id
                logger.info(f"飞书工单创建成功: {record_id}")

                # 发送通知
                await self._send_notification(ticket_type, title, data)

                return {
                    "success": True,
                    "record_id": record_id,
                    "url": f"https://feishu.cn/base/{self.app_token}/{self.table_id}?record={record_id}"
                }
            else:
                logger.error(f"飞书工单创建失败: {result.msg}")
                return {
                    "success": False,
                    "error": result.msg
                }

        except Exception as e:
            logger.error(f"创建飞书工单异常: {e}")
            return {
                "success": False,
                "error": str(e)
            }

    async def _create_record(self, fields: Dict) -> CreateAppTableRecordResponse:
        """创建记录"""
        # 这里需要使用飞书 SDK
        # 具体实现依赖飞书开放平台 API
        # 这是一个示例框架
        pass

    def _translate_type(self, ticket_type: str) -> str:
        """翻译工单类型"""
        type_map = {
            "bug": "缺陷",
            "feature": "需求",
            "usage": "使用咨询"
        }
        return type_map.get(ticket_type, "其他")

    def _calculate_priority(self, ticket_type: str, data: Dict) -> str:
        """
        计算优先级

        Args:
            ticket_type: 工单类型
            data: 工单数据

        Returns:
            优先级 (P0/P1/P2/P3)
        """
        # 简单的优先级计算逻辑
        if ticket_type == "bug":
            # Bug 根据影响范围判断
            description = data.get("description", "").lower()
            if any(keyword in description for keyword in ["崩溃", "数据丢失", "无法使用"]):
                return "P0"
            elif any(keyword in description for keyword in ["严重", "错误"]):
                return "P1"
            else:
                return "P2"

        elif ticket_type == "feature":
            # 需求默认 P2
            return "P2"

        else:
            # 使用问题默认 P3
            return "P3"

    async def _send_notification(
        self,
        ticket_type: str,
        title: str,
        data: Dict
    ):
        """
        发送飞书通知

        Args:
            ticket_type: 工单类型
            title: 标题
            data: 工单数据
        """
        try:
            if not self.config.feishu_ticket.notification.enabled:
                return

            # 构建通知消息
            message_template = self.config.feishu_ticket.notification.message_template
            message = message_template.format(
                type=self._translate_type(ticket_type),
                title=title,
                submitter=data.get("submitter", "未知用户"),
                priority=self._calculate_priority(ticket_type, data)
            )

            # @负责人
            mention_users = self.config.feishu_ticket.notification.mention_users
            if mention_users:
                mentions = " ".join([f"<at user_id=\"{uid}\"></at>" for uid in mention_users])
                message = f"{mentions}\n{message}"

            # 发送消息（需要飞书机器人）
            logger.info(f"发送飞书通知: {message}")

        except Exception as e:
            logger.error(f"发送通知失败: {e}")

    async def get_record(self, record_id: str) -> Dict:
        """
        获取工单记录

        Args:
            record_id: 记录ID

        Returns:
            记录数据
        """
        try:
            # 调用飞书 API
            pass
        except Exception as e:
            logger.error(f"获取记录失败: {e}")
            return {}

    async def update_record(self, record_id: str, fields: Dict) -> bool:
        """
        更新工单记录

        Args:
            record_id: 记录ID
            fields: 要更新的字段

        Returns:
            是否成功
        """
        try:
            # 调用飞书 API
            pass
            return True
        except Exception as e:
            logger.error(f"更新记录失败: {e}")
            return False
