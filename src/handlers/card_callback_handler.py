"""
飞书卡片回调处理模块
处理交互卡片按钮点击事件
"""

import json
from typing import Dict, Optional
from loguru import logger
from pathlib import Path

from src.integrations.lark_cli_wrapper import LarkCliWrapper


class CardCallbackHandler:
    """卡片回调处理器"""

    def __init__(self, config):
        self.config = config
        self.lark_cli = LarkCliWrapper(config)
        logger.info("卡片回调处理器已初始化")

    def handle_callback(self, callback_data: Dict) -> Dict:
        """
        处理卡片回调

        Args:
            callback_data: 回调数据，包含 action、record_id 等

        Returns:
            处理结果
        """
        action = callback_data.get("action")
        record_id = callback_data.get("record_id")
        table_id = callback_data.get("table_id")
        user_id = callback_data.get("user_id", "")  # 点击者的飞书 open_id

        logger.info(f"收到卡片回调: action={action}, record_id={record_id}")

        if action == "claim":
            return self._handle_claim(record_id, table_id, user_id)
        elif action == "convert_pm":
            return self._handle_convert_pm(record_id, table_id, user_id)
        else:
            logger.warning(f"未知操作: {action}")
            return {"success": False, "error": f"未知操作: {action}"}

    def _handle_claim(self, record_id: str, table_id: str, user_id: str) -> Dict:
        """
        处理「一键认领并跟进」操作

        Args:
            record_id: 记录 ID
            table_id: 表 ID
            user_id: 点击者 ID

        Returns:
            处理结果
        """
        try:
            # 更新多维表格记录：设置负责人
            fields = {}
            field_mappings = self.config.feishu_ticket.bug_field_mappings

            # 设置负责人字段（如果有）
            if "submitter" in field_mappings:
                # 使用字段映射中的负责人字段名（通常也叫"负责人"或"处理人"）
                owner_field = field_mappings.get("owner", "负责人")
                fields[owner_field] = [{"id": user_id}] if user_id else []

            # 更新状态为"处理中"
            if "状态" in field_mappings:
                fields["状态"] = "处理中"

            # 调用 lark-cli 更新记录
            result = self.lark_cli.update_record(
                table_id=table_id,
                record_id=record_id,
                fields=fields
            )

            if result.get("success"):
                logger.info(f"认领成功: record_id={record_id}, user={user_id}")
                return {
                    "success": True,
                    "message": f"已成功认领，记录已更新",
                    "record_id": record_id
                }
            else:
                logger.error(f"认领失败: {result.get('error')}")
                return {
                    "success": False,
                    "error": result.get("error", "更新失败")
                }

        except Exception as e:
            logger.error(f"认领处理异常: {e}")
            return {"success": False, "error": str(e)}

    def _handle_convert_pm(self, record_id: str, table_id: str, user_id: str) -> Dict:
        """
        处理「转为 PM 需求」操作

        Args:
            record_id: 记录 ID
            table_id: 表 ID（当前是 bug 表，需要转到需求表）
            user_id: 点击者 ID

        Returns:
            处理结果
        """
        try:
            # TODO: 实现 Bug 转需求的功能
            # 1. 从 Bug 表读取记录详情
            # 2. 在需求表创建新记录
            # 3. 更新 Bug 记录状态为"已转需求"

            logger.info(f"转需求处理: record_id={record_id}")

            # 暂时返回提示
            return {
                "success": True,
                "message": "需求已提交给产品团队",
                "todo": "需要实现完整转需求流程"
            }

        except Exception as e:
            logger.error(f"转需求处理异常: {e}")
            return {"success": False, "error": str(e)}

    def update_card_status(
        self,
        message_id: str,
        status: str,
        user_name: str = ""
    ) -> Dict:
        """
        更新卡片状态（认领后显示"已由 XXX 认领"）

        Args:
            message_id: 消息 ID
            status: 新状态
            user_name: 认领者名称

        Returns:
            更新结果
        """
        try:
            # 构建更新后的卡片内容
            # TODO: 使用 lark-cli 的消息更新接口

            logger.info(f"卡片状态更新: message_id={message_id}, status={status}")

            return {
                "success": True,
                "message": f"卡片已更新为 {status}",
                "todo": "需要实现消息卡片更新"
            }

        except Exception as e:
            logger.error(f"卡片状态更新异常: {e}")
            return {"success": False, "error": str(e)}


# FastAPI 路由示例（用于接收飞书回调）
def create_callback_routes(app, handler: CardCallbackHandler):
    """
    创建回调路由

    Args:
        app: FastAPI 应用
        handler: 卡片回调处理器
    """
    from fastapi import Request, Response

    @app.post("/feishu/card/callback")
    async def handle_card_callback(request: Request):
        """处理飞书卡片回调"""
        try:
            body = await request.body()
            data = json.loads(body)

            # 验证签名（TODO: 实现飞书签名验证）
            # ...

            # 解析回调数据
            challenge = data.get("challenge")
            if challenge:
                # 首次验证请求
                return Response(content=json.dumps({"challenge": challenge}))

            # 处理卡片事件
            event = data.get("event", {})
            action_value = event.get("action", {}).get("value", {})
            user_id = event.get("user", {}).get("open_id", "")

            # 添加用户 ID 到回调数据
            action_value["user_id"] = user_id

            # 处理回调
            result = handler.handle_callback(action_value)

            return Response(content=json.dumps(result))

        except Exception as e:
            logger.error(f"回调处理异常: {e}")
            return Response(
                content=json.dumps({"success": False, "error": str(e)}),
                status_code=500
            )