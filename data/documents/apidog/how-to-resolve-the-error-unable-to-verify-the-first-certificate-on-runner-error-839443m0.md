# How to resolve the "Error: unable to verify the first certificate on runner" error?

When running Apidog's Runner, if you encounter the "Error: unable to verify the first certificate on runner" error, it's usually because the Runner cannot verify the server's SSL certificate. This can be caused by the server using a self-signed certificate or a certificate in the certificate chain not being trusted.

You can try the following methods to resolve this issue:

### Add the server's root certificate to the Runner's certificate list
This will allow the Runner to verify the server's certificate and establish a secure connection. Refer to the <a href="/5714000m0#Saving Files in Runner">help documentation</a> for specific instructions on uploading the certificate file to the Runner and configuring it in the running environment.

### Disable certificate verification
Disable certificate verification by adding the environment variable `-e NODE_TLS_REJECT_UNAUTHORIZED=0` to the docker startup command in the Runner Deployment Command.
<Background>
![image.png](https://api.apidog.com/api/v1/projects/544525/resources/350299/image-preview)
</Background>
:::warning[]
Disabling certificate verification poses a security risk as it allows connections to any server, even if its certificate is invalid. Only use this in a testing environment and ensure you understand the risks involved.
:::

