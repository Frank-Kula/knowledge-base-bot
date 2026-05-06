# Introduction to SCIM Provisioning

:::info
SCIM is available on [Apidog Enterprise plans](https://www.apidog.com/pricing).
:::

When using Apidog, you can configure SCIM provisioning by organization. Apidog's SCIM provisioning supports identity providers (IdPs) that compatible with the SCIM protocol, such as Microsoft Entra ID (formerly Azure Active Directory).

When managers add or remove users within the IdP, these changes will be synchronized to Apidog's organizational members.

## SCIM Features

Apidog supports the following provisioning features:

- **Add users**: Add SSO identities to the organization. If an Apidog user uses an identity in the organization for SSO login, the Apidog account will be linked to the SSO identity, and the account will become active. Users in the provisioned status will not occupy seats.
- **Remove users**: If the enterprise administrator deletes a user from the IdP, and the user's SSO identity has been linked with an Apidog account. Then, the user will be removed from the corresponding Apidog organization.

Apidog doesn't support the following provisioning features:

- Update users
- Groups

However, Apidog supports mapping the user's group in the identity provider (IdP) to the team in Apidog through SAML. Find more details here:

[Mapping Groups to Teams](https://docs.apidog.com/mapping-groups-to-teams-741932m0.md)

## Configuring SCIM

After configuring SAML and saving it, you can enable SCIM:

1. Click the **Generate a SCIM token** button.
2. Copy the **SCIM Token** and fill it into your identity provider (IdP)'s dashboard.
3. Copy the **SCIM API endpoint URL** and fill it into your identity provider (IdP)'s dashboard.

<details>
<summary>📷 Visual Reference</summary>

<Background>
![scim-setting-step-1.png](https://api.apidog.com/api/v1/projects/544525/resources/347383/image-preview)
</Background>

<Background>
![scim-setting-step-2.png](https://api.apidog.com/api/v1/projects/544525/resources/347384/image-preview)
</Background>

</details>

Next, you need to go to the identity provider's dashboard for configurations. Learn more details here:

[Microsoft Entra ID (formerly Azure Active Directory)](https://docs.apidog.com/microsoft-entra-id-741945m0.md)

## Advantages of Using SCIM Provisioning for Enterprises

- **Streamlined Identity Management**: Automates the provisioning and de-provisioning of user accounts, reducing administrative overhead and errors associated with manual processes.
- **Improved Security**: Ensures that user access is promptly revoked when employees leave or change roles, minimizing the risk of unauthorized access.
- **Scalability**: Supports large-scale user management across diverse applications, making it ideal for growing organizations with numerous cloud-based services.
- **Interoperability**: Provides a standardized approach to identity management, allowing seamless integration between different identity systems and applications.
- **Enhanced Compliance**: Facilitates easier tracking and reporting of access controls, aiding in compliance with regulatory requirements by maintaining accurate and up-to-date user records.
- **Increased Productivity**: Reduces the time IT departments spend on routine tasks, enabling them to focus on more strategic initiatives.

## Prerequisites for SCIM Provisioning with Apidog

- The identity provider (IdP) must support the SCIM protocol.
- An organization has been set up in Apidog and is subscribed to the enterprise edition payment plan.
- The organization has been using SAML authentication.

