"""
逐步测试找出问题所在
"""

import subprocess
import json
import sys
import io
import platform

# Windows 编码兼容
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

def test_card(card_json, name):
    print(f"\n=== {name} ===")
    print(f"JSON 长度: {len(card_json)}")

    cmd = [
        "C:\\Users\\hr\\AppData\\Roaming\\npm\\lark-cli.cmd",
        "im", "+messages-send",
        "--as", "bot",
        "--chat-id", "oc_9181c1f2869b0ec0af937f5c6f9a82aa",
        "--msg-type", "interactive",
        "--content", card_json
    ]

    result = subprocess.run(
        cmd,
        capture_output=True,
        text=True,
        timeout=30,
        encoding='utf-8',
        errors='replace'
    )

    print(f"返回码: {result.returncode}")
    if result.returncode == 0:
        print("成功!")
    else:
        print(f"错误: {result.stderr}")

# 测试 1: 简单 JSON（无换行）
test_card(json.dumps({
    "config": {"wide_screen_mode": True},
    "header": {"template": "red", "title": {"content": "Test", "tag": "plain_text"}},
    "elements": [{"tag": "div", "text": {"tag": "lark_md", "content": "**Test**"}}]
}, ensure_ascii=False), "测试 1: 简单 JSON（无换行）")

# 测试 2: JSON 带换行符
test_card(json.dumps({
    "config": {"wide_screen_mode": True},
    "header": {"template": "red", "title": {"content": "Test", "tag": "plain_text"}},
    "elements": [{"tag": "div", "text": {"tag": "lark_md", "content": "**Test**\nLine2"}}]
}, ensure_ascii=False), "测试 2: JSON 带换行符")

# 测试 3: JSON 带中文
test_card(json.dumps({
    "config": {"wide_screen_mode": True},
    "header": {"template": "red", "title": {"content": "测试", "tag": "plain_text"}},
    "elements": [{"tag": "div", "text": {"tag": "lark_md", "content": "**测试内容**"}}]
}, ensure_ascii=False), "测试 3: JSON 带中文")

# 测试 4: JSON 带中文和换行
test_card(json.dumps({
    "config": {"wide_screen_mode": True},
    "header": {"template": "red", "title": {"content": "测试", "tag": "plain_text"}},
    "elements": [{"tag": "div", "text": {"tag": "lark_md", "content": "**测试**\n第二行"}}]
}, ensure_ascii=False), "测试 4: JSON 带中文和换行")

# 测试 5: JSON 带引号嵌套
test_card(json.dumps({
    "config": {"wide_screen_mode": True},
    "header": {"template": "red", "title": {"content": "Test", "tag": "plain_text"}},
    "elements": [{"tag": "div", "text": {"tag": "lark_md", "content": "> \"quoted text\""}}]
}, ensure_ascii=False), "测试 5: JSON 带引号嵌套")

# 测试 6: JSON 带所有特殊元素
test_card(json.dumps({
    "config": {"wide_screen_mode": True},
    "header": {"template": "red", "title": {"content": "测试", "tag": "plain_text"}},
    "elements": [
        {"tag": "div", "fields": [{"is_short": True, "text": {"tag": "lark_md", "content": "**标题**\n内容"}}]},
        {"tag": "hr"},
        {"tag": "div", "text": {"tag": "lark_md", "content": "> \"引用\""}}
    ]
}, ensure_ascii=False), "测试 6: JSON 带所有特殊元素")