# MCP 调试


:::tip[]
- Apifox 版本需 `≥2.8.3`
- 如果你要在 AI 编程工具里使用 MCP 获取 Apifox 项目内的接口数据，可以移步 [Apifox MCP Server](https://docs.apifox.com/apifox-mcp-server) 文档
:::

## 概览

MCP（Model Context Protocol）是一个开放协议，用于在大语言模型（LLM）应用与外部数据源和工具之间建立标准化通信。你可以在 Apifox 中创建 MCP 客户端，以调试和测试 MCP 服务端。

MCP 服务端提供三大核心功能，Apifox MCP 客户端均支持对其进行调试：

- **Tools**：可在服务端执行的函数
- **Resources**：服务端提供的数据资源
- **Prompts**：预定义的提示词模板

支持两种传输方式：

- **STDIO**：通过标准输入/输出进行通信，适用于本地进程
- **HTTP**：通过可流式传输的 HTTP（Streamable HTTP）进行通信，适用于远程服务端

:::tip[]
请使用 Web 版或从官网首页下载最新版本的桌面版。
:::


## 新建 MCP 客户端

在 HTTP 项目中新建一个接口，并选择 **MCP**。

<Background>
  ![新建 MCP 客户端](https://api.apifox.com/api/v1/projects/5097254/resources/618459/image-preview)
</Background>




## 连接 MCP 服务端

### 输入服务端地址

Apifox 支持多种方式输入 MCP 服务端连接信息：

**直接输入命令或 URL**

粘贴终端命令时，协议会自动切换为 STDIO：
```bash
npx -y @modelcontextprotocol/server-everything
```

粘贴 URL 时，协议会自动切换为 HTTP：
```
https://example-server.modelcontextprotocol.io/mcp
```

**粘贴配置文件**

Apifox 支持直接粘贴 MCP 服务端配置文件，并会自动解析并填充相关信息。

MCP Servers 文件示例：

```json
{
  "mcpServers": {
    "Everything Server": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-everything"],
      "env": {}
    }
  }
}
```

MCP Server 条目示例：
```json
{
  "type": "streamable-http",
  "url": "https://example-server.modelcontextprotocol.io/mcp"
}
```

粘贴配置文件后，Apifox 会自动提取服务端名称、地址、环境变量等信息。如果配置文件包含多个服务端，将使用第一个。

### 建立连接

点击**连接**按钮发起连接。

**STDIO 连接**

由于需要执行本地命令，Apifox 会显示安全确认对话框。确认后，将启动本地进程并建立连接。

**HTTP 连接**

直接向指定的 URL 发送连接请求。

- 对于支持 OAuth 2.0 鉴权的 MCP 服务端，Apifox 会自动获取鉴权配置并显示鉴权窗口
- 其他鉴权方式（API Key、Bearer Token、Basic Auth 等）也可以在 Auth 标签页中手动配置

连接成功后，目录树将显示该服务端提供的 Tools、Resources 和 Prompts 列表。


## 调试功能

### Tools

Tools 是服务端提供的可执行函数。选择某个 Tool 后，你可以通过表单或 JSON 编辑器配置参数。

配置参数后，点击**运行**即可执行。结果将显示在响应区域。

<Background>

![CleanShot 2026-01-27 at 15.24.42@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/618533/image-preview)
</Background>

### Resources

Resources 是服务端提供的数据资源。选择某个 Resource 后，点击**运行**即可获取资源内容。

<Background>

![CleanShot 2026-01-27 at 15.25.12@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/618534/image-preview)
</Background>

### Prompts

Prompts 是预定义的提示词模板。选择某个 Prompt 后，配置参数（如有）并点击**运行**即可获取生成的提示词。

<Background>
 
![CleanShot 2026-01-27 at 15.26.24@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/618535/image-preview)
</Background>



## 配置选项

### 环境

仅适用于 STDIO 模式。用于配置启动 MCP 服务端进程时的环境变量。

示例：

| Key | Value |
|-----|-------|
| ACCESS_TOKEN | your-token-here |
| NODE_ENV | production |

### Auth

仅适用于 HTTP 模式。支持多种鉴权方式：

- API Key
- Bearer Token
- JWT Bearer
- Basic Auth
- Digest Auth
- OAuth 2.0

对于支持 OAuth 2.0 的 MCP 服务端，Apifox 可以自动获取并填充鉴权配置。

<Background>

![CleanShot 2026-01-27 at 15.29.08@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/618537/image-preview)
</Background>


### Headers

仅适用于 HTTP 模式。用于配置自定义 HTTP 请求 header。



## 查看响应

响应区域分为两个标签页：

- **Messages**：显示与用户操作相关的消息（连接/断开事件、请求/响应）

- **Notifications**：显示服务端主动发送的消息（通知、工具列表更新等）

点击单条消息可查看详情，包括消息类型、内容、时间戳等。

你可以切换到 "包含信封" 模式来查看完整的 JSON-RPC 格式。

<Background>

![CleanShot 2026-01-27 at 15.32.43@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/618542/image-preview)
</Background>




## 变量支持

在以下位置支持使用变量 `{{variable_name}}`：

- 服务端地址或命令
- 环境变量值
- 请求 header
- 鉴权信息
- 参数值


## 保存与共享

配置好的 MCP 客户端可以保存到项目中，以便后续使用和团队协作。

> **注意**：MCP 目录树（Tools、Prompts、Resources 列表）仅存储在本地，并在每次连接时自动刷新。



## 常见问题

### STDIO 连接失败，提示 "command not found" 错误？

请确保已安装所需的运行时（如 Node.js），并检查命令路径是否正确。

### HTTP 连接返回 401 错误？

Apifox 会自动尝试获取 OAuth 2.0 配置。如果失败，请在 Auth 标签页中手动配置鉴权信息。

### 连接成功但目录树为空？

请检查服务端配置是否正确，并查看 Notifications 标签页以确认服务端是否返回了工具列表。

### 参数类型不匹配？

使用表单模式时，Apifox 会自动校验参数类型。在 JSON 编辑器模式下，请注意不要给数字添加引号，布尔值请使用 `true`/`false`。
