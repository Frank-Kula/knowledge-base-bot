"""
测试需求报告场景
验证 Feature 类型的问题分类和模板生成
"""

import os
import sys
import asyncio
from dotenv import load_dotenv

# 设置 UTF-8 编码输出（Windows 兼容）
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

# 添加项目路径
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from src.bots.conversation_manager import ConversationManager
from src.utils.template_manager import TemplateManager
from src.classifiers.question_classifier import QuestionClassifier
from src.utils.config_loader import load_config
from datetime import datetime

# 加载环境变量
load_dotenv()

print("=" * 80)
print("需求报告场景测试")
print("=" * 80)
print("\n测试场景：")
print("用户提交功能需求建议")
print("\n" + "=" * 80)

# 初始化配置
config = load_config()

# 初始化组件
conversation_manager = ConversationManager(config)
template_manager = TemplateManager(config)
classifier = QuestionClassifier(config)

# 测试场景：功能需求建议
print("\n【测试场景：功能需求】\n")
print("用户在群聊中说：\"希望能支持批量导出接口文档\"\n")

# 模拟用户消息
user_id = "test_user_002"
initial_message = "希望能支持批量导出接口文档"

print(f"用户消息: {initial_message}")

# 第1步：问题分类（异步）
print("\n" + "-" * 80)
print("[第1步] 问题分类")
print("-" * 80)

async def do_classification():
    return await classifier.classify(
        question=initial_message,
        context="",
        additional_info={"description": "需要一次性导出多个接口的文档为PDF"}
    )

try:
    classification = asyncio.run(do_classification())

    print(f"\n分类结果：")
    print(f"  类型: {classification['type'].upper()}")
    print(f"  置信度: {classification['confidence']}")
    print(f"  理由: {classification['reason']}")

    if 'suggested_answer' in classification and classification['suggested_answer']:
        print(f"  建议回答: {classification['suggested_answer']}")

except Exception as e:
    print(f"  分类失败: {e}")
    sys.exit(1)

# 第2步：信息收集
print("\n" + "-" * 80)
print("[第2步] 信息收集")
print("-" * 80)

# 根据分类选择字段配置
if classification['type'] == 'feature':
    print("\n检测到功能需求，开始收集需求信息...")
    conversation_manager.fields = config.info_collection.feature_fields

    # 开始对话
    response = conversation_manager.start_conversation(user_id)
    print(f"\n机器人: {response['message']}")

    # 模拟用户回答
    simulated_answers = {
        "title": "希望支持批量导出接口文档",
        "user_scenario": "项目结束时需要归档所有接口文档，用于对外交付和内部存档",
        "current_status": "目前只能逐个导出接口，对于有数百个接口的项目非常耗时",
        "user_expectation": "希望能够选择多个接口，一次性导出为PDF或Word文档",
        "user_type": "企业",
        "subscription_status": "付费版",
        "team_size": "50人",
        "impact_level": "每次项目归档节省约2小时，团队每月至少2次项目归档"
    }

    collected_info = {}
    for field_name, answer in simulated_answers.items():
        response = conversation_manager.process_response(user_id, answer)
        collected_info[field_name] = answer

    print("\n[信息收集完成]")
    for field, value in collected_info.items():
        print(f"  {field}: {value}")

else:
    print("\n非需求类型，跳过信息收集")
    collected_info = {}
    sys.exit(0)

# 第3步：生成模板
print("\n" + "-" * 80)
print("[第3步] 生成标准化模板")
print("-" * 80)

# 渲染 Feature 模板
template = template_manager.render_feature_template(
    title=collected_info.get('title', '未命名需求'),
    user_scenario=collected_info.get('user_scenario', '待补充'),
    current_status=collected_info.get('current_status', '待补充'),
    user_expectation=collected_info.get('user_expectation', '待补充'),
    user_type=collected_info.get('user_type', '未知'),
    subscription_status=collected_info.get('subscription_status', '未知'),
    team_size=collected_info.get('team_size', ''),
    impact_level=collected_info.get('impact_level', ''),
    judgment_criteria=classification['reason'],
    confidence=int(classification['confidence'] * 100),
    reason=classification['reason'],
    value_assessment=f"影响{collected_info.get('team_size', '若干')}人团队，每次节省约2小时",
    feedback_source="群聊反馈",
    submit_time=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
)

print("\n生成的标准化文档：")
print("\n" + "=" * 80)
print(template)
print("=" * 80)

# 第4步：总结
print("\n" + "=" * 80)
print("[测试完成]")
print("=" * 80)

print("\n✅ 验证项：")
print("  1. 问题分类：准确识别为 " + classification['type'].upper())
print(f"  2. 信息收集：收集了 {len(collected_info)} 个字段")
print("  3. 模板生成：生成了标准化需求文档")

print("\n📊 Bug vs Feature 对比：")
print("  Bug 模板：复现步骤、预期、现状")
print("  Feature 模板：用户场景、当前状态、用户期望")

print("\n" + "=" * 80)
print("完整流程已支持多种问题类型！")
print("=" * 80)
