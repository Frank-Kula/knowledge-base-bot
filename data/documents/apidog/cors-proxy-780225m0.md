# CORS Proxy

When debugging endpoints on a published doc site, users might run into CORS (Cross-origin Resource Sharing) issues caused by browser security restrictions. To fix this, you can set up a CORS proxy for the site. This ensures that all endpoint requests from the doc site are routed through a designated Request Proxy Agent.

<Background>
![cors-proxy-settings.png](https://api.apidog.com/api/v1/projects/544525/resources/349514/image-preview)
</Background>

Here are the proxy options available, depending on your needs:

- **Cloud Agent**: This uses Apidog'sCloud Agentto handle endpoint requests from the shared documentation. Keep in mind that the Cloud Agent cannot access endpoints on internal network.

- **Browser Extensions**: This option uses a browser extension installed in the user's browser to handle requests. If the user hasn't installed the extension, they'll be prompted to do so before initiating any endpoint requests.

- **No Proxy**: Selecting this option means that requests will be directly sent from the user's browser to the endpoint. Ensure the endpoint server settings are configured correctly to handle CORS, preventing potential issues.

- **Self-hosted Request Proxy Agent**: This allows you to use a [Self-hosted Request Proxy Agent](https://docs.apidog.com/request-proxy-agent-780303m0.md) deployed within your team to handle endpoint requests from the shared documentation.

## How to Choose a Proxy Type?
- **Public API/Endpoints**: Prioritize using **Cloud Agent**.
- **Internal API/Endpoints**: 
  - Simple scenarios: Use **Browser Extension**.
  - High-security requirements: Use **Self-Hosted Request Proxy Agent**.


## FAQ

<Accordion title="Why can't the browser extension carry Cookies?" defaultOpen>
Browser security policies block extensions from modifying reserved headers like `Cookie` ([full list](https://developer.mozilla.org/en-US/docs/Glossary/Forbidden_request_header)). To carry Cookies in requests, use the [Cloud Agent](https://docs.apidog.com/request-proxy-in-web-835152m0.md) or [Apidog Desktop Client](https://apidog.com/download/).
</Accordion>

## Learn more


- [Request proxy in Apidog web](https://docs.apidog.com/request-proxy-in-web-835152m0.md)

- [Request proxy in shared docs](https://docs.apidog.com/request-proxy-in-shared-docs-835153m0.md)

- [Request proxy in Apidog client](https://docs.apidog.com/request-proxy-in-client-835154m0.md)

