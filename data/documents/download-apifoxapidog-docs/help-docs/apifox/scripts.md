# 使用脚本

Apifox 内置了基于 JavaScript 的脚本引擎，你可以通过脚本 *（JavaScript 代码）* 为接口请求或自动化测试添加动态操作。

脚本可以实现以下功能：

1. 校验接口返回结果是否正确 *（后置脚本）*
2. 动态修改接口请求参数，如添加签名参数等 *（前置脚本）*
3. 在不同接口之间传递数据 *（通过脚本操作变量）*
4. 调用其它编程语言编写的程序，支持 Java（.jar）、Python、PHP、JS、BeanShell、Go、Shell、Ruby、Lua 等语言

:::tip[]

Apifox 的脚本语法和 Postman 完全兼容，Postman 的脚本可以无缝迁移到 Apifox。

查看支持的所有 [pm 语法](https://docs.apifox.com/postman-script-api.md)。
:::


:::highlight purple

对不熟悉 JavaScript 的同学来说，写 pm 脚本可能会有点难度。

你可以使用 AI 来辅助生成，善用 AI 可以解决你的大部分问题。
:::

## 脚本使用方法

脚本可以在这两个阶段使用：

1. 发送接口请求到服务器之前，用前置脚本
2. 收到响应之后，用后置脚本


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/480387/image-preview)
</Background>


## 脚本调试

你可以在前置脚本和后置脚本中写调试代码，通过 `console.log("message") `在控制台输出信息。

```js
console.log("anything")
```

## 脚本示例

1. [断言示例](https://docs.apifox.com/assertion-examples.md)
2. [脚本中使用变量](https://docs.apifox.com/use-variables-in-scripts.md)
3. [脚本读取/修改接口请求信息](https://docs.apifox.com/access-modify-request-data.md)
4. [参数加密/解密](https://docs.apifox.com/js-libraries.md)


## 脚本 API

请查看 [pm 脚本 API](https://docs.apifox.com/postman-script-api.md) 模块文档。

## 常见问题

<Accordion title="Apifox 支持 pm.nextRequest() 吗？" defaultOpen>
Apifox 不支持 “运行集合” 功能，因此无法使用 `pm.nextRequest()`。不过，你可以在自动化测试模块中创建**测试场景**，并添加 **if** 条件，根据不同的条件发送不同的请求。
</Accordion>

