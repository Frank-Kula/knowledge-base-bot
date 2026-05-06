# How do I resolve the "Error: unable to verify the first certificate on runner" error?

If you encounter an "Error: unable to verify the first certificate on runner" error when running Runner with Apidog, it is usually because Runner is unable to verify the server's SSL certificate. This can be due to the server using a self-signed certificate or an untrusted certificate in the certificate chain.

You can try the following methods to resolve this issue:

#### Add the server's root certificate to the Runner's list of certificates
This will allow the Runner to verify the server's certificate and establish a secure connection. For details, see the help documentation. 

#### Disable certificate validation
Disable certificate validation by adding the environment variable `-e NODE_TLS_REJECT_UNAUTHORIZED=0` on docker startup to the Runner deployment command.

<Background>
 
![image.png](https://api.apidog.com/api/v1/projects/544525/resources/352546/image-preview)
</Background>

Disabling certificate validation poses a security risk because it allows connections to any server, even if its certificate is invalid. Use only in a test environment and make sure you understand the risks.


:::warning[]
Disabling certificate validation poses a security risk because it allows connections to any server, even if its certificate is invalid. Use only in a test environment and make sure you understand the risks.
:::
