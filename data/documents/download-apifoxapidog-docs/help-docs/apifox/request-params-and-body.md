# 请求参数与请求体

在请求 API 时，了解如何发送不同类型的数据至关重要。Apifox 提供了一个用户友好的界面，帮助你构建并发送带有不同请求参数和请求体类型的 API 请求。

## 请求参数

参数可以让你可以向服务器发送额外的信息。Apifox 支持两种主要的参数类型：查询参数 *（Query params）* 和路径参数 *（Path params）* 。

### Query 参数

Query 参数附加在 URL 末尾的问号 *（?）* 之后，并用与号 *（&）* 分隔。它们用于向服务器发送可选或附加的数据。在 Apifox 中，你可以轻松地为你的 API 请求添加和管理 Query 参数。

有两种方便的方法来为你的接口添加 Query 参数：

1. **直接在 URL 中：** 你可以在地址栏中的 URL 末尾直接附加 Query 参数。例如：<CopyToClipboard>`https://api.example.com/users?page=1&limit=10`</CopyToClipboard>

2. **使用 Query 参数输入框：** Apifox 提供了一个位于 URL 输入框下方的专用 Query 参数输入框。在这里，你可以使用一个用户友好的界面来添加、编辑和删除 Query 参数。你在这一部分添加的参数将自动附加到请求 URL 中。


**Query 参数中的等号**

在某些特殊情况下，Query 参数可能不会以键值对的形式出现。例如，请求 URL 可能是这样的：

```
https://api.example.com/users?available
```

在这种情况下，`available` 可以作为一个没有值的参数。当值为空时，Apifox 会自动省略键和值之间的等号。

如果不想省略这个等号，你可以手动选择 “添加等号”。

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/470030/image-preview)
</Background>

将 JSON 粘贴到请求的参数名字段时，其内容将被自动转换为参数名和参数值。
![自动解析JSON](https://cdn.apifox.cn/uploads/help/202505211656044.gif)



### Path 参数

Path 参数是 URL 路径的一部分，用来标识特定的资源。在 Apifox 里需要用**单大括号 `{}`** 包裹。示例：

```
https://api.example.com/pet/{petId}
```

只要你在 URL 栏输入`{参数名}`，Apifox 就会自动识别，并在下方自动显示对应的参数输入框。
<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/595357/image-preview)
</Background>

如果你需要在 URL 路径里使用变量，建议的写法是：**URL 保持标准的 `{}` 占位符格式，变量只写在 Path 参数的 “参数值” 中**。


<TipGood>推荐的写法：在 Path 参数的参数值里引用变量</TipGood>


<Steps>
  <Step>
        在 URL 栏保留占位符格式，例如 `/pet/{petId}`
  </Step>
  <Step>
    在 Path 参数列表中找到 `petId`，在 “参数值” 里使用**双大括号 `{{}}`** 填入变量名，例如 `{{petId}}`。这样就相当于在 URL 路径里使用变量了。
  </Step>
</Steps>

<Frame>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/579049/image-preview)
</Frame>


<TipBad>
    不推荐的写法：把变量直接写在 URL 栏里
    
</TipBad>

直接在路径中使用变量`{{}}`会影响 Apifox 的 Mock API 功能的使用。另外，这种写法不符合 OAS 规范，无法在 OpenAPI 生态的工具中正常集成。因此，**不推荐**在 URL 上直接写变量，例如 ~~`/pet/{{petId}}`~~。

<Frame>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/579050/image-preview)
</Frame>

:::tip[关键概念区分：`{parameter}` vs `{{variable}}`]

- **`{parameter}` (Path 参数)**
这是 URL 路径的一部分，作为资源的占位符（如 `/pet/{petId}`）。它告诉系统 “这里有一个参数”，需要单独定义类型和说明。

- **`{{variable}}` (变量引用)**
这是动态赋值的手段。它用于读取环境变量的具体值，应该填在 Path 参数的 “参数值” 输入框中，而不是直接写在 URL 栏里。 
:::


