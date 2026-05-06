# Generating OpenAPI Access Token

Apidog supports OpenAPI specifications from version 2.28 onward, enabling programmatic access to your API projects. This guide walks you through generating and using an OpenAPI access token to integrate with Apidog's OpenAPI services.

For complete API reference documentation, visit [Apidog's OpenAPI documentation](https://openapi.apidog.io/).

## Create a New Token

To generate a new access token, follow these steps:

1. Hover over your avatar on the top right and navigate through **Account Settings** → **API Access Token**.

2. Click **Create a new personal token**.

<Background>
![](https://assets.apidog.com/uploads/help/2024/04/11/6635b66cde699a3643de8939a0a2cd2d.png)
</Background>

:::caution
This token grants the same functionality and access rights as your account across all teams and projects within Apidog. Keep it secure and never share it publicly.
:::

3. Enter a name for your token and choose a validity period.

4. Click **Save and generate token** to create the token. 

<Background>
![](https://assets.apidog.com/uploads/help/2024/04/11/e2887ac09c9c7e3ee14fdbd64143f447.png)
</Background>

:::warning
The token will be displayed only once at this moment. Copy and save it immediately in a secure location. Once you navigate away from this page, the token will not be visible again.
:::

:::tip
Modifying the name or the expiration date of the token does not regenerate a new token. If you misplace it, you need to create a new token by clicking **New**.
:::

## Use the Token

To utilize your access token with the OpenAPI, you'll need two key pieces of information:

1. **Authorization Token**: The token you generated in the previous section
2. **Project ID**: Available under **Project Settings** → **Basic Settings**

<details>
<summary>📷 Finding Your Project ID</summary>

<Background>
![](https://assets.apidog.com/uploads/help/2024/04/11/e84c1a097c4e42748b870a41fd9da748.png)
</Background>

</details>

### Setting Up the OpenAPI Project

1. Clone the [Apidog OpenAPI project](https://openapi.apidog.io/) to your workspace.

<details>
<summary>📷 Visual Reference</summary>

<Background>
![](https://assets.apidog.com/uploads/help/2024/04/11/b60796e8375e5faa6761ecdc7908b2f0.png)
</Background>

</details>

2. Click on the **Environment Management** button in the top right corner.

3. Input the required parameters (authorization token and project ID) and save them.

<details>
<summary>📷 Visual Reference</summary>

<Background>
![](https://assets.apidog.com/uploads/help/2024/04/11/dee01fd497a7de7da70d775ef9f05c84.png)
</Background>

</details>

4. Select the desired OpenAPI service, fill in the request parameters, and execute your API calls.

<details>
<summary>📷 Visual Reference</summary>

<Background>
![](https://assets.apidog.com/uploads/help/2024/04/11/025f882d40c14f2ef6835744c9513633.png)
</Background>

</details>

By following these steps, you'll be able to seamlessly integrate and utilize Apidog's OpenAPI functionalities in your workflows.

