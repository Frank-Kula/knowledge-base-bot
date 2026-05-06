"""
问题分类器
判断用户问题是 Bug、需求还是使用问题
"""

from typing import Dict, List, Optional
from loguru import logger
from anthropic import Anthropic

from src.utils.config_loader import Config


class QuestionClassifier:
    """问题分类器"""

    def __init__(self, config: Config):
        self.config = config
        # 支持自定义 API 端点
        client_kwargs = {"api_key": config.llm.api_key}
        if config.llm.base_url:
            client_kwargs["base_url"] = config.llm.base_url
        self.client = Anthropic(**client_kwargs)

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

            # 提取文本内容（处理 ThinkingBlock）
            response_text = self._extract_text_from_response(response.content)

            # 解析结果
            result = self._parse_classification_result(response_text)

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

        # 强制品牌约束：严禁提及 Apidog
        brand_instruction = "【注意】你目前仅代表 Apifox 品牌。严禁在输出中包含 'Apidog' 关键词。如果提供的背景文档中包含 Apidog，请在回答时将其替换为 Apifox。"
        
        prompt = self.config.classifier.prompt_template.format(
            question=question,
            context=context,
            additional_info=self._format_additional_info(additional_info)
        ) + "\n" + brand_instruction

        # 添加分类指导
        classification_guide = """
## 分类标准

### Bug（缺陷）
- 产品功能异常、错误或崩溃
- **所有 HTTP 错误（如 400, 401, 403, 404, 500, 502 等）**
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

    def _extract_text_from_response(self, content_blocks) -> str:
        """
        从 LLM 响应中提取文本内容
        处理 TextBlock 和 ThinkingBlock 混合的情况
        """
        text_parts = []
        for block in content_blocks:
            # 检查块的类型
            block_type = getattr(block, 'type', None)
            if block_type == 'text':
                # TextBlock - 直接获取 text 属性
                text_parts.append(block.text)
            elif block_type == 'thinking':
                # ThinkingBlock - 跳过，只提取最终文本
                continue
            elif hasattr(block, 'text'):
                # 兼容旧版本 API
                text_parts.append(block.text)
            else:
                # 尝试转换为字符串
                logger.debug(f"未知块类型: {type(block)}")
                text_parts.append(str(block))

        return "\n".join(text_parts)

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

    async def extract_info(
        self,
        history: List[Dict[str, str]],
        target_fields: List[str]
    ) -> Dict:
        """
        从对话历史中提取结构化信息

        Args:
            history: 对话历史 [{"role": "user|assistant", "content": "..."}]
            target_fields: 目标字段列表，如 ["version", "os", "steps"]

        Returns:
            提取到的字段字典，未找到的标记为 "未提及"
        """
        try:
            # 构建提取 Prompt
            prompt = self._build_extraction_prompt(history, target_fields)

            # 调用 LLM
            response = self.client.messages.create(
                model=self.config.llm.model,
                max_tokens=1000,
                temperature=0.0,  # 提取信息要求准确，使用 0.0
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )

            # 提取文本内容
            response_text = self._extract_text_from_response(response.content)

            # 解析结果
            result = self._parse_extraction_result(response_text, target_fields)

            logger.info(f"信息提取结果: {result}")
            return result

        except Exception as e:
            logger.error(f"信息提取失败: {e}")
            return {field: "提取失败" for field in target_fields}

    def _build_extraction_prompt(
        self,
        history: List[Dict[str, str]],
        target_fields: List[str]
    ) -> str:
        """Build extraction prompt - optimized for multi-turn context awareness"""

        history_text = ""
        for msg in history:
            role = "用户" if msg["role"] == "user" else "助手"
            history_text += f"{role}: {msg['content']}\n"

        # Field meaning descriptions
        field_meanings = {
            "version": "软件版本号（如 Apifox 2.3.5、v1.0 等）",
            "os": "操作系统（如 Windows 11、Mac、Linux 等）",
            "steps": "复现步骤/操作流程（用户描述的如何触发问题）",
            "environment": "运行环境信息",
            "background": "需求背景说明",
            "scenario": "使用场景描述"
        }

        field_desc_detail = "\n".join([f"- {field}: {field_meanings.get(field, field)}" for field in target_fields])

        prompt = f"""
你是一个精干的技术支持助理。请仔细分析对话历史，提取用户提到的关键信息。

## 对话历史
{history_text}

## 需要提取的字段
{field_desc_detail}

## 提取规则
1. **必须返回标准 JSON 格式**，包含所有目标字段。
2. **优先关注最新回复**：用户可能在最近的消息中补充了之前缺失的信息。
3. **不要遗漏片段信息**：即使信息不完整，也要记录下来（如"Windows"记录为"Windows"）。
4. **不猜测不编造**：对话中确实没提到某字段，标记为"未提及"。
5. **合并相似表达**：如"Win10"和"Windows 10"统一记录为用户原话。

## 识别技巧
- 版本号：关注数字+字母组合，如 "2.3.5"、"v1.0"、"beta版"
- 操作系统：关注 "Windows"、"Mac"、"Linux"、"安卓"、"iOS" 等关键词
- 复现步骤：关注用户描述的操作流程、点击、输入等动作描述

## 返回格式
```json
{{
  "version": "提取到的版本号或'未提及'",
  "os": "提取到的操作系统或'未提及'",
  "steps": "提取到的复现步骤或'未提及'"
}}
```
"""
        return prompt

    def _parse_extraction_result(self, response_text: str, target_fields: List[str]) -> Dict:
        """解析提取结果"""
        import json
        try:
            start_idx = response_text.find("{")
            end_idx = response_text.rfind("}") + 1
            if start_idx != -1 and end_idx != -1:
                json_str = response_text[start_idx:end_idx]
                result = json.loads(json_str)

                # 补全缺失字段
                for field in target_fields:
                    if field not in result:
                        result[field] = "未提及"
                return result
        except Exception as e:
            logger.warning(f"解析提取结果失败: {e}")

        return {field: "未提及" for field in target_fields}

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