# 推送到 GitHub - 最后一步

## 📦 当前状态

✅ Git 仓库已初始化
✅ 所有文件已提交（30 个文件，5353 行代码）
✅ GitHub Actions 配置已就绪
✅ 只需推送到 GitHub！

## 🚀 推送到 GitHub（二选一）

### 方法 A：使用 GitHub CLI（推荐，最快）

```bash
# 1. 安装 GitHub CLI（如果未安装）
# Windows: winget install GitHub.cli
# Mac: brew install gh
# Linux: https://cli.github.com/

# 2. 登录 GitHub
gh auth login

# 按提示选择：
# - What account? → GitHub.com
# - What protocol? → HTTPS
# - Authenticate? → Login with a web browser

# 3. 创建仓库并推送
gh repo create knowledge-base-bot --public --source=. --remote=origin --push
```

**就这么简单！** 🎉

---

### 方法 B：通过 GitHub 网页（直观）

#### 1. 创建 GitHub 仓库

访问：https://github.com/new

填写信息：
- **Repository name**: `knowledge-base-bot`
- **Description**: `技术支持知识库机器人`
- **Public / Private**: 选择一个（Public 免费，Private 需要 GitHub 账号）
- **不要勾选** "Add a README file"
- **不要勾选** "Add .gitignore"

点击 **"Create repository"**

#### 2. 复制仓库 URL

创建后会看到：
```bash
git remote add origin https://github.com/你的用户名/knowledge-base-bot.git
git branch -M main
git push -u origin main
```

#### 3. 在项目目录执行

```bash
cd knowledge-base-bot

# 添加远程仓库（替换成你的用户名）
git remote add origin https://github.com/你的用户名/knowledge-base-bot.git

# 推送代码
git branch -M main
git push -u origin main
```

**如果是私有仓库**，需要认证：
```bash
# 使用 GitHub Personal Access Token
# 1. 访问：https://github.com/settings/tokens
# 2. 生成新 Token（权限：repo）
# 3. 使用 Token 作为密码

git push -u origin main
# Username: 你的 GitHub 用户名
# Password: ghp_xxxxxxxxxxxxxxxxxxxx（你的 Token）
```

## ✅ 验证推送成功

```bash
# 查看远程仓库
git remote -v

# 查看分支
git branch -a
```

访问：`https://github.com/你的用户名/knowledge-base-bot`

你应该能看到：
- ✅ 所有源代码文件
- ✅ 配置文件
- ✅ 文档
- ✅ GitHub Actions 工作流

## 🤖 启动 GitHub Actions

### 自动激活

推送代码后，GitHub Actions 会自动激活！

访问：`https://github.com/你的用户名/knowledge-base-bot/actions`

### 手动触发第一次运行

1. 在 Actions 页面
2. 左侧选择 **"Update Apifox Docs"**
3. 点击右侧 **"Run workflow"**
4. 选择分支：**main**
5. 点击 **"Run workflow"** 按钮

### 查看运行结果

等待几分钟（首次运行需要安装依赖），然后：
- 点击运行记录查看详情
- 可以看到每一步的输出
- 查看是否成功爬取文档

## 📊 查看工作流状态

### 在仓库主页添加徽章

编辑 `README.md`，添加：

```markdown
![Docs Update](https://github.com/你的用户名/knowledge-base-bot/actions/workflows/update-docs.yml/badge.svg)
```

### 使用 GitHub CLI 查看状态

```bash
# 列出所有运行
gh run list --repo knowledge-base-bot

# 查看最新运行
gh run view --repo knowledge-base-bot

# 查看运行日志
gh run view --repo knowledge-base-bot --log
```

## ⏰ 自动运行时间

默认配置：**每天 UTC 2:00**（北京时间 10:00）

如需修改，编辑 `.github/workflows/update-docs.yml`：

```yaml
on:
  schedule:
    # 北京时间每天凌晨 2 点
    - cron: '0 18 * * *'

    # 或每天早上 9 点
    # - cron: '0 1 * * *'
```

修改后提交并推送：

```bash
git add .github/workflows/update-docs.yml
git commit -m "config: 调整文档更新时间"
git push
```

## 🎯 下一步

### 1. 配置 .env 文件（重要！）

```bash
# 复制环境变量模板
cp .env.example .env

# 编辑并填写：
# - LLM_API_KEY（必需）
# - FEISHU_APP_ID（必需）
# - FEISHU_APP_SECRET（必需）
# - 其他配置...
```

### 2. 首次运行机器人

```bash
# 安装依赖
pip install -r requirements.txt

# 爬取文档
python src/rag/crawl_apifox_docs.py

# 构建知识库
python src/rag/knowledge_base.py

# 测试运行
python src/bots/main.py
```

### 3. 配置飞书应用

按照 `docs/前置准备.md` 中的步骤：
1. 创建飞书应用
2. 开启机器人权限
3. 创建多维表格
4. 配置 Webhook

### 4. 开始使用

在飞书群中发送测试消息：
```
接口测试失败了怎么办？
```

## 📝 完整流程总结

```
1. 初始化 Git     ✅ (已完成)
   ↓
2. 提交代码       ✅ (已完成)
   ↓
3. 创建 GitHub 仓库 ← 你在这里
   ↓
4. 推送代码
   ↓
5. GitHub Actions 自动运行
   ↓
6. 文档自动更新
   ↓
7. 享受自动化！🎉
```

## 💡 小贴士

### 克隆到其他地方

```bash
# 在另一台电脑上
git clone https://github.com/你的用户名/knowledge-base-bot.git
cd knowledge-base-bot
pip install -r requirements.txt
```

### 查看更新内容

```bash
# 拉取最新更改
git pull origin main

# 查看更新的文档
git log --oneline --grep="docs"

# 查看文档变化
git diff HEAD~1 HEAD data/documents/
```

### 回滚到之前版本

```bash
# 查看历史版本
git log --oneline

# 回滚到特定版本
git checkout <commit-hash>
```

## 🆘 常见问题

### Q: 推送失败？

**A**: 检查远程仓库配置
```bash
git remote -v
# 如果不对，重新添加
git remote remove origin
git remote add origin https://github.com/你的用户名/knowledge-base-bot.git
```

### Q: Actions 不运行？

**A**: 确认 workflow 文件路径正确
```bash
# 应该是
.github/workflows/update-docs.yml
```

### Q: 如何停止自动更新？

**A**: 禁用 workflow
1. 访问 Actions 页面
2. 点击 "Update Apifox Docs"
3. 点击右侧 "..." → "Disable workflow"

## 🎉 完成后你将拥有

✅ 完整的技术支持机器人
✅ 自动更新的 Apifox 文档
✅ 完全免费的 CI/CD
✅ 代码和文档的版本控制
✅ 随时可以回滚的历史记录

---

**现在就推送代码，开始享受自动化吧！** 🚀

有任何问题随时问我。
