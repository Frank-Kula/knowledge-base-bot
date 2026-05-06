# 新建接口

在 Apifox 中，设计和配置 API 是创建强大且高效 API 的基础环节。

建议遵循 [OAS *（OpenAPI 规范 ）*](https://swagger.io/specification/) 来设计接口，以确保在 OpenAPI 生态系统中的各种工具和服务之间具有良好的兼容性。如果偏离了 OAS，在使用 OpenAPI 兼容的工具和服务时可能会出现兼容性问题。

要在 `接口管理` 模块中创建新接口，点击 `新建接口` 按钮。

<Background>
<img src="https://api.apifox.com/api/v1/projects/5097254/resources/588479/image-preview" style="width: 640px" />
</Background>


清晰完整的接口应包含以下要素：

1. 接口路径
2. 请求方法
3. 接口描述信息
4. 请求参数
5. 返回响应和示例

<Background>

![CleanShot 2024-11-08 at 14.03.35@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/476062/image-preview)
</Background>

:::tip[]
Apifox 的接口界面提供两种模式：`文档模式`（以设计为主）和 `调试模式`（以代码为主）。可以在界面左下角切换模式。本文基于 `文档模式` 。了解更多关于[文档/调试模式](https://docs.apifox.com/design-and-request-mode.md)的信息。
:::

## 接口路径

接口路径是 API 与外部应用进行交互的特定地址，客户端会通过该地址访问 API 服务。

<Frame>
    <img src="https://api.apifox.com/api/v1/projects/5097254/resources/476064/image-preview" style="width: 640px" />
</Frame>

不同于 Postman，Apifox 推荐遵循 OpenAPI 规范，接口里只需填写 Path，无需填写完整的 URL，“前置 URL（Base URL） ”放到环境里，运行时 Apifox 会自动将“前置 URL ”加到 Path 前，Path 里无需额外添加变量。

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/517502/image-preview)
</Background>

Apifox 推荐遵循 OpenAPI 规范，接口路径（Path） 以`/`起始，使接口更规范，并且使用 Apifox 过程中能获得更好更完整的功能体验。

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/517504/image-preview)
</Background>

:::tip[推荐路径以 `/` 开头的原因]

- 按照 OAS 规范，以 `/` 开头路径有助于在 OpenAPI 生态中的兼容性。如果路径没有以 `/` 开头，在使用工具时可能会遇到兼容性问题。
- 此外，以 `/` 开头的路径支持 URL 模式 Mock 功能，这对 Apifox 的测试和验证功能非常重要。
:::

## 请求方法

请求方法决定了客户端如何与服务端资源交互。每种方法具有其独特的含义，并会触发服务器的不同响应。设计 API 时，根据业务需求选择合适的请求方法，以有效实现预期操作。


<Frame>
 <p style="text-align: center">
    <img src="https://api.apifox.com/api/v1/projects/5097254/resources/476066/image-preview" style="width: 140px" />
</p>
</Frame>




以下是常用的 API 请求方法：

1. **GET**：获取指定资源，通过 Query 参数传递数据。
2. **POST**：提交数据进行处理，通常将数据放在请求体中。
3. **PUT**：完整更新或替换指定资源。
4. **DELETE**：删除指定资源。
5. **OPTIONS**：查询目标资源支持的 HTTP 方法。
6. **HEAD**：与 GET 类似，但仅返回响应头，用于检查资源存在及修改情况。
7. **PATCH**：部分更新指定资源。
8. **TRACE**：返回服务器收到的请求，用于调试和诊断。
9. **CONNECT**：建立到服务器的隧道，通常用于代理服务器的请求转发。

## 接口描述信息

在 Apifox 中，每个接口都包含一组默认的描述信息字段，用于规范和管理 API 的文档、可访问性以及生命周期。

<Background>   
![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/476071/image-preview)
</Background>

以下是各默认描述信息字段的简要说明：

