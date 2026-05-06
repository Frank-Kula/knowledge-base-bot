"""
测试 BUG 关键词扫描器
"""

import sys
from pathlib import Path
from dotenv import load_dotenv

# 加载环境变量
load_dotenv(Path(__file__).parent.parent / '.env')

sys.path.insert(0, str(Path(__file__).parent.parent))

from src.watchers.bug_keyword_watcher import BugKeywordWatcher
from loguru import logger


def test_keywords():
    """测试关键词分析"""
    watcher = BugKeywordWatcher()

    # 测试 BUG 关键词匹配
    test_messages = [
        {"content": "Apifox 打开就报错了，提示连接失败", "message_id": "test_1"},
        {"content": "希望能支持导出 PDF 格式", "message_id": "test_2"},
        {"content": "导入数据的时候白屏了，没有任何提示", "message_id": "test_3"},
        {"content": "今天的天气不错", "message_id": "test_4"},
        {"content": "接口请求超时，返回 500 错误", "message_id": "test_5"},
    ]

    print("\n=== 测试关键词分析 ===")
    for msg in test_messages:
        analysis = watcher.analyze_message(msg)
        print(f"\n消息: {msg['content']}")
        print(f"  类型: {analysis['type']}")
        print(f"  置信度: {analysis['confidence']:.1%}")
        print(f"  关键词: {analysis['keywords']}")
        print(f"  原因: {analysis['reason']}")


def test_scan_once():
    """测试单次扫描（需要搜索权限）"""
    watcher = BugKeywordWatcher()

    print("\n=== 测试单次扫描 ===")
    try:
        result = watcher.scan_once()
        print(f"扫描结果: {result}")
    except Exception as e:
        print(f"扫描失败（可能缺少权限）: {e}")


if __name__ == "__main__":
    logger.info("开始测试 BUG 关键词扫描器")

    # 测试关键词分析
    test_keywords()

    # 测试扫描（需要授权）
    test_scan_once()

    logger.info("测试完成")