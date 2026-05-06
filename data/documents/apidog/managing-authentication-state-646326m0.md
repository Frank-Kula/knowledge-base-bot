# Managing Authentication State

Authentication is a crucial aspect of API testing and development. Properly managing authentication state ensures that your API requests are secure, efficient, and accurately reflect real-world usage scenarios.

This guide demonstrates how to effectively handle authentication state in Apidog, covering common authentication methods and automatic login implementation.

## Common Authentication Methods

### 1. Session/Cookie Authentication

Apidog automatically maintains authentication state through sessions and cookies.

**How it works:**
- Upon execution of the login API, Apidog saves the returned Session/Cookie information globally
- Subsequent API calls automatically include this Session/Cookie information
- No manual configuration required for each request

:::tip[]
See the [Auto-Login Implementation](#auto-login-implementation) section for details on achieving automatic login via Session/Cookie.
:::

### 2. Token-Based Authentication

Token-based authentication involves including login credentials in API request parameters, typically in the Header. Common approaches include Basic Auth, Bearer Token, and API Key.

**Implementation options:**

#### Option 1: Configure Authentication Globally

Set authentication information at different levels:
- **Project level**: Project overview page
- **Group level**: Group settings
- **Individual API level**: Documentation page

<Background>
<img src="https://api.apidog.com/api/v1/projects/544525/resources/349751/image-preview" style="width: 640px" />
</Background>

**Supported authentication types:**
- Basic Auth
- Bearer Token
- API Key
- OAuth 2.0
- And more

#### Option 2: Manual Token Configuration

Manually add the token to the Header or other relevant parameters. We recommend using environment variables for token storage.

**Examples:**
- **Bearer Token**: Set a Header named `Authorization` with the value `Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9yJpZCI6`
- **Using environment variables**: `Bearer {{AUTH_TOKEN}}`

#### Option 3: Global Parameters

Set the value in global parameters. All APIs will automatically include global parameters during runtime, eliminating the need for manual configuration per API.

:::tip[]
Refer to the [Auto-Login Implementation](#auto-login-implementation) section for details on achieving automatic login via tokens.
:::

### 3. Automatic Login Method

This method automatically invokes the login API to complete authentication without manual intervention, maintaining authentication state across requests.

## Auto-Login Implementation

### Desired Outcome

1. **Automatic invocation** of the login API without manual intervention
2. **Preservation of authentication state** after successful login to avoid redundant login API calls
3. **Token refresh** when credentials expire

### Implementation Steps

**Step 1: Set up environment variables**

Use environment variables to store authentication credentials:
- `ACCESS_TOKEN`: Stores login credentials
- `ACCESS_TOKEN_EXPIRES`: Stores expiration time (if applicable)

**Step 2: Create a public script**

The script should:
1. Check if `ACCESS_TOKEN` has a value and if `ACCESS_TOKEN_EXPIRES` is still valid
   - If valid, proceed with the request
   - If invalid or missing, continue to the next step
2. Use `pm.sendRequest` to call the login API
3. Write the returned credentials and expiration time to environment variables

**Step 3: Configure APIs requiring authentication**

For each API that requires authentication:

1. **Set the authentication parameter** to `{{ACCESS_TOKEN}}`
   - Set the `Authorization` header to `{{ACCESS_TOKEN}}`
   - Or use cookies/other parameters as needed
   - Alternatively, set the value in global parameters for automatic inclusion in all API calls

2. **Reference the public script** in the preprocessor script

### Public Script Example

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

:::warning[]
**Important notes:**
- The login credentials in this script are sourced from `LOGIN_USERNAME` and `LOGIN_PASSWORD` environment variables. Ensure these are set before using this code.
- If your token doesn't expire, remove `ACCESS_TOKEN_EXPIRES`-related code.
- Adjust the login request structure and response handling according to your specific API requirements.
:::

### Additional Resources

- [`pm.sendRequest` documentation](https://docs.apidog.com/postman-scripts-reference-593586m0.md#pmsendrequest)
- [`pm.cookies` documentation](https://docs.apidog.com/postman-scripts-reference-593586m0.md#pmcookies)
