# GitHub Actions 设置指南

## 🚀 5 分钟快速设置

### 第一步：初始化 Git 仓库

```bash
# 进入项目目录
cd knowledge-base-bot

# 初始化 Git 仓库
git init

# 添加所有文件
git add .

# 首次提交
git commit -m "feat: 初始化技术支持机器人

- 添加 RAG 知识库检索
- 添加问题分类器
- 添加飞书/企微机器人
- 添加文档自动更新
"
```

### 第二步：创建 GitHub 仓库

#### 方法 A：通过 GitHub CLI（推荐）

```bash
# 安装 GitHub CLI（如果未安装）
# Windows: winget install GitHub.cli
# Mac: brew install gh
# Linux: 参考https://cli.github.com/

# 登录 GitHub
gh auth login

# 创建仓库并推送
gh repo create knowledge-base-bot --public --source=. --remote=origin --push
```

#### 方法 B：通过 GitHub 网页

1. 访问 https://github.com/new
2. 填写信息：
   - Repository name: `knowledge-base-bot`
   - Description: `技术支持知识库机器人`
   - 选择 Public 或 Private（Private 更安全）
   - 不要勾选 "Add a README file"
3. 点击 "Create repository"
4. 复制仓库 URL

```bash
# 添加远程仓库
git remote add origin https://github.com/你的用户名/knowledge-base-bot.git

# 推送代码
git branch -M main
git push -u origin main
```

### 第三步：验证 GitHub Actions

1. 访问：`https://github.com/你的用户名/knowledge-base-bot/actions`
2. 应该能看到 "Update Apifox Docs" 工作流
3. 点击工作流查看详情

### 第四步：首次手动运行

1. 在 Actions 页面
2. 左侧选择 "Update Apifox Docs"
3. 点击右侧 "Run workflow"
4. 选择分支（main）
5. 点击 "Run workflow" 按钮

### 第五步：查看执行结果

1. 等待几分钟（首次运行需要安装依赖）
2. 点击运行记录查看详情
3. 可以看到每一步的输出：
   - 检查文档更新
   - 爬取文档
   - 重建知识库
   - 提交更改

## ⚙️ 配置选项

### 调整更新频率

编辑 `.github/workflows/update-docs.yml`：

```yaml
on:
  schedule:
    # 每天凌晨 2 点（UTC 时间）
    - cron: '0 2 * * *'

    # 每 6 小时
    # - cron: '0 */6 * * *'

    # 每周日凌晨 3 点
    # - cron: '0 3 * * 0'

    # 每月 1 号凌晨 2 点
    # - cron: '0 2 1 * *'
```

**注意**：cron 使用 UTC 时间，北京时间需要减 8 小时

例如：
- 北京时间凌晨 2 点 → UTC 时间 18:00（前一天）
- `cron: '0 18 * * *'`

### 更新后自动部署

如果需要同时更新飞书应用，可以添加部署步骤：

```yaml
      - name: 通知飞书
        run: |
          curl -X POST "https://open.feishu.cn/open-apis/bot/v2/hook/${{ secrets.FEISHU_WEBHOOK }}" \
            -H "Content-Type: application/json" \
            -d '{
              "msg_type": "text",
              "content": {
                "text": "✅ Apifox 文档已更新，知识库已重建"
              }
            }'
```

### 添加环境变量和密钥

如果需要访问私有资源：

1. 在 GitHub 仓库页面
2. Settings → Secrets and variables → Actions
3. 点击 "New repository secret"
4. 添加密钥：
   - Name: `FEISHU_WEBHOOK`
   - Value: 你的飞书 Webhook URL

然后在 workflow 中使用：

```yaml
- name: 通知
  run: |
    curl -X POST "${{ secrets.FEISHU_WEBHOOK }}"
```

## 📊 监控和日志

### 查看执行历史

```bash
# 使用 GitHub CLI
gh run list --repo knowledge-base-bot

# 查看最新运行
gh run view --repo knowledge-base-bot

# 查看运行日志
gh run view --repo knowledge-base-bot --log
```

### 设置失败通知

在 GitHub 仓库设置中：

1. Settings → Notifications
2. 勾选 "Workflow runs" 通知
3. 选择通知方式（邮件、GitHub 移动端等）

### 添加状态徽章

在 README.md 中添加：

```markdown
![Docs Update](https://github.com/你的用户名/knowledge-base-bot/actions/workflows/update-docs.yml/badge.svg)
```

