# 自动化测试

测试是保障 API 可靠性的核心。它不仅能验证功能逻辑，还能确保模块集成顺畅，并帮助你在 API 上线前发现潜在的性能瓶颈。

## API 测试类型

Apifox 支持涵盖全生命周期的测试场景：

1. **[集成测试](https://docs.apifox.com/integration-testing.md)**：验证多模块或外部系统间的协同工作，确保微服务交互的准确性。
2. **[端到端测试](https://docs.apifox.com/end-to-end-testing.md)**：模拟真实用户操作路径，评估完整业务流程的可用性。
3. **[回归测试](https://docs.apifox.com/regression-testing.md)**：在功能迭代后快速验证现有业务逻辑，防止新代码引入故障。
4. **[性能测试](https://docs.apifox.com/performance-testing.md)**：评估 API 在高负载下的表现，分析响应时间与资源消耗。
5. **[契约测试](https://docs.apifox.com/contract-testing.md)**：校验接口实际返回结果是否符合 OpenAPI 规范。

## 自动化测试

Apifox 的自动化测试通过**场景用例**实现。它类似于 Postman 的 Flows，允许你将多个接口或用例组合在一起，并利用 `If`、`For`、`Wait` 等流程控制组件编排复杂的业务逻辑。


<Background>

![CleanShot 2026-02-09 at 12.13.44@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/622954/image-preview)
</Background>


## 快速开始

依照以下步骤快速上手自动化测试：

<Steps>
  <Step title="创建场景用例">
    新建场景并从 API 文档导入接口、用例或添加自定义请求。[了解更多](https://docs.apifox.com/new-test-scenario.md)
  </Step>
  <Step title="步骤间数据传递">
    配置变量提取，将前序步骤的响应输出传递给后续请求。[了解更多](https://docs.apifox.com/pass-data-between-test-steps.md)
  </Step>
  <Step title="编排测试流程">
    通过 If、For、Wait 等逻辑组件设计复杂的自动化执行分支。[了解更多](https://docs.apifox.com/flow-control-conditions.md)
  </Step>
  <Step title="运行与验证">
    一键执行场景，实时查看每个步骤的执行细节与断言结果。[了解更多](https://docs.apifox.com/run-test-scenarios.md)
  </Step>
  <Step title="分析测试报告">
    查看自动生成的详细报告，快速定位失败原因或性能异常。[了解更多](https://docs.apifox.com/test-reports.md)
  </Step>
  <Step title="扩展：性能测试">
    直接使用场景用例发起并发压力测试，评估系统负载上限。[了解更多](https://docs.apifox.com/performance-testing.md)
  </Step>
  <Step title="集成 CI/CD">
    通过 CLI 工具将测试流程无缝接入持续集成流水线。[了解更多](https://docs.apifox.com/cicd.md)
  </Step>
</Steps>
