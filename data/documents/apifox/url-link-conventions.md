# 在线 URL 链接规范

Apifox 支持在共享文档的 URL 中直接包含特定的参数和变量值。默认情况下，共享文档仅包含 API 规范。此功能允许您共享特定的值。

## 参数类型

通过 URL 传递的参数值，其行为取决于参数类型：

1.  **环境变量**：通过 URL 设置的值将应用于文档中的所有接口。在不同接口间切换或打开新标签页时，这些值都会生效，直到被显式覆盖或用户修改。

2.  **请求参数**（Query、Path、Body、Header、Cookie）：这些值仅作用于通过 URL 访问的特定接口。切换到其他接口时，这些值不会保留。

## 参数模式

有两种模式可以嵌入参数值：简单模式和复杂模式。

- 简单模式更简洁，不需要 URL 编码，但无法处理方括号等特殊字符。
- 复杂模式支持所有字符，但需要对参数数据进行 URL 编码。

### 简单模式

简单模式使用 `参数类型[参数名]=值` 的格式。

示例：

- `https://apifox.com/apidoc/docs-site/4478210/api-173409873-run?environment[access_token]=example_value&query[locale]=en-US`

| 参数类型        | 参数值格式       | 描述                                                | 作用范围                 |
| :-------------------- | :--------------------- | :---------------------------------------------------------- | :----------------------- |
| Query 参数      | `query[xxx]=yyy`       |                                                             | 仅当前接口    |
| Path 参数       | `path[xxx]=yyy`        |                                                             | 仅当前接口    |
| Body 参数       | `body[xxx]=yyy`        | 适用于 `form-data` 或 `x-www-form-urlencoded` 类型的请求体 | 仅当前接口    |
| Body 参数       | `body=yyy`             | 适用于其他类型的请求体（例如，原始 JSON、XML）                   | 仅当前接口    |
| Header 参数     | `header[xxx]=yyy`      |                                                             | 仅当前接口    |
| Cookie 参数     | `cookie[xxx]=yyy`      |                                                             | 仅当前接口    |
| 环境变量 | `environment[xxx]=yyy` | 设置默认环境中的值。                  | 跨接口持久有效 |

### 复杂模式

复杂模式将一个 URL 编码的 JSON 对象作为 `params` 参数的值传递。此 JSON 对象必须使用 `encodeURIComponent` 进行编码。在 JavaScript 中，可以使用以下代码实现：`encodeURIComponent(JSON.stringify({"query":["id",1]}))`。

示例 JSON（编码前）：

```json
{
    "query": [
        ["id", "value1"],
        ["id", "value2"],
        ["key2", "value3"]
    ],
    "path": [
        ["key1", "value1"],
        ["key2", "value2"]
    ],
    "body": [
        ["aaa", "value1"],
        ["key2", "value2"]
    ],
    "header": [
        ["testHeader", "value1"],
        ["key2", "value2"]
    ],
    "cookie": [
        ["testCookie", "value1"],
        ["key2", "value2"]
    ],
    "environment": [
        ["access_token", "example_value"],
        ["projectId", "1"]
    ]
}
```

示例 URL（编码后）：

```
https://apifox.com/apidoc/docs-site/4478210/api-173409873-run?params=%7B%22query%22%3A%5B%5B%22id%22%2C%22value1%22%5D%2C%5B%22id%22%2C%22value2%22%5D%2C%5B%22key2%22%2C%22value3%22%5D%5D%2C%22path%22%3A%5B%5B%22key1%22%2C%22value1%22%5D%2C%5B%22key2%22%2C%22value2%22%5D%5D%2C%22body%22%3A%5B%5B%22aaa%22%2C%22value1%22%5D%2C%5B%22key2%22%2C%22value2%22%5D%5D%2C%22header%22%3A%5B%5B%22testHeader%22%2C%22value1%22%5D%2C%5B%22key2%22%2C%22value2%22%5D%5D%2C%22cookie%22%3A%5B%5B%22testCookie%22%2C%22value1%22%5D%2C%5B%22key2%22%2C%22value2%22%5D%5D%2C%22environment%22%3A%5B%5B%22access_token%22%2C%22example_value%22%5D%2C%5B%22projectId%22%2C%221%22%5D%5D%7D
```
| 参数类型       | 参数值 | 描述                                                                                            | 作用范围                 |
|:---------------------|:----------------|:-------------------------------------------------------------------------------------------------------|:-------------------------|
| Query 参数     | `query`         | 键值对数组。                                                                         | 仅当前接口    |
| Path 参数      | `path`          | 键值对数组。                                                                         | 仅当前接口    |
| Body 参数      | `body`          | `form-data` 或 `x-www-form-urlencoded` 类型为键值对数组；其他请求体类型为字符串。 | 仅当前接口    |
| Header 参数    | `header`        | 键值对数组。                                                                         | 仅当前接口    |
| Cookie 参数    | `cookie`        | 键值对数组。                                                                         | 仅当前接口    |
| 环境变量| `environment`   | 键值对数组。设置默认环境中的值。                                  | 跨接口持久有效 |

## 环境变量

要想用户访问 URL 的时候能自动设置好特定环境变量的值，可以将这些值包含在 URL 中。这些变量值在文档中的所有接口都是有效的。

示例：

-   `https://apifox-openapi.apifox.cn/api-173409873-run?environment[access_token]=example_value`

<br/>

<TipGood>环境变量跨接口持久有效，而其他参数类型（Query、Path、Body、Header、Cookie）仅作用于当前用户访问的接口 URL。环境变量是最适合在多个接口之间共享可重用的值。</TipGood>
