# 快速上手


`Apifox Helper` 是 Apifox 团队针对 IntelliJ IDEA 环境所推出的插件，可以在 IDEA 环境中识别本地 Java、Kotlin 后端项目的源代码，自动生成 API 文档并一键同步到 Apifox 的项目中。


对于常见的开发框架，`Apifox Helper` 插件能够做到开箱即用，实现真正的代码零侵入。如下图所示，仅通过识别最基本的 SpringBoot 代码，即可生成一份详尽的 API 文档。

<Background>
![](https://cdn.apifox.cn/uploads/help/202401101156728.png)
</Background>



支持开箱即用的框架和库如下：

| 类型       | 名称                                                                                        | 注解示例                                      |
| ---------- | ------------------------------------------------------------------------------------------- | --------------------------------------------- |
| 服务端框架 | &#8226; Spring                           <br> &#8226; Jakarta RESTful Web Services (JAX-RS) | @RestController, @GetMapping <br> @Path, @Get |
| 校验库     | &#8226; Jakarta Bean Validation <br> &#8226; Java Bean Validation                           | @NotNull                                      |
| 序列化库   | &#8226; FASTJSON <br>  &#8226; Jackson  <br> &#8226; GSON <br>                              | @JsonProperty <br>  @SerializedName           |
| API 规格库 | &#8226; Swagger 2.x  <br> &#8226; Swagger/OpenAPI 3.x                                       | @ApiOperation, @ApiParam                      |
| 客户端库   | &#8226; Spring Cloud OpenFeign                                                              |                                               |
| 性能指标库 | &#8226; Spring Boot Actuator                                                                |                                               |
| 语言与注释 | &#8226; Java: Javadoc <br> &#8226; Kotlin: KDoc                                             |                                               |


:::highlight purple 📌
本插件基于 [easy-api](https://github.com/tangcent/easy-api) 定制开发，**感谢 easy-api 作者。**
:::


## 下载与安装

可以在 IntelliJ IDEA 中安装 Apifox Helper 插件。打开 IDEA 设置，进入 Plugins（插件）页面，搜索 “Apifox” 并安装 “Apifox Helper” 插件，安装完成后需要重启 IDEA 使插件生效。

<Background>

![CleanShot 2025-01-07 at 14.33.08@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/488261/image-preview)
</Background>

也可以在 Jetbrains Marketplace 中下载并安装 [Apifox Helper](https://plugins.jetbrains.com/plugin/20549-apifox-helper) 插件。

<Embed src="https://plugins.jetbrains.com/embeddable/install/20549" width="245px" height="48px"/>

<br />

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/492317/image-preview)
</Background>



:::tip[]
插件仅支持 IntelliJ IDEA 2019.3 及更高的版本。
:::

## 配置 API 访问令牌

在使用 `Apifox Helper` 插件之前，需要提前注册 [Apifox 账号](https://apifox.com/)，并生成对应的 [API 访问令牌](https://docs.apifox.com/api-access-token.md)，详细说明请参考[《Apifox 开放 API》](https://apifox.com/help/openapi)。


在 `Apifox Helper` 内填写自己的 API 访问令牌，然后点击「测试令牌」。如果测试成功，请点击「应用」或「确定」按钮，然后正常使用 Apifox Helper。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/488262/image-preview)
</Background>


## 同步接口

支持同步以下范围内的接口：

- **模块内的全部接口**：在左侧目录树的模块节点，点击右键，选择「Upload to Apifox」
- **Controller 内的全部接口**：在 Controller 文件内部，点击右键，选择「Upload to Apifox」


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/488264/image-preview)
</Background>

- **Controller 里的指定接口**：找到 Apifox Helper 菜单即可上传指定接口
 
<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/546479/image-preview)
</Background>


如果是首次同步，需要在弹出的对话框内选择接口的目标同步项目，你可以选择项目或项目内的目录。如果选择项目，则将会上传至项目的根目录。


数据模型无需配置，API 文档将默认上传至接口所在项目的**数据模型根目录**。

<Background>
 
![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/488265/image-preview)
</Background>


:::warning 注意事项
`Apifox Helper` 旧版本中所提供的，通过输入文字来指定上传的目标目录方式将被废弃。如果你使用该方式指定目录，当项目内的其他目录存在相同接口时，有可能出现以下问题：
- 创建了新的目录，但是目录内没有接口，即产生空目录；
- 创建了新的目录，目录内有接口，但是其他目录内的同名接口消失。

请尽快改用新的目录选择方式。
:::

## 查看接口文档

API 文档同步成功后，打开 Apifox。点击右上角的刷新按钮，即可看到从 Java 或 Kotlin 源代码中识别出来的接口文档。


你可以非常方便的将自动生成的 API 文档分享出去，以便其他人可以很方便地通过浏览器中进行查看。详细说明请参考[分享 API 文档](https://docs.apifox.com/share-api-documentation.md)。

## 常见问题


<Accordion title="为什么网络连接正常，但是点击「测试令牌」或上传接口时，界面提示「网络连接超时，请检查网络」？" defaultOpen>
一般是配置了无法访问外网的代理服务器所导致的，请将 IDEA 配置为「无代理」。

    
    <Background>

    ![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/488267/image-preview)
    </Background>

</Accordion>


<Accordion title="为什么 IDEA 控制台输出的中文，比如项目名称，无法正常显示？" defaultOpen={false}>
请在「更多设置项」中调整 Common 的 charset 设置，依次尝试里面的不同编码。

    
    <Background>

    ![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/488268/image-preview)
    </Background>
</Accordion>


## 隐私与安全声明

`Apifox Helper` 插件仅在用户本机执行对于 Java 、Kotlin 源代码的识别工作。Apifox 重视您的数据资产安全，您的 Java 、Kotlin 源代码永远不会被上传至 Apifox 服务器。

## 联系我们

在使用 `Apifox Helper` 插件中所遇到的任何问题或建议反馈，请添加下方微信（备注：IDEA），加入用户群沟通交流。

<Background>
<img alt="Apifox IEDA 插件交流群" src="https://api.apifox.com/api/v1/projects/5097254/resources/488269/image-preview" width="360px"/>

</Background>



