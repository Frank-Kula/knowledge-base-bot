# Pre/Post Processors in Apidog

Pre and post-processors are a key feature in Apidog. When you send a request, you can use pre-processors to dynamically control your request, or use post-processors to handle the received response.

Apidog provides a visual, drag-and-drop interface for pre and post-request operations, complementing traditional script-based approaches. This visual interface allows you to configure common operations without writing code, while still supporting custom scripts for advanced use cases.


## Quick Start
Here are the steps to use pre and post-processors in Apidog:

<Steps>
  <Step>
    Open any endpoint and navigate to the **Run** tab (Design-first Mode) or **Request** tab (Request-first mode).
    <Tabs>
      <Tab title="Design-first Mode">
        <Background>
          ![Pre/Post Processors in Design Mode](https://api.apidog.com/api/v1/projects/544525/resources/352194/image-preview)
        </Background>
      </Tab>
      <Tab title="Request-first Mode">
        <Background>
          ![Pre/Post Processors in Request Mode](https://api.apidog.com/api/v1/projects/544525/resources/352193/image-preview)
        </Background>
      </Tab>
    </Tabs>
  </Step>
  <Step>
    Switch to the **Pre Processors** or **Post Processors** section, hover over **+ Add**, and select the desired processor.
  </Step>
  <Step>
    Fill in the necessary fields for the added processor.
  </Step>
  <Step>
    Click **Send**, and the request will execute with the configured pre/post processors.
  </Step>
  <Step>
    In Design-first Mode, click **Save as case** to save the request. In Request-first Mode, click **Save** or **Save as case** to save the request.
    <Tabs>
      <Tab title="Design-first Mode">
        <Background>
          ![Save Case in Design Mode](https://api.apidog.com/api/v1/projects/544525/resources/352190/image-preview)
        </Background>
      </Tab>
      <Tab title="Request-first Mode">
        <Background>
          ![Save Request in Request Mode](https://api.apidog.com/api/v1/projects/544525/resources/352189/image-preview)
        </Background>
      </Tab>
    </Tabs>
  </Step>
</Steps>

:::tip
You can also create a standalone request and apply pre/post-processors to it. However, we recommend leveraging pre/post-processors on top of the endpoint specification to make debugging and testing more streamlined.
:::

## Capabilities

Pre and post processors can collectively achieve various functionalities:

### Pre Processors
*   **Request Parameter Setup**: Dynamically define input data for the API endpoint.
*   **Header Configuration**: Specify headers such as `Content-Type`, `Accept`, and `Authorization`.
*   **Authentication**: Add tokens, API keys, or credentials for protected endpoints.
*   **Database Integration**: Retrieve values from a database to use as request parameters.
*   **Encryption**: Secure the request payload before transmission.

### Post Processors
*   **Assertions**: Validate the received response against expected results (status codes, body content, etc.).
*   **Variable Extraction**: Extract values from the response to use in subsequent requests.
*   **Database Operations**: Write response data to a database for storage or updating.
*   **Data Visualization**: Generate reports or visual representations of the response data.

## Available Processors

Apidog supports the following pre/post processors:

| Processor | Type | Description |
| :--- | :--- | :--- |
| **[Assertion](https://docs.apidog.com/assertion-588467m0.md)** | Post | Define validation rules to check response data against expected values (status code, body, headers). |
| **[Extract Variable](https://docs.apidog.com/extract-variable-588468m0.md)** | Post | Extract values from the response (JSON, XML, Text) and store them as variables using JSONPath or XPath. |
| **[Database Operation](https://docs.apidog.com/database-operations-in-apidog-588469m0.md)** | Pre/Post | Connect to SQL/NoSQL databases to execute queries. Results can be stored as variables. |
| **[Custom Scripts](https://docs.apidog.com/use-scripts-in-apidog-593582m0.md)** | Pre/Post | Write custom JavaScript code to handle complex logic. Access request/response data and environment variables. |
| **[Public Scripts](https://docs.apidog.com/public-scripts-593613m0.md)** | Pre/Post | Create reusable script snippets shared across multiple processors or scenarios. |
| **[Wait](https://docs.apidog.com/wait-588474m0.md)** | Pre/Post | Introduce a delay before or after a request, useful for simulating real-world latency. |

:::highlight purple
We recommend using the **[Apidog Script Generator](https://app.anakin.ai/apps/21857)** to simplify script writing. Describe your logic in natural language, and the generator will create a runnable script for you.
:::

## Execution Order

Pre and post-processors can be configured at multiple levels:

1.  **Run/Endpoint Case Level** (Default): Affects only the current run/case.
2.  **Endpoint Level**: Applies to all cases associated with the endpoint.
3.  **Folder Level**: Impacts all endpoints within the folder.
4.  **Project Level**: Applies to all requests within the project (highest scope).

The execution flows from the highest level (Project/Folder) down to the specific Run/Case level.

### Visualizing Execution
A set of pre-processors in a request may look like this:

<Background>
  ![Pre-processor Execution Order](https://api.apidog.com/api/v1/projects/544525/resources/342813/image-preview)
</Background>

In the screenshot above:
*   The first three processors are grouped under **Inherit from parent**. They are defined in the Root folder, specific folders (e.g., "Pets"), or the endpoint itself.
*   These inherited processors are read-only in the current run but can be toggled on/off.
*   The last processor is a custom script added specifically for this run and can be edited directly.

### Variable Substitution
You may notice a step called **Variable Substitution & Inherit from Parents**. This special pre-processor replaces placeholders like `{{variable}}` with their actual values.

*   **Default Behavior**: Most pre-processors execute *before* variable substitution.
*   **Post-Substitution**: Some scripts (e.g., API signing) must run *after* variables are replaced. You can manually drag these processors below the "Variable Substitution" step.

### Complete Execution Flow
The detailed execution order for a single request is as follows:

<Background>
  <p style="text-align: center">
    <img src="https://api.apidog.com/api/v1/projects/544525/resources/342850/image-preview" style="width: 640px" />
  </p>
</Background>

