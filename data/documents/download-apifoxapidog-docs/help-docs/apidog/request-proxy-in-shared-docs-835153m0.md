# Request Proxy in Shared Docs

When sharing an API documentation or making it public, you can choose a request proxy for the online documentations to avoid cross-origin (CORS) issues.

## Available Request Proxies

| Request Proxy | Description |
|---------------|-------------|
| **Cloud Agent** | Uses Apidog's cloud agent to handle requests. Note that this Agent cannot access endpoints from the intranet. |
| **Browser Extension** | Uses the [browser extension](https://docs.apidog.com/installing-apidog-chrome-extension-821769m0.md) installed by the user in their own browser as the Agent to send requests. If the user has not installed the extension, they will be prompted to install it to initiate requests. |
| **No Proxy** | Does not use a cross-origin proxy, meaning requests are sent directly from the user's browser to the endpoint. Ensure that the endpoint server is properly configured to avoid CORS (Cross-Origin Resource Sharing) issues. |
| **Self-hosted request proxy Agent** | Uses a self-hosted [request proxy agent](https://docs.apidog.com/request-proxy-agent-780303m0.md) deployed by your team to handle requests. |

<details>
<summary>📷 Visual Reference</summary>

<Background>
![request-proxy-online-documentation.png](https://api.apidog.com/api/v1/projects/544525/resources/350187/image-preview)
</Background>

</details>

:::tip
For public documentation, consider using the Cloud Agent for the best user experience, as it requires no installation. For internal documentation, a self-hosted proxy agent provides better security and access to private networks.
:::

