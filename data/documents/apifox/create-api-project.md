# 新建 API 项目

在 Apifox 中，每个项目都对应一个 API 定义（<Tooltip tip="也称 OpenAPI/Swagger 规范">API specification</Tooltip>） 文件或 OAS（OpenAPI 规范） 文件。你可以在 Apifox 应用的 **“首页 -> 我的团队 -> 新建项目”** 中创建新的 API 项目，或导入已有的项目。

## 创建项目

<Steps>
  <Step>
    在 “主窗口” 中点击右上角的 **“新建项目”**。
  </Step>
  <Step>
    选择项目类型。Apifox 目前支持三种类型的项目：`HTTP`、`gRPC`和`Dubbo`。

<p style="text-align:center">
    
<Background>
    <img src="https://api.apifox.com/api/v1/projects/5097254/resources/476054/image-preview" style="width:640px" />
</Background>
</p>

    - `HTTP`：适用于 `REST`、`SOAP`、`GraphQL`、`WebSocket` 等 API。
     
    - `gRPC`：适用于使用 [`gRPC`](https://docs.apifox.com/grpc.md) 协议的 API。
   
    - `Dubbo`：适用于使用 [`Dubbo`](https://docs.apifox.com/create-dubbo-api.md) 协议的 API。
  </Step>
  <Step>
    输入项目名称。
  </Step>
  <Step>
      （可选）勾选 **包含示例** 选项，以创建带有 “ 宠物商店” 示例数据的项目。
  </Step>
  <Step>
    （适用于有多个用户的团队）在创建项目时，为其他团队成员[设置权限](https://docs.apifox.com/member-roles-and-permissions.md)。
  </Step>
  <Step>
    （可选）设置[项目语言](https://docs.apifox.com/language-settings.md)。
  </Step>
</Steps>

## 导入已有 API

如果你已有 API 定义 *（<Tooltip tip="也称 OpenAPI/Swagger 规范">API specification</Tooltip>）* 文件，你可以在 **“团队 -> 项目”** 页面选择导入项目，或在现有项目中的 **“项目设置 -> 导入数据”** 里导入，适合将已有的 API 相关数据直接迁移到 Apifox 中。

<Steps>
  <Step>
    点击 “导入项目”
  </Step>
  <Step>
    选择已有的 API 数据的格式
        
<Background>

![CleanShot 2025-07-04 at 10.54.59@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/542125/image-preview)
</Background>


  </Step>
    
    <Step>
    将文件或带有数据的 URL（仅 OpenAPI/Swagger 格式支持）放入 Apifox 中
  </Step>
    <Step>
    Apifox 根据选中格式，自动识别文件或 URL 内的数据并解析渲染出来，可以在界面中预览实际要导入的数据。选择需要导入的内容并配置导入逻辑后，确认创建并导入。
        
<Background>

![CleanShot 2025-07-04 at 10.58.48@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/542126/image-preview)
</Background>

  </Step>
    <Step>
   完成后，即可看到新导入创建的项目。
  </Step>
</Steps>

:::highlight purple
更多导入流程的详细信息，请参考[导入指南](https://docs.apifox.com/manual-import.md)。
:::
