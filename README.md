# 技术支持知识库机器人

## 项目概述

这是一个智能技术支持机器人系统，用于企微/飞书用户群的问题收集、分类和处理。

## 功能流程

```
用户提问 → 机器人接收 → 信息收集 → 知识库检索 → 问题分类 → 输出模板 → 飞书工单
```

### 核心功能

1. **信息收集**
   - 版本号确认
   - Web端复现确认
   - 特定数据复现确认
   - 问题二次确认

2. **问题分类**
   - Bug 判断
   - 需求判断
   - 最佳实践/使用问题判断

3. **知识库检索**
   - 基于 Apifox 帮助文档 (https://docs.apifox.com/)
   - RAG 向量检索
   - 历史问题匹配

4. **模板输出**
   - Bug 缺陷模板
   - 需求模板
   - 飞书多维表格/工单集成

## 目录结构

```
knowledge-base-bot/
├── config/              # 配置文件
│   ├── config.yaml      # 主配置
│   └── prompts.yaml     # LLM Prompt 模板
├── data/                # 数据目录
│   ├── documents/       # 帮助文档（用于RAG）
│   ├── templates/       # 缺陷/需求模板
│   └── history/         # 历史记录
├── src/                 # 源代码
│   ├── bots/           # 企微/飞书机器人
│   ├── handlers/       # 回调处理器（卡片按钮交互）
│   ├── integrations/   # 第三方集成（lark-cli）
│   ├── rag/            # 知识库检索
│   ├── classifiers/    # 问题分类器
│   └── utils/          # 工具函数
├── logs/               # 日志文件
├── requirements.txt    # Python依赖
└── README.md          # 项目说明
```

## 快速开始

### 1. 前置准备

#### 必需资源
- [ ] 企微机器人 Webhook 或 飞书开放平台应用
- [ ] 飞书多维表格（用于接收工单）
- [ ] LLM API（Claude/GPT/DeepSeek等）
- [ ] 向量数据库（Chroma/Pinecone/Weaviate）

#### 配置清单
```yaml
# config/config.yaml
bots:
  wecom:
    enabled: true
    webhook: "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=YOUR_KEY"
  feishu:
    enabled: true
    app_id: "cli_xxxxxxxxxxxxx"
    app_secret: "xxxxxxxxxxxxxx"

llm:
  provider: "anthropic"  # anthropic/openai/deepseek
  api_key: "your-api-key"
  model: "claude-3-5-sonnet-20241022"

vector_db:
  provider: "chroma"  # chroma/pinecone/weaviate
  path: "./data/vectordb"

feishu:
  base_url: "https://open.feishu.cn"
  spreadsheet_token: "your-sheet-token"
```

### 2. 安装依赖

```bash
pip install -r requirements.txt
```

### 3. 初始化知识库

```bash
python src/rag/build_knowledge_base.py
```

### 4. 启动机器人

```bash
python src/bots/main.py
```

## 工作流程示例

### 用户提问流程

**用户**: "接口测试失败，报500错误"

**机器人**:
1. 🔍 收集信息：
   - 请问您的 Apifox 版本号是多少？
   - 这个问题在 Web 端能否复现？
   - 是否是特定接口/数据才出现？
   - 能否提供完整的错误信息截图？

2. 📚 知识库检索：
   - 在帮助文档中搜索相关问题
   - 匹配历史相似问题

3. 🏷️ 问题分类：
   - 分析问题类型（Bug/需求/使用问题）
   - 给出分类依据和置信度

4. 📝 生成模板：
   ```
   【Bug 报告】
   标题：接口测试返回500错误
   版本：2.x.x
   环境：Windows / Web端
   复现步骤：...
   预期结果：...
   实际结果：...
   ```

5. 📋 同步飞书：
   - 创建飞书多维表格记录
   - @负责人进行最终确认

## 开发计划

- [ ] Phase 1: 基础框架搭建
- [ ] Phase 2: 企微/飞书机器人集成
- [ ] Phase 3: RAG 知识库构建
- [ ] Phase 4: 问题分类器开发
- [x] Phase 5: 飞书工单系统集成
- [ ] Phase 6: 测试与优化

## 更新日志

### 2026-04-24 沉浸式交互与智能提取优化

**新增功能**
- **智能信息收集卡片**：推出「填空题」样式卡片（`build_smart_collection_card`），实时显示收集进度并引导用户点击按钮补充。
- **LLM 异步实体提取**：利用 LLM 自动从多轮对话中识别版本、系统、步骤等信息，自动填补进度卡片，极大降低用户录入成本。
- **飞书长连接 (WebSocket) 支持**：提供 `src/bots/feishu_ws_main.py`，无需公网 IP 即可接收回调，解决内网开发及部署难题。
- **工单交互闭环**：卡片支持「立即提交」、「强制提交」、「继续修改」等动作，并与多维表格深度同步。

**代码变更**
- `src/bots/feishu_bot.py`：重构消息处理逻辑，集成会话管理器和智能分类/提取。
- `src/utils/message_card_builder.py`：新增多种交互式卡片模板，支持 AppLink 和 callback。
- `src/bots/feishu_ws_main.py`：新增 WebSocket 入口，支持去重和 SSL 证书自动 Patch。

### 2026-04-20 交互式消息卡片功能

**新增功能**
- 创建 `src/utils/message_card_builder.py` - 飞书交互卡片构建器
- 支持 Bug 告警卡片（红色标题）、功能建议卡片（蓝色标题）
- 多列布局、分割线、引用区块、操作按钮

**卡片按钮交互逻辑**
- 「查看完整上下文」按钮：AppLink 协议跳转到多维表格记录详情页
- 「一键认领并跟进」按钮：callback 类型，触发后端更新负责人字段
- 「转为 PM 需求」按钮：callback 类型，将 Bug 转为需求记录

**技术要点**
- 使用 Git Bash 解决 Windows 命令行 JSON 引号问题
- Shell 命令替换 `$(cat file)` 传递复杂 JSON
- AppLink 协议：`lark://applink.feishu.cn/client/bitable/open?appToken=xxx&tableId=xxx&recordId=xxx`

**文件变更**
- `src/utils/message_card_builder.py` - 新增，支持 AppLink 和 callback
- `src/integrations/lark_cli_wrapper.py` - 修复交互卡片发送逻辑
- `src/handlers/card_callback_handler.py` - 新增，处理按钮回调事件

### 2026-04-17 飞书集成优化

**代码简化**
- 删除 httpx 降级逻辑，统一使用 lark-cli
- `src/bots/feishu_integration.py` 从 ~300 行简化到 ~100 行

**lark-cli 封装**
- `src/integrations/lark_cli_wrapper.py` 封装飞书 CLI 操作
- 支持发送消息、创建多维表格记录、搜索消息等

**企微消息桥接**
- 配置企微机器人参数（Token、EncodingAESKey）
- 域名验证暂受阻（ngrok 域名不符合企业要求）

## 技术栈

- **机器人框架**: 企微 Webhook / 飞书开放平台
- **LLM**: Claude 3.5 / GPT-4 / DeepSeek
- **RAG 框架**: LangChain / LlamaIndex
- **向量数据库**: Chroma / Pinecone
- **Web框架**: FastAPI
- **数据库**: SQLite / PostgreSQL
