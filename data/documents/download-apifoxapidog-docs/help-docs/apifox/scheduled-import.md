# 定时导入（绑定数据源）

如果你在 Apifox 之外维护 API 定义 *（<Tooltip tip="也称 OpenAPI/Swagger 规范">API specification</Tooltip>）* ，但希望使用 Apifox 进行 API 调试、测试和文档管理，你可以使用定时导入功能。

## 创建定时导入


<Steps>
  <Step>
前往 **项目设置** - **导入数据** - **定时导入（绑定数据源）**
      

<Background>
![CleanShot 2025-11-21 at 16.09.51@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/596009/image-preview)
</Background>

  </Step>
  <Step>
点击 “**新建**” 来创建一个数据源。
  </Step>
  <Step>
填写必要信息，例如导入频率、数据源的 URL 等。
<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/606697/image-preview)
</Background>
  </Step>
  <Step>
点击 **保存**。定时导入会根据你设置的导入频率自动执行。
  </Step>
</Steps>

## 工作原理

定时导入的工作方式如下：默认情况下，定时导入是从你的 **本地客户端** 启动的。首先，你的 Apifox 客户端会访问数据源，获取数据后再更新到 Apifox 项目中。

这意味着：

1. 定时导入仅在客户端打开时执行。具体来说，只有当你对项目有写入权限、项目已经在客户端打开，并且距离上一次定时导入的时间超过了你设置的导入频率间隔时，定时导入才会执行。
2. 定时导入可以将内网数据导入到 Apifox，只要你的客户端可以正常访问数据源地址。

因此，如果项目长时间未打开，定时导入将不会生效。下次打开时才会进行更新。

:::tip[]
如果你在 [Apifox Web](https://app.apifox.com) 版中打开项目，也会触发定时导入。但在这种情况下可能会有些不同：由于浏览器网络环境的限制，Web 版可能无法访问内网数据。
:::

为了解决上述问题，Apifox 提供了第二种定时导入机制：你可以通过自托管的 Runner 来启动导入，而不是依赖本地客户端。

如果你已经在服务器上部署了 Runner，Runner 将会按照固定的时间间隔自动从数据源导入数据，而不需要考虑客户端是否打开。

:::highlight purple
了解更多关于[自托管 Runner](https://docs.apifox.com/universal-runner.md) 的信息。
:::

## 导入迭代分支

可以选择一个迭代分支定时导入数据，默认选中主分支。如果切换了其他迭代分支，会按照设置规则定时向这个迭代分支中导入数据。导入迭代分支的详情可以参考[将 OAS 导入迭代分支](https://docs.apifox.com/api-changes-in-sprint-branch.md)模块。

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/596016/image-preview)
</Background>


## 定时导入选项

- **目标分支**： 将数据导入到选中的分支

- **模块**：将数据导入到选中的模块

- **导入频率**：设置多久触发一次导入。如果上次导入后的时间超过了该时间段，导入将会被触发。

- **数据源格式**：支持 OpenAPI、ApiDoc 或 Apifox 等格式。

- **数据源名称**：自定义名称，用于区分不同的数据源。

- **数据源**：
    - **URL**：数据源的 JSON/Yaml 文件 URL，例如：<CopyToClipboard>`https://petstore.swagger.io/v2/swagger.json`</CopyToClipboard>
    - **Git 仓库**：Git 仓库里的 JSON/Yaml 文件，参考 [Git 仓库连接](https://docs.apifox.com/7230090m0)。

- **运行位置**：选择定时导入的启动位置。默认是本地客户端，你也可以选择已部署的 Runner。

- **Basic Auth**：用于访问加密的 URL。

- **高级设置**：请查看[导入设置](https://docs.apifox.com/import-settings.md)。

:::tip[]
Apifox 支持在单个项目中创建多个数据源，并将数据同步到不同的文件夹中。
:::


