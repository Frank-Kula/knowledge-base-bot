# JSONPath 介绍

JSONPath 是一种用于从 JSON 数据结构中提取数据的查询语言，类似于 XPath 对 XML 的作用。Apifox 中使用的 JSONPath 基于 [JSONPath Plus](https://github.com/JSONPath-Plus/JSONPath)，你可以访问该链接查看详细的语法说明。

:::tip[]
如果不熟悉 JSONPath，可使用免费的 [AI 工具生成表达式](https://app.anakin.ai/apps/21854)。
:::



## 快速入门


<Steps>
  <Step title="原始 JSON 响应">
    假设我们有如下的 JSON 响应：
      
      ```json
      {
          "store": {
            "book": [
              { "category": "fiction", "author": "Author A", "title": "Book 1" },
              { "category": "reference", "author": "Author B", "title": "Book 2" },
              { "category": "fiction", "author": "Author C", "title": "Book 3" }
            ]
          }
      }

      ```
  </Step>
  <Step title="访问元素">
      
      如果你想快速提取 `book` 数组中第一本书的标题 *(`title`)*，可以使用以下 JSONPath：
      ```json
      $.store.book[0].title
      ```
      这将返回 `"Book 1"`。
      
<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/496395/image-preview)
    
</Background>
:::tip[]
你可以在 [JSONPath 测试工具](http://jsonpath.com/)中验证这些表达式 *(验证时需选择 JSONPath Plus)*。
:::

  </Step>
    
    <Step title="理解含义">
      这个 JSONPath 表达式 `$.store.book[0].title` 的含义是：

        - **`$`**：表示 JSON 文档的根节点。在这个例子中，它指向整个 JSON 数据结构。
        - **`store`**：访问根节点下的 `store` 属性，它是一个对象。
        - **`book`**：在 `store` 对象下访问 `book` 属性，它是一个数组。
        - **`[0]`**：访问 `book` 数组中的第一个元素（索引从 `0` 开始）。
        - **`title`**：访问数组中的第一个书籍对象的 `title` 属性。

        所以，整个表达式的意思是：从 JSON 文档的根节点开始，找到 `store` 对象，进入 `book` 数组，获取数组中的第一个元素，然后提取该元素的 `title` 属性值。

   
  </Step>
</Steps>


:::highlight purple 💡
- JSONPath 索引从 `0` 开始计数。  
- JSONPath 中字符串必须使用单引号，例如：`$.store.book[?(@.category=='reference')]`。
:::

## 语法详解

### 基本语法

| 语法              | 描述                                    |
| ----------------- | --------------------------------------- |
| `$`               | 根节点                                  |
| `@`               | 当前节点                                |
| `.node` 或 `['node']` | 访问下级节点                            |
| `[index]`         | 数组下标访问，支持从 `0` 开始计数        |
| `[start:end:step]`| 数组切片                                |
| `*`               | 通配符，匹配所有下级节点                |
| `..`              | 递归通配符，匹配所有子节点              |
| `(<expr>)`        | 动态表达式                              |
| `?(<boolean expr>)` | 过滤条件                              |


### 扩展语法

| 语法                         | 描述                                                       |
| ---------------------------- | ---------------------------------------------------------- |
| `^`                          | 获取匹配项的父级                                           |
| `~`                          | 获取匹配项的属性名（以数组形式）                           |
| `@null()`, `@boolean()`, `@number()`, `@string()`, `@array()`, `@object()` | 获取基本 JSON 类型                                          |
| `@integer()`                 | 获取整数类型                                               |
| `@scalar()`                  | 获取复合类型，接受 `undefined` 和非有限数字（查询 JavaScript 对象时） |
| `@other()`                   | 可与用户定义的 `otherTypeCallback` 一起使用                |
| `@undefined()`, `@function()`, `@nonFinite()` | 查询非 JSON JavaScript 对象时使用的非 JSON 类型            |
| `@path`, `@parent`, `@property`, `@parentProperty`, `@root` | 过滤器中的简写选择器                                      |
| `` ` ``                       | 转义剩余序列                                               |
| `@['...']`, `?@['...']`       | 在过滤器中转义属性名称中的特殊字符                        |
| `$..`                         | 获取所有父级组件                                           |


<!--
### JSONPath 与 XPath 对比

| XPath                  | JSONPath                                   | 描述                                       |
| ---------------------- | ------------------------------------------ | ------------------------------------------ |
| `/`                    | `$`                                       | 根节点                                     |
| `.`                    | `@`                                       | 当前节点                                   |
| `/`                    | `.` 或 `[]`                               | 访问下级节点                               |
| `..`                   | `..`                                      | 递归匹配所有子节点                         |
| `*`                    | `*`                                       | 通配符，匹配所有下级节点                   |
| `[index]`              | `[index]`                                 | 根据索引访问数组元素，JSONPath 从 0 开始计数 |
| `[start:end:step]`     | `[start:end:step]`                        | 支持切片操作，XPath 不支持                 |
| `[condition]`          | `?()`                                     | 过滤条件                                   |
| `()`                   | `N/A`                                     | XPath 支持分组，JSONPath 不支持            |


-->



## JSONPath 示例

以下是基于示例 JSON 数据的常用 JSONPath 表达式：

### 示例 JSON 数据
```json
{
  "store": {
    "book": [
      {
        "category": "reference",
        "author": "Nigel Rees",
        "title": "Sayings of the Century",
        "price": 8.95
      },
      {
        "category": "fiction",
        "author": "Evelyn Waugh",
        "title": "Sword of Honour",
        "price": 12.99
      },
      {
        "category": "fiction",
        "author": "Herman Melville",
        "title": "Moby Dick",
        "isbn": "0-553-21311-3",
        "price": 8.99
      },
      {
        "category": "fiction",
        "author": "J. R. R. Tolkien",
        "title": "The Lord of the Rings",
        "isbn": "0-395-19395-8",
        "price": 22.99
      }
    ],
    "bicycle": {
      "color": "red",
      "price": 19.95
    }
  }
}
```

### JSONPath 查询示例

| XPath                  | JSONPath                                   | 结果                                         |
| ---------------------- | ------------------------------------------ | -------------------------------------------- |
| `/store/book/author`   | `$.store.book[*].author`                   | 所有书籍的作者                               |
| `//author`             | `$..author`                                | 所有作者                                     |
| `/store/*`             | `$.store.*`                                | `store` 下的所有子节点                       |
| `/store//price`        | `$.store..price`                           | 所有价格字段                                 |
| `//book[3]`            | `$..book[2]`                               | 第三本书（索引从 0 开始）                    |
| `//book[last()]`       | `$..book[(@.length-1)]` 或 `$..book[-1:]` | 最后一本书                                   |
| `//book[position()<3]` | `$..book[:2]` 或 `$..book[0,1]`           | 前两本书                                     |
| `//book[isbn]`         | `$..book[?(@.isbn)]`                       | 含 `isbn` 的书                               |
| `//book[price<10]`     | `$..book[?(@.price<10)]`                   | 价格小于 10 的书                             |
| `//*`                  | `$..*`                                     | 递归匹配所有子节点                           |


:::tip[]
你可以在 [JSONPath 测试工具](http://jsonpath.com/)中验证这些表达式 *(验证时需选择 JSONPath Plus)*。

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/495752/image-preview)
</Background>

:::



## 参考资料

- [JSONPath Plus](https://github.com/JSONPath-Plus/JSONPath)
- [JSONPath - XPath for JSON](https://goessner.net/articles/JsonPath/)
- [Querying JSON with SelectToken](https://www.newtonsoft.com/json/help/html/SelectToken.htm)

