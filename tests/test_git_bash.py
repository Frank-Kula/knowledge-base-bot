"""
测试使用 Git Bash 发送卡片
"""

import subprocess
import json
import sys
import io
import os
from pathlib import Path

# Windows 编码兼容
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

# 创建 JSON 文件
card_json = json.dumps({
    "config": {"wide_screen_mode": True},
    "header": {"template": "red", "title": {"content": "[BUG] Test", "tag": "plain_text"}},
    "elements": [{"tag": "div", "text": {"tag": "lark_md", "content": "**Test**"}}]
}, ensure_ascii=False)

json_file = Path(".test_git_bash.json")
json_file.write_text(card_json, encoding='utf-8')

print(f"JSON 文件已创建: {json_file.name}")

# 使用 Git Bash
git_bash = "D:\\software-all\\Git\\Git\\usr\\bin\\bash.exe"
npm_path = "/c/Users/hr/AppData/Roaming/npm"

cmd_str = f'export PATH="{npm_path}:$PATH" && lark-cli im +messages-send --as bot --chat-id oc_9181c1f2869b0ec0af937f5c6f9a82aa --msg-type interactive --content "$(cat {json_file.name})"'

print(f"使用 Git Bash: {git_bash}")
print(f"命令: {cmd_str[:100]}...")

# 设置环境变量
cwd = os.getcwd()
env = os.environ.copy()

result = subprocess.run(
    [git_bash, "-c", cmd_str],
    capture_output=True,
    text=True,
    timeout=30,
    encoding='utf-8',
    cwd=cwd,
    env=env
)

print(f"\n返回码: {result.returncode}")
print(f"输出: {result.stdout[:300] if result.stdout else 'None'}")
print(f"错误: {result.stderr}")

# 清理
json_file.unlink(missing_ok=True)