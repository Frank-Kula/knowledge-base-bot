"""
飞书卡片回调 HTTP 服务 (FastAPI)
处理交互卡片按钮点击事件

启动方式:
    python src/bots/feishu_card_server.py

需要配合内网穿透工具 (如 ngrok) 让飞书能访问:
    ngrok http 8080

然后在飞书开放平台配置卡片回调地址:
    https://xxx.ngrok.io/feishu/card/callback
"""

import os
import sys
import json
import hashlib

# 添加项目根目录和 src 目录到 Python 路径（与 feishu_ws_main.py 一致）
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
src_dir = os.path.join(project_root, "src")
sys.path.insert(0, project_root)  # 支持 src. 前缀导入
sys.path.insert(0, src_dir)       # 支持 bots. rag. 等直接导入

import uvicorn
from fastapi import FastAPI, Request, Response
from fastapi.responses import JSONResponse
from loguru import logger

# 加载配置
from dotenv import load_dotenv
load_dotenv()

from utils.config_loader import load_config
from pathlib import Path
config_path = Path(project_root) / "config" / "config.yaml"
config = load_config(str(config_path))

logger.info("正在初始化组件...")

# 初始化依赖组件（不带 src. 前缀，因为 sys.path 已指向 src/）
from rag.knowledge_base import KnowledgeBase
kb = KnowledgeBase(config)

from classifiers.question_classifier import QuestionClassifier
classifier = QuestionClassifier(config)

from utils.template_manager import TemplateManager
template_mgr = TemplateManager(config)

# 初始化 FeishuBot 逻辑（用于处理卡片事件）
from bots.feishu_bot import FeishuBot
feishu_bot_logic = FeishuBot(config, kb, classifier, template_mgr)
logger.info("组件初始化完成")

app = FastAPI(title="Feishu Card Callback Server")


def verify_signature(timestamp: str, nonce: str, body: str, signature: str) -> bool:
    """验证飞书回调签名"""
    token = os.environ.get("FEISHU_VERIFICATION_TOKEN") or getattr(config.bots.get("feishu", {}), "verification_token", "")
    if not token:
        logger.warning("未配置 verification_token，跳过签名验证")
        return True

    # 验证签名
    if signature:
        expected = hashlib.sha256(f"{timestamp}{nonce}{token}".encode()).hexdigest()
        return expected == signature
    return True


@app.post("/feishu/card/callback")
async def handle_card_callback(request: Request):
    """处理飞书卡片回调"""
    try:
        body = await request.body()
        body_str = body.decode("utf-8")
        data = json.loads(body_str)

        logger.info(f"[卡片回调] 收到请求: {json.dumps(data, ensure_ascii=False)[:500]}")

        # 处理首次验证请求 (challenge)
        challenge = data.get("challenge")
        if challenge:
            logger.info(f"[卡片回调] Challenge 验证请求: {challenge}")
            return JSONResponse(content={"challenge": challenge})

        # 验证签名
        timestamp = request.headers.get("X-Lark-Request-Timestamp", "")
        nonce = request.headers.get("X-Lark-Request-Nonce", "")
        signature = request.headers.get("X-Lark-Request-Signature", "")

        if not verify_signature(timestamp, nonce, body_str, signature):
            logger.warning("[卡片回调] 签名验证失败")
            return JSONResponse(content={"error": "Invalid signature"}, status_code=403)

        # 解析卡片事件 - 飞书回调格式
        # 格式参考: https://open.feishu.cn/document/ukTMukTMukTM/uYjNwUjL2YDM14iN2ATN
        event_context = data.get("event", {})

        # 提取关键信息
        token = data.get("token", "")  # 这个是 app_token

        # 从不同可能的字段中提取信息
        operator = event_context.get("operator", {})
        user_id = operator.get("user_id", "") or operator.get("open_id", "") or operator.get("union_id", "")

        message_id = event_context.get("message_id", "")

        # action.value 包含按钮点击时携带的数据
        action = event_context.get("action", {})
        action_value = action.get("value", {})
        action_type = action.get("type", "")  # 按钮类型

        logger.info(f"[卡片回调] message_id={message_id}, user_id={user_id}")
        logger.info(f"[卡片回调] action_value={action_value}")

        # 构建事件字典（与 feishu_bot.handle_card_action 期望的格式一致）
        processed_event = {
            "message_id": message_id,
            "operator": {"user_id": user_id},
            "action": {
                "value": action_value
            }
        }

        # 处理卡片动作
        result = await feishu_bot_logic.handle_card_action(processed_event)

        logger.info(f"[卡片回调] 处理结果: {result}")

        # 返回结果（飞书期望 JSON 格式）
        return JSONResponse(content=result)

    except json.JSONDecodeError as e:
        logger.error(f"[卡片回调] JSON 解析失败: {e}")
        return JSONResponse(content={"success": False, "error": "Invalid JSON"}, status_code=400)
    except Exception as e:
        logger.error(f"[卡片回调] 处理异常: {e}")
        return JSONResponse(content={"success": False, "error": str(e)}, status_code=500)


@app.get("/health")
async def health_check():
    """健康检查"""
    return {"status": "ok", "service": "feishu-card-server"}


@app.get("/")
async def root():
    """根路径"""
    return {
        "service": "Feishu Card Callback Server",
        "endpoints": {
            "callback": "/feishu/card/callback",
            "health": "/health"
        }
    }


def run_server(port: int = 8080):
    """启动 HTTP 服务"""
    logger.info(f"启动飞书卡片回调服务，端口: {port}")
    logger.info(f"本地回调地址: http://localhost:{port}/feishu/card/callback")
    logger.info("=")
    logger.info("需要配合内网穿透工具 (如 ngrok) 使用:")
    logger.info("  1. 安装 ngrok: https://ngrok.com/download")
    logger.info("  2. 运行: ngrok http 8080")
    logger.info("  3. 将 ngrok 提供的 https 地址配置到飞书开放平台")
    logger.info("=")
    uvicorn.run(app, host="0.0.0.0", port=port, log_level="info")


if __name__ == "__main__":
    port = int(os.environ.get("CARD_SERVER_PORT", 8080))
    run_server(port)