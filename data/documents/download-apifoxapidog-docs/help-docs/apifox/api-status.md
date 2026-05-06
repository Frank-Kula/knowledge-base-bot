# 接口状态

在 Apifox 中，一个非常实用的内置字段是 “接口状态”。该字段用于指示接口的当前状态，例如开发阶段、测试阶段或已发布。

接口状态字段不仅供内部团队参考，还会在 Apifox 为外部用户生成的 API 文档中显示。

## 使用接口状态

在 Apifox 中指定一个接口时，你可以选择该接口的状态。默认情况下，新创建的接口状态为 “开发中”。

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/477517/image-preview)
</Background>


在接口目录中，每个状态名称前都有一个彩色圆点，用于表示接口的不同状态。该颜色标识帮助用户快速区分接口及其状态，使接口目录树一目了然。


<Background>
<p style="text-align:center">
    <img src="https://api.apifox.com/api/v1/projects/5097254/resources/477518/image-preview" style="width:440px" />
</p>
</Background>

在该颜色方案中，蓝色表示 “开发中”，红色代表 “测试中”，灰色表示 “已弃用”。没有彩色圆点的接口则表示 “已发布”，通常无需特别关注。

在发布的文档中，这些彩色圆点也用于标识接口的状态。

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/477519/image-preview)
</Background>


## 配置接口状态

每个团队的开发流程可能不同，因此所需的接口状态也会有所差异。Apifox 允许团队根据实际需求自定义和选择适用的接口状态。

你可以在 “项目设置 -> 通用设置 -> 功能设置 -> 接口功能设置” 模块中配置和启用所需的接口状态。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/477520/image-preview)
</Background>


## 常见问题


<Accordion title="我可以自定义一个新的状态吗？" defaultOpen>
由于不同的状态对应特定的功能，因此不支持自定义新的状态。你可以从列出的状态中选择最适合你团队需求的状态。
</Accordion>

