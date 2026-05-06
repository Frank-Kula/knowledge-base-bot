# LLM-friendly Features

> Apidog Version Should Be 2.7.2 or Later.

Navigate to: `Share Docs` -> `Publish Docs Sites` -> `LLM-friendly Features` to enable the following options.

<Background>
![llm-friendly-features.png](https://api.apidog.com/api/v1/projects/544525/resources/356565/image-preview)
</Background>

## Enable "MCP"

If enabled, a "MCP" button will be displayed in the documentation, guiding end users how to use the current API documentation in MCP-enabled IDEs, such as Cursor, Cline, etc., to assist the Agentic AI in writing code. For more details, please read: [Conntect Online API Documentation Published by Apidog to AI via Apidog MCP Server](https://docs.apidog.com/connect-online-api-documentation-published-by-apidog-to-ai-via-apidog-mcp-server-901468m0.md).

![Apidog MCP Server](https://assets.apidog.com/uploads/help/2025/03/26/1562f2ed8710ec754897595552c1b84c.gif)

## Enable "Copy Page"

If enabled, a "Copy page" button will be displayed in the documentation. Users can copy web page as Markdown for LLMs.

<Background>
![copy-page.png](https://api.apidog.com/api/v1/projects/544525/resources/356566/image-preview)
</Background>

## Enable LLMs.txt

If enabled, a `llms.txt` Markdown file will be generated in the root directory of your documentation site. This file contains links to every Markdown page on your site, along with concise descriptions. For example:

<Background>
![llms-txt.png](https://api.apidog.com/api/v1/projects/544525/resources/356567/image-preview)
</Background>

### How can AI assistants use LLMs.txt?

There are two common methods for using LLMs.txt and the related Markdown files:

**1. Share Markdown links with AI assistants that can access URLs**

Each online documentation page published via Apidog has a Markdown version. You can:

- Add ".md" to any doc URL (e.g., https://example.apidog.io/page.md)
- Or click "View as Markdown" in the online documentation

<Background>
![Add-.md-to-any-doc-URL.png](https://api.apidog.com/api/v1/projects/544525/resources/356568/image-preview)
</Background>

AI assistants with Web Browsing capabilities can use these ".md" URLs to retrieve concise documentation.

For example, in Cursor, you can ask "Understand this info: @https://zojphlasi1.apidog.io/find-pet-by-id-12888653e0.md and help me generate a TypeScript client".

<Background>
![usage example using Cursor.png](https://api.apidog.com/api/v1/projects/544525/resources/356570/image-preview)
</Background>

:::tip[]
The prompt format must follow the specific rules of the AI tool being used. For instance, in Cursor, URLs must begin with `@` to be recognized as context.
:::

**2. Copy Markdown content for AI assistants that can't access URLs**

If the AI assistant cannot access content via URL, you need to copy and paste the Markdown content manually.

<Background>
![image.png](https://api.apidog.com/api/v1/projects/544525/resources/356571/image-preview)
</Background>

Click the "Copy Page" button in the online documentation to get the current page content in Markdown format, then paste it into your conversation with the AI assistant.

Example prompt:
"Based on this endpoint definition, please generate a TypeScript client: (paste the copied content here)."

<Background>
![image.png](https://api.apidog.com/api/v1/projects/544525/resources/356578/image-preview)
</Background>

### FAQs

<Accordion title="Does enabling LLMs.txt affect documentation security?" defaultOpen>
**No.** LLMs.txt only includes content that has already been publicly published. It simply converts HTML to Markdown and does not expose private or unpublished documentations. If access control (password, IP allowlist, email allowlist, etc.) is set up, users must still pass authentication to access LLMs.txt and the Markdown files. 
</Accordion>

<Accordion title="Can I use LLMs.txt if my docs are protected by password, IP, or email allowlist?？" defaultOpen={false}>
Yes, you can. However, since accessing LLMs.txt and Markdown files requires authentication, AI assistants may not be able to access them directly via URL. In that case, use the "**Copy Page**" feature and paste the content manually. 
</Accordion>

<Accordion title="Why don't I see the button `Copy Page` in Apidog App?" defaultOpen={false}>
These features are available in the **published online documentation**. After publishing the docs, open them in your **web browser** to see the buttons. 
</Accordion>

<Accordion title="I’ve enabled 'Web Search' feature for my AI assistant. Why can’t it read the web page content via URL?" defaultOpen={false}>
"Web Search" and "Web Browsing" are different features. 
- **Web Search** allows the AI to query search engines and summarize results. 
- **Web Browsing** allows the AI to directly access and read a specific URL’s content. 
</Accordion>

<Accordion title="What should I do if the AI assistant fails to access the Markdown file via URL?" defaultOpen={false}>
Use the "**Copy Page**" button in the online documentation and paste the content directly into the AI conversation. 
</Accordion>

<Accordion title="Do I need to do anything else after enabling LLMs.txt?" defaultOpen={false}>
No. Once enabled, the system will automatically generate `llms.txt` and Markdown files for each documentation page. You just need to maintain the original documentation.
</Accordion>

<Accordion title="How can I verify that LLMs.txt is working properly?" defaultOpen={false}>
Visit the `/llms.txt` path at the root of your published documentation site. If you see a structured list of page links, the feature is enabled and working.
</Accordion>
