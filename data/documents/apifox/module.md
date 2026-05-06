# 模块

在一个 Apifox 项目中，你可以使用模块来对你项目中的接口进行组织。模块与技术领域中的 “服务” 概念类似，意在帮助微服务架构等场景下的接口能够更好的进行管理与展示。每个模块拥有一套相关的业务**接口**、**组件**（数据模型、响应、鉴权）、**前置 URL**（每个环境均有一个），对应一份完整独立的 Swagger/OpenAPI 规范文件。

当你的接口有类似以下情况，需要使用多套前置 URL，并且期望更高效的进行管理与展示，我们都建议通过使用模块的方式来组织接口：
- **关联性较强**。例如 AI 项目，有文本模型 API、文生图模型 API、语音模型 API...
- **微服务**。例如电商项目，有鉴权服务、订单服务、商品服务...
- **多版本**。例如项目中存在多个版本 API 提供给外部用户， Legacy 版本、LTS 版本、Latest 版本...


## 创建模块


<Steps>
  <Step>
    在项目中，将鼠标悬停在目录树上方的 `+` 按钮，即可在下拉菜单中看到 “新建模块” 的入口。

<Background>
<img src="https://api.apifox.com/api/v1/projects/5097254/resources/588569/image-preview" width="460px"/>
</Background>

  </Step>
  <Step>
输入模块名称后点击保存，即可创建新模块，并在目录树中看到。可以点击查看模块本身的详情，包括：
  - 模块中资源的数据统计；
  - 模块中 API 的用例与场景覆盖统计；
  - 模块中 API 的导出入口；
  - 模块的数据源设置；
  - 模块变量（类似 [环境变量](https://docs.apifox.com/global-environment-session-variables)，该变量范围为仅本模块内的接口请求可用）
      
<Background>

![CleanShot 2025-07-07 at 11.35.37@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/542710/image-preview)
</Background>

  </Step>
</Steps>


## 维护模块对应的前置 URL

如果已经创建好了模块，则在 [环境管理](https://docs.apifox.com/environments-and-services) 中，可以看到前置 URL 部分会自动增加新创建的模块。你可以在环境管理内给每个环境中的新创建模块填写对应的前置 URL。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/542714/image-preview)
</Background>

## 请求时正确使用前置 URL

在一般情况下，本模块中的接口，实际请求时，会根据当前所处环境，取到当前模块环境中设置的前置 URL，拼接接口的 path 后发出请求。不可以让当前模块中的接口使用其他模块的前置 URL 实际发送请求。

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/542716/image-preview)
</Background>


:::caution[]
如果你的某个模块中存在多个服务（前置 URL），可以在模块的目录、接口中指定该资源实际使用的前置  URL。此功能主要为兼容以前 Apifox 的概念和用法，在 `2.7.16` 版本后，已**不推荐单个模块中存在多服务**。如仍有相关需求，请将一个模块内的多服务拆成多个模块进行使用。

了解更多：[通过模块来使用多个前置 URL](https://docs.apifox.com/environments-and-services#%E9%80%9A%E8%BF%87%E6%A8%A1%E5%9D%97%E6%9D%A5%E4%BD%BF%E7%94%A8%E5%A4%9A%E4%B8%AA%E5%89%8D%E7%BD%AE-url)
:::
