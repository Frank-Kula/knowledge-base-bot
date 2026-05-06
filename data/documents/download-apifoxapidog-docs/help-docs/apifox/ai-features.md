# AI 相关特性

> Apifox 版本要求 ≥ 2.7.2

在项目的 “分享文档 -> 发布文档站 -> AI 相关特性” 中即可进行相关操作。

<Background>

![CleanShot 2025-04-17 at 10.35.15@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/514268/image-preview)
</Background>


## 开启 MCP

如果开启，在线文档中将显示 “MCP” 按钮，指导用户如何在支持 MCP 的 IDE（如 Cursor、Cline 等）中使用当前 API 文档来帮助 AI 代理编写代码。详情请看[通过 MCP 使用公开发布的 API 文档](https://docs.apifox.com/6327890m0.md)。

![f08ea56d-7779-414d-b8b9-c8aedc219e82.gif](https://api.apifox.com/api/v1/projects/5097254/resources/507182/image-preview)

## 开启“复制页面”

如果开启，在线文档中将显示“复制页面”按钮。你可以复制网页为 Markdown 格式，以供 AI 大模型使用。

<Background>
![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/516329/image-preview)
</Background>



## 开启 LLMs.txt

如果开启，网站的根目录会出现一个名为 `llms.txt` 的 Markdown 文件，包含网站内每个 Markdown 页面的链接，以及一些简明扼要的信息。例如：

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/513178/image-preview)
</Background>

### 如何让 AI 助手使用 LLMs.txt？

如何使用 LLMs.txt 及相关的 Markdown 文件？这里提供 2 种最常见的方法：

**1. 分享 Markdown 链接给可以访问 URL 的 AI 助手**

浏览使用 Apifox 发布的在线文档时，直接给页面的 URL 添加 `.md` 后缀，或者点击“以 Markdown 格式查看”，就可以得到对应页面的 Markdown 版本。

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/514283/image-preview)
</Background>

对于能访问网络 URL，即具备 Web Browsing 能力的 AI 助手，可以直接将在线文档的 `.md` URL 提供过去，以便 AI 获取简洁、精炼的文档内容。

例如在腾讯元宝中，你可以这样提问：“请查看`https://wn50ds108y.apifox.cn/api-205194698.md`获取宠物商店 API 的详细信息”。

<Background>
<img src="https://api.apifox.com/api/v1/projects/5097254/resources/514285/image-preview" style="width: 460px" />
</Background>


在 Cursor 中，你可以这样提问：“理解这里的信息：`@https://wn50ds108y.apifox.cn/api-205194698.md`，帮我生成一个 TypeScript 客户端代码”。

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/514287/image-preview)
</Background>

:::tip[]
具体的格式，需要遵循所使用 AI 工具的规定。在 Cursor 中，URL 需以 `@` 开头标记为 Context，才能被正确识别并正常工作。
:::


**2. 复制 Markdown 内容给无法访问 URL 的 AI 助手**

如果 AI 助手无法通过识别 URL 访问 Markdown 内容，就需要手动复制内容给它：

<Background>
![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/516337/image-preview)
</Background>



此时，可以点击在线文档页面上的「复制页面」按钮，获取当前页面的 Markdown 内容，粘贴到与 AI 助手的对话内。

例如你可以这样问：“基于这个 API 定义，帮我生成一个 TypeScript 客户端代码：”，然后粘贴复制到的内容。

<Background>
![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/516339/image-preview)
</Background>

### 常见问题

<Accordion title="开启 LLMs.txt 会对文档安全性产生影响吗？" defaultOpen>
不会。LLMs.txt 仅包含已经公开发布的文档内容，只是将 HTML 格式转换为 Markdown 格式呈现，不会暴露未公开的文档信息。如果在线文档配置了密码、IP 白名单、邮箱白名单等，访问 LLMs.txt 和 Markdown 文件时也需要先完成鉴权。
</Accordion>

<Accordion title="如果我的在线文档设置了密码、IP 白名单、邮箱白名单等，能否使用 LLMs.txt 功能？" defaultOpen={false}>
可以使用。但由于访问 LLMs.txt 和 Markdown 文件时也需要先完成鉴权，因此 AI 助手可能无法通过 URL 直接读取 `.md` 文件，需要通过“复制页面”功能将内容复制出来后，粘贴给 AI。
</Accordion>

<Accordion title="为什么我没有在 Apifox App 内看到“复制页面”等按钮？" defaultOpen={false}>
这是分享/发布的在线文档的功能，请发布在线文档后，使用浏览器查看在线文档。
</Accordion>

<Accordion title="我已经开启了 AI 助手的“联网搜索”功能，为什么 AI 无法通过 URL 读取网页内容？" defaultOpen={false}>
“联网搜索”与“Web Browsing”是不同的功能。“联网搜索”是指 AI 可以调用搜索引擎，将用户发送的内容进行搜索，然后对搜索引擎的返回的内容进行总结。而“Web Browsing”是指 AI 可以直接访问指定的 URL，并读取其中的内容。
</Accordion>

<Accordion title="AI 通过 URL 访问 Markdown 文件失败怎么办？" defaultOpen={false}>
如果 AI 无法访问 URL，可以点击在线文档的“复制页面”按钮，复制`.md`文件里的内容给 AI。
</Accordion>

<Accordion title="启用 LLMs.txt 后，我需要做什么额外工作吗？" defaultOpen={false}>
不需要。一旦功能开启，系统会自动为你的文档生成 LLMs.txt 和各页面的 Markdown 文件，你只需专注于维护好原始文档即可。
</Accordion>

<Accordion title="如何验证 LLMs.txt 是否正常工作？" defaultOpen={false}>
访问你的文档站点根目录下的 `/llms.txt` 路径，若能看到结构化的站点索引，则表明功能已正常启用。
</Accordion>
