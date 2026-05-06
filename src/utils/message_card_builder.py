"""
飞书消息卡片生成器
生成结构化、可操作的交互式卡片
"""

from typing import Dict, List, Optional
from datetime import datetime
import json


class MessageCardBuilder:
    """飞书消息卡片构建器"""

    # 颜色模板
    COLORS = {
        "bug": "red",       # BUG 使用红色
        "feature": "blue",  # 需求使用蓝色
        "usage": "grey",    # 使用问题使用灰色
        "success": "green"  # 成功/测试通过使用绿色
    }

    # 标题图标（Windows subprocess 不支持 emoji，使用文本标记）
    ICONS = {
        "bug": "[BUG]",
        "feature": "[FEATURE]",
        "usage": "[USAGE]",
        "success": "[OK]"
    }

    def __init__(self):
        self.card = {
            "config": {
                "wide_screen_mode": True,
                "enable_forward": True
            },
            "header": {},
            "elements": []
        }

    def set_header(self, title: str, card_type: str = "bug"):
        """
        设置卡片标题栏

        Args:
            title: 标题内容
            card_type: 卡片类型 (bug/feature/usage/success)
        """
        color = self.COLORS.get(card_type, "grey")
        icon = self.ICONS.get(card_type, "")

        self.card["header"] = {
            "template": color,
            "title": {
                "content": f"{icon} {title}",
                "tag": "plain_text"
            }
        }
        return self

    def add_div(self, content: str):
        """
        添加文本区块

        Args:
            content: Markdown 内容
        """
        self.card["elements"].append({
            "tag": "div",
            "text": {
                "tag": "lark_md",
                "content": content
            }
        })
        return self

    def add_fields(self, fields: List[Dict]):
        """
        添加多列字段（支持双列布局）

        Args:
            fields: 字段列表，每个字段包含 is_short 和 content
        """
        formatted_fields = []
        for field in fields:
            formatted_fields.append({
                "is_short": field.get("is_short", True),
                "text": {
                    "tag": "lark_md",
                    "content": field.get("content", "")
                }
            })

        self.card["elements"].append({
            "tag": "div",
            "fields": formatted_fields
        })
        return self

    def add_hr(self):
        """添加分割线"""
        self.card["elements"].append({"tag": "hr"})
        return self

    def add_quote(self, content: str, title: str = "用户原话"):
        """
        添加引用区块

        Args:
            content: 引用内容
            title: 标题
        """
        self.add_div(f"**{title}：**\n> \"{content}\"")
        return self

    def add_ai_insights(self, doc_gap: str = "", product_suggestion: str = ""):
        """
        添加 AI 深度洞察区块

        Args:
            doc_gap: 文档缺口分析
            product_suggestion: 产品建议
        """
        content = "**AI 改进洞察：**\n"
        if doc_gap:
            content += f"- **文档缺口**：{doc_gap}\n"
        if product_suggestion:
            content += f"- **产品建议**：{product_suggestion}\n"

        self.add_div(content)
        return self

    def add_actions(self, actions: List[Dict]):
        """
        添加操作按钮

        Args:
            actions: 按钮列表，支持 url 和 callback 类型
        """
        formatted_actions = []
        for action in actions:
            if action.get("type") == "button":
                button = {
                    "tag": "button",
                    "text": {
                        "content": action.get("text", ""),
                        "tag": "plain_text"
                    },
                    "type": action.get("style", "default")
                }
                # callback 类型：点击后触发回调
                if action.get("callback"):
                    button["value"] = action.get("callback")
                    # 按钮需要使用 callback 模式才能触发事件
                    button["click_type"] = "callback"
                # url 类型：点击后跳转
                if action.get("url"):
                    button["url"] = action.get("url")
                    button["click_type"] = "url"
                formatted_actions.append(button)

        self.card["elements"].append({
            "tag": "action",
            "actions": formatted_actions
        })
        return self

    def build(self) -> Dict:
        """构建完整卡片 JSON"""
        return self.card

    def to_json(self) -> str:
        """转换为 JSON 字符串"""
        return json.dumps(self.card, ensure_ascii=False)


def build_applink_url(app_token: str, table_id: str, record_id: str) -> str:
    """
    生成飞书 AppLink URL（在飞书客户端内打开，体验更好）

    Args:
        app_token: 多维表格 App Token
        table_id: 表 ID
        record_id: 记录 ID

    Returns:
        AppLink URL
    """
    return f"lark://applink.feishu.cn/client/bitable/open?appToken={app_token}&tableId={table_id}&recordId={record_id}"


