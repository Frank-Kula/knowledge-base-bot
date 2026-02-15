@echo off
REM 定时更新文档脚本（Windows）

cd /d %~dp0

REM 激活虚拟环境
call venv\Scripts\activate

REM 智能更新文档
python src\rag\auto_update_docs.py --mode smart --rebuild-kb

REM 记录日志
if %errorlevel% equ 0 (
    echo 文档更新成功: %date% %time% >> logs\update.log
) else (
    echo 文档更新失败: %date% %time% >> logs\update.log
)
