"""
飞书机器人测试脚本
测试 _analyze_and_classify 方法
"""

import asyncio
import sys
from pathlib import Path

# 添加项目路径
sys.path.insert(0, str(Path(__file__).parent.parent))
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from src.rag.knowledge_base import KnowledgeBase
from src.classifiers.question_classifier import QuestionClassifier
from src.utils.config_loader import load_config
from src.utils.template_manager import TemplateManager
from src.bots.feishu_bot import FeishuBot


async def test_analyze_and_classify():
    """测试问题分析和分类流程"""

    print("=" * 50)
    print("测试飞书机器人 _analyze_and_classify 方法")
    print("=" * 50)

    # 加载配置
    config = load_config()
    print("\n[1] 配置加载成功")

    # 初始化组件
    kb = KnowledgeBase(config)
    await kb.initialize()
    print("[2] 知识库初始化成功")

    classifier = QuestionClassifier(config)
    print("[3] 分类器初始化成功")

    template_mgr = TemplateManager(config)
    print("[4] 模板管理器初始化成功")

    # 创建飞书机器人实例
    feishu_bot = FeishuBot(config, kb, classifier, template_mgr)
    print("[5] 飞书机器人初始化成功")

    # 模拟收集的数据
    test_cases = [
        {
            "name": "Bug 测试用例",
            "data": {
                "title": "接口测试返回500错误",
                "description": "接口测试返回500错误",
                "version": "2.5.0",
                "environment": "Web端",
                "steps": "1. 创建接口\n2. 点击发送\n3. 返回500错误",
                "expected": "正常返回200",
                "actual": "返回500错误",
                "reproducibility": "必现"
            }
        },
        {
            "name": "Feature 测试用例",
            "data": {
                "title": "希望能支持导出Word格式文档",
                "description": "希望能支持导出Word格式文档",
                "user_scenario": "在写API文档时，需要导出给客户查看",
                "current_status": "目前只能导出Markdown和HTML",
                "user_expectation": "支持导出Word格式"
            }
        },
        {
            "name": "Usage 测试用例",
            "data": {
                "title": "如何设置全局变量",
                "description": "如何设置全局变量",
                "version": "2.5.0",
                "environment": "客户端"
            }
        }
    ]

    # 测试每个用例
    for i, test_case in enumerate(test_cases, 1):
        print(f"\n{'='*50}")
        print(f"测试用例 {i}: {test_case['name']}")
        print(f"{'='*50}")

        # 模拟 chat_id 和 user_id
        test_chat_id = "test_chat_123"
        test_user_id = "test_user_456"

        # 由于 send_message 会真正发送消息，我们用 mock 或只测试分类逻辑
        # 这里只测试分类器
        collected_data = test_case["data"]
        question = collected_data.get("title", "") or collected_data.get("description", "")

        print(f"\n问题: {question}")
        print("\n正在检索知识库...")

        # 检索知识库
        context = await kb.search_with_context(question)
        print(f"知识库检索结果:\n{context[:500]}..." if len(context) > 500 else f"知识库检索结果:\n{context}")

        print("\n正在调用 LLM 分类...")

        # 调用分类器
        classification = await classifier.classify(
            question=question,
            context=context,
            additional_info=collected_data
        )

        print(f"\n分类结果:")
        print(f"  - 类型: {classification['type']}")
        print(f"  - 置信度: {classification['confidence'] * 100:.1f}%")
        print(f"  - 理由: {classification['reason']}")
        print(f"  - 建议回答: {classification['suggested_answer'][:200]}..." if len(classification['suggested_answer']) > 200 else f"  - 建议回答: {classification['suggested_answer']}")

        # 测试模板渲染
        template_content = template_mgr.render_template(
            classification["type"],
            title=question[:50],
            submitter=test_user_id,
            confidence=int(classification["confidence"] * 100),
            reason=classification["reason"],
            suggested_answer=classification["suggested_answer"],
            **collected_data
        )

        print(f"\n生成的工单模板:")
        print("-" * 40)
        print(template_content)
        print("-" * 40)

    print("\n" + "=" * 50)
    print("测试完成！")
    print("=" * 50)

    # 关闭知识库
    await kb.close()


async def test_knowledge_base_search():
    """单独测试知识库检索"""
    print("=" * 50)
    print("测试知识库检索")
    print("=" * 50)

    config = load_config()
    kb = KnowledgeBase(config)
    await kb.initialize()

    # 查看知识库状态
    stats = kb.get_stats()
    print(f"\n知识库状态: {stats}")

    # 测试几个搜索
    queries = [
        "如何发送接口请求",
        "Mock API 怎么用",
        "导入 Swagger 文档",
        "团队协作功能"
    ]

    for query in queries:
        print(f"\n查询: {query}")
        results = await kb.search(query, top_k=3)
        if results:
            for j, doc in enumerate(results, 1):
                print(f"  结果 {j}: {doc.page_content[:100]}...")
        else:
            print("  未找到相关文档")

    await kb.close()


if __name__ == "__main__":
    # 运行测试
    # asyncio.run(test_analyze_and_classify())

    # 或单独测试知识库
    asyncio.run(test_knowledge_base_search())