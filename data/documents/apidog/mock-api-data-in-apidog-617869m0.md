# Mock API Data in Apidog

Apidog provides an efficient mock engine that automatically generates realistic API responses based on your API specifications. This powerful feature eliminates the need for manual configuration, accelerating development and testing workflows.

## Use Cases

Mock APIs are valuable in various development and testing scenarios:

| Scenario | Description | Benefit |
|----------|-------------|---------|
| **Parallel Development** | Frontend development when APIs are designed but not yet implemented | Frontend teams can proceed without waiting for backend completion |
| **Data Security** | Avoiding production data exposure during development | Maintains data privacy and security compliance |
| **Testing** | Creating test datasets for external dependencies | Ensures consistent and controlled test data |


## Getting Started

<Steps>
  <Step>
    Create an endpoint or import an API spec. The endpoint must have a specified response.
  </Step>
  <Step>
   Navigate to the **Mock** tab and click the mock URL to copy it. 
<Background>
![image.png](https://api.apidog.com/api/v1/projects/544525/resources/352100/image-preview)
</Background>
  </Step>
  <Step>
    Paste the URL in your browser to retrieve mock data. Refresh the page to generate new data.
<Background>
<img src="https://api.apidog.com/api/v1/projects/544525/resources/343580/image-preview" style="width: 440px" />
</Background>
  </Step>
</Steps>

## Mock Capabilities

Apidog's mock functionality supports various response types:

1. [Automatically generated data based on API specifications](https://docs.apidog.com/smart-mock-618190m0.md)
2. [Response examples from API specifications](https://docs.apidog.com/mock-priority-sequence-618208m0.md)
3. [Custom fixed responses](https://docs.apidog.com/custom-mock-618204m0.md)
4. [Conditional responses based on request parameters](https://docs.apidog.com/custom-mock-618204m0.md)
5. [Dynamic responses related to request parameters](https://docs.apidog.com/mock-scripts-618209m0.md)

## Mock Server Types

Apidog offers three mock server options to suit different development needs:

### Local Mock
Local mock runs on your computer alongside the Apidog client. It operates only when the client is open.

**Characteristics:**
- Installed automatically with Apidog client
- Starts when Apidog client launches
- Accessible only while client is running
- Cannot be disabled or removed from environments

**Best for:** Local frontend debugging and individual development

**Availability:** Apidog Client only (not available in Apidog Web)

:::info[]
Find the Local mock server URL in the environment management popup under "Local mock environment."
:::

### Cloud Mock
Cloud mock provides the same functionality as local mock but runs on Apidog's servers. It remains accessible regardless of whether your local machine is running.

**Characteristics:**
- Hosted on Apidog servers
- Available 24/7 from any location
- Supports encrypted access
- Can be toggled on/off as needed
- Off by default

**Best for:** Sandbox environments for public APIs and team collaboration

:::tip[]
Learn more about configuring and using [Cloud mock](https://docs.apidog.com/cloud-mock-621066m0.md).
:::

### Runner Mock
Runner mock operates on your team's self-hosted runner infrastructure. After deploying a runner on your server, all team members can access mock data through it.

**Characteristics:**
- Self-hosted on your infrastructure
- Available independently of local machines
- Shared across all team members

**Best for:** Large-scale automated testing and sandbox environments for internal/private APIs

:::tip[]
Learn more about setting up [Self-hosted runner mock](https://docs.apidog.com/self-hosted-runner-mock-621086m0.md).
:::

## Accessing Mock Servers

You can access mock data through two primary methods:

### URL Access
Every HTTP endpoint in Apidog includes a **Mock** module:
- In **DESIGN** mode: Found in the **API** tab
- In **DEBUG** mode: Found in the **Mock** tab

From this module, you can copy the mock URL and use it in any application or tool to request mock data.

:::info[Multiple Responses]
If an endpoint defines multiple responses or mock expectations, each will have its own unique mock URL.
:::

<Background>
![image.png](https://api.apidog.com/api/v1/projects/544525/resources/343588/image-preview)
</Background>

You can click **Request** to test the mock URL directly within Apidog.

:::caution[]
The **Click to copy** button copies only the URL. You must manually add the HTTP method and request body when using the URL elsewhere.
:::

### Accessing Mock Within Apidog

Each Apidog project includes Local mock and Cloud mock environments in the environment switcher (top right corner).

When you select a mock environment, all requests in Apidog are automatically routed to that mock server.

:::warning[Path Requirements]
Only endpoints with paths starting with `/` will be sent to the mock environment. Endpoints with complete URLs (not starting with `/`) will not use the mock environment.
:::

