"""
简化版测试脚本 - 只测试 LLM 分类器
跳过知识库部分
"""

import asyncio
import sys
import os
from pathlib import Path
from dotenv import load_dotenv

# 设置 UTF-8 编码
os.environ['PYTHONIOENCODING'] = 'utf-8'
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

# 切换到项目根目录并加载 .env
project_root = Path(__file__).parent.parent
os.chdir(project_root)
load_dotenv(project_root / ".env")

print("=" * 60)
print("环境变量检查")
print("=" * 60)
print(f"工作目录: {os.getcwd()}")
print(f"LLM_API_KEY: {os.getenv('LLM_API_KEY', 'NOT SET')[:20]}...")
print(f"LLM_BASE_URL: {os.getenv('LLM_BASE_URL', 'NOT SET')}")
print(f"LLM_MODEL: {os.getenv('LLM_MODEL', 'NOT SET')}")

# 添加项目路径
sys.path.insert(0, str(project_root))
sys.path.insert(0, str(project_root / "src"))

from src.classifiers.question_classifier import QuestionClassifier
from src.utils.config_loader import load_config


async def test_classifier():
    """只测试分类器，不依赖知识库"""

    print("\n" + "=" * 60)
    print("测试 LLM 问题分类器")
    print("=" * 60)

    # 加载配置
    config = load_config()
    print("\n[1] 配置加载成功")
    print(f"    LLM Provider: {config.llm.provider}")
    print(f"    LLM Model: {config.llm.model}")
    print(f"    API Base URL: {config.llm.base_url}")

    # 初始化分类器
    classifier = QuestionClassifier(config)
    print("[2] 分类器初始化成功")

    # 测试用例
    test_cases = [
        {
            "name": "Bug - 接口报错",
            "question": "接口测试返回500错误，点击发送就报错",
            "context": "",
            "additional_info": {"version": "2.5.0", "environment": "Web端"}
        },
        {
            "name": "Feature - 导出功能需求",
            "question": "希望能支持导出Word格式文档，目前只能导出Markdown",
            "context": "",
            "additional_info": {"user_scenario": "需要给客户发API文档"}
        },
        {
            "name": "Usage - 使用咨询",
            "question": "请问怎么设置全局变量？在项目里找不到这个功能",
            "context": "",
            "additional_info": {}
        }
    ]

    # 测试每个用例
    for i, test_case in enumerate(test_cases, 1):
        print(f"\n{'='*60}")
        print(f"测试用例 {i}: {test_case['name']}")
        print(f"{'='*60}")
        print(f"问题: {test_case['question']}")

        print("\n正在调用 LLM 分类...")

        try:
            classification = await classifier.classify(
                question=test_case["question"],
                context=test_case["context"],
                additional_info=test_case["additional_info"]
            )

            print(f"\n[OK] 分类结果:")
            print(f"   类型: {classification['type']}")
            print(f"   置信度: {classification['confidence'] * 100:.1f}%")
            print(f"   理由: {classification['reason']}")
            if classification['suggested_answer']:
                answer = classification['suggested_answer']
                print(f"   建议回答: {answer[:150]}..." if len(answer) > 150 else f"   建议回答: {answer}")

        except Exception as e:
            print(f"\n[FAIL] 分类失败: {e}")
            import traceback
            traceback.print_exc()

    print("\n" + "=" * 60)
    print("测试完成!")
    print("=" * 60)


if __name__ == "__main__":
    asyncio.run(test_classifier())