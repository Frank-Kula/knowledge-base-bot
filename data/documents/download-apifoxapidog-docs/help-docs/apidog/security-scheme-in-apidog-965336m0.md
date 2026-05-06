# Security Scheme in Apidog

## What are Security Schemes?

Security schemes are a way to define how your endpoints are authenticated, following the OpenAPI Specification (OAS). Instead of setting up authentication for each endpoint individually, you can create a reusable template (a security scheme) that separates the authentication methods from the actual credentials. This makes it easier for teams to manage, update, and reuse authentication settings more flexibly.

## Why Use Security Schemes?

- **Define Once, Use Everywhere**: Create a security scheme once and reuse it across multiple endpoints or folders.
- **Flexible Combinations**: An endpoint can use more than one type of security scheme.
- **Separation of Template and Value**: Keep the authentication rules (template) separate from the actual values (credentials), which makes things easier to maintain.
- **Prevents Credential Leakage**: When testing endpoints with security schemes on online documentation, credentials must be entered manually.
- **Inherits Automatically**: Endpoints can inherit security schemes from their parent folders, reducing repetitive setup.
- **Supports All Major Auth Methods**: Including API Key, Bearer Token, Basic Auth, OAuth 2.0, and more.
- **OpenAPI Compliant**: Fully compatible with the OpenAPI 3.0 Security Schemes specification.

## When Should You Use It?

- When several endpoints share the same authentication method.
- When a single endpoint requires multiple authentication types.
- When you need different credentials for different environments.
- When teams are working together and need a unified way to manage authentication.
- When you want to include clear, standardized security definitions in your OpenAPI documentation.

