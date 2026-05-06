# Network Proxy Configuration

A **network proxy** acts as an intermediary server, routing requests from Apidog to internet resources while safeguarding your internal network. Apidog provides flexible proxy configuration options to accommodate different network environments and security requirements.

## Proxy Configuration Types

- **Default Proxy Configuration**: Manages how Apidog connects to the internet and sends API requests
- **API Request Proxy Configuration**: Specific to API requests and can be customized independently to use either the default settings or a custom setup

If your proxy requires authentication, enter the necessary details under **Settings** → **Network Proxy**, accessible from the lower-left corner of the Apidog interface.

<Background>
![](https://assets.apidog.com/uploads/help/2023/07/12/73e06342d8c940c7214fc4a10c5e1ace.png)
</Background>

Both proxy settings offer a default option of **Do Not Use Proxy**, with the API configurations set to **Use Default Configuration** initially.

## Default Proxy Configuration

1. The default proxy includes all network services related to Apidog such as server connection and API requests, with the initial setting of **Do Not Use Proxy**.

2. If your local system uses a proxy, set Apidog's default proxy to **Use System Proxy**.

3. You can also configure a **Custom Proxy** if needed.

## API Request Proxy Configuration

1. If set to **Use Default Configuration**, API requests will mirror the default proxy settings.

2. For API requests to use the system proxy settings, ensure both default and API proxy settings are appropriately linked.

:::tip
To incorporate the HTTP_PROXY, HTTPS_PROXY, and NO_PROXY environment variables from your system into Apidog, enable the following option:

<details>
<summary>📷 Visual Reference</summary>

<Background>
![](https://assets.apidog.com/uploads/help/2023/07/12/89fc0e4b725db4fecd6d77c0baec680b.png)
</Background>

</details>

:::

## Specific Proxy Configuration 

### Configure Custom Proxy

For using a different proxy server from the system settings for API requests, configure a custom proxy. You have the flexibility to route HTTP, HTTPS, or both types of requests through the custom proxy.

**Configuration Options:**

- **API Type**: Define if HTTP, HTTPS, or both are routed via the proxy
- **Proxy Server**: Input the hostname or IP and port number
- **Bypass**: List the hosts that should bypass the proxy
- **Authentication**: If needed, enable this option and provide the username and password for the proxy

<details>
<summary>📷 Visual Reference</summary>

<Background>
![](https://assets.apidog.com/uploads/help/2023/07/12/6e35db4edabc9b3c462a7c377f111286.png)
</Background>

</details>

### Authentication Process

For proxies requiring credentials, provide the username and password under **Settings** → **Network Proxy**. 

1. Enable the **Authentication** feature under the chosen proxy configuration (either **System Proxy** or **Custom**)
2. Enter your credentials
3. Click **Save and Restart Apidog**

<details>
<summary>📷 Visual Reference</summary>

<Background>
![](https://assets.apidog.com/uploads/help/2023/07/12/7b64445da5b6952dfb17c35c16910037.png)
</Background>

</details>

## Proxy Setup During Login

You can configure the **Network Proxy** directly from the login screen if a proxy is essential for accessing Apidog.

<Background>
![](https://assets.apidog.com/uploads/help/2023/07/12/143262ed496369b012ff059599ef998d.png)
</Background>

:::info
If you're behind a corporate firewall or VPN, consult your IT department for the correct proxy settings to use with Apidog.
:::

