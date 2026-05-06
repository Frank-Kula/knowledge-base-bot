# Azure Key Vault

:::tip[]
Vault secrets is available on the [Apidog Enterprise plan](https://apidog.com/pricing).
:::

Apidog supports integration with Azure Key Vault via the OIDC auth method.

## Configure Microsoft Entra ID

To configure your OIDC application, follow these steps:

1. Open your Microsoft Entra ID management portal in a browser.
2. Go to **App registrations** and select **New registration**.
3. Enter the name of the application (e.g., "Vault Integration") and click **Register**.
4. On the application's **Overview** page, copy the **Application (client) ID** and paste it into the **Client ID** field in Apidog.
5. Click **Endpoints**.
6. Copy the **OAuth 2.0 authorization endpoint (v2)** and paste it into the **Auth URL** field in Apidog.
7. Copy the **OAuth 2.0 token endpoint (v2)** and paste it into the **Access Token URL** field in Apidog.
8. Go to the application's **Authentication** page, click **Add a platform**, then select **Single-page application**.
9. Copy the **Callback URL** from Apidog and paste it into the **Redirect URIs** field.
10. Return to the home page of the Microsoft Entra ID management portal, go to **Enterprise Applications**, and select the application you just registered.
11. On the **Users and groups** page, add users or groups who require access to the key vault.

<Background>
![Configure Microsoft Entra ID for Azure Key Vault](https://api.apidog.com/api/v1/projects/544525/resources/348724/image-preview)
</Background>

## Test Connection

1. Enter the key vault name in Apidog.
2. Click **Test Connection**. An OAuth 2.0 login window will appear.
3. After successfully logging in, "Succeeded" will be displayed.

<Background>
![Test Azure Key Vault connection](https://api.apidog.com/api/v1/projects/544525/resources/348725/image-preview)
</Background>

## Link Secrets

Assume there is a secret named `foo` in Azure Key Vault:

<Background>
![Azure Key Vault secret example](https://api.apidog.com/api/v1/projects/544525/resources/348726/image-preview)
</Background>

To link this secret in Apidog:

1. Enter the metadata as shown below.

<Background>
![Link Azure secret metadata](https://api.apidog.com/api/v1/projects/544525/resources/348727/image-preview)
</Background>

2. Click the **Fetch Secrets** button.
3. Click the eye icon on the right to view the retrieved secret value.

<Background>
![View fetched Azure secret](https://api.apidog.com/api/v1/projects/544525/resources/348728/image-preview)
</Background>

