# 接口调试用例

不同于 Postman，Apifox 分为 “接口” 和 “接口调试用例”，一个接口有多个调试用例。当接口里的 URL 或者参数更改后，会自动同步修改所有的调试用例。而 Postman 全是 Request，每个 Request 相互独立，接口的 URL 参数名等变化后需要手动修改所有 Request。

<Background>
![Postman → Apifox（中文）.png](https://api.apifox.com/api/v1/projects/5097254/resources/555436/image-preview)
</Background>



## 创建一个接口调试用例

当你在接口的 “运行” 标签页中发送请求或调试时，如果想要长久保存该请求，可以点击 `保存为用例`。


<Frame>
![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/477665/image-preview)

</Frame>


你可以为调试用例命名，然后用例类型设置为调试用例，并且选择是否同时保存响应。

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/555438/image-preview)
</Background>





## 接口调试用例中保存了什么

如前所述，接口定义 *（<Tooltip tip="也称 OpenAPI/Swagger 规范，在 Apifox 中表示接口文档。">API specification</Tooltip>）*  是保存在接口中的，而具体的值则存储在接口调试用例中。具体来说，调试用例包括以下数据：

- **请求参数值**：涵盖 Path 参数、Query 参数、Header 参数以及 `form-data` 格式的请求体参（Body）。
- **请求体内容**：格式可以是 RAW、JSON、XML 等。
- **接口的前后置操作**
- **接收到的响应数据**
- **响应校验设置**：指示校验是否启用，以及指定校验的响应组件。

因此，如果你修改了接口中某个参数的内容，相关的调试用例将会实时更新。例如，如果将某个 `integer` 类型的参数更改为 `string`，则对应的调试用例中的参数类型也会随之调整。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/477668/image-preview)
</Background>


## 使用接口调试用例的最佳实践

1. 确定 API 定义 *（<Tooltip tip="也称 OpenAPI/Swagger 规范，在 Apifox 中表示接口文档。">API specification</Tooltip>）*  的数据结构。
2. 为每个接口创建多个调试用例，以覆盖不同条件。
3. 为每个调试用例编写断言或其他发送请求前后的处理脚本。
4. 在接口测试用例中，可以复制接口调试用例，或者直接将调试用例转化成测试用例，以满足单接口测试的需求。
5. 在自动化测试中引用接口调试用例，以组建测试场景。
6. 如果 API 定义有更新，接口调试用例、测试用例和测试场景都可以进行同步。针对于调试用例，是全部自动同步的；针对于测试用例，你可以选择手动更新；针对于测试场景中的相关步骤，你可以设置为自动同步或手动同步。
