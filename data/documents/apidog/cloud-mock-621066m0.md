# Cloud Mock

Cloud mock provides a continuously available mock endpoint that persists independently of individual machines. Unlike local mocks, which run on a user's computer and become unavailable when shut down, cloud mocks offer a persistent solution ideal for team collaboration and continuous access.

## Key Benefits

Cloud mock is essential for teams requiring reliable, always-on mock endpoints:

| Benefit | Description |
|---------|-------------|
| **Team-wide Accessibility** | All team members share the same cloud mock URL |
| **24/7 Availability** | Accessible regardless of individual computer status |
| **Public API Sandbox** | Ideal for public-facing API documentation |
| **Non-production Data Source** | Provides reliable test data for development environments |


## Enabling Cloud Mock

<Steps>
  <Step>
    Navigate to **Project Settings**
  </Step>
  <Step>
    Select **Mock Settings**
  </Step>
  <Step>
    Toggle on **Cloud Mock**
  </Step>
</Steps>

<Background>
![image.png](https://api.apidog.com/api/v1/projects/544525/resources/343629/image-preview)
</Background>

## Using Cloud Mock

Once enabled, access cloud mock through multiple methods:

### Copying the Cloud Mock URL

<Steps>
  <Step>
    Open the desired endpoint
  </Step>
  <Step>
    Navigate to the **Mock** tab
  </Step>
  <Step>
    Click the **Cloud Mock** button to copy the URL
  </Step>
</Steps>

### Testing Immediately

Use the **Request** button to instantly retrieve mock response data within Apidog.

### Browser Access

For GET requests, paste the cloud mock URL directly into a web browser to view the response data.

## Implementing Access Control

Secure your cloud mock endpoints with token-based authentication:

### Configuring Token Authentication

<Steps>
  <Step>
    Go to **Project Settings** → **Mock Settings**
  </Step>
  <Step>
    Set access permission to **Token Authentication**
  </Step>
</Steps>

### Using Authenticated Endpoints

Once token authentication is enabled, include the token with requests:

**URL Parameter Method:**

Append the `apidogToken` parameter to the request URL:

```
https://mock.apidog.com/m1/2689726-0-default/users?apidogToken=GdfNrEm6lxM9nDGGIMCWC1OPSiZ6hGOi
```

**Header Parameter Method:**

For Quick Requests, add the `apidogToken` parameter to the request headers.

**Body Parameter Method:**

For form-data and x-www-form-urlencoded requests, include the `apidogToken` parameter in the request body.

## Summary

Cloud mock streamlines API development by providing:
- Consistent, always-available mock endpoints
- Enhanced team collaboration with shared URLs
- Flexible access control for security
- Reliable data sources for non-production environments

By implementing cloud mock, teams ensure uninterrupted access to test data, improved documentation experiences, and seamless collaboration across distributed teams.

