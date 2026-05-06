"""
检查GitHub Actions爬虫状态和文档质量
"""

import os
import sys
from pathlib import Path
from datetime import datetime, timedelta

# 设置 UTF-8 编码输出
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

print("=" * 80)
print("GitHub Actions 爬虫状态检查")
print("=" * 80)

# 第1步：检查是否有爬取的文档
print("\n[第1步] 检查文档目录")
print("-" * 80)

docs_dir = Path("data/documents")
if not docs_dir.exists():
    print("[X] data/documents 目录不存在")
    print("\n建议：运行爬虫")
    print("  python src/rag/simple_crawler.py")
    sys.exit(1)

# 统计文档
all_docs = list(docs_dir.rglob("*.md"))
print(f"[OK] 找到 {len(all_docs)} 个Markdown文件")

# 按目录分类
dirs = {}
for doc in all_docs:
    parent_dir = doc.parent.name
    if parent_dir not in dirs:
        dirs[parent_dir] = []
    dirs[parent_dir].append(doc)

for dir_name, files in dirs.items():
    print(f"\n  {dir_name}/: {len(files)} 个文件")

# 第2步：检查GitHub Actions配置
print("\n[第2步] 检查GitHub Actions配置")
print("-" * 80)

workflow_file = Path(".github/workflows/update-docs.yml")
if workflow_file.exists():
    print("[OK] GitHub Actions 配置文件存在")
    print(f"   文件: {workflow_file}")

    with open(workflow_file, "r", encoding="utf-8") as f:
        content = f.read()
        if "simple_crawler.py" in content:
            print("[OK] 配置了爬虫脚本")
        if "schedule:" in content:
            print("[OK] 配置了定时任务（每天 UTC 2:00）")
        if "workflow_dispatch:" in content:
            print("[OK] 支持手动触发")
else:
    print("[X] GitHub Actions 配置文件不存在")

# 第3步：检查最近更新
print("\n[第3步] 检查文档更新时间")
print("-" * 80)

now = datetime.now()
recent_docs = []

for doc in all_docs:
    mtime = datetime.fromtimestamp(doc.stat().st_mtime)
    age = now - mtime
    recent_docs.append((doc, mtime, age))

recent_docs.sort(key=lambda x: x[1], reverse=True)

print("\n最近更新的文档（前5个）：")
for doc, mtime, age in recent_docs[:5]:
    age_str = ""
    if age.days > 0:
        age_str = f"{age.days}天前"
    elif age.seconds > 3600:
        hours = age.seconds // 3600
        age_str = f"{hours}小时前"
    else:
        minutes = age.seconds // 60
        age_str = f"{minutes}分钟前"

    print(f"  {doc.name:40} {mtime.strftime('%Y-%m-%d %H:%M')} ({age_str})")

# 第4步：检查文档质量
print("\n[第4步] 抽查文档质量")
print("-" * 80)

if recent_docs:
    # 随机选一个文档检查
    sample_doc = recent_docs[0][0]
    print(f"\n检查文档: {sample_doc.name}")
    print("-" * 40)

    with open(sample_doc, "r", encoding="utf-8") as f:
        content = f.read()

    lines = content.split('\n')
    print(f"总行数: {len(lines)}")
    print(f"字符数: {len(content)}")

    # 检查标题结构
    h1_count = content.count('\n# ')
    h2_count = content.count('\n## ')
    h3_count = content.count('\n### ')
    code_blocks = content.count('```')

    print(f"\n标题统计:")
    print(f"  一级标题 (#): {h1_count}")
    print(f"  二级标题 (##): {h2_count}")
    print(f"  三级标题 (###): {h3_count}")
    print(f"  代码块 (```): {code_blocks}")

    # 检查是否有原文链接
    if "**来源**:" in content or "**来源**:" in content:
        print("\n✅ 包含来源链接")

    if "https://docs.apifox.com/" in content:
        print("✅ 包含Apifox文档链接")

    # 显示前几行内容
    print(f"\n前10行内容:")
    print("-" * 40)
    for i, line in enumerate(lines[:10], 1):
        print(f"{i:2d}: {line}")

# 第5步：检查爬虫脚本
print("\n[第5步] 检查爬虫脚本")
print("-" * 80)

crawler_file = Path("src/rag/simple_crawler.py")
if crawler_file.exists():
    print("[OK] 爬虫脚本存在")
    print(f"   文件: {crawler_file}")

    with open(crawler_file, "r", encoding="utf-8") as f:
        content = f.read()
        if "docs.apifox.com" in content:
            print("[OK] 配置了Apifox文档URL")
        if "BeautifulSoup" in content:
            print("[OK] 使用BeautifulSoup解析HTML")
        if "Markdown" in content:
            print("[OK] 转换为Markdown格式")
else:
    print("[X] 爬虫脚本不存在")

# 第6步：总结和建议
print("\n" + "=" * 80)
print("总结与建议")
print("=" * 80)

if len(all_docs) <= 7:
    print("\n[!] 文档数量较少（只有测试文档）")
    print("\n可能原因:")
    print("  1. GitHub Actions从未成功运行")
    print("  2. 爬虫被Apifox网站阻止（403错误）")
    print("  3. 需要手动触发GitHub Actions")
    print("\n建议:")
    print("  1. 访问GitHub仓库Actions页面查看运行记录")
    print("  2. 手动触发一次爬取（workflow_dispatch）")
    print("  3. 或者手动运行爬虫:")
    print("     python src/rag/simple_crawler.py")
else:
    print("\n[OK] 文档数量正常")
    print(f"\n建议:")
    print("  1. 抽查几个文档，检查内容质量")
    print("  2. 重新构建向量数据库")
    print("  3. 测试检索效果")

print("\n" + "=" * 80)
print("如何查看GitHub Actions运行记录")
print("=" * 80)

print("\n1. 访问你的GitHub仓库")
print("2. 点击顶部的 'Actions' 标签")
print("3. 查看工作流 'Update Apifox Docs' 的运行记录")
print("4. 点击最近的运行查看详情")
print("5. 查看日志，是否有错误信息")

print("\n如何手动触发爬虫")
print("-" * 80)

print("\n方式1: 在GitHub Actions页面手动触发")
print("  1. 进入 'Update Apifox Docs' 工作流")
print("  2. 点击 'Run workflow' 按钮")
print("  3. 等待运行完成")

print("\n方式2: 本地手动运行")
print("  python src/rag/simple_crawler.py")
print("  # 然后手动提交到GitHub")

print("\n" + "=" * 80)
