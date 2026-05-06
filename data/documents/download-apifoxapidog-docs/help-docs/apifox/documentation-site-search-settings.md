# 文档站搜索设置



> Apifox 版本需 `≥ 2.7.61`

发布文档提供默认的搜索功能，默认的搜索功能目前只能搜索文档/接口的名称和路径。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/484826/image-preview)
</Background>


Apifox 也支持 Algolia 的搜索功能，你只需将 Algolia 中的字段回填到 Apifox 的设置项中，即可启用此功能。


<Background>


![CleanShot 2025-12-25 at 15.10.17@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/607404/image-preview)
    

![CleanShot 2025-12-25 at 15.10.55@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/607405/image-preview)
</Background>



:::tip[]
注意：Algolia 可以免费使用，但是有一定限额；如需提升限额，可以使用 Algolia 的付费版，或者[申请免费的 Algolia DocSearch 计划](https://docsearch.algolia.com/apply/)。
:::


## Algolia 基础配置流程


### 注册并创建 Algolia 应用

登录 Algolia 官网 `https://www.algolia.com/`，进行注册账号。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/484830/image-preview)
</Background>


注册账号后，创建一个新的应用。

### 创建 Index（数据源）

在创建流程中，数据源选择 「上传文件」。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/484831/image-preview)
</Background>


将页面中提供的示例数据复制出来，保存为一个 `.json` 文件，并上传。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/484832/image-preview)
</Background>


:::tip[]
JSON 文件的名字，就是实际的 `Index Name`，需要回填到 Apifox 的搜索配置表中。
:::

### 完成 Index 创建

后续步骤中，数据展示配置可随意填写。

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/484833/image-preview)
</Background>


后面几步可以忽略，直接往下点击“下一步”。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/484834/image-preview)
</Background>


到最后一步，会让你选择构建搜索的方式，忽略即可。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/484835/image-preview)
</Background>

### 将 Algolia 配置回填至 Apifox

Index 创建完成后，在 Algolia 应用首页可以找到以下关键信息：

- Application ID

- Search API Key

- Write API Key

- Index Name

将这些字段完整填写到 Apifox 在线文档的搜索配置中并保存。

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/484836/image-preview)
    
![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/484837/image-preview)
    
</Background>


配置项中 `Index Name` 的值可以在这里找到，也就是你在第一步中上传的 JSON 文件的名字。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/484838/image-preview)
</Background>

配置完毕后，Apifox 会自动将 Algolia 的配置项同步，并启用 Algolia 的搜索功能。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/484839/image-preview)
</Background>


![Kapture 2024-12-19 at 15.03.29.gif](https://api.apifox.com/api/v1/projects/5097254/resources/484841/image-preview)

:::tip[]
注意：Algolia 可以免费使用，但是有一定限额；如需提升限额，可以使用 Algolia 的付费版，或者[申请免费的 Algolia DocSearch 计划](https://docsearch.algolia.com/apply/)。
:::

## 免费的 Algolia DocSearch 计划（推荐）

Algolia 提供专门面向文档站点的 DocSearch 免费计划，非常适合 Apifox 发布的在线文档使用。

你可以在此[申请免费的 Algolia DocSearch 计划](https://docsearch.algolia.com/apply/)，里面需要填入的 Documentation URL 可以填写 Apifox 中公开的文档地址。


当申请成功之后，Algolia 会给你发送邮件，并且在其后台，会收到一条邀请你加入应用程序的消息，点击确认即可。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/484844/image-preview)
</Background>


:::tip[]
邮件通常会在申请通过后 1–3 个工作日内发送，具体以 Algolia 实际处理时间为准。
:::

### 获取 Application ID 和 Search API Key

在页面左上角切换到相应应用程序，找到该应用程序的 **Application ID** 和 **Search API Key** ，并将其填入 Apifox 的相应配置项。请注意，**Write API Key** 需要在其他位置查找。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/484846/image-preview)
</Background>

### 获取 Write API Key

要找到免费的 Algolia DocSearch 计划中的 Write API Key，你可以参考以下图文步骤获取。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/484847/image-preview)
    
 ![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/484848/image-preview)
</Background>




这里的 `Algolia API Key` 需要配置到 Apifox 配置项中的 `Write API Key` 里。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/484849/image-preview)
</Background>

### 获取 Index Name

配置项中 `Index Name` 的值可以在这里找到。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/484850/image-preview)
</Background>

配置完毕后，Apifox 会自动将 Algolia 的配置项同步，并启用 Algolia 的搜索功能。

## Ask AI 搜索

在启用 Algolia 搜索的基础上，Apifox 还支持 Ask AI 搜索，用于在文档中提供更智能的问答式搜索体验。

Ask AI 搜索无需额外复杂配置，只需在 Apifox 中填写 Algolia 提供的 Ask AI Assistant ID 即可启用。

<Background>

![CleanShot 2025-12-25 at 15.51.13@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/607429/image-preview)
</Background>


**如何获取 Ask AI Assistant ID？**


<Steps>
  <Step>
    登录 Algolia 后台，进入对应的 Application（应用）
  </Step>
  <Step>
    在左侧导航中找到 Ask AI 或 AI Assistant 相关配置入口
      
<Background>

![CleanShot 2025-12-25 at 16.06.02@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/607438/image-preview)
</Background>

  </Step>
  <Step>
    创建或选择一个 Assistant，根据操作步骤来填写相关信息，完成后，等待 Algolia 官方审核。在 Assistant 详情页中即可看到 Assistant ID。
  </Step>
</Steps>


将该 Ask AI Assistant ID 填写到 Apifox 在线文档的 Ask AI 配置项中并保存，即可生效。


配置完成后，可以直接通过自然语言向文档提问，搜索结果将由 Algolia Ask AI 智能返回。


<Background>
![Algolia Ask AI](https://cdn.apifox.cn/uploads/help/202512251632119.gif)
</Background>





