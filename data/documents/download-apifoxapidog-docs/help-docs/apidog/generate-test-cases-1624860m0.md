# Generate Test Cases

:::tip[About AI features]
- You need to manually [enable the AI feature](https://docs.apidog.com/enable-ai-features-1225685m0) to access AI-related functionalities (available in version 2.7.37 and above).
- Please note that you need to [add your own AI model key (Claude, OpenAI, Gemini, etc.)](https://docs.apidog.com/enable-ai-features-1225685m0#configure-model-providers) to utilize Apidog's AI capabilities. Apidog's AI functions are **FREE** and do not provide a native AI model; they will only use your own AI model to process your data.
:::

AI can quickly generate a large number of test cases based on your current API specs. These cases help verify the functionality, compliance, stability, and security of a single endpoint. You can also manage test cases by grouping and type.

On any endpoint documentation page, switch to the `Test Cases` tab. There you'll find the `Generate with AI`button. Click it to start.

<Background>
![image.png](https://api.apidog.com/api/v1/projects/544525/resources/362628/image-preview)
</Background>


## Selecting Test Case Categories

When you click `Generate with AI`, a settings panel will slide out on the right. Here, you can choose the types of test cases to generate — such as positive, negative, boundary, security, and more.

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

Click`Generate`, and AI will start creating test cases based on API specs and configuration. Once complete, you can click on a specific test case to view its request parameters, rename it, or adjust its category.

 ![use AI to generate test cases](https://assets.apidog.com/uploads/help/2025/09/28/nmubo-ds.gif)

- Click`Run`to check if the test case matches expectations via response.
- Click`Accept` to save the test case under the `Test Cases` tab in your documentation.
- Click`Discard`to remove test cases you don't need.
- Select multiple test cases at once to run bulk actions.

<Background>
![ai-generated-api-test-case.png](https://api.apidog.com/api/v1/projects/544525/resources/362634/image-preview)
</Background>

:::tip[]
**Pro Tip:** Run multiple generation tasks at the same time with different AI models, providers, and configurations. This makes it easy to compare results, validate outputs, and quickly adopt the best test cases.
:::
