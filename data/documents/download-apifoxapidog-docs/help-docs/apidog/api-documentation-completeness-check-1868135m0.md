# API Documentation Completeness Check

:::info
See [Getting Started with AI Features](https://docs.apidog.com/overview-of-ai-features-in-apidog-1225682m0.md#getting-started-with-ai-features) for setup requirements. Note: This feature requires Apidog version **2.7.55 or later**.
:::

## Overview

You can use AI to run an `API Documentation Completeness Check` on your current API documentation and generate a detailed review report. Based on this report, you can refine and improve your documentation — making collaboration smoother, the docs easier to read, and all AI features more effective thanks to more accurate endpoint specs.

## What Is Checked

Before running the `API Documentation Completeness Check`, it's helpful to review whether the descriptions and definitions in the current API documentation are complete. The check analyzes the following aspects:

### 1. Basic Definitions

Check whether the endpoint documentation clearly and accurately specifies:

| Element | Purpose |
|---------|---------|
| **Request Method** | Defines the HTTP method (GET, POST, PUT, DELETE) to determine request semantics, idempotency, and parameter structure |
| **Request Path** | The full URL path (excluding base URL) to uniquely identify the endpoint and infer path parameter structure |
| **Endpoint Name and Description** | Short explanation of the endpoint's purpose to help readers and AI understand business logic |

<details>
<summary>📷 Basic Definitions Example</summary>
<Background>
![image.png](https://api.apidog.com/api/v1/projects/544525/resources/368451/image-preview)
</Background>
</details>

### 2. Parameter Descriptions

Check whether the endpoint documentation clearly and accurately specifies:

| Element | Purpose |
|---------|---------|
| **Parameter Name** | Ensures parameter structure is complete, naming is consistent, and each parameter is in the correct location (Params, Body, Headers, Cookies) |
| **Example** | Provides valid sample input values to help understand typical values, formats, data types, and business meaning |
| **Description** | Explains the meaning, purpose, and business scenarios of the parameter |

The basic information of request parameters can be generated or modified with the help of AI.

<details>
<summary>📷 Parameter Descriptions Example</summary>
<Background>
![image.png](https://api.apidog.com/api/v1/projects/544525/resources/368452/image-preview)
</Background>
</details>

### 3. Parameter Constraints

Check whether the endpoint documentation clearly and accurately specifies:

| Constraint | Purpose |
|------------|---------|
| **Required/Nullable** | Indicates whether a parameter is required and whether null values are allowed |
| **Enums/Const** | Lists possible enum or constant values and their meanings |
| **Boundary Values** | Provides minimum/maximum values, length limits, and other constraints |
| **Format** | Describes special formats (date-time, email, uuid, binary, int64, json-string, etc.) |

<details>
<summary>📷 Parameter Constraints Examples</summary>
<Background>
![image.png](https://api.apidog.com/api/v1/projects/544525/resources/368453/image-preview)
</Background>

<Background>
![param-advanced-settings.gif](https://api.apidog.com/api/v1/projects/544525/resources/368457/image-preview)
</Background>
</details>

### 4. Response

Check whether the API documentation clearly and accurately specifies:

| Element | Purpose |
|---------|---------|
| **Response Body** | Provides complete structure for response content type, field explanations, HTTP status codes, and error codes |

The basic information of responses can also be generated or modified with the help of AI.

<details>
<summary>📷 Response Example</summary>
<Background>
![image.png](https://api.apidog.com/api/v1/projects/544525/resources/368454/image-preview)
</Background>
</details>

## API Documentation Completeness Check

You can find the `API Documentation Completeness Check` feature in the upper-right corner of an endpoint documentation page. Click it to start the check.

<Background>
![image.png](https://api.apidog.com/api/v1/projects/544525/resources/368455/image-preview)
</Background>

If the feature is grayed out, it means it's currently disabled. A team or organization admin must first enable it in the settings. Also, make sure your Apidog client is updated to the latest version.

<details>
<summary>📷 Disabled Feature Example</summary>
<Background>
![image.png](https://api.apidog.com/api/v1/projects/544525/resources/368456/image-preview)
</Background>
</details>

Once you start the check, AI will review the current endpoint documentation against predefined criteria. It then generates a detailed report with scores, explanations, and actionable optimization suggestions for each review item — helping you quickly see what's missing and how to improve it.

<Background>
![API documentation completeness](https://assets.apidog.com/uploads/help/2025/12/15/mujvq-pa.gif)
</Background>

