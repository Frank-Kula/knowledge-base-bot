# 请求 URL 与方法

Apifox 客户端支持通过 HTTP、GraphQL、SOAP、gRPC 等主流协议发送 API 请求。你可以创建请求、发送并查看响应结果，还可以将请求保存，方便团队协作。

## 请求 URL

发起请求时，需要填写目标 API 的 URL。通常，每个 API 操作对应一个唯一的接口地址。

URL 一般由基础地址和接口路径组成。例如：

```js
http://127.0.0.1:3000/users/12
```

其中：

- `http://127.0.0.1:3000` 是基础地址，建议配置在环境的 “前置 URL” 中；

- `/users/12` 是接口路径，以 `/` 开头，填写在接口地址栏中。


Query 参数可以直接写在 URL 中，也可以在 Params 标签下填写。

如果请求使用了 Path 参数，则需要将其嵌入到 URL 路径中 *（使用`{}`格式，如 <CopyToClipboard>`/users/{id}`</CopyToClipboard>*）。



<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/541618/image-preview)
</Background>



## 请求方法

在 Apifox 中，你可以在请求 URL 左侧选择请求方法，默认是 GET。常用的请求方法包括：

* **GET**：用于获取资源数据，不应对资源状态产生影响。
* **POST**：用于向服务器提交数据，常用于创建新资源。
* **PUT**：用于整体更新资源，将其替换为请求中提供的数据。
* **PATCH**：用于部分更新资源，仅修改部分字段。
* **DELETE**：用于删除指定资源。

在 API 设计中，相同的 URL 配合不同的方法，表示对同一资源的不同操作。例如：

* `GET /user/{id}` 表示获取用户信息
* `PUT /user/{id}` 表示更新该用户信息

