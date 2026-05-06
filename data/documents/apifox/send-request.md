# 发送请求

点击 `发送` 按钮即可在 `运行` 标签页中发送请求。

文档模式中的 `运行` 界面与调试模式中的 `请求` 界面非常相似。主要的区别在于，文档模式 的`运行` 是基于接口的，可以根据接口定义生成请求并验证响应，当接口定义发生变化时，`运行` 界面也会相应更新。另一方面，调试模式的 `请求` 是独立的，与接口定义无关。

## 发送请求

当你发送请求时，Apifox 会以可视化的方式显示从服务器返回的响应。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/477637/image-preview)
</Background>


这个界面分为两部分：上半部分是输入你想发送的请求，下半部分则显示你实际发送的请求、收到的响应，以及对响应的校验和断言结果。

:::tip[]
你可以悬停在右下角的 `分隔` 按钮上来调整运行界面的布局，可以选择将界面上下、左右分屏，或者不分屏。
<p style="text-align: center">
    <img src="https://api.apifox.com/api/v1/projects/5097254/resources/477638/image-preview" style="width: 340px" />
</p>
:::

### 实际请求

在上半部分，你可以利用变量、动态值、脚本等来调整你发送的请求。如何查看实际发送的请求？你可以在下半部分的 `实际请求` 标签中看到完整的实际请求。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/477639/image-preview)
</Background>


### 校验响应

Apifox 会自动校验响应是否符合基于接口定义的数据结构。你可以选择启用或者禁用校验，并选择要校验的响应。

:::highlight purple
了解更多关于[校验响应](https://docs.apifox.com/validate-response.md)的信息。
:::

### 提取响应

Apifox 支持将响应提取到接口定义中，可以提取为 `响应定义` 或者 `响应示例`。

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/477640/image-preview)
</Background>

## 修改请求

你可以在 `运行` 标签页中修改请求。可以更改参数值或切换参数前面的复选框，以改变请求。这些操作不与接口定义冲突。

有时你可能需要修改参数类型或添加/移除参数。在这种情况下，请求就会偏离接口定义。在 Apifox 中，这些不一致的地方会以橙色高亮显示。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/477643/image-preview)
</Background>


悬停在这些橙色标记上，会显示接口文档与当前请求之间的差异。你可以点击 `复原` 将其恢复到一致的状态，或点击 `保存到文档` 以更新接口文档。你还可以点击右上角的 `不一致` 按钮，批量恢复或保存所有差异到接口文档中。

## 保存请求

在文档模式下的 `运行` 标签页中，没有 “保存” 按钮。这是因为接口定义中的请求数据不受 “运行” 页中请求数据的影响。

为了方便调试，Apifox 提供了一个 `暂存` 按钮。点击暂存会保存当前运行界面中的内容，不会影响接口定义，并且这些内容不会与其他人同步。


<Frame>
<p style="text-align: center">
    <img src="https://api.apifox.com/api/v1/projects/5097254/resources/477659/image-preview" />
</p>
</Frame>




如果你想长久保存某个请求，可以点击 `保存为用例`。这个请求将以接口用例的形式保存到接口的层级中。


<Background>
    <p style="text-align: center">
    <img src="https://api.apifox.com/api/v1/projects/5097254/resources/477660/image-preview" style="width: 240px" />
</p>
</Background>



你可以将这个接口的每种使用场景保存为接口用例，便于开发者调试，并在自动化测试中作为一个 “测试步骤” 轻松导入。

:::highlight purple
了解更多关于[接口用例](https://docs.apifox.com/api-test-cases.md)的信息。
:::

:::tip[]
当导入 Postman 集合时，每个 Postman 请求会对应 Apifox 中的一个接口用例。因此，它们将显示为接口层级下的 `成功` 用例，而不是接口定义内的内容。

了解更多关于[从 Postman 迁移](https://apifox.com/blog/migrate-from-postman-to-apifox/)的信息。
:::

## 常见问题

<Accordion title="为什么相同的请求在其他工具（例如 Postman）中可以正常工作，而在 Apifox 中却不行？" defaultOpen>
如果请求是相同的，那么响应应该也会是相同的，与使用的工具无关。如果你得到的响应不同，可以切换到 `实际请求` 标签，将你在其他工具中发送的请求进行对比，找出差异。
</Accordion>

