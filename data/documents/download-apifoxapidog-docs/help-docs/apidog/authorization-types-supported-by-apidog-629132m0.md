# Authorization types supported by Apidog

Apidog offers various authentication methods for API requests. You can select an authentication type from the **Type** menu in the **Authorization** section of a request. Authentication can be applied at the request, collection, or folder level.

## Inherit from parent

"Inherit from Parent" is the default Auth type in Apidog. When a request's auth type is set to "Inherit from Parent," it will inherit the auth from its parent folder, and continue inheriting up to the root folder.

## No auth

If no authentication is required, Apidog won't include any authorization details. Simply choose "No Auth" from the **Type** dropdown in the **Authorization** tab for unauthenticated requests.

## API key

For API key auth, you provide a key-value pair in either the request headers or query parameters. Select "API Key" from the **Type** options, enter your key name and value, and choose to add it to either **Headers** or **Query Params**. For enhanced security, consider storing values in variables.
<p style="text-align: center">
    <img src="https://api.apidog.com/api/v1/projects/544525/resources/344013/image-preview" style="width: 640px" />
</p>

Apidog will automatically append the necessary information to your request Headers or URL query string.

## Bearer token

Bearer token auth, such as JSON Web Tokens (JWT), uses an access key in the request header. Choose "Bearer Token" from the **Type** list and input your API key in the **Token** field. For better security, use a variable to store and reference the token.

Apidog will add the token to the Authorization header in this format:
```
Bearer <Your API key>
```

For custom prefixes, utilize the API Key option with "Authorization" as the key.

## JWT bearer

Apidog also supports JWT token generation. Select "JWT Bearer" from the **Type** options. 

You can specify whether to add the token to the **Request Header** or **Query Param**, choose an algorithm (HS, RS, ES, or PS variants with SHA), and enter the necessary secret or private key. Input the payload data in JSON format.

Advanced settings allow you to configure header prefixes and custom headers.

## Basic auth

Basic auth involves sending verified credentials with your request. Select "Basic Auth" from the **Type** menu and enter your API username and password. For added security, store these in variables.

Apidog will include an Authorization header with a Base64 encoded string of your credentials in this format:
```
Basic <Base64 encoded username and password>
```

## Other authorization types

Apidog also support these authorizations:

- [Digest Auth](https://docs.apidog.com/digest-auth-629143m0.md)
- [OAuth 1.0](https://docs.apidog.com/oauth-1-0-629224m0.md)
- [OAuth 2.0](https://docs.apidog.com/oauth-2-0-629226m0.md)
- [Hawk Authentication](https://docs.apidog.com/hawk-authentication-629227m0.md)
- [NTLM](https://docs.apidog.com/ntlm-629228m0.md)
- [Akamai EdgeGrid](https://docs.apidog.com/akamai-edgegrid-629230m0.md)
