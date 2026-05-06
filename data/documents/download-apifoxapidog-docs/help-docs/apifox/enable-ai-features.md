# 启用 AI 功能

Apifox AI 功能是默认关闭的，你可以在 「组织 / 团队设置 - AI 功能」 中，开启 AI 功能，来让组织 / 团队内的全部项目，都可以使用 AI 能力来提升效率。

- AI 功能依赖你自行配置的 AI 模型提供商，你可以选择任意 AI 模型提供商，并使用自己的 API key。

- Apifox 本身不提供 AI 模型，也不会使用你的数据进行训练。

:::caution[]
配置 AI 功能需具备**组织或团队管理员及以上权限**，并确保 Apifox 版本为最新版本。
:::

## 配置 AI 供应商

在 AI 功能开启后，即可看到 AI 模型供应商的配置入口。点击添加供应商，即可开始进行配置。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/548314/image-preview)
</Background>

目前 Apifox 提供以下供应商来接入 AI 模型：

- 火山引擎
- 阿里云百炼
- 腾讯云
- 硅基流动
- 深度求索

如果以上供应商不满足你的需求，你也可以通过 “自定义 API 配置”，来接入其他供应商的模型。


:::caution[]
AI 功能是经过 Apifox 服务端访问大模型的，故当前只支持国内的模型提供商。
:::

一般来说，以下内容可以由你自定义配置：

1. **API Key**

调用各个供应商 AI 接口的鉴权。可以使用测试功能来看 Key 是否生效；

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/548315/image-preview)
</Background>


2. **API 前置 URL**

在 Apifox 中使用 AI 功能时，请求实际发送到的 URL。预设的供应商会自动填充通用的前置 URL，你也可以根据实际情况修改。

:::tip[]
每次对 AI 模型的请求，均是从 Apifox 服务端发起至此 API 前置 URL。
:::

3. **模型列表**

AI 供应商提供的模型列表。如果使用 Apifox 预设的供应商，会有一些默认模型供选择。此列表中开启的模型才可在 AI 功能中被使用。如果你需要使用的模型不在此列表中，你可以使用添加模型功能来添加你需要的模型。


:::tip[]
Apifox 相关 AI 功能，有我们预设好的 Prompt 和调用流程。如果想要 AI 功能有较好的效果，**请务必选择先进、强大的模型**（支持更长的上下文、function calling 等高级能力）。如 Apifox 预设提供的模型，DeepSeek-V3-0324 等。 能力较弱的模型可能会导致 Apifox AI 相关功能的使用结果不符预期。
:::

4. **API 格式**

在 “自定义 API 配置” 中可以调整，影响自定义 API 请求与响应的格式使用，选择不正确可能会导致 API 调用失败。一般来说，大多数模型都支持 OpenAI 格式。


## 设置默认模型

当在 AI 功能中没有指定使用哪个模型时，功能默认使用的模型即为此处指定的模型。下拉可选项，是模型供应商中设置启用的具体模型。你可根据实际需求指定某个模型作为整个组织 / 团队中 AI 功能使用的默认模型。

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/548318/image-preview)
</Background>


默认模型会默认使用 “自动选择” 模型，其逻辑为根据启用供应商及启用模型的顺序，自动选中一个有效模型进行使用。

如果你在默认模型中指定了某个具体模型（例如设置了阿里云百炼的 DeepSeek V3 模型），如果此模型或所属供应商被停用 / 删除，则默认模型会重置为 “自动选择”。

## 功能 & 提示词

所有 Apifox AI 功能，都可以由此处进行功能入口的控制与提示词的调整。相关 AI 功能的开关打开后，在项目中的对应位置才可看到功能入口；可以查看 Apifox 预设的提示词，并根据自己的实际情况，对提示词进行调整，让 AI 能够输出更符合实际需求的数据。

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/548320/image-preview)
</Background>


:::warning[]
提示词调整功能目前暂未开放，敬请期待。
:::

## 从组织中继承 AI 配置到团队

如果你使用到了组织功能，则可以让组织的管理员、所有者在组织层级配置 AI 功能。这样在组织下的全部团队，都可继承使用组织中已经配好的相关 AI 配置，并且团队中的配置会受到组织中配置的管控，用以更好的控制整个组织对 AI 功能的使用。

在组织的「设置 - AI 功能」中，同样有配置的界面，可以进行跟上述团队配置 AI 供应商一样的操作。

<Background>

![CleanShot 2025-07-23 at 10.14.46@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/548325/image-preview)
</Background>


在组织中配置好 AI 功能后，组织下的全部团队均可继承来自组织的 AI 供应商、默认模型、功能配置。

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/548328/image-preview)
</Background>


**组织下团队继承的特点：**

1. 所有开关<span style="color: #999">（AI 功能整体开关、供应商开关、模型开关、具体功能开关）</span>，均会继承组织级别的配置。如果组织级开启，则组织下团队的对应开关可以选择开启或关闭；如果组织级关闭，则组织下团队的对应开关直接禁用。这样是为了更好的适配从组织级对 AI 功能的整体管理需求。



2. 模型供应商可以选择继承自组织，也可以选择自定义来根据团队的实际情况自己配置。

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/548330/image-preview)
</Background>


3. 默认模型配置同样可以选择继承组织配置的供应商，也可以团队自己独立设置有效的模型。

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/548334/image-preview)
</Background>

