# 文档模式/调试模式

Apifox 的 API 调试有两种模式，可以在界面左下角切换：`文档模式` 和 `调试模式`。


<Background>
<p style="text-align: center">
    <img src="https://api.apifox.com/api/v1/projects/5097254/resources/478886/image-preview" style="width: 640px" />
</p>
</Background>



这两种模式提供了类似的功能，但界面不同，以适应不同团队的工作流程。

**文档模式**是 Apifox 推荐的模式，适合采用 API 设计优先的团队。在这个模式中，团队首先定义 API，随后根据 API 文档进行开发和测试。

<Background>
<p style="text-align: center">
    <img src="https://api.apifox.com/api/v1/projects/5097254/resources/505429/image-preview" style="width: 540px" />
</p>
</Background>


而**调试模式**则特别适合那些没有事先定义 API 文档的团队。这样的团队通常集中在后端开发，先完成代码，然后再生成 API 文档，进行测试和客户端工作。

<Background>
<p style="text-align: center">
    <img src="https://api.apifox.com/api/v1/projects/5097254/resources/505431/image-preview" style="width: 540px" />
</p>
</Background>

如果需要调用其他人开发的 API 而没有文档，建议也使用调试模式。

## 文档模式

在**文档模式**下，编辑 API 文档和发送请求是通过不同的标签页来进行的。用户在**修改接口**标签页中修改 API 文档，而在**运行**标签页中发送请求。


<Background>

![CleanShot 2024-11-22 at 14.48.41@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/478887/image-preview)
</Background>


这种分离方式适合遵循 API 设计优先的团队，其中 API 设计者和开发/使用者有明确的角色分工。API 设计者在不发送请求的情况下定义 API 文档，而开发者专注于 API 的开发与测试，不会修改 API 文档。

分开的标签页符合这些团队的使用习惯。在编辑标签页中，API 设计者可以指定请求示例，这些示例会自动设置为 “运行” 标签页中的默认参数值。API 开发者/使用者可以在 “运行” 标签页中进一步修改参数值和请求体。

## 调试模式

**调试模式**适合那些没有事先定义 API 的团队。后端开发者直接进行 API 开发，开发过程中可能需要调用 API 进行调试。

在这个模式下，开发者无需事先指定 API，可以直接输入请求，就像在 Postman 中创建新请求一样。在这个界面下，开发者可以轻松修改参数类型、名称、值、请求体组件等，而无需单独调整 API 文档和请求参数值。


<Background>

![CleanShot 2024-11-22 at 14.51.17@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/478888/image-preview)
</Background>


一旦调试完成并保存，请求会自动**解析**为一个接口文档。参数会被转化为文档中的参数和示例值，而请求/响应体会解析为一个数据结构，其中的值会被解析为请求/响应示例。开发者可以根据需求进一步完善和增强这个接口文档。

## 模式之间的区别

这两种模式的主要区别在于，调试模式下，请求体用作接口请求体示例。相对的，在文档模式中，用户可以在 “运行” 标签页中输入实际的请求体以及请求体示例。因此，**运行**标签页中的请求体部分仅在文档模式中可用，而在调试模式中不可见。

另一个区别是，在文档模式中，可以在接口文档级别或运行/接口用例级别添加前置脚本或后置脚本。而在调试模式中，由于没有 “运行” 标签页，所有的前置脚本或后置脚本都被视为在接口文档级别。运行/接口用例级别的前置脚本或后置脚本在调试模式下是不可见的。
