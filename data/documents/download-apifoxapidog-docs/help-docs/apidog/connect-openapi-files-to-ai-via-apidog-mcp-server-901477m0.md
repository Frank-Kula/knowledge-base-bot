# Connect OpenAPI Files to AI via Apidog MCP Server

In addition to the API specification within Apidog project, online API documentation published via Apidog, Apidog MCP Server also has the ability to directly read Swagger or OpenAPI Specification (OAS) files.

## Configuring the MCP Client

### Prerequisites

- Node.js environment installed (version 18 or later, latest LTS recommended)
- Any IDE that supports MCP:
  - Cursor
  - VSCode + Cline extension
  - Others

### Common Configuration Steps

<Steps>
  <Step title="Prepare OpenAPI File">
   - Ensure you have a URL or a local path to a Swagger/OpenAPI file
   - Supported formats: OpenAPI files in JSON or YAML 
  </Step>
  <Step title="Configure MCP in IDE">    
    Add this JSON configuration to your IDE's MCP config file:
      
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

   Where `<oas-url-or-path>` can be:  
    - A remote URL (e.g.,`https://petstore.swagger.io/v2/swagger.json`)
    - A local file path (e.g.,`~/data/petstore/swagger.json`)

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
In the opened `mcp.json` file, add the following configuration (remember to replace `https://petstore.swagger.io/v2/swagger.json` with your actual OpenAPI file path or URL):
      
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
If the AI returns correct API information in your OpenAPI file, the connection is successful.      
      
<Background>
![connect-ai-to-open-api-file-using-apidog-mcp-server.png](https://api.apidog.com/api/v1/projects/544525/resources/352793/image-preview)
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
In the opened `mcp.json` file, add the following configuration (remember to replace `https://petstore.swagger.io/v2/swagger.json` with your actual OpenAPI file path or URL)
      
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
 Test the connection by asking the AI (in `Builder with MCP` agent):

```
Please fetch API specification via MCP and tell me how many endpoints exist in the project
```   
If the AI returns correct API information in your OpenAPI file, the connection is successful.

<Background>
![verify configuration.png](https://api.apidog.com/api/v1/projects/544525/resources/354117/image-preview)
</Background>
</Step>
</Steps>
 -->
         
## Important Notes
         
- If you need to use multiple OpenAPI specification files, you can add multiple MCP Servers in the configuration file, each with a different `--oas` parameter.
- For local file paths, ensure the path is correct and the file exists. For URLs, make sure they are publicly accessible and return a valid OpenAPI specification file.
- If your OpenAPI file is large or contains complex data structures, the MCP server may take longer to process it.
- For users of the on-premise deployment, please include your on-premise server's API address in the IDE MCP configuration: "--apidog-api-base-url=`<API address of the on-premise server, starting with http:// or https://>`" Additionally, ensure network access to `www.npmjs.com` properly.
         
    ```json
    {
      "mcpServers": {
        "API specification": {
          "command": "npx",
          "args": [
            "-y",
            "apidog-mcp-server@latest",
            "--oas=<oas-url-or-path>",
            // Required for on-premise deployment:
            "--apidog-api-base-url=<API address of the on-premise server, starting with http:// or https://>"
          ]
        }
      }
    }
    ```

## Connecting Other Data Resources to AI

<Card title="Conntect API Specification within Apidog Project to AI via Apidog MCP Server" href="https://docs.apidog.com/connect-api-specification-within-apidog-project-to-ai-via-apidog-mcp-server-901476m0.md">
</Card>
    
<Card title="Conntect Online API Documentation Published by Apidog to AI via Apidog MCP Server" href="https://docs.apidog.com/connect-online-api-documentation-published-by-apidog-to-ai-via-apidog-mcp-server-901468m0.md">
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
        "--oas=<oas-url-or-path>"
      ]
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