### 参数编码与解码

选择参数文本后右键点击，可以对参数进行 `EncodeURIComponent` 编码或 `DecodeURIComponent` 解码，也可以将其存入变量。

<Background>
![](https://cdn.apifox.cn/uploads/help/202411291746511.gif)
</Background>


:::tip[]
了解更多 [URL 参数编码](https://docs.apifox.com/request-param-encoding-decoding.md)信息。
:::


## 请求体

请求体（Body）用于在 POST、PUT 或 PATCH 请求中传递数据到服务器。Apifox 支持多种请求体数据格式。

### form-data

`form-data` 是一种发送键值对的方式，类似于提交 HTML 表单。这种格式特别适用于需要上传文件的同时发送其他数据的情况。

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/470035/image-preview)
</Background>

form-data 类型的请求 Body 将在请求中显示为 `multipart/form-data`。对于请求 Body 中的每个参数，你可以选择其类型，如字符串、整数等。

如果需要在 form-data 中发送 JSON，你需要将参数类型设置为 `string`，然后在字段的参数值中填入 JSON。

如果需要在请求中发送文件，请选择类型为文件，然后点击 “Upload” 并选择本地文件。

:::tip[]
Apifox 仅在请求中发送文件，但不会将文件保存在云端。因此，在团队协作期间，其他人可以看到这个请求但不能直接发送这个文件。你需要通过其他方式将文件传输给同事，以便他们能够发送。
:::


### x-www-form-urlencoded

这种格式类似于 Query 参数，但发送在请求 Body 中。它常用于提交不需要上传文件的简单表单。在 Apifox 中，你可以轻松地使用键值对添加和编辑 `x-www-form-urlencoded` 数据。

### JSON

JSON 是接口请求和响应中广泛使用的数据格式，你可以在接口的 “请求参数 - Body - JSON” 中设计数据结构。
<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/583026/image-preview)
</Background>

在设计 JSON 数据结构时，可以[「通过 JSON 等生成」](https://docs.apifox.com/generate-from-json)这个功能来快速生成，不用一个一个手动添加。

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/583032/image-preview)
</Background>

手动在数据结构中添加字段时，默认是`string`类型，如果需要添加子节点，需要将字段设置成 `object` 或 `array` 类型。



<Background>
![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/583033/image-preview)
</Background>




:::tip[]
在接口 “调试” 页，如果你想在 JSON 中添加注释，可以在“设置 -> 常规设置 -> 功能设置 -> 高级设置”中启用“兼容带注释的 JSON”。发送 JSON 时，这些注释将自动移除。

<Background>

![CleanShot 2024-10-12 at 16.01.15@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/470038/image-preview)
</Background>

:::

### XML

XML（可扩展标记语言）是另一种在 API 通信中常用的格式。Apifox 支持 XML 载荷，允许你以 XML 格式发送结构化的数据。

### raw

`raw` 选项允许在请求体 *（Body）* 中发送任何自定义数据格式。这对于处理一些期望特定数据结构或格式的 API 非常有用，尤其是当这些结构或格式不属于其他选项覆盖的范围时。

### binary

此选项允许发送二进制数据，对上传文件或与需要二进制数据的 API 交互特别有用。Apifox 支持选择并发送二进制文件作为 API 请求的一部分。

### GraphQL

对于基于 [GraphQL](https://docs.apifox.com/graphql.md) 的 API，Apifox 提供了一个专用的 GraphQL 编辑器。这个功能允许你构建并发送 GraphQL 查询 *（Query）* 和变量 *（Variables）* ，并支持语法高亮和自动补全。


### Msgpack

MessagePack 是一种比 JSON 更紧凑且更快速的二进制序列化格式。Apifox 支持发送 MessagePack 数据，这对于需要优化性能和减少数据传输的 API 非常有利。

