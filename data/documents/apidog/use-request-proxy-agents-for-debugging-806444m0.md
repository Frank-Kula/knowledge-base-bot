# Use Request Proxy Agents for Debugging

When sending or debugging endpoint requests in Apidog, you can use a request proxy agent to initiate requests. This helps avoid issues like being unable to access intranet endpoints due to network restrictions or firewall configurations.

## Personal Request Proxy Agent Settings

In Apidog, you'll find the request proxy agent settings at the **bottom-right corner** after entering a project. Through this setting, you can choose different methods to proxy the endpoint requests initiated from Apidog.

<Background>
![use request proxy for sending endpoint request.png](https://api.apidog.com/api/v1/projects/544525/resources/349515/image-preview)
</Background>

### Apidog Client Options

| Option | Description |
|--------|-------------|
| **Follow Software Settings** | Requests sent via software proxy (requires proper configuration in [Proxy configurations for sending requests](https://docs.apidog.com/network-proxy-configuration-640838m0.md#api-request-proxy-configuration)). If `Not Using Proxy` is selected, requests are sent directly from the client to the endpoint |
| **Use Self-hosted Request Proxy Agent** | Requests routed through the specified [self-hosted request proxy agent](https://docs.apidog.com/request-proxy-agent-780303m0.md) |

<Background>
![software proxy settings.png](https://api.apidog.com/api/v1/projects/544525/resources/349517/image-preview)
</Background>

<Background>
![using-self-hosted-request-proxy-agent-sending-requests.png](https://api.apidog.com/api/v1/projects/544525/resources/349518/image-preview)
</Background>

### Apidog Web Options

| Option | Description |
|--------|-------------|
| **Auto-select Proxy** | Apidog automatically chooses between browser extension agent or cloud agent based on current browser setup (browser extension agent takes priority) |
| **Browser Extension Agent** | Uses a browser extension as the proxy for endpoint requests (requires [extension installation](https://docs.apidog.com/644359m0.md)) |
| **Cloud Agent** | Uses Apidog's cloud-based request proxy agent to send requests (cannot access internal network endpoints) |
| **Self-hosted Request Proxy Agent** | Requests routed through the [self-hosted request proxy agent](https://docs.apidog.com/request-proxy-agent-780303m0.md) you've specified |

:::info[Settings Storage]
Personal request proxy agent settings are stored in the cloud and are specific to each project, making it easy to apply them quickly in future debugging sessions.
:::

## Setting Request Proxy Agents for Services in Different Environments

Within the project, you can configure self-hosted request proxy agents for different environments and services (Base URLs) on the environment management page. Once a service is assigned a request proxy agent, all endpoint requests to that service automatically route through the selected agent.

This simplifies proxy setup across services with varying network environments, saving time and effort for your team members.

<Background>
![use request proxy for debugging endpoint request.png](https://api.apidog.com/api/v1/projects/544525/resources/349569/image-preview)
</Background>

:::warning[Important Considerations]
1. **Service Proxy Settings Take Priority**: If a request proxy agent is configured for a service, it overrides any personal proxy settings. For example, if a service is configured to use Proxy A, but a team member has set their personal proxy settings to `Not Using Proxy`, the service will still use Proxy A.
2. **Service Proxy Settings Apply Only Within Apidog App**: The request proxy agent settings in the service apply only to endpoint requests made within the project. For endpoint debugging initiated from shared documentations or public doc sites, the [CORS proxy](https://docs.apidog.com/quick-share-630189m0.md) configured in those documentations will be used to send the requests.
:::

### Managing Service Proxy Agents

You can view or configure the request proxy agent for all services using the proxy selector located at the **bottom right** of the project.

<Background>
![view or configure the request proxy agent for all services on project page.png](https://api.apidog.com/api/v1/projects/544525/resources/349521/image-preview)
</Background>

:::info[Shared Settings]
The request proxy agent settings for services are stored in the cloud and are shared among all project members.
:::

