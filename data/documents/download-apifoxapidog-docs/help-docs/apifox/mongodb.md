# MongoDB

MongoDB 是一种面向文档的数据库管理系统，属于非关系型数据库（NoSQL），旨在为 Web 应用提供可扩展的高性能数据存储解决方案。与关系型数据库（SQL）不同，MongoDB 不使用 SQL 语句对数据库进行操作，而是使用数据库命令（Database Commands）或者更加简单易用的增删查改方法。扩展阅读：[《MongoDB 中文手册》](https://docs.mongoing.com/)。



## 连接数据库

1. 点击接口中的 “前置/后置操作”，选择 “数据库操作”。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/480342/image-preview)
</Background>


2. 点击 “数据库连接” 下拉框中的 “数据库连接管理” 选项，然后点击右上角的新建按钮。


<Background>
![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/480349/image-preview)
</Background>


3. 选择 MongoDB 数据库类型，然后填写相对应的连接信息。


<Background>
<img style="width:440px" src="https://api.apifox.com/api/v1/projects/5097254/resources/480357/image-preview"/>
</Background>


:::tip[]
Apifox 重视您的数据安全。**数据库地址、端口、用户名、 密码、数据库名**仅存储在客户端本地，不会同步到云端。即便是同一团队内，成员之间也不会相互同步数据库的连接信息，每个团队成员需要自己手动设置数据库。
:::

## 操作数据库

MongoDB 使用 BSON 格式存储文档数据。在 Apifox 中，你可以直接使用标准的 MongoDB 查询语法（如 `ISODate(...)`、`ObjectId(...)`）来编写查询条件与更新内容，从而更精确地控制数据类型。

例如，假设现在 MongoDB 内有这样一个 BSON 文档：

```json
{
    _id: ObjectId('65486728456e79993a150f1c'),
    name: "Apifox"
}
```

那么使用 Apifox 通过 `_id` 查询该文档时，你可以在「查询条件」处输入：

```json
{
    "_id": "65486728456e79993a150f1c"
}

// 或

{
    "_id": ObjectId('65486728456e79993a150f1c')
}
```


:::tip[]
当你使用字符串形式的 `_id` 且其格式符合 ObjectId 规范时，Apifox 会自动将其转换为 BSON 的 ObjectId 类型进行查询。
:::


### 常用操作

对于常用的增删查改操作，支持通过可视化界面操作。无需撰写任何 JavaScript 代码，只需要在 “操作类型” 中指定动作，然后指定 “集合名”，接着在 “查询条件” 中使用 JSON 撰写相应的内容。

例如针对上文提到的查询操作，输入命令并开启 “控制台打印结果” 后，就可以在控制台查看查询到的文档。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/480363/image-preview)
</Background>



为满足更多高级查询需求，你也可以在查询条件中使用 BSON 数据类型表达式，兼容 MongoDB 官方语法。

比如，你可以在查询条件中使用如下语法：

```js
{
  createdAt: ISODate("2023-11-15T00:00:00.000+00:00"),
  price: NumberDecimal("19.99"),
  _id: ObjectId("507f1f77bcf86cd799439011"),
  ts: Timestamp(1601000000, 1),
  bigNumber: NumberLong("9223372036854775807")
}
```

支持的 BSON 类型包括（不限于）：

| 类型         | 示例写法                                   | 说明               |
| ---------- | -------------------------------------- | ---------------- |
| Date       | `ISODate("2023-11-15T00:00:00.000+00:00")`     | 精确到毫秒的时间戳        |
| ObjectId   | `ObjectId("507f1f77bcf86cd799439011")` | MongoDB 文档主键常用类型 |
| Timestamp  | `Timestamp(1601000000, 1)`             | 内部 oplog 增量操作使用  |
| Decimal128 | `NumberDecimal("19.99")`               | 高精度小数            |
| Int64      | `NumberLong("9223372036854775807")`    | 大整数类型            |


### 进阶命令

如果需要更高级的操作，你也可以直接运行数据库命令。在 “操作类型” 中选择 “运行数据库命令”，然后输入 JSON 格式的数据库命令。需要注意的是，数据库命令并非指的是类似 `db.collection.findOne()` 的方法调用，而是特定格式的 JSON 数据。

比如，要查询 users 集合内的文档数量，就可以使用 `count` 这个数据库命令：

```json
{
    "count": "users"
}
```

输入命令后可以在控制台中查看结果。

## 了解更多

:::tip[最佳实践]
[操作指南：如何使用 Apifox 操作 MongoDB 数据库](https://apifox.com/blog/mongodb/)
:::
