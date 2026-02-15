"""
技术支持机器人主入口
支持企微和飞书机器人
"""

import asyncio
import uvicorn
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from loguru import logger

import sys
from pathlib import Path

# 添加项目根目录到路径
sys.path.insert(0, str(Path(__file__).parent.parent))

from bots.wecom_bot import WeComBot
from bots.feishu_bot import FeishuBot
from rag.knowledge_base import KnowledgeBase
from classifiers.question_classifier import QuestionClassifier
from utils.config_loader import load_config
from utils.template_manager import TemplateManager

# 初始化应用
app = FastAPI(title="技术支持知识库机器人")

# 加载配置
config = load_config()

# 初始化组件
kb = KnowledgeBase(config)
classifier = QuestionClassifier(config)
template_mgr = TemplateManager(config)

# 初始化机器人
wecom_bot = WeComBot(config, kb, classifier, template_mgr)
feishu_bot = FeishuBot(config, kb, classifier, template_mgr)


@app.get("/")
async def root():
    """健康检查"""
    return {"status": "ok", "message": "技术支持机器人运行中"}


@app.post("/webhook/wecom")
async def wecom_webhook(request: Request):
    """企微机器人 Webhook"""
    try:
        data = await request.json()

        # 企微消息验证
        if data.get("MsgType") != "text":
            return JSONResponse(content={"errmsg": "ok"})

        # 异步处理消息
        asyncio.create_task(wecom_bot.handle_message(data))

        return JSONResponse(content={"errmsg": "ok"})

    except Exception as e:
        logger.error(f"企微 Webhook 处理错误: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/webhook/feishu")
async def feishu_webhook(request: Request):
    """飞书机器人 Webhook"""
    try:
        data = await request.json()

        # 飞书挑战验证
        if "challenge" in data:
            return JSONResponse(content={"challenge": data["challenge"]})

        # 飞书消息处理
        if data.get("type") == "event":
            event = data.get("event", {})
            if event.get("type") == "message":
                asyncio.create_task(feishu_bot.handle_message(event))

        return JSONResponse(content={"code": 0, "msg": "ok"})

    except Exception as e:
        logger.error(f"飞书 Webhook 处理错误: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@app.on_event("startup")
async def startup_event():
    """启动事件"""
    logger.info("技术支持知识库机器人启动中...")

    # 初始化知识库
    await kb.initialize()

    logger.info("机器人启动完成，监听端口: {}", config.server.port)


@app.on_event("shutdown")
async def shutdown_event():
    """关闭事件"""
    logger.info("机器人正在关闭...")
    await kb.close()


if __name__ == "__main__":
    # 启动服务器
    uvicorn.run(
        "main:app",
        host=config.server.host,
        port=config.server.port,
        reload=config.server.debug,
    )
