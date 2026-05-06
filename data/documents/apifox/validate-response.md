# 校验响应

在 Apifox 中，发送接口请求后，系统会依据接口定义自动校验响应的结构是否符合预期。


<Background>
<p style="text-align: center">
    <img src="https://api.apifox.com/api/v1/projects/5097254/resources/478841/image-preview" style="width: 340px" />
</p>


</Background>


## 校验规则

### 校验范围

- 接口返回的 HTTP 状态码
- 返回内容的数据格式：`JSON`、`XML`、`HTML`、`Raw`、`Binary`、`No-Content`、`MsgPack`、`Event-Stream`
- 数据结构：只有 `JSON` 和 `XML` 能配置数据结构。。

| 校验项                          | 属性类型                | 示例                                   |
|-------------------------------|---------------------|------------------------------------------|
| 必需属性                    | All                   | $ 应该有必需属性 code               |
| 值类型                  | All                   | $.data.id 应当是 string 类型                        |
| 非空键为空值               | All                   | $.data.id 应当是 string 类型                         |
| 枚举值                 | String, Integer, Number          | $.data.status 应等于预定义值之一（可用值：available，pending，sold）  |
| 数值范围                   | Integer, Number                | $.data.age 应大于等于 0                    |
| 数值满足多重要求               | Integer, Number               | $.data.quantity 应为 10 的倍数              |
| 字符串长度范围             | String                | $.data.name 应不少于 3 个字符               |
| 字符串与接口定义                 | String                | $.data.name 应符合模式 "^[A-Za-z]"        |
| 数组元素数量         | Array                   | $.data.tags 不应超过 2 项                   |


### 校验示例

如果接口返回的响应与定义的数据接口一致，则以上的 “校验项” 不会被触发。

<Background>
<p style="text-align: center">
    <img src="https://api.apifox.com/api/v1/projects/5097254/resources/478854/image-preview" style="width: 340px" />
</p>
</Background>


当你在右侧看到相应的提示时，可以根据提示解决问题。

一般来说，问题主要有两类：第一类是服务器的响应不正确，这种情况下，后端需要修改以符合接口定义；第二类是接口文档中的数据结构定义不正确，需要做相应的修改。

通过使用自动校验功能，你可以省去手动编写脚本来验证响应的时间。此外，当接口定义发生变化时，验证也会自动调整。

### 校验其他响应

默认情况下，Apifox 会校验接口中的第一个响应，通常是 200 响应。然而，一个接口可能返回多个不同的响应，且每个响应的模式也不同。在这种情况下，可以选择在校验区域右上角选择要校验的响应。


<Background>
<p style="text-align: center">
    <img src="https://api.apifox.com/api/v1/projects/5097254/resources/478859/image-preview" style="width: 340px" />
</p>
</Background>


你还可以通过点击响应前面的开关，关闭 “校验响应” 功能。此更改仅适用于当前接口。

## 校验额外字段

随着实际业务的升级，响应可能会增加附加属性。在这种情况下，Apifox 允许用户决定是否允许额外字段的存在。

例如，有一个查询用户信息的 API，之前返回的字段是 `name` 和 `phone`，因此数据结构指定如下：


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/478860/image-preview)
</Background>


随着业务的提升，新增了一个 `city` 字段，但接口文档没有更新。根据默认的校验机制，发送请求后控制台不会报错，意味着默认允许添加额外字段。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/478863/image-preview)
</Background>



然而，对于更严格的开发场景，如果返回值包含不符合定义的附加字段，响应校验也应报告错误。在此情况下，可以按以下步骤实现期望的行为：

1. 修改 API 定义 *（<Tooltip tip="也称 OpenAPI/Swagger 规范，在 Apifox 中表示接口文档。">API specification</Tooltip>）* 中的响应。在 `object` 的高级设置中，将 “额外字段” 配置为 “禁止”，这个设置这只会对当前接口生效。


    <Background>
       ![CleanShot 2024-11-22 at 14.30.05@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/478865/image-preview) 
    </Background>



2. 如果想要对项目中的所有接口禁止附加字段，可以前往 **“项目设置** → **功能设置** → **响应验证设置”**，并关闭 **“Object 对象允许额外字段”**。


    <Background>

    ![CleanShot 2024-11-22 at 14.30.05@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/478868/image-preview)
    </Background>


3. 完成配置后，再次发送请求时，响应校验机制将报告错误，表明不允许有额外的属性。


    <Background>

    ![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/478870/image-preview)
    </Background>


## 响应校验设置

“校验响应” 开关默认是开启的，你可以在项目设置界面的 “响应校验设置” 中进行调整。此设置只对当前项目中的所有 API 生效，不影响已保存的 `接口用例`。


<Background>

![CleanShot 2024-11-22 at 14.33.42@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/478873/image-preview)
</Background>


如果你只需要校验断言或脚本内容，而不需要 Apifox 来校验响应与接口定义的一致性，可以对特定模块禁用校验功能。



返回响应包含 “HTTP 状态码”、“Header”、“Body” 等内容，你可以在项目设置中的 “校验内容” 中进行调整。此设置只对当前项目中的所有 API 生效，不影响已保存的 `接口用例`。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/478882/image-preview)
</Background>

