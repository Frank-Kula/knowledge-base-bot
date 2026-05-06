"""
直接测试交互卡片发送
"""

import subprocess
import json
import sys
import io
from pathlib import Path
import os
import re

# Windows 编码兼容
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

def win_path_to_bash(win_path):
    """将 Windows 路径转换为 bash 格式"""
    # D:\path -> /d/path
    match = re.match(r'^([A-Z]):(.*)$', win_path)
    if match:
        drive = match.group(1).lower()
        rest = match.group(2).replace('\\', '/')
        return f'/{drive}{rest}'
    return win_path.replace('\\', '/')

# 创建卡片 JSON
card_json = json.dumps({
    "config": {"wide_screen_mode": True},
    "header": {
        "template": "red",
        "title": {"content": "Test Bug Card", "tag": "plain_text"}
    },
    "elements": [
        {
            "tag": "div",
            "fields": [
                {"is_short": True, "text": {"tag": "lark_md", "content": "**Source:**\nTest"}},
                {"is_short": True, "text": {"tag": "lark_md", "content": "**User:**\nTestUser"}}
            ]
        },
        {"tag": "hr"},
        {
            "tag": "div",
            "text": {"tag": "lark_md", "content": "**Test Card**"}
        }
    ]
}, ensure_ascii=False)

# 写入临时文件
cwd = os.getcwd()
content_file = Path(cwd) / ".test_card_direct.json"
content_file.write_text(card_json, encoding='utf-8')

# bash 格式的绝对路径
file_bash = win_path_to_bash(str(content_file))

print(f"Windows path: {content_file}")
print(f"Bash file path: {file_bash}")

# 使用 lark-cli 直接（通过 PATH）
cmd_str = f'lark-cli im +messages-send --as bot --chat-id oc_9181c1f2869b0ec0af937f5c6f9a82aa --msg-type interactive --content "$(cat {file_bash})"'

print(f"Command: {cmd_str}")

# 使用 bash 执行
result = subprocess.run(
    ["bash", "-c", cmd_str],
    capture_output=True,
    text=True,
    timeout=60,
    encoding='utf-8'
)

print(f"Return code: {result.returncode}")
print(f"Output: {result.stdout}")
print(f"Error: {result.stderr}")

# 清理
content_file.unlink(missing_ok=True)