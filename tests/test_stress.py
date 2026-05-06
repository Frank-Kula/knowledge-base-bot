"""
压力测试：测试20+个边界案例
验证LLM分类和RAG检索的准确性
"""

import os
import sys
import asyncio
from dotenv import load_dotenv

# 设置 UTF-8 编码输出
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from src.classifiers.question_classifier import QuestionClassifier
from src.utils.config_loader import load_config
from datetime import datetime

# 加载环境变量
load_dotenv()

print("=" * 80)
print("压力测试：边界案例和模糊场景")
print("=" * 80)

# 初始化
config = load_config()
classifier = QuestionClassifier(config)

# 测试用例（20个边界案例）
test_cases = [
    # 明确的Bug
    {
        "question": "点击保存按钮没反应",
        "description": "点击后没有任何提示，也不保存",
        "expected": "bug",
        "reason": "功能异常"
    },
    {
        "question": "系统卡死了，无法操作",
        "description": "界面完全冻结",
        "expected": "bug",
        "reason": "性能问题"
    },
    {
        "question": "导入数据时丢失了部分字段",
        "description": "有些字段没有被导入",
        "expected": "bug",
        "reason": "数据错误"
    },

    # 明确的需求
    {
        "question": "希望能支持暗黑模式",
        "description": "晚上使用太刺眼了",
        "expected": "feature",
        "reason": "新功能建议"
    },
    {
        "question": "建议增加批量删除功能",
        "description": "现在只能一个一个删除",
        "expected": "feature",
        "reason": "功能改进"
    },
    {
        "question": "希望能够导出为Word格式",
        "description": "现在只支持PDF",
        "expected": "feature",
        "reason": "格式扩展"
    },

    # 明确的使用问题
    {
        "question": "找不到导出按钮在哪里",
        "description": "看遍了菜单都没找到",
        "expected": "usage",
        "reason": "不知道如何操作"
    },
    {
        "question": "怎么修改接口的路径？",
        "description": "不知道在哪里设置",
        "expected": "usage",
        "reason": "配置问题"
    },

    # 模糊场景1：可能被误判
    {
        "question": "导出功能太慢了",
        "description": "导出1000条数据要等很久",
        "expected": "bug",  # 性能问题
        "reason": "可能是性能bug，也可能是需求要优化"
    },
    {
        "question": "界面有点丑",
        "description": "颜色搭配不太好",
        "expected": "feature",  # 需求建议
        "reason": "UI改进需求"
    },
    {
        "question": "每次都要重新登录，很麻烦",
        "description": "token过期太快了",
        "expected": "bug",  # 可能是bug
        "reason": "或者需要记住密码功能"
    },

    # 模糊场景2：描述不清
    {
        "question": "不行",
        "description": "就是不行",
        "expected": "unknown",
        "reason": "信息不足"
    },
    {
        "question": "有问题",
        "description": "遇到问题了",
        "expected": "unknown",
        "reason": "信息不足"
    },

    # 边界场景3：复合问题
    {
        "question": "我想用API但是找不到文档，而且示例代码也报错",
        "description": "两方面问题",
        "expected": "usage",  # 优先级：使用问题
        "reason": "找不到文档是usage，报错是bug"
    },
    {
        "question": "希望增加批量操作，同时现在的单选也不太好用",
        "description": "两个问题",
        "expected": "feature",  # 优先级：需求
        "reason": "批量操作是feature，单选问题可能是usage"
    },

    # 边界场景4：特殊格式
    {
        "question": "500 Internal Server Error",
        "description": "服务器返回错误",
        "expected": "bug",
        "reason": "明确的错误码"
    },
    {
        "question": "404 Not Found",
        "description": "页面找不到",
        "expected": "bug",
        "reason": "明确的错误码"
    },

    # 边界场景5：长描述
    {
        "question": "我在使用这个产品的时候，发现了一个很严重的问题，就是在大量数据并发处理的时候，会出现内存溢出的情况，导致整个系统崩溃，需要重启才能恢复",
        "description": "详细的bug描述",
        "expected": "bug",
        "reason": "明确的崩溃问题"
    },

    # 边界场景6：需求变bug
    {
        "question": "这个功能和我想的不一样",
        "description": "我以为会是另一种效果",
        "expected": "usage",  # 可能是理解偏差
        "reason": "或者需求不匹配"
    },
    {
        "question": "能不能把字号调大一点",
        "description": "现在太小了看不清",
        "expected": "feature",
        "reason": "功能改进，但也可能是usage有设置"
    },

    # 边界场景7：技术术语
    {
        "question": "API返回的JSON格式不对",
        "description": "字段类型错误",
        "expected": "bug",
        "reason": "数据格式问题"
    },
    {
        "question": "OAuth认证总是失败",
        "description": "token无效",
        "expected": "bug",
        "reason": "认证问题"
    },
]

