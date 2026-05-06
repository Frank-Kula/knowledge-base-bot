# 生成代码

根据 API 定义 *（<Tooltip tip="也称 OpenAPI/Swagger 规范，在 Apifox 中表示接口文档。">API specification</Tooltip>）*，Apifox 支持自动生成多种语言和框架的业务代码，包括但不限于 TypeScript、Java、Go、Swift、ObjectiveC、Kotlin、Dart、C++、C#、Rust 以及其他 130 种语言和框架。


Apifox 提供三种代码生成类型：**生成业务代码**、**生成接口请求代码**和**生成数据模型代码**。

- **生成业务代码**：面向 API 开发者，生成用于实现 API 功能的服务器端代码。业务代码专注于 API 的服务端实现，与用于与 API 交互的接口请求代码不同。  
- **生成接口请求代码**：为 API 使用者生成客户端代码，用于在不同编程语言中实现与服务端 API 的交互。  
- **生成数据模型代码**：用于定义数据结构，适用于 API 数据的序列化（发送数据时）与反序列化（接收数据时）处理。

## 生成业务代码


### 如何生成

**1. 安装代码生成插件**

在接口文档中点击 `生成代码`，选择 `生成业务代码`。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/478895/image-preview)
</Background>


如果没有安装代码生成插件，需要在业务代码生成页面，点击 `下载并安装` 按钮。

<Background>

![CleanShot 2025-12-01 at 16.29.36@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/599774/image-preview)
</Background>


