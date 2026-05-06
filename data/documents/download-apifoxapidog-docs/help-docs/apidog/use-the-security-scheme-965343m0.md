# Use the Security Scheme

## Configuring Security Schemes at the Folder Level

<Steps>
  <Step>
   Select any folder, click the **Auth** tab on the right, and choose **Security Scheme** as the authentication type.
      
<Background>
![Choosing security scheme auth type](https://api.apidog.com/api/v1/projects/544525/resources/354019/image-preview)
</Background>
  </Step>
  <Step>
  Select the desired **Security Scheme** from the dropdown menu.
      
<Background>
![Selecting desired security scheme](https://api.apidog.com/api/v1/projects/544525/resources/354020/image-preview)
</Background>
  </Step>
  <Step>
  If you choose OAuth 2.0 as the security scheme, you can further select the required **Scopes**.
      
<Background>
![Selecting security scheme scope](https://api.apidog.com/api/v1/projects/544525/resources/354021/image-preview)
</Background>
  </Step>
</Steps>

Security schemes configured at the folder level will apply to all subfolders and endpoints under that folder, unless they have their own auth configuration.

## Configuring Security Schemes at the Endpoint Level

<Steps>
  <Step>
  Select any endpoint and go to the **Edit** tab on the right. At the **Request** section, choose **Security Scheme** as the authorization type.
      
<Background>
![Configuring security scheme at endpoint level](https://api.apidog.com/api/v1/projects/544525/resources/354024/image-preview)
</Background>
  </Step>
  <Step>
    Select the desired **Security Scheme** from the dropdown menu.
      
<Background>
![Selecting desired security scheme for endpoint](https://api.apidog.com/api/v1/projects/544525/resources/354023/image-preview)
</Background>
  </Step>
  <Step>
  If you choose OAuth 2.0 as the security scheme, you can further select the required **Scopes**.

<Background>
![Selecting endpoint security scheme scope](https://api.apidog.com/api/v1/projects/544525/resources/354025/image-preview)
</Background>
  </Step>
</Steps>

Auth settings configured at the endpoint level will override those at the folder level.

## Setting Default Values for Security Scheme

Security scheme only define the auth method. You still need to provide actual auth values when debugging endpoints.

To avoid repeatedly filling in auth values during endpoint debugging, Apidog allows you to set default auth values. Once set, these defaults are used automatically during debugging, unless manually overridden. If a folder has default auth values configured, all endpoints under it can use them.

<Steps>
  <Step>
        Choose a security scheme from the list and set a **Default Auth Values**.

<Background>
![Default auth value](https://api.apidog.com/api/v1/projects/544525/resources/354028/image-preview)
</Background>
  </Step>
  <Step>
   Fill in values based on the authentication type:

   - **API Key**: Enter your key
   - **Basic Auth**: Enter username and password
   - **Bearer Token**: Enter the token
   - **OAuth 2.0**: Enter client ID, client secret, etc.
   - **Other methods**: Fill in corresponding values
  </Step>
</Steps>

## Inheriting & Customizing Auth Values

When using security scheme, you can either:

### 1. Inherit from Parent Folder

Use the security scheme and default values defined in the parent or root folder.

<Background>
![Inherit security scheme](https://api.apidog.com/api/v1/projects/544525/resources/354030/image-preview)
</Background>

### 2. Customize Auth Values

Keep the same security scheme, but override its default values.

<Background>
![Customize security scheme](https://api.apidog.com/api/v1/projects/544525/resources/354038/image-preview)
</Background>

## Using Multiple Security Schemes

Apidog supports configuring multiple security schemes for a single endpoint, which aligns with the multiple authentication types mechanisms defined in the OpenAPI spec:

- **AND**: Security schemes combined via **AND** must be used simultaneously in the same request (coming soon).
- **OR**: Security schemes combined via **OR** are alternatives – any one can be used in the given context.

Use the **+** button in the **Auth** settings to add more security schemes.

<Background>
![Add multiple security schemes](https://api.apidog.com/api/v1/projects/544525/resources/354040/image-preview)
</Background>

## Choosing Scopes for OAuth 2.0 Security Scheme

According to the OpenAPI spec, when creating an OAuth 2.0 security scheme, all possible **Scopes** should be defined. When using it in an endpoint, you must select the required scopes.

To make things easier, Apidog allows you to set default scopes at the folder level. These defaults will apply to all endpoints in the folder — unless you manually set different scopes at the endpoint level.

<Steps>
  <Step>
    In the endpoint's **Auth** settings, select OAuth 2.0.
  </Step>
  <Step>
    Under the **Scopes** section, you can view all available scopes defined by the security scheme and select the ones needed.

<Background>
![Choose auth scopes at endpoint level](https://api.apidog.com/api/v1/projects/544525/resources/354041/image-preview)
</Background>     
  </Step>
  <Step>
    If the endpoint inherits scopes from a parent folder, you can click **Reset the scopes to the configuration of the parent folder** to revert to the parent configuration.
      
<Background>
![Reset scope settings](https://api.apidog.com/api/v1/projects/544525/resources/354042/image-preview)
</Background>        
  </Step>
</Steps>

## Debugging Endpoints with OAuth 2.0 Security Scheme

You can pre-configure a token as the default value for OAuth 2.0 security scheme, so you don't need to obtain a new token every time you debug an API.

### Getting Token at the Folder Level as the Default Auth Value

<Steps>
  <Step>
  Select a folder, go to the **Auth** tab, choose an OAuth 2.0 security scheme, select scopes and grant type, then click **Get Token**.
      
<Background>
![Get OAuth 2.0 token at folder level](https://api.apidog.com/api/v1/projects/544525/resources/354043/image-preview)
</Background>
  </Step>
  <Step>
    In the pop-up panel:
    
    - Enter the client ID, client secret, etc.
    - Click **Continue**
      
<Background>
![Test OAuth 2.0 token security scheme](https://api.apidog.com/api/v1/projects/544525/resources/354044/image-preview)
</Background>
  </Step>
  <Step>
After getting the token, you can view its details, including when it expires. This token can be used across all endpoints in the folder.
      
<Background>
![View token details in folder](https://api.apidog.com/api/v1/projects/544525/resources/354052/image-preview)
</Background>
  </Step>
</Steps>

### Getting Token at the Endpoint Level as the Default Auth Value

<Steps>
  <Step>
   Select the desired endpoint, go to **Edit**, choose an OAuth 2.0 security scheme, and click **Get Token**.
      
<Background>
![Get token at endpoint level](https://api.apidog.com/api/v1/projects/544525/resources/354047/image-preview)
</Background>
  </Step>
  <Step>
   In the pop-up panel:
   
   - Enter the client ID, client secret, etc.
   - Click **Continue**
    
<Background>
![Test OAuth 2.0 token security scheme at endpoint level](https://api.apidog.com/api/v1/projects/544525/resources/354048/image-preview)
</Background>
  </Step>
  <Step>
    - Complete the authorization to get a token
    - The token will be used for debugging this endpoint
    
<Background>
![View token details](https://api.apidog.com/api/v1/projects/544525/resources/354051/image-preview)
</Background>
  </Step>
</Steps>

### Using a Default Token or Generating a New One for Endpoint Debugging

When debugging an endpoint in Apidog, you have two options to apply an auth token:

#### Method 1: Use a Default Auth Token

When running an endpoint, go to the **Auth** tab under the **Run** panel. Select **Use Parent Default Auth Values**. The default auth token configured in the parent folder will be automatically applied to the endpoint request.

<Background>
![Use a default auth token for endpoint debugging](https://api.apidog.com/api/v1/projects/544525/resources/354053/image-preview)
</Background>

#### Method 2: Generate a New Token

<Steps>
  <Step>
When running an endpoint, go to the **Auth** tab under the **Run** panel. Select **Set Manually**. Click **Get Token** to open the token generation panel.

<Background>
![Generate a new token for endpoint debugging](https://api.apidog.com/api/v1/projects/544525/resources/354057/image-preview)
</Background>
  </Step>
  <Step>
   In the pop-up panel:
   
   - Enter the client ID, client secret, etc.
   - Click **Continue**
    
<Background>
![Fill information for generating new token](https://api.apidog.com/api/v1/projects/544525/resources/354058/image-preview)
</Background>
  </Step>
  <Step>
    - Complete the authorization to get a token
    - The token will be used for debugging the current endpoint
  </Step>
</Steps>

