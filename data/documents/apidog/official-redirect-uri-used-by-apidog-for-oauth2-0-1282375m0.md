# Official Redirect URI used by Apidog for OAuth2.0

#### Q: What is the official redirect URI used by Apidog for OAuth2.0 authentication?
**A**: When setting up OAuth2.0 authentication for your API in Apidog, you may need to register an official redirect URI in your authorization server or client settings. This ensures the OAuth flow can complete successfully and that Apidog can receive the access token after authorization.

✅ Apidog’s Official Redirect URI:

<Container>
  https://oauth.apidog.com/v1/browser-callback
</Container>
📌 When to Use It:

If your API uses the OAuth2.0 Authorization Code Flow, and you are configuring client settings (such as in your OAuth provider or Identity Platform), then you should add this URI to the "Redirect URIs" or "Callback URLs" field.


