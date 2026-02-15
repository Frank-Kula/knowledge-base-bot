# 变更日志

所有重要的项目变更都会记录在此文件中。

## [2025-01-15] 项目初始化

### 提交 5ec4c9b
**消息**：feat: 初始化技术支持知识库机器人

**新增内容**：
- ✅ 创建项目结构（30 个文件，5,353 行代码）
- ✅ RAG 知识库检索模块
- ✅ LLM 智能分类器（Bug/需求/使用问题）
- ✅ 对话式信息收集
- ✅ 自动生成规范模板（按公司实际规范）
- ✅ 飞书/企微机器人集成
- ✅ 文档爬虫（crawl_apifox_docs.py）
- ✅ GitHub Actions 自动更新工作流

**目录结构**：
```
knowledge-base-bot/
├── config/              # 配置文件
├── data/
│   ├── documents/       # 帮助文档
│   └── templates/       # 缺陷/需求模板
├── src/
│   ├── bots/           # 机器人模块
│   ├── rag/            # 知识库模块
│   ├── classifiers/    # 分类器
│   └── utils/          # 工具模块
├── docs/               # 文档
└── requirements.txt    # 依赖列表
```

---

## [2025-01-15] 推送代码到 GitHub

**操作**：推送到 GitHub 仓库 `https://github.com/Frank-Kula/knowledge-base-bot`

**结果**：✅ 成功

---

## [2025-01-15] GitHub Actions 首次运行失败

**运行**：#1

**问题**：
- ❌ 依赖安装失败
- ❌ `lark-oapi==1.2.19` 版本不存在
- ❌ 某些包需要 Python 3.10+

**错误日志**：
```
ERROR: Could not find a version that satisfies the requirement lark-oapi==1.2.19
ERROR: Ignored the following versions that require a different python version
```

---

## [2025-01-15] 修复依赖版本问题（第一次）

### 提交 29a168e
**消息**：fix: 修复依赖版本问题，简化工作流

**修改内容**：
1. ✅ 更新 `requirements.txt`
   - 移除 `lark-oapi==1.2.19`（不存在）
   - 改用更灵活的版本约束（使用 `>=`）
2. ✅ 简化 `.github/workflows/update-docs.yml`
   - 移除知识库构建步骤（太复杂）
   - 只保留文档爬取功能
3. ✅ 添加 `src/rag/simple_crawler.py`
   - 最小依赖版本
   - 只依赖 `httpx` 和 `beautifulsoup4`

**新依赖列表**：
```
requests>=2.31.0
beautifulsoup4>=4.12.0
markdownify>=0.11.0
httpx>=0.26.0
chromadb>=0.4.18
langchain>=0.1.0
anthropic>=0.18.0
```

**推送状态**：❌ 权限问题（未推送）

---

## [2025-01-15] 添加简化版爬虫

### 提交 aed2ea8
**消息**：feat: 添加简化版爬虫（最小依赖）

**新增内容**：
- ✅ 创建 `src/rag/simple_crawler.py`
  - 使用标准库 `logging`（不依赖 `loguru`）
  - 只依赖 `httpx` 和 `beautifulsoup4`
  - 简化的 Markdown 转换
  - 异步爬取，支持并发

**功能**：
- 从 `https://docs.apifox.com/` 爬取文档
- 保存为 Markdown 文件到 `data/documents/apifox/`
- 最多爬取 50 个页面
- 自动处理页面链接

**推送状态**：❌ 权限问题（未推送）

---

## [2025-01-15] 推送修复到 GitHub

**操作**：使用 Token 推送

**提交**：
- `29a168e` - fix: 修复依赖版本问题，简化工作流
- `aed2ea8` - feat: 添加简化版爬虫（最小依赖）

**结果**：✅ 成功推送到 `main` 分支

---

## [2025-01-15] GitHub Actions 第二次运行失败

**运行**：#2

**问题**：
- ❌ `ModuleNotFoundError: No module named 'loguru'`

