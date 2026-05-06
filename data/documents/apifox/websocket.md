# WebSocket 调试

WebSocket 是一种在 TCP 连接上进行全双工通信的 API 技术。相比于传统的 HTTP 类型 API，WebSocket 类型接口有着更低的延迟和更高的效率，它适用于需要长时间保持连接并实时传输数据的场景，例如在线游戏、实时聊天等服务。


## 新建接口

1. 点击项目左侧的“+”按钮，选择“新建 WebSocket 接口”。
    
    <Background>

    ![CleanShot 2025-11-05 at 16.47.49@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/588582/image-preview)
    </Background>

3. 输入 WebSocket 服务器的 URL，格式需以 `ws` 或 `wss` 开头。
4. 点击“连接”。
5. 若要断开 WebSocket API，请点击“断开连接”。

:::tip[]
建议使用 Apifox 客户端以体验 WebSocket 接口的完整功能。
:::

## 发送消息

建立 WebSocket 连接后，你可以在 `Message` 标签下撰写消息。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/469969/image-preview)
</Background>


除了直接撰写 `Text`、 `JSON`、`XML`、`HTML` 等文本格式的消息之外，还可以通过 `Base64` 或 `Hexadecimal` 来撰写二进制格式的消息。

编辑器会根据所选的消息格式，对消息内容进行语法高亮。如果消息是 `JSON`、`XML` 或 `HTML` 格式，还可以对输入的内容进行格式化操作。

## 查看消息

下方的 `Messages` 按照时间顺序集中展示连接状态、发送的消息、收到的消息。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/469970/image-preview)
</Background>


点击单条消息，则可以在右侧查看消息详情：

- 如果消息是文本格式，默认会显示格式化后的消息，也可以手动切换消息格式和编码。

   
    <Background>

    ![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/469971/image-preview)
    </Background>


- 如果消息是二进制格式，默认会显示消息的 `Hexdump`，也可以查看经过 `Base64` 编码后的消息和原始消息。

   
    <Background>

    ![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/469972/image-preview)
    </Background>


## 添加握手请求参数

你也可以自定义 WebSocket 握手时所需要传递的参数，比如 `Params`、`Headers`、`Cookies`，以满足鉴权或其他复杂场景。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/469973/image-preview)
</Background>


:::tip[]
建立连接后无法修改握手请求的参数，必须在建立连接之前或者断开连接之后进行配置。

:::

## 使用变量

你可以在 WebSocket 连接的握手和消息中使用 Apifox 变量。

有关如何使用变量的更多信息，请参阅[使用变量](https://docs.apifox.com/global-environment-session-variables.md)。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/469974/image-preview)
</Background>


## 保存接口

在完成调试后，你可以点击 `保存` 按钮将 WebSocket 接口保存到 `HTTP` 项目的目录树中，以便团队内的其他成员进行调试或查看接口文档。



## 生成接口文档

你可以对 Websocket 接口设定 `状态`、`责任人`、`标签`，还可以用 `Markdown` 格式撰写详细的接口说明。Apifox 支持生成在线接口文档，你可以将文档 URL 分享给团队内部的其他成员。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/469975/image-preview)
</Background>


## 常见问题


<Accordion title="为什么不需要设置校验响应？" defaultOpen>
WebSocket 请求在建立连接时，正常情况下 HTTP 状态码一定是 `101`，表示协议已升级。因此，校验状态码意义不大。
</Accordion>


<Accordion title="如何设置接口鉴权？" defaultOpen={false} >

目前推荐两种方式进行 WebSocket 接口鉴权：
  1. 在建立连接时，用`Param`、`Header` 或 `Cookie`中的某个字段传递鉴权信息；
  2. 在发送消息时，用消息的某个字段传递鉴权信息。
</Accordion>


<Accordion title="是否支持前置/后置脚本、断言？" defaultOpen={false} >
暂不支持，已在设计开发中。
</Accordion>


<Accordion title="支持请求示例和响应示例吗？" defaultOpen={false} >
暂不支持，后续会评估迭代。
</Accordion>

<Accordion title="WS 接口不支持 Mock 吗？" defaultOpen={false} >
当前 Mock 库不支持 WebSocket 的 API 定义，因此无法根据定义生成消息体。
</Accordion>

