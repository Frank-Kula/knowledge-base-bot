"""
模板管理器
处理缺陷和需求模板
"""

from pathlib import Path
from typing import Dict
from jinja2 import Template
from loguru import logger


class TemplateManager:
    """模板管理器"""

    def __init__(self, config):
        self.config = config
        self.template_dir = Path("data/templates")
        self.templates = self._load_templates()

    def _load_templates(self) -> Dict[str, Template]:
        """加载所有模板"""
        templates = {}

        # 加载 Bug 模板
        bug_template_path = self.template_dir / "bug_template.md"
        if bug_template_path.exists():
            with open(bug_template_path, "r", encoding="utf-8") as f:
                templates["bug"] = Template(f.read())
            logger.info("Bug 模板加载成功")

        # 加载 Feature 模板
        feature_template_path = self.template_dir / "feature_template.md"
        if feature_template_path.exists():
            with open(feature_template_path, "r", encoding="utf-8") as f:
                templates["feature"] = Template(f.read())
            logger.info("Feature 模板加载成功")

        # 加载 Usage 模板
        usage_template_path = self.template_dir / "usage_template.md"
        if usage_template_path.exists():
            with open(usage_template_path, "r", encoding="utf-8") as f:
                templates["usage"] = Template(f.read())
            logger.info("Usage 模板加载成功")

        return templates

    def render_bug_template(self, **kwargs) -> str:
        """
        渲染 Bug 模板

        Args:
            **kwargs: 模板变量

        Returns:
            渲染后的内容
        """
        template = self.templates.get("bug")
        if not template:
            logger.warning("Bug 模板不存在")
            return ""

        # 设置默认值
        defaults = {
            "title": "未命名 Bug",
            "version": "未知",
            "environment": "未知",
            "priority_level": "2",
            "description": "待补充",
            "expected": "待补充",
            "actual": "待补充",
            "error_log": "",
            "attachments": "",
            "specific_case": "",
            "related_docs": "",
            "confidence": "0",
            "reason": "",
            "suggested_answer": ""
        }

        defaults.update(kwargs)

        return template.render(**defaults)

    def render_feature_template(self, **kwargs) -> str:
        """
        渲染 Feature 模板

        Args:
            **kwargs: 模板变量

        Returns:
            渲染后的内容
        """
        template = self.templates.get("feature")
        if not template:
            logger.warning("Feature 模板不存在")
            return ""

        # 设置默认值
        defaults = {
            "title": "未命名需求",
            "feature_type": "功能增强",
            "priority_level": "3",
            "background": "待补充",
            "scenario": "待补充",
            "expected": "待补充",
            "relation": "",
            "business_value": "待补充",
            "other_benefits": "",
            "workaround": "",
            "references": "",
            "attachments": "",
            "confidence": "0",
            "reason": "",
            "suggested_answer": ""
        }

        defaults.update(kwargs)

        return template.render(**defaults)

    def render_usage_template(self, **kwargs) -> str:
        """
        渲染 Usage 模板

        Args:
            **kwargs: 模板变量

        Returns:
            渲染后的内容
        """
        template = self.templates.get("usage")
        if not template:
            logger.warning("Usage 模板不存在")
            return ""

        # 设置默认值
        defaults = {
            "question": "",
            "answer": "",
            "related_docs": ""
        }

        defaults.update(kwargs)

        return template.render(**defaults)

    def render_template(self, template_type: str, **kwargs) -> str:
        """
        根据类型渲染模板

        Args:
            template_type: 模板类型 (bug/feature/usage)
            **kwargs: 模板变量

        Returns:
            渲染后的内容
        """
        if template_type == "bug":
            return self.render_bug_template(**kwargs)
        elif template_type == "feature":
            return self.render_feature_template(**kwargs)
        elif template_type == "usage":
            return self.render_usage_template(**kwargs)
        else:
            logger.warning(f"未知的模板类型: {template_type}")
            return ""
