"""
Apifox 帮助文档爬虫
爬取 https://docs.apifox.com/ 并转换为 Markdown
"""

import asyncio
import time
from pathlib import Path
from urllib.parse import urljoin, urlparse
from loguru import logger

import httpx
from bs4 import BeautifulSoup
from markdownify import markdownify as md


class ApifoxDocsCrawler:
    """Apifox 文档爬虫"""

    def __init__(self, output_dir: str = "data/documents/apifox"):
        self.base_url = "https://docs.apifox.com/"
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

        # 已爬取的 URL
        self.visited_urls = set()

        # 要爬取的 URL 队列
        self.url_queue = []

        # HTTP 客户端
        self.client = None

    async def init_client(self):
        """初始化 HTTP 客户端"""
        self.client = httpx.AsyncClient(
            headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
            },
            timeout=30.0,
            follow_redirects=True
        )

    async def close_client(self):
        """关闭 HTTP 客户端"""
        if self.client:
            await self.client.aclose()

    async def crawl(self, max_pages: int = 50):
        """
        开始爬取

        Args:
            max_pages: 最大爬取页面数
        """
        await self.init_client()

        try:
            # 从首页开始
            self.url_queue.append(self.base_url)

            count = 0
            while self.url_queue and count < max_pages:
                url = self.url_queue.pop(0)

                if url in self.visited_urls:
                    continue

                logger.info(f"爬取页面 ({count+1}/{max_pages}): {url}")

                try:
                    await self.crawl_page(url)
                    self.visited_urls.add(url)
                    count += 1

                    # 延迟，避免过快请求
                    await asyncio.sleep(1)

                except Exception as e:
                    logger.error(f"爬取页面失败 {url}: {e}")

            logger.info(f"爬取完成，共爬取 {count} 个页面")

        finally:
            await self.close_client()

    async def crawl_page(self, url: str):
        """
        爬取单个页面

        Args:
            url: 页面 URL
        """
        try:
            # 获取页面内容
            response = await self.client.get(url)
            response.raise_for_status()

            html = response.text
            soup = BeautifulSoup(html, "html.parser")

            # 提取标题
            title = self.extract_title(soup)

            # 提取内容
            content = self.extract_content(soup)

            # 转换为 Markdown
            markdown_content = md(content)

            # 保存到文件
            self.save_page(url, title, markdown_content)

            # 提取链接并添加到队列
            self.extract_links(soup, url)

        except Exception as e:
            logger.error(f"处理页面失败 {url}: {e}")
            raise

    def extract_title(self, soup: BeautifulSoup) -> str:
        """提取页面标题"""
        # 尝试多种方式获取标题
        title_selectors = [
            "h1",
            "title",
            "[class*='title']",
            "[class*='Title']"
        ]

        for selector in title_selectors:
            element = soup.select_one(selector)
            if element:
                title = element.get_text().strip()
                # 清理标题中的特殊字符
                title = "".join(c for c in title if c.isalnum() or c in (" ", "-", "_", "/"))
                return title

        return "未命名页面"

    def extract_content(self, soup: BeautifulSoup) -> str:
        """提取页面主要内容"""
        # 移除不需要的元素
        for element in soup.find_all(["script", "style", "nav", "footer", "header"]):
            element.decompose()

        # 尝试找到主内容区域
        content_selectors = [
            "main",
            "article",
            "[class*='content']",
            "[class*='Content']",
            "[class*='doc']",
            "[class*='article']",
            "body"
        ]

        for selector in content_selectors:
            element = soup.select_one(selector)
            if element:
                return str(element)

        # 如果没找到，返回整个 body
        return str(soup.body)

    def extract_links(self, soup: BeautifulSoup, base_url: str):
        """提取页面中的链接"""
        links = soup.find_all("a", href=True)

        for link in links:
            href = link["href"]

            # 构建完整 URL
            full_url = urljoin(base_url, href)

            # 只处理同域名的链接
            if urlparse(full_url).netloc == urlparse(self.base_url).netloc:
                # 过滤掉已访问的和非 HTML 的链接
                if (
                    full_url not in self.visited_urls
                    and full_url not in self.url_queue
                    and not full_url.endswith(".pdf")
                    and not full_url.endswith(".zip")
                    and not "#" in full_url  # 跳过锚点链接
                ):
                    self.url_queue.append(full_url)

    def save_page(self, url: str, title: str, content: str):
        """
        保存页面到文件

        Args:
            url: 页面 URL
            title: 页面标题
            content: Markdown 内容
        """
        try:
            # 构建文件路径
            parsed_url = urlparse(url)
            path = parsed_url.path.strip("/")

            if not path:
                path = "index"

            # 创建文件名
            filename = f"{title}.md"
            filepath = self.output_dir / filename

            # 如果文件已存在，添加序号
            counter = 1
            while filepath.exists():
                filepath = self.output_dir / f"{title}_{counter}.md"
                counter += 1

            # 写入文件
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(f"# {title}\n\n")
                f.write(f"**来源**: {url}\n\n")
                f.write("---\n\n")
                f.write(content)

            logger.info(f"保存文件: {filepath}")

        except Exception as e:
            logger.error(f"保存文件失败: {e}")


async def main():
    """主函数"""
    logger.info("开始爬取 Apifox 帮助文档...")

    crawler = ApifoxDocsCrawler()
    await crawler.crawl(max_pages=100)

    logger.info("爬取完成！")


if __name__ == "__main__":
    import sys
    from loguru import logger as loguru_logger

    # 配置日志
    loguru_logger.remove()
    loguru_logger.add(
        sys.stderr,
        format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <level>{message}</level>",
        level="INFO"
    )

    # 运行爬虫
    asyncio.run(main())
