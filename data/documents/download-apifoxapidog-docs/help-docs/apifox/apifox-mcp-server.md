# Apifox MCP Server

![NPM Version](https://img.shields.io/npm/v/apifox-mcp-server)

Apifox MCP Server，可以将 Apifox 的接口文档提供给 Cursor 等支持 AI 编程的 IDE，或其他支持 MCP 的 AI 工具。

有了 Apifox MCP Server，开发者就可以通过 AI 助手完成以下工作：根据接口文档生成或修改代码、搜索接口文档内容等等，至于通过这个接口文档数据能让 AI 干什么更多更强大的活，请发挥你和你们团队的想象力。

<Video src="https://cdn.apifox.cn/uploads/help/202503191817472.mp4"></Video>

:::tip[]
Apifox MCP Server 正在内测阶段，本帮助文档的内容会动态更新，请关注。
:::

## 🎯 如何使用

完成配置后，Apifox MCP Server 会自动获取接口文档的数据并缓存在本地，AI 助手可以通过 MCP 读取接口文档数据。

你只要告诉 AI 你想要通过 API 文档做什么即可，示例：

- "通过 MCP 获取 API 文档，然后生成 Product 及其相关模型的定义代码"
- "根据 API 文档，在 Product DTO 里添加 API 文档新增的几个字段"
- "根据 API 文档给 Product 类的每个字段都加上注释"
- "根据 API 文档，生成接口 /users 相关的所有 MVC 代码"

注意：接口文档数据默认缓存在本地，如果 Apifox 内的数据有更新，请告诉 AI 刷新接口文档数据，否则 AI 读到的数据可能不是最新的。

## 🚀 如何配置

### 前置条件

- 已安装 Node.js 环境（版本号 >= 18，推荐最新的 LTS 版本）
- 任意一个支持 MCP 的 IDE：
  - Cursor
  - VS Code + Cline 插件


### 根据不同场景，选择配置方法

Apifox MCP Server 支持以下三种不同的使用场景，可以根据不同场景选择对应的配置方法：


<AccordionGroup>
  <Accordion title="通过 MCP 使用 Apifox 项目内的 API 文档" defaultOpen>
**适用场景**
- 使用 AI 读取自己团队的 API 文档

**特点**
- 需要 Apifox 个人访问令牌
      

具体配置方法，请查看：[通过 MCP 使用 Apifox 项目内的 API 文档](https://docs.apifox.com/6327888m0)
  </Accordion>
  <Accordion title="通过 MCP 使用公开发布的 API 文档">
**适用场景**

- 使用 AI 读取别人公开发布的 API 文档
- 让自己团队外的开发者，即 API 的调用方，通过 AI 读取自己团队公开发布的 API 文档

**特点**
- 无需 Apifox 个人访问令牌
- 仅支持公开发布、任何人都可以直接访问的在线文档，不支持设置了密码、邮箱白名单、IP 白名单的在线文档
- 如果不希望公开接口文档，仅仅是内部人员可以访问，建议使用项目 ID 和个人访问令牌读取 Apifox 项目数据
 

具体配置方法，请查看：[通过 MCP 使用公开发布的 API 文档](https://docs.apifox.com/6327890m0)。
  </Accordion>
      
  <Accordion title="通过 MCP 使用 OpenAPI/Swagger 文档">
**适用场景**
- 使用 AI 读取本地或线上的 Swagger/OpenAPI 文件
      
**特点**
- 不依赖 Apifox 项目或在线文档
- 无需 Apifox 个人访问令牌

具体配置方法，请查看：[通过 MCP 使用 OpenAPI/Swagger 文档](https://docs.apifox.com/6327891m0)
  </Accordion>
</AccordionGroup>


## 🏢 私有化部署配置

对于使用 Apifox 私有化部署版本的用户，无论你选择上述哪种配置方式，都需要添加在配置文件中私有化部署服务器的 API 地址："--apifox-api-base-url=`<私有化部署服务器的 API 地址，以 http:// 或 https:// 开头>`"

:::tip[]
**注意**：请确保网络可以正常访问 `www.npmjs.com`。
:::

## ❓帮助与支持
    
Apifox MCP Server 还在内测阶段，欢迎各位给我们提建议和想法，请加内测群：

<img src="https://api.apifox.com/api/v1/projects/5097254/resources/534409/image-preview" style="width:300px;"></img>


