# Akamai EdgeGrid

Akamai EdgeGrid is an HTTP request-based authentication protocol developed by Akamai Technologies. It uses a signature algorithm to generate cryptographic signatures, ensuring the integrity and authenticity of requests and preventing them from being tampered with or forged.

EdgeGrid is specifically designed for authenticating requests to Akamai's APIs and services, providing enterprise-grade security for CDN management and configuration.

:::info[Official Documentation]
For more information about Akamai EdgeGrid, visit the [official documentation](https://developer.akamai.com/legacy/introduction/Client_Auth.html).
:::

<Background>
![Akamai EdgeGrid Configuration](https://assets.apidog.com/uploads/help/2024/04/28/631a6f9d8b27dae397f14b79e059b49c.png)
</Background>

## Basic Settings

Configure the essential Akamai EdgeGrid authentication parameters:

| Parameter | Description | Source |
|-----------|-------------|--------|
| **Access Token** | Access token for the current request | Akamai Control Center → Identity Management → API Credentials |
| **Client Token** | Client token for the current request | Akamai Control Center → Identity Management → API Credentials |
| **Client Secret** | Client secret for the current request | Akamai Control Center → Identity Management → API Credentials |

:::caution[Credential Security]
Store your Akamai credentials securely. These credentials provide access to your Akamai configuration and should be treated as highly sensitive. Consider using environment variables in Apidog.
:::

## Advanced Settings

Click the **Advanced** button to configure additional EdgeGrid parameters. If left blank, they will be automatically generated.

<Background>
![Akamai EdgeGrid Advanced Settings](https://assets.apidog.com/uploads/help/2024/04/28/ca1b4a71cd8b29ad9c83ca97e8757f48.png)
</Background>

| Parameter | Description | Purpose |
|-----------|-------------|---------|
| **Nonce** | Random client-generated string | Prevents replay attacks by ensuring request uniqueness |
| **Timestamp** | Unix timestamp | Prevents requests outside the time window (anti-replay protection) |
| **Base URL** | API target address | The base URL for your Akamai API endpoint |
| **Headers to Sign** | Request headers to include in signature | Select which headers should be included in the signature calculation |

### Headers to Sign

The **Headers to Sign** option allows you to specify which request headers should be included in the signature calculation. This ensures that critical headers cannot be modified in transit without invalidating the signature.

**Common headers to sign:**
- `Content-Type`
- `Content-Length`
- Custom headers specific to your API

:::tip[Automatic Generation]
Apidog automatically generates `Nonce` and `Timestamp` values if left blank, ensuring proper security without manual configuration.
:::

