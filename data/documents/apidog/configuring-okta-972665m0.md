# Configuring Okta

## Preparation

Before configuring in Okta admin console, please open the **SAML SSO** page in Apidog organization settings, enable **Require SAML Authentication**, and **keep this page open** for the next steps.

<details>
<summary>📷 Visual Reference</summary>

<Background>
![set-up-saml-sso.png](https://api.apidog.com/api/v1/projects/544525/resources/354273/image-preview)
</Background>

</details>

## Configuring Okta

To configure your SAML application, follow these steps:

1. Open the Okta admin console in your browser.
2. Navigate to **Applications**, click **Create App Integration**.
3. Select **SAML** as the sign-in method.
4. Enter an App name on the **General Settings** page, such as "Apidog".
5. In Apidog, copy the **Assertion Consumer Service URL** and paste it into the **Single sign-on URL** field in Okta.
6. In Apidog, copy the **Identifier** and paste it into the **Audience URI (SP Entity ID)** field in Okta.
7. Leave the **Default RelayState** field in Okta **empty**.
8. Set the following options in the Okta **Configure SAML** page:
   - **Name ID format**: Select **Persistent**.
   - **Application username**: Select **Okta username**.
9. Leave the rest of the options as default and save the configuration.
10. In the **Sign On** tab of your Okta app, under **SAML 2.0**, click **More details**.
11. Copy the **Sign on URL** and paste it into the **Login URL** field in Apidog.
12. Copy the **Issuer** from Okta and paste it into the **Issuer** field in Apidog.
13. In Okta, next to **Signing Certificate**, click **Download**. Open the downloaded certificate with a text editor like Visual Studio Code. Copy the certificate text and paste it into the **Certificate** field in Apidog.
14. Save the configuration in Apidog.

## Testing Your SAML Setup

Go back to Apidog's main window, click your organization name in the sidebar, then select **Single Sign-On** on the right. Test the logging process to make sure everything is working correctly.

