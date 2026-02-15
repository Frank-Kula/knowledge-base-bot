# 快速开始指南

## 环境准备

### 1. Python 环境
确保已安装 Python 3.9 或更高版本：
```bash
python --version
```

### 2. 安装依赖
```bash
# 创建虚拟环境（推荐）
python -m venv venv

# 激活虚拟环境
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# 安装依赖
pip install -r requirements.txt
```

## 配置步骤

### 1. 配置环境变量
```bash
# 复制环境变量模板
cp .env.example .env

# 编辑 .env 文件，填写以下内容：
# - LLM_API_KEY（必需）
# - FEISHU_APP_ID（必需）
# - FEISHU_APP_SECRET（必需）
# - FEISHU_SPREADSHEET_TOKEN（必需）
```

### 2. 准备帮助文档

#### 方法 A: 使用爬虫（推荐）
```bash
python src/rag/crawl_apifox_docs.py
```

#### 方法 B: 手动准备
将 Markdown 格式的文档放入 `data/documents/` 目录

### 3. 构建知识库
```bash
python src/rag/knowledge_base.py
```

### 4. 测试知识库
```bash
python -c "
import asyncio
from src.rag.knowledge_base import KnowledgeBase
from src.utils.config_loader import load_config

async def test():
    config = load_config()
    kb = KnowledgeBase(config)
    await kb.initialize()

    results = await kb.search('如何发送接口请求')
    for doc in results:
        print(doc.page_content)
        print('---')

asyncio.run(test())
"
```

### 5. 配置飞书

#### 创建飞书应用
1. 访问 https://open.feishu.cn/app
2. 创建企业自建应用
3. 开启机器人权限
4. 获取 App ID 和 App Secret

#### 创建多维表格
1. 创建新的多维表格
2. 设计字段结构（参考 `data/templates/`）
3. 获取 `app_token` 和 `table_id`

### 6. 启动机器人
```bash
python src/bots/main.py
```

### 7. 配置 Webhook

#### 使用 ngrok 测试（开发环境）
```bash
# 安装 ngrok
# 下载地址: https://ngrok.com/download

# 启动隧道
ngrok http 8000

# 将生成的 URL 配置到飞书事件订阅
# 例如: https://xxx.ngrok.io/webhook/feishu
```

#### 生产环境
使用 nginx 反向代理，配置 SSL 证书

## 测试流程

### 1. 在飞书群中测试
```
接口测试失败，报500错误
```

### 2. 机器人应该：
1. 确认收到问题
2. 询问版本号
3. 询问环境信息
4. 询问复现步骤
5. 分析问题类型
6. 生成工单模板
7. 发送到飞书多维表格

## 常见问题

### Q: 知识库构建失败？
A: 检查文档格式是否为 Markdown，确保至少有 10 篇文档

### Q: 飞书机器人无响应？
A:
1. 检查应用权限是否开启
2. 检查事件订阅 URL 是否可访问
3. 查看日志文件 `logs/bot.log`

### Q: 分类不准确？
A:
1. 增加文档数量
2. 调整 `config/config.yaml` 中的 Prompt
3. 尝试使用更强大的 LLM

### Q: 如何优化成本？
A:
1. 使用 DeepSeek 替代 Claude
2. 启用结果缓存
3. 调整 `max_tokens` 参数

## 下一步

- [ ] 自定义 Prompt 模板
- [ ] 添加更多文档源
- [ ] 配置监控和告警
- [ ] 优化分类准确度
- [ ] 添加数据分析

## 获取帮助

- 查看日志: `tail -f logs/bot.log`
- 查看配置: `config/config.yaml`
- 查看文档: `docs/前置准备.md`
