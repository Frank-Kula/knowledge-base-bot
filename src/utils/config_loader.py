"""
配置加载器
"""

import os
from pathlib import Path
from typing import Any, Dict
import yaml
from pydantic import BaseModel, ConfigDict, Field
from pydantic_settings import BaseSettings


class BotConfig(BaseModel):
    """机器人配置"""
    enabled: bool = False
    webhook_url: str = ""
    app_id: str = ""
    app_secret: str = ""
    encrypt_key: str = ""
    verification_token: str = ""
    welcome_message: str = ""
    triggers: dict = {}
    chat_ids: list = []
    # 企微回调配置
    token: str = ""
    encoding_aes_key: str = ""
    corp_id: str = ""


class LLMConfig(BaseModel):
    """LLM 配置"""
    provider: str = "anthropic"
    api_key: str = ""
    base_url: str = ""  # 自定义 API 端点
    model: str = "glm-5"
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


class RequiredField(BaseModel):
    """必需字段配置"""
    name: str
    question: str
    required: bool = True
    example: str = ""
    hint: str = ""


class InfoCollectionConfig(BaseModel):
    """信息收集配置"""
    bug_fields: list = []
    feature_fields: list = []
    max_rounds: int = 8


class ClassifierConfig(BaseModel):
    """分类器配置"""
    question_types: list = ["bug", "feature", "usage"]
    confidence_threshold: float = 0.6
    prompt_template: str = ""


class KeywordTableConfig(BaseModel):
    """关键词表配置"""
    base_token: str = ""
    table_id: str = ""


class FeishuTicketConfig(BaseModel):
    """飞书工单配置"""
    app_token: str = ""
    bug_table_id: str = ""
    feature_table_id: str = ""
    bug_field_mappings: Dict[str, str] = Field(default_factory=dict)
    feature_field_mappings: Dict[str, str] = Field(default_factory=dict)


class Config(BaseModel):
    """主配置"""

    bots: Dict[str, Any] = Field(default_factory=dict)
    llm: LLMConfig = Field(default_factory=LLMConfig)
    rag: RAGConfig = Field(default_factory=RAGConfig)
    server: ServerConfig = Field(default_factory=ServerConfig)
    info_collection: InfoCollectionConfig = Field(default_factory=InfoCollectionConfig)
    classifier: ClassifierConfig = Field(default_factory=ClassifierConfig)
    keyword_table: KeywordTableConfig = Field(default_factory=KeywordTableConfig)
    feishu_ticket: FeishuTicketConfig = Field(default_factory=FeishuTicketConfig)

    model_config = ConfigDict(extra="ignore")


def load_config(config_path: str = "config/config.yaml") -> Config:
    """
    加载配置文件

    Args:
        config_path: 配置文件路径

    Returns:
        配置对象
    """
    # 加载 .env
    from dotenv import load_dotenv
    load_dotenv()

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
                app_id=bot_data.get("app_id", ""),
                app_secret=bot_data.get("app_secret", ""),
                encrypt_key=bot_data.get("encrypt_key", ""),
                verification_token=bot_data.get("verification_token", ""),
                welcome_message=bot_data.get("welcome_message", ""),
                triggers=bot_data.get("triggers", {}),
                chat_ids=bot_data.get("chat_ids", [])
            )
        elif bot_name == "apifox_wecom":
            bots_config["apifox_wecom"] = bot_data

    # RAG 配置
    rag_data = data.get("rag", {}).get("retrieval", {})
    rag_config = RAGConfig(**rag_data)

    # 服务器配置
    server_data = data.get("server", {})
    server_config = ServerConfig(**server_data)

    # 信息收集配置
    info_collection_data = data.get("info_collection", {})
    info_collection_config = InfoCollectionConfig(
        bug_fields=[RequiredField(**f) for f in info_collection_data.get("bug_fields", [])],
        feature_fields=[RequiredField(**f) for f in info_collection_data.get("feature_fields", [])],
        max_rounds=info_collection_data.get("max_rounds", 8)
    )

    # 分类器配置
    classifier_data = data.get("classifier", {})
    classifier_config = ClassifierConfig(
        question_types=classifier_data.get("question_types", ["bug", "feature", "usage"]),
        confidence_threshold=classifier_data.get("confidence_threshold", 0.6),
        prompt_template=classifier_data.get("prompt_template", "")
    )

    # 关键词表配置
    keyword_table_data = data.get("keyword_table", {})
    keyword_table_config = KeywordTableConfig(
        base_token=keyword_table_data.get("base_token", ""),
        table_id=keyword_table_data.get("table_id", "")
    )

    # 飞书工单配置
    feishu_ticket_data = data.get("feishu_ticket", {})
    feishu_ticket_config = FeishuTicketConfig(
        app_token=feishu_ticket_data.get("app_token", ""),
        bug_table_id=feishu_ticket_data.get("bug_table_id", ""),
        feature_table_id=feishu_ticket_data.get("feature_table_id", ""),
        bug_field_mappings=feishu_ticket_data.get("bug_field_mappings", {}),
        feature_field_mappings=feishu_ticket_data.get("feature_field_mappings", {})
    )

    # 构建主配置
    config = Config(
        bots=bots_config,
        llm=llm_config,
        rag=rag_config,
        server=server_config,
        info_collection=info_collection_config,
        classifier=classifier_config,
        keyword_table=keyword_table_config,
        feishu_ticket=feishu_ticket_config
    )

    return config
