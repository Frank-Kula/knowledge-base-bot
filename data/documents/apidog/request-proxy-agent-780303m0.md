# Request Proxy Agent

You can deploy the Apidog Request Proxy Agent on a machine with the appropriate network environment. This allows endpoint requests from the Apidog client, web, or shared documentation to be routed through this agent to the target endpoint.

This feature is particularly useful for debugging endpoints on shared documentations, as it helps resolve cross-origin resource sharing (CORS) issues. It's ideal for scenarios where different environments have specific network requirements, making direct debugging from a local environment impossible.

## Prerequisites

- A server, preferably running Linux.
- [Docker](https://www.docker.com/) installed on the server (Minimum required version: 20.10.0. Recommended version: 20.10.13).

## Deploying the Request Proxy Agent

The request proxy agent is a team/organization-level resource. Once deployed, it can be used across all projects within your team or organization. To deploy the agent on a Docker-enabled server, run the following command:

```bash
docker pull apidog/apidog-request-proxy-agent && \
docker run --name apidog-request-proxy-agent \
-p 9159:9159 \
-d apidog/apidog-request-proxy-agent
```

You can configure basic settings using environment variables during deployment. Use the following options as needed:

| **Environment Variable** | **Description** | **Example** |
|--------------------------|-----------------|-------------|
| SOURCE_IP_WHITELIST | List of allowed source IPs, separated by commas (Due to operating system restrictions, this variable can only be used on Linux and must be used with `--network=host`.) | --network=host <br> -e SOURCE_IP_WHITELIST=134.34.4.3,123.333.33.0/24 |
| SOURCE_IP_BLACKLIST | List of blocked source IPs, separated by commas (Due to operating system restrictions, this variable can only be used on Linux and must be used with `--network=host`.) | --network=host <br> -e SOURCE_IP_BLACKLIST=134.34.4.3,123.333.33.0/24 |
| DESTINATION_DOMAIN_WHITELIST | List of allowed target domain names, separated by commas | -e DESTINATION_DOMAIN_WHITELIST=xxx.yyy.com,*.yyy.com |
| DESTINATION_DOMAIN_BLACKLIST | List of blocked target domain names, separated by commas | -e DESTINATION_DOMAIN_BLACKLIST=xxx.yyy.com,*.yyy.com |
| DESTINATION_IP_WHITELIST | List of allowed target IPs, separated by commas | -e DESTINATION_IP_WHITELIST=134.34.4.3,123.333.33.0/24 |
| DESTINATION_IP_BLACKLIST | List of blocked target IPs, separated by commas | -e DESTINATION_IP_BLACKLIST=134.34.4.3,123.333.33.0/24 |
| ALLOW_PRIVATE_IP | Allow requests to internal IPs (boolean, default is false) | -e ALLOW_PRIVATE_IP=false |

:::info
The Apidog Request Proxy Agent is open-source, allowing you to customize it further to meet your needs (e.g., adding custom header parameters). [Access the source code here]().
:::

## Adding the Request Proxy Agent in Apidog

Once the Apidog request proxy agent is running on Docker, you can add it to the team resources in Apidog. Enter the server's host information (the default port is 9159) in the pop-up window and click save. Apidog will then attempt to connect.

<details>
<summary>📷 Visual Reference</summary>

<Background>
![Adding the Request Proxy Agent in Apidog.png](https://api.apidog.com/api/v1/projects/544525/resources/349524/image-preview)
</Background>

</details>

- If the connection fails, you'll see a notification and the creation will not be allowed.

<details>
<summary>📷 Visual Reference</summary>

<Background>
![connection fails.png](https://api.apidog.com/api/v1/projects/544525/resources/349525/image-preview)
</Background>

</details>

- If the connection succeeds, the request proxy agent will be successfully created within your team.

<details>
<summary>📷 Visual Reference</summary>

<Background>
![connection succeeds.png](https://api.apidog.com/api/v1/projects/544525/resources/349526/image-preview)
</Background>

</details>

Once the agent is deployed and successfully connected in Apidog, it can be used for:

- [Sending or debugging endpoint request in Apidog client using CORS proxy.](https://docs.apidog.com/use-request-proxy-agents-for-debugging-806444m0.md)
- [Resolving CORS issues on shared API documentation.](https://docs.apidog.com/quick-share-630189m0.md)

