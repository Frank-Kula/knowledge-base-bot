"""
文档更新调度器
支持多种调度策略
"""

import asyncio
import schedule
from datetime import datetime
from loguru import logger

from auto_update_docs import AutoDocsUpdater
from knowledge_base import KnowledgeBase
from utils.config_loader import load_config


class DocsUpdateScheduler:
    """文档更新调度器"""

    def __init__(self):
        self.updater = AutoDocsUpdater()
        self.config = load_config()

    async def scheduled_update(self):
        """定时更新任务"""
        logger.info("=" * 50)
        logger.info(f"开始执行定时更新任务: {datetime.now()}")
        logger.info("=" * 50)

        try:
            # 智能更新
            need_rebuild = await self.updater.smart_update()

            # 如果有更新，重建知识库
            if need_rebuild:
                logger.info("检测到文档更新，重建知识库...")
                await self._rebuild_knowledge_base()

            logger.info("定时更新任务完成")

        except Exception as e:
            logger.error(f"定时更新任务失败: {e}")

    async def _rebuild_knowledge_base(self):
        """重建知识库"""
        import shutil
        from pathlib import Path

        # 删除旧的向量数据库
        vectordb_path = Path("data/vectordb")
        if vectordb_path.exists():
            shutil.rmtree(vectordb_path)
            logger.info("已删除旧的向量数据库")

        # 重建
        kb = KnowledgeBase(self.config)
        await kb.initialize()
        await kb.close()

        logger.info("知识库重建完成")

    def run_scheduler(self):
        """运行调度器"""
        # 设置定时任务
        schedule.every().day.at("02:00").do(
            lambda: asyncio.run(self.scheduled_update())
        )

        # 也可以设置为每小时检查一次
        # schedule.every().hour.do(
        #     lambda: asyncio.run(self.scheduled_update())
        # )

        logger.info("调度器已启动，等待下次执行...")
        logger.info("下次执行时间: 每天 02:00")

        # 持续运行
        while True:
            schedule.run_pending()
            import time
            time.sleep(60)  # 每分钟检查一次


async def main():
    """主函数"""
    import argparse

    parser = argparse.ArgumentParser(description="文档更新调度器")
    parser.add_argument(
        "--mode",
        type=str,
        choices=["scheduler", "once"],
        default="once",
        help="运行模式: scheduler(持续运行), once(执行一次)"
    )

    args = parser.parse_args()

    scheduler = DocsUpdateScheduler()

    if args.mode == "scheduler":
        # 持续运行模式
        scheduler.run_scheduler()
    else:
        # 执行一次
        await scheduler.scheduled_update()


if __name__ == "__main__":
    asyncio.run(main())
