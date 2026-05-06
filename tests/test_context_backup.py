"""
测试上下文备份功能
"""

import sys
from pathlib import Path
from dotenv import load_dotenv

load_dotenv(Path(__file__).parent.parent / '.env')

sys.path.insert(0, str(Path(__file__).parent.parent))

from src.watchers.bug_keyword_watcher import BugKeywordWatcher
from src.integrations.lark_cli_wrapper import LarkCliWrapper
from src.utils.config_loader import load_config


def test_get_chat_messages():
    """测试获取历史消息"""
    config = load_config()
    wrapper = LarkCliWrapper(config)

    chat_id = "oc_9181c1f2869b0ec0af937f5c6f9a82aa"

    print("\n=== 测试获取历史消息 ===")
    result = wrapper.get_chat_messages(chat_id, page_size=5)

    if result.get("success"):
        msgs = result.get("messages", [])
        print(f"获取到 {len(msgs)} 条消息")
        for m in msgs:
            msg_id = m.get("message_id", "")
            # 避免打印包含 emoji 的内容
            print(f"  [{msg_id}] (消息类型: {m.get('msg_type', 'text')})")
    else:
        print(f"失败: {result.get('error')}")


def test_context_messages():
    """测试获取上下文消息"""
    watcher = BugKeywordWatcher()

    test_msg = {
        "content": "测试：Apifox 打开就报错了",
        "message_id": "test_msg_001",
        "chat_id": "oc_9181c1f2869b0ec0af937f5c6f9a82aa",
        "create_time": "2026-04-17T15:30:00+08:00",
        "sender": {"id": "test_sender", "name": "测试用户"}
    }

    print("\n=== 测试获取上下文 ===")
    context = watcher.get_context_messages(
        test_msg["chat_id"],
        test_msg["create_time"],
        context_size=20
    )

    print(f"获取到 {len(context)} 条上下文消息")


def test_format_markdown():
    """测试格式化 Markdown"""
    watcher = BugKeywordWatcher()

    test_msg = {
        "content": "测试：Apifox 打开就报错了",
        "message_id": "test_msg_001",
        "chat_id": "oc_9181c1f2869b0ec0af937f5c6f9a82aa",
        "create_time": "2026-04-17T15:30:00+08:00",
        "sender": {"id": "test_sender", "name": "测试用户"}
    }

    context = watcher.get_context_messages(
        test_msg["chat_id"],
        test_msg["create_time"]
    )

    print("\n=== 测试格式化 Markdown ===")
    md = watcher.format_context_markdown(context, test_msg["message_id"])

    if md:
        # 保存到文件（避免编码问题）
        output_file = Path(__file__).parent / "context_output.md"
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(md)
        print(f"Markdown 已保存到: {output_file}")
        print(f"内容长度: {len(md)} 字符")
    else:
        print("Markdown 为空")


def test_full_flow():
    """测试完整流程"""
    watcher = BugKeywordWatcher()

    test_msg = {
        "content": "Apifox 导入数据的时候白屏了，没有任何提示",
        "message_id": "test_msg_002",
        "chat_id": "oc_9181c1f2869b0ec0af937f5c6f9a82aa",
        "create_time": "2026-04-17T15:31:00+08:00",
        "sender": {"id": "test_sender", "name": "用户A"}
    }

    print("\n=== 测试完整流程 ===")

    # 1. 分析消息
    analysis = watcher.analyze_message(test_msg)
    print(f"类型: {analysis['type']}")
    print(f"置信度: {analysis['confidence']:.1%}")
    print(f"关键词: {analysis['keywords']}")

    # 2. 获取上下文
    context = watcher.get_context_messages(
        test_msg["chat_id"],
        test_msg["create_time"]
    )
    print(f"上下文: {len(context)} 条")

    # 3. 格式化 Markdown
    md = watcher.format_context_markdown(context, test_msg["message_id"])
    print(f"Markdown: {len(md)} 字符")


if __name__ == "__main__":
    print("=" * 50)
    print("上下文备份功能测试")
    print("=" * 50)

    test_get_chat_messages()
    test_context_messages()
    test_format_markdown()
    test_full_flow()

    print("\n" + "=" * 50)
    print("测试完成")
    print("=" * 50)