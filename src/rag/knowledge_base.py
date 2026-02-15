"""
知识库检索模块 (RAG)
基于帮助文档构建向量数据库
"""

from typing import List, Dict
from pathlib import Path
from loguru import logger

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.document_loaders import (
    DirectoryLoader,
    TextLoader,
    BSHTMLLoader
)
from langchain.schema import Document


class KnowledgeBase:
    """知识库管理器"""

    def __init__(self, config):
        self.config = config
        self.embeddings = None
        self.vectorstore = None
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=config.rag.chunk_size,
            chunk_overlap=config.rag.chunk_overlap,
            length_function=len,
        )

    async def initialize(self):
        """初始化知识库"""
        try:
            logger.info("初始化知识库...")

            # 初始化嵌入模型
            self.embeddings = HuggingFaceEmbeddings(
                model_name="shibing624/text2vec-base-chinese",
                model_kwargs={'device': 'cpu'},
                encode_kwargs={'normalize_embeddings': True}
            )

            # 检查向量数据库是否存在
            vectordb_path = Path("data/vectordb")
            if vectordb_path.exists():
                # 加载现有数据库
                logger.info("加载现有向量数据库...")
                self.vectorstore = Chroma(
                    persist_directory=str(vectordb_path),
                    embedding_function=self.embeddings
                )
                logger.info(f"向量数据库加载成功，文档数: {len(self.vectorstore.get())}")
            else:
                logger.warning("向量数据库不存在，请先运行 build_knowledge_base.py")

        except Exception as e:
            logger.error(f"知识库初始化失败: {e}")
            raise

    async def search(self, query: str, top_k: int = None) -> List[Document]:
        """
        搜索相关文档

        Args:
            query: 查询文本
            top_k: 返回前K个结果，默认使用配置值

        Returns:
            相关文档列表
        """
        if not self.vectorstore:
            logger.warning("向量数据库未初始化")
            return []

        try:
            k = top_k or self.config.rag.top_k

            # 相似度搜索
            results = self.vectorstore.similarity_search_with_score(
                query,
                k=k
            )

            # 过滤低分结果
            filtered_results = [
                (doc, score) for doc, score in results
                if score >= self.config.rag.score_threshold
            ]

            logger.info(f"搜索查询: {query}, 结果数: {len(filtered_results)}")

            # 只返回文档
            return [doc for doc, score in filtered_results]

        except Exception as e:
            logger.error(f"搜索失败: {e}")
            return []

    async def search_with_context(
        self,
        query: str,
        top_k: int = None
    ) -> str:
        """
        搜索并返回格式化的上下文

        Args:
            query: 查询文本
            top_k: 返回前K个结果

        Returns:
            格式化的上下文字符串
        """
        docs = await self.search(query, top_k)

        if not docs:
            return "未找到相关文档"

        context_parts = []
        for i, doc in enumerate(docs, 1):
            context_parts.append(f"### 文档 {i}\n{doc.page_content}\n")

        return "\n".join(context_parts)

    async def add_documents(self, documents: List[Document]):
        """
        添加文档到知识库

        Args:
            documents: 文档列表
        """
        if not self.vectorstore:
            logger.error("向量数据库未初始化")
            return

        try:
            # 分割文档
            splits = self.text_splitter.split_documents(documents)

            # 添加到向量数据库
            self.vectorstore.add_documents(splits)

            logger.info(f"成功添加 {len(splits)} 个文档片段")

        except Exception as e:
            logger.error(f"添加文档失败: {e}")

    async def delete_documents(self, ids: List[str]):
        """
        删除文档

        Args:
            ids: 文档ID列表
        """
        if not self.vectorstore:
            logger.error("向量数据库未初始化")
            return

        try:
            self.vectorstore.delete(ids)
            logger.info(f"成功删除 {len(ids)} 个文档")

        except Exception as e:
            logger.error(f"删除文档失败: {e}")

    def get_stats(self) -> Dict:
        """
        获取知识库统计信息

        Returns:
            统计信息
        """
        if not self.vectorstore:
            return {"status": "not_initialized"}

        collection = self.vectorstore.get()
        return {
            "status": "ok",
            "total_documents": len(collection.get('ids', [])),
            "embeddings_model": "shibing624/text2vec-base-chinese"
        }

    async def close(self):
        """关闭知识库"""
        if self.vectorstore:
            # Chroma 会自动持久化
            logger.info("知识库已关闭")


def build_knowledge_base():
    """
    构建知识库
    从帮助文档构建向量数据库
    """
    import argparse
    from langchain_community.document_loaders import DirectoryLoader

    parser = argparse.ArgumentParser(description="构建知识库")
    parser.add_argument(
        "--docs-dir",
        type=str,
        default="data/documents",
        help="文档目录路径"
    )
    args = parser.parse_args()

    logger.info("开始构建知识库...")

    # 加载文档
    docs_dir = Path(args.docs_dir)
    if not docs_dir.exists():
        logger.error(f"文档目录不存在: {docs_dir}")
        return

    # 加载所有文档
    loader = DirectoryLoader(
        str(docs_dir),
        glob="**/*.md",
        loader_cls=TextLoader,
        loader_kwargs={"autodetect_encoding": True}
    )
    documents = loader.load()

    logger.info(f"加载了 {len(documents)} 个文档")

    # 初始化知识库
    from utils.config_loader import load_config
    config = load_config()
    kb = KnowledgeBase(config)

    # 初始化嵌入模型
    kb.embeddings = HuggingFaceEmbeddings(
        model_name="shibing624/text2vec-base-chinese",
        model_kwargs={'device': 'cpu'},
        encode_kwargs={'normalize_embeddings': True}
    )

    # 分割文档
    logger.info("分割文档...")
    splits = kb.text_splitter.split_documents(documents)
    logger.info(f"分割为 {len(splits)} 个片段")

    # 创建向量数据库
    logger.info("创建向量数据库...")
    kb.vectorstore = Chroma.from_documents(
        documents=splits,
        embedding=kb.embeddings,
        persist_directory="data/vectordb"
    )

    logger.info("知识库构建完成！")


if __name__ == "__main__":
    build_knowledge_base()
