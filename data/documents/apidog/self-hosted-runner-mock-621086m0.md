# Self-Hosted Runner Mock

Runner mock provides a self-hosted mock service for teams requiring mock endpoints in private networks or intranets. When a request is made to a runner mock URL, the request is sent to your self-hosted runner server, which generates and returns the mock response.

## Prerequisites

Before configuring runner mock:
- A deployed runner on your server or intranet (see [deploying the Runner](https://docs.apidog.com/general-runner-755233m0.md))
- Team or project admin permissions
- Access to team resources settings

:::info[]
Runner mock is ideal for teams that need mock services in private networks or for large-scale automated testing scenarios.
:::

## Configuration Steps

### 1. Configure the Server Host

<Steps>
  <Step>
    Navigate to **Team Resources** → **General Runner**
  </Step>
  <Step>
    Locate your deployed runner
  </Step>
  <Step>
    Enter the **IP address** or **domain** of your runner server in the **Server Host** field
  </Step>
</Steps>

**Server Host Examples:**

<Tabs>
  <Tab title="Example 1">
   
    ```js
    https://runner.example.com:443
    ```
  </Tab>
  <Tab title="Example 2">

    ```js
    http://127.0.0.1:80
    ```
  </Tab>

</Tabs>

<Background>
![configure the server host.png](https://api.apidog.com/api/v1/projects/544525/resources/355210/image-preview)
</Background>

### 2. Verify the Runner Mock Environment

After configuration, confirm the runner mock environment is available:

<Steps>
  <Step>
    Navigate to **Environment Management** in your project
  </Step>
  <Step>
    Check that the **Runner Mock** environment appears in the list
  </Step>
</Steps>

If properly configured, the runner mock environment will be visible and selectable.

<Background>
![verify the Runner mock environment.png](https://api.apidog.com/api/v1/projects/544525/resources/355217/image-preview)
</Background>

### 3. Use the Runner Mock Environment

To send requests to your runner mock server:

<Steps>
  <Step>
    Open the endpoint you want to test
  </Step>
  <Step>
    Select the **Runner Mock** environment from the environment dropdown
  </Step>
  <Step>
    Send the request
  </Step>
</Steps>

The request will be routed to your runner server, which will return the generated mock response.

<Background>
![use the Runner mock environment.png](https://api.apidog.com/api/v1/projects/544525/resources/355220/image-preview)
</Background>

## FAQ

<Accordion title="Does Runner Mock support HTTPS? How can I enable it?" defaultOpen>

Yes, runner mock **can be accessed via HTTPS**, but note the following:

**Important Details:**
- The runner itself does **not include built-in HTTPS certificate support** or automatic certificate provisioning
- If your domain is already configured with HTTPS (e.g., via a reverse proxy like Nginx with a certificate), you can use it directly

**Configuration:**

Simply enter `https://your-domain:port` in the **Server Host** field to access the runner mock service over HTTPS. No additional runner configuration is needed.

**Example:**

 ```js
https://runner.example.com:443
```

<Frame>
<Background>
![image.png](https://api.apidog.com/api/v1/projects/544525/resources/353876/image-preview)
</Background>
</Frame>

</Accordion>

