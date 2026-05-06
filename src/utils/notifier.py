import httpx
from loguru import logger
from typing import Optional, Dict


class FeishuNotifier:
    """飞书群 Webhook 通知器"""

    def __init__(self, webhook_url: Optional[str] = None):
        """
        初始化
        Args:
            webhook_url: 飞书群自定义机器人的 Webhook URL
        """
        self.webhook_url = webhook_url

    async def send_text(self, text: str) -> bool:
        """发送纯文本消息"""
        if not self.webhook_url:
            logger.warning("未配置飞书 Webhook URL，跳过发送消息")
            return False

        payload = {
            "msg_type": "text",
            "content": {"text": text}
        }
        return await self._post(payload)

    async def send_card(self, title: str, content: Dict, status: str = "blue") -> bool:
        """
        发送交互式卡片
        Args:
            title: 卡片标题
            content: { "key": "value" } 形式的内容结构
            status: 卡片颜色 (blue, green, red, yellow 等)
        """
        if not self.webhook_url:
            logger.warning("未配置飞书 Webhook URL，跳过发送通知卡片")
            return False

        # 构建字段列表
        fields = []
        for k, v in content.items():
            fields.append({
                "is_short": True,
                "text": {
                    "tag": "lark_md",
                    "content": f"**{k}:** {v}"
                }
            })

        payload = {
            "msg_type": "interactive",
            "card": {
                "header": {
                    "title": {
                        "tag": "plain_text",
                        "content": title
                    },
                    "template": status
                },
                "elements": [
                    {
                        "tag": "div",
                        "fields": fields
                    }
                ]
            }
        }

        return await self._post(payload)

    async def _post(self, payload: dict) -> bool:
        """发送 POST 请求"""
        try:
            async with httpx.AsyncClient() as client:
                response = await client.post(
                    self.webhook_url,
                    json=payload,
                    timeout=10.0
                )
                result = response.json()
                if result.get("StatusCode") == 0 or result.get("code") == 0:
                    logger.info("发送飞书 Webhook 通知成功")
                    return True
                else:
                    logger.error(f"发送飞书 Webhook 通知失败: {result}")
                    return False
        except Exception as e:
            logger.error(f"发送飞书 Webhook 异常: {e}")
            return False
