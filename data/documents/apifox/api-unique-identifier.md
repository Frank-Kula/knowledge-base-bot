# 接口唯一标识

目前，大多数接口通过请求方法和接口路径进行区分。但在某些开发项目中，例如电商 API 文档，接口的请求 URL 是固定的，需要通过 `Query`、`Header` 中的参数来区分接口。

**“接口唯一标识”** 功能允许 `operationId`、`Query 参数`、`Body 参数` 和 `Header 参数` 作为区分接口的唯一标识符。

## 设置接口唯一标识

“接口唯一标识” 是目录层级的设置。当你需要为某个接口设置唯一标识时，必须在该接口的 “父级目录” 中进行配置。选择所需的唯一标识参数并点击保存后，该设置将应用于该目录下的所有接口。


<Background>

![CleanShot 2024-11-15 at 15.07.02@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/477551/image-preview)
</Background>


举例：现在存在一个电商 API 接口，它以 `Query 参数` 作为参数 action ，这可以作为“接口唯一标识”的参数。

在下图选择 “Query 参数” 后，在右侧的输入框中输入对应的参数名。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/477552/image-preview)
</Background>


## 填写标识的参数值

在 “接口唯一标识” 中点击该目录下的某个接口。点击 “修改接口” 选项后，你可以看到接口的基础信息和下方的请求参数中，均带有一个 `K` 的 icon，表示这是该 `接口唯一标识` 的参数。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/477553/image-preview)
</Background>


你可以在对应参数下填入对应的值并以此作为接口唯一标识的值。

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/477555/image-preview)
</Background>


## 查看接口唯一标识

设置 “接口唯一标识” 后，接口页将出现以下显示：


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/477556/image-preview)
</Background>




## 导入外部接口

导入时，接口匹配规则会根据目标 “目录” 的设置进行。如果导入目标的目录中的 “接口唯一标识” 不符合需求，可以在导入设置中进行修改；修改后，该设置将立即应用于目标目录。

举例来说，某电商 API 接口使用 `Query 参数` 中的 `action` 作为“接口唯一标识”。在将该接口导入 Apifox 时，可以选择目标目录，并点击 “接口唯一标识” 名称进行修改。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/477564/image-preview)
    
    
![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/477565/image-preview)
</Background>


:::tip[]
1. 将 `Query` 参数作为 “固定值” 功能仍然保留，但 “固定值” 在导入时仍会根据 URL 进行覆盖判断。建议使用 “接口唯一标识” 功能来替代 “固定值”。
2. “接口唯一标识” 功能支持设置多个参数。
3. 如果目录中仅某个子目录被设置为 “接口唯一标识”，在导入 Swagger 并更新所有目录时，请避免将所有项目导入到根目录进行更新。建议将已设置 “接口唯一标识” 的接口单独导入该特定子目录。
:::

## Mock 数据

若接口设置了 `接口唯一标识` 为 `Body 参数`、`Header 参数`，在使用 Mock 服务时需要发送 “路径 + 唯一标识的参数与参数值” 才能获得对应的 Mock 数据。


<Background>
 
![CleanShot 2024-11-15 at 15.46.00@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/477573/image-preview)
</Background>


:::tip[]
已设置 “接口唯一标识” 的项目，接口填写时需保持规范，避免出现相同 URL 的接口未设置 “接口唯一标识” 情况，以免导致无法正确获取 Mock 数据。
:::

