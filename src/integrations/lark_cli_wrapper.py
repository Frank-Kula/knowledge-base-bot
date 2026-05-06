"""
lark-cli 封装模块
通过 subprocess 调用 lark-cli 命令实现飞书操作
"""

import subprocess
import json
import shlex
from typing import Dict, Optional, List
from loguru import logger
from pathlib import Path
import platform
import os


class LarkCliWrapper:
    """lark-cli 命令封装"""

    def __init__(self, config):
        """
        初始化

        Args:
            config: 配置对象，包含飞书相关配置
        """
        self.config = config

        # 多维表格配置
        self.app_token = getattr(config.feishu_ticket, 'app_token', '')
        self.bug_table_id = getattr(config.feishu_ticket, 'bug_table_id', '')
        self.feature_table_id = getattr(config.feishu_ticket, 'feature_table_id', '')

        # 字段映射
        self.bug_field_mappings = getattr(config.feishu_ticket, 'bug_field_mappings', {})
        self.feature_field_mappings = getattr(config.feishu_ticket, 'feature_field_mappings', {})

        logger.info("lark-cli wrapper 已初始化")

    def _run_command(
        self,
        cmd: List[str],
        timeout: int = 60,
        check: bool = False
    ) -> Dict:
        """
        执行 lark-cli 命令

        Args:
            cmd: 命令列表（含 lark-cli 前缀）
            timeout: 超时时间（秒）
            check: 是否检查返回码

        Returns:
            命令输出解析结果
        """
        try:
            cmd_str = shlex.join(cmd)
            logger.debug(f"执行命令: {cmd_str}")

            # Windows 上使用完整路径调用 lark-cli（避免 shell 引号问题）
            if platform.system() == "Windows":
                # 替换 lark-cli 为完整路径
                full_cmd = []
                for part in cmd:
                    if part == "lark-cli":
                        full_cmd.append("C:\\Users\\hr\\AppData\\Roaming\\npm\\lark-cli.cmd")
                    else:
                        full_cmd.append(part)

                result = subprocess.run(
                    full_cmd,
                    capture_output=True,
                    text=True,
                    timeout=timeout,
                    encoding='utf-8',
                    errors='replace'
                )
            else:
                result = subprocess.run(
                    cmd,
                    capture_output=True,
                    text=True,
                    timeout=timeout
                )

            # 解析 JSON 输出
            try:
                output = json.loads(result.stdout) if result.stdout else {}
            except json.JSONDecodeError:
                output = {"raw_output": result.stdout}

            # 添加执行状态
            output["returncode"] = result.returncode
            output["stderr"] = result.stderr

            if result.returncode != 0:
                logger.error(f"命令执行失败: {result.stderr}")
                if check:
                    raise subprocess.CalledProcessError(
                        result.returncode, cmd, result.stdout, result.stderr
                    )

            return output

        except subprocess.TimeoutExpired:
            logger.error(f"命令超时: {cmd}")
            return {"error": "timeout", "returncode": -1}

        except Exception as e:
            logger.error(f"命令执行异常: {e}")
            return {"error": str(e), "returncode": -1}

    def _run_command_shell(
        self,
        cmd_str: str,
        timeout: int = 60,
        cwd: Optional[str] = None
    ) -> Dict:
        """
        通过 shell 执行命令（支持 shell 特性如命令替换）

        Args:
            cmd_str: 命令字符串
            timeout: 超时时间（秒）
            cwd: 工作目录（可选）

        Returns:
            命令输出解析结果
        """
        try:
            logger.debug(f"执行 shell 命令: {cmd_str}")

            # Windows 上使用 bash 执行命令（支持 $(cat file) 语法）
            if platform.system() == "Windows":
                # 获取当前环境变量，确保 PATH 包含 lark-cli
                env = os.environ.copy()
                # 确保 npm 目录在 PATH 中
                npm_path = "C:\\Users\\hr\\AppData\\Roaming\\npm"
                if npm_path not in env.get("PATH", ""):
                    env["PATH"] = npm_path + ";" + env.get("PATH", "")

                # 使用 Git Bash 的 bash.exe
                git_bash_paths = [
                    "C:\\Program Files\\Git\\bin\\bash.exe",
                    "C:\\Program Files (x86)\\Git\\bin\\bash.exe",
                    "C:\\Git\\bin\\bash.exe"
                ]
                bash_exe = None
                for path in git_bash_paths:
                    if os.path.exists(path):
                        bash_exe = path
                        break

                if not bash_exe:
                    # 尝试通过 PATH 找 bash
                    bash_exe = "bash"

                result = subprocess.run(
                    [bash_exe, "-c", cmd_str],
                    capture_output=True,
                    text=True,
                    timeout=timeout,
                    encoding='utf-8',
                    errors='ignore',
                    cwd=cwd or os.getcwd(),
                    env=env
                )
            else:
                result = subprocess.run(
                    cmd_str,
                    shell=True,
                    capture_output=True,
                    text=True,
                    timeout=timeout,
                    cwd=cwd
                )

            # 解析 JSON 输出
            try:
                output = json.loads(result.stdout) if result.stdout else {}
            except json.JSONDecodeError:
                output = {"raw_output": result.stdout}

            output["returncode"] = result.returncode
            output["stderr"] = result.stderr

            if result.returncode != 0:
                logger.error(f"命令执行失败: {result.stderr}")

            return output

        except subprocess.TimeoutExpired:
            logger.error(f"命令超时: {cmd_str}")
            return {"error": "timeout", "returncode": -1}

        except Exception as e:
            logger.error(f"命令执行异常: {e}")
            return {"error": str(e), "returncode": -1}

    def _run_command_with_stdin(
        self,
        cmd: List[str],
        input_file: Path,
        timeout: int = 60
    ) -> Dict:
        """
        通过 stdin 传递文件内容执行命令

        Args:
            cmd: 命令列表
            input_file: 输入文件路径
            timeout: 超时时间（秒）

        Returns:
            命令输出解析结果
        """
        try:
            cmd_str = shlex.join(cmd)
            logger.debug(f"执行命令（stdin）: {cmd_str}")

            # 读取文件内容
            with open(input_file, 'r', encoding='utf-8') as f:
                file_content = f.read()

            # Windows 上使用完整路径
            if platform.system() == "Windows":
                full_cmd = []
                for part in cmd:
                    if part == "lark-cli":
                        full_cmd.append("C:\\Users\\hr\\AppData\\Roaming\\npm\\lark-cli.cmd")
                    else:
                        full_cmd.append(part)

                result = subprocess.run(
                    full_cmd,
                    input=file_content,
                    capture_output=True,
                    text=True,
                    timeout=timeout,
                    encoding='utf-8',
                    errors='ignore'
                )
            else:
                result = subprocess.run(
                    cmd,
                    input=file_content,
                    capture_output=True,
                    text=True,
                    timeout=timeout
                )

            # 解析 JSON 输出
            try:
                output = json.loads(result.stdout) if result.stdout else {}
            except json.JSONDecodeError:
                output = {"raw_output": result.stdout}

            output["returncode"] = result.returncode
            output["stderr"] = result.stderr

            if result.returncode != 0:
                logger.error(f"命令执行失败: {result.stderr}")

            return output

        except subprocess.TimeoutExpired:
            logger.error(f"命令超时: {cmd}")
            return {"error": "timeout", "returncode": -1}

        except Exception as e:
            logger.error(f"命令执行异常: {e}")
            return {"error": str(e), "returncode": -1}

    def _run_command_stdin_json(
        self,
        cmd: List[str],
        json_content: str,
        timeout: int = 60
    ) -> Dict:
        """
        通过 stdin 传递 JSON 内容执行交互卡片发送命令

        Args:
            cmd: 命令列表
            json_content: JSON 字符串内容
            timeout: 超时时间（秒）

        Returns:
            命令输出解析结果
        """
        try:
            cmd_str = shlex.join(cmd)
            logger.debug(f"执行命令（stdin JSON）: {cmd_str}")

            # Windows 上使用完整路径
            if platform.system() == "Windows":
                full_cmd = []
                for part in cmd:
                    if part == "lark-cli":
                        full_cmd.append("C:\\Users\\hr\\AppData\\Roaming\\npm\\lark-cli.cmd")
                    else:
                        full_cmd.append(part)

                # 使用 stdin 传递 JSON 内容
                result = subprocess.run(
                    full_cmd,
                    input=json_content,
                    capture_output=True,
                    text=True,
                    timeout=timeout,
                    encoding='utf-8',
                    errors='ignore'
                )
            else:
                result = subprocess.run(
                    cmd,
                    input=json_content,
                    capture_output=True,
                    text=True,
                    timeout=timeout
                )

            # 解析 JSON 输出
            try:
                output = json.loads(result.stdout) if result.stdout else {}
            except json.JSONDecodeError:
                output = {"raw_output": result.stdout}

            output["returncode"] = result.returncode
            output["stderr"] = result.stderr

            if result.returncode != 0:
                logger.error(f"命令执行失败: {result.stderr}")

            return output

        except subprocess.TimeoutExpired:
            logger.error(f"命令超时: {cmd}")
            return {"error": "timeout", "returncode": -1}

        except Exception as e:
            logger.error(f"命令执行异常: {e}")
            return {"error": str(e), "returncode": -1}

    def send_message(
        self,
        receive_id: str,
        content: str,
        receive_id_type: str = "chat_id",
        msg_type: str = "text",
        as_identity: str = "bot"
    ) -> Dict:
        """
        发送飞书消息

        Args:
            receive_id: 接收者 ID（群 ID 或用户 ID）
            content: 消息内容
            receive_id_type: ID 类型 (chat_id/open_id/user_id)
            msg_type: 消息类型 (text/post/interactive)
            as_identity: 执行身份 (bot/user)

        Returns:
            发送结果
        """
        cmd = [
            "lark-cli", "im", "+messages-send",
            "--as", as_identity
        ]

        # 添加接收者参数
        if receive_id_type == "chat_id":
            cmd.extend(["--chat-id", receive_id])
        else:
            cmd.extend(["--user-id", receive_id])

        # 判断是否使用临时文件（多行文本、markdown 或 interactive 卡片）
        use_file = msg_type in ("post", "interactive") or "\n" in content or len(content) > 200

        if use_file:
            # 使用临时文件传递内容
            cwd = os.getcwd()
            if msg_type == "interactive":
                content_file = Path(cwd) / ".lark_card_temp.json"
            else:
                content_file = Path(cwd) / ".lark_msg_temp.md"

            content_file.write_text(content, encoding='utf-8')

            try:
                if msg_type == "interactive":
                    # 发送交互式卡片 - 使用 Git Bash 执行（避免 Windows 命令行引号问题）
                    # 使用 Git Bash 的完整路径
                    git_bash = "D:\\software-all\\Git\\Git\\usr\\bin\\bash.exe"
                    npm_path = "/c/Users/hr/AppData/Roaming/npm"

                    cmd_str = f'export PATH="{npm_path}:$PATH" && lark-cli im +messages-send --as {as_identity} --chat-id {receive_id} --msg-type interactive --content "$(cat {content_file.name})"'

                    logger.debug(f"Interactive card command: {cmd_str[:100]}...")

                    result = subprocess.run(
                        [git_bash, "-c", cmd_str],
                        capture_output=True,
                        text=True,
                        timeout=30,
                        encoding='utf-8',
                        cwd=cwd
                    )

                    # 解析结果
                    try:
                        output = json.loads(result.stdout) if result.stdout else {}
                    except json.JSONDecodeError:
                        output = {"raw_output": result.stdout}

                    output["returncode"] = result.returncode
                    output["stderr"] = result.stderr

                    if result.returncode != 0:
                        logger.error(f"卡片发送失败: {result.stderr}")

                    result = output
                elif msg_type == "post":
                    # Markdown 格式 - 使用 shell 命令替换
                    cmd_str = shlex.join(cmd) + f" --markdown \"$(cat {content_file.name})\""
                    result = self._run_command_shell(cmd_str, timeout=30, cwd=cwd)
                else:
                    cmd.extend(["--text", content])
                    result = self._run_command(cmd, timeout=30)
            finally:
                content_file.unlink(missing_ok=True)
        else:
            # 短文本直接传递
            if msg_type == "text":
                cmd.extend(["--text", content])
            elif msg_type == "post":
                cmd.extend(["--markdown", content])
            else:
                cmd.extend(["--msg-type", msg_type, "--content", content])

            result = self._run_command(cmd, timeout=30)

        if result.get("ok") and result.get("data"):
            message_id = result["data"].get("message_id")
            logger.info(f"消息发送成功: message_id={message_id}")
            return {
                "success": True,
                "message_id": message_id,
                "chat_id": result["data"].get("chat_id")
            }
        else:
            error = result.get("error", {})
            if isinstance(error, dict):
                error_msg = error.get("message", result.get("stderr", "未知错误"))
            else:
                error_msg = str(error) if error else result.get("stderr", "未知错误")
            logger.error(f"消息发送失败: {error_msg}")
            return {
                "success": False,
                "error": error_msg
            }

    def create_record(
        self,
        table_id: str,
        fields: Dict,
        base_token: Optional[str] = None
    ) -> Dict:
        """
        创建多维表格记录

        Args:
            table_id: 表 ID
            fields: 字段数据
            base_token: Base Token（可选，默认使用配置）

        Returns:
            创建结果
        """
        token = base_token or self.app_token

        # 在当前目录创建临时文件（lark-cli 要求相对路径）
        json_file = Path(".lark_cli_temp.json")
        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump(fields, f, ensure_ascii=False)

        try:
            cmd = [
                "lark-cli", "base", "+record-upsert",
                "--as", "user",  # 使用用户身份（已授权）
                "--base-token", token,
                "--table-id", table_id,
                "--json", f"@{json_file.name}"  # 使用相对路径
            ]

            result = self._run_command(cmd, timeout=60)

            if result.get("ok") and result.get("data"):
                record = result["data"].get("record", {})
                record_id = record.get("record_id_list", [None])[0]
                logger.info(f"记录创建成功: record_id={record_id}")
                return {
                    "success": True,
                    "record_id": record_id,
                    "url": f"https://feishu.cn/base/{token}/{table_id}?record={record_id}"
                }
            else:
                error = result.get("error", {})
                if isinstance(error, dict):
                    error_msg = error.get("message", result.get("stderr", "未知错误"))
                else:
                    error_msg = str(error) if error else result.get("stderr", "未知错误")
                logger.error(f"记录创建失败: {error_msg}")
                return {
                    "success": False,
                    "error": error_msg
                }
        finally:
            # 清理临时文件
            json_file.unlink(missing_ok=True)

    def update_record(
        self,
        table_id: str,
        record_id: str,
        fields: Dict,
        base_token: Optional[str] = None
    ) -> Dict:
        """
        更新多维表格记录

        Args:
            table_id: 表 ID
            record_id: 记录 ID
            fields: 更新的字段数据
            base_token: Base Token（可选）

        Returns:
            更新结果
        """
        token = base_token or self.app_token

        cmd = [
            "lark-cli", "base", "+record-upsert",
            "--as", "bot",
            "--base-token", token,
            "--table-id", table_id,
            "--record-id", record_id,
            "--json", json.dumps(fields)
        ]

        result = self._run_command(cmd, timeout=30)

        if result.get("ok") and result.get("data"):
            logger.info(f"记录更新成功: record_id={record_id}")
            return {
                "success": True,
                "record_id": record_id
            }
        else:
            error_msg = result.get("error", {}).get("message", result.get("stderr", "未知错误"))
            logger.error(f"记录更新失败: {error_msg}")
            return {
                "success": False,
                "error": error_msg
            }

    def search_messages(
        self,
        query: str,
        chat_id: Optional[str] = None,
        start_time: Optional[str] = None,
        end_time: Optional[str] = None,
        limit: int = 50
    ) -> Dict:
        """
        搜索消息

        Args:
            query: 搜索关键词
            chat_id: 群 ID（可选）
            start_time: 开始时间
            end_time: 结束时间
            limit: 返回数量限制

        Returns:
            搜索结果
        """
        cmd = [
            "lark-cli", "im", "+messages-search",
            "--as", "user",
            "--query", query,
            "--page-size", str(limit)
        ]

        if chat_id:
            cmd.extend(["--chat-id", chat_id])
        if start_time:
            cmd.extend(["--start", start_time])
        if end_time:
            cmd.extend(["--end", end_time])

        result = self._run_command(cmd, timeout=60)

        if result.get("ok") and result.get("data"):
            messages = result["data"].get("items", [])
            logger.info(f"搜索到 {len(messages)} 条消息")
            return {
                "success": True,
                "messages": messages,
                "total": result["data"].get("total", len(messages))
            }
        else:
            return {
                "success": False,
                "error": result.get("error", {}).get("message", "搜索失败")
            }

    def get_chat_messages(
        self,
        chat_id: str,
        start_time: Optional[str] = None,
        end_time: Optional[str] = None,
        page_size: int = 20,
        sort: str = "desc"
    ) -> Dict:
        """
        获取聊天历史消息

        Args:
            chat_id: 群 ID
            start_time: 开始时间 (ISO 8601)
            end_time: 结束时间 (ISO 8601)
            page_size: 返回数量 (1-50)
            sort: 排序 (asc/desc)

        Returns:
            消息列表
        """
        cmd = [
            "lark-cli", "im", "+chat-messages-list",
            "--as", "bot",  # 使用 bot 身份（b2c app 需要）
            "--chat-id", chat_id,
            "--page-size", str(page_size),
            "--sort", sort
        ]

        if start_time:
            cmd.extend(["--start", start_time])
        if end_time:
            cmd.extend(["--end", end_time])

        result = self._run_command(cmd, timeout=60)

        if result.get("ok") and result.get("data"):
            messages = result["data"].get("messages", [])
            logger.info(f"获取到 {len(messages)} 条历史消息")
            return {
                "success": True,
                "messages": messages,
                "has_more": result["data"].get("has_more", False)
            }
        else:
            return {
                "success": False,
                "error": result.get("error", {}).get("message", "获取历史消息失败")
            }

    def get_field_list(
        self,
        table_id: str,
        base_token: Optional[str] = None
    ) -> Dict:
        """
        获取表字段列表

        Args:
            table_id: 表 ID
            base_token: Base Token（可选）

        Returns:
            字段列表
        """
        token = base_token or self.app_token

        cmd = [
            "lark-cli", "base", "+field-list",
            "--base-token", token,
            "--table-id", table_id
        ]

        result = self._run_command(cmd, timeout=30)

        if result.get("ok") and result.get("data"):
            fields = result["data"].get("items", [])
            logger.info(f"获取到 {len(fields)} 个字段")
            return {
                "success": True,
                "fields": fields
            }
        else:
            return {
                "success": False,
                "error": result.get("error", {}).get("message", "获取字段失败")
            }

    def create_bug_record(
        self,
        data: Dict,
        submitter: Optional[str] = None
    ) -> Dict:
        """
        创建 Bug 记录（便捷方法）

        Args:
            data: Bug 数据
            submitter: 提交人（可选）

        Returns:
            创建结果
        """
        # 构建字段数据
        fields = {}

        # 使用字段映射
        for key, field_name in self.bug_field_mappings.items():
            if key in data and data[key]:
                fields[field_name] = data[key]

        # 添加提交人
        if submitter and "提交人" in self.bug_field_mappings:
            fields["提交人"] = [{"id": submitter}]

        # 设置默认值
        if "类型" not in fields:
            fields["类型"] = "缺陷"
        if "状态" not in fields:
            fields["状态"] = "待处理"

        return self.create_record(self.bug_table_id, fields)

    def create_feature_record(
        self,
        data: Dict,
        submitter: Optional[str] = None
    ) -> Dict:
        """
        创建 Feature 记录（便捷方法）

        Args:
            data: Feature 数据
            submitter: 提交人（可选）

        Returns:
            创建结果
        """
        # 构建字段数据
        fields = {}

        # 使用字段映射
        for key, field_name in self.feature_field_mappings.items():
            if key in data and data[key]:
                fields[field_name] = data[key]

        # 添加提交人
        if submitter and "提交人" in self.feature_field_mappings:
            fields["提交人"] = [{"id": submitter}]

        # 设置默认值
        if "类型" not in fields:
            fields["类型"] = "需求"
        if "状态" not in fields:
            fields["状态"] = "待评估"

        return self.create_record(self.feature_table_id, fields)