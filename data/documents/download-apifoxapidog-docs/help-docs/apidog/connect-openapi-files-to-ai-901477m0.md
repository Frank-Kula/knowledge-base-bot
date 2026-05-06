# Connect OpenAPI Files to AI

Apidog MCP Server can directly read Swagger or OpenAPI Specification (OAS) files, enabling AI assistants to work with API specifications independently of Apidog projects or online documentation.

## Prerequisites

Before configuring the MCP client, ensure you have:

- **Node.js** (version 18 or later, preferably the latest LTS version)
- An **MCP-compatible IDE**:
  - Cursor
  - VS Code + Cline plugin
  - Other MCP-supported editors
- A **Swagger/OpenAPI file** (URL or local path)

## Preparing Your OpenAPI File

Ensure you have one of the following:

- **Remote URL**: A publicly accessible OpenAPI file (e.g., `https://petstore.swagger.io/v2/swagger.json`)
- **Local file path**: An OpenAPI file on your machine (e.g., `~/data/petstore/swagger.json`)

**Supported formats:** JSON or YAML

## Configuration Overview

The basic MCP configuration for OpenAPI files:

<Tabs>
  <Tab title="macOS / Linux">
    ```json
    {
      "mcpServers": {
        "API specification": {
          "command": "npx",
          "args": [
            "-y",
            "apidog-mcp-server@latest",
            "--oas=<oas-url-or-path>"
          ]
        }
      }
    }
    ```
  </Tab>
  <Tab title="Windows">
    ```json
    {
      "mcpServers": {
        "API specification": {
          "command": "cmd",
          "args": [
            "/c",
            "npx",
            "-y",
            "apidog-mcp-server@latest",
            "--oas=<oas-url-or-path>"
          ]
        }
      }
    }
    ```
  </Tab>
</Tabs>

Replace `<oas-url-or-path>` with:
- A remote URL (e.g., `https://petstore.swagger.io/v2/swagger.json`)
- A local file path (e.g., `~/data/petstore/swagger.json`)

## Configuring MCP in Cursor

<Steps>
  <Step title="Open MCP Settings">
1. Open Cursor editor
2. Click the settings icon (top-right)
3. Select **MCP** from the left menu
4. Click **+ Add new global MCP server**
      
<Background>
![MCP server settings in Cursor](https://api.apidog.com/api/v1/projects/544525/resources/352759/image-preview)
</Background>
  </Step>
    
  <Step title="Add Configuration"> 
In the opened `mcp.json` file, add the following configuration. Replace `https://petstore.swagger.io/v2/swagger.json` with your actual OpenAPI file path or URL:
      
     <Tabs>
      <Tab title="macOS / Linux">
        ```json
        {
          "mcpServers": {
            "API specification": {
              "command": "npx",
              "args": [
                "-y",
                "apidog-mcp-server@latest",
                "--oas=https://petstore.swagger.io/v2/swagger.json"
              ]
            }
          }
        }
        ```
      </Tab>
      <Tab title="Windows">
        ```json
        {
          "mcpServers": {
            "API specification": {
              "command": "cmd",
              "args": [
                "/c",
                "npx",
                "-y",
                "apidog-mcp-server@latest",
                "--oas=https://petstore.swagger.io/v2/swagger.json"
              ]
            }
          }
        }
        ```
      </Tab>
    </Tabs>  
      
  </Step>
  <Step title="Verify Configuration">
Test the connection by asking the AI (in Agent mode):

```plain
Please fetch API documentation via MCP and tell me how many endpoints exist in the project
```

If the AI returns correct API information from your OpenAPI file, the connection is successful.      
      
<Background>
![Successful connection verification](https://api.apidog.com/api/v1/projects/544525/resources/352793/image-preview)
</Background>

  </Step>
</Steps>

## Important Notes

### Working with Multiple OpenAPI Files

To use multiple OpenAPI specification files, add multiple MCP Servers in the configuration file, each with a different `--oas` parameter.

Example:

```json
{
  "mcpServers": {
    "Petstore API": {
      "command": "npx",
      "args": [
        "-y",
        "apidog-mcp-server@latest",
        "--oas=https://petstore.swagger.io/v2/swagger.json"
      ]
    },
    "Local API": {
      "command": "npx",
      "args": [
        "-y",
        "apidog-mcp-server@latest",
        "--oas=~/data/my-api/openapi.yaml"
      ]
    }
  }
}
```

### File Path and URL Requirements

- **Local file paths**: Ensure the path is correct and the file exists
- **URLs**: Ensure they are publicly accessible and return a valid OpenAPI specification file

### Performance Considerations

If your OpenAPI file is large or contains complex data structures, the MCP server may take longer to process it.

### On-Premise Deployment

For on-premise deployments, include your server's API address in the IDE MCP configuration:

```json
{
  "mcpServers": {
    "API specification": {
      "command": "npx",
      "args": [
        "-y",
        "apidog-mcp-server@latest",
        "--oas=<oas-url-or-path>",
        "--apidog-api-base-url=<your-server-url>"
      ]
    }
  }
}
```

Replace `<your-server-url>` with your on-premise server's API address (starting with `http://` or `https://`). Ensure network access to `www.npmjs.com`.

## Other Data Sources

<Card title="Connect API Specification within Apidog Project to AI" href="https://docs.apidog.com/connect-apidog-project-to-ai-901476m0.md">
</Card>
    
<Card title="Connect Online API Documentation Published by Apidog to AI" href="https://docs.apidog.com/connect-published-documentation-to-ai-901468m0.md">
</Card>
    
## FAQs

<Accordion title="Windows Configuration Issues" defaultOpen>

If standard configuration fails on Windows, use this alternative:

```json
{
  "mcpServers": {
    "API specification": {
      "command": "cmd",
      "args": [
        "/c",
        "npx",
        "-y",
        "apidog-mcp-server@latest",
        "--oas=<oas-url-or-path>"
      ]
    }
  }
}
```
</Accordion>

<Accordion title="Node.js Version Problems" defaultOpen={false}>

If you encounter Node.js version errors, ensure you're using v18 or higher. Check your version with:

```bash
node -v
```
</Accordion>