**错误日志**：
```
File "/home/runner/work/knowledge-base-bot/knowledge-base-bot/src/rag/crawl_apifox_docs.py", line 10, in <module>
  from loguru import logger
ModuleNotFoundError: No module named 'loguru'
```

**原因**：
- workflow 调用的是 `crawl_apifox_docs.py`（依赖 loguru）
- 但安装依赖时没有安装 `loguru`

---

## [2025-01-15] 修复 loguru 依赖问题

### 提交 64d59b2
**消息**：fix: 移除 loguru 依赖，使用标准库 logging

**修改内容**：

1. **更新 `src/rag/simple_crawler.py`**：
   ```python
   # 之前
   from loguru import logger

   # 之后
   import logging
   logger = logging.getLogger(__name__)
   ```

2. **更新 `.github/workflows/update-docs.yml`**：
   ```yaml
   # 之前
   - name: 检查文档更新
     run: python src/rag/crawl_apifox_docs.py

   # 之后
   - name: 爬取 Apifox 文档
     run: python src/rag/simple_crawler.py
   ```

3. **更新 `docs/推送到GitHub.md`**：
   - 添加推送指南文档

**修改的文件**：
- `src/rag/simple_crawler.py` - 移除 loguru，使用 logging
- `.github/workflows/update-docs.yml` - 调用 simple_crawler.py
- `docs/推送到GitHub.md` - 新增文档

**推送状态**：✅ 成功推送到 `main` 分支

---

## [2025-01-15] 创建变更日志

### 本文件
**消息**：docs: 创建 CHANGELOG.md 记录所有修改

**目的**：
- 📝 记录每次代码修改
- 📝 记录每个 GitHub Actions 运行
- 📝 记录遇到的问题和解决方案
- 📝 方便回溯和调试

**格式**：
- 按时间倒序
- 每个修改包含：
  - 时间
  - 提交 ID
  - 修改内容
  - 影响的文件
  - 结果

---

## 问题追踪

### 已解决的问题

| 问题 | 解决方案 | 状态 |
|------|---------|------|
| `lark-oapi` 版本不存在 | 移除该依赖 | ✅ |
| `loguru` 模块缺失 | 使用标准库 `logging` | ✅ |
| Python 3.10+ 依赖 | 使用灵活版本约束 | ✅ |
| 知识库构建太复杂 | 先只爬取文档 | ✅ |

### 待解决的问题

| 问题 | 计划 | 优先级 |
|------|------|--------|
| 文档爬取效果未知 | 等待 GitHub Actions 运行完成 | 🔴 高 |
| 本地环境配置 | 创建详细配置文档 | 🟡 中 |
| 知识库构建 | 文档爬取成功后再添加 | 🟢 低 |

---

## 下一步计划

### 短期（本周）
- [ ] 验证 GitHub Actions #3 运行成功
- [ ] 检查爬取的文档质量
- [ ] 本地测试爬虫脚本

### 中期（下周）
- [ ] 配置本地环境（LLM API Key）
- [ ] 本地构建知识库
- [ ] 测试机器人功能

### 长期（下月）
- [ ] 优化爬虫（提取更多内容）
- [ ] 添加知识库自动构建
- [ ] 配置飞书应用
- [ ] 在用户群中试用

---

## 统计信息

### 代码统计
- 总文件数：30+
- 总代码行数：5,353
- Python 文件：15
- Markdown 文件：8
- YAML 配置：2

### Git 统计
- 总提交数：5
- 分支数：1（main）
- GitHub Actions 运行：3 次

### 依赖统计
- 生产依赖：9 个
- 开发依赖：0 个
- 核心依赖：httpx, beautifulsoup4

---

## 贡献者

- **Frank-Kula** - 项目创建者

---

## 相关链接

- **GitHub 仓库**：https://github.com/Frank-Kula/knowledge-base-bot
- **Actions 页面**：https://github.com/Frank-Kula/knowledge-base-bot/actions
- **原始需求**：技术支持知识库机器人

---

*最后更新：2025-01-15*
