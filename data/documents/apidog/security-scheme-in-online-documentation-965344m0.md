# Security Scheme in Online Documentation

## How Security Schemes Are Shown in Online Documentation

Apidog automatically displays the auth method (security scheme) for each endpoint in the online documentation. This helps users easily identify how to authenticate their requests.

### Single Security Scheme

<Background>
![Single security scheme in documentation](https://api.apidog.com/api/v1/projects/544525/resources/354089/image-preview)
</Background>

### Multiple Security Schemes

<Background>
![Multiple security schemes in documentation](https://api.apidog.com/api/v1/projects/544525/resources/354090/image-preview)
</Background>

## How OAuth 2.0 Security Scheme Appears in Documentation

If an endpoint uses OAuth 2.0, the documentation provides more detailed information, including:

- Grant Type
- Related URLs (Authorize URL, Token URL, etc.)
- Available scopes with descriptions
- Required Scopes for the endpoint

<Background>
![OAuth 2.0 security scheme in documentation](https://api.apidog.com/api/v1/projects/544525/resources/354091/image-preview)
</Background>

## Debugging Endpoints in Online Documentation

To protect user data, Apidog separates the auth method from the auth credentials. This means that even if the default auth values are set at the folder or endpoint level, they won't be applied automatically during online debugging. You'll need to enter the credentials manually.

<Steps>
  <Step>
  Go to the online API documentation.
  </Step>
  <Step>
  Click **Try it** to open the endpoint debugging panel. In the **Auth** section, enter the required auth credentials.
  </Step>
  <Step>
  These credentials will be used for requests sent from the current endpoint.
  </Step>
</Steps>

<Background>
![Debug endpoints in online documentation](https://api.apidog.com/api/v1/projects/544525/resources/354092/image-preview)
</Background>