如果你的网络无法访问外网，请手动下载 `openapi-generator-cli-7.13.0.jar`，下载地址：
[`https://repo1.maven.org/maven2/org/openapitools/openapi-generator-cli/7.13.0/openapi-generator-cli-7.13.0.jar`](https://repo1.maven.org/maven2/org/openapitools/openapi-generator-cli/7.13.0/openapi-generator-cli-7.13.0.jar)

并将这个 JAR 包放到对应系统的目录下：
- **macOS**: `~/Library/Application Support/apifox/`
- **Windows**: `C:\Users\<用户名>\AppData\Roaming\apifox\`
- **Linux**: `~/.config/apifox/`

插件会自动识别并使用本地 JAR，无需联网下载。

<Background>
<img src="https://api.apifox.com/api/v1/projects/5097254/resources/599773/image-preview" width="460px" />
</Background>



**2. 生成代码**

选择所需的业务代码，然后点击 `生成代码`。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/478897/image-preview)
</Background>


**3. 使用自定义模板**

你还可以使用**自定义模板**功能生成符合团队架构规范的代码，以满足各种个性化需求。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/478898/image-preview)
</Background>



### 支持的语言/框架

| 语言 | 服务端/客户端 | 框架 |   
|-|-|-|
| Java | 服务端 | Spring、Inflector、Msf4j、Pkmst、Play Framework、Undertow Server、Vertx、Vertx Web、JAX-RS Cxf、JAX-RS Cxf Cdi、JAX-RS Cxf Extended、JAX-RS Jersey、JAX-RS Resteasy、JAX-RS Resteasy Eap、JAX-RS Spec |
| Java | 客户端 | Android、Java |
| PHP | 服务端 | Laravel、Lumen、Symfony、Ze Ph、Slim4、Slim（已弃用）、Silex（已弃用） |
| PHP | 客户端 | PHP |
| Swift | 客户端 | Swift5、Swift4、Swift3（已弃用）、Swift2（已弃用） |
| Kotlin | 服务端 | Kotlin Server、Kotlin Spring、Kotlin Vertx |
| Kotlin | 客户端 | Kotlin |
| JavaScript | 客户端 | Apollo、Flowtyped、Closure Angular |
| Node.js | 服务端 | Express、GraphQL Express |
| TypeScript | 客户端 | Axios、Fetch、Redux Query、Angular、Angularjs、Jquery、Rxjs、Node、Aurelia、Inversify |
| C++ | 服务端 | Pistache Server、Qt5 Qhttpengine Server、Restbed Server |
| C++ | 客户端 | Qt5 Client、Restsdk、Tizen |
| C# | 服务端 | C# Nancyfx |
| C# | 客户端 | C#、C# Netcore、C# Dotnet2 |
| ASP.NET | 服务端 | ASP.NET Core |
| Dart | 客户端 | Dart、Dart Dio、Dart Jaguar |
| Go | 服务端 | Go Server、Go Gin Server |
| Go | 客户端 | Go、Go（实验性） |
| C | 客户端 | C |
| Objective-C | 客户端 | Objective-C |
| Scala | 服务端 | Scala Akka Http Server、Scala Finch、Scala Lagom Server、Scala Play Server |
| Scala | 客户端 | Scala Akka、Scala Gatling、Scala Sttp、Scalaz、Scala Httpclient（已弃用） |
| Clojure | 客户端 | Clojure |
| Groovy | 客户端 | Groovy |
| Python | 服务端 | Python Aiohttp、Python Blueplanet、Python Flask |
| Python | 客户端 | Python、Python（实验性） |
| Rust | 服务端 | Rust Server |
| Rust | 客户端 | Rust |
| Ruby | 服务端 | Ruby On Rails、Ruby Sinatra |
| Ruby | 客户端 | Ruby |
| R | 客户端 | R |
| Perl | 客户端 | Perl |
| PowerShell | 客户端 | PowerShell |
| JMeter | 客户端 | JMeter |
| Bash | 客户端 | Bash |
| Lua | 客户端 | Lua |
| F# | 服务端 | F# Functions、F# Giraffe Server |
| OCaml | 客户端 | OCaml |
| Erlang | 服务端 | Erlang Server |
| Erlang | 客户端 | Erlang Client、Erlang Proper |
| Flash | 客户端 | Flash |
| Elixir | 客户端 | Elixir |
| Haskell | 服务端 | Haskell |
| Haskell | 客户端 | Haskell Http Client |
| Elm | 客户端 | Elm |
| Nim | 客户端 | Nim |
| Ada | 服务端 | Ada Server |
| Ada | 客户端 | Ada |
| Apex | 客户端 | Apex |
| Eiffel | 客户端 | Eiffel |

:::tip[]
Apifox 的代码模板功能基于 OpenAPI Generator，但经过简化。
:::

## 生成接口请求代码

接口请求代码用于在各种开发环境中发起 API 请求。点击 API 文档中的 `生成接口请求代码` 按钮。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/478899/image-preview)
</Background>


你也可以通过在 API 的运行标签中点击代码图标 `</>` 来生成代码。

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/478900/image-preview)
</Background>


注意：通过上述方法生成的接口请求代码将**仅包含** API 定义，**不包含**请求参数值。如果你想生成包含请求参数值的接口请求代码，需先发送请求，然后切换到返回响应面板的 `实际请求` 标签。向下滚动查找包含参数值的接口请求代码。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/478901/image-preview)
</Background>


### 支持的语言

| 语言 | 框架/库        |
|-----------|---------------|
| Shell | cURL、cURL-Windows、Httpie、wget、PowerShell |
| JavaScript | Fetch、Axios、jQuery、XHR、Native、Request、Unirest |
| Java | Unirest、OkHttp |
| Swift | URLSession | 
| Go | Native | 
| PHP | cURL、Guzzle、pecl_http、HTTP_Request2 |
| Python | http.client、Requests |
| HTTP | HTTP | 
| C | libcurl |
| C# | RestSharp | 
| Objective-C| NSURLSession|
| Ruby | Net::HTTP |
| OCaml | Cohttp | 
| Dart | http | 
| R | httr、RCurl |

## 生成数据模型代码

数据模型代码用于定义数据结构，常用于 API 发送数据时的序列化和接收数据时的反序列化处理。在生成 SQL 代码类型后，你还可以在数据库表创建场景中定义建表语句，以便在数据库中创建数据表。

要访问数据模型，可以在数据结构编辑组件中点击 `生成代码` 按钮。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/478902/image-preview)
</Background>


之后，你可以选择生成代码所需的编程语言，并配置特定的代码风格偏好。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/478903/image-preview)
</Background>


### 支持的语言

<Columns>
  <Column>
C#
C++
Crystal
Dart
Elm
  </Column>
  <Column>
Flow
Go
Haskell
Java
JavaScript
  </Column>
  <Column>
Kotlin
Objective-C
Pike
Python
Ruby
  </Column>
  <Column>
Rust
SQL
Swift
TypeScript
  </Column>
</Columns>

## 在线 API 文档生成代码

在 Apifox 生成的在线 API 文档中，你可以轻松生成 `接口请求代码` 和 `数据模型代码`。


<Background>

![CleanShot 2024-11-22 at 15.29.40@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/478906/image-preview)
</Background>

