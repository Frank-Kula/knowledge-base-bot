# Connect Apidog Project to AI

Apidog MCP Server enables AI to connect and utilize API specifications within your Apidog project, allowing AI assistants to generate code, search specifications, and accelerate development workflows.

## Prerequisites

Before configuring the MCP client, ensure you have:

- **Node.js** (version 18 or later, preferably the latest LTS version)
- An **MCP-compatible IDE**:
  - Cursor
  - VS Code + Cline plugin
  - Other MCP-supported editors

## Obtaining Required Credentials

<Steps>
  <Step title="Generate API Access Token">
   1. Open Apidog and hover over your profile picture (top-right)
   2. Select **Account Settings** → **API Access Token**
   3. [Create a new API access token](https://docs.apidog.com/api-access-token.md)
   4. Copy the token to replace `<access-token>` in the configuration
      
    <Background>  
![Creating a new API access token](https://api.apidog.com/api/v1/projects/544525/resources/352790/image-preview)
    </Background>
 
  </Step>
  <Step title="Get Apidog Project ID (Optional)">
   1. Open your target project in Apidog
   2. Click **Project Settings** in the left sidebar
   3. Navigate to **Basic Settings**
   4. Copy the Project ID to replace `<project-id>` in the configuration
      
    <Background>
![Apidog project ID location](https://api.apidog.com/api/v1/projects/544525/resources/352791/image-preview)
    </Background>

  </Step>
  <Step title="Copy the MCP Configuration within the Project">
  
You can open any API and use the **AI Coding** entry to copy its MCP configuration directly.
      
    <Background>
![Copying MCP configuration from Apidog](https://api.apidog.com/api/v1/projects/544525/resources/358488/image-preview)
</Background>

  </Step>
</Steps>

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
Paste the following configuration into the opened `mcp.json` file. Replace `<access-token>` and `<project-id>` with your actual values:
      
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
                "--project=<project-id>"
              ],
              "env": {
                "APIDOG_ACCESS_TOKEN": "<access-token>"
              }
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
                "--project=<project-id>"
              ],
              "env": {
                "APIDOG_ACCESS_TOKEN": "<access-token>"
              }
            }
          }
        }
        ```
      </Tab>
    </Tabs>  
  </Step>
  <Step title="Verify Configuration">
Test the connection by asking the AI (in Agent mode):

```
Please fetch API specification via MCP and tell me how many endpoints exist in the project
```   

If the AI returns your Apidog project's API information, the connection is successful.

<Background>
![Successful connection verification](https://api.apidog.com/api/v1/projects/544525/resources/352792/image-preview)
</Background>
  </Step>
</Steps>    

## Important Notes

:::warning[]
Replace `<access-token>` and `<project-id>` with your personal Apidog API access token and project ID.
:::

### Working with Multiple Projects

To work with API specifications from multiple projects, add multiple MCP Server configurations to the configuration file. Each project should have its own unique `<project-id>`. 

For clarity, name each MCP Server following the format **"[Project Name] API Specification"**.

### Security Best Practices

If your team syncs the MCP configuration file to a code repository:

1. Remove the line `"APIDOG_ACCESS_TOKEN": "<access-token>"` from the configuration
2. Configure `APIDOG_ACCESS_TOKEN` as an environment variable on each team member's machine

This prevents token leakage in version control.

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
        "--project=<project-id>",
        "--apidog-api-base-url=<your-server-url>"
      ],
      "env": {
        "APIDOG_ACCESS_TOKEN": "<access-token>"
      }
    }
  }
}
```

Replace `<your-server-url>` with your on-premise server's API address (starting with `http://` or `https://`). Ensure network access to `www.npmjs.com`.

## Other Data Sources

<Card title="Connect Online API Documentation Published by Apidog to AI" href="https://docs.apidog.com/connect-published-documentation-to-ai-901468m0.md">
</Card>

<Card title="Connect OpenAPI Files to AI" href="https://docs.apidog.com/connect-openapi-files-to-ai-901477m0.md">
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
        "--project=<project-id>"
      ],
      "env": {
        "APIDOG_ACCESS_TOKEN": "<access-token>"
      }
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

<Accordion title="How to let AI read the latest data from updated API specifications?" defaultOpen={false}>

AI caches API specifications locally. If specifications are updated, tell the AI to refresh the data to ensure it uses the latest version when generating code.

For example:

```
Please reload API specification and add the new fields in Pet DTO
```
</Accordion>

