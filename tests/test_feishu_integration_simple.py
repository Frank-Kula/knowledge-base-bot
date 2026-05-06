"""
测试飞书集成模块（简化版）
验证 FeishuIntegration 的发送消息和创建工单功能
测试结果发送到飞书群（markdown 格式）
"""

import os
import sys
import asyncio
import io
from datetime import datetime

# Windows 编码兼容
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

# 添加项目路径
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

from dotenv import load_dotenv
load_dotenv()

from src.bots.feishu_integration import FeishuIntegration
from src.utils.config_loader import load_config


async def test_send_message():
    """测试发送消息"""
    print("\n" + "=" * 60)
    print("测试 1: 发送消息到飞书群")
    print("=" * 60)

    config = load_config()
    feishu = FeishuIntegration(config)

    chat_id = "oc_9181c1f2869b0ec0af937f5c6f9a82aa"

    result = await feishu.send_message(
        receive_id=chat_id,
        content="飞书集成模块测试启动...",
        receive_id_type="chat_id"
    )

    if result:
        print("消息发送成功")
    else:
        print("消息发送失败")

    return result, chat_id


async def test_create_bug_ticket():
    """测试创建 Bug 工单"""
    print("\n" + "=" * 60)
    print("测试 2: 创建 Bug 工单")
    print("=" * 60)

    config = load_config()
    feishu = FeishuIntegration(config)

    ticket_data = {
        "title": "测试 Bug：飞书集成模块验证",
        "environment_version": "Web端, 2.5.0",
        "steps": "1. 启动测试脚本\n2. 检查飞书群消息\n3. 验证多维表格记录",
        "status_expected": "现状：测试通过\n预期：功能正常",
    }

    result = await feishu.create_ticket(
        ticket_type="bug",
        title="[测试] 飞书集成模块验证 - lark-cli 模式",
        data=ticket_data
    )

    if result.get("success"):
        print(f"工单创建成功: {result.get('record_id')}")
        print(f"URL: {result.get('url')}")
    else:
        print(f"工单创建失败: {result.get('error')}")

    return result, ticket_data


async def test_create_feature_ticket():
    """测试创建需求工单"""
    print("\n" + "=" * 60)
    print("测试 3: 创建需求工单")
    print("=" * 60)

    config = load_config()
    feishu = FeishuIntegration(config)

    ticket_data = {
        "title": "测试需求：飞书集成优化",
        "description": "简化飞书集成代码，删除冗余的 httpx 降级逻辑，统一使用 lark-cli"
    }

    result = await feishu.create_ticket(
        ticket_type="feature",
        title="[测试] 飞书集成优化 - 删除 httpx 降级",
        data=ticket_data
    )

    if result.get("success"):
        print(f"工单创建成功: {result.get('record_id')}")
        print(f"URL: {result.get('url')}")
    else:
        print(f"工单创建失败: {result.get('error')}")

    return result, ticket_data


async def main():
    """运行所有测试"""
    print("\n" + "=" * 60)
    print("飞书集成模块测试（lark-cli 模式）")
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
    msg_result, chat_id = await test_send_message()
    bug_result, bug_data = await test_create_bug_ticket()
    feature_result, feature_data = await test_create_feature_ticket()

    print("\n" + "=" * 60)
    print("测试完成！")
    print("=" * 60)

    # 构建详细测试报告（markdown 格式）
    config = load_config()
    feishu = FeishuIntegration(config)

    all_pass = msg_result and bug_result.get("success") and feature_result.get("success")

    # Bug 工单详情
    bug_title = bug_data.get("title", "N/A")
    bug_env = bug_data.get("environment_version", "N/A")
    bug_steps = bug_data.get("steps", "N/A")
    bug_id = bug_result.get("record_id", "N/A") if bug_result.get("success") else "失败"
    bug_url = bug_result.get("url", "N/A") if bug_result.get("success") else "N/A"

    # 需求工单详情
    feature_title = feature_data.get("title", "N/A")
    feature_desc = feature_data.get("description", "N/A")
    feature_id = feature_result.get("record_id", "N/A") if feature_result.get("success") else "失败"
    feature_url = feature_result.get("url", "N/A") if feature_result.get("success") else "N/A"

    report = f"""**飞书集成模块测试报告**

测试时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
测试模式：lark-cli（已删除 httpx 降级逻辑）

---

**测试结果总览**

| 测试项 | 状态 | 结果 |
| :--- | :---: | :--- |
| 发送消息 | {'通过' if msg_result else '失败'} | {'成功' if msg_result else '失败'} |
| Bug 工单 | {'通过' if bug_result.get('success') else '失败'} | {bug_id} |
| 需求工单 | {'通过' if feature_result.get('success') else '失败'} | {feature_id} |

---

**Bug 工单详情**

- **标题**: {bug_title}
- **环境版本**: {bug_env}
- **复现步骤**:
{bug_steps}
- **Record ID**: {bug_id}
- **链接**: [{bug_url}]({bug_url})

---

**需求工单详情**

- **标题**: {feature_title}
- **描述**: {feature_desc}
- **Record ID**: {feature_id}
- **链接**: [{feature_url}]({feature_url})

---

**优化内容**

1. 删除 httpx 降级逻辑（`_get_tenant_access_token`、`_create_record_httpx` 等）
2. 统一使用 lark-cli 调用飞书 API
3. 代码从 ~300 行简化到 ~100 行

---

**{'全部测试通过' if all_pass else '部分测试失败'}**"""

    # 使用 markdown 格式发送
    result = feishu.lark_cli.send_message(
        receive_id=chat_id,
        content=report,
        receive_id_type="chat_id",
        msg_type="post"  # markdown 格式
    )

    if result.get("success"):
        print(f"\n测试报告已发送到飞书群 (message_id: {result.get('message_id')})")
    else:
        print(f"\n测试报告发送失败: {result.get('error')}")


if __name__ == "__main__":
    asyncio.run(main())