# Environment Management

When making API requests, it is often necessary to switch between development, testing, and production environments. Apidog makes it convenient to send requests to different environments—you simply need to click and select the desired environment at the top right corner of the interface.

An Apidog environment consists of two core elements:
1.  **Base URL**: Maintains the target of request delivery.
2.  **Variables**: Groups of variables that can be referenced in requests or scripts.

When switching between environments, both the base URL and environment variables will use the values defined in the current environment.

## Create an Environment

<Steps>
  <Step>
    **Open Environment Management**
    
    Click on the **Environment Management** button `≡` in the top right corner of the interface.
  </Step>
  <Step>
    **Create New Environment**
    
    Click on the last item in the left-side list labeled **New Environment**.
  </Step>
  <Step>
    **Configure Environment**
    
    Enter a name for your new environment. Add the Base URL and variables.
      
<Background>
![Create environment](https://api.apidog.com/api/v1/projects/544525/resources/358404/image-preview)
</Background>
  </Step>
  <Step>
    **Save**
    
    Click **Save**.
  </Step>
  <Step>
    **Select Environment**
    
    To use the new environment, select it from the environment selector at the top right of the interface. This makes it the active environment and sets all variables to the values specified in the environment.
  </Step>
</Steps>

:::tip
Apidog maintains a clear separation between environments and base URLs. Environments represent different deployment stages (development, testing, production), while base URLs are configured within each environment. This separation provides flexibility when managing multiple services or micro-services across different environments.

In contrast, Apidog's environments directly reflect real environments like development, testing, and production, rather than treating each base URL as a single environment.
:::

## Base URLs

The **Base URL** is the primary feature in an Apidog environment. In Apidog, an endpoint path usually starts with a forward slash (`/`) and does not include the base URL. When sending a request, Apidog prepends the destination Base URL to the endpoint path.

A standardized Base URL format begins with the protocol and excludes the trailing slash (`/`).

**Examples:**
*   `https://127.0.0.1`
*   `http://abc.com/v1`

Each Base URL corresponds to a specific [Module](https://docs.apidog.com/module-1261913m0.md). In most cases, an endpoint will use the Base URL of its module to send requests.

For instance, if the **Base URL** of the default module for the **Production** environment is `http://abc.com/v1` and your endpoint path is `/pet`, then when you send a request in the Production environment, the actual request URL sent would be:

```
http://abc.com/v1/pet
```

:::tip
If the endpoint path begins with `http://` or `https://`, the Base URL will not be appended. However, hardcoding full URLs in endpoints is generally discouraged.
:::

:::tip[BASE_URL variable]
In Apidog, there is a special environment variable called `BASE_URL` which stores the Base URL for the "Default Server" of the current environment. It is generally discouraged to use this variable directly.

For custom scripts:
*   **Recommended**: Use `pm.request.getBaseUrl()` to fetch the Base URL for the current endpoint.
*   **Avoid**: Using `pm.environment.get('BASE_URL')`, as it may not correctly capture the Base URL if the endpoint does not occupy the "Default Server".

If you manually create an environment variable labeled `BASE_URL`, it will supersede the system's predefined `BASE_URL`.

**Note**: Scripts cannot modify the Base URL configuration itself. The command `pm.environment.set('BASE_URL', 'My_url')` will only create a variable named `BASE_URL`.
:::

## Using Multiple Base URLs with Modules

If your project’s endpoints need to connect to multiple Base URLs (e.g., microservices), the best way to manage them is by using multiple [Modules](https://docs.apidog.com/module-1261913m0.md) in Apidog.

**Example Scenario:**
*   User endpoints: `https://user.example.com`
*   Order endpoints: `https://order.example.com`
*   Product endpoints: `https://product.example.com`

**Setup Steps:**

<Steps>
  <Step>
    **Create Modules**
    
    At the top of the API folder tree, add multiple modules corresponding to your services.

<Background>
![Add modules](https://api.apidog.com/api/v1/projects/544525/resources/358484/image-preview)
</Background>
  </Step>
  <Step>
    **Configure Base URLs**
    
    In **Environment Management**, you’ll see fields to set the **Base URL** for each module. Enter the URLs for each environment and click **Save**.

<Background>
![Configure module base URLs](https://api.apidog.com/api/v1/projects/544525/resources/358405/image-preview)
</Background>
  </Step>
  <Step>
    **Set Module Base URL**
    
    In a module’s **root folder** settings, choose which Base URL the module’s endpoints should use.
    *   **Default Settings**: Uses the first Base URL listed for that module (Recommended).
    *   **Manually Specify**: Select another Base URL manually. (Not recommended for most cases).

<Background>
![Module folder settings](https://api.apidog.com/api/v1/projects/544525/resources/358134/image-preview)
</Background>
  </Step>
  <Step>
    **Inheritance**
    
    In subfolders or individual endpoints, you can also specify the Base URL.
    *   **Inherit from Parents**: Follows the parent folder (Default).
    *   **Manually Specify**: Override for specific items.

<Background>
![Endpoint settings](https://api.apidog.com/api/v1/projects/544525/resources/358135/image-preview)
</Background>
  </Step>
  <Step>
    **Send Requests**
    
    Once set up, just click **Send**. Apidog determines the proper Base URL based on module and environment settings.
  </Step>
</Steps>

## Add Environment Variables

When you add a variable to an environment, you can specify two values:
*   **Initial value**: Shared with the team.
*   **Current value**: Stored locally on your machine.

:::tip[]
Learn more about [Using Variables](https://docs.apidog.com/using-variables-577908m0.md).
:::

## Switch Between Environments

Apidog shows the current environment in the environment selector at the top right of the workbench. Whenever you make a request or execute a script, Apidog will use the current values for all variables in the selected environment.

To switch, simply choose a different environment from the selector.

<Background>
<p style="text-align: center">
    <img src="https://api.apidog.com/api/v1/projects/544525/resources/342800/image-preview" style="width: 340px" />
</p>
</Background>

:::tip
**Endpoints vs. Requests**

In Apidog:
*   **Endpoint**: The API specification (path usually starts with `/`).
*   **Request**: The actual HTTP request sent (includes the full URL).

The services defined in an Environment apply to *Endpoints*. When using the *Request* tab for ad-hoc debugging (similar to Postman), you can use the `{{Base_url}}` syntax if needed.
:::

## Environment Migration

In Apidog, the **Initial value** of variables is synchronized within the team, while the **Current value** is only stored locally. This means current values do not carry over to other devices.

Apidog provides export/import functionality to migrate environments (including local current values) between machines.

<Steps>
  <Step>
    **Export**
    
    In Environment Management, hover over the `...` next to the environment, click **Export** to get a JSON file.
<Background>
<p style="text-align: center">
    <img src="https://api.apidog.com/api/v1/projects/544525/resources/342803/image-preview" style="width: 540px" />
</p>
</Background>
  </Step>
  <Step>
    **Import**
    
    On the target computer, open Environment Management, hover over `...`, click **Import**, and select the JSON file.
  </Step>
</Steps>

## Visibility Scope of Environments

You can create **Private Environments** for variables you don't want to share.

In the top right corner of the environment settings, set the visibility scope.
*   **Shared**: Visible to the team (Default).
*   **Private**: Visible only to you.

<Background>
<p style="text-align: center">
    <img src="https://api.apidog.com/api/v1/projects/544525/resources/342804/image-preview" style="width: 340px" />
</p>
</Background>

:::tip
Private Environments share the same **Service list** (Base URLs) as other environments. Adding or removing services in a Private Environment will affect all environments simultaneously.
:::

## FAQ

**How to get service Base URL in a custom script?**

Use `pm.request.getBaseUrl()` to retrieve the Base URL of the current endpoint.

