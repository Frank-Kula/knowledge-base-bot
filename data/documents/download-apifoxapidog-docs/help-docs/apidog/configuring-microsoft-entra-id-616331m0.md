# Configuring Microsoft Entra ID

:::info
SSO is available on [Apidog Enterprise plan](https://www.apidog.com/pricing).
:::

To configure SSO with [Microsoft Entra ID](https://www.microsoft.com/en-gb/security/business/identity-access/microsoft-entra-id/) (formerly Azure Active Directory) for your organization, you must have administrator access for both Microsoft Entra ID and Apidog.

Here is a step-by-step video tutorial on how to enable Apidog Single Sign-On (SSO) with Microsoft Entra ID (Azure AD).
<Video src="https://youtu.be/xTqPVffCwNg?si=-4OnmkXYtf13wEmJ"></Video>

## Preparation

Before configuring in the Microsoft Entra ID dashboard, please visit the SAML SSO page in the organization settings of Apidog, then turn on the **Require SAML Authentication** switch, and keep this page open.

<details>
<summary>📷 Visual Reference</summary>

<Background>
![](https://assets.apidog.com/help/assets/images/set-up-saml-sso-a41582f2b1bde2577afa6138d8046870.png)
</Background>

</details>

## Configuration of Microsoft Entra ID

To configure your SAML application, do the following:

1. Open your Microsoft Entra ID management portal in a browser.
2. Go to **Enterprise applications** and select **New application**.
3. Click **Create your own application**, enter the name of the application such as "Apidog", and then select "Integrate any other application you don't find in the gallery (Non-gallery)."
4. On the application's **Overview** page, Click **Set up single sign on**, and select **SAML** as the single sign-on method.
5. Copy the **Identifier** in Apidog, and paste it to the **Identifier (Entity ID)** of Basic SAML Configuration in Microsoft Entra ID.
6. Copy the **Assertion consumer service URL** in Apidog, and paste it to the **Reply URL (Assertion Consumer Service URL)** of Basic SAML Configuration in Microsoft Entra ID.
7. Download the Certificate (Base64) of SAML Certificates in Microsoft Entra ID, open it with a code editor such as Visual Studio Code, copy the text in file, and paste it to the **Public Certificate** in Apidog.
8. Copy the **Login URL** in Microsoft Entra ID, and paste it to the **IdP Sign on URL** field in Apidog.
9. Copy the **Microsoft Entra Identifier** in Microsoft Entra ID, and paste it to the **Issuer** field in Apidog.
10. To support identity provisioning, you should set the **Unique User Identifier (Name identifier)** claim in Microsoft Entra ID as follows:
    - **Name identifier format** to `Persistent`.
    - **Source attribute** to `user.objectid`.
11. Save these configurations in both Microsoft Entra ID and Apidog.

<details>
<summary>📷 Visual Reference</summary>

<Background>
![](https://assets.apidog.com/help/assets/images/configuring-microsoft-entra-id-fff7499639792d254a331f17c774128a.png)
</Background>

</details>

## Testing Your SAML Configuration

You can now return to Apidog's homepage, select your organization from the sidebar, and click the entrance for SSO login on the right. Please test if you can log in normally.

