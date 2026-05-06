import sys
import time
import threading
import io
import ssl

# 跳过 SSL 证书验证（解决代理/安全软件导致的证书链问题）
ssl._create_default_https_context = ssl._create_unverified_context

# Windows 终端 GBK 编码兼容：强制 UTF-8 输出
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

# Patch requests SSL 配置（飞书SDK使用requests获取WebSocket endpoint）
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Patch websockets SSL 配置（飞书SDK使用websockets库）
def _patch_websockets_ssl():
    import websockets

    # 创建不验证证书的SSL context
    insecure_ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    insecure_ssl_context.check_hostname = False
    insecure_ssl_context.verify_mode = ssl.CERT_NONE

    # websockets 16.0 版本使用 websockets.connect
    # 同时patch websockets.client.connect以兼容旧代码
    original_connect = websockets.connect

    async def patched_connect(uri, **kwargs):
        if 'ssl' not in kwargs:
            kwargs['ssl'] = insecure_ssl_context
        # 增加超时时间
        if 'open_timeout' not in kwargs:
            kwargs['open_timeout'] = 30
        return await original_connect(uri, **kwargs)

    websockets.connect = patched_connect
    # 兼容旧API
    if hasattr(websockets, 'client'):
        websockets.client.connect = patched_connect

_patch_websockets_ssl()

# Patch requests 默认 session 跳过 SSL 验证
def _patch_requests_ssl():
    import requests
    original_post = requests.post
    original_get = requests.get

    def patched_post(url, **kwargs):
        kwargs['verify'] = False
        return original_post(url, **kwargs)

    def patched_get(url, **kwargs):
        kwargs['verify'] = False
        return original_get(url, **kwargs)

    requests.post = patched_post
    requests.get = patched_get

_patch_requests_ssl()

def log_startup(msg):
    print(f"[{time.strftime('%H:%M:%S')}] {msg}")
    sys.stdout.flush()

log_startup("========================================")
log_startup("🚀 飞书长连接机器人启动序列开始...")
log_startup("========================================")

log_startup("正在加载基础模块 (os, pathlib, loguru)...")
import os
from pathlib import Path
from loguru import logger

# 确保日志目录存在
log_dir = Path(__file__).parent.parent.parent / "logs"
log_dir.mkdir(exist_ok=True)
logger.add(log_dir / "bot.log", rotation="10 MB", retention="30 days", level="DEBUG")

log_startup("正在加载飞书 SDK (lark-oapi)... 这可能需要 10-20 秒...")
import lark_oapi as lark
from lark_oapi.api.im.v1 import *
log_startup("飞书 SDK 加载完成 ✅")

# 添加项目根目录和 src 目录到路径
root_dir = Path(__file__).parent.parent.parent
sys.path.insert(0, str(root_dir))
sys.path.insert(0, str(root_dir / "src"))

# 加载 .env 文件（在 import 项目模块前）
from dotenv import load_dotenv
load_dotenv(root_dir / ".env")
log_startup(".env 环境变量加载完成 ✅")

from bots.feishu_bot import FeishuBot
from rag.knowledge_base import KnowledgeBase
from classifiers.question_classifier import QuestionClassifier
from utils.config_loader import load_config
from utils.template_manager import TemplateManager

# 加载配置（使用项目根目录的配置文件）
config = load_config(str(root_dir / "config" / "config.yaml"))

# 初始化组件
log_startup("正在初始化知识库实例...")
kb = KnowledgeBase(config)

log_startup("正在初始化问题分类器...")
classifier = QuestionClassifier(config)

log_startup("正在初始化模板管理器...")
template_mgr = TemplateManager(config)

# 初始化机器人逻辑处理器
log_startup("正在初始化 FeishuBot 核心逻辑 (会在此处请求飞书 API 获取关键词)...")
feishu_bot_logic = FeishuBot(config, kb, classifier, template_mgr)
log_startup("FeishuBot 核心逻辑初始化完成 ✅")

