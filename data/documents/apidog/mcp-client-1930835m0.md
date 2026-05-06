# MCP Client

## Overview

MCP (Model Context Protocol) is an open protocol for establishing standardized communication between large language model (LLM) applications and external data sources and tools. Apidog has a built-in MCP Client that supports debugging and testing MCP Servers.

MCP Servers provide three main features, all of which are supported for debugging by the Apidog MCP Client:

- **Tools**: Executable server-side functions
- **Prompts**: Predefined prompt templates
- **Resources**: Data resources provided by the server

Two transport methods are supported:

- **STDIO**: Communication via standard input/output, suitable for local processes
- **HTTP**: Communication via Streamable HTTP, suitable for remote servers


:::tip

  Please use the web version or download the latest version of the desktop application from the homepage.

 :::
---

## Create MCP Client

Create a new endpoint in an HTTP project and select **MCP**.

<Background>
  ![Create MCP Client](https://api.apidog.com/api/v1/projects/544525/resources/370567/image-preview)
</Background>


---

## Connect to MCP Server

### Enter Server Address

Apidog supports multiple ways to input MCP Server connection information:

**Direct Command or URL Input**

When pasting a terminal command, the protocol automatically switches to STDIO:
```bash
npx -y @modelcontextprotocol/server-everything
```

When pasting a URL, the protocol automatically switches to HTTP:
```
https://example-server.modelcontextprotocol.io/mcp
```

**Paste Configuration File**

Apidog supports pasting MCP Server configuration files directly and will automatically parse and populate the relevant information.

MCP Servers File Example:

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

MCP Server Entry Example:
```json
{
  "type": "streamable-http",
  "url": "https://example-server.modelcontextprotocol.io/mcp"
}
```

After pasting the configuration file, Apidog will automatically extract the server name, address, environment variables, and other information. If the configuration file contains multiple servers, the first one will be used.

### Establish Connection

Click the **Connect** button to initiate the connection.

**STDIO Connection**

Since local command execution is required, Apidog will display a security confirmation dialog. After confirmation, it will start the local process and establish the connection.

**HTTP Connection**

Send a connection request directly to the specified URL.

- For MCP Servers with OAuth 2.0 authentication, Apidog will automatically retrieve authentication configuration and display the authentication window
- Other authentication methods (API Key, Bearer Token, Basic Auth, etc.) can also be manually configured in the Auth tab

After a successful connection, the directory tree will display the list of Tools, Prompts, and Resources provided by the server.

---

## Debugging Features

### Tools

Tools are executable functions provided by the server. After selecting a Tool, you can configure parameters via form or JSON editor.

After configuring the parameters, click **Run** to execute. Results will be displayed in the response area.

<Background>
  ![](https://api.apidog.com/api/v1/projects/544525/resources/372745/image-preview)
</Background>


### Prompts

Prompts are predefined prompt templates. After selecting a Prompt, configure parameters (if any) and click **Run** to get the generated prompt.

<Background>
  ![](https://api.apidog.com/api/v1/projects/544525/resources/372746/image-preview)
</Background>


### Resources

Resources are data resources provided by the server. After selecting a Resource, click **Run** to retrieve the resource content.

<Background>
  ![](https://api.apidog.com/api/v1/projects/544525/resources/372747/image-preview)
</Background>


---

## Configuration Options

### Environment

Available only for STDIO mode. Used to configure environment variables when starting the MCP Server process.

Example:

| Key | Value |
|-----|-------|
| ACCESS_TOKEN | your-token-here |
| NODE_ENV | production |

### Auth

Available only for HTTP mode. Supports multiple authentication methods:

- API Key
- Bearer Token
- JWT Bearer
- Basic Auth
- Digest Auth
- OAuth 2.0

For MCP Servers that support OAuth 2.0, Apidog can automatically retrieve and populate authentication configuration.

<Background>
  ![](https://api.apidog.com/api/v1/projects/544525/resources/370606/image-preview)
</Background>


### Headers

Available only for HTTP mode. Used to configure custom HTTP request headers.

---

## View Response

After clicking **Run**, the tool execution results will be displayed in the **Response** panel. Apidog categorizes the interaction into two types: **Messages** and **Notifications**.

### Messages
A **Message** represents a standard request-response interaction (e.g., executing a tool and receiving a result).

For each message, Apidog provides three view modes to help you visualize the data. You can toggle between them using the tabs at the top of the response area:

*   **Content:** The default view. Displays the clean text output. Apidog parses the JSON-RPC message and extracts only the core content returned by the tool (e.g., the `text` field), stripping away protocol details for easier reading.

<Background>
  ![](https://api.apidog.com/api/v1/projects/544525/resources/372739/image-preview)
</Background>

*   **Preview:** Renders rich content returned by the tool. If the response contains **Markdown**, **images**, or other multimedia resources, this tab automatically renders them into a visual format (e.g., formatted text, charts, or decoded Base64 images). This eliminates the need for manual decoding or raw text parsing.

<Background>
  ![](https://api.apidog.com/api/v1/projects/544525/resources/372740/image-preview)
</Background>

*   **Raw:** Displays the complete JSON-RPC interaction message, including all protocol details (such as `jsonrpc`, `id`, and `result` structure). Use this mode when debugging MCP servers to verify protocol compliance.

<Background>
  ![](https://api.apidog.com/api/v1/projects/544525/resources/372741/image-preview)
</Background>

### Notifications
A **Notification** represents a one-way message from the MCP server (e.g., logging, progress updates, or resource changes) that does not require a response.

*   Notifications are listed separately in the response timeline.
*   They typically display log levels (e.g., `info`, `debug`, `error`) and the accompanying message text.

---

## Variable Support

Variables `{{variable_name}}` are supported in the following locations:

- Server address or command
- Environment variable values
- Request headers
- Authentication information
- Parameter values

---

## Save and Share

Configured MCP clients can be saved to the project for subsequent use and team collaboration.

> **Note**: The MCP directory tree (Tools, Prompts, Resources list) is stored locally only and refreshes automatically on each connection.

---

## FAQ

### STDIO connection fails with "command not found" error

Ensure the required runtime (such as Node.js) is installed and check that the command path is correct.

### HTTP connection returns 401 error

Apidog will automatically attempt to retrieve OAuth 2.0 configuration. If it fails, manually configure authentication information in the Auth tab.

### Connection successful but directory tree is empty

Check that the server configuration is correct and view the Notifications tab to confirm whether the server has returned the tool list.

### Parameter type mismatch

When using form mode, Apidog will automatically validate parameter types. In JSON editor mode, be careful not to add quotes around numbers and use `true`/`false` for boolean values.

