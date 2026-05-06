# gRPC 调试

gRPC 是一种高效、快速、可靠的远程过程调用（RPC, Remote Procedure Call）框架，在多种不同的场景都有着广泛的应用。在微服务架构中，gRPC 可以实现跨服务的高效通信。对于需要大量数据传输的场景，gRPC 可以使用流式传输功能，以减少网络传输延迟和带宽占用。

<Embed src="//player.bilibili.com/player.html?isOutside=true&aid=113525229886509&bvid=BV189BeYEEVF&cid=27187610713&p=1" width="720px" height="405px" />


:::tip[]
Apifox 版本号需大于等于 `2.3.0` 才能够使用 `gRPC` 接口调试功能。
:::

## 新建 gRPC 项目

点击 Apifox 首页的“新建项目”按钮，选择 “gRPC 项目（Beta）”。


<Background>

![CleanShot 2024-10-12 at 10.42.27@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/469933/image-preview)
</Background>


## 导入 Proto

gRPC 是一种 API-First 的 API 技术，这意味着在开发之前，必须先通过 `.proto` 文件来定义服务、方法和消息。因此，使用 Apifox 调试 gRPC 接口之前，也需要先导入作为 API 定义的 `.proto` 文件。 

### 首次导入

目前支持以下三种方式导入 `.proto` 文件：

- 本地文件
- 托管 `.proto` 文件的 URL
- 服务器反射（Server Reflection）


<Background>

![apifox-grpc-02.gif](https://api.apifox.com/api/v1/projects/5097254/resources/528311/image-preview)
</Background>


目标 `.proto` 文件会被导入为 1 个 `Proto`，其中 `service` 会被导入为服务，`rpc` 会被导入为方法。

如果选择的 `.proto` 文件依赖于其他 `.proto` 文件，那么需要手动添加依赖关系目录。

选择的 `.proto` 文件所依赖的其他 `.proto` 文件内的 `service`，如果其归属的 `package` 与选择的 `.proto` 文件的 `package` 相同，也会被导入到相同的 `Proto` 中。

### 重新导入

如果导入的 `.proto` 文件发生了变化，那么可以在 Apifox 内重新导入 `.proto` 文件：右键点击 `Proto`，然后点击重新导入按钮。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/469943/image-preview)
</Background>


## 调用方法

使用 `.proto` 文件定义 gRPC 的方法时，支持 4 种类型：

- Unary：一元调用
- Server Streaming：服务端流
- Client Streaming：客户端流
- Bidirectional Streaming：双向流

Apifox 支持全部 4 种方法的调用。

### 一元调用

一元调用类似于 HTTP 请求。在地址栏输入 URL，在 Message 标签下以 JSON 格式输入消息内容，点击“调用”按钮，即可发起一元调用。

此外，你也可以手动填写 Metadata 和 Auth 信息，以满足鉴权或其他复杂场景。

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/469944/image-preview)
</Background>

### 流式调用

流式调用类似于 WebSocket 连接。在发起调用之后，你可以在 Message 标签下撰写消息并发送。服务端流、客户端流与双向流皆属于流式调用类型。

Apifox 提供了一个时间线视图，按照时间顺序集中展示调用状态、发送的消息、收到的消息。点击消息之后，可以非常方便地查看消息的详情。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/469945/image-preview)
</Background>




## 进阶使用

### 自动生成动态值

Apifox 能够识别 `.proto` 文件中的内容，因此你可以点击“自动生成”按钮生成消息体。如果你需要使用更加灵活的动态数据，那么可以点击[动态值](https://docs.apifox.com/dynamic-values.md)功能配置并生成表达式。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/469946/image-preview)
</Background>


### 使用变量

你可以在 gRPC 的消息和 Metadata 中使用 Apifox 变量。


:::tip[]
详细说明请参考[使用变量](https://docs.apifox.com/global-environment-session-variables.md)。
:::



<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/469947/image-preview)
</Background>


### 启用 TLS

gRPC 接口支持通过 TLS 建立安全的连接。

使用 Apifox，你可以点击 URL 前面的协议选择器来快速切换 TLS 的状态。

此外，Apifox 也兼容在 URL 中使用 `grpcs://` 来为连接启用 TLS。与之相对应，`grpc://` 表示不启用 TLS。


<Background>
 
![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/469948/image-preview)
</Background>


## 管理服务器地址与环境

你可以点击 URL 地址栏右侧的加号图标，将当前正在使用的服务器地址添加到一个环境。


<Background>
![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/469949/image-preview)
</Background>


然后，在右上角选择环境和服务器地址，再在 URL 地址栏中选择“跟随默认”，就可以给所有方法使用统一的服务器地址来进行调试。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/469950/image-preview)
</Background>


## 查看 Proto 文件和接口参数

### 查看 Proto 文件内容

在 Apifox 中点击左侧目录树中的 `Proto` 即可查看 `.proto` 文件的原始内容。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/469951/image-preview)
</Background>


### 查看请求和响应的参数

gRPC 使用 ProtoBuf 作为序列化格式，这意味着在发送、接收消息时，每条消息都以 ProtoBuf 格式进行传输。与其他基于文本的序列化格式（JSON、XML）不同，ProtoBuf 是一种二进制格式，不适合人类进行书写、阅读。因此，在 Apifox 中调用 gRPC 接口时，所有消息都使用 JSON 格式来撰写、展示。

你可以在接口信息页面查看以 JSON 形式表示的请求参数和响应参数。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/469952/image-preview)
</Background>


ProtoBuf 和 JSON 的数据类型存在着映射关系，如下表所示：

| ProtoBuf 3             | JSON          | JSON 示例                          |
| ---------------------- | ------------- | ---------------------------------- |
| message                | object        | `{"fooBar": v, "g": null, …}`      |
| enum                   | string        | `"FOO_BAR"`                        |
| `map<K,V>`               | object        | `{"k": v, …}`                      |
| repeated V             | array         | `[v, …]`                           |
| bool                   | boolean       | `true, false`                      |
| string                 | string        | `"Hello World!"`                   |
| bytes                  | base64 string | `"YWJjMTIzIT8kKiYoKSctPUB+"`       |
| int32, fixed32, uint32 | number        | `1, -10, 0`                        |
| int64, fixed64, uint64 | string        | `"1", "-10"`                       |
| float, double          | number        | `1.1, -10.0, 0, "NaN", "Infinity"` |



### gRPC 与 Triple

Triple 是一种兼容 gRPC 的 API 技术，它们都使用 gRPC 通信协议和 ProtoBuf 序列化格式。

如果你的 Triple 接口通过 `.proto` 文件进行定义，而不是 Java Interface 或其他方式定义，那么同样可以在 Apifox 的 gRPC 项目中加载 `.proto` 文件来调试 Triple 接口。

此时，URL 中的协议名 `tri://` 和 `grpc://` 是等价的。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/469953/image-preview)
</Background>


## 保存调试信息

完成调试后可以点击“保存”按钮将服务器 URL、消息、Metadata 等调试信息保存在当前方法中，以便团队内的其他成员进行调试。


