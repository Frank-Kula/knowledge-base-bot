# 字段命名

:::tip[关于 AI 功能]

1. AI 功能默认关闭，你需要手动 [启用 AI 功能](https://docs.apifox.com/enable-ai-features) 才可以开始使用（请确保 Apifox 版本`≥2.7.37`）。

2. AI 功能免费提供，但不内置 AI 模型，你需要自行 [添加 AI 模型](https://docs.apifox.com/enable-ai-features#%E9%85%8D%E7%BD%AE-ai-%E4%BE%9B%E5%BA%94%E5%95%86) 并配置对应的 API Key。
:::


可以让 AI 基于你对当前接口文档中的某个字段的描述，结合[接口设计规范](https://docs.apifox.com/api-design-guidelines.md)，生成符合要求、规范、专业易读的字段名称。

你可以在接口文档/数据模型/响应组件中，针对某个字段的右侧找到 AI 字段命名的功能入口，点击即可让 AI 开始命名。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/551043/image-preview)
</Background>

点击 AI 命名功能后，输入一段对当前需要命名字段的描述，用来指导 AI 进行字段名生成，也可更改使用模型。如果你已经在当前字段的描述文本框中输入了内容，产品会自动将其带入 AI 命名的描述中。

<Background>
<img src="https://api.apifox.com/api/v1/projects/5097254/resources/551053/image-preview" width="460px"  />
    
</Background>


点击发送后，AI 会根据接口设计规范、当前文档内容、字段描述，生成多个字段名，并给出每个字段名的介绍与评分。
<Background>
<img src="https://api.apifox.com/api/v1/projects/5097254/resources/551062/image-preview" width="460px"  />
    
</Background>


可以选择某个 AI 生成的字段名，然后点击采纳，即可将此字段名应用到文档中。

<Background>

![03-Apifox.gif](https://api.apifox.com/api/v1/projects/5097254/resources/551069/image-preview)
</Background>