def build_web_url(app_token: str, table_id: str, record_id: str) -> str:
    """
    生成飞书多维表格 Web URL

    Args:
        app_token: 多维表格 App Token
        table_id: 表 ID
        record_id: 记录 ID

    Returns:
        Web URL
    """
    return f"https://feishu.cn/base/{app_token}/{table_id}?record={record_id}"


def build_bug_alert_card(
    title: str,
    source: str,
    user: str,
    keywords: List[str],
    confidence: float,
    quote: str,
    record_id: str,
    app_token: str,
    table_id: str,
    doc_gap: str = "",
    product_suggestion: str = ""
) -> str:
    """
    构建 BUG 告警卡片

    Args:
        title: 标题
        source: 来源平台
        user: 触发用户
        keywords: 命中关键词
        confidence: AI 置信度
        quote: 用户原话
        record_id: 记录 ID
        record_url: 记录链接
        doc_gap: 文档缺口分析
        product_suggestion: 产品建议

    Returns:
        卡片 JSON 字符串
    """
    builder = MessageCardBuilder()

    # 设置标题
    builder.set_header(f"发现疑似线上 BUG ({source})", "bug")

    # 基本信息（双列布局）
    keywords_str = " ".join([f"#{kw}" for kw in keywords])
    confidence_level = "High" if confidence > 0.8 else "Medium" if confidence > 0.6 else "Low"

    builder.add_fields([
        {"is_short": True, "content": f"**来源平台：**\n{source}"},
        {"is_short": True, "content": f"**触发用户：**\n{user}"}
    ])

    builder.add_fields([
        {"is_short": True, "content": f"**命中关键词：**\n{keywords_str}"},
        {"is_short": True, "content": f"**AI 置信度：**\n{confidence:.0%} ({confidence_level})"}
    ])

    builder.add_hr()

    # 用户原话
    builder.add_quote(quote[:200] + "..." if len(quote) > 200 else quote)

    builder.add_hr()

    # AI 深度洞察
    builder.add_ai_insights(doc_gap, product_suggestion)

    # 生成 AppLink URL（在飞书客户端内打开）
    applink_url = build_applink_url(app_token, table_id, record_id)

    # 操作按钮
    builder.add_actions([
        {
            "type": "button",
            "text": "一键认领并跟进",
            "style": "primary",
            "callback": {"action": "claim", "record_id": record_id, "table_id": table_id}
        },
        {
            "type": "button",
            "text": "查看完整上下文",
            "style": "default",
            "url": applink_url
        }
    ])

    return builder.to_json()


def build_feature_card(
    title: str,
    source: str,
    user: str,
    keywords: List[str],
    confidence: float,
    quote: str,
    record_id: str,
    app_token: str,
    table_id: str,
    scenario: str = ""
) -> str:
    """
    构建需求建议卡片

    Args:
        title: 标题
        source: 来源平台
        user: 触发用户
        keywords: 命中关键词
        confidence: AI 置信度
        quote: 用户原话
        record_id: 记录 ID
        record_url: 记录链接
        scenario: 需求场景推测

    Returns:
        卡片 JSON 字符串
    """
    builder = MessageCardBuilder()

    # 设置标题（蓝色）
    builder.set_header(f"用户功能建议 ({source})", "feature")

    # 基本信息
    keywords_str = " ".join([f"#{kw}" for kw in keywords])

    builder.add_fields([
        {"is_short": True, "content": f"**来源平台：**\n{source}"},
        {"is_short": True, "content": f"**触发用户：**\n{user}"}
    ])

    builder.add_fields([
        {"is_short": True, "content": f"**命中关键词：**\n{keywords_str}"},
        {"is_short": True, "content": f"**AI 置信度：**\n{confidence:.0%}"}
    ])

    builder.add_hr()

    # 用户原话
    builder.add_quote(quote[:200] + "..." if len(quote) > 200 else quote)

    builder.add_hr()

    # AI 场景推测
    if scenario:
        builder.add_div(f"**AI 场景推测：**\n{scenario}")

    # 生成 AppLink URL
    applink_url = build_applink_url(app_token, table_id, record_id)

    # 操作按钮
    builder.add_actions([
        {
            "type": "button",
            "text": "转为 PM 需求",
            "style": "primary",
            "callback": {"action": "convert_pm", "record_id": record_id, "table_id": table_id}
        },
        {
            "type": "button",
            "text": "查看完整上下文",
            "style": "default",
            "url": applink_url
        }
    ])

    return builder.to_json()


