# Create a Security Scheme

Apidog offers a wide range of security scheme types, supporting various authentication methods, including:

1. **API Key** – Authenticate using a key passed via Header, Query, or Cookie.
2. **Bearer Token** – Authenticate using the `Authorization: Bearer` header.
3. **JWT** – Authenticate with tokens in JSON Web Token format.
4. **Basic Auth** – Use a username and password for basic authentication.
5. **Digest Auth** – More secure than basic auth.
6. **OAuth 2.0** – A widely adopted authorization standard supporting multiple grant types.
7. **OAuth 1.0** – An earlier version of OAuth with a different signature mechanism.
8. **Hawk Authentication** – HMAC-based authentication protocol.
9. **AWS Signature** – Signature-based authentication used for Amazon AWS services.
10. **Kerberos** – Ticket-based network authentication protocol.
11. **NTLM Authentication** – Authentication protocol developed by Microsoft.
12. **Akamai EdgeGrid** – Authentication method used by the Akamai API platform.
13. **Customize** – Allows you to define and use authentication methods that aren't natively supported by Apidog.

<Background>
![Security scheme types in Apidog](https://api.apidog.com/api/v1/projects/544525/resources/353982/image-preview)
</Background>

## Creating Security Schemes Manually

<Steps>
  <Step>
    In your project, navigate to **Components** > **Security Schemes** at the left sidebar, then click **New Security Scheme**.
      
<Background>
![Creating new security scheme](https://api.apidog.com/api/v1/projects/544525/resources/353983/image-preview)
</Background>
  </Step>
  <Step>
   Select the security scheme type and fill in the name and relevant configuration.
      
<Background>
![Configuring security scheme](https://api.apidog.com/api/v1/projects/544525/resources/353984/image-preview)
</Background>
  </Step>
  <Step>
    Click **Save** to complete the creation process.
       
<Background>
![Saving new security scheme](https://api.apidog.com/api/v1/projects/544525/resources/353985/image-preview)
</Background>
  </Step>
  <Step>
    In the editing view of the security scheme, click **Advanced Configuration** at the bottom of the page.
   
<Background>
![Security scheme advanced configuration](https://api.apidog.com/api/v1/projects/544525/resources/353986/image-preview)
</Background>
      
   The system will display the OAS (OpenAPI Specification) code for the current security scheme, available in both JSON and YAML formats.

<Background>
![Security scheme OAS code](https://api.apidog.com/api/v1/projects/544525/resources/353988/image-preview)
</Background>

   You can directly edit here to define more complex specifications. The system will update the security scheme settings based on your changes.
  </Step>
</Steps>

## Creating Security Schemes via OAS Import

When importing an OpenAPI file that includes security schemes, Apidog will automatically detect and create corresponding security schemes. These will appear in the project's **Security Schemes** list.

You can configure the mapping between Security and Auth when importing OAS files.

<Background>
![Security scheme mapping during OAS import](https://api.apidog.com/api/v1/projects/544525/resources/366288/image-preview)
</Background>

## Creating OAuth 2.0 Security Scheme

OAuth 2.0 is a widely used authorization framework, and Apidog offers full support for it. To create an OAuth 2.0 security scheme, configure the following:

1. **Grant Type**: Choose from `Authorization Code`, `Client Credentials`, `Implicit`, or `Password`.
2. **URL Settings**: Based on the selected grant type, configure the relevant URLs:
   - **Auth URL**
   - **Access Token URL**
   - **Refresh URL** (optional)
   - **Callback URL** (also known as Redirect URL)
3. **Scope Settings** (Define the permission scopes your app can request):
   - Add scope names and descriptions
   - Configure different sets of scopes for each grant type
  
<Background>
![OAuth 2.0 settings](https://api.apidog.com/api/v1/projects/544525/resources/353999/image-preview)
</Background>

4. Click the **Test** button to open the test panel. Fill in the **Client ID**, **Client Secret**, and other required fields to test and verify your OAuth 2.0 configuration.

<Background>
![Testing OAuth 2.0 security scheme](https://api.apidog.com/api/v1/projects/544525/resources/354000/image-preview)
</Background>

