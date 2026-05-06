# Configuring SSO for an Organization

:::info
SSO is available on [Apidog Enterprise plan](https://www.apidog.com/pricing).
:::

## Creating an Organization

Please refer to the [Managing Organization](https://docs.apidog.com/managing-teams-612998m0.md) guide for instructions on how to create and manage organizations.

After the organization is created, a default name composed of only numbers will be generated. This name is a unique identifier for this organization and is used for URLs related to SSO. Therefore, you can manually change it to a name that is more likely to be recognized by members of your organization.

<details>
<summary>📷 Visual Reference</summary>

<Background>
![](https://assets.apidog.com/help/assets/images/rename-organization-cf3f008f539399e897735b2fe3324ebe.png)
</Background>

</details>

## Configuring SAML SSO

After successfully creating an organization, you can click SAML SSO to access the SSO configuration page. Please do the following:

1. Turn on the **Require SAML Authentication** switch.
2. Copy the **Sign on URL** from your identity provider (IdP) and fill it in.
3. Copy the **Issuer** from your identity provider (IdP) and fill it in.
4. Get the certificate from your identity provider (IdP) and paste its contents here.
5. Click the save button. Congratulations, you have successfully enabled SSO for the organization.

After you turn on SAML authentication, members of your organization must authenticate with your SAML identity provider (IdP) to access any of the organization's resources.

<details>
<summary>📷 Visual Reference</summary>

<Background>
![alt text](https://assets.apidog.com/help/assets/images/set-up-saml-sso-a41582f2b1bde2577afa6138d8046870.png)
</Background>

</details>

:::tip
The prerequisite for the above steps is that you have already completed the relevant configuration in the backend of your identity provider (IdP). Refer to the corresponding section of the documentation and follow the outlined procedure there:
- [Configure Microsoft Entra ID](https://docs.apidog.com/configuring-microsoft-entra-id-616331m0.md) (formerly Azure Active Directory)
:::

## Configuring Allowed Email Domains

You can set allowed email domains, and anyone with the email address in these domains can join your organization via SSO.

<details>
<summary>📷 Visual Reference</summary>

<Background>
![](https://assets.apidog.com/help/assets/images/enter-email-domain-cc5ed11f00251885731b5f5468f9d232.png)
</Background>

</details>

