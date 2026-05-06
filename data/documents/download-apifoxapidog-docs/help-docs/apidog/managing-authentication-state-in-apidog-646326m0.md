# Managing authentication state in Apidog

Authentication is a crucial aspect of API testing and development. Properly managing authentication state ensures that your API requests are secure, efficient, and accurately reflect real-world usage scenarios. This guide focuses on handling authentication state in Apidog, a powerful API development and testing platform.

This guide will help you effectively handle authentication state within Apidog.

## Common Authentication Methods

### 1. Session/Cookie Method

Apidog automatically maintains authentication state through sessions and cookies.

Usage:
- Upon execution of the login API, the global Cookie saves the returned Session/Cookie information.
- Subsequent API calls automatically include this Session/Cookie information.

:::tip
See the "Auto-Login Implementation" section below for details on achieving automatic login via Session/Cookie.
:::

### 2. Token-Based Authentication

Token-based authentication involves including login credentials in API request parameters (typically in the Header). Common approaches include Basic Auth, Bearer Token, and API Key.

Implementation options:

1. Set authentication information globally (project overview page), at the group level (group settings), or for individual APIs (documentation page). Supported auth types are shown below:

   
    <Background>
    <img src="https://api.apidog.com/api/v1/projects/544525/resources/349751/image-preview" width="640px"/>
    </Background>


2. Manually add the token to the Header or other relevant parameters. We recommend using environment variables for token storage. For example:
   - Bearer Token: Set a Header named `Authorization` with the value `Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9yJpZCI6`, or use an environment variable: `Bearer {{AUTH_TOKEN}}`.

3. Set the value in global parameters. All APIs will automatically include global parameters during runtime, eliminating the need for manual configuration per API.

:::tip
Refer to the "Auto-Login Implementation" section for details on achieving automatic login via tokens.
:::

### 3. Automatic Login Method

This method automatically invokes the login API to complete authentication without manual intervention.

## Auto-Login Implementation

### Desired Outcome

1. Automatic invocation of the login API without manual intervention.
2. Preservation of authentication state after successful login to avoid redundant login API calls.

### Step-by-Step Guide

1. Use an environment variable (e.g., `ACCESS_TOKEN`) to store login credentials.
2. If credentials have an expiration time, use an environment variable (e.g., `ACCESS_TOKEN_EXPIRES`) to store this information.
3. Create a public script that:
   a. Checks if `ACCESS_TOKEN` has a value and if `ACCESS_TOKEN_EXPIRES` is still valid. If so, proceed to execution; otherwise, continue to the next step.
   b. Uses `pm.sendRequest` to call the login API and write the returned credentials and expiration time to the environment variables.
4. Configure APIs requiring authentication:
   a. Set the auth verification parameter to `{{ACCESS_TOKEN}}`.
      - Set the `Authorization` header to `{{ACCESS_TOKEN}}`, or use cookies/other parameters as needed.
      - Alternatively, set the value in global parameters for automatic inclusion in all API calls.
   b. Reference the public script created above in the preprocessor script.

### Public Script Example

:::tip
- The login credentials in this script are sourced from `LOGIN_USERNAME` and `LOGIN_PASSWORD` environment variables. Ensure these are set if you use this code.
- If your token doesn't expire, remove `ACCESS_TOKEN_EXPIRES`-related code.
- For `pm.sendrequest` documentation, [click here](https://docs.apidog.com/postman-scripts-reference-593586m0#pmsendrequest).
- For `pm.cookies` documentation, [click here](https://docs.apidog.com/postman-scripts-reference-593586m0#pmcookies).
:::

```javascript
function sendLoginRequest() {
  const baseUrl = pm.request.getBaseUrl();
  const username = pm.environment.get("LOGIN_USERNAME");
  const password = pm.environment.get("LOGIN_PASSWORD");

  const loginRequest = {
    url: baseUrl + "/api/v1/login",
    method: "POST",
    body: {
      mode: "urlencoded",
      urlencoded: [
        { key: "account", value: username },
        { key: "password", value: password },
      ],
    },
  };

  pm.sendRequest(loginRequest, function(err, res) {
    if (err) {
      console.error("Login request failed:", err);
    } else {
      const jsonData = res.json();
      pm.environment.set("ACCESS_TOKEN", jsonData.data.accessToken);
      pm.environment.set("ACCESS_TOKEN_EXPIRES", jsonData.data.accessTokenExpires);
    }
  });
}

const accessToken = pm.environment.get("ACCESS_TOKEN");
const accessTokenExpires = pm.environment.get("ACCESS_TOKEN_EXPIRES");

if (!accessToken || (accessTokenExpires && new Date(accessTokenExpires) <= new Date())) {
  sendLoginRequest();
}
```

This script provides a robust foundation for implementing auto-login in Apidog. Remember to adjust the login request structure and response handling according to your specific API requirements.
