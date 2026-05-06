"""
测试完整的问题分类流程（LLM + 知识库）
"""

import os
from dotenv import load_dotenv
from openai import OpenAI

# 加载环境变量
load_dotenv()

# 初始化
client = OpenAI(
    api_key=os.getenv("LLM_API_KEY"),
    base_url="https://api.deepseek.com"
)

print("=" * 60)
print("测试问题分类（LLM + 知识库）")
print("=" * 60)

# 模拟知识库检索（简化版）
def search_knowledge_base(query, top_k=3):
    """从知识库检索相关文档"""
    from langchain_community.vectorstores import Chroma
    from langchain_openai import OpenAIEmbeddings

    embeddings = OpenAIEmbeddings(
        openai_api_key=os.getenv("OPENAI_API_KEY")
    )

    vectorstore = Chroma(
        persist_directory="data/vectordb",
        embedding_function=embeddings
    )

    results = vectorstore.similarity_search(query, k=top_k)
    return results

# 测试用例
test_cases = [
    {
        "question": "接口测试失败了，返回500错误",
        "description": "在测试接口时，服务器返回500内部错误"
    },
    {
        "question": "希望能批量导出接口文档",
        "description": "需要一次性导出多个接口的文档为PDF"
    },
    {
        "question": "怎么在 Apifox 中设置环境变量？",
        "description": "不知道如何在 Apifox 中配置base_url"
    },
    {
        "question": "数据库连接超时",
        "description": "连接数据库时一直超时无法连接"
    }
]

for i, test_case in enumerate(test_cases, 1):
    print(f"\n{'=' * 60}")
    print(f"测试 {i}/{len(test_cases)}")
    print(f"{'=' * 60}")
    print(f"问题：{test_case['question']}")
    print(f"描述：{test_case['description']}")

    # 1. 知识库检索
    print("\n[1] 知识库检索...")
    try:
        docs = search_knowledge_base(test_case['question'], top_k=2)
        print(f"    找到 {len(docs)} 个相关文档")

        context = ""
        for j, doc in enumerate(docs, 1):
            content = doc.page_content.replace('\n', ' ')[:150]
            print(f"    文档 {j}: {content}...")
            context += f"\n### 文档 {j}\n{doc.page_content}\n"

    except Exception as e:
        print(f"    检索失败: {e}")
        context = "未找到相关文档"

    # 2. 问题分类
    print("\n[2] 问题分类...")
    prompt = f"""
你是技术支持专家，需要根据用户反馈判断问题类型。

## 用户问题
{test_case['question']}

## 补充信息
{test_case['description']}

## 帮助文档相关内容
{context}

## 判断标准
1. **Bug（缺陷）**：产品功能与预期设计不符，或出现了错误/报错
   - 例如：功能异常、崩溃、报错、性能问题

2. **需求（Feature）**：产品缺少某个功能，或现有功能无法满足工作流
   - 例如：新功能建议、功能改进、工作流优化

3. **使用问题（Usage）**：用户未找到正确的操作方式
   - 例如：不知道如何配置、找不到某个功能

请严格按照以上标准判断，返回 JSON 格式：
{{
  "type": "bug|feature|usage",
  "confidence": 0.0-1.0,
  "reason": "判断理由",
  "suggested_answer": "基于文档的建议回答（如果是使用问题）"
}}
"""

    try:
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0.3,
            max_tokens=1000
        )

        result_text = response.choices[0].message.content
        print(f"    分类完成！")

        # 解析 JSON
        import json
        start = result_text.find("{")
        end = result_text.rfind("}") + 1

        if start != -1 and end != -1:
            result = json.loads(result_text[start:end])

            print(f"\n[3] 分类结果")
            print(f"    类型: {result['type']}")
            print(f"    置信度: {result['confidence']}")
            print(f"    理由: {result['reason']}")

            if result['type'] == 'usage':
                print(f"    建议回答: {result.get('suggested_answer', '')}")

        else:
            print(f"\n    无法解析 JSON，原始回复：")
            print(f"    {result_text}")

    except Exception as e:
        print(f"    分类失败: {e}")

print("\n" + "=" * 60)
print("测试完成！")
print("=" * 60)
print("\n下一步:")
print("1. 测试完整的对话流程（信息收集 + 分类 + 模板生成）")
print("2. 配置飞书应用")
print("3. 部署到生产环境")
