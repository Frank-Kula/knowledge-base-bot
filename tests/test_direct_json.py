"""
直接测试 subprocess 调用 lark-cli 发送交互卡片
"""

import subprocess
import json
import sys
import io

# Windows 编码兼容
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

# 测试 1: 纯英文 JSON
print("=== 测试 1: 纯英文 JSON ===")
card_json_en = json.dumps({
    "config": {"wide_screen_mode": True},
    "header": {
        "template": "red",
        "title": {"content": "[BUG] Alert (Test Group)", "tag": "plain_text"}
    },
    "elements": [
        {
            "tag": "div",
            "fields": [
                {"is_short": True, "text": {"tag": "lark_md", "content": "**Source:**\nTest"}},
                {"is_short": True, "text": {"tag": "lark_md", "content": "**User:**\nTestUser"}}
            ]
        }
    ]
}, ensure_ascii=False)

cmd = [
    "C:\\Users\\hr\\AppData\\Roaming\\npm\\lark-cli.cmd",
    "im", "+messages-send",
    "--as", "bot",
    "--chat-id", "oc_9181c1f2869b0ec0af937f5c6f9a82aa",
    "--msg-type", "interactive",
    "--content", card_json_en
]

result = subprocess.run(
    cmd,
    capture_output=True,
    text=True,
    timeout=30,
    encoding='utf-8',
    errors='replace'
)

print(f"Return code: {result.returncode}")
print(f"Stdout: {result.stdout[:200] if result.stdout else 'None'}")
print(f"Stderr: {result.stderr}")

# 测试 2: 中文 JSON (ensure_ascii=False)
print("\n=== 测试 2: 中文 JSON ===")
card_json_cn = json.dumps({
    "config": {"wide_screen_mode": True},
    "header": {
        "template": "red",
        "title": {"content": "[BUG] 测试卡片", "tag": "plain_text"}
    },
    "elements": [
        {
            "tag": "div",
            "text": {"tag": "lark_md", "content": "**测试内容**"}
        }
    ]
}, ensure_ascii=False)

cmd2 = [
    "C:\\Users\\hr\\AppData\\Roaming\\npm\\lark-cli.cmd",
    "im", "+messages-send",
    "--as", "bot",
    "--chat-id", "oc_9181c1f2869b0ec0af937f5c6f9a82aa",
    "--msg-type", "interactive",
    "--content", card_json_cn
]

result2 = subprocess.run(
    cmd2,
    capture_output=True,
    text=True,
    timeout=30,
    encoding='utf-8',
    errors='replace'
)

print(f"Return code: {result2.returncode}")
print(f"Stdout: {result2.stdout[:200] if result2.stdout else 'None'}")
print(f"Stderr: {result2.stderr}")