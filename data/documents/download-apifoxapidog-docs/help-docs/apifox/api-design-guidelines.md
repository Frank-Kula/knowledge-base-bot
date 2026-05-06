# 接口设计规范

> 请确保 Apifox 版本不低于 `2.7.22`

Apifox 强烈建议全部的接口文档，在设计时遵从 [OpenAPI（Swagger）规范](https://swagger.io/resources/open-api/)。你可以参考[这篇文章](https://www.openapis.org/what-is-openapi)，来了解为什么我们的接口需要遵从规范。

同时，Apifox 的很多其他功能，例如 AI 检测接口规范、AI 字段命名等，都依赖于一份已经完成的完整设计规范。有了这份规范，不仅可以让 Apifox 中的其他相关功能的效果更好，同时也可以规范团队成员按照规范来设计接口。

在 Apifox 中，你可以在 **“接口管理 -> 目录树”** 上方的主添加按钮中，点击“更多”，然后新建一个接口设计规范。


<Background>

![CleanShot 2025-11-05 at 16.38.09@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/588566/image-preview)
</Background>

点击新建接口设计规范后，有两种选择：

1. 选择使用 Apifox 提供的完整接口设计规范模板进行创建，推荐一般情况下使用。此模板是基于 OAS 规范并参考了微软接口设计最佳实践后整理出来的；

2. 选择创建一个空的设计规范，仅有一个设计规范的基本结构，没有详细内容。自己撰写自己团队的接口设计规范，如果你的团队已有沉淀规范和最佳实践，可以选择从这种方式开始。

<Background>
<img src="https://api.apifox.com/api/v1/projects/5097254/resources/553581/image-preview" width="460px"  />

</Background>

选择符合需求的模板并预览确认后，即在当前项目中会新建出一个接口设计规范。设计规范中的全部内容可以根据实际情况任意进行调整。设计规范会展示在接口管理的目录树最上方，用以让全部成员注意规范的重要性。

<Background>

![CleanShot 2025-07-31 at 15.48.04@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/551090/image-preview)
</Background>


:::tip[]
了解更多：[接口规范性检测](https://docs.apifox.com/api-compliance-check.md)
:::
