# 快捷分享


在 API 设计、开发、沟通、协作中，逻辑上应该以团队内共同定义的 API 文档为标准。但实际操作中，团队成员习惯依靠 Word、PDF 格式文件进行 API 文档协作，造成大量信息未能及时同步，将接口以**在线文档**形式分享将有助于提高团队之间的沟通效率。



## 创建快捷分享

在左侧切换到 **“分享文档”** 模块。

<Background>   

![CleanShot 2024-12-10 at 18.09.52@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/482860/image-preview)
</Background>

点击「+新建分享」按钮以创建快捷分享。一个项目可以创建多个不同的快捷分享，可以分发给不同的协作者。所有团队成员都能看到其他人创建的所有快捷分享。

<Background>

<img style="width: 460px"  src="https://api.apifox.com/api/v1/projects/5097254/resources/482861/image-preview" />

</Background>

在新建分享弹窗中，你可以自定义以下选项：

- **标题**：此分享的名称，仅在 Apifox 团队内可见，用于内部识别，在分享的文档中不可见。

- **运行环境**：选择在线文档中可用的环境。默认不选择任何环境，可以自由选择多个环境。读者可以在文档中看到已选择的环境，并在 “在线调试” 时使用这些环境。
    :::tip[]
    创建文档时如果选择了云端 Mock 环境，相当于为文档读者开启了一个简单的沙箱环境。
    :::

- **展示内容**：文档有两个可选组件：前置 URL 和示例代码。你可以选择是否在文档中显示它们。
  - **前置 URL**：这是在环境中设置的前置 URL。如果选中，文档中的每个接口都会显示完整 URL；如果不选中，文档中的 URL 将以"/"开头。
  - **示例代码**：是否显示调用请求的示例代码。。

- **允许导出数据**：是否允许读者以 OAS/Markdown/HTML/Apifox 格式导出数据。

- **分享接口范围**：选择要包含在此分享中的 API 和 Markdown。可以按目录选择或通过标签筛选和排除。

- **安全性**：可以设置访问文档是否需要密码，以及文档的过期时间。如果不选择过期时间，则永不过期。

- **项目展示字段**：接口字段中启用的自定义字段，可以设置这些字段是否在文档中显示。

- **文档语言**：设置文档界面的显示语言，这会改变系统内置的一些文本显示，比如 “Query 参数”、“示例代码” 等固定用语，但不会影响你自己编写的 API 文档内容。

- **AI 相关特性**：LLMs.txt 及 “复制页面” 功能默认开启，你无需额外设置即可使用，可在此管理启用状态。

- **高级设置**：可以在这里设置隐藏 “在线调试” 按钮和隐藏 “Powered by Apifox”。

### 分享整个目录

快捷分享支持 “分享整个目录” 功能。这适用于分享链接后，你可能在目录中增删了文档，希望协作者能同步看到这些变化的场景。

在 “分享接口范围” 中，选择 “手动圈选接口” 时，可以看到 “整目录分享” 选项。启用后，协作者将自动获得访问该目录下所有文档的权限，这样你就不需要在每次添加新文档时调整分享设置。
<Background>
<img style="width: 460px"  src="https://api.apifox.com/api/v1/projects/5097254/resources/482866/image-preview" />
</Background>

### 跨域代理

在线分享给外部用户的文档，如果用户想要在文档页中调试接口，则很有可能碰到浏览器的[跨域请求（CORS）](https://baike.baidu.com/item/%E8%B7%A8%E6%9D%A5%E6%BA%90%E8%B5%84%E6%BA%90%E5%85%B1%E4%BA%AB?fromModule=lemma_search-box)问题。通过给该 “在线分享” 内容设置跨域代理即可帮助解决这个问题。用户从此分享页中发起的全部接口请求，都将会通过指定的请求代理 Agent，来代理发起请求。


在线分享的下方有跨域代理的设置入口，点击即可进行设置。所有在线分享默认会使用 Apifox 提供的 “云端 Agent” 来代理接口请求。


<Background>
<img src="https://api.apifox.com/api/v1/projects/5097254/resources/490617/image-preview" alt="跨域代理" style="width: 460px;" />

</Background>



可以在跨域代理详情中，根据你的实际场景和使用需求，来设置使用具体某个跨域代理：

- **云端 Agent：** 使用 Apifox 提供的云端请求代理 Agent 来代理从此分享页中发起的接口请求。需要注意这个 Agent 无法访问内网接口。
  
- **浏览器扩展：** 使用用户在自己浏览器中安装的浏览器扩展作为 Agent 来发起请求。如果用户没有安装浏览器扩展则会在页面引导其安装扩展来发起请求。
  
- **不使用代理：** 不使用跨域代理，请求将从用户浏览器直接发起到接口。需要注意接口服务端的配置以避免跨域问题。
  
- **自托管请求代理 Agent：** 使用某个团队中部署的[请求代理 Agent](https://docs.apifox.com/request-proxy-agent.md) 来代理从此分享页中发起的接口请求。


<Background>
<img src="https://api.apifox.com/api/v1/projects/5097254/resources/490618/image-preview" alt="跨域代理" style="width: 460px;" />
</Background>



### 示例代码

创建分享时可以选择是否显示这个模块。

你可以自定义示例代码，具体步骤如下：

1. 在 **“项目设置** - **功能设置** - **接口功能设置** - **接口字段”** 中，开启示例代码字段。
2. 然后在 **“接口** - **修改接口”** 中，最后会出现示例代码模块。
3. 你可以在这里点击 **添加示例代码**，添加需要的语言示例。之后它会显示在文档中。

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/482867/image-preview)
</Background>

## 分享链接

完成设置后，复制链接分享给团队成员。即可[查看 API 文档](https://docs.apifox.com/view-api-documentation.md)。

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/482868/image-preview)
</Background>

