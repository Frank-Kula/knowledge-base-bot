"""
配置加载器
"""

import os
from pathlib import Path
from typing import Any, Dict
import yaml
from pydantic import BaseModel
from pydantic_settings import BaseSettings


class BotConfig(BaseModel):
    """机器人配置"""
    enabled: bool = False
    webhook_url: str = ""
    chat_ids: list = []


class LLMConfig(BaseModel):
    """LLM 配置"""
    provider: str = "anthropic"
    api_key: str = ""
    model: str = "claude-3-5-sonnet-20241022"
    temperature: float = 0.3
    max_tokens: int = 2000
    timeout: int = 30


class RAGConfig(BaseModel):
    """RAG 配置"""
    chunk_size: int = 500
    chunk_overlap: int = 50
    top_k: int = 5
    score_threshold: float = 0.7


class ServerConfig(BaseModel):
    """服务器配置"""
    host: str = "0.0.0.0"
    port: int = 8000
    debug: bool = False


class Config(BaseSettings):
    """主配置"""

    bots: Dict[str, BotConfig] = {}
    llm: LLMConfig = None
    rag: RAGConfig = None
    server: ServerConfig = None

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


def load_config(config_path: str = "config/config.yaml") -> Config:
    """
    加载配置文件

    Args:
        config_path: 配置文件路径

    Returns:
        配置对象
    """
    # 读取 YAML 配置
    config_file = Path(config_path)
    if not config_file.exists():
        raise FileNotFoundError(f"配置文件不存在: {config_path}")

    with open(config_file, "r", encoding="utf-8") as f:
        config_data = yaml.safe_load(f)

    # 替换环境变量
    config_data = _replace_env_variables(config_data)

    # 构建配置对象
    return _build_config(config_data)


def _replace_env_variables(data: Any) -> Any:
    """
    递归替换配置中的环境变量

    支持格式：${ENV_VAR} 或 ${ENV_VAR:default_value}
    """
    import re

    if isinstance(data, str):
        # 替换环境变量
        pattern = r'\$\{([^}:]+)(?::([^}]*))?\}'

        def replacer(match):
            var_name = match.group(1)
            default_value = match.group(2) if match.group(2) is not None else ""
            return os.getenv(var_name, default_value)

        return re.sub(pattern, replacer, data)

    elif isinstance(data, dict):
        return {k: _replace_env_variables(v) for k, v in data.items()}

    elif isinstance(data, list):
        return [_replace_env_variables(item) for item in data]

    return data


def _build_config(data: Dict) -> Config:
    """构建配置对象"""

    # LLM 配置
    llm_data = data.get("llm", {})
    llm_config = LLMConfig(**llm_data)

    # 机器人配置
    bots_data = data.get("bots", {})
    bots_config = {}
    for bot_name, bot_data in bots_data.items():
        if bot_name == "wecom":
            bots_config["wecom"] = BotConfig(
                enabled=bot_data.get("enabled", False),
                webhook_url=bot_data.get("webhook_url", ""),
                chat_ids=bot_data.get("chat_ids", [])
            )
        elif bot_name == "feishu":
            bots_config["feishu"] = BotConfig(
                enabled=bot_data.get("enabled", False),
                webhook_url=bot_data.get("app_id", ""),  # 复用字段
                chat_ids=bot_data.get("chat_ids", [])
            )

    # RAG 配置
    rag_data = data.get("rag", {}).get("retrieval", {})
    rag_config = RAGConfig(**rag_data)

    # 服务器配置
    server_data = data.get("server", {})
    server_config = ServerConfig(**server_data)

    # 构建主配置
    config = Config()
    config.llm = llm_config
    config.bots = bots_config
    config.rag = rag_config
    config.server = server_config

    return config
