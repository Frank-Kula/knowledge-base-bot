"""
直接测试 subprocess 执行 bash 命令字符串
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

json_file = Path(".test_cmd_card.json")
json_file.write_text(card_json, encoding='utf-8')

print(f"JSON 文件已创建: {json_file.name}")

# 测试 1: 使用 bash -c 执行命令字符串（添加 PATH）
print("\n=== 测试 1: bash -c 命令字符串（添加 PATH） ===")
npm_path = "/c/Users/hr/AppData/Roaming/npm"
cmd_str = f'export PATH="{npm_path}:$PATH" && lark-cli im +messages-send --as bot --chat-id oc_9181c1f2869b0ec0af937f5c6f9a82aa --msg-type interactive --content "$(cat {json_file.name})"'

# 获取当前工作目录
cwd = os.getcwd()

# 设置环境变量
env = os.environ.copy()
env["PATH"] = f"C:\\Users\\hr\\AppData\\Roaming\\npm;{env.get('PATH', '')}"

result = subprocess.run(
    ["bash", "-c", cmd_str],
    capture_output=True,
    text=True,
    timeout=30,
    encoding='utf-8',
    cwd=cwd,
    env=env
)

print(f"返回码: {result.returncode}")
print(f"输出: {result.stdout[:200] if result.stdout else 'None'}")
print(f"错误: {result.stderr}")

# 测试 2: 检查 bash 是否可用
print("\n=== 测试 2: 检查 bash ===")
result2 = subprocess.run(
    ["bash", "--version"],
    capture_output=True,
    text=True,
    timeout=5,
    encoding='utf-8'
)
print(f"Bash version: {result2.stdout[:100] if result2.stdout else 'None'}")

# 清理
json_file.unlink(missing_ok=True)