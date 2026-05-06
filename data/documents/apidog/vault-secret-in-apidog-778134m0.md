# Vault Secret in Apidog

:::tip[]
Vault secrets is available on [Apidog Enterprise plan](https://apidog.com/pricing).
:::

When using Apidog, you can fetch secrets from external vaults such as HashiCorp Vault, Azure Key Vault, and AWS Secrets Manager, and use them like global variables when sending requests.

Administrators can configure integration with external vaults for teams and projects, allowing users to log in with OAuth 2.0 or their own access tokens to fetch secrets securely. The fetched secrets are encrypted and stored in your local client, ensuring privacy and security.

## Configure Vault Providers

On the team resources page, you can configure multiple vault providers for your team. Each provider can be assigned to different projects based on requirements.

<Background>
![Configure vault providers on team resources page](https://api.apidog.com/api/v1/projects/544525/resources/348641/image-preview)
</Background>

Within the project, you have the option to either customize the vault provider for that specific project or use a provider configured at the team level.

<Background>
![Customize vault provider within project settings](https://api.apidog.com/api/v1/projects/544525/resources/348673/image-preview)
</Background>

Learn more about specific providers:
- [HashiCorp Vault](https://docs.apidog.com/hashicorp-vault-780714m0.md)
- [Azure Key Vault](https://docs.apidog.com/azure-key-vault-781845m0.md)
- [AWS Secrets Manager](https://docs.apidog.com/aws-secrets-manager-781902m0.md)

## Link and Fetch Secrets

1. Click the button next to the environment menu in the upper-right corner of the project and select **Vault Secrets**.
2. In the **Value** input box, configure the metadata for the secret stored in the external vault (e.g., engine, path, key). The required metadata varies depending on the vault provider.

<Background>
![Configure secret metadata in Vault Secrets dialog](https://api.apidog.com/api/v1/projects/544525/resources/348675/image-preview)
</Background>

3. Click **Fetch Secrets** to retrieve the secret, which will be securely encrypted and stored on your local client.

<Background>
![Fetch secrets successfully](https://api.apidog.com/api/v1/projects/544525/resources/348676/image-preview)
</Background>

## Use Secrets

Secrets can be used in any context where a variable is supported, following the syntax `{{vault:key}}`.

<Background>
![Use secrets in request parameters](https://api.apidog.com/api/v1/projects/544525/resources/348677/image-preview)
</Background>

Within a script, you can use `await pm.vault.get("key")` to retrieve the value of the secret. If you use `console.log` to print the value, it will be masked for security.

<Background>
![Use secrets in scripts](https://api.apidog.com/api/v1/projects/544525/resources/348678/image-preview)
</Background>

:::info
Secret values are never shared with team members. However, variable names and metadata are shared to eliminate the need for reconfiguration. Team members can fetch the secrets using proper authorization, ensuring a balance between collaboration and privacy.
:::

## Advantages for Enterprises

- **Secure Storage of Secrets**: Vaults provide a secure way to store sensitive information such as API keys, passwords, certificates, and tokens, ensuring that they are protected against unauthorized access.
- **Access Control**: Vaults allow organizations to define strict access control policies, ensuring that only authorized users or services can access particular secrets.
- **Encryption**: Vaults often provide built-in encryption to protect data both at rest and in transit, adding an extra layer of security.
- **Auditing and Monitoring**: Vaults offer auditing and monitoring capabilities to keep track of who accessed which secret and when, aiding in compliance and detection of unauthorized access.
- **Integration with Other Services**: Vaults are designed to integrate seamlessly with other cloud services (including Apidog) and DevOps tools, facilitating secret management across environments.
- **Centralized Management**: Vaults provide a centralized way to manage secrets across different applications, services, and environments, reducing management overhead.
- **Risk Reduction**: By reducing the chance of credentials being hardcoded into applications or leaking into source code, vaults help mitigate the risk of credential exposure.

## Prerequisites

- Secrets must be stored in [HashiCorp Vault](https://docs.apidog.com/hashicorp-vault-780714m0.md), [Azure Key Vault](https://docs.apidog.com/azure-key-vault-781845m0.md), or [AWS Secrets Manager](https://docs.apidog.com/aws-secrets-manager-781902m0.md).
- The organization or team must be subscribed to the [Apidog Enterprise Plan](https://apidog.com/pricing/).

