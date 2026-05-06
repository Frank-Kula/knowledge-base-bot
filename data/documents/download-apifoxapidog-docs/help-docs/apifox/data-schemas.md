# 数据模型 (Schema)

**Schema** 是 [OpenAPI 规范（OAS）](https://swagger.io/specification/) 的核心概念，也被称为“数据模型”，用于定义 API 中请求和响应的数据结构。

Apifox 基于 [JSON Schema](https://json-schema.org/) 标准构建数据模型。


## 数据模型的作用


- **统一数据结构**：定义标准的数据格式，确保 API 的一致性

- **生成 Mock 数据**：自动生成测试数据，支持前端开发

- **自动生成文档**：基于模型生成详细的 API 文档

- **数据验证**：验证 API 响应是否符合预期结构

- **模型复用**：在多个接口间共享数据结构

## 新建数据模型

你可以在 “数据模型” 目录中新建模型，创建方式有：

1. **手动创建**：在 “数据模型” 目录下新建

2. **快速导入**：支持从数据库表或 JSON Schema 中导入

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/476135/image-preview)

</Background>



## 构建数据模型

使用可视化编辑器，基于 JSON Schema 规范构建数据模型：

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/476136/image-preview)

</Background>

你还可以通过 [导入数据库表或 JSON](https://docs.apifox.com/generate-from-json.md) 来便捷地构建数据模型。

## 引用数据模型

创建好后，你可以在接口的请求体、响应体或其他数据模型中**直接引用**。
<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/476137/image-preview)

</Background>

