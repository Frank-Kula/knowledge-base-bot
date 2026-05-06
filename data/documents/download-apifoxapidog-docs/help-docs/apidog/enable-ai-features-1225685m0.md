# Enable AI features

AI features in Apidog are disabled by default. To enable them, go to **"Organizations/Team Settings – AI Features"** and switch them on. Once enabled, all projects within your organization or team can start using AI to boost productivity.

- Apidog’s AI features use the AI model providers you configure (you can use any AI model provider with your own API key).
- Apidog does not provide AI models and will not use your data for training.

:::caution[]
Only organization or team admins (or higher roles) can configure AI features.
:::

## Configure Model Providers

Once `AI features` are enabled, you'll see an option to configure model providers. Click `+ Add Provider` to start configuration.

<Background>

![image.png](https://api.apidog.com/api/v1/projects/544525/resources/358907/image-preview)
</Background>

Currently, Apidog supports the following model providers:

- OpenAI
- Anthropic 
- Google Al studio
- Google Vertex

<Background>
![img_v3_02nl_16642d0d-72b2-4618-9a38-4eeef7db106g.png](https://api.apidog.com/api/v1/projects/544525/resources/357480/image-preview)
</Background>

If these providers don’t meet your needs, you can also use `Custom API Configuration` to connect other providers models.

Generally, you can customize the following settings:

1. **API Key**

Enter the API Key provided by your chosen model provider. Use the `Test` function to check if the key is valid.

<Background>

![image.png](https://api.apidog.com/api/v1/projects/544525/resources/358908/image-preview)
</Background>

2. **API Base URL**

The actual URL to which requests are sent when using `AI features` in Apidog. For built-in providers, we pre-fill the base URL — you can edit it as needed.

:::tip[]
Each request to the AI model is sent from the Apidog server to this API base URL.
:::

3. **Model List**

The list of models provided by the AI provider. If you’re using a preset provider, some models will appear by default. Only the models enabled in this list can be used for AI features. If a model you need isn’t listed, you can add it manually.

:::tip[]
Apidog’s`AI features`come with preset prompts and invocation flows. To get the best results, **be sure to select advanced, powerful models** (supporting longer context, function calling, etc. for example: GPT-4.1-mini).
:::

4. **API Format**

Under `Custom API Configuration`, you can define the request and response format. Using the wrong format may cause API request to fail. Most models follow the OpenAI format.

## Set Default Model

If a user doesn’t specify a model when using AI features, Apidog will use the default model set here. You’ll see a dropdown with all models currently enabled — just choose the one you want to use by default.

<Background>

![image.png](https://api.apidog.com/api/v1/projects/544525/resources/358909/image-preview)
</Background>

The default model is set to "**Auto Select**" by default, which automatically picks an available model based on the order of enabled providers and models.

If you set a specific model as the default but it gets disabled or removed, Apidog will automatically switch back to "**Auto Select**".

## Functions & Prompt

You can manage all Apidog AI features and customize their prompts here. Once a feature is enabled, you’ll see it appear in the relevant section of your project. Apidog provides default prompts for each feature, which you can adjust to better suit your needs.

<Background>

![image.png](https://api.apidog.com/api/v1/projects/544525/resources/358910/image-preview)
</Background>

:::warning[]
Custom prompt editing is not yet supported—stay tuned for future updates!
:::

## Inherit AI Configuration from Organization to Team

When using organization management, organization admins or owners can set up AI features at the organization level. These settings can apply to all teams under the organization, helping you maintain consistency and simplify management across projects.

You’ll find the same `AI Features` configuration interface under `Settings` in the organization management page as you do at the team level.

<Background>

![CleanShot 2025-07-23 at 10.52.37@2x.png](https://api.apidog.com/api/v1/projects/544525/resources/358913/image-preview)
</Background>

Once AI features are set up at the organization level, all teams within the organization can inherit the configured model providers, default model, and functions.

<Background>

![image.png](https://api.apidog.com/api/v1/projects/544525/resources/358914/image-preview)
</Background>

**Key points about team inheritance under organizations:**

1. All toggles — such as AI feature switches, model provider settings, default model selections, and functions — follow the organization’s configuration:
    - If a feature is enabled at the organization level, teams can choose to turn it on or off.
    - If a feature is disabled at the organization level, teams won’t be able to enable it.

This ensures centralized control and consistency across all teams.


2. Model providers can either be inherited from the organization or set up independently by each team, depending on your needs.

<Background>

![image.png](https://api.apidog.com/api/v1/projects/544525/resources/358915/image-preview)
</Background>

3. Teams can also choose to use the default model defined at the organization level or configure their own.

<Background>

![image.png](https://api.apidog.com/api/v1/projects/544525/resources/358916/image-preview)
</Background>
