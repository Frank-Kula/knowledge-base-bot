# AI Features

Make your API documentation AI-ready with AI features that enable seamless integration with AI assistants and development tools. These features help developers leverage AI tools like Cursor, Cline, and other AI-powered IDEs to accelerate API integration and code generation.

:::info[Version Requirement]
Apidog version must be ≥ 2.7.2 to access these features.
:::

**To enable these features:** Navigate to `Publish Docs` → `Publish Docs Sites` → `AI Features`.

<Background>
<p style="text-align: center">
  <img src="https://api.apidog.com/api/v1/projects/544525/resources/371647/image-preview" />
</p>
</Background>

## Ask AI 
This feature enables conversational searching feature on your documentaton page. You can connect your AI Assistant from Algolia to utilize this feature. You can learn more about this feature on the [Ask AI](https://docs.apidog.com/documentation-search-746862m0.md#ask-ai) section of the **Documentation Search** page. 

## Enable MCP (Model Context Protocol)

When enabled, an "MCP" button appears in your documentation, guiding users on how to connect your API documentation to MCP-enabled IDEs such as Cursor and Cline. This allows Agentic AI to assist with code generation directly from your API documentation.

:::tip[Learn More]
For detailed setup instructions, read: [Connect Online API Documentation Published by Apidog to AI via Apidog MCP Server](https://docs.apidog.com/connect-published-documentation-to-ai-901468m0.md).
:::

<Background>
<p style="text-align: center">
  <img src="https://assets.apidog.com/uploads/help/2025/03/26/1562f2ed8710ec754897595552c1b84c.gif" />
</p>
</Background>

## Enable Copy Page

When enabled, a "Copy page" button appears in your documentation, allowing users to copy the current page as Markdown format—perfect for pasting into AI conversations.

<Background>
<p style="text-align: center">
  <img src="https://api.apidog.com/api/v1/projects/544525/resources/356566/image-preview" />
</p>
</Background>

## Enable llms.txt

When enabled, a `llms.txt` Markdown file is automatically generated in the root directory of your documentation site. This file contains links to every Markdown page with concise descriptions, making it easy for AI assistants to discover and navigate your documentation.

**Example:**

<Background>
<p style="text-align: center">
  <img src="https://api.apidog.com/api/v1/projects/544525/resources/356567/image-preview" />
</p>
</Background>

### How AI Assistants Use llms.txt

There are two common methods for using llms.txt and related Markdown files:

**1. Share Markdown links with AI assistants that can access URLs**

Each online documentation page published via Apidog has a Markdown version. You can:

- Add ".md" to any doc URL (e.g., https://example.apidog.io/page.md)
- Or click "View as Markdown" in the online documentation

<Background>
<p style="text-align: center">
  <img src="https://api.apidog.com/api/v1/projects/544525/resources/356568/image-preview" />
</p>
</Background>

AI assistants with Web Browsing capabilities can use these ".md" URLs to retrieve concise documentation.

For example, in Cursor, you can ask "Understand this info: @https://zojphlasi1.apidog.io/find-pet-by-id-12888653e0.md and help me generate a TypeScript client".

<Background>
<p style="text-align: center">
  <img src="https://api.apidog.com/api/v1/projects/544525/resources/356570/image-preview" />
</p>
</Background>

:::tip[Prompt Format]
The prompt format must follow the specific rules of the AI tool being used. For instance, in Cursor, URLs must begin with `@` to be recognized as context.
:::

**2. Copy Markdown content for AI assistants that can't access URLs**

If the AI assistant cannot access content via URL, you need to copy and paste the Markdown content manually.

<Background>
<p style="text-align: center">
  <img src="https://api.apidog.com/api/v1/projects/544525/resources/356571/image-preview" />
</p>
</Background>

Click the "Copy Page" button in the online documentation to get the current page content in Markdown format, then paste it into your conversation with the AI assistant.

**Example prompt:**

"Based on this endpoint definition, please generate a TypeScript client: (paste the copied content here)."

<Background>
<p style="text-align: center">
  <img src="https://api.apidog.com/api/v1/projects/544525/resources/356578/image-preview" />
</p>
</Background>

### FAQs

<Accordion title="Does enabling llms.txt affect documentation security?" defaultOpen>
**No.** llms.txt only includes content that has already been publicly published. It simply converts HTML to Markdown and does not expose private or unpublished documentation. If access control (password, IP allowlist, email allowlist, etc.) is configured, users must still pass authentication to access llms.txt and Markdown files. 
</Accordion>

<Accordion title="Can I use llms.txt if my docs are protected by password, IP, or email allowlist?？" defaultOpen={false}>
Yes, you can. However, since accessing llms.txt and Markdown files requires authentication, AI assistants may not be able to access them directly via URL. In that case, use the **Copy Page** feature and paste the content manually. 
</Accordion>

<Accordion title="Why don't I see the button `Copy Page` in Apidog App?" defaultOpen={false}>
These features are available in the **published online documentation**. After publishing your docs, open them in your **web browser** to see the buttons. 
</Accordion>

<Accordion title="I’ve enabled 'Web Search' feature for my AI assistant. Why can’t it read the web page content via URL?" defaultOpen={false}>
"Web Search" and "Web Browsing" are different features. 
- **Web Search** allows the AI to query search engines and summarize results. 
- **Web Browsing** allows the AI to directly access and read a specific URL’s content. 
</Accordion>

<Accordion title="What should I do if the AI assistant fails to access the Markdown file via URL?" defaultOpen={false}>
Use the "**Copy Page**" button in the online documentation and paste the content directly into the AI conversation. 
</Accordion>

<Accordion title="Do I need to do anything else after enabling llms.txt?" defaultOpen={false}>
No. Once enabled, the system will automatically generate `llms.txt` and Markdown files for each documentation page. You just need to maintain the original documentation.
</Accordion>

<Accordion title="How can I verify that llms.txt is working properly?" defaultOpen={false}>
Visit the `/llms.txt` path at the root of your published documentation site. If you see a structured list of page links, the feature is enabled and working.
</Accordion>
