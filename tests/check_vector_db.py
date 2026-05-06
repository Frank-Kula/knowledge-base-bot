"""
检查向量数据库质量
"""

from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
import os

load_dotenv()

print("=" * 80)
print("向量数据库质量检查")
print("=" * 80)

embeddings = OpenAIEmbeddings(openai_api_key=os.getenv('OPENAI_API_KEY'))
vectorstore = Chroma(persist_directory='data/vectordb', embedding_function=embeddings)

collection = vectorstore.get()

print(f"\n总向量数: {len(collection['ids'])}")
print(f"唯一文档数: {len(set([m.get('source', '') for m in collection.get('metadatas', [{}]*len(collection['ids']))]))}")

# 检查前5个片段
print("\n" + "=" * 80)
print("前5个向量片段详情")
print("=" * 80)

for i in range(min(5, len(collection['ids']))):
    print(f"\n片段 {i+1}:")
    print(f"内容: {collection['documents'][i][:100]}...")

    metadata = collection['metadatas'][i] if collection.get('metadatas') else {}
    print(f"元数据: {metadata}")

    # 检查内容特征
    content = collection['documents'][i]
    lines = content.split('\n')
    print(f"行数: {len(lines)}")
    print(f"字符数: {len(content)}")

print("\n" + "=" * 80)
print("分块策略评估")
print("=" * 80)

# 统计所有片段的长度
lengths = [len(doc) for doc in collection['documents']]
if lengths:
    print(f"平均字符数: {sum(lengths) / len(lengths):.0f}")
    print(f"最短: {min(lengths)} 字符")
    print(f"最长: {max(lengths)} 字符")
else:
    print("没有找到文档片段")

print("\n" + "=" * 80)
print("元数据评估")
print("=" * 80)

# 检查元数据完整性
metadatas = collection.get('metadatas', [])
if metadatas:
    has_source = sum(1 for m in metadatas if m.get('source'))
    has_title = sum(1 for m in metadatas if m.get('title'))
    has_chunk = sum(1 for m in metadatas if m.get('chunk'))

    print(f"有source元数据: {has_source}/{len(metadatas)}")
    print(f"有title元数据: {has_title}/{len(metadatas)}")
    print(f"有chunk元数据: {has_chunk}/{len(metadatas)}")
else:
    print("没有元数据")

print("\n" + "=" * 80)
print("结论")
print("=" * 80)

if metadatas and metadatas[0].get('source'):
    print("✅ 有基本元数据（source）")
else:
    print("❌ 缺少元数据，只有source")

if lengths and max(lengths) - min(lengths) > 1000:
    print("⚠️ 片段长度差异大，可能需要优化分块策略")
else:
    print("✅ 片段长度相对均匀")

if len(collection['ids']) < 50:
    print("⚠️ 向量数量较少，知识库覆盖可能不足")
else:
    print("✅ 向量数量充足")
