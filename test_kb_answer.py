"""
测试知识库智能回答功能
"""
import sys
import asyncio
from pathlib import Path

# 添加路径
root_dir = Path(__file__).parent
sys.path.insert(0, str(root_dir))
sys.path.insert(0, str(root_dir / "src"))

from dotenv import load_dotenv
load_dotenv(root_dir / ".env")

from rag.knowledge_base import KnowledgeBase
from utils.config_loader import load_config


async def test_kb_search():
    """测试知识库检索"""
    config = load_config(str(root_dir / "config" / "config.yaml"))
    kb = KnowledgeBase(config)

    print("初始化知识库...")
    await kb.initialize()

    # 测试问题
    test_questions = [
        "如何导出接口文档",
        "怎么导入 Swagger 文档",
        "接口测试怎么跑",
        "Mock 功能怎么用",
        "这个功能报错了怎么办",  # 预期无匹配或低置信度
    ]

    print("\n" + "="*60)
    print("知识库检索测试")
    print("="*60)

    for question in test_questions:
        print(f"\n问题: {question}")
        docs = await kb.search(question)
        print(f"匹配结果: {len(docs)} 个文档片段")

        if docs:
            # 显示第一个结果的摘要
            first_doc = docs[0]
            content_preview = first_doc.page_content[:200].replace('\n', ' ')
            print(f"最相关内容预览: {content_preview}...")

            # 获取完整上下文
            context = await kb.search_with_context(question)
            print(f"上下文长度: {len(context)} 字符")
        else:
            print("无匹配结果 → 应启动信息收集流程")


async def test_llm_answer():
    """测试 LLM 生成回答"""
    from anthropic import Anthropic
    import os

    config = load_config(str(root_dir / "config" / "config.yaml"))
    kb = KnowledgeBase(config)

    print("\n初始化知识库...")
    await kb.initialize()

    # 初始化 LLM client
    client_kwargs = {"api_key": config.llm.api_key}
    if config.llm.base_url:
        client_kwargs["base_url"] = config.llm.base_url
    llm_client = Anthropic(**client_kwargs)

    # 测试问题
    question = "如何导出接口文档"

    print(f"\n测试问题: {question}")

    # 检索知识库
    docs = await kb.search(question)
    if not docs:
        print("无匹配结果，无法测试 LLM 回答")
        return

    context = await kb.search_with_context(question)

    # 构建 prompt
    prompt = f"""你是 Apifox 技术支持助手。

用户问题：{question}

相关文档内容：
{context}

请基于以上文档内容，简洁准确地回答用户问题。
"""

    print("\n调用 LLM 生成回答...")
    response = llm_client.messages.create(
        model=config.llm.model,
        max_tokens=500,
        temperature=0.3,
        messages=[{"role": "user", "content": prompt}]
    )

    # 提取文本
    answer = ""
    for block in response.content:
        if getattr(block, 'type', None) == 'text':
            answer = block.text
            break

    print("\n" + "="*60)
    print("LLM 生成的回答:")
    print("="*60)
    print(answer)


async def main():
    print("="*60)
    print("知识库智能回答功能测试")
    print("="*60)

    await test_kb_search()
    await test_llm_answer()


if __name__ == "__main__":
    asyncio.run(main())