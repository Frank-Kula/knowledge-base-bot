# Microsoft Entra ID

To configure SCIM with [Microsoft Entra ID](https://www.microsoft.com/en-gb/security/business/identity-access/microsoft-entra-id/) (formerly Azure Active Directory) for your organization, you must have administrator access for both Microsoft Entra ID and Apidog.

Updated Text: Here is a step-by-step video tutorial on how to enable Apidog SCIM Provisioning using Microsoft Entra ID (Azure AD).

<Video src="https://www.youtube.com/watch?v=Lwgs6QkLLRE&t=8s"></Video>

## Preparation

Before configuring settings in the Microsoft Entra ID dashboard, navigate to the SAML SSO page within your Apidog organization settings. Click on the **Generate a SCIM token** button, and keep this page open for the next steps.

<details>
<summary>📷 Visual Reference</summary>

<Background>
![scim-setting-preparation.png](https://api.apidog.com/api/v1/projects/544525/resources/347385/image-preview)
</Background>

</details>

## Modifying Claim of SSO

To support SCIM provisioning, you should modify Unique User Identifier claim of SSO:

1. Open your Microsoft Entra ID management portal in a browser.
2. Go to **Enterprise applications** and open your desired application.
3. On the application's **Overview** page, click **Set up single sign on**.
4. Set up the **Unique User Identifier (Name identifier)** claim as follows:
   - **Name identifier format** to `Persistent`.
   - **Source attribute** to `user.objectid`.

<details>
<summary>📷 Visual Reference</summary>

<Background>
![modify-claim-sso-step-1.png](https://api.apidog.com/api/v1/projects/544525/resources/347386/image-preview)
</Background>

<Background>
![modify-claim-sso-step-2.png](https://api.apidog.com/api/v1/projects/544525/resources/347387/image-preview)
</Background>

</details>

## Configuring SCIM Provisioning

To configure your SCIM provisioning, follow these steps:

1. Open your Microsoft Entra ID management portal in a browser.
2. Go to **Enterprise applications** and open your desired application.
3. On the application's **Overview** page, click **Provision User Accounts**.
4. Click **Get started**.
5. Select **Automatic** for **Provisioning Mode**, then copy and fill in the information from the Apidog page, and then click Test. The test results will be displayed in the upper right corner. If there is no problem, save it.
6. After saving, you can configure **mapping**. First **turn off** "Groups Mapping".
7. Then configure "Users Mapping".
8. Delete `externalId`.
9. Edit the first attribute to have a:
   - **source attribute** of `objectId`
   - **target attribute** of `externalId`
   - **matching precedence** of `1`
10. Add a new mapping:
    - **source attribute** of `userPrincipalName`
    - **target attribute** of `userName`
11. Then delete other items and keep only the required items.
12. Save, then return to the provisioning homepage and click **Start provisioning**.
13. After a while, the provisioning results will be displayed.

<details>
<summary>📷 Configuration Steps</summary>

<Background>
![configure-scim-provisioning-1.png](https://api.apidog.com/api/v1/projects/544525/resources/347388/image-preview)
</Background>

<Background>
![configure-scim-provisioning-2.png](https://api.apidog.com/api/v1/projects/544525/resources/347389/image-preview)
</Background>

<Background>
![configure-scim-provisioning-3.png](https://api.apidog.com/api/v1/projects/544525/resources/347390/image-preview)
</Background>

<Background>
![configure-scim-provisioning-4.png](https://api.apidog.com/api/v1/projects/544525/resources/347391/image-preview)
</Background>

<Background>
![configure-scim-provisioning-5.png](https://api.apidog.com/api/v1/projects/544525/resources/347392/image-preview)
</Background>

<Background>
![configure-scim-provisioning-6.png](https://api.apidog.com/api/v1/projects/544525/resources/347393/image-preview)
</Background>

<Background>
![configure-scim-provisioning-7.png](https://api.apidog.com/api/v1/projects/544525/resources/347979/image-preview)
</Background>

<Background>
![configure-scim-provisioning-8.png](https://api.apidog.com/api/v1/projects/544525/resources/347395/image-preview)
</Background>

<Background>
![configure-scim-provisioning-9.png](https://api.apidog.com/api/v1/projects/544525/resources/347396/image-preview)
</Background>

<Background>
![configure-scim-provisioning-10.png](https://api.apidog.com/api/v1/projects/544525/resources/347397/image-preview)
</Background>

<Background>
![configure-scim-provisioning-11.png](https://api.apidog.com/api/v1/projects/544525/resources/347398/image-preview)
</Background>

<Background>
![configure-scim-provisioning-12.png](https://api.apidog.com/api/v1/projects/544525/resources/347399/image-preview)
</Background>

</details>

## Testing Your SCIM and SAML Configuration

Go back to Apidog and you can see the users who have been provisioned.

- Once these provisioned members sign in using SSO, their status will change to Active and they will occupy paid seats.
- Users in provisioned status do not occupy paid seats.
- According to Azure's rules, synchronization occurs approximately every 40 minutes.

<details>
<summary>📷 Visual Reference</summary>

<Background>
![test-saml-configuration.png](https://api.apidog.com/api/v1/projects/544525/resources/347400/image-preview)
</Background>

</details>

