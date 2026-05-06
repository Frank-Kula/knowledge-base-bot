# 导入 OpenAPI/Swagger

Apifox 支持导入 OpenAPI 3.0、3.1 或 Swagger 2.0 数据格式的 JSON 或 YAML 文件。


支持导入 OpenAPI/Swagger 扩展，点击[此文档](https://docs.apifox.com/apifox-openapi-swagger-extension.md)查看 Apifox 所支持的接口字段。

在[手动导入](https://docs.apifox.com/manual-import.md)和[定时导入](https://docs.apifox.com/scheduled-import.md)时，都会出现一系列的导入选项，示例如下：

<Background>  
 
![CleanShot 2025-11-21 at 16.18.25@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/596020/image-preview)
</Background>

## 导入目标设置

### 目标分支
选择你想将数据导入到项目的哪个工作分支（通常默认为 `main` 主分支）。

### 导入到
你可以选择将新接口和数据导入到项目已有的模块中，或者直接创建一个全新的模块来存放它们。

## 接口和用例设置

### 自动生成接口用例
如果导入的文档不包含具体的测试用例，开启这个选项后，Apifox 会为每个接口自动生成一个默认的 “成功” 用例，方便你快速开始测试。

### 导入 Servers 为环境
如果导入的文档中定义了不同的服务器地址，开启后，Apifox 会将这些地址自动创建为项目中的不同环境，方便你切换测试目标。

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/596045/image-preview)
</Background>


## 安全和鉴权处理

Security Scheme（鉴权组件）是在 API 文档（例如 OpenAPI）里用来描述接口授权方式的配置。

它告诉客户端：访问接口时应该怎么携带认证信息，例如 Token、API Key、或 OAuth2 授权等。

### 导入 Security Scheme
开启后，会将文档中定义的各种安全设置（如 API Key、Basic Auth 等）导入到 Apifox 的 Auth 中。

- 你可以选择将 “导入文档” 中定义的全局鉴权配置，应用于 Apifox 项目根目录的 Auth 设置。

- 对于那些在 “导入文档” 中未明确设置 Security 的接口，你可以指定它们的处理方式，例如：继承父级目录的 Auth 配置，或者统一设置为“无需鉴权”。
<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/596121/image-preview)
</Background>

## 命名规则和 Summary

### 接口 Summary 为空
如果导入的接口没有一个清晰的名字（`Summary`），Apifox 会默认使用接口的 `operationId` 字段作为接口的名称。你也可以使用 path，或者从 description 提取。

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/596070/image-preview)
</Background>


## 资源冲突处理

当导入的数据与项目中的接口、数据模型或组件发生重复时，你需要决定如何处理。

### 接口冲突
当导入的接口与现有接口的 **方法（Method）和路径（Path）完全相同** 时：
* **覆盖已有接口**：新导入的接口会完全替换掉旧的接口内容。
* **保留两者**：两个接口都会被保留在项目中。
* **不导入**：直接忽略新导入的这个冲突接口。
* **智能合并**： 会保留旧接口内修改的中文名、Mock 规则、参数说明和接口的响应示例等。
* **覆盖指定字段**：选中的字段会被覆盖，其他未选中字段会保留现有的内容。

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/596098/image-preview)
</Background>

### Markdown、数据模型和组件
对于 Markdown 文件、数据模型和组件的冲突处理，有类似的下拉列表可供选择，例如选择 “覆盖” 或者 “智能合并”。

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/596109/image-preview)
</Background>


### 目录同步

当导入的接口与项目中的接口匹配时，但它们所属的目录信息（如目录名称、前/后置操作等）在新旧文件中不一致时，你可以选择：

- **保持已有接口的目录不变**：忽略新文件的目录信息，保留项目里原有的目录设置。

- **更新接口目录**：用新文件中的目录信息来更新项目里接口所属的目录。

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/596114/image-preview)
</Background>



### 资源清理

Apifox 会比较导入的新文件和项目中的现有资源：

- **不删除**：项目中那些在新文件中不存在的旧资源会被保留下来（安全选项）。

- **删除**：项目中那些在新文件中不存在的旧资源会被从项目中移除（同步选项，可以保持项目与导入源数据完全一致）。


<Background>
![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/596115/image-preview)

</Background>




## URL 导入

使用 URL 导入方式时需填写 `.json` 或 `.yaml` 数据文件的 URL（直链），而并非 `Swagger UI` 的 URL。例如：

```js
https://petstore.swagger.io/v2/swagger.json
```


<Background>
  
![CleanShot 2024-09-23 at 16.49.14@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/466995/image-preview)
</Background>


如果你是通过 URL 导入的，有些 URL 可能使用了 Basic auth 加密。在这种情况下，只需打开 Basic auth 开关并填写用户名和密码即可。

## 定时导入

打开 “项目设置”，点击 “导入数据 -> 定时导入” 选项。你可以在此处设置多个数据源并定时同步到具体目录中。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/467013/image-preview)
</Background>


:::tip[]
更详细的教程，请参考这篇最佳实践：[之前使用 Swagger 来管理 API，如何迁移到 Apifox？](https://apifox.com/blog/how-to-migrate-from-swagger-to-apifox/)
:::
