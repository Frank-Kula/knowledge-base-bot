# Endpoint Unique Identification

Currently, most APIs are differentiated based on the **method and path**. However, some development projects (such as some e-commerce API documents) use a fixed URL for the API request and differentiate between APIs using parameters in the Query / Header.

After version 2.2.9, Apidog added the **endpoint unique identification** feature, which supports **OperationId**, **Query parameters**, **Body parameters**, and **Header parameters** as parameters to differentiate between APIs.

## Setting Endpoint Unique Identification

**Endpoint unique ID** is defined at the **directory** level. When you need to set an API as a unique identification, you need to set it in its **parent directory**. Click on the directory and choose the unique identification parameter according to your needs, and after clicking save it will take effect on all APIs under that directory.

<Background>
![Setting endpoint unique identification](https://api.apidog.com/api/v1/projects/544525/resources/348231/image-preview)
</Background>

For this example we will choose Query parameter and write `OperationID` inside param name.

## Filling in the Corresponding Parameter Value

After setting the endpoint unique identification for the directory, click on an API under that directory, click the **operationid** tab, and in both the basic information and request parameters at the bottom of the API, there is an icon of **K**, which represents the parameter for the **endpoint unique ID**.

<Background>
![Endpoint unique ID parameter indicator](https://api.apidog.com/api/v1/projects/544525/resources/348232/image-preview)
</Background>

You can enter the corresponding value under the corresponding parameter as the value for the endpoint unique identification.

## Importing with Unique Identification

If you use parameters in Query/Header to distinguish between APIs in your project and import an OpenAPI formatted file into Apidog, the following page will appear.

The rule for matching APIs during import is subject to the settings of the target directory. If the setting of the endpoint unique identification in the target directory does not meet the requirements, you can modify it in the import settings. After modification, it will take effect directly on the target directory.

As an example we will import this directory and create endpoint unique ID for it with **Query Param** and **Param Name** for it called `action`.

<Background>
![Import settings for unique identification](https://api.apidog.com/api/v1/projects/544525/resources/348236/image-preview)
</Background>

:::important
Remember, if your directory already has unique ID, the new import can't overwrite it.
:::

<Background>
![Existing unique ID warning](https://api.apidog.com/api/v1/projects/544525/resources/348233/image-preview)

![Import completion with unique ID](https://api.apidog.com/api/v1/projects/544525/resources/348237/image-preview)
</Background>

:::tip[Important Notes]
1. Users who have used the **Fixed Value** in Query parameters need not worry because this function will still be retained. However, when importing, the **Fixed Value** is judged based on the URL, so it is recommended that users who have used the **Fixed Value** use the endpoint unique identification.

2. The endpoint unique identification supports setting **multiple parameters**.

3. If only a subdirectory in your directory is set as the **endpoint unique identification**, when importing Swagger and updating all directories, please avoid importing all projects to the root directory for updating. It is recommended to import APIs set as **endpoint unique identification** separately into that special directory.
:::

## Mock Data

Starting from version 2.2.24, if the API has set the **unique identifier** as **Body Parameter** or **Header Parameter**, you need to send the **path + parameter name and value of the unique identifier** to get the corresponding Mock Data.

:::tip[Mock Data Best Practices]
1. When accessing Mock Data during development, frontend developers also need to send the **path + parameter name and value of the unique identifier** if the API has set the **unique identifier** as **Body Parameter** or **Header Parameter**.

2. For projects that have a **unique identifier** for APIs, the API documentation needs to be standardized to avoid cases where APIs have the same URL but do not have a **unique identifier** set. This is to avoid the failure of obtaining Mock Data correctly.
:::

