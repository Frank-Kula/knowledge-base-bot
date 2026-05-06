"""
企微消息接收服务
接收企微后台推送的消息，转发给 WeComBridge 处理
"""

import hashlib
import hmac
import base64
import json
import asyncio
from typing import Optional
from Crypto.Cipher import AES
from fastapi import FastAPI, Request, Query, HTTPException
from fastapi.responses import PlainTextResponse
from loguru import logger
from pathlib import Path

from dotenv import load_dotenv
load_dotenv(Path(__file__).parent.parent.parent / '.env')

from src.bridges.wecom_bridge import WeComBridge
from src.utils.config_loader import load_config


class WeComCrypto:
    """企微消息加解密"""

    def __init__(self, token: str, encoding_aes_key: str, corp_id: str = ""):
        self.token = token
        # EncodingAESKey 是 43 位，需要补 '=' 变成 44 位 base64
        self.aes_key = base64.b64decode(encoding_aes_key + "=")
        self.corp_id = corp_id

    def verify_signature(self, signature: str, timestamp: str, nonce: str) -> bool:
        """验证签名"""
        try:
            # 签名算法: sha1(token + timestamp + nonce)
            items = [self.token, timestamp, nonce]
            items.sort()
            joined = "".join(items)
            calculated = hashlib.sha1(joined.encode()).hexdigest()

            return calculated == signature
        except Exception as e:
            logger.error(f"签名验证失败: {e}")
            return False

    def decrypt(self, encrypt_msg: str) -> str:
        """解密消息"""
        try:
            cipher = AES.new(self.aes_key, AES.MODE_CBC, self.aes_key[:16])

            # Base64 解码
            encrypted = base64.b64decode(encrypt_msg)

            # AES 解密
            decrypted = cipher.decrypt(encrypted)

            # 去除 PKCS7 padding
            pad = decrypted[-1]
            decrypted = decrypted[:-pad]

            # 解析内容格式: random(16) + msg_len(4) + msg + corp_id
            # 跳过前 16 字节随机数
            msg_len = int.from_bytes(decrypted[16:20], 'big')
            msg_content = decrypted[20:20 + msg_len].decode('utf-8')

            return msg_content
        except Exception as e:
            logger.error(f"消息解密失败: {e}")
            return ""

    def encrypt(self, msg: str) -> str:
        """加密响应消息"""
        try:
            # 添加 corp_id
            msg_bytes = msg.encode('utf-8')
            corp_bytes = self.corp_id.encode('utf-8')

            # 构造内容: random(16) + msg_len(4) + msg + corp_id
            import os
            random_bytes = os.urandom(16)
            msg_len_bytes = len(msg_bytes).to_bytes(4, 'big')
            content = random_bytes + msg_len_bytes + msg_bytes + corp_bytes

            # PKCS7 padding
            pad_len = 32 - (len(content) % 32)
            content += bytes([pad_len] * pad_len)

            # AES 加密
            cipher = AES.new(self.aes_key, AES.MODE_CBC, self.aes_key[:16])
            encrypted = cipher.encrypt(content)

            # Base64 编码
            return base64.b64encode(encrypted).decode('utf-8')
        except Exception as e:
            logger.error(f"消息加密失败: {e}")
            return ""


app = FastAPI(title="WeCom Message Receiver")

# 全局变量
wecom_bridge: Optional[WeComBridge] = None
wecom_crypto: Optional[WeComCrypto] = None


@app.on_event("startup")
async def startup():
    """初始化"""
    global wecom_bridge, wecom_crypto

    config = load_config()
    wecom_bridge = WeComBridge()

    # 从配置读取 Token 和 EncodingAESKey
    wecom_config = getattr(config.bots, 'wecom', {})
    token = getattr(wecom_config, 'token', 'YourTokenHere')
    encoding_aes_key = getattr(wecom_config, 'encoding_aes_key', '')
    corp_id = getattr(wecom_config, 'corp_id', '')

    wecom_crypto = WeComCrypto(token, encoding_aes_key, corp_id)

    logger.info(f"企微接收服务已启动, token={token[:4]}...")


@app.get("/wecom/callback")
async def verify_url(
    msg_signature: str = Query(...),
    timestamp: str = Query(...),
    nonce: str = Query(...),
    echostr: str = Query(...)
):
    """
    验证 URL（企微配置时调用）

    企微会发送 GET 请求验证 URL 是否有效
    需要验证签名，解密 echostr 并返回
    """
    logger.info(f"收到企微 URL 验证请求: timestamp={timestamp}, nonce={nonce}")

    # 验证签名
    if not wecom_crypto.verify_signature(msg_signature, timestamp, nonce):
        logger.warning(f"签名验证失败: {msg_signature}")
        raise HTTPException(status_code=403, detail="签名验证失败")

    # 解密 echostr
    decrypted_echo = wecom_crypto.decrypt(echostr)
    if not decrypted_echo:
        logger.warning("echostr 解密失败")
        raise HTTPException(status_code=400, detail="解密失败")

    logger.info(f"URL 验证成功, 返回: {decrypted_echo}")
    return PlainTextResponse(content=decrypted_echo)


@app.post("/wecom/callback")
async def receive_message(request: Request):
    """
    接收企微消息推送

    企微会发送 POST 请求推送群消息
    """
    try:
        # 解析 XML 或 JSON
        body = await request.body()
        content_type = request.headers.get("content-type", "")

        if "xml" in content_type.lower():
            # XML 格式（旧版）
            import xml.etree.ElementTree as ET
            root = ET.fromstring(body.decode('utf-8'))
            encrypt_msg = root.find('Encrypt').text
        else:
            # JSON 格式（新版）
            data = json.loads(body.decode('utf-8'))
            encrypt_msg = data.get('encrypt', '')

        # 解密消息
        decrypted = wecom_crypto.decrypt(encrypt_msg)
        if not decrypted:
            logger.warning("消息解密失败")
            return PlainTextResponse(content="success")

        logger.info(f"收到企微消息: {decrypted[:200]}")

        # 解析消息内容
        raw_message = json.loads(decrypted)

        # 调用 WeComBridge 处理
        result = await asyncio.to_thread(
            wecom_bridge.process_message,
            raw_message
        )

        if result:
            logger.info(f"企微消息处理成功: {result.get('record_id')}")
        else:
            logger.debug("企微消息未创建工单（已处理或未匹配关键词）")

        # 返回 success 表示接收成功
        return PlainTextResponse(content="success")

    except Exception as e:
        logger.error(f"企微消息处理异常: {e}")
        return PlainTextResponse(content="success")


def main():
    """启动服务"""
    import uvicorn

    config = load_config()
    port = getattr(config.server, 'port', 8000)

    logger.info(f"启动企微接收服务: http://0.0.0.0:{port}/wecom/callback")

    uvicorn.run(
        "src.servers.wecom_server:app",
        host="0.0.0.0",
        port=port,
        reload=False
    )


if __name__ == "__main__":
    main()