# CA and Client Certificates

You can add and manage certificates in Apidog to enable authentication when sending requests to APIs that require certificate-based security. This is essential for connecting to APIs that use Mutual TLS (mTLS) or custom certificate authorities.

## Understanding Certificate Authentication

**Mutual TLS (mTLS)** is an authentication method that requires both the client and the server to confirm their identity with a certificate. Once the identity of both parties is confirmed, an encrypted connection is established. This provides stronger security than traditional one-way TLS.

**Custom CA certificates** enable you to connect to endpoints that use certificates registered with an internal certificate registry. Without adding the CA certificate, requests sent from Apidog will fail with "SSL Error: Self signed certificate."

## Managing Certificates

In the Apidog settings, you can view installed certificates, add new certificates, or remove certificates.

<Steps>
<Step>
Select the settings icon <Icon icon="material-outline-settings"/> in the top right.
</Step>
<Step>
Select the **Certificates** tab.     
<Background>
<img src="https://api.apidog.com/api/v1/projects/544525/resources/347480/image-preview" style="width:540px"/>
</Background>
</Step>
</Steps>

## Adding CA Certificates

To avoid "self signed certificate" errors when sending requests to APIs with custom certificate authorities, add your CA certificate to Apidog.

<Steps>
  <Step>
Turn on the toggle next to **CA Certificates**.
  </Step>
  <Step>
Select the PEM file for your CA certificate.
      
<Background>
     <img src="https://api.apidog.com/api/v1/projects/544525/resources/347481/image-preview" style="width:540px"/>
</Background>

  </Step>
</Steps>

:::info[Multiple CA Certificates]
The PEM file can contain multiple CA certificates. Apidog will load all certificates from the file.
:::

## Adding Client Certificates

To send requests to an API that uses mutual TLS authentication, add your client certificate to Apidog.

<Steps>
<Step>
Select **Add Certificate**.
</Step>
<Step>
Enter the **Host** domain for the certificate (don't include the protocol).

:::tip[Pattern Matching]
The Host field supports pattern matching. If you enter `*.example.com`, the same client certificate will be used for all example.com subdomains.
:::

</Step>
<Step>
(Optional) Enter a custom port number to associate with the domain. If you don't specify a port, Apidog uses the default HTTPS port (443).
</Step>
<Step>
Select the certificate files:
- **Option 1**: Select the **CRT file** and the **Key file** for your certificate
- **Option 2**: Select the **PFX file** for your certificate
</Step>
<Step>
If you used a Passphrase when generating the client certificate, enter it in the box. Otherwise, leave the box blank.
</Step>
<Step>
Select **Add**.
      
<Background>
<img src="https://api.apidog.com/api/v1/projects/544525/resources/347482/image-preview" style="width:540px"/>
</Background>

</Step>
</Steps>

:::caution[One Certificate Per Domain]
Each client certificate is specific to a domain. Don't add more than one certificate for the same domain. If you add multiple certificates for a domain, Apidog will use the last certificate added, which may cause unexpected behavior.
:::

## Editing a Certificate

You can't edit a certificate after adding it. To make changes:

1. Remove the existing certificate
2. Generate a new certificate with the desired settings
3. Add the new certificate to Apidog

## Removing a Certificate

Remove a certificate if you no longer need it to send requests from Apidog.

| Certificate Type | How to Remove |
|------------------|---------------|
| **CA certificate** | Select the remove icon (Close icon) next to the certificate |
| **Client certificate** | Select the delete icon (Delete icon) next to the certificate |

## Using a Certificate

After adding a client certificate, you don't have to perform any extra steps to use the certificate in Apidog. 

**Automatic behavior:**
- When you make an **HTTPS** request to a configured domain, Apidog automatically sends the client certificate with the request
- The certificate is sent using OpenSSL handling
- Apidog doesn't modify the certificate in any way

:::warning[HTTP Requests]
Apidog won't send the certificate if you make an HTTP request. Certificates are only sent over HTTPS connections.
:::

