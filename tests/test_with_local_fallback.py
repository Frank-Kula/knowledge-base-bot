"""
测试飞书集成（本地降级方案）
如果多维表格写入失败，则记录到本地文件
"""

import os
import sys
import asyncio
import json
from datetime import datetime
from dotenv import load_dotenv

# 设置 UTF-8 编码输出
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from src.bots.message_processor import MessageProcessor

# 加载环境变量
load_dotenv()

print("=" * 80)
print("飞书集成测试（本地降级方案）")
print("=" * 80)

async def test_with_fallback():
    """测试消息处理，失败时记录到本地"""
    processor = MessageProcessor()

    user_id = "test_user_001"
    chat_id = "test_chat_001"
    message = "接口测试失败了，返回500错误"

    print(f"\n[用户] {message}")

    # 处理消息
    result = await processor.process_message(
        user_id=user_id,
        chat_id=chat_id,
        message=message
    )

    print(f"\n[机器人] {result['reply']}")

    # 如果是Bug或Feature，模拟信息收集
    if result['success'] and "已识别为" in result['reply']:
        print("\n[模拟信息收集 - 自动填充]")

        from src.utils.config_loader import load_config
        config = load_config()

        # 判断类型
        if "缺陷" in result['reply']:
            processor.conversation_manager.fields = config.info_collection.bug_fields
            problem_type = "bug"
            test_data = {
                "title": "接口测试返回500错误",
                "version": "2.5.0",
                "environment": "Web端",
                "steps": "1. 打开Apifox\n2. 创建接口测试\n3. 发送请求",
                "expected": "返回200",
                "actual": "返回500错误",
                "reproducibility": "必现",
                "additional_info": "测试数据"
            }
        else:
            processor.conversation_manager.fields = config.info_collection.feature_fields
            problem_type = "feature"
            test_data = {
                "title": "希望支持批量导出",
                "user_scenario": "项目归档需要",
                "current_status": "只能逐个导出",
                "user_expectation": "批量导出PDF",
                "user_type": "企业",
                "subscription_status": "付费版",
                "team_size": "50",
                "impact_level": "节省时间"
            }

        # 保存分类信息
        processor.conversation_manager.conversations[user_id]["collected_data"]["_classification"] = {
            "type": problem_type,
            "confidence": 0.95,
            "reason": "测试分类"
        }
        processor.conversation_manager.conversations[user_id]["collected_data"]["_chat_id"] = chat_id

        # 模拟收集所有信息
        for field_name, value in test_data.items():
            result = await processor.process_message(user_id, chat_id, value)

            # 工单创建完成或失败
            if "工单" in result['reply'] or "失败" in result['reply']:
                print(f"\n[机器人] {result['reply']}")

                # 如果创建失败，保存到本地文件
                if not result.get('success', True):
                    save_to_local(problem_type, test_data)
                break

def save_to_local(problem_type, data):
    """保存到本地JSON文件"""
    os.makedirs("data/local_tickets", exist_ok=True)
    filename = f"data/local_tickets/{problem_type}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"

    ticket = {
        "type": problem_type,
        "created_at": datetime.now().isoformat(),
        "data": data
    }

    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(ticket, f, ensure_ascii=False, indent=2)

    print(f"\n✅ 已保存到本地文件：{filename}")
    print(f"📁 文件内容：")
    print(json.dumps(ticket, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    asyncio.run(test_with_fallback())
