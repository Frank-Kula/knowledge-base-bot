"""
测试 lark_cli_wrapper 封装
"""

import sys
import os

# 加载 .env 环境变量
from dotenv import load_dotenv
load_dotenv('D:/document-all/TechnicalSupport/knowledge-base-bot/.env')

sys.path.insert(0, 'D:/document-all/TechnicalSupport/knowledge-base-bot')

from src.integrations.lark_cli_wrapper import LarkCliWrapper
from src.utils.config_loader import load_config
from loguru import logger


def test_send_message():
    """测试发送消息"""
    config = load_config()
    wrapper = LarkCliWrapper(config)

    # 发送测试消息到 bot 群
    result = wrapper.send_message(
        receive_id="oc_9181c1f2869b0ec0af937f5c6f9a82aa",
        content="✅ 测试：lark_cli_wrapper 发送消息成功",
        receive_id_type="chat_id"
    )

    print(f"发送结果: {result}")
    assert result["success"], "消息发送失败"


def test_get_field_list():
    """测试获取字段列表"""
    config = load_config()
    wrapper = LarkCliWrapper(config)

    result = wrapper.get_field_list(wrapper.bug_table_id)
    print(f"字段列表: {result}")

    if result["success"]:
        for field in result["fields"]:
            print(f"  - {field['field_name']}: {field['type']}")


def test_create_record():
    """测试创建记录（需要权限）"""
    config = load_config()
    wrapper = LarkCliWrapper(config)

    result = wrapper.create_record(
        table_id=wrapper.bug_table_id,
        fields={
            "标题": "测试：lark_cli_wrapper 创建记录",
            "类型": "缺陷",
            "环境": "测试环境",
            "状态": "待处理"
        }
    )

    print(f"创建结果: {result}")
    if result["success"]:
        print(f"记录 ID: {result['record_id']}")
        print(f"记录链接: {result['url']}")


if __name__ == "__main__":
    logger.info("开始测试 lark_cli_wrapper")

    # 测试发送消息
    print("\n=== 测试发送消息 ===")
    test_send_message()

    # 测试获取字段列表
    print("\n=== 测试获取字段列表 ===")
    test_get_field_list()

    # 测试创建记录
    print("\n=== 测试创建记录 ===")
    test_create_record()

    logger.info("测试完成")