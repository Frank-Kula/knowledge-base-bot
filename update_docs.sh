#!/bin/bash
# 定时更新文档脚本（Linux/Mac）

# 进入项目目录
cd "$(dirname "$0")"

# 1. 从 Sitemap 同步最新文档 (Node.js)
echo "正在同步最新文档..."
cd data/documents/download-apifoxapidog-docs
npm run download:apifox
cd ../../..

# 2. 激活虚拟环境
source venv/bin/activate

# 3. 重建知识库 (Python RAG)
python src/rag/auto_update_docs.py --mode smart --rebuild-kb

# 如果更新成功，发送通知（可选）
if [ $? -eq 0 ]; then
    echo "文档更新成功: $(date)" >> logs/update.log
else
    echo "文档更新失败: $(date)" >> logs/update.log
fi
