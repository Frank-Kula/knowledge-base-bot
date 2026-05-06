# Enabling AI Features

### Prerequisites

Before configuring AI features in Apidog, ensure you have:

- An Apidog account with **organization or team admin** (or higher) role
- Apidog client version **2.7.18 or later**
- An API key from a supported AI model provider (OpenAI, Anthropic, Google AI Studio, Google Vertex, or a custom provider)

:::caution
Only organization or team admins (or higher roles) can configure AI features.
:::

## Overview

AI features in Apidog are disabled by default. To enable them, go to **"Organizations/Team Settings – AI Features"** and switch them on. Once enabled, all projects within your organization or team can start using AI to boost productivity.

For general information about AI features, see [Getting Started with AI Features](https://docs.apidog.com/overview-of-ai-features-in-apidog-1225682m0.md#getting-started-with-ai-features).

## Configure Model Providers

Once `AI features` are enabled, you'll see an option to configure model providers. Click `+ Add Provider` to start configuration.

<Background>
![image.png](https://api.apidog.com/api/v1/projects/544525/resources/358907/image-preview)
</Background>

Currently, Apidog supports the following model providers:

| Provider |
| :--- |
| OpenAI |
| Anthropic |
| Google AI Studio |
| Google Vertex |
| Azure OpenAI |
| Custom API Configuration |

<Background>
![img_v3_02nl_16642d0d-72b2-4618-9a38-4eeef7db106g.png](https://api.apidog.com/api/v1/projects/544525/resources/357480/image-preview)
</Background>

If these providers don't meet your needs, you can also use `Custom API Configuration` to connect other providers models.

### Configuration Settings

When adding a model provider, you can customize the following settings:

| Setting | Description |
|---------|-------------|
| **API Key** | Enter the API Key provided by your chosen model provider. Use the `Test` function to check if the key is valid. |
| **API Base URL** | The actual URL to which requests are sent when using AI features in Apidog. For built-in providers, we pre-fill the base URL — you can edit it as needed. |
| **Model List** | The list of models provided by the AI provider. Only enabled models can be used for AI features. Add models manually if needed. |
| **API Format** | (Custom API Configuration only) Define the request and response format. Most models follow the OpenAI format. |

<details>
<summary>📷 API Key Configuration</summary>
<Background>
![image.png](https://api.apidog.com/api/v1/projects/544525/resources/358908/image-preview)
</Background>
</details>

:::tip
Each request to the AI model is sent from the Apidog server to this API base URL.
:::

:::important
Apidog's AI features come with preset prompts and invocation flows. To get the best results, **be sure to select advanced, powerful models** (supporting longer context, function calling, etc. for example: GPT-4.1-mini).
:::

## Set Default Model

If a user doesn't specify a model when using AI features, Apidog will use the default model set here. You'll see a dropdown with all models currently enabled — just choose the one you want to use by default.

<Background>
![image.png](https://api.apidog.com/api/v1/projects/544525/resources/358909/image-preview)
</Background>

The default model is set to "**Auto Select**" by default, which automatically picks an available model based on the order of enabled providers and models.

If you set a specific model as the default but it gets disabled or removed, Apidog will automatically switch back to "**Auto Select**".

## Functions & Prompt

You can manage all Apidog AI features and customize their prompts here. Once a feature is enabled, you'll see it appear in the relevant section of your project. Apidog provides default prompts for each feature, which you can adjust to better suit your needs.

<Background>
![image.png](https://api.apidog.com/api/v1/projects/544525/resources/358910/image-preview)
</Background>

:::warning
Custom prompt editing is not yet supported—stay tuned for future updates!
:::

## Inherit AI Configuration from Organization to Team

When using organization management, organization admins or owners can set up AI features at the organization level. These settings can apply to all teams under the organization, helping you maintain consistency and simplify management across projects.

You'll find the same `AI Features` configuration interface under `Settings` in the organization management page as you do at the team level.

<Background>
![CleanShot 2025-07-23 at 10.52.37@2x.png](https://api.apidog.com/api/v1/projects/544525/resources/358913/image-preview)
</Background>

Once AI features are set up at the organization level, all teams within the organization can inherit the configured model providers, default model, and functions.

<Background>
![image.png](https://api.apidog.com/api/v1/projects/544525/resources/358914/image-preview)
</Background>

### Inheritance Rules

| Setting | Behavior |
|---------|----------|
| **Feature Toggles** | If enabled at organization level, teams can turn on/off. If disabled at organization level, teams cannot enable. |
| **Model Providers** | Teams can inherit from organization or set up independently |
| **Default Model** | Teams can use organization's default or configure their own |

<details>
<summary>📷 Team Inheritance Settings</summary>
<Background>
![image.png](https://api.apidog.com/api/v1/projects/544525/resources/358915/image-preview)
</Background>

<Background>
![image.png](https://api.apidog.com/api/v1/projects/544525/resources/358916/image-preview)
</Background>
</details>

**Key points about team inheritance under organizations:**

1. All toggles — such as AI feature switches, model provider settings, default model selections, and functions — follow the organization's configuration. This ensures centralized control and consistency across all teams.

2. Model providers can either be inherited from the organization or set up independently by each team, depending on your needs.

3. Teams can also choose to use the default model defined at the organization level or configure their own.

