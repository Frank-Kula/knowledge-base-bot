# 基本概念

本节介绍了 Apifox 中的一些核心概念，这些概念与其它类似产品 *（如 Postman）* 可能有所不同，理解这些定义和区别，有助于更好地掌握 Apifox 的工作流程，帮助你快速上手。

## 文档模式/调试模式

Apifox 的 API 调试有两种模式，可以在界面左下角切换，分别是：`文档模式` 和 `调试模式`。


<Background>
<p style="text-align: center">
    <img src="https://api.apifox.com/api/v1/projects/5097254/resources/478886/image-preview" style="width: 640px" />
</p>
</Background>



这两种模式提供了类似的功能，但界面不同，以适应不同团队的工作流程。

**文档模式**是 Apifox 推荐的模式，适合采用 API 设计优先的团队。在这个模式中，团队优先定义 API，随后根据 API 文档进行开发和测试。


<Background>
<p style="text-align: center">
    <img src="https://api.apifox.com/api/v1/projects/5097254/resources/505429/image-preview" style="width: 540px" />
</p>
</Background>


**调试模式**则特别适合那些没有事先定义 API 文档的团队。这样的团队通常集中在后端开发，先完成代码，然后再生成 API 文档进行测试工作。

<Background>
<p style="text-align: center">
    <img src="https://api.apifox.com/api/v1/projects/5097254/resources/505431/image-preview" style="width: 540px" />
</p>
</Background>


如果需要调用其他人开发的 API 而没有文档，建议也使用调试模式。


