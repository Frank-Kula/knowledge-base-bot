# Connect API Specification within Apidog Project to AI via Apidog MCP Server

Apidog MCP Server enables AI to connect and utilize API specifications within your Apidog project.

## Configuring the MCP Client

### Prerequisites

- Node.js environment installed (version 18 or higher, latest LTS recommended)
- Any IDE that supports MCP:
  - Cursor
  - VSCode + Cline extension
  - Others

### Obtaining API Access Token and Project ID

<Steps>
  <Step title="Generate API Access Token">
   - Open Apidog, hover over your profile picture (top-right), and select `Account Settings` → `API Access Token`
   - [Create a new API access token](https://docs.apidog.com/api-access-token.md) and replace `<access-token>` in the configuration below
      
    <Background>  
![creating-new-api-access-token.png](https://api.apidog.com/api/v1/projects/544525/resources/352790/image-preview)
    </Background>
 
  </Step>
  <Step title="Get Apidog Project ID (Optional)">
   - Open your target project in Apidog
   - Click "Project Settings" in the left sidebar, then copy the Project ID from "Basic Settings"
   - Replace `<project-id>` in the configuration below 
      
    <Background>
![apidog-project-id.png](https://api.apidog.com/api/v1/projects/544525/resources/352791/image-preview)
    </Background>

  </Step>
  <Step title="Copy the MCP Configuration within the Project">
  
You can open any API and use the AI Coding entry to copy its MCP configuration.
      
    <Background>

![03-apidog.gif](https://api.apidog.com/api/v1/projects/544525/resources/358488/image-preview)
    </Background>

  </Step>
</Steps>

### Configuring MCP in Cursor

<Steps>
  <Step title="Edit MCP Config File">
Open Cursor editor, click the settings icon (top-right), select "MCP" from the left menu, then click "+ Add new global MCP server".
      
<Background>
![mcp-server-setting-cursor.png](https://api.apidog.com/api/v1/projects/544525/resources/352759/image-preview)
</Background>

  </Step>
  <Step title="Add Configuration">
Paste the following configuration in the opened `mcp.json`. Remember to replace `<access-token>` and `<project-id>` with your own:
      
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
Successful connection is confirmed when AI returns your Apidog project's API information.

<Background>
![connecting-apidog-project-with-idea.png](https://api.apidog.com/api/v1/projects/544525/resources/352792/image-preview)
</Background>
  </Step>
</Steps>    

<!--          
### Configuring MCP in Trae

<Steps>
  <Step title="Edit the MCP Configuration File">
Open the latest version (v1.3.2 or higher) of the Trae editor. Click `Toggle AI Side Bar` → `AI Management` at the top-right corner. 
      
![trae-ai-tool-settings.png](https://api.apidog.com/api/v1/projects/544525/resources/354096/image-preview)
    
Go to the "MCP" tab.      
<Background>
![trae-mcp-settings.png](https://api.apidog.com/api/v1/projects/544525/resources/354097/image-preview)
</Background>

Click on `+ Add MCP Servers`. 
      
<Background>
![add-mcp-servers-trae-ai.png](https://api.apidog.com/api/v1/projects/544525/resources/354099/image-preview)
</Background>

In the MCP Marketplace, click on `Configure Manually`.    

<Background>
![conigure-mcp-server-manually-trae-ai.png](https://api.apidog.com/api/v1/projects/544525/resources/354100/image-preview)
</Background>      

You will be directed to the `mcp.json` panel.

<Background>
![configure-manually-mcp-sever-trae-ai-editor.png](https://api.apidog.com/api/v1/projects/544525/resources/354101/image-preview)
</Background> 

  </Step>
  <Step title="Add MCP Configuration">
In the opened `mcp.json` file, add the following configuration. Make sure to replace `<access-token>` and `<project-id>` with your own values:
      
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
 Test the connection by asking the AI (in `Builder with MCP` agent):

```
Please fetch API specification via MCP and tell me how many endpoints exist in the project
```   
Successful connection is confirmed when AI returns your Apidog project's API information. 

<Background>
![verify MCP server.png](https://api.apidog.com/api/v1/projects/544525/resources/354102/image-preview)
</Background>
</Step>
</Steps>
-->         
    
## Important Notes

- Replace `<access-token>` and `<project-id>` with your personal Apidog API access token and project ID.
- If you need to work with API specification from several projects, simply add multiple MCP Server configurations to the configuration file. Each project should have its own unique `<project-id>`. For clarity, name each MCP Server following the format **"xxx API Specification"**.
- If your team syncs the MCP configuration file to a code repository, it is recommended to remove the line `"APIDOG_ACCESS_TOKEN": "<access-token>"` and instead, configure the `APIDOG_ACCESS_TOKEN` as an environment variable on each member's machine to prevent token leakage.
- For users of the on-premise deployment, please include your on-premise server's API address in the IDE MCP configuration: "--apidog-api-base-url=`<API address of the on-premise server, starting with http:// or https://>`". Additionally, ensure network access to `www.npmjs.com` properly.
      
    ```json
    {
      "mcpServers": {
        "API specification": {
          "command": "npx",
          "args": [
            "-y",
            "apidog-mcp-server@latest",
            "--project=<project-id>",
            // Required for on-premise deployment:
            "--apidog-api-base-url=<API address of the on-premise server, starting with http:// or https://>"
          ],
          "env": {
            "APIDOG_ACCESS_TOKEN": "<access-token>"
          }
        }
      }
    }
    ```
  
## Connecting Other Data Resources to AI


<Card title="Conntect Online API Documentation Published by Apidog to AI via Apidog MCP Server" href="https://docs.apidog.com/connect-online-api-documentation-published-by-apidog-to-ai-via-apidog-mcp-server-901468m0.md">
</Card>

<Card title="Conntect OpenAPI Files to AI via Apidog MCP Server" href="https://docs.apidog.com/connect-openapi-files-to-ai-via-apidog-mcp-server-901477m0.md">
</Card>
      
      
## FAQs


<Accordion title="Windows Configuration Issues" defaultOpen>

If standard configuration fails on Windows, use this instead:

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

If you see Node.js version errors, ensure you’re using v18 or higher. Check with:

```bash
node -v
```
</Accordion>

<Accordion title="How to let AI reads the latest data from the updated API specification?" defaultOpen={false}>
AI caches API specification locally. If the API specifications are updated, make sure to tell the AI to refresh the API specification data to ensure that the latest version is used when generating code.

For example：

```
Please reload API specification and add the new fields in Pet DTO
```
</Accordion>


