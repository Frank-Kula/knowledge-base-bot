# Connect Published Documentation to AI

Apidog MCP Server enables AI to connect and utilize online API documentation published by Apidog, allowing external developers and AI assistants to access public API documentation seamlessly.

:::info[]
This configuration method only supports publicly published online documentation. It does not support documentation with [password or allowlist settings](https://docs.apidog.com/publishing-documentation-sites-631325m0.md#docs-site-visibility-setting).

For non-public documentation, use the [Apidog Project data source](https://docs.apidog.com/connect-apidog-project-to-ai-901476m0.md) instead.
:::

## Enabling MCP for Online Documentation

:::tip[]
Apidog version 2.7.2 or later is required.
:::

<Steps>
  <Step title="Enable MCP Service">
1. Navigate to your Apidog project
2. Go to **Publish Docs** → **Publish Docs Sites** → **LLM-friendly Features**
3. Enable the MCP service
      
<Background>
![Enabling MCP service for online documentation](https://api.apidog.com/api/v1/projects/544525/resources/368855/image-preview)
</Background>

  </Step>
  <Step title="Get Configuration File">
After enabling MCP, the **MCP** button will appear when accessing your online documentation.
      
<Background>
![MCP button on online documentation](https://api.apidog.com/api/v1/projects/544525/resources/368856/image-preview)
</Background>

Click the button to display the configuration guide and MCP config file, which automatically includes your documentation's `site-id`. Copy this configuration for IDE integration.
      
<Background>
![MCP configuration with site-id](https://api.apidog.com/api/v1/projects/544525/resources/368857/image-preview)
</Background>
  </Step>
</Steps>

## Configuring MCP Client

### Prerequisites

Before configuring the MCP client, ensure you have:

- **Node.js** (version 18 or later, preferably the latest LTS version)
- An **MCP-compatible IDE**:
  - Cursor
  - VS Code + Cline plugin
  - Other MCP-supported editors
- **Copied MCP JSON configuration** from Apidog online documentation

### Configuring MCP in Cursor

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
Paste the MCP JSON configuration copied from online documentation into the opened `mcp.json` file:
      
<Tabs>
  <Tab title="macOS / Linux">
    ```json
    {
      "mcpServers": {
        "apidog-site-123456": {
          "command": "npx",
          "args": [
            "-y",
            "apidog-mcp-server@latest",
            "--site-id=123456"
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
        "apidog-site-123456": {
          "command": "cmd",
          "args": [
            "/c",
            "npx",
            "-y",
            "apidog-mcp-server@latest",
            "--site-id=123456"
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
Please fetch API documentation via MCP and tell me how many endpoints exist in the project.
```
      
If the AI returns correct API information, the connection is successful.
      
<Background>
![Successful connection verification](https://api.apidog.com/api/v1/projects/544525/resources/352763/image-preview)
</Background>
  </Step>
</Steps>

## Important Notes

### Working with Multiple Documentation Sites

To work with different API documentation sites, add multiple MCP Server configurations to the configuration file. Each documentation site should have its own unique `<site-id>`.

### On-Premise Deployment

For on-premise deployments, include your server's API address in the IDE MCP configuration:

```json
{
  "mcpServers": {
    "apidog-site-123456": {
      "command": "npx",
      "args": [
        "-y",
        "apidog-mcp-server@latest",
        "--site-id=123456",
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

<Card title="Connect OpenAPI Files to AI" href="https://docs.apidog.com/connect-openapi-files-to-ai-901477m0.md">
</Card>

## FAQs

<Accordion title="Windows Configuration Issues" defaultOpen>

If standard configuration fails on Windows, use this alternative:

```json
{
  "mcpServers": {
    "apidog-site-123456": {
      "command": "cmd",
      "args": [
        "/c",
        "npx",
        "-y",
        "apidog-mcp-server@latest",
        "--site-id=123456"
      ]
    }
  }
}
```
</Accordion>

<Accordion title="Node.js Version Problems" defaultOpen={false}>

If you encounter Node.js version errors, ensure you have Node.js v18 or higher. Check your version with:

```bash
node -v
```
</Accordion>

<Accordion title="How to let AI read the latest data from updated API documentation?" defaultOpen={false}>

AI caches API documentation locally. If documentation is updated, tell the AI to refresh the data to ensure it uses the latest version when generating code.

For example:

```
Please reload API documentation and add the new fields in Pet DTO
```
</Accordion>

