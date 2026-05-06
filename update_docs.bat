@echo off
REM 定时更新文档脚本（Windows）

cd /d %~dp0

REM 1. 从 Sitemap 同步最新文档 (Node.js)
echo 正在同步最新文档...
cd data\documents\download-apifoxapidog-docs
call npm run download:apifox
cd ..\..\..

REM 2. 激活虚拟环境
call venv\Scripts\activate

REM 3. 重建知识库 (Python RAG)
REM 注意：这里直接运行重建逻辑，因为文档已由 Node.js 同步完成
python src\rag\auto_update_docs.py --mode smart --rebuild-kb

REM 记录日志
if %errorlevel% equ 0 (
    echo 文档更新成功: %date% %time% >> logs\update.log
) else (
    echo 文档更新失败: %date% %time% >> logs\update.log
)
