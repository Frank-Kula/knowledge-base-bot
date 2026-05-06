# Request Routing and Data Security

Understanding how API requests are routed is crucial for maintaining data security and privacy when using Apidog.

## Apidog Desktop Client

When using the Apidog desktop client:

**Request routing:**
- Requests are sent **directly** from your local computer to the target server
- **No routing through Apidog servers**
- Direct connection maintained

**Security:**
- Sending requests from the Apidog client is identical to sending them from your own local code
- Ensures data privacy and security
- No intermediary servers involved

## Apidog Web

When using Apidog Web, browser cross-origin restrictions prevent direct requests. You have three options to overcome this limitation:

| Option | Method | Routing | Apidog Server Involvement |
|--------|--------|---------|---------------------------|
| **1. Browser Extension** | Install Apidog Browser Extension | Direct from local computer | ❌ No |
| **2. Cloud Agent** | Use Apidog Cloud Agent | Through Apidog agent server | ✅ Yes (no logs kept) |
| **3. Self-Hosted Proxy** | Install Apidog Self-hosted Request Proxy Agent | Through your deployed agent | ❌ No |

### Option 1: Apidog Browser Extension (Recommended)

**How it works:**
- Requests sent directly from your local computer
- No Apidog server involvement
- Maximum privacy and security

### Option 2: Apidog Cloud Agent

**How it works:**
- Requests routed through Apidog agent server
- **Important**: Apidog server does NOT keep any record of the requests
- Temporary routing only

### Option 3: Self-Hosted Request Proxy Agent

**How it works:**
- Requests sent from a server where you've deployed the agent
- Full control over the proxy server
- No Apidog server involvement

:::tip[Maximum Privacy]
To ensure your requests completely bypass Apidog's servers:
- Use the **Apidog Desktop Client**, or
- Use **Option 1** (Browser Extension), or
- Use **Option 3** (Self-Hosted Proxy Agent)
:::

For detailed information, see [Request Proxy in Apidog Web](https://docs.apidog.com/request-proxy-in-web-835152m0.md).

## Data Security Commitment

Apidog takes data security very seriously and ensures protection through comprehensive security measures.

For detailed information, see our [Security Measures](https://legal.apidog.com/security-measures-645653m0).

## Related Topics

- [Data Storage and Security](https://docs.apidog.com/data-storage-and-security-1032941m0.md)
- [User Data Storage and Privacy](https://docs.apidog.com/user-data-privacy-and-security-1032859m0.md)

