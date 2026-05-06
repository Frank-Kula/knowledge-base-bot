# GraphQL 调试

GraphQL 是一种用于 API 的查询语言，以及使用类型系统执行查询的服务器端运行时 *（类型系统由你的数据定义）*。GraphQL 并不依赖于特定的数据库或存储引擎，而是与现有的代码和数据一起工作。

## 新建 GraphQL 请求

在项目中新建一个接口，依次点击 “Body -> GraphQL” 即可创建一个 GraphQL 请求。


<Background>
![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/468394/image-preview)
</Background>



## 调试 GraphQL

在运行页面中的 Query 框内输入查询语句。你也可以点击输入框的的手动 `获取 Schema` 按钮以启用 Query 表达式的 “代码补全” 功能，用以辅助输入 Query 查询语句。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/468396/image-preview)
</Background>


查询语句支持使用 GraphQL 变量进行调试，具体用法请参考 [GraphQL 语法](https://graphql.cn/learn/queries/#variables)。


<Background>
  
![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/468398/image-preview)
</Background>


## 常见问题

**出现类似`SyntaxError: Unexpected token } in JSON at position 214`这样的报错如何解决？**

通常是因为 JSON 格式不正确，可能是多了或少了一个括号、逗号，或者字符串没有正确关闭等问题。可以使用一些在线的 JSON 校验工具，检查是否有格式错误。

