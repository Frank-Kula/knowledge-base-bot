# Connect Online API Documentation Published by Apidog to AI via Apidog MCP Server

Apidog MCP Server enables AI to connect and utilize online API documentation published by Apidog.

![Apidog MCP Server](https://assets.apidog.com/uploads/help/2025/03/26/1562f2ed8710ec754897595552c1b84c.gif)

This configuration method only supports publicly published online documentation and does not support documentation with [password or whitelist settings](https://docs.apidog.com/publish-docs-sites-631325m0#docs-site-visibility-setting). For non-public documentations, it is recommended to use the project ID and personal API access token to read Apidog project data. For more details, refer to: [Connecting API Documentation within Apidog Project to AI via Apidog](https://docs.apidog.com/connect-api-specification-within-apidog-project-to-ai-via-apidog-mcp-server-901476m0.md).

## Enabling MCP for Online Documentation

>  Apidog version should be 2.7.2 or later.

<Steps>
  <Step title="Enable MCP Service">
Navigate to Apidog project, then go to `Share Docs` → `Publish Docs Sites` → `AI Features` to enable MCP service.
      
<Background>
![enabling-mcp-service.png](https://api.apidog.com/api/v1/projects/544525/resources/352755/image-preview)
</Background>

  </Step>
  <Step title="Get Configuration File">
After enabling, the `Vibe Coding(via MCP)` button will appear when accessing online documentation.
      
<Background>
![vibe-coding-via-mcp-button-api-documentation.png](https://api.apidog.com/api/v1/projects/544525/resources/352756/image-preview)
</Background>

Clicking the button will display the configuration guide and the MCP config file, which automatically includes your documentation's `site-id`. Simply copy this configuration for IDE integration.
      
<Background>
![vibe-coding-mcp-configuration-guide.png](https://api.apidog.com/api/v1/projects/544525/resources/352757/image-preview)
</Background>
  </Step>
</Steps>


## Configuring MCP Client

### Prerequisites

- Node.js environment installed (version 18 or later, latest LTS recommended)
- Any IDE that supports MCP:
  - Cursor
  - VSCode + Cline extension
  - Others
- Copied MCP JSON configuration from Apidog online documentations


### Configuring MCP in Cursor

<Steps>
  <Step title="Edit MCP Config File">
Open Cursor editor, click the settings icon (top-right), select "MCP" from the left menu, then click "+ Add new global MCP server".
      
<Background>
![mcp-server-setting-cursor.png](https://api.apidog.com/api/v1/projects/544525/resources/352759/image-preview)
</Background>

  </Step>
  <Step title="Add Configuration">
Paste the MCP JSON configuration copied from online documentations into the opened `mcp.json` file:
      
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
Test the connection by asking the AI (in Agent mode), for example:

```plain
Please fetch API documentation via MCP and tell me how many endpoints exist in the project.
```
      
If the AI returns correct API information, the connection is successful.
      
<Background>
![apidog-mcp-server-in-cursor.png](https://api.apidog.com/api/v1/projects/544525/resources/352763/image-preview)
</Background>
  </Step>
</Steps>


 
## Important Notes

- If you need to work with different API documentations, simply add multiple MCP Server configurations to the configuration file. Each API documentation should have its own unique `<site-id>`.
- For users of the on-premise deployment, please include your on-premise server's API address in the IDE MCP configuration: "--apidog-api-base-url=`<API address of the on-premise server, starting with http:// or https://>`" Additionally, ensure network access to `www.npmjs.com` properly.
      
    ```json
     {
      "mcpServers": {
        "apidog-site-123456": {
          "command": "npx",
          "args": [
            "-y",
            "apidog-mcp-server@latest",
            "--site-id=123456",
            // Required for on-premise deployment:
            "--apidog-api-base-url=<API address of the on-premise server>"
          ]
        }
      }
    }
    ```

## Connecting Other Data Resources to AI

<Card title="Conntect API Specification within Apidog Project to AI via Apidog MCP Server" href="https://docs.apidog.com/connect-api-specification-within-apidog-project-to-ai-via-apidog-mcp-server-901476m0.md"> 
</Card>

<Card title="Conntect OpenAPI Files to AI via Apidog MCP Server
" href="https://docs.apidog.com/connect-openapi-files-to-ai-via-apidog-mcp-server-901477m0.md">
</Card>

## FAQs


<Accordion title="Windows Configuration Issues" defaultOpen>

If standard configuration fails on Windows, use this instead:

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
        "--site-id=123456"  // Replace with your Site ID
      ]
    }
  }
}
```
</Accordion>

<Accordion title="Node.js Version Problems" defaultOpen={false}>

If receiving Node.js version errors, ensure you have Node.js v18 or higher version. You can check the version with the following command:

```bash
node -v
```
</Accordion>


<Accordion title="How to let AI reads the latest data from the updated API documentation?" defaultOpen={false}>
AI caches API documentation locally. If the API documentations are updated, make sure to tell the AI to refresh the API documentation data to ensure that the latest version is used when generating code.

For example：

```
Please reload API documentation and add the new fields in Pet DTO
```
</Accordion>

    

