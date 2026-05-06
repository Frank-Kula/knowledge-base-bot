# Documentation Search

> Discover how to integrate Apidog with Algolia to enhance search functionality for your API documentation.

By default, the published API documentation includes a built-in search feature that lets users search for endpoints or documentation by name or path. 

<Background>
![search-bar-api-documentation.png](https://api.apidog.com/api/v1/projects/544525/resources/347620/image-preview)
</Background>

Additionally, Apidog offers integration with Algolia to enhance search capabilities. To take advantage of this feature, you'll need to enable it and complete the required configurations. 

:::info[] 
Apidog version `v2.6.31` or later is required.
:::

After you publish your documentation, you can navigate to the **Publish Docs Site** tab on the side bar then to the **Documentation Search** option. Click on the **Edit** button to fill out your Algolia Search details.
<Background>
![algolia-search-integration.png](https://api.apidog.com/api/v1/projects/544525/resources/347621/image-preview)
</Background>


## Integrating Algolia with Apidog

### Step 1: Create an Algolia Account
1. Visit the [Algolia website](https://www.algolia.com/) and sign up for an account.
2. After registering, log in to your Algolia account.

<Background>
![algoria-website.png](https://api.apidog.com/api/v1/projects/544525/resources/347623/image-preview)
</Background>

### Step 2: Create an Algolia Application
1. Once logged in, create a new application in the Algolia dashboard.
2. Click on`Upload a File`to upload data.

<Background>
![uploading-files-algolia.png](https://api.apidog.com/api/v1/projects/544525/resources/347624/image-preview)
</Background>

:::tip
For starters to set up easier, you can use the provided example code to generate a JSON file. Simply drag and drop the JSON file into Algolia. The JSON file's name will be your `Index Name`, which you’ll need later in Apidog’s documentation search configuration.
:::

<Background>
![upload-records-algolia.png](https://api.apidog.com/api/v1/projects/544525/resources/347625/image-preview)
</Background>

3. Design your search display.

<Background>
![designing-search-display-algolia.png](https://api.apidog.com/api/v1/projects/544525/resources/347626/image-preview)
</Background>

4. Proceed by clicking`Next`until you reach the final step.

<Background>
![order-results-setting-algolia.png](https://api.apidog.com/api/v1/projects/544525/resources/347627/image-preview)
</Background>

5. In the final step, you will be asked how you want to build the search front-end. You can skip this option.

<Background>
![finish-algolia-settings.png](https://api.apidog.com/api/v1/projects/544525/resources/347628/image-preview)
</Background>

### Step 3: Configure Apidog with Algolia Settings
1. Navigate to the Algolia **Settings** -> **API Keys** page and get the configuration details for your application.

<Background>
![img_v3_02ud_9a628b38-c4fa-41e6-ba53-af9aff2bf93g.jpg](https://api.apidog.com/api/v1/projects/544525/resources/370886/image-preview)
</Background>


The`Index Name`will be displayed here:

<Background>
![finding-algolia-index-name.png](https://api.apidog.com/api/v1/projects/544525/resources/347630/image-preview)
</Background>

2. Copy and fill these configuration details into Apidog’s documentation search settings.

### Step 4: Save and Enable the Feature

After filling in the required configuration details in Apidog, save the settings to enable the enhanced search functionality.

<Background>
![integrating-algolia-with-apidog.png](https://api.apidog.com/api/v1/projects/544525/resources/347631/image-preview)
</Background>

:::tip
While Algolia is free to use, there are limits on its usage. You can either upgrade to a paid plan for higher limits or [apply for the free Algolia DocSearch plan](https://docsearch.algolia.com/apply).

If you hit the free plan’s limits, you will see a notification in Apidog:

<Background>
![algolia-limits.png](https://api.apidog.com/api/v1/projects/544525/resources/347632/image-preview)
</Background>
:::

## Ask AI
<Background>
![image.png](https://api.apidog.com/api/v1/projects/544525/resources/371375/image-preview)
</Background>
The Ask AI feature enables users to experience conversational, AI-powered Q&A directly within your documentation search. You can enable the Ask AI feature by binding your `assistant_id` in the **Documentation Search** settings as shown below. 

<Background>
![image.png](https://api.apidog.com/api/v1/projects/544525/resources/371376/image-preview)
</Background>

## Free Algolia DocSearch Plan

Algolia offers a free DocSearch plan for specific purposes (like documentation search). You can [apply for the free Algolia DocSearch plan here](https://docsearch.algolia.com/apply/). For the `Documentation URL` field in the application form, you can enter your public API documentation URL from Apidog.

Once the application is successful, Algolia will send you a confirmation email, and you will receive a message in Algolia dashboard inviting you to join the application. Click to confirm to join the application Algolia offers.

<Background>
![applying-algolia-free-plan.png](https://api.apidog.com/api/v1/projects/544525/resources/347633/image-preview)
</Background>

After confirmation, follow the same process mentioned above to get the configuration details for your application and bind it with your Apidog project.

