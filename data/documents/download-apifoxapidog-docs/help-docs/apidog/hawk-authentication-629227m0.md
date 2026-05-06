# Hawk Authentication

Hawk Authentication is an HTTP request-based authentication protocol designed to provide a simple, flexible, and secure authentication mechanism. It uses HMAC (Hash-based Message Authentication Code) to create cryptographic signatures that verify both the authenticity and integrity of requests.

Hawk is particularly useful for APIs that require strong security without the complexity of OAuth, providing a lightweight alternative for service-to-service communication.

<Background>
![Hawk Authentication Configuration](https://assets.apidog.com/uploads/help/2024/04/28/8067a0e0194d2050a07be6b5bd674f7f.png)
</Background>


## Basic Settings

Configure the essential Hawk authentication parameters:

| Parameter | Description | Required |
|-----------|-------------|----------|
| **Hawk Auth ID** | Authentication identifier for the current request | Yes |
| **Hawk Auth Key** | Authentication key for the current request | Yes |
| **Algorithm** | HMAC algorithm for message authentication | Yes (SHA-256, SHA-1, etc.) |

:::info[Algorithm Selection]
The algorithm must match what your API provider expects. SHA-256 is recommended for modern implementations, while SHA-1 is supported for legacy systems.
:::

## Advanced Settings

Click the **More** option to configure additional Hawk parameters. If left blank, they will be generated automatically.

| Parameter | Description | Purpose |
|-----------|-------------|---------|
| **User** | User identifier | Identifies the user making the request |
| **Nonce** | Random client-generated string | Prevents replay attacks by ensuring request uniqueness |
| **ext** | Application-specific information | Custom data sent with the API request |
| **app** | Application identifier | Prevents credential impersonation by binding credentials to specific apps |
| **dlg** | Delegation application ID | Identifies the application that issued the credentials |
| **Timestamp** | Unix timestamp | Prevents requests outside the time window (anti-replay protection) |
| **Include payload hash** | Checkbox option | When enabled, includes a hash of the request payload in the signature |

### Security Features

**Replay Attack Prevention:**
- **Timestamp**: Ensures requests are only valid within a specific time window
- **Nonce**: Ensures each request is unique and cannot be replayed

**Credential Binding:**
- **app**: Prevents attackers from using credentials issued to other applications
- **dlg**: Tracks which application delegated the credentials

:::tip[Automatic Generation]
Apidog automatically generates `Timestamp` and `Nonce` values if left blank, ensuring proper security without manual configuration.
:::

:::warning[Payload Hash]
Enable "Include payload hash" when your API requires verification of the request body integrity. This adds the payload to the signature calculation, preventing tampering with the request body.
:::