:::tip[]
了解更多[文档/调试模式](https://docs.apifox.com/design-and-request-mode.md)的知识。
:::

## 接口

Apifox 是一个以 API *（接口）* 为核心的产品，这意味着所有操作都从定义 API 开始。

<Background>

![CleanShot 2025-03-20 at 17.20.43@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/505485/image-preview)
</Background>



在 Apifox 的主界面中，接口是基本元素，它们以目录的形式进行分组。对于每个接口，你可以进行修改、预览、发送请求，或者将请求保存为[接口用例](https://docs.apifox.com/api-test-cases.md)。


这种结构与 Postman 大不相同，Apifox 更像是一种基于 <Tooltip tip="即 OpenAPI Specification，一种用于描述和定义 RESTful API 的标准化格式">OAS</Tooltip> 的扩展——你可以直接调试和保存请求。


在 Postman 中，基本元素是 “请求”，而这些请求与 <Tooltip tip="即 API specification，也称 OpenAPI/Swagger 规范，在 Apifox 中表示接口文档，是定义和描述 API 行为的关键文档或标准">API 定义</Tooltip>本身是分离的。这意味着当 API 定义发生变化时，所有的请求和脚本都需要重新编写。


在 Apifox 中，所有的接口用例 *（对应 Postman 的请求）* 都是基于 “API 定义” 的。当 API 定义发生变化时，接口用例会同步变化，所有基于此的测试场景和 CI/CD 也可以自动或手动更新，非常适合开发团队在维护和更新 API 时使用。

## 快捷请求

在 Apifox 中，你也可以创建[快捷请求](https://docs.apifox.com/quick-request.md)。这些快捷请求不需要基于 API 定义进行设计，其方式与 Postman 请求相同。你还可以[将成功的请求保存为接口文档](https://docs.apifox.com/extract-response-example.md)。

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/505501/image-preview)
</Background>



## 测试场景

当你需要批量发送请求时 *（类似运行 Postman Collection）*，你可以使用自动化测试来编排测试场景。


<Background>

![CleanShot 2025-03-20 at 17.32.07@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/505502/image-preview)
</Background>

一个测试场景包括一系列测试步骤。这些测试步骤可以从[接口或接口用例中导入到测试场景](https://docs.apifox.com/create-test-scenario.md)，并可以[在接口文档发生变化时自动或手动更新](https://docs.apifox.com/sync-from-endpoint-or-test-case.md)相应的参数。

测试场景还支持[流程控制条件](https://docs.apifox.com/flow-control-conditions.md)如 If、for、forEach 等。你可以在[测试步骤间传递数据](https://docs.apifox.com/pass-data-between-test-steps.md)、[动态生成请求参数](https://docs.apifox.com/dynamic-values.md)。

基于测试场景，你还可以查看[测试报告](https://docs.apifox.com/test-reports.md)、[运行性能测试](https://docs.apifox.com/performance-testing.md)、[管理测试数据](https://docs.apifox.com/data-driven-testing.md)、[集成 CI/CD](https://docs.apifox.com/cicd.md) 等。

## 环境

Apifox 中的 [环境](https://docs.apifox.com/environments-and-variables.md) 与 Postman 中的环境类似，包含许多变量。切换环境时，可以使用相同环境变量的不同值。然而，Apifox 的环境还包括另一个重要概念：[前置 URL](https://docs.apifox.com/environments-and-services.md)。

在 Apifox 中，**前置 URL** 是接口请求地址中的基础部分，与接口路径拼接后，构成请求最终发送的完整 URL。一个环境可以配置多个前置 URL，以支持多服务、微服务架构等情况下的接口管理需求。

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/542677/image-preview)
</Background>


这与 OpenAPI（Swagger）规范是一致的。OpenAPI 中接口路径通常以 `/` 开头，而完整请求地址由 **“前置 URL + 接口路径”** 拼接而成。

也就是说，你只需在接口中填写路径部分（如 `/user`），Apifox 会根据接口所属模块，自动拼接对应模块在当前环境下配置的前置 URL，形成完整请求地址。

例如，项目中有三个模块，在“正式环境”中，每个模块对应的 **名称** 和 **前置 URL** 如下：
 
* 用户服务：`https://user.example.com`
* 订单服务：`https://order.example.com`
* 商品服务：`https://product.example.com`

每个模块下各有一个接口路径：

* 用户服务中的接口：`GET /user/{id}`
* 订单服务中的接口：`GET /order/{id}`
* 商品服务中的接口：`GET /product/{id}`

当你切换到正式环境时，这三个接口的实际请求地址将自动拼接为：

* `https://user.example.com/user/{id}`
* `https://order.example.com/order/{id}`
* `https://product.example.com/product/{id}`

<Background>

![CleanShot 2025-07-07 at 14.07.25@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/542756/image-preview)
</Background>

你无需在 URL 中手动写 `{{BaseUrl}}` 变量，也不必为每个模块重复创建环境。Apifox 会根据接口所属模块，在当前环境中查找对应的前置 URL，自动拼接成完整的请求地址。

## 模块

在一个 Apifox 项目中，你可以使用 [模块](https://docs.apifox.com/module.md) 来对你项目中的接口进行组织。模块与技术领域中的 “服务” 概念类似，意在帮助微服务架构等场景下的接口能够更好的进行管理。每个模块拥有一套相关的业务**接口**、**组件**（数据模型、响应、鉴权）、**前置 URL**（每个环境均有一个），对应一份完整独立的 Swagger/OpenAPI 规范文件。

<Background>
<img src="https://api.apifox.com/api/v1/projects/5097254/resources/542706/image-preview" width="460px" />
</Background>

在导入/导出数据时，除了 Apifox 格式之外，其他大部分格式都是对一个模块进行导入/导出操作的。这样与 OAS 更好的对应，让 Apifox 中管理的接口更遵从通用标准，能与其他的产品或 AI 更好的集成。

每个项目在创建时即拥有一个默认模块。在环境管理中，如果你需要在一个环境中使用多个前置 URL，建议你通过新建模块的方式来实现。某个模块下的所有接口，实际请求时会发送至该模块对应的前置 URL 中。

## 项目

模块（接口、组件）、环境、测试场景等的集合构成了一个项目。在 Apifox 中，项目是协作的基本单位。一个项目对应多套 API 定义 *（<Tooltip tip="也称 OpenAPI/Swagger 规范，在 Apifox 中表示接口文档。">API specification</Tooltip>）*。与 Postman 相比，Apifox 项目大致相当于 Postman 的 Workspace，项目中的一个模块对应一个 Collection 文件夹。而 Apifox 团队则类似于 Postman 的 Team。
