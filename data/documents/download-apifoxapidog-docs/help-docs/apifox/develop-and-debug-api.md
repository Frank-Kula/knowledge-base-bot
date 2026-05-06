# 开发和调试 API

Apifox 旨在简化和高效地进行 API 调试，优化测试和开发流程。以下是 Apifox 核心调试功能的概述。

## 自动生成请求

Apifox 可以根据你的 API 定义自动生成请求参数和请求体，从而提高调试过程的准确性和效率。

- [**自动生成请求参数与请求体**](https://docs.apifox.com/request-params-and-body.md)

   根据你定义的接口自动生成对应的请求参数和请求体，不需要手动输入，减少人为错误，确保发送的请求与接口定义完全一致。
   
- **[通过“动态值”生成数据](https://docs.apifox.com/dynamic-values.md)**
    向请求中注入真实的动态值，模拟实际场景，帮助识别数据变更处理中的潜在问题。

-  [**将请求保存为接口用例**](https://docs.apifox.com/api-test-cases.md)

   把已调试好的接口请求直接保存，转换为可重复使用的接口用例，方便构建测试集合，编排测试场景。

## 便捷的可视化调试

通过 Apifox，你可以直观的调试你的接口，无需手动设置，确保 API 在不同场景下按预期工作。

- [**自动校验响应**](https://docs.apifox.com/validate-response.md)
   
   自动检查接口返回的响应，校验响应是否符合预先定义的数据结构，快速发现接口返回与预期不符的情况。
   
- [**可视化断言和变量提取**](https://docs.apifox.com/assertions.md)
   
    通过图形界面创建断言测试，可视化地从接口响应中提取需要的变量。
    
- [**兼容 Postman 脚本**](https://docs.apifox.com/scripts.md)

   完全支持并兼容 Postman 格式的脚本，可以直接导入现有的 Postman 脚本，让熟悉 Postman 的团队无缝切换。

## 独特功能

Apifox 提供独特的功能组件，使其在同类产品中脱颖而出，能够进行更全面的 API 测试，特别适合复杂项目。

- [**执行数据库操作**](https://docs.apifox.com/database.md)
   
   可以直接连接数据库，并在测试接口时执行数据库操作，支持数据库的增删改查功能。
   
- [**调用外部程序**](https://docs.apifox.com/call-external-programs.md)

   支持与多种编程语言集成，帮助团队根据需求扩展功能，自定义工作流程。
   
- [**兼容微服务场景**](https://docs.apifox.com/environments-and-services.md)

   适配微服务系统，帮助管理复杂的分布式 API，支持微服务间的切换测试。

## 其他功能

Apifox 还提供额外的功能组件和调试模式，以提升你的调试体验和 API 开发工作流。

- **[文档/调试模式](https://docs.apifox.com/design-and-request-mode.md)**
    
    支持在文档模式与调试模式之间自由切换，方便专注于撰写 API 定义或调试 API。
    

-  **[代码生成](https://docs.apifox.com/generate-code.md)**

    根据 API 定义自动生成请求代码和业务逻辑代码。
    
-  [**将快捷请求保存为接口**](https://docs.apifox.com/extract-response-example.md)

    自动分析已发送的快捷请求，可保存标准的接口文档，简化接口文档维护工作。


## 不同团队的最佳实践

### 对于以 API 设计为先的团队

一旦 API 设计完成，后端开发团队可以利用 API 定义 *（<Tooltip tip="也称 OpenAPI/Swagger 规范">API specification</Tooltip>）* 进行 API 的开发与调试。Apifox 提供以下开发和调试功能：

#### 开发前

- **[代码生成](https://docs.apifox.com/generate-code.md)**

    根据 API 定义自动生成请求代码和业务逻辑代码。

#### 开发后

- **[生成并发送 API 请求](https://docs.apifox.com/generate-request.md)**

  根据 API 定义生成请求。

- **[通过“动态值”生成数据](https://docs.apifox.com/dynamic-values.md)**

    向请求中注入真实的动态值，模拟实际场景，帮助识别数据变更处理中的潜在问题。

- **[环境与服务](https://docs.apifox.com/environments-and-services.md)**

    支持不同环境和服务的配置，允许开发者在开发、测试和生产环境之间切换。该功能为在各种条件下测试 API 提供了灵活性。

- [**自动校验响应**](https://docs.apifox.com/validate-response.md)
   
   自动检查接口返回的响应，校验响应是否符合预先定义的数据结构，快速发现接口返回与预期不符的情况。

- **[前后置操作](https://docs.apifox.com/pre-post-processors.md)**

    允许定义在发送 API 请求前后可以执行的脚本、断言、提取响应数据等操作。这些操作可以包括数据处理、错误处理或 API 响应处理等。

- **[使用脚本](https://docs.apifox.com/scripts.md)**

    开发者可以编写和执行脚本，实现高级定制和自动化的 API 开发与测试任务。脚本可用于执行复杂操作、与外部系统交互，或增强 API 请求和响应的功能。

- **[接口用例](https://docs.apifox.com/api-test-cases.md)**

    Apifox 中的接口用例是针对特定 API 接口预定义的测试用例，用于简化创建、管理和执行 API 测试的过程，以及将其集成到自动化测试工作流中。

### 对于以代码为先的团队

如果你的团队采用代码优先的开发方法，Apifox 提供了一系列支持这一工作流程的工具：

- **[IDEA 插件](https://docs.apifox.com/apifox-idea-plugin.md)**

    可以在 IDEA 环境中识别本地 Java、Kotlin 后端项目的源代码，自动生成 API 文档并一键同步到 Apifox 的项目中。

- **[定时导入](https://docs.apifox.com/scheduled-import.md)**

    提供自动从 Swagger 同步的功能，确保你的 API 文档与代码中的修改保持最新。

- **[调试模式](https://docs.apifox.com/design-and-request-mode.md)**

    借助调试模式特性，可以在调试过程中实时修改 API 定义，支持在开发和测试代码时对 API 进行迭代。

- **[动态值](https://docs.apifox.com/dynamic-values.md)**

    向请求中注入真实的动态值，模拟实际场景，帮助识别数据变更处理中的潜在问题。

- **[环境与服务](https://docs.apifox.com/environments-and-services.md)**

    支持不同环境和服务的配置，允许开发者在开发、测试和生产环境之间切换。该功能为在各种条件下测试 API 提供了灵活性。

- **[前后置操作](https://docs.apifox.com/pre-post-processors.md)**

    允许定义在发送 API 请求前后可以执行的脚本、断言、提取响应数据等操作。这些操作可以包括数据处理、错误处理或 API 响应处理等。

- **[使用脚本](https://docs.apifox.com/scripts.md)**

    开发者可以编写和执行脚本，实现高级定制和自动化的 API 开发与测试任务。脚本可用于执行复杂操作、与外部系统交互，或增强 API 请求和响应的功能。

- **[接口用例](https://docs.apifox.com/api-test-cases.md)**

    Apifox 中的接口用例是针对特定 API 接口预定义的测试用例，用于简化创建、管理和执行 API 测试的过程，以及将其集成到自动化测试工作流中。
