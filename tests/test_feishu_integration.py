"""
测试飞书集成
模拟消息处理流程
"""

import os
import sys
import asyncio
from dotenv import load_dotenv

# 设置 UTF-8 编码输出（Windows 兼容）
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

# 添加项目路径
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from src.bots.message_processor import MessageProcessor

# 加载环境变量
load_dotenv()

print("=" * 80)
print("飞书集成测试")
print("=" * 80)
print("\n注意：此测试需要配置飞书环境变量")
print("如果未配置，将只测试消息处理流程\n")

print("=" * 80)
print("测试场景 1：Bug 报告")
print("=" * 80)

async def test_bug_scenario():
    """测试 Bug 报告场景"""
    processor = MessageProcessor()

    user_id = "test_user_001"
    chat_id = "test_chat_001"

    # 第1步：用户报告问题
    print("\n[用户] 接口测试失败了，返回500错误")

    result = await processor.process_message(
        user_id=user_id,
        chat_id=chat_id,
        message="接口测试失败了，返回500错误"
    )

    print(f"[机器人] {result['reply']}")

    if result['success'] and "已识别为" in result['reply']:
        # 第2步：提供信息（简化版，直接跳到最后）
        print("\n[模拟信息收集 - 自动填充测试数据]")

        # 模拟提供所有字段
        from src.utils.config_loader import load_config
        config = load_config()
        processor.conversation_manager.fields = config.info_collection.bug_fields

        # 保存分类结果到对话上下文
        processor.conversation_manager.conversations[user_id]["collected_data"]["_classification"] = {
            "type": "bug",
            "confidence": 0.95,
            "reason": "测试分类"
        }
        processor.conversation_manager.conversations[user_id]["collected_data"]["_chat_id"] = chat_id

        answers = {
            "title": "接口测试返回500错误",
            "version": "2.5.0",
            "environment": "Web端",
            "steps": "1. 打开 Apifox\n2. 创建接口测试\n3. 发送请求\n4. 返回500错误",
            "expected": "接口正常返回200",
            "actual": "服务器返回500错误",
            "reproducibility": "必现",
            "additional_info": "Console报错截图已上传"
        }

        for field_name, answer in answers.items():
            result = await processor.process_message(
                user_id=user_id,
                chat_id=chat_id,
                message=answer
            )

            # 如果完成了，显示结果
            if "工单" in result['reply'] or "创建" in result['reply']:
                print(f"\n[机器人] {result['reply']}")
                break

    return result

print("\n" + "=" * 80)
print("测试场景 2：需求报告")
print("=" * 80)

async def test_feature_scenario():
    """测试需求报告场景"""
    processor = MessageProcessor()

    user_id = "test_user_002"
    chat_id = "test_chat_002"

    # 第1步：用户提出需求
    print("\n[用户] 希望能支持批量导出接口文档")

    result = await processor.process_message(
        user_id=user_id,
        chat_id=chat_id,
        message="希望能支持批量导出接口文档"
    )

    print(f"[机器人] {result['reply']}")

    if result['success'] and "已识别为" in result['reply']:
        print("\n[模拟信息收集 - 自动填充测试数据]")

        # 模拟提供所有字段
        from src.utils.config_loader import load_config
        config = load_config()
        processor.conversation_manager.fields = config.info_collection.feature_fields

        # 保存分类结果到对话上下文
        processor.conversation_manager.conversations[user_id]["collected_data"]["_classification"] = {
            "type": "feature",
            "confidence": 1.0,
            "reason": "测试分类"
        }
        processor.conversation_manager.conversations[user_id]["collected_data"]["_chat_id"] = chat_id

        answers = {
            "title": "希望支持批量导出接口文档",
            "user_scenario": "项目结束时需要归档所有接口文档",
            "current_status": "目前只能逐个导出接口",
            "user_expectation": "希望能够选择多个接口，一次性导出为PDF",
            "user_type": "企业",
            "subscription_status": "付费版",
            "team_size": "50人",
            "impact_level": "每次项目归档节省约2小时"
        }

        for field_name, answer in answers.items():
            result = await processor.process_message(
                user_id=user_id,
                chat_id=chat_id,
                message=answer
            )

            if "工单" in result['reply'] or "创建" in result['reply']:
                print(f"\n[机器人] {result['reply']}")
                break

    return result

async def main():
    """运行所有测试"""
    print("\n🚀 开始测试...\n")

    # 检查环境变量
    required_vars = [
        "FEISHU_APP_ID",
        "FEISHU_APP_SECRET",
        "FEISHU_APP_TOKEN",
        "FEISHU_BUG_TABLE_ID",
        "FEISHU_FEATURE_TABLE_ID"
    ]

    missing_vars = [var for var in required_vars if not os.getenv(var)]

    if missing_vars:
        print("⚠️  警告：以下飞书环境变量未配置：")
        for var in missing_vars:
            print(f"   - {var}")
        print("\n将跳过实际的多维表格写入，只测试消息处理流程。\n")

    # 测试 Bug 场景
    print("\n" + "📋 " + "=" * 76)
    try:
        await test_bug_scenario()
        print("\n✅ Bug 场景测试完成")
    except Exception as e:
        print(f"\n❌ Bug 场景测试失败: {e}")

    # 测试 Feature 场景
    print("\n" + "📋 " + "=" * 76)
    try:
        await test_feature_scenario()
        print("\n✅ Feature 场景测试完成")
    except Exception as e:
        print(f"\n❌ Feature 场景测试失败: {e}")

    print("\n" + "=" * 80)
    print("测试完成！")
    print("=" * 80)
    print("\n下一步：")
    print("1. 配置飞书环境变量")
    print("2. 启动服务器: python -m uvicorn src.main:app --reload")
    print("3. 配置飞书 Webhook URL")
    print("4. 在飞书群中测试")

if __name__ == "__main__":
    asyncio.run(main())
