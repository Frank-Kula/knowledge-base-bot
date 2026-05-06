# Configure Okta

## Preparation

Before configuring in Okta admin console, please open the `SAML SSO` page in Apidog organization settings, enable **Require SAML Authentication**, and **keep this page open** for the next steps.

<Background>
![set-up-saml-sso.png](https://api.apidog.com/api/v1/projects/544525/resources/354273/image-preview)
</Background>

## Configure Okta

To configure your SAML application, follow these steps:

- Open the Okta admin console in your browser.
- Navigate to **Applications**, click **Create App Integration**.
- Select **SAML** as the sign-in method.
- Enter an App name on the **General Settings** page, such as "Apidog".
-  In Apidog, copy the **Assertion Consumer Service URL** and paste it into the **Single sign-on URL** field in Okta.
- In Apidog, copy the **Identifier** and paste it into the **Audience URI (SP Entity ID)** field in Okta.
- Leave the **Default RelayState** field in Okta **empty**.
-  Set the following options in the Okta **Configure SAML** page:
   - **Name ID format:** Select **Persistent**.
   - **Application username:** Select **Okta username**.
- Leave the rest of the options as default and save the configuration.
- In the **Sign On** tab of your Okta app, under **SAML 2.0**, click **More details**.
- Copy the **Sign on URL** and paste it into the **Login URL** field in Apidog.
- Copy the **Issuer** from Okta and paste it into the **Issuer** field in Apidog.
- In Okta, next to **Signing Certificate**, click **Download**. Open the downloaded certificate with a text editor like Visual Studio Code. Copy the certificate text and paste it into the **Certificate** field in Apidog.
- Save the configuration in Apidog.

## Test Your SAML Setup

Go back to Apidog's main window, click your organization name in the sidebar, then select `Single Sign-On` on the right. Test the logging process to make sure everything is working correctly.
