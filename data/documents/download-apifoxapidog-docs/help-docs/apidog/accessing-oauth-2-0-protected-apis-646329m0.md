# Accessing OAuth 2.0 Protected APIs

OAuth 2.0 is an authorization framework that allows users to grant third-party applications permission to access services on their behalf, eliminating the need for repetitive credential entry while ensuring security and flexibility.

This guide demonstrates how to debug OAuth 2.0 APIs using Apidog, with Google account sign-in as a practical example.

## Understanding the OAuth 2.0 Flow

In a typical OAuth 2.0 scenario:
- **Client**: Your website or application
- **Authorization Server**: The service providing authentication (e.g., Google)
- **Resource Server**: The service hosting protected resources

## Prerequisites

Before testing OAuth 2.0 APIs, ensure you have:

- An OAuth client registered with the authorization server (e.g., Google API Console Project)
- Client ID and client secret credentials
- Configured redirect URIs

:::tip[]
If you haven't registered a Google API Console Project, refer to the [official documentation](https://support.google.com/cloud/answer/6158849?hl=en) to create a new OAuth client.
:::

## OAuth 2.0 Authorization Flow

### Step 1: Request User Authorization

When a user clicks the "Sign in with Google" button, your website sends a request to Google's OAuth 2.0 authorization server to obtain permission to access the user's Google account.

<Background>
![Sign in with Google button](https://assets.apidog.com/uploads/help/2024/02/01/f93d59b83923adf0f5c3de485a418d9f.png)
</Background>

The authorization request is sent to `https://accounts.google.com/o/oauth2/v2/auth/` with the following parameters:

| Parameter | Required | Description |
|-----------|----------|-------------|
| `client_id` | **Required** | The client ID for your application from the API Console Credentials page |
| `redirect_uri` | **Required** | Where the API server redirects the user after authorization. Must exactly match one of the authorized redirect URIs in your OAuth 2.0 client configuration |
| `response_type` | **Required** | Set to `code` for web server applications to receive an authorization code |
| `scope` | **Required** | Space-delimited list of scopes identifying the resources your application can access on the user's behalf |
| `access_type` | Recommended | `online` (default) or `offline`. Use `offline` if your application needs to refresh access tokens when the user is not present |
| `state` | Recommended | Any string value to maintain state between your authorization request and the authorization server's response |

:::info[]
This table shows the basic parameters required by Google OAuth 2.0. Many other optional parameters are available to customize the user experience and security. See the [official documentation](https://developers.google.com/identity/protocols/oauth2/web-server) for complete details.
:::

### Step 2: User Grants Authorization

Google presents a consent screen requesting permission to access the specified resources. 

<Background>
<img src="https://assets.apidog.com/uploads/help/2024/02/01/9985f92060d76557702e6f38dd703e4c.png" style="width: 700px" />
</Background>

**Possible outcomes:**
- **User approves**: Google sends an authorization token to your web server
- **User denies**: Google sends an error message to your web server

### Step 3: Exchange Authorization Code for Access Token

After the user grants permission, the authorization code is included in the response. The response appears in the query string:

```url
# Error response
http://example.com/#error=access_denied&state=state_parameter_passthrough_value

# Success response
http://example.com/#state=state_parameter_passthrough_value&access_token=***&token_type=Bearer&expires_in=***&scope=email%20https://www.googleapis.com/auth/userinfo.email%20openid&authuser=0&prompt=consent
```

Extract the access token from the URL to use with other Google API services.

### Step 4: Access Protected Resources

Using the Openidconnect API as an example, you can access the user's Google account information by sending a request with the access token.

**Testing in Apidog:**

1. Create a new request in your Apidog project
2. Use the URL: `https://openidconnect.googleapis.com/v1/userinfo?access_token=ACCESS_TOKEN`
3. Replace `ACCESS_TOKEN` with your actual token
4. Click **Send**

<Background>
![Sending request with access token in Apidog](https://assets.apidog.com/uploads/help/2024/02/02/da83643979f78c194c87555045556b51.png)
</Background>

### Step 5: Receive User Information

Google verifies the access token's validity and determines the associated authorized client.

**Possible outcomes:**
- **Valid token**: Google responds with the user's information
- **Invalid/expired token**: Google responds with an error message

<Background>
![Successful response with user information](https://assets.apidog.com/uploads/help/2024/02/02/7686ad0670029db2874b7cab69660a5e.png)
</Background>

The API response is a JSON object containing the user's Google account information, such as `picture` and `email`. Your website can use this data to automatically display the user's profile without manual entry.

## Benefits of Using Apidog for OAuth 2.0 Testing

Using Apidog to debug OAuth 2.0 APIs provides:

- **Clear visibility** into parameters required by upstream and downstream processes
- **Optimized development experience** with visual parameter management
- **Workflow validation** before writing code
- **Reduced debugging time** during implementation

Once the complete workflow is successfully executed in Apidog, backend developers can confidently write code to complete the business process without needing to verify while developing.

## References

- [Google OAuth 2.0 Documentation](https://developers.google.com/identity/protocols/oauth2)

<details>
<summary>📄 Example Web Page Source Code</summary>

**HTML:**

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>OAuth OAuth Login Demo Websites</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to CSS file -->
</head>

<body>
    <h1>Welcome to OAuth Login Demo Websites</h1>
    <button id="signinButton">Sign in with Google</button>

    <script src="main.js"></script> <!-- Link to JavaScript file -->

</body>
</html>
```

**JavaScript:**

```javascript
document.getElementById('signinButton').addEventListener('click', function() {
  var oauth2Endpoint = 'https://accounts.google.com/o/oauth2/v2/auth';

  var client_id = 'your_client_id';
  var redirect_uri = 'http://localhost:5500/';
  var scope = 'email';
  var state = 'state_parameter_passthrough_value';
  var response_type = 'token';

  var authUrl = `${oauth2Endpoint}?response_type=${encodeURIComponent(response_type)}&client_id=${encodeURIComponent(client_id)}&redirect_uri=${encodeURIComponent(redirect_uri)}&scope=${encodeURIComponent(scope)}&state=${encodeURIComponent(state)}`;

  window.location = authUrl; // Redirect to Google OAuth 2.0 authorization page

});
```

</details>

