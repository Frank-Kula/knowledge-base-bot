"""
测试交互式消息卡片发送
验证 MessageCardBuilder 和 lark-cli 交互卡片功能
"""

import os
import sys
import asyncio
import io

# Windows 编码兼容
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

# 添加项目路径
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

from dotenv import load_dotenv
load_dotenv()

from src.utils.config_loader import load_config
from src.integrations.lark_cli_wrapper import LarkCliWrapper
from src.utils.message_card_builder import build_bug_alert_card, build_feature_card


async def test_bug_alert_card():
    """测试 Bug 告警卡片"""
    print("\n" + "=" * 60)
    print("测试 1: 发送 Bug 告警卡片")
    print("=" * 60)

    config = load_config()
    lark_cli = LarkCliWrapper(config)

    chat_id = "oc_9181c1f2869b0ec0af937f5c6f9a82aa"

    # 从配置获取 app_token 和 table_id
    app_token = lark_cli.app_token
    table_id = lark_cli.bug_table_id

    # 构建卡片 JSON（使用 AppLink）
    card_json = build_bug_alert_card(
        title="测试 Bug：交互卡片验证",
        source="技术支持群",
        user="测试用户",
        keywords=["崩溃", "无法登录"],
        confidence=0.85,
        quote="用户反馈：打开软件后立即崩溃，无法正常使用",
        record_id="rec_test123",
        app_token=app_token,
        table_id=table_id,
        doc_gap="缺少错误码对应解决方案文档",
        product_suggestion="建议增加自动崩溃日志收集功能"
    )

    print(f"卡片 JSON 长度: {len(card_json)} 字符")

    # 发送交互卡片
    result = lark_cli.send_message(
        receive_id=chat_id,
        content=card_json,
        receive_id_type="chat_id",
        msg_type="interactive"
    )

    if result.get("success"):
        print(f"Bug 卡片发送成功: message_id={result.get('message_id')}")
    else:
        print(f"Bug 卡片发送失败: {result.get('error')}")

    return result


async def test_feature_card():
    """测试需求建议卡片"""
    print("\n" + "=" * 60)
    print("测试 2: 发送需求建议卡片")
    print("=" * 60)

    config = load_config()
    lark_cli = LarkCliWrapper(config)

    chat_id = "oc_9181c1f2869b0ec0af937f5c6f9a82aa"

    # 从配置获取 app_token 和 table_id
    app_token = lark_cli.app_token
    table_id = lark_cli.feature_table_id

    # 构建卡片 JSON（使用 AppLink）
    card_json = build_feature_card(
        title="测试需求：批量导出功能",
        source="技术支持群",
        user="产品经理",
        keywords=["批量", "导出"],
        confidence=0.75,
        quote="希望能支持批量导出所有数据，而不是逐条导出",
        record_id="rec_feature123",
        app_token=app_token,
        table_id=table_id,
        scenario="用户需要定期备份系统数据，当前逐条导出效率低"
    )

    print(f"卡片 JSON 长度: {len(card_json)} 字符")

    # 发送交互卡片
    result = lark_cli.send_message(
        receive_id=chat_id,
        content=card_json,
        receive_id_type="chat_id",
        msg_type="interactive"
    )

    if result.get("success"):
        print(f"需求卡片发送成功: message_id={result.get('message_id')}")
    else:
        print(f"需求卡片发送失败: {result.get('error')}")

    return result


async def test_text_message():
    """测试普通文本消息（对照组）"""
    print("\n" + "=" * 60)
    print("测试 3: 发送普通文本消息")
    print("=" * 60)

    config = load_config()
    lark_cli = LarkCliWrapper(config)

    chat_id = "oc_9181c1f2869b0ec0af937f5c6f9a82aa"

    # 发送普通文本
    result = lark_cli.send_message(
        receive_id=chat_id,
        content="交互卡片测试完成 ✅",
        receive_id_type="chat_id",
        msg_type="text"
    )

    if result.get("success"):
        print(f"文本消息发送成功: message_id={result.get('message_id')}")
    else:
        print(f"文本消息发送失败: {result.get('error')}")

    return result


async def main():
    """运行所有测试"""
    print("\n" + "=" * 60)
    print("交互式消息卡片测试")
    print("=" * 60)

    required_vars = ["FEISHU_APP_TOKEN", "FEISHU_BUG_TABLE_ID", "FEISHU_FEATURE_TABLE_ID"]
    missing_vars = [var for var in required_vars if not os.getenv(var)]

    if missing_vars:
        print("\n缺少环境变量:")
        for var in missing_vars:
            print(f"   - {var}")
        return

    print("\n开始测试...\n")

    # 执行测试
    bug_result = await test_bug_alert_card()
    feature_result = await test_feature_card()
    text_result = await test_text_message()

    print("\n" + "=" * 60)
    print("测试完成！")
    print("=" * 60)

    # 统计结果
    all_pass = bug_result.get("success") and feature_result.get("success") and text_result.get("success")
    print(f"\n{'全部测试通过 ✅' if all_pass else '部分测试失败 ❌'}")


if __name__ == "__main__":
    asyncio.run(main())