# Authentication and Authorization in Apidog

APIs utilize authentication and authorization to ensure that client requests access data securely. **Authentication** involves verifying the identity of the request sender, while **authorization** confirms that the sender has permission to access the endpoint. Apidog provides comprehensive support for both mechanisms, enabling you to secure your API requests and integrate with third-party services seamlessly.

If you're building an API, you can choose from a variety of auth models. If you're integrating with a third-party API, the required authorization will be specified by the API provider.

## What is Authentication and Authorization?

Understanding the distinction between these two concepts is essential:

| Concept | Purpose | Example |
|---------|---------|---------|
| **Authentication** | Verifies *who* you are | Logging in with username and password |
| **Authorization** | Verifies *what* you can access | Checking if you have permission to view a resource |

:::info
Some APIs require establishing a client's identity with a digital certificate. Apidog supports certificate authority (CA) and client certificates for secure authentication. Learn more about [CA and Client Certificates](https://docs.apidog.com/ca-and-client-certificates-629101m0.md).
:::

## Authentication in Apidog

Apidog supports multiple authentication methods to meet diverse security requirements. You can configure authentication at three levels:

- **Request level**: Apply auth to individual requests
- **Folder level**: Apply auth to all requests within a folder
- **Collection level**: Apply auth to all requests in a collection

### Certificate-Based Authentication

For APIs that require digital certificates, you can add your certificate authority (CA) or client certificates to Apidog. This enables you to access APIs that require mutual TLS (mTLS) authentication. Learn more about [CA and Client Certificates](https://docs.apidog.com/ca-and-client-certificates-629101m0.md).

## Authorization in Apidog

You can pass authorization details along with any request you send in Apidog. Auth data can be included in the header, body, or as parameters of a request.

### How to Configure Authorization

When you enter your auth details in the **Authorization** tab of a request, Apidog automatically populates the relevant parts of the request for your chosen auth type. This eliminates manual configuration and reduces errors.

**Key features:**
- **Inheritance**: Requests can inherit authorization from parent folders
- **Multiple auth types**: Support for API Key, Bearer Token, OAuth, Basic Auth, and more
- **Automatic population**: Auth details are automatically added to headers, body, or query parameters

:::tip
Use the **Authorization** tab of a request or folder to select an auth type and complete relevant details. This approach is more maintainable than manually adding auth headers.
:::

For a complete list of supported authorization types and detailed configuration instructions, see [Authorization Types](https://docs.apidog.com/authorization-types-629132m0.md).

