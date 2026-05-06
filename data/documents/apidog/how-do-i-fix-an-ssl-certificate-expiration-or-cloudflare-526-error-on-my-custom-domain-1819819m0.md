# How do I fix an SSL certificate expiration or Cloudflare 526 error on my custom domain?

### **Q: Why does my custom domain show "Certificate has expired"?**

A: This happens because Cloudflare's proxy (the orange cloud) is enabled. When Cloudflare takes over HTTPS, the SSL certificate issued by Apidog is no longer used, so it appears as expired.

<Background>

![image.png](https://api.apidog.com/api/v1/projects/544525/resources/367249/image-preview)
</Background>



### **Q: How can I resolve the certificate expiration or Cloudflare 526 error?**

A: Turn off Enable HTTPS in the Custom Domain settings in Apidog. Cloudflare will handle HTTPS for you.


<Background>
 <img src="https://api.apidog.com/api/v1/projects/544525/resources/367247/image-preview" width="560px" />
</Background>

### **Q: Why am I getting the "SSL handshake failed (Error 525)" message?**
A: This happens because Cloudflare is trying to connect to your origin using HTTPS, but HTTPS is disabled on Apidog after turning off Enable HTTPS. To fix this, change Cloudflare's SSL mode to Flexible, so Cloudflare can serve HTTPS to users while connecting to Apidog over HTTP.

Learn more: https://developers.cloudflare.com/ssl/origin-configuration/ssl-modes/flexible/
