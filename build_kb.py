"""
构建知识库（使用测试文档）
"""

import sys
sys.path.insert(0, '.')

from langchain_community.document_loaders import DirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

print("=" * 60)
print("构建知识库")
print("=" * 60)

# 文档目录
docs_dir = "data/documents/apifox"

# 加载文档
print(f"\n1. 加载文档从: {docs_dir}")
loader = DirectoryLoader(docs_dir, glob="**/*.md")
documents = loader.load()

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

# 初始化嵌入模型
print("\n3. 初始化嵌入模型（中文）")
print("   模型: shibing624/text2vec-base-chinese")
print("   首次运行需要下载模型，请稍候...")

embeddings = HuggingFaceEmbeddings(
    model_name="shibing624/text2vec-base-chinese",
    model_kwargs={'device': 'cpu'},
    encode_kwargs={'normalize_embeddings': True}
)

# 创建向量数据库
print("\n4. 创建向量数据库")
print("   保存到: data/vectordb")

vectorstore = Chroma.from_documents(
    documents=splits,
    embedding=embeddings,
    persist_directory="data/vectordb"
)

print(f"   向量数据库已创建!")

# 统计信息
collection = vectorstore.get()
print(f"\n5. 统计信息")
print(f"   总文档数: {len(collection.get('ids', []))}")

# 测试检索
print("\n6. 测试检索")
test_query = "接口测试失败怎么办？"
print(f"   查询: {test_query}")

results = vectorstore.similarity_search_with_score(test_query, k=3)

print(f"   找到 {len(results)} 个相关文档:\n")

for i, (doc, score) in enumerate(results, 1):
    print(f"   文档 {i} (相似度: {score:.4f}):")
    print(f"   {doc.page_content[:100]}...")
    print()

print("=" * 60)
print("✅ 知识库构建完成!")
print("=" * 60)
print("\n下一步:")
print("1. 测试知识库检索")
print("2. 测试问题分类")
print("3. 测试完整流程")
