"""
直接测试 bash subprocess 调用
"""

import subprocess
import sys
import os

# 测试 1: 直接使用 bash -c
print("测试 1: bash -c 直接调用")
cmd_str = 'lark-cli im +messages-send --as bot --chat-id oc_9181c1f2869b0ec0af937f5c6f9a82aa --msg-type interactive --content "$(cat .test_simple.json)"'
print(f"命令: {cmd_str}")

try:
    result = subprocess.run(
        ["bash", "-c", cmd_str],
        capture_output=True,
        text=True,
        timeout=30,
        encoding='utf-8'
    )
    print(f"返回码: {result.returncode}")
    print(f"输出: {result.stdout}")
    print(f"错误: {result.stderr}")
except subprocess.TimeoutExpired:
    print("超时!")

# 测试 2: 使用 shell=True
print("\n测试 2: shell=True 调用")
cmd_str2 = 'lark-cli im +messages-send --as bot --chat-id oc_9181c1f2869b0ec0af937f5c6f9a82aa --msg-type interactive --content "$(cat .test_simple.json)"'

try:
    result = subprocess.run(
        cmd_str2,
        shell=True,
        capture_output=True,
        text=True,
        timeout=30,
        encoding='utf-8'
    )
    print(f"返回码: {result.returncode}")
    print(f"输出: {result.stdout}")
    print(f"错误: {result.stderr}")
except subprocess.TimeoutExpired:
    print("超时!")

# 测试 3: 不使用 shell 替换
print("\n测试 3: 直接传递 JSON 内容")
import json
with open('.test_simple.json', 'r', encoding='utf-8') as f:
    json_content = f.read()

try:
    result = subprocess.run(
        ["lark-cli", "im", "+messages-send", "--as", "bot",
         "--chat-id", "oc_9181c1f2869b0ec0af937f5c6f9a82aa",
         "--msg-type", "interactive",
         "--content", json_content],
        capture_output=True,
        text=True,
        timeout=30,
        encoding='utf-8'
    )
    print(f"返回码: {result.returncode}")
    print(f"输出: {result.stdout}")
    print(f"错误: {result.stderr}")
except subprocess.TimeoutExpired:
    print("超时!")