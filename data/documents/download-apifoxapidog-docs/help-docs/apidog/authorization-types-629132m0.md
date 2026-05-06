# Authorization Types

Apidog offers various authentication methods for API requests, enabling you to secure your integrations and access protected resources. This page provides a comprehensive reference of all supported authorization types and how to configure them in Apidog.

You can select an authentication type from the **Type** menu in the **Authorization** section of a request. Authentication can be applied at the request, folder, or collection level, providing flexibility in how you manage credentials across your API workspace.

## Authorization Types Comparison

| Type | Use Case | Security Level | Common Applications |
|------|----------|----------------|---------------------|
| **Inherit from Parent** | Reuse auth from parent folder/collection | Varies | Organizing requests with shared auth |
| **No Auth** | Public endpoints | None | Health checks, public data |
| **API Key** | Simple token-based auth | Medium | Internal APIs, basic integrations |
| **Bearer Token** | Token-based auth (JWT, etc.) | Medium-High | Modern APIs, microservices |
| **JWT Bearer** | Self-generated JWT tokens | High | Custom JWT implementations |
| **Basic Auth** | Username/password | Low-Medium | Legacy systems, simple auth |
| **Digest Auth** | Encrypted username/password | Medium | Enhanced security over Basic Auth |
| **OAuth 1.0** | Delegated authorization (legacy) | Medium | Twitter API, legacy services |
| **OAuth 2.0** | Modern delegated authorization | High | Google, GitHub, Microsoft APIs |
| **Hawk Authentication** | HMAC-based auth | High | Specialized secure APIs |
| **NTLM** | Windows authentication | Medium | Microsoft environments |
| **Akamai EdgeGrid** | Akamai CDN authentication | High | Akamai services |

## Inherit from Parent

:::tip[Simplify Auth Management]
"Inherit from Parent" is the default auth type in Apidog. When a request's auth type is set to "Inherit from Parent," it will inherit the auth configuration from its parent folder, and continue inheriting up to the root folder. This allows you to configure auth once at the folder level and apply it to all child requests automatically.
:::

**Benefits:**
- Centralized auth management
- Easier credential updates
- Consistent auth across related requests

## No Auth

If no authentication is required, Apidog won't include any authorization details. Simply choose **No Auth** from the **Type** dropdown in the **Authorization** tab for unauthenticated requests.

**When to use:**
- Public API endpoints
- Health check endpoints
- Endpoints that handle auth in custom ways

## API Key

For API key auth, you provide a key-value pair in either the request headers or query parameters. Select **API Key** from the **Type** options, enter your key name and value, and choose to add it to either **Headers** or **Query Params**.

<Background>
<img src="https://api.apidog.com/api/v1/projects/544525/resources/344013/image-preview" style="width: 640px" />
</Background>

Apidog will automatically append the necessary information to your request Headers or URL query string.

:::warning[Security Best Practice]
For enhanced security, store API keys in environment variables instead of hardcoding them in requests. This prevents accidental exposure in version control or shared workspaces.
:::

## Bearer Token

Bearer token auth, such as JSON Web Tokens (JWT), uses an access key in the request header. Choose **Bearer Token** from the **Type** list and input your API key in the **Token** field.

Apidog will add the token to the Authorization header in this format:
```
Bearer <Your API key>
```

:::info[Custom Prefixes]
For custom prefixes other than "Bearer", use the **API Key** option with "Authorization" as the key name.
:::

## JWT Bearer

Apidog also supports JWT token generation directly within the application. Select **JWT Bearer** from the **Type** options.

**Configuration options:**
- **Location**: Add token to **Request Header** or **Query Param**
- **Algorithm**: Choose from HS, RS, ES, or PS variants with SHA
- **Secret/Key**: Enter the necessary secret or private key
- **Payload**: Input payload data in JSON format

Advanced settings allow you to configure header prefixes and custom headers.

## Basic Auth

Basic auth involves sending verified credentials with your request. Select **Basic Auth** from the **Type** menu and enter your API username and password.

Apidog will include an Authorization header with a Base64 encoded string of your credentials in this format:
```
Basic <Base64 encoded username and password>
```

:::caution[Security Limitation]
Basic Auth transmits credentials in Base64 encoding, which is easily decoded. Always use HTTPS when using Basic Auth, and consider more secure alternatives like OAuth 2.0 for production environments.
:::

## Other Authorization Types

Apidog also supports these advanced authorization methods:

- [Digest Auth](https://docs.apidog.com/digest-auth-629143m0.md) - Enhanced security over Basic Auth with encryption
- [OAuth 1.0](https://docs.apidog.com/oauth-1-0-629224m0.md) - Legacy delegated authorization protocol
- [OAuth 2.0](https://docs.apidog.com/oauth-2-0-629226m0.md) - Modern delegated authorization with multiple grant types
- [Hawk Authentication](https://docs.apidog.com/hawk-authentication-629227m0.md) - HMAC-based authentication protocol
- [NTLM](https://docs.apidog.com/ntlm-629228m0.md) - Windows NT LAN Manager authentication
- [Akamai EdgeGrid](https://docs.apidog.com/akamai-edgegrid-629230m0.md) - Akamai CDN authentication protocol

For detailed configuration instructions for each type, click the links above to view the dedicated documentation pages.