- **命名**  
接口的描述性名称，用于概述接口的功能。
- **可见性**
该接口文档的可见性，方便灵活控制项目资源的访问权限。
- **状态**  
默认为 “开发中”，可在[接口状态](https://docs.apifox.com/api-status.md)下更改，标识不同阶段如 “测试中” 或 “已发布”。
- **责任人**  
指定负责该接口的成员，可以从项目成员中选择用户分配此角色。
- **标签**  
关键词或短语，用于对接口进行分类或描述。可以键入新标签或从已有标签中选择。
- **服务（前置 URL）**  
接口路径的基础 URL，默认为“继承自父级”，也可以通过界面右上角的环境设置手动指定。
    :::highlight purple
    了解更多关于[环境与服务](https://docs.apifox.com/environments-and-services.md)。
    :::
- **OperationId**  
在 API 中帮助区分该操作的唯一标识符 *（OAS 中的 operationId）*。
- **说明**  
详细说明接口的目的及用途，支持 Markdown 格式。

:::highlight purple
除默认描述信息字段外，还可以灵活添加[自定义字段](https://docs.apifox.com/api-fields.md)，以进一步完善接口描述信息。
:::

## 请求参数


请求参数用于控制数据返回或修改服务器响应的选项。

<Background>
    <img src="https://api.apifox.com/api/v1/projects/5097254/resources/476077/image-preview" style="width: 640px" />
</Background>


请求参数包括查询参数 *（Query）*、路径参数 *（Path）*、请求头参数 *（Header）* 和请求体参数 *（Body）*。

### Query 参数

查询参数是键值对，在 URL 末尾以 `?` 开始，以 `&` 分隔，例如：`?id=2&status=available`。通常用于筛选、排序或修改 API 的输出。

:::tip[]
在 Apifox 中，Query 参数独立描述以保持清晰。但在发送请求时，这些 Query 参数会拼接在接口路径后面。
:::

### Path 参数

Path 参数是接口 URL 中的一部分，用于识别 API 中的特定资源或实体。

在 Apifox 中，Path 参数用 **单大括号** 表示而非冒号。例如，


<TipGood> **正确示例**</TipGood>
`/pet/{petId}`
<TipBad>
    **错误示例**
</TipBad>
`/pet/:petId`


只要你在 URL 栏输入`{参数名}`，Apifox 就会自动识别，并在下方自动显示对应的参数输入框。
<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/595357/image-preview)
</Background>

如果你需要在 URL 路径里使用变量，建议的写法是：**URL 保持标准的 `{}` 占位符格式，变量只写在 Path 参数的 “参数值” 中**。


<TipGood>推荐的写法：在 Path 参数的参数值里引用变量</TipGood>


<Steps>
  <Step>
        在 URL 栏保留占位符格式，例如 `/pet/{petId}`
  </Step>
  <Step>
    在 Path 参数列表中找到 `petId`，在 “参数值” 里使用**双大括号 `{{}}`** 填入变量名，例如 `{{petId}}`。这样就相当于在 URL 路径里使用变量了。
  </Step>
</Steps>

<Frame>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/579049/image-preview)
</Frame>


<TipBad>
    不推荐的写法：把变量直接写在 URL 栏里
    
</TipBad>

直接在路径中使用变量`{{}}`会影响 Apifox 的 Mock API 功能的使用。另外，这种写法不符合 OAS 规范，无法在 OpenAPI 生态的工具中正常集成。因此，**不推荐**在 URL 上直接写变量，例如 ~~`/pet/{{petId}}`~~。

<Frame>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/579050/image-preview)
</Frame>


:::tip[区分 `{parameter}` 和 `{{variable}}`]

- `{parameter}`：单大括号表示 Path 参数，是 URL 路径中的占位符，当访问接口时会替换为具体的值。
- `{{variable}}`：双大括号用于在请求中引用变量，请求发送时可替换为实际值，实现动态和自定义输入。
:::



### 请求头参数

请求头参数提供关于请求的额外信息，通常用于认证、内容类型及其它元数据。

