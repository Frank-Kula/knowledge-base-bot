# HashiCorp Vault

:::tip[]
Vault secrets is available on the [Apidog Enterprise plan](https://apidog.com/pricing).
:::

Apidog supports integration with both the Community and Cloud editions of HashiCorp Vault. Two authentication methods are supported: **Token** and **OIDC**.

## Configure Vault Provider: Community Edition

### Token Auth

1. Enter the **URL**. By default, the local Vault service runs on `http://127.0.0.1:8200`.
2. Enter the **Token**. Detailed instructions on generating tokens can be found in the [Vault documentation](https://developer.hashicorp.com/vault/docs/commands/token).
   
   :::note
   The token is NOT uploaded to the server and is NOT shared with other team members.
   :::

3. Click **Test Connection**. If the configuration is correct, "Succeeded" will be displayed.

<Background>
![Connect to Community Edition via Token](https://api.apidog.com/api/v1/projects/544525/resources/348706/image-preview)
</Background>

### OIDC Auth

First, [enable and configure the OIDC auth method](https://developer.hashicorp.com/vault/tutorials/auth-methods/oidc-auth) in your Vault. When configuring the third-party OAuth 2.0 service provider, ensure you add Apidog's callback URL.

Then, proceed to Apidog:

1. Enter the **URL**. By default, the local Vault service runs on `http://127.0.0.1:8200`.
2. Enter the **Auth URL**. By default, it is `http://127.0.0.1:8200/v1/auth/oidc/oidc/auth_url`.
3. Enter the **Access Token URL**. By default, it is `http://127.0.0.1:8200/v1/auth/oidc/oidc/callback`.
4. Click **Test Connection**. An OAuth 2.0 login window will appear. After logging in, "Succeeded" will be displayed.

<Background>
![Connect to Community Edition via OIDC](https://api.apidog.com/api/v1/projects/544525/resources/348708/image-preview)
</Background>

## Configure Vault Provider: HCP Vault Dedicated (Cloud Edition)

### Token Auth

1. Enter the **URL**, which you can find in the HashiCorp Cloud Portal.
2. Enter the **Namespace**. The default namespace is usually `admin`. See [Namespace usage](https://developer.hashicorp.com/vault/docs/enterprise/namespaces#usage) for details.
3. Enter the **Token**. You can generate a token in the HashiCorp Cloud Portal.
   
   :::note
   The token is NOT uploaded to the server and is NOT shared with other team members.
   :::

4. Click **Test Connection**. If the configuration is correct, "Succeeded" will be displayed.

<Background>
![Connect to Cloud Edition via Token](https://api.apidog.com/api/v1/projects/544525/resources/348709/image-preview)
</Background>

### OIDC Auth

First, [enable and configure the OIDC auth method](https://developer.hashicorp.com/vault/tutorials/auth-methods/oidc-auth) in your Vault. When configuring the third-party OAuth 2.0 service provider, ensure you add Apidog's callback URL.

Then, proceed to Apidog:

1. Enter the **Namespace**. The default namespace is usually `admin`.
2. Enter the **Auth URL** in the format: `{{VAULT_ADDR}}/v1/auth/oidc/oidc/auth_url`.
3. Enter the **Access Token URL** in the format: `{{VAULT_ADDR}}/v1/auth/oidc/oidc/callback`.
4. Click **Test Connection**. An OAuth 2.0 login window will appear. After logging in, "Succeeded" will be displayed.

<Background>
![Connect to Cloud Edition via OIDC](https://api.apidog.com/api/v1/projects/544525/resources/348710/image-preview)
</Background>

## Link Secrets

The process for linking secrets is the same for both the Community and Cloud editions of HashiCorp Vault.

If you created the secret using the CLI, the output might look like this:

```shell
$ vault kv put -mount=secret hello foo=world

== Secret Path ==
secret/data/hello

======= Metadata =======
Key                Value
---                -----
created_time       2022-06-15T19:36:54.389113Z
custom_metadata    <nil>
deletion_time      n/a
destroyed          false
version            1
```

In the Web UI, the secret will appear as follows:

<Background>
![HashiCorp Vault Web UI secret example](https://api.apidog.com/api/v1/projects/544525/resources/348711/image-preview)
</Background>

To link this secret in Apidog:

1. Enter the metadata as shown below.

<Background>
![Link HashiCorp secret metadata](https://api.apidog.com/api/v1/projects/544525/resources/348712/image-preview)
</Background>

2. Click the **Fetch Secrets** button.
3. Click the eye icon on the right to view the retrieved secret value.

<Background>
![View fetched HashiCorp secret](https://api.apidog.com/api/v1/projects/544525/resources/348713/image-preview)
</Background>

