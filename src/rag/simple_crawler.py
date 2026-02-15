"""
简化的 Apifox 文档爬虫
最小依赖，只使用 requests 和 BeautifulSoup
"""

import asyncio
import sys
from pathlib import Path
from urllib.parse import urljoin, urlparse
import time

try:
    import httpx
    from bs4 import BeautifulSoup
except ImportError:
    print("请先安装依赖：pip install httpx beautifulsoup4")
    sys.exit(1)


class SimpleCrawler:
    """简单的文档爬虫"""

    def __init__(self, output_dir: str = "data/documents/apifox"):
        self.base_url = "https://docs.apifox.com/"
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.visited_urls = set()
        self.url_queue = [self.base_url]

    async def crawl(self, max_pages: int = 50):
        """爬取文档"""
        print(f"开始爬取 Apifox 文档，最大页面数: {max_pages}")

        async with httpx.AsyncClient(timeout=30.0, follow_redirects=True) as client:
            count = 0

            while self.url_queue and count < max_pages:
                url = self.url_queue.pop(0)

                if url in self.visited_urls:
                    continue

                print(f"[{count+1}/{max_pages}] 爬取: {url}")

                try:
                    await self.crawl_page(url, client)
                    self.visited_urls.add(url)
                    count += 1
                    time.sleep(1)  # 避免过快请求

                except Exception as e:
                    print(f"  ✗ 失败: {e}")

            print(f"\n✓ 爬取完成！共爬取 {count} 个页面")

    async def crawl_page(self, url: str, client):
        """爬取单个页面"""
        response = await client.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        # 提取标题
        title = self.extract_title(soup) or "未命名"

        # 提取内容
        content = self.extract_content(soup)

        # 转换为 Markdown（简化版）
        markdown = self.to_markdown(content, title, url)

        # 保存文件
        self.save_file(title, url, markdown)

        # 提取链接
        self.extract_links(soup, url)

    def extract_title(self, soup):
        """提取标题"""
        for tag in ["h1", "title"]:
            elem = soup.find(tag)
            if elem:
                return elem.get_text().strip()
        return None

    def extract_content(self, soup):
        """提取主要内容"""
        # 移除不需要的元素
        for tag in soup.find_all(["script", "style", "nav", "footer", "header"]):
            tag.decompose()

        # 查找主要内容
        for selector in ["main", "article", "[class*='content']", "[class*='doc']"]:
            elem = soup.select_one(selector)
            if elem:
                return elem

        return soup.body

    def to_markdown(self, soup, title, url):
        """转换为 Markdown"""
        lines = []
        lines.append(f"# {title}\n")
        lines.append(f"**来源**: {url}\n")
        lines.append("---\n")

        # 简化的 Markdown 转换
        for tag in soup.find_all(['h2', 'h3', 'p', 'ul', 'ol', 'pre', 'code']):
            if tag.name == 'h2':
                lines.append(f"\n## {tag.get_text().strip()}\n")
            elif tag.name == 'h3':
                lines.append(f"\n### {tag.get_text().strip()}\n")
            elif tag.name == 'p':
                text = tag.get_text().strip()
                if text:
                    lines.append(f"{text}\n")
            elif tag.name == 'pre':
                code = tag.get_text()
                lines.append(f"\n```\n{code}\n```\n")

        return "\n".join(lines)

    def extract_links(self, soup, base_url):
        """提取链接"""
        for link in soup.find_all("a", href=True):
            href = link["href"]
            full_url = urljoin(base_url, href)

            # 只处理同域名的链接
            if urlparse(full_url).netloc == urlparse(self.base_url).netloc:
                if full_url not in self.visited_urls and full_url not in self.url_queue:
                    self.url_queue.append(full_url)

    def save_file(self, title, url, content):
        """保存文件"""
        # 清理标题
        title = "".join(c for c in title if c.isalnum() or c in (" ", "-", "_")).strip()
        if not title:
            title = "未命名"

        filepath = self.output_dir / f"{title}.md"

        # 如果文件已存在，添加序号
        counter = 1
        while filepath.exists():
            filepath = self.output_dir / f"{title}_{counter}.md"
            counter += 1

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)

        print(f"  ✓ 保存: {filepath.name}")


async def main():
    """主函数"""
    print("=" * 60)
    print("Apifox 文档爬虫（简化版）")
    print("=" * 60)

    crawler = SimpleCrawler()
    await crawler.crawl(max_pages=50)

    print("\n✓ 所有文档已保存到 data/documents/apifox/")


if __name__ == "__main__":
    asyncio.run(main())
