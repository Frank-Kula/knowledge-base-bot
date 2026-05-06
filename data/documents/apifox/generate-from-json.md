# 通过 JSON 等生成

在创建数据模型时，Apifox 提供了一些非常实用的功能组件，可以让你快速识别和从现有数据中创建数据模型。点击 “通过 JSON 等生成”，即可弹出面板。

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/476196/image-preview)
</Background>

在这里，你可以粘贴你的 JSON、XML、JSON Schema 数据以及从数据库导入数据，Apifox 会自动根据这些数据生成数据模型。

## 从 JSON/XML 生成


<Background>
 <p style="text-align: center">
    <img src="https://api.apifox.com/api/v1/projects/5097254/resources/476198/image-preview" style="width: 640px" />
</p>

</Background>


对于 JSON/XML，你只需将现有的 JSON 或 XML 粘贴到指定区域，系统会自动识别并转换为相应的数据模型和数据类型。

:::tip[]
- JSON 智能识别会根据提供的 JSON 自动生成数据结构，但不会保存 JSON 中包含的具体值。
- JSON/XML 中出现的所有属性默认为 “必需”。
- 描述和示例字段将保持空白。
:::



### 覆盖模式

当第二次从 JSON 生成数据模型时，新导入的数据将覆盖现有的数据模型。在这种情况下，提供两种 “覆盖模式”：

- **智能合并（默认）**：在匹配参数时，保留原数据模型中的示例和描述。
- **完全覆盖**：所有现有数据将被替换，新数据将完全覆盖旧数据。

### 命名风格

你可以选择合适的命名风格：

- **保持原样**
- **小驼峰 camelCase**
- **大驼峰 PascalCase**
- **下划线 snake_case**


### 保存为示例

在接口的请求体或响应体中使用 “通过 JSON 等生成” 时，启用 “保存为示例” 功能将把当前的 JSON/XML 内容作为请求/响应示例，随数据模型一起生成。

## 从 JSON Schema 生成

直接粘贴 JSON Schema 可以实现数据结构的可视化识别。

## 从数据库导入

Apifox 支持两种从数据库表生成数据模型的方法。第一种方法是直接连接到数据库以读取表结构，第二种方法是粘贴 SQL DDL 来识别表结构。

### 数据库连接


要从数据库导入数据模型，请按照以下步骤操作：
<Steps>
  <Step>
    设置数据库连接。
      
:::highlight purple
了解更多关于[数据库连接](https://docs.apifox.com/database.md)的信息。
:::
  </Step>
  <Step>
    在 “从数据库导入” 中选择数据库连接。
  </Step>
  <Step>
    选择要导入的表。
      ![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/476200/image-preview)
  </Step>
  <Step>
    配置导入选项。具体配置，请参考之前关于 JSON/XML 处理的部分。
  </Step>
</Steps>

:::tip[]
当“遵循数据库字段长度”开关启用时，Apifox 将根据表中定义的字段长度设置最小和最大属性长度值。
:::

### 输入 SQL（DDL）


粘贴数据库表的 “创建” 语句（DDL）以生成数据模型，支持与 MySQL 兼容的 SQL。
![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/476201/image-preview)

有关具体的配置设置，请参考之前关于 JSON/XML 处理的部分。

## Mockjs

Apifox 支持通过 Mock.js 格式的示例数据生成数据模型结构。你可以粘贴带有 `@cname`、`@email` 等占位符的 JSON 示例，系统会自动识别字段类型和 Mock 配置。

**示例：**

```json
{
  "id": 1,
  "name": "@cname",
  "email": "@email",
  "age": 28,
  "isVip": true,
  "tags": ["@word", "@word"],
  "scores": [90, 85, 78],
  "profile": {
    "avatar": "@image",
    "bio": "@sentence"
  },
  "createdAt": "@datetime",
  "location": {
    "province": "@province",
    "city": "@city"
  }
}
```

**生成效果说明：**

* 所有字段会自动识别为对应的类型（string、number、boolean、array、object）
* 包含 `@xxx` 占位符的字段，会自动填入对应的 Mock 值
* 嵌套结构会被保留为子对象
* 数组会自动识别 `items` 类型


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/551602/image-preview)
</Background>


:::tip[]
* 示例必须是**合法 JSON 格式**，字段名及字段值需使用 **双引号 `"`**，不能使用 **单引号 `'`**。
* Mock.js 中的字段名修饰语法（如 `"id|+1"`、`"tags|1-3"`）**不会被识别**，可在模型生成后手动设置 Mock 规则。
:::


