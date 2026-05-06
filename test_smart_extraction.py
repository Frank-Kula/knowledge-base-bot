import os
import sys
from pathlib import Path

# 设置 PYTHONPATH
root_dir = Path(__file__).parent
sys.path.append(str(root_dir))

from src.classifiers.question_classifier import QuestionClassifier
from src.utils.config_loader import load_config

async def test_extraction():
    config = load_config("config/config.yaml")
    classifier = QuestionClassifier(config)
    
    history = [
        {"role": "user", "content": "我的 Apifox 打不开了，版本是 2.8.22"},
        {"role": "assistant", "content": "请问您的操作系统是什么？"},
        {"role": "user", "content": "Windows 11，一启动就崩溃"}
    ]
    
    target_fields = ["version", "os", "steps"]
    print(f"Testing extraction from history: {history}")
    
    result = await classifier.extract_info(history, target_fields)
    print("\nExtraction Result:")
    print(result)

if __name__ == "__main__":
    import asyncio
    asyncio.run(test_extraction())