def build_test_report_card(
    test_results: Dict,
    optimizations: List[str]
) -> str:
    """
    构建测试报告卡片

    Args:
        test_results: 测试结果
        optimizations: 优化内容列表

    Returns:
        卡片 JSON 字符串
    """
    builder = MessageCardBuilder()

    # 设置标题
    builder.set_header("飞书集成模块测试报告", "success")

    # 基本信息
    builder.add_fields([
        {"is_short": True, "content": f"**测试时间：**\n{datetime.now().strftime('%Y-%m-%d %H:%M')}"},
        {"is_short": True, "content": f"**测试模式：**\nlark-cli"}
    ])

    builder.add_hr()

    # 测试结果表格
    results_content = "**测试结果总览**\n"
    for test_name, result in test_results.items():
        status = "✅ 通过" if result.get("success") else "❌ 失败"
        detail = result.get("detail", "")
        results_content += f"| {test_name} | {status} | {detail} |\n"

    builder.add_div(results_content)

    builder.add_hr()

    # 优化内容
    if optimizations:
        opt_content = "**本次优化内容：**\n"
        for i, opt in enumerate(optimizations, 1):
            opt_content += f"{i}. {opt}\n"
        builder.add_div(opt_content)

    return builder.to_json()


def build_smart_collection_card(
    title: str,
    collected_data: Dict,
    missing_fields: List[str],
    state: str = "collecting",
    card_type: str = "bug"
) -> str:
    """
    构建智能收集进度卡片（填空题样式）

    优化后的沉浸式交互卡片，首答即展示，用户可逐项补充

    Args:
        title: 初始问题标题
        collected_data: 已收集的数据
        missing_fields: 尚缺少的字段
        state: 当前状态 (collecting/confirming)

    Returns:
        卡片 JSON 字符串
    """
    builder = MessageCardBuilder()

    # 根据状态设置不同的header
    if state == "collecting":
        missing_count = len([f for f in missing_fields if f != "title"])
        type_label = "需求" if card_type == "feature" else "问题"
        header_text = f"{type_label}信息收集进行中 (还缺 {missing_count} 项)"
        builder.set_header(header_text, card_type)
    else:
        builder.set_header("信息已收集完整，请确认", "success")

    # 问题描述摘要
    builder.add_div(f"**问题描述：**\n> {title[:100]}")
    builder.add_hr()

    # 字段名映射（中文显示名）
    field_name_map = {
        "version": "软件版本",
        "os": "操作系统",
        "steps": "复现步骤",
        "environment": "运行环境",
        "background": "需求背景",
        "scenario": "使用场景",
        "title": "标题"
    }

    # 构建字段展示（已填写 vs 待填写）
    builder.add_div("**📋 已获取信息：**")

    filled_fields = []
    for key, value in collected_data.items():
        if key == "title": continue
        name = field_name_map.get(key, key)
        if value and value != "未提及" and value != "提取失败":
            filled_fields.append(f"✅ **{name}**: {value}")

    if filled_fields:
        builder.add_div("\n".join(filled_fields))
    else:
        builder.add_div("*(暂无，请在下方补充)*")

    if state == "collecting" and missing_fields:
        builder.add_hr()
        builder.add_div("**✏️ 待补充信息：**")

        # 为每个缺失字段显示状态和按钮
        actions = []
        for field in missing_fields:
            if field == "title": continue
            name = field_name_map.get(field, field)
            # 显示待填写状态
            builder.add_div(f"🔴 **【{name}】** *(待填写)*")
            # 添加对应的填写按钮
            actions.append({
                "type": "button",
                "text": f"✍️ 补充{name}",
                "style": "default",
                "callback": {"action": "input_field", "field": field}
            })

        if actions:
            builder.add_actions(actions)

    builder.add_hr()

    # 根据状态显示不同的底部提示和按钮
    if state == "confirming":
        builder.add_div("💡 *信息已完整，确认后将自动创建工单。*")
        builder.add_actions([
            {
                "type": "button",
                "text": "✅ 确认并提交工单",
                "style": "primary",
                "callback": {"action": "confirm_ticket", "is_confirmed": True}
            },
            {
                "type": "button",
                "text": "✏️ 继续修改",
                "style": "default",
                "callback": {"action": "edit_ticket"}
            }
        ])
    else:
        builder.add_div("💡 *请直接在群内回复文字或截图，我会自动提取并更新卡片。*")
        builder.add_actions([
            {
                "type": "button",
                "text": "强制提交（信息可能不完整）",
                "style": "default",
                "callback": {"action": "force_submit"}
            }
        ])

    return builder.to_json()


    return builder.to_json()


