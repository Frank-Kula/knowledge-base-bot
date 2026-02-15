"""
自动更新 Apifox 文档
支持定时任务、增量更新、变更检测
"""

import asyncio
import hashlib
import json
from datetime import datetime
from pathlib import Path
from loguru import logger

from crawl_apifox_docs import ApifoxDocsCrawler
from knowledge_base import KnowledgeBase
from utils.config_loader import load_config


class AutoDocsUpdater:
    """文档自动更新器"""

    def __init__(self, output_dir: str = "data/documents/apifox"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

        # 元数据文件
        self.metadata_file = self.output_dir / ".metadata.json"

        # 加载元数据
        self.metadata = self._load_metadata()

    def _load_metadata(self) -> dict:
        """加载元数据"""
        if self.metadata_file.exists():
            with open(self.metadata_file, "r", encoding="utf-8") as f:
                return json.load(f)
        return {
            "last_update": None,
            "pages": {},
            "version": "1.0"
        }

    def _save_metadata(self):
        """保存元数据"""
        with open(self.metadata_file, "w", encoding="utf-8") as f:
            json.dump(self.metadata, f, ensure_ascii=False, indent=2)

    def _get_file_hash(self, filepath: Path) -> str:
        """计算文件哈希值"""
        with open(filepath, "rb") as f:
            return hashlib.md5(f.read()).hexdigest()

    async def check_updates(self) -> dict:
        """
        检查文档更新

        Returns:
            更新统计信息
        """
        logger.info("检查文档更新...")

        crawler = ApifoxDocsCrawler(str(self.output_dir))
        await crawler.init_client()

        try:
            stats = {
                "total": 0,
                "updated": 0,
                "new": 0,
                "unchanged": 0,
                "deleted": 0,
                "failed": 0
            }

            # 获取所有已爬取的页面
            known_pages = set(self.metadata["pages"].keys())

            # 遍历文档目录
            for md_file in self.output_dir.glob("*.md"):
                try:
                    # 从文件中提取 URL
                    with open(md_file, "r", encoding="utf-8") as f:
                        content = f.read()
                        # 查找来源 URL
                        for line in content.split("\n"):
                            if line.startswith("**来源**"):
                                url = line.split(":")[1].strip()
                                break
                        else:
                            continue

                    stats["total"] += 1

                    # 获取最新内容
                    response = await crawler.client.get(url)
                    response.raise_for_status()

                    # 计算新内容的哈希
                    soup = crawler.extract_content(response.text)
                    new_content = crawler.markdownify(soup)
                    new_hash = hashlib.md5(new_content.encode()).hexdigest()

                    # 检查是否有更新
                    if url not in self.metadata["pages"]:
                        # 新页面
                        stats["new"] += 1
                        logger.info(f"新页面: {url}")

                        # 更新文件
                        with open(md_file, "w", encoding="utf-8") as f:
                            f.write(new_content)

                        # 更新元数据
                        self.metadata["pages"][url] = {
                            "hash": new_hash,
                            "last_update": datetime.now().isoformat(),
                            "file": md_file.name
                        }

                    elif self.metadata["pages"][url]["hash"] != new_hash:
                        # 内容有更新
                        stats["updated"] += 1
                        logger.info(f"更新页面: {url}")

                        # 备份旧文件
                        backup_file = md_file.with_suffix(".md.backup")
                        md_file.rename(backup_file)

                        # 更新文件
                        with open(md_file, "w", encoding="utf-8") as f:
                            f.write(new_content)

                        # 更新元数据
                        self.metadata["pages"][url] = {
                            "hash": new_hash,
                            "last_update": datetime.now().isoformat(),
                            "file": md_file.name
                        }

                    else:
                        # 未更新
                        stats["unchanged"] += 1

                    known_pages.discard(url)

                except Exception as e:
                    logger.error(f"检查页面失败 {md_file}: {e}")
                    stats["failed"] += 1

            # 检查删除的页面
            for url in known_pages:
                stats["deleted"] += 1
                logger.warning(f"页面已删除: {url}")
                del self.metadata["pages"][url]

            # 更新时间戳
            self.metadata["last_update"] = datetime.now().isoformat()
            self._save_metadata()

            logger.info(f"检查完成: {stats}")
            return stats

        finally:
            await crawler.close_client()

    async def full_update(self, max_pages: int = 100):
        """
        全量更新

        Args:
            max_pages: 最大爬取页面数
        """
        logger.info("开始全量更新...")

        # 备份现有文档
        backup_dir = self.output_dir.parent / "apifox_backup"
        if self.output_dir.exists():
            import shutil
            if backup_dir.exists():
                shutil.rmtree(backup_dir)
            shutil.copytree(self.output_dir, backup_dir)
            logger.info(f"已备份到: {backup_dir}")

        # 爬取最新文档
        crawler = ApifoxDocsCrawler(str(self.output_dir))
        await crawler.crawl(max_pages=max_pages)

        # 更新元数据
        self.metadata["last_update"] = datetime.now().isoformat()
        self._save_metadata()

        logger.info("全量更新完成")

    async def smart_update(self, force: bool = False):
        """
        智能更新（检查 + 按需更新）

        Args:
            force: 是否强制全量更新
        """
        if force or not self.metadata["last_update"]:
            # 首次运行或强制更新
            await self.full_update()
        else:
            # 检查更新
            stats = await self.check_updates()

            # 如果有大量更新，建议全量更新
            if stats["updated"] + stats["new"] > 10:
                logger.info("检测到大量更新，建议全量更新")
                await self.full_update()

            # 如果更新后需要重建知识库
            if stats["updated"] + stats["new"] > 0:
                logger.info("文档已更新，需要重建知识库")
                return True

        return False


async def rebuild_knowledge_base():
    """重建知识库"""
    logger.info("开始重建知识库...")

    config = load_config()
    kb = KnowledgeBase(config)

    # 删除旧的向量数据库
    import shutil
    vectordb_path = Path("data/vectordb")
    if vectordb_path.exists():
        shutil.rmtree(vectordb_path)
        logger.info("已删除旧的向量数据库")

    # 初始化并重建
    await kb.initialize()
    await kb.close()

    logger.info("知识库重建完成")


async def main():
    """主函数"""
    import argparse

    parser = argparse.ArgumentParser(description="自动更新 Apifox 文档")
    parser.add_argument(
        "--mode",
        type=str,
        choices=["check", "full", "smart"],
        default="smart",
        help="更新模式: check(检查), full(全量), smart(智能)"
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="强制全量更新"
    )
    parser.add_argument(
        "--rebuild-kb",
        action="store_true",
        help="更新后重建知识库"
    )

    args = parser.parse_args()

    updater = AutoDocsUpdater()

    if args.mode == "check":
        stats = await updater.check_updates()
        print(f"\n更新统计:")
        print(f"  总计: {stats['total']}")
        print(f"  新增: {stats['new']}")
        print(f"  更新: {stats['updated']}")
        print(f"  未变: {stats['unchanged']}")
        print(f"  删除: {stats['deleted']}")
        print(f"  失败: {stats['failed']}")

    elif args.mode == "full":
        await updater.full_update()

    elif args.mode == "smart":
        need_rebuild = await updater.smart_update(force=args.force)
        if need_rebuild and args.rebuild_kb:
            await rebuild_knowledge_base()


if __name__ == "__main__":
    asyncio.run(main())
