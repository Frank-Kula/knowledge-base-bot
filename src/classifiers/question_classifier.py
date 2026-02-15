"""
问题分类器
判断用户问题是 Bug、需求还是使用问题
"""

from typing import Dict, List, Optional
from loguru import logger
from anthropic import Anthropic

from utils.config_loader import Config


class QuestionClassifier:
    """问题分类器"""

    def __init__(self, config: Config):
        self.config = config
        self.client = Anthropic(api_key=config.llm.api_key)

    async def classify(
        self,
        question: str,
        context: str = "",
        additional_info: Dict = None
    ) -> Dict:
        """
        分类问题

        Args:
            question: 用户问题
            context: 知识库检索到的相关内容
            additional_info: 收集的额外信息

        Returns:
            分类结果
            {
                "type": "bug|feature|usage",
                "confidence": 0.0-1.0,
                "reason": "判断理由",
                "suggested_answer": "建议回答"
            }
        """
        try:
            # 构建分类 Prompt
            prompt = self._build_classification_prompt(
                question, context, additional_info or {}
            )

            # 调用 LLM
            response = self.client.messages.create(
                model=self.config.llm.model,
                max_tokens=2000,
                temperature=self.config.llm.temperature,
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )

            # 解析结果
            result = self._parse_classification_result(response.content[0].text)

            logger.info(f"问题分类结果: {result}")
            return result

        except Exception as e:
            logger.error(f"分类失败: {e}")
            return {
                "type": "unknown",
                "confidence": 0.0,
                "reason": f"分类失败: {str(e)}",
                "suggested_answer": ""
            }

    def _build_classification_prompt(
        self,
        question: str,
        context: str,
        additional_info: Dict
    ) -> str:
        """构建分类 Prompt"""

        prompt = self.config.classifier.prompt_template.format(
            question=question,
            context=context,
            additional_info=self._format_additional_info(additional_info)
        )

        # 添加分类指导
        classification_guide = """
## 分类标准

### Bug（缺陷）
- 产品功能异常、错误或崩溃
- 与文档描述不一致的行为
- 性能问题（响应慢、卡顿等）
- 兼容性问题

### Feature（需求）
- 新功能建议
- 功能改进建议
- 新增场景支持

### Usage（使用问题）
- 用户不知道如何操作
- 未找到最佳实践
- 配置/设置问题

请严格按照以上标准进行分类，并在 reason 中详细说明判断依据。
"""

        return prompt + "\n" + classification_guide

    def _format_additional_info(self, info: Dict) -> str:
        """格式化额外信息"""
        if not info:
            return "无"

        formatted = []
        for key, value in info.items():
            formatted.append(f"- {key}: {value}")

        return "\n".join(formatted)

    def _parse_classification_result(self, response_text: str) -> Dict:
        """解析 LLM 返回的分类结果"""

        import json

        try:
            # 尝试提取 JSON
            start_idx = response_text.find("{")
            end_idx = response_text.rfind("}") + 1

            if start_idx != -1 and end_idx != -1:
                json_str = response_text[start_idx:end_idx]
                result = json.loads(json_str)

                # 验证必需字段
                required_fields = ["type", "confidence", "reason", "suggested_answer"]
                for field in required_fields:
                    if field not in result:
                        result[field] = ""

                # 验证类型
                if result["type"] not in ["bug", "feature", "usage"]:
                    result["type"] = "unknown"

                # 验证置信度
                try:
                    result["confidence"] = float(result["confidence"])
                except:
                    result["confidence"] = 0.5

                return result

        except Exception as e:
            logger.warning(f"解析分类结果失败: {e}, 原始响应: {response_text}")

        # 默认返回
        return {
            "type": "unknown",
            "confidence": 0.3,
            "reason": "无法解析分类结果",
            "suggested_answer": response_text
        }

    async def batch_classify(
        self,
        questions: List[Dict[str, str]]
    ) -> List[Dict]:
        """
        批量分类

        Args:
            questions: 问题列表 [{"question": "...", "context": "..."}]

        Returns:
            分类结果列表
        """
        results = []
        for item in questions:
            result = await self.classify(
                item.get("question", ""),
                item.get("context", ""),
                item.get("additional_info", {})
            )
            results.append(result)

        return results
