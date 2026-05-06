# Generating Test Cases

:::info
See [Getting Started with AI Features](https://docs.apidog.com/overview-of-ai-features-in-apidog-1225682m0.md#getting-started-with-ai-features) for setup requirements.
:::

## Overview

AI can quickly generate a large number of test cases based on your current API specs. These cases help verify the functionality, compliance, stability, and security of a single endpoint. You can also manage test cases by grouping and type.

On any endpoint documentation page, switch to the `Test Cases` tab. There you'll find the `Generate with AI` button. Click it to start.

<Background>
![image.png](https://api.apidog.com/api/v1/projects/544525/resources/362628/image-preview)
</Background>


## Selecting Test Case Categories

When you click `Generate with AI`, a settings panel will slide out on the right. Here, you can choose the types of test cases to generate:

| Category | Description |
|----------|-------------|
| **Positive Tests** | Verify expected behavior with valid inputs |
| **Negative Tests** | Test error handling with invalid inputs |
| **Boundary Tests** | Check edge cases and limit values |
| **Security Tests** | Validate authentication, authorization, and security measures |

<Background>
![image.png](https://api.apidog.com/api/v1/projects/544525/resources/362629/image-preview)
</Background>


## Configuring Credentials

If the endpoint requires credentials, the configuration will reference `credentials`. You can modify the credential values as needed. Keys are encrypted locally before being sent to the AI LLM's provider and automatically decrypted after generating test cases. This ensures both quick validation of credentials and information security.

<Background>
![image.png](https://api.apidog.com/api/v1/projects/544525/resources/362632/image-preview)
</Background>


## Adding More Requirements

Before generating, you can provide additional requirements in the text box at the bottom to improve accuracy. In the lower-left corner, you can configure how many test cases to generate — up to 80 cases at once. In the lower-right corner, you can switch the large language model and provider.

<Background>
![image.png](https://api.apidog.com/api/v1/projects/544525/resources/362633/image-preview)
</Background>


## Generating Test Cases

Click `Generate`, and AI will start creating test cases based on API specs and configuration. Once complete, you can click on a specific test case to view its request parameters, rename it, or adjust its category.

<details>
<summary>📷 Test Case Generation Demo</summary>

<Background>
![use AI to generate test cases](https://assets.apidog.com/uploads/help/2025/09/28/nmubo-ds.gif)
</Background>
</details>

### Managing Generated Test Cases

After generation, you can perform the following actions:

| Action | Description |
|--------|-------------|
| **Run** | Check if the test case matches expectations via response |
| **Accept** | Save the test case under the `Test Cases` tab in your documentation |
| **Discard** | Remove test cases you don't need |
| **Bulk Actions** | Select multiple test cases at once to run bulk operations |

<Background>
![ai-generated-api-test-case.png](https://api.apidog.com/api/v1/projects/544525/resources/362634/image-preview)
</Background>

:::tip
**Pro Tip:** Run multiple generation tasks at the same time with different AI models, providers, and configurations. This makes it easy to compare results, validate outputs, and quickly adopt the best test cases.
:::

