# Apidog MCP Server

<img src="https://img.shields.io/npm/v/apidog-mcp-server"></img>

The Apidog MCP Server enables AI-powered IDEs like Cursor to directly access and work with your API specifications, accelerating development and streamlining your workflow.

<Video src="https://www.youtube.com/watch?v=lw046MO5POY"></Video>

:::tip[]
The Apidog MCP Server is currently in beta. This documentation will be updated regularly with new features and improvements.
:::

## What Can You Do with Apidog MCP Server?

With Apidog MCP Server, AI assistants can:

- **Generate code** based on your API specifications
- **Search and query** API specification content
- **Update DTOs** with new fields from specifications
- **Add documentation** comments to code based on API specs
- **Create complete MVC code** for specific endpoints

The possibilities are endless—let your creativity guide you!

## How It Works

Once configured, Apidog MCP Server automatically reads and caches all API specification data locally. The AI can then seamlessly retrieve and utilize this data.

Simply tell the AI what you want to accomplish. For example:

- *"Use MCP to fetch the API specification and generate Java records for the 'Product' schema and related schemas"*
- *"Based on the API specification, add the new fields to the 'Product' DTO"*
- *"Add comments for each field in the 'Product' class based on the API specification"*
- *"Generate all the MVC code related to the endpoint '/users' according to the API specification"*

:::info[]
API specifications are cached locally. If data in Apidog changes, ask the AI to refresh to ensure it reads the latest updates.
:::

## Prerequisites

Before setting up Apidog MCP Server, ensure you have:

- **Node.js** (version 18 or later, preferably the latest LTS version)
- An **MCP-compatible IDE**:
  - Cursor
  - VS Code + Cline plugin
  - Other MCP-supported editors

## Choosing Your Data Source

Apidog MCP Server supports three different data sources. Select the configuration method that matches your needs:

<AccordionGroup>
  <Accordion title="Use Apidog Project as the Data Source" defaultOpen>

**Best for:**
- Accessing API specifications within your Apidog team
- Private or internal API development

**Requirements:**
- Apidog personal API access token

**Setup guide:** [Connect Apidog Project to AI](https://docs.apidog.com/connect-apidog-project-to-ai-901476m0.md)
  </Accordion>
      
   <Accordion title="Use Online API Documentation Published by Apidog as the Data Source">

**Best for:**
- Reading publicly published API documentation
- Allowing external developers (API consumers) to access your team's public documentation via AI

**Requirements:**
- No Apidog personal API access token required
- Only supports publicly accessible documentation (password-protected or allowlist documentation is not supported)

**Setup guide:** [Connect Published Documentation to AI](https://docs.apidog.com/connect-published-documentation-to-ai-901468m0.md)

:::tip[]
For non-public API specifications within your team, use the [Apidog Project data source](https://docs.apidog.com/connect-apidog-project-to-ai-901476m0.md) instead.
:::
  </Accordion>
      
  <Accordion title="Use Swagger/OpenAPI Files as the Data Source">

**Best for:**
- Reading local or online Swagger/OpenAPI files
- Working independently of Apidog projects

**Requirements:**
- No Apidog personal API access token required
- Independent of Apidog projects or online documentation

**Setup guide:** [Connect OpenAPI Files to AI](https://docs.apidog.com/connect-openapi-files-to-ai-901477m0.md)
  </Accordion>
</AccordionGroup>

## On-Premise Deployment Configuration

For on-premise deployments, add your server's API address to the configuration regardless of which data source you choose:

```json
{
  "mcpServers": {
    "API specification": {
      "command": "npx",
      "args": [
        "-y",
        "apidog-mcp-server@latest",
        "--apidog-api-base-url=<your-server-url>"
      ]
    }
  }
}
```

Replace `<your-server-url>` with your on-premise server's API address (starting with `http://` or `https://`).

:::tip[]
Ensure your environment can access `www.npmjs.com` properly.
:::

## Help and Support

The Apidog MCP Server is currently in beta. We'd love to hear your feedback and suggestions!

Join our community:
- [Discord](https://discord.com/invite/ZBxrzyXfbJ)
- [Slack](https://join.slack.com/t/apidogcommunity/shared_invite/zt-2sgz1kxxe-QvLy_LfE6piCYzw_c~kunQ)