def build_faq_answer_card(
    question: str,
    answer: str,
    source_url: str = "",
    related_docs: List[Dict] = None
) -> str:
    """
    构建 FAQ 知识库回答卡片
    """
    builder = MessageCardBuilder()
    
    # 标题栏：使用灰色标记为使用问题解答
    builder.set_header("已为您找到相关解答", "usage")
    
    # 用户问题摘要
    builder.add_quote(question[:100] + "..." if len(question) > 100 else question, title="您的问题")
    
    # AI 整理后的核心答案
    builder.add_div(f"**核心解答：**\n{answer}")
    
    # 如果有相关文档列表
    if related_docs:
        builder.add_hr()
        doc_links = []
        for doc in related_docs[:3]:  # 最多展示3个相关链接
            title = doc.get('title', '相关文档')
            url = doc.get('url', '#')
            doc_links.append(f"🔗 [{title}]({url})")
        builder.add_div("**参考文档：**\n" + "\n".join(doc_links))
    
    builder.add_hr()
    
    # 交互反馈
    builder.add_actions([
        {
            "type": "button",
            "text": "👍 已解决",
            "style": "default",
            "callback": {"action": "kb_feedback", "score": 1}
        },
        {
            "type": "button",
            "text": "❓ 没帮到我，转人工",
            "style": "primary",
            "callback": {"action": "transfer_to_human", "q": question}
        }
    ])
    
    return builder.to_json()


def build_formal_feature_card(
    initial_question: str,
    scenario: str,
    background: str,
    target_users: str = "通用用户",
    product_value: str = "待评估",
    state: str = "confirming"
) -> str:
    """
    构建正式的需求确认卡片
    """
    builder = MessageCardBuilder()
    
    # 标题栏：使用蓝色
    builder.set_header("捕获到功能建议", "feature")
    
    # 用户原始反馈
    builder.add_quote(initial_question[:100], title="用户原声")
    
    builder.add_hr()
    
    # 结构化需求描述
    builder.add_div(f"**💡 场景还原：**\n{scenario if scenario and scenario != '未提及' else '*(待补充场景描述)*'}")
    builder.add_div(f"**📖 背景动机：**\n{background if background and background != '未提及' else '*(待补充痛点背景)*'}")
    
    # 分列展示
    builder.add_fields([
        {"is_short": True, "content": f"**受众群体：**\n{target_users}"},
        {"is_short": True, "content": f"**价值预估：**\n{product_value}"}
    ])
    
    builder.add_hr()
    
    if state == "confirming":
        builder.add_div("💡 *此需求将同步至「用户声音池」，请核对信息。*")
        
        # 操作按钮
        builder.add_actions([
            {
                "type": "button",
                "text": "✅ 确认并同步",
                "style": "primary",
                "callback": {"action": "confirm_ticket", "type": "feature"}
            },
            {
                "type": "button",
                "text": "✏️ 继续修改",
                "style": "default",
                "callback": {"action": "edit_ticket"}
            }
        ])
    else:
        builder.add_div("✅ **已成功同步至需求池**")
        
    return builder.to_json()


def build_confirm_summary_card(
    title: str,
    summary_text: str,
    action_data: Dict
) -> str:
    """
    构建简要确认卡片（Summary & Confirm）

    Args:
        title: 汇总标题
        summary_text: 摘要正文
        action_data: 回调携带的数据
    """
    builder = MessageCardBuilder()
    builder.set_header("摘要确认", "success")
    
    builder.add_div(f"**我已为您记录：**\n{summary_text}")
    builder.add_div("请问是否直接提交工单？")
    
    builder.add_actions([
        {
            "type": "button",
            "text": "立即提交",
            "style": "primary",
            "callback": {**action_data, "action": "confirm_ticket"}
        },
        {
            "type": "button",
            "text": "修改信息",
            "style": "default",
            "callback": {"action": "edit_ticket"}
        }
    ])
    
    return builder.to_json()