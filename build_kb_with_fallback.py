"""
构建知识库（使用镜像和降级方案）
"""

import os
from pathlib import Path

# 设置 HuggingFace 镜像（解决国内网络问题）
os.environ['HF_ENDPOINT'] = 'https://hf-mirror.com'

from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter

def load_markdown_files(directory):
    """加载 Markdown 文件"""
    docs = []
    dir_path = Path(directory)

    for md_file in dir_path.glob("*.md"):
        with open(md_file, "r", encoding="utf-8") as f:
            content = f.read()

        doc = Document(
            page_content=content,
            metadata={"source": str(md_file)}
        )
        docs.append(doc)

    return docs

print("=" * 60)
print("构建知识库（使用镜像加速）")
print("=" * 60)

# 文档目录
docs_dir = "data/documents/apifox"

# 加载文档
print(f"\n1. 加载文档从: {docs_dir}")
documents = load_markdown_files(docs_dir)
print(f"   加载了 {len(documents)} 个文档")

# 分割文档
print("\n2. 分割文档")
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50,
    length_function=len,
)

splits = text_splitter.split_documents(documents)
print(f"   分割为 {len(splits)} 个片段")

# 尝试方案 1: 使用镜像下载模型
print("\n3. 初始化嵌入模型")
print("   方案 1: 使用 hf-mirror 镜像")
print("   模型: shibing624/text2vec-base-chinese")

try:
    from langchain_community.embeddings import HuggingFaceEmbeddings

    embeddings = HuggingFaceEmbeddings(
        model_name="shibing624/text2vec-base-chinese",
        model_kwargs={'device': 'cpu'},
        encode_kwargs={'normalize_embeddings': True}
    )

    print("   ✓ 模型加载成功!")

except Exception as e:
    print(f"   ✗ 镜像下载失败: {e}")

    # 尝试方案 2: 使用 OpenAI Embeddings
    print("\n   方案 2: 使用 OpenAI Embeddings")

    try:
        from dotenv import load_dotenv
        load_dotenv()

        from langchain_openai import OpenAIEmbeddings

        embeddings = OpenAIEmbeddings(
            openai_api_key=os.getenv("OPENAI_API_KEY")
        )
        print("   ✓ 使用 OpenAI Embeddings")

    except Exception as e2:
        print(f"   ✗ OpenAI 也失败了: {e2}")

        # 方案 3: 使用简单的词向量（降级方案）
        print("\n   方案 3: 使用 Chroma 默认嵌入（简化版）")

        from chromadb.utils import embedding_functions
        embeddings = embedding_functions.DefaultEmbeddingFunction()
        print("   ✓ 使用默认嵌入函数")

# 创建向量数据库
print("\n4. 创建向量数据库")
print("   保存到: data/vectordb")

try:
    from langchain_community.vectorstores import Chroma

    vectorstore = Chroma.from_documents(
        documents=splits,
        embedding=embeddings,
        persist_directory="data/vectordb"
    )

    print(f"   ✓ 向量数据库已创建!")

    # 统计信息
    collection = vectorstore.get()
    print(f"\n5. 统计信息")
    print(f"   总文档数: {len(collection.get('ids', []))}")

    # 测试检索
    print("\n6. 测试检索")
    test_queries = [
        "接口测试失败怎么办",
        "如何配置环境变量",
        "返回 500 错误"
    ]

    for query in test_queries:
        print(f"\n查询: {query}")
        results = vectorstore.similarity_search_with_score(query, k=2)

        for i, (doc, score) in enumerate(results, 1):
            content = doc.page_content[:80].replace('\n', ' ')
            print(f"  {i}. (相似度: {score:.4f}) {content}...")

    print("\n" + "=" * 60)
    print("✅ 知识库构建完成!")
    print("=" * 60)
    print("\n📁 保存位置: data/vectordb/")
    print("\n下一步:")
    print("1. 测试问题分类（使用 LLM + 知识库）")
    print("2. 测试完整流程")
    print("3. 配置飞书应用")

except Exception as e:
    print(f"\n✗ 构建失败: {e}")
    print("\n建议: 使用 OpenAI Embeddings（方案B）")