效果：
![Docs Update](https://github.com/你的用户名/knowledge-base-bot/actions/workflows/update-docs.yml/badge.svg)

## 🔧 高级配置

### 1. 并行运行多个任务

```yaml
jobs:
  update-docs:
    runs-on: ubuntu-latest
    steps:
      # ... 现有步骤

  lint-code:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: 运行代码检查
        run: |
          pip install flake8
          flake8 src/
```

### 2. 缓存依赖（加速构建）

```yaml
      - name: 缓存 Python 依赖
        uses: actions/cache@v3
        with:
          path: ~/.cache/pip
          key: ${{ runner.os }}-pip-${{ hashFiles('**/requirements.txt') }}
          restore-keys: |
            ${{ runner.os }}-pip-
```

### 3. 只在文档变化时提交

```yaml
      - name: 检查是否有变化
        id: check_changes
        run: |
          if git diff --quiet data/documents/; then
            echo "has_changes=false" >> $GITHUB_OUTPUT
          else
            echo "has_changes=true" >> $GITHUB_OUTPUT
          fi

      - name: 提交更改
        if: steps.check_changes.outputs.has_changes == 'true'
        run: |
          git config --local user.email "github-actions[bot]"
          git config --local user.name "github-actions[bot]"
          git add data/documents/ data/vectordb/
          git commit -m "docs: 自动更新文档"
```

### 4. 添加更新摘要

```yaml
      - name: 生成更新摘要
        run: |
          echo "## 📚 文档更新摘要" >> $GITHUB_STEP_SUMMARY
          echo "" >> $GITHUB_STEP_SUMMARY
          echo "- 更新时间: $(date)" >> $GITHUB_STEP_SUMMARY
          echo "- 更新页面数: $(git diff --name-only data/documents/ | wc -l)" >> $GITHUB_STEP_SUMMARY
```

## 🎯 实际使用流程

### 日常使用（自动运行）

1. GitHub Actions 每天自动运行
2. 检查 Apifox 文档更新
3. 如果有更新，自动下载并重建知识库
4. 提交更改到仓库
5. 你会收到通知（如果配置了）

### 手动触发更新

**方法 1：通过网页**
1. 访问 Actions 页面
2. 点击 "Run workflow"

**方法 2：通过 GitHub CLI**
```bash
gh workflow run update-docs.yml --repo knowledge-base-bot
```

**方法 3：通过 API**
```bash
curl -X POST \
  -H "Authorization: token $GITHUB_TOKEN" \
  -H "Accept: application/vnd.github.v3+json" \
  https://api.github.com/repos/你的用户名/knowledge-base-bot/actions/workflows/update-docs.yml/dispatches \
  -d '{"ref":"main"}'
```

### 查看更新内容

```bash
# 拉取最新更改
git pull origin main

# 查看更新的文档
git log --oneline --all --grep="docs"

# 查看具体变化
git show <commit-hash>
```

## 📈 成本和使用限制

### GitHub Actions 免费额度

| 账号类型 | 每月免费分钟数 | 存储 |
|---------|--------------|------|
| Public 仓库 | 无限制 | 无限制 |
| Private 仓库 | 2000 分钟 | 500 MB |

**预计消耗**：
- 每次运行约 5-10 分钟
- 每天 1 次 = 每月约 150-300 分钟
- **完全在免费额度内！**

### 优化建议

如果超出免费额度：

1. **减少运行频率**
   ```yaml
   # 从每天改为每周
   schedule:
     - cron: '0 3 * * 0'
   ```

2. **使用缓存**
   ```yaml
   - name: 缓存向量数据库
     uses: actions/cache@v3
     with:
       path: data/vectordb
       key: vectordb-${{ github.run_id }}
       restore-keys: |
         vectordb-
   ```

3. **只在有变化时运行**
   ```yaml
   # 先检查 API，有变化才更新
   ```

## 🔒 安全建议

### 1. 保护敏感信息

```yaml
# ❌ 不要直接写密钥
- name: 发送通知
  run: curl "https://api.feishu.cn/webhook/xxx/yyy/zzz"

# ✅ 使用 Secrets
- name: 发送通知
  run: curl "${{ secrets.FEISHU_WEBHOOK }}"
```

### 2. 限制权限

在 workflow 中设置最小权限：

```yaml
permissions:
  contents: write  # 只需要写仓库权限
  pull-requests: read
```

### 3. 审计日志

定期查看 Actions 运行记录：
- 确保只有预期的任务在运行
- 检查是否有异常的执行时间
- 查看是否有失败的运行

## 🐛 故障排查

### 问题 1：工作流不运行

**检查**：
```bash
# 查看工作流是否启用
gh workflow list --repo knowledge-base-bot

# 查看触发条件
gh workflow view update-docs.yml --repo knowledge-base-bot
```

**解决**：
- 确认 workflow 文件在 `.github/workflows/` 目录
- 确认 cron 表达式正确
- 查看是否需要手动触发一次

### 问题 2：爬取失败

**检查**：
1. 在 Actions 日志中查看错误信息
2. 可能是网络问题或网站结构变化

**解决**：
- 增加重试逻辑
- 调整爬虫代码
- 使用全量更新

### 问题 3：提交失败

**错误信息**：`git diff --staged --quiet`

**原因**：没有实际变化

**解决**：修改 workflow，只在有变化时提交

## 📝 维护建议

### 每周
- 查看 Actions 运行状态
- 检查是否有失败的任务
- 查看更新日志

### 每月
- 手动运行一次全量更新
- 检查文档数量和大小
- 清理旧的运行记录

### 每季度
- 评估更新频率是否合适
- 优化 workflow 配置
- 更新依赖版本

## 🎉 完成！

现在你的 Apifox 文档会自动更新，完全免费且无需服务器！

**验证设置**：
```bash
# 1. 访问 Actions 页面
https://github.com/你的用户名/knowledge-base-bot/actions

# 2. 手动运行一次
点击 "Run workflow"

# 3. 查看结果
等待完成后，查看更新的文档
```

**下次自动运行**：根据你设置的 cron 表达式自动执行

祝你使用愉快！🚀
