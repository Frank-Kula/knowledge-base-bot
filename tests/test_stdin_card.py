"""
测试 stdin 输入方式发送卡片
"""

import subprocess
import json
import sys
import io

# Windows 编码兼容
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

# 创建带引号的 JSON
card_json = json.dumps({
    "config": {"wide_screen_mode": True},
    "header": {"template": "red", "title": {"content": "Test", "tag": "plain_text"}},
    "elements": [{"tag": "div", "text": {"tag": "lark_md", "content": "> \"quoted text\""}}]
}, ensure_ascii=False)

print(f"JSON: {card_json}")

# 使用 stdin 输入
cmd = [
    "C:\\Users\\hr\\AppData\\Roaming\\npm\\lark-cli.cmd",
    "im", "+messages-send",
    "--as", "bot",
    "--chat-id", "oc_9181c1f2869b0ec0af937f5c6f9a82aa",
    "--msg-type", "interactive"
]

result = subprocess.run(
    cmd,
    input=card_json,  # 通过 stdin 输入 JSON
    capture_output=True,
    text=True,
    timeout=30,
    encoding='utf-8'
)

print(f"返回码: {result.returncode}")
print(f"输出: {result.stdout}")
print(f"错误: {result.stderr}")