:::highlight purple
了解更多关于[请求头](https://docs.apifox.com/request-headers.md)。
:::

### 请求体参数

请求体参数包含请求体中的数据，通常用于 POST、PUT 和 PATCH 请求，用于创建或更新资源，数据通常以 JSON 或 XML 格式发送。

:::highlight purple
了解更多关于[请求体参数](https://docs.apifox.com/request-params-and-body.md)。
:::

### 参数描述

参数描述应包括名称、类型 *（如 string、integer、boolean 等）*、是否必填、默认值或约束条件。

描述参数时，常用以下关键属性：

1. **参数名**：指定参数名称，必填字段，应准确代表参数。
2. **类型**：定义参数值的数据类型，如 string、number、integer、boolean、array、object 等，便于理解请求数据的格式。
3. **说明**：简要说明参数的作用或使用方法。
4. **是否必需**：标识参数是否为必填项，为布尔值（`true` 或 `false`）。
5. **高级设置**：定义参数的数据类型、格式及约束，详细说明参数值的结构及内容。

:::highlight purple
可以使用 “数据模型” 功能轻松修改参数的高级设置。了解更多关于[数据模型](https://docs.apifox.com/build-data-schemas.md)。
:::

### 数据结构

当请求体参数类型为 `JSON` 或 `XML` 时，需要设置数据结构。数据结构可引用 `数据模型`。

:::highlight purple
了解更多关于数据结构，请参见[数据模型](https://docs.apifox.com/data-schemas.md)。
:::


## 返回响应和示例

在向 API 发送请求后，服务器会返回响应。定义预期的返回结果并提供示例，是让开发人员更好地理解和使用 API 的关键步骤。

<Background>
![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/476079/image-preview)
</Background>

返回结果的定义主要包括以下几个部分：

1. **HTTP 状态码**：确定接口可能返回的所有状态码，包括常见的 200（OK）、404（Not Found）和 500（Server Error）等。
2. **数据格式**：为每个状态码定义返回结果的数据格式，可以是 `JSON`、`XML`、`HTML`、`Raw`、`Binary` 或其他适合的格式。
3. **数据结构**：对于携带数据的响应（主要是状态码 200 的情况），详细描述返回的数据结构。这包括指定类型、嵌套对象、可选字段和数组。清晰的定义能帮助客户端开发人员了解应期望的数据及其解析方式。仅 `JSON` 和 `XML` 格式可以配置数据结构。

    :::highlight purple
    关于 “数据结构” 的详细信息，请参考[构建数据模型](https://docs.apifox.com/build-data-schemas.md)。
    :::

4. **示例**：提供示例响应对于展示 API 在实际场景中的表现至关重要。理想情况下，示例应基于预定义请求，展示服务器返回的数据集。示例应该准确反映响应的数据结构、格式和类型，确保与响应的数据结构定义一致。

### 添加返回响应

通常建议在 API 文档中为每个接口至少定义一个成功响应和一个错误响应。这种实践可以全面覆盖不同可能的结果，帮助开发人员清晰了解 API 在各种场景下的表现。

点击 `返回响应` 模块右上角的 `+ 添加` 按钮，即可添加返回响应。

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/476080/image-preview)
</Background>

通常在 API 设计中，成功的 `200 OK` 响应因各个接口的输出需求不同而有所差异，但错误响应如 `400 Bad Request` 和 `404 Not Found` 往往在不同接口间一致。Apifox 针对此类需求提供了[响应组件](https://docs.apifox.com/response-components.md)功能，可以复用预定义的错误响应，从而提高文档编写效率并保持 API 的一致性。


如果不需要 “响应组件”，可以选择 `添加空白响应` 来定义各接口独特的返回结果。

### 添加响应示例

在 Apifox 中，点击 “添加” 以增加响应示例。

一个响应可以包含多个不同的示例。在添加示例时，需要为示例命名并提供对应的响应数据。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/476081/image-preview)
</Background>


### 自动生成示例
点击 `自动生成`，Apifox 会根据 “返回响应的数据结构” 定义自动生成合理的响应数据。

<Background>
![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/476082/image-preview)
</Background>

## 预览接口

完成接口设计后，点击 “确定” 保存更改，然后切换到 “接口” 标签页预览刚刚配置的接口。