# ============================================================
# 消息去重机制
# 飞书会在未及时收到响应时重复推送事件，需要对 message_id 去重
# ============================================================
_processed_message_ids = set()
_processed_lock = threading.Lock()
MAX_CACHE_SIZE = 1000


def is_duplicate_message(message_id: str) -> bool:
    """
    检查消息是否已处理过（去重）

    Args:
        message_id: 飞书消息 ID

    Returns:
        True 表示重复消息，应跳过
    """
    with _processed_lock:
        if message_id in _processed_message_ids:
            return True
        _processed_message_ids.add(message_id)
        # 简单淘汰策略：超过上限时清除较早的一半
        if len(_processed_message_ids) > MAX_CACHE_SIZE:
            items = list(_processed_message_ids)
            for mid in items[:MAX_CACHE_SIZE // 2]:
                _processed_message_ids.discard(mid)
        return False


# ============================================================
# 事件处理函数
# ============================================================

def handle_message(data: P2ImMessageReceiveV1):
    """处理消息接收事件 (im.message.receive_v1)"""
    try:
        message_id = data.event.message.message_id
        chat_id = data.event.message.chat_id
        content_raw = data.event.message.content

        log_startup(f"【消息】收到消息 message_id={message_id}, chat_id={chat_id}")
        log_startup(f"【消息】内容: {content_raw[:100] if content_raw else 'empty'}")
        logger.info(f"【事件】im.message.receive_v1, message_id: {message_id}")

        # 去重检查
        if is_duplicate_message(message_id):
            logger.warning(f"【去重】跳过重复消息 message_id: {message_id}")
            return

        # 辅助函数：从 UserId 对象或普通对象中提取 ID 字符串
        # 关键逻辑：当 @机器人时，mention.id 中包含 app_id 属性（机器人的应用 ID）
        # 当 @用户时，只有 open_id 属性，app_id 为空
        # 因此优先检查 app_id，以便正确识别机器人被 @ 的情况
        def get_id_str(obj):
            if obj is None: return ""
            # 优先检查 app_id（机器人 mention 时有此属性）
            app_id_val = getattr(obj, 'app_id', None)
            if app_id_val and isinstance(app_id_val, str) and app_id_val.startswith('cli_'):
                return app_id_val
            # 否则返回 open_id（用户 mention）
            return getattr(obj, 'open_id', None) or getattr(obj, 'user_id', None) or getattr(obj, 'union_id', None) or str(obj)

        # 安全提取 mentions
        raw_mentions = data.event.message.mentions or []
        mentions = []
        for m in raw_mentions:
            try:
                mention_id_obj = getattr(m, 'id', None)
                if mention_id_obj:
                    # 打印完整结构（使用 INFO 级别确保可见）
                    log_startup(f"【Mention】完整对象属性: open_id={getattr(mention_id_obj, 'open_id', None)}, app_id={getattr(mention_id_obj, 'app_id', None)}, user_id={getattr(mention_id_obj, 'user_id', None)}, union_id={getattr(mention_id_obj, 'union_id', None)}")
                    mention_key = get_id_str(mention_id_obj)
                    log_startup(f"【Mention】提取到 ID: {mention_key}")
                    mentions.append({"id": mention_key})
            except Exception as me:
                logger.error(f"Mention 解析失败: {me}")
                pass

        # 将 SDK 对象转换为 FeishuBot 期望的字典格式
        processed_event = {
            "chat_id": data.event.message.chat_id,
            "sender": {
                "sender_id": {
                    "user_id": get_id_str(data.event.sender.sender_id)
                }
            },
            "content": data.event.message.content,
            "message_id": message_id,
            "message": {
                "mentions": mentions
            }
        }

        # 异步交给逻辑处理类 - 在新线程的事件循环中执行
        import asyncio
        try:
            # ws.Client 使用自己的事件循环，我们需要在单独的线程中运行异步任务
            import concurrent.futures
            executor = concurrent.futures.ThreadPoolExecutor(max_workers=1)
            future = executor.submit(asyncio.run, feishu_bot_logic.handle_message(processed_event))
            logger.debug(f"已提交消息处理任务: {message_id}")
        except Exception as task_error:
            logger.error(f"提交消息处理任务失败: {task_error}")

    except Exception as e:
        logger.error(f"【事件处理异常】im.message.receive_v1: {e}")


def handle_bot_added(data):
    """
    处理机器人进群事件 (im.chat.member.bot.added_v1)
    当机器人被添加到群聊时触发
    """
    try:
        chat_id = data.event.chat_id if hasattr(data.event, 'chat_id') else "unknown"
        operator = ""
        if hasattr(data.event, 'operator_id') and data.event.operator_id:
            operator = getattr(data.event.operator_id, 'user_id', 'unknown')

        logger.info(f"【事件】机器人被添加到群 chat_id: {chat_id}, 操作人: {operator}")

        # 发送欢迎消息
        welcome = getattr(config.bots.get("feishu", {}), "welcome_message", None)
        if not welcome:
            # 尝试从 dict 形式获取
            feishu_cfg = config.bots.get("feishu", {})
            if isinstance(feishu_cfg, dict):
                welcome = feishu_cfg.get("welcome_message", "")
            else:
                welcome = getattr(feishu_cfg, "welcome_message", "")

        if welcome and chat_id != "unknown":
            import asyncio
            import concurrent.futures
            executor = concurrent.futures.ThreadPoolExecutor(max_workers=1)
            executor.submit(asyncio.run, feishu_bot_logic.send_message(chat_id, welcome))
            logger.info(f"已发送欢迎消息到群 {chat_id}")

    except Exception as e:
        logger.error(f"【事件处理异常】bot.added: {e}")


def handle_bot_removed(data):
    """
    处理机器人出群事件 (im.chat.member.bot.deleted_v1)
    当机器人被移出群聊时触发
    """
    try:
        chat_id = data.event.chat_id if hasattr(data.event, 'chat_id') else "unknown"
        operator = ""
        if hasattr(data.event, 'operator_id') and data.event.operator_id:
            operator = getattr(data.event.operator_id, 'user_id', 'unknown')

        logger.info(f"【事件】机器人被移出群 chat_id: {chat_id}, 操作人: {operator}")

    except Exception as e:
        logger.error(f"【事件处理异常】bot.deleted: {e}")


def handle_card_action(data):
    """
    处理卡片交互事件 (card.action.trigger)
    当用户点击卡片按钮时触发
    """
    from lark_oapi.event.callback.model.p2_card_action_trigger import P2CardActionTriggerResponse, CallBackToast

    try:
        logger.info(f"【事件】card.action.trigger 收到卡片交互事件")

        # 提取关键信息
        event_obj = data.event if hasattr(data, 'event') else data

        # 从 context.open_message_id 获取 message_id
        context = getattr(event_obj, 'context', None)
        message_id = getattr(context, 'open_message_id', '') if context else ''
        chat_id = getattr(context, 'open_chat_id', '') if context else ''

        # 提取 user_id（优先 open_id）
        operator = getattr(event_obj, 'operator', None)
        user_id = getattr(operator, 'open_id', '') if operator else ''

        # 提取 action.value
        action = getattr(event_obj, 'action', None)
        action_value = getattr(action, 'value', {}) if action else {}

        logger.info(f"【卡片】message_id={message_id}, chat_id={chat_id}, user_id={user_id}")
        logger.info(f"【卡片】action_value: {action_value}")

        # 构建事件字典
        processed_event = {
            "message_id": message_id,
            "chat_id": chat_id,
            "operator": {"user_id": user_id, "open_id": user_id},
            "action": {
                "value": action_value
            }
        }

        # 处理卡片动作并获取结果（在已有事件循环中使用线程执行）
        import asyncio
        import concurrent.futures
        executor = concurrent.futures.ThreadPoolExecutor(max_workers=1)
        future = executor.submit(
            lambda: asyncio.run(feishu_bot_logic.handle_card_action(processed_event))
        )
        result_dict = future.result(timeout=30)
        logger.info(f"【卡片】处理结果: {result_dict}")

        # 构建 SDK 响应对象
        response = P2CardActionTriggerResponse()
        if result_dict and 'toast' in result_dict:
            toast_info = result_dict['toast']
            toast = CallBackToast()
            toast.type = toast_info.get('type', 'info')
            toast.content = toast_info.get('content', '')
            response.toast = toast

        return response

    except Exception as e:
        logger.error(f"【事件处理异常】card.action.trigger: {e}")
        # 返回错误 toast
        response = P2CardActionTriggerResponse()
        toast = CallBackToast()
        toast.type = 'error'
        toast.content = f"处理失败: {str(e)}"
        response.toast = toast
        return response


# ============================================================
# 主入口
# ============================================================

def main():
    """同步启动入口 - ws.Client.start() 使用自己的事件循环"""

    log_startup("========================================")
    log_startup("🚀 飞书长连接机器人启动中 (SDK + WebSocket)...")
    log_startup("========================================")

    # 打印关键词加载状态
    log_startup(f"关键词表配置: base_token={feishu_bot_logic.keyword_base_token}, table_id={feishu_bot_logic.keyword_table_id}")
    log_startup(f"已加载关键词数量: {len(feishu_bot_logic.keyword_replies)}")

    # 后台线程初始化知识库
    def init_kb_background():
        import asyncio
        try:
            logger.info("后台开始初始化知识库...")
            asyncio.run(kb.initialize())
            logger.info("后台知识库初始化成功！")
        except Exception as e:
            logger.error(f"后台知识库初始化失败: {e}")

    kb_thread = threading.Thread(target=init_kb_background, daemon=True)
    kb_thread.start()
    log_startup("知识库后台初始化线程已启动")

    # 获取凭证
    app_id = os.environ.get("FEISHU_APP_ID") or config.bots["feishu"].app_id
    app_secret = os.environ.get("FEISHU_APP_SECRET") or config.bots["feishu"].app_secret
    encrypt_key = os.environ.get("FEISHU_ENCRYPT_KEY") or getattr(config.bots["feishu"], "encrypt_key", "")
    verification_token = os.environ.get("FEISHU_VERIFICATION_TOKEN") or getattr(config.bots["feishu"], "verification_token", "")

    log_startup(f"凭证配置: app_id={app_id[:10]}...")

    if not app_id or not app_secret:
        log_startup("❌ 未找到 FEISHU_APP_ID 或 FEISHU_APP_SECRET")
        return

    # 注册事件处理器（使用新版 API）
    log_startup("正在注册事件处理器...")
    event_handler = lark.EventDispatcherHandler.builder(encrypt_key, verification_token) \
        .register_p2_im_message_receive_v1(handle_message) \
        .register_p2_im_chat_member_bot_added_v1(handle_bot_added) \
        .register_p2_im_chat_member_bot_deleted_v1(handle_bot_removed) \
        .register_p2_card_action_trigger(handle_card_action) \
        .build()
    log_startup("事件处理器注册完成 ✅")

    # 创建长连接客户端（使用新版 API）
    log_startup("正在创建 WebSocket 客户端...")
    client = lark.ws.Client(
        app_id=app_id,
        app_secret=app_secret,
        log_level=lark.LogLevel.INFO,
        event_handler=event_handler
    )
    log_startup("WebSocket 客户端创建完成 ✅")

    log_startup("已注册事件: im.message.receive_v1, im.chat.member_bot.added_v1, im.chat.member_bot.deleted_v1, card.action.trigger")
    log_startup("🚀 启动 WebSocket 连接，等待消息...")
    client.start()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        logger.info("机器人已手动停止")