async def run_stress_test():
    """运行压力测试"""

    print(f"\n开始测试 {len(test_cases)} 个场景...")
    print("=" * 80)

    results = {
        "total": len(test_cases),
        "correct": 0,
        "wrong": 0,
        "unknown": 0,
        "low_confidence": 0,
        "details": []
    }

    for i, test in enumerate(test_cases, 1):
        print(f"\n[测试 {i}/{len(test_cases)}]")
        print(f"问题: {test['question']}")
        print(f"期望: {test['expected']} ({test['reason']})")

        # LLM分类
        try:
            classification = await classifier.classify(
                question=test['question'],
                context="",
                additional_info={"description": test['description']}
            )

            predicted = classification['type']
            confidence = classification['confidence']

            # 判断是否正确
            is_correct = (predicted == test['expected'])
            is_low_confidence = (confidence < 0.7)

            if is_correct:
                results['correct'] += 1
                status = "✅"
            else:
                results['wrong'] += 1
                status = "❌"

            if test['expected'] == 'unknown':
                results['unknown'] += 1

            if is_low_confidence:
                results['low_confidence'] += 1
                status += " ⚠️低置信度"

            # 显示结果
            print(f"预测: {predicted} (置信度: {confidence:.0%}) {status}")
            print(f"理由: {classification['reason'][:100]}...")

            # 记录详情
            results['details'].append({
                "question": test['question'],
                "expected": test['expected'],
                "predicted": predicted,
                "confidence": confidence,
                "correct": is_correct,
                "low_confidence": is_low_confidence
            })

        except Exception as e:
            print(f"❌ 分类失败: {e}")
            results['wrong'] += 1

    # 统计结果
    print("\n" + "=" * 80)
    print("测试结果统计")
    print("=" * 80)

    accuracy = results['correct'] / results['total'] if results['total'] > 0 else 0

    print(f"\n总测试数: {results['total']}")
    print(f"正确: {results['correct']} ({accuracy:.1%})")
    print(f"错误: {results['wrong']}")
    print(f"未知: {results['unknown']}")
    print(f"低置信度: {results['low_confidence']}")

    # 错误案例分析
    if results['wrong'] > 0:
        print("\n" + "=" * 80)
        print("错误案例分析")
        print("=" * 80)

        for detail in results['details']:
            if not detail['correct']:
                print(f"\n问题: {detail['question']}")
                print(f"期望: {detail['expected']}")
                print(f"预测: {detail['predicted']}")
                print(f"置信度: {detail['confidence']:.0%}")

    # 低置信度案例
    if results['low_confidence'] > 0:
        print("\n" + "=" * 80)
        print("低置信度案例（<70%）")
        print("=" * 80)

        for detail in results['details']:
            if detail['low_confidence']:
                print(f"\n问题: {detail['question']}")
                print(f"预测: {detail['predicted']}")
                print(f"置信度: {detail['confidence']:.0%}")

    # 评估
    print("\n" + "=" * 80)
    print("评估")
    print("=" * 80)

    if accuracy >= 0.9:
        print("✅ 优秀！准确率 >= 90%，系统可用")
    elif accuracy >= 0.8:
        print("⚠️ 良好，准确率 80-90%，需要优化提示词")
    elif accuracy >= 0.7:
        print("❌ 及格，准确率 70-80%，需要调整策略")
    else:
        print("❌ 不及格，准确率 < 70%，需要重新设计")

    if results['low_confidence'] > results['total'] * 0.2:
        print(f"\n⚠️ 警告：{results['low_confidence']}个案例置信度低于70%，可能需要调整")

    # 保存结果
    from pathlib import Path
    Path("data/test_results").mkdir(parents=True, exist_ok=True)
    result_file = f"data/test_results/stress_test_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"

    import json
    with open(result_file, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

    print(f"\n结果已保存: {result_file}")

if __name__ == "__main__":
    asyncio.run(run_stress_test())
