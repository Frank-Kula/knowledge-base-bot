# Global Parameters

Global parameters let you define common parameters that can be applied across your entire project. These parameters can be included automatically in all endpoint requests, boosting both the efficiency and consistency of your API testing.

## Configuring Global Parameters

<Steps>
  <Step>
    Navigate to **Environment Management** at the top right of the page to access the global parameter settings.

<Background>
![Global parameters settings page](https://api.apidog.com/api/v1/projects/544525/resources/350490/image-preview)
</Background>
  </Step>
  <Step>
    Choose where the parameter should be used (Headers, Cookies, Query, or Body).
  </Step>
  <Step>
    Fill in the parameter details (parameter name, type, default value, etc.).
  </Step>
  <Step>
    Enable or disable the parameter using the toggle switch.
  </Step>
  <Step>
    Save your configuration settings.
  </Step>
</Steps>

## Parameter Configuration Details

### Global Parameter Types

Global parameters can be used in:

- **Headers**: Request Header
- **Cookies**: Cookie Information
- **Query**: URL Query Parameter
- **Body**: Request Body Parameter

### Parameter Properties

| Property | Description |
|----------|-------------|
| **Name** | The name that identifies the parameter in requests. |
| **Type** | The data type, such as string or number. |
| **Default Value** | A suggested preset value, often in the format of `{{variable}}`. |
| **Default** | A toggle to control whether the parameter is effective. |
| **Description** | An explanation of what the parameter is for. |

<Background>
![Global variable settings](https://api.apidog.com/api/v1/projects/544525/resources/350499/image-preview)
</Background>

### Special Mark

The `*` (asterisk) mark indicates that the parameter is required.

## Example Usage

Let's take the `API_KEY` shown in the image above as an example:

- **Location**: Header (Request Header)
- **Name**: Authorization
- **Type**: string
- **Default Value**: `{{API_KEY}}`, sourced from environment variables
- **Purpose**: API Key for DeepSeek API

<Background>
![Global parameter default value](https://api.apidog.com/api/v1/projects/544525/resources/350505/image-preview)
</Background>

After sending a request, you can view the parameter details in the response console under **Actual Request**.

<Background>
![Global parameters usage example](https://api.apidog.com/api/v1/projects/544525/resources/350506/image-preview)
</Background>

## Important Notes

1. Global parameters have lower priority than parameters defined at the endpoint level.
2. Always check for duplicate names when adding new parameters to avoid conflicts.
3. Make sure each parameter type aligns with how it will be used to ensure effectiveness.
4. For sensitive information, it's best to use [environment variables](https://docs.apidog.com/environment-management-584758m0.md) or other secure methods for parameter management.

## FAQs

<Accordion title="How to temporarily disable a global parameter?" defaultOpen>
Simply toggle the enable/disable switch on the right side of the parameter.
    
<Frame>
<Background>
![Disabling global parameters](https://api.apidog.com/api/v1/projects/544525/resources/350507/image-preview)
</Background>
</Frame>
</Accordion>

<Accordion title="What is the difference between global parameters and environment variables?" defaultOpen>
Global parameters are for fixed configurations that remain the same in all environments, while environment variables are used to manage configurations that may change across different environments.
</Accordion>

