# API 响应

Apifox 的响应控制台提供强大的功能来可视化和验证 API 响应，帮助你检查详细的响应信息，包括测试结果、网络信息、响应大小、响应时间和安全警报。

## 响应 Body

在 Apifox 响应控制台的 Body 标签中，你可以选择多种视图来解读响应内容。

### Pretty

此视图将 JSON 或 XML 响应格式化，提升可读性。它高亮显示链接，并允许折叠大段内容以便于快速导航。

<Background>
    <p style="text-align: center">
    <img src="https://api.apifox.com/api/v1/projects/5097254/resources/472901/image-preview" style="width: 640px" />
</p>
</Background>



:::tip 强制 JSON 格式化
要在 Apifox 中启用响应 Body 的自动格式化，响应应包含正确的 `Content-Type` 头部。如果收到的响应具有不同的 `Content-Type` 头部，你可以手动强制进行 JSON 格式化。
:::

### Raw

Raw 视图以纯文本形式显示未格式化的响应主体，适合查看原始或压缩格式的响应内容。

### Preview

Preview 视图在沙盒 iframe 中渲染 HTML 响应，帮助调试和查看渲染效果。

<Background>

    <p style="text-align: center">
    <img src="https://api.apifox.com/api/v1/projects/5097254/resources/472903/image-preview" style="width: 640px" />
</p>
</Background>


对于二进制响应，你可以点击 “发送” 按钮旁的下箭头，选择 “发送并下载” 将响应保存到本地。


### Visualize

此视图通过你在接口的 “后置操作” 中添加的 “自定义脚本” 来可视化渲染响应数据。

:::highlight purple
了解更多关于[响应数据可视化](https://docs.apifox.com/response-data-visualization.md)的信息。
:::

## Cookie

Cookie 标签显示服务器发送的所有 Cookies，包括名称、值、域、路径和其它相关信息。

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/472906/image-preview)
</Background>


:::highlight purple
了解更多关于在 Apifox 中[创建和发送 Cookie](https://docs.apifox.com/create-and-send-cookie.md) 的信息。
:::


## Header

Headers 标签以键值对的形式显示响应头信息。

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/472907/image-preview)
</Background>


## 网络信息

Apifox 会显示相关的网络细节。将鼠标悬停在这些信息上，可以查看简要的描述。

此外，会计算并显示响应的时间和大小，你可以将鼠标光标悬停在这些字段上查看更详细的数值。


<Background>
    <p style="text-align: center">
    <img src="https://api.apifox.com/api/v1/projects/5097254/resources/472909/image-preview" style="width: 640px" />
</p>
</Background>



