# Request Proxy in Client

In Apidog client, cross-origin restrictions can be completely avoided. However, we still provide the option to select a request proxy for situations where local network environments cannot access certain endpoints.

## Available Request Proxies

| Request Proxy | Description |
|---------------|-------------|
| **Use System Proxy** | Endpoint requests from Apidog will use the proxy configured in the [network proxy configuration](https://docs.apidog.com/network-proxy-configuration-640838m0.md). Note that only proxies specified in the `Proxy configurations for sending requests` are applied during requests. If the setting is configured to `Not Using Proxy`, requests will be sent directly from the client to the endpoint. |
| **Self-hosted Request Proxy** | Endpoint requests from Apidog will use a specified [self-hosted request proxy](https://docs.apidog.com/request-proxy-agent-780303m0.md) for handling requests. |

<details>
<summary>📷 Visual Reference</summary>

<Background>
![configure-request-proxy.jpg](https://api.apidog.com/api/v1/projects/544525/resources/350192/image-preview)
</Background>

</details>

:::info
When a [self-hosted request proxy](https://docs.apidog.com/use-request-proxy-agents-for-debugging-806444m0.md#set-different-request-proxy-agents-for-services-in-different-environments) is set up for a specific service (via its base URL) within a project environment, all endpoint requests to that service made through the Apidog web or client will automatically use this assigned proxy. This setting overrides any personal proxy configurations made in `Request Proxy`.
:::

