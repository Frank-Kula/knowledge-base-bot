# CI/CD 集成

持续集成和持续交付（CI/CD）是 API 开发工作流程中的重要组成部分。Apifox 支持与主流 CI 工具集成，让你能在设计和测试 API 的同一个平台中直接监控 API 的构建。

你可以通过 Apifox CLI 在 CI 流水线中执行 Apifox 中创建的 API 场景用例。

## 开始使用

<Steps>
  <Step>
在自动化测试模块中[新建场景用例](https://docs.apifox.com/new-test-scenario.md)并调试，直到测试通过。
    </Step>
  <Step>
切换到 CI/CD 标签页，配置运行环境、测试数据和其它必要配置项。

:::highlight purple
了解更多 [Apifox CLI 命令选项](https://docs.apifox.com/cli-command-options.md)。
:::
    </Step>
  <Step>
选择你的 CI/CD 平台，复制对应的命令到你的 CI/CD 平台中进行配置。

<Background>

![CleanShot 2024-12-10 at 16.52.20@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/482776/image-preview)
</Background>

    </Step>
  <Step>
运行流水线，在 CI/CD 平台中查看结果。
    </Step>
</Steps>

## 支持的 CI/CD 平台

Apifox 支持多个 CI/CD 平台，包括：

- **Jenkins**
- **GitLab**
- **GitHub Actions**
- **Azure Pipelines**
- **Bitbucket Pipelines**
- **CircleCI**
- **Travis CI**

如果你使用的 CI/CD 平台不在上述列表中，你仍然可以使用 “命令行” 选项中提供的代码来配置 CI/CD。
