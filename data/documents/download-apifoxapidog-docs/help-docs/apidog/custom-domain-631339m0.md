# Custom Domain

Professional API documentation deserves a professional domain. By default, Apidog documentation is accessible on a `<subdomain>.apidog.io` domain. However, you can customize this by setting up your own domain, allowing your audience to access documentation on a domain that aligns with your organization's branding.

### Prerequisites

Before setting up a custom domain, ensure you have:

- Admin permissions for the Apidog project
- Ownership or control of the domain you want to use
- Access to your domain's DNS settings
- (For Reverse Proxy method) Familiarity with CDN or reverse proxy configuration

## Initiating Custom Domain Setup

To access custom domain settings, navigate to the **Publish Docs** menu in the sidebar, then go to the **Publish** settings page. You'll find a **Custom Domain** section where you can click the **Edit** button to begin setup.

<Background>
![CleanShot 2025-12-29 at 17.31.22@2x.png](https://api.apidog.com/api/v1/projects/544525/resources/369074/image-preview)
</Background>


### Custom Domain Setup Methods

There are two types of options for setting a custom domain:

1. **CNAME** (Recommended): The easiest to set up and maintain; works for both subdomains and root domains, providing maximum flexibility.
2. **Reverse Proxy** (Advanced): Requires using a Content Delivery Network (CDN) or setting up a reverse proxy on your own server; recommended for users familiar with these technologies.
<Background>
<img src="https://api.apidog.com/api/v1/projects/544525/resources/371655/image-preview" style="width: 440px" />
</Background>

## Configuring CNAME

:::info[Applicability]
This section is only applicable if you selected the **CNAME** option in the previous step.
:::

Configuring DNS happens _outside_ of Apidog, at the DNS provider you are using for your domain.

There are two parts to this step:

1. Configure a CNAME record
2. Wait for the changes to take effect

### Configure a CNAME Record

The field names and configuration steps may differ between DNS control panels, but the core concepts remain the same. If you're uncertain, verify with your DNS provider.

* The **type** is the kind of DNS record that you want to create. Here, you need to choose **CNAME**.
* The **name** or **DNS entry** is where you enter your subdomain. You might need to enter it in full (e.g. **docs.example.com**) or you might just need to enter the part before your apex domain (e.g. **docs**). If you’re not sure which to use, check with your DNS provider.
* The **target** or **value** or **destination** is where the subdomain should be pointed. You should see the value for this in the Publish settings in Apidog when you choose the DNS CNAME option. It will look something like `{docsSiteId}.apidog.io`. You should enter this value in full (e.g. `12345678.apidog.io`).
* You might also see a field named **TTL**, which stands for Time To Live. It’s the number of seconds that the DNS record can be cached for. If you’re not sure what to set, we suggest select `Auto` or remain default value.

Here’s an example of how a correct configuration looks in Cloudflare’s control panel:
<Background>
![](https://assets.apidog.com/help/assets/images/custom-domain-with-dns-cname-e2aa8ebcf17f637e3224c99a1a784e03.png)
</Background>



:::caution[]
CNAME record cannot co-exist with another record for the same name. If you already have an A record, AAAA record, TXT record, or any other type of record for your chosen subdomain, you would need to remove those first, _before_ adding the CNAME record.
:::


:::caution[Are you using Cloudflare?]
If you are configuring DNS in Cloudflare’s control panel, please ensure that Cloudflare’s proxying (the orange cloud, also called "Proxy status" in your domain settings) is **disabled**. This is for two reasons:

* This option obfuscates the DNS target for your domain to the public, preventing Apidog from properly running routine checks on your custom domain.
* Your custom domain will already benefit from CDN.

Again, please **turn off Cloudflare proxying** to ensure that your documentation is served without issues.
:::





### How Much Time Does it Take for Changes to Take Effect?


The short answer: you might need to wait 10 minutes up to 48 hours for the DNS changes to take effect before moving onto the next step.

Remember the TTL (Time To Live) field we mentioned earlier? DNS records are cached for a period of time — which is usually a very good thing for performance reasons, because they typically don’t change very often. When they _do_ change, there is a period of time (the TTL value) where DNS cache servers need their cache to expire before they will check for any changes and behave accordingly.

In most cases, it’s best to allow at least 10 minutes before moving onto the next and final step. Sometimes it could all update a bit more quickly, or it could take longer. It’s rare for this to take longer than 48 hours.

Want to check how this process, known as _propagation_, is progressing? You could use a DNS lookup tool, such as [WhatsMyDNS](https://www.whatsmydns.net/). Enter your full subdomain, select CNAME from the dropdown list, and press the Search button. DNS cache servers around the world will respond to let you know what their cached result is. You’ll want to periodically check these results until the vast majority respond with your assigned CNAME value.

## Configuring CDN or Your Own Reverse Proxy Server

:::info[Applicability]
This section is only applicable if you selected the **Reverse Proxy** option in the previous step.
:::

### Configure AWS CloudFront

You can utilize the CDN service provided by cloud vendors like AWS CloudFront, Cloudflare Enterprise to set it up as your own reverse proxy server.

In the following example, we will configure AWS CloudFront as Reverse Proxy.

1. Log in to AWS, and navigate to [CloudFront](https://console.aws.amazon.com/cloudfront). Click Create Distribution.
2. Configure your distribution settings. Here are the values you'll need to change.

| Settings                        | Value                                                        |
| :------------------------------ | :----------------------------------------------------------- |
| Origin Domain Name              | Set to `{docsSiteId}.apidog.io`                               |
| Name                            | A description for the origin. This value lets you distinguish between multiple origins in the same distribution and therefore must be unique. |
| Origin Protocol Policy          | Set to **HTTP** Only                                         |
| Alternate Domain Names (CNAMEs) | Set to your custom domain name (the same one your configured in the Publish settings during the custom domain setup) |
| SSL Certificate                 | Set to the SSL Certificate for your custom domain stored in AWS Certificate Manager (ACM). |

3. Provide information on the Origin Custom Headers (the Header Name and Value fields appear only after you've provided an Origin Domain Name)

| Header Name         | Value                |
| :------------------ | :------------------- |
| X-Apidog-Docs-Site-ID | Set to `{docsSiteId}` |

:::tip[]
`{docsSiteId}` is your Docs Site ID, which can be found in the custom domain panel. Please make sure to enter the correct ID.

<Background>
<img src="https://api.apidog.com/api/v1/projects/544525/resources/355223/image-preview" style="width: 460px"/>
</Background>
:::

4. Configure the Default Cache Behavior Settings. Here are the values you'll need to change.

| Setting                           | Value                                                        |
| --------------------------------- | ------------------------------------------------------------ |
| Viewer Protocol Policy            | Select **Redirect HTTP to HTTPS**                            |
| Allowed HTTP Methods              | Select **GET, HEAD, OPTIONS, PUT, POST, PATCH, DELETE**.     |
| Cache and origin request settings | Select **Use legacy cache settings**. Select **All** for Headers, Query strings and Cookies |
<Background>
![](https://assets.apidog.com/help/assets/images/custom-domain-with-cdn-1-cae8a72ee17ee23e9bd3f3438109d2bd.png)
</Background>
5. Do not enable AWS **Web Application Firewall (WAF)**.
6. Click **Create distribution** at bottom of the page. You'll see your newly-created distribution in your CloudFront Distributions list. Note that the Status will reflect In progress until the distribution is Deployed.
7. Add a new CNAME record to your DNS for your custom domain pointing to the CloudFront Domain Name for your Distribution. This can be found by clicking on your Distribution ID, under the General tab, Distribution domain name (for example, fd1fbc7cac6197.cloudfront.net).


### Configure Cloudflare as Reverse Proxy

You can use Cloudflare Workers to act as a reverse proxy. This allows you to keep your domain proxied (Orange Cloud) while ensuring Apidog receives the necessary project identifiers.

1. Log in to your [Cloudflare Dashboard](https://dash.cloudflare.com/) and navigate to **Workers & Pages**.
2. Click **Create Application** and then **Create Worker**. (Continue with **Start with Hello World!**, if prompted to select a method)
3. Name your worker (e.g., `apidog-docs-proxy`) and click **Deploy**.
4. Click **Edit Code** and replace the existing script with the following:

```javascript
export default {
  async fetch(request, env, ctx) {
    const url = new URL(request.url);
    
    // Replace with your actual Apidog target and Site ID
    const targetHost = "{docsSiteId}.apidog.io";
    const docsSiteId = "{docsSiteId}";

    url.hostname = targetHost;

    const modifiedRequest = new Request(url, {
      method: request.method,
      headers: new Headers(request.headers),
      body: request.body,
      redirect: "manual"
    });

    // Required headers for Apidog to identify your project
    modifiedRequest.headers.set("X-Apidog-Docs-Site-ID", docsSiteId);
    modifiedRequest.headers.set("Host", targetHost);

    return await fetch(modifiedRequest);
  }
};

```

:::tip[]
You can find your `{docsSiteId}` in the custom domain panel. Please make sure to enter the correct ID in both the `targetHost` and `docsSiteId` variables.
:::

5. Click **Save and Deploy**.
6. Navigate to the **Settings** tab of your Worker, select **Domains & Routes**, and click on the **+Add** button.
7. Enter your custom domain (e.g., `docs.example.com`). Cloudflare will automatically handle the DNS records and SSL certificates.
8. Ensure your Cloudflare **SSL/TLS encryption mode** is set to **Full** or **Full (Strict)** to allow secure communication between Cloudflare and Apidog.

:::tip[Prerequisite]
Before attaching a custom domain to your worker, ensure the domain (e.g., `example.com`) is already added to your Cloudflare account and its nameservers are active.
:::


### Configuring Your Own Reverse Proxy Server

You can configure your own reverse proxy server for your API documentation. In the following example, we will use `Nginx` as the reverse proxy server.

1. Add the following content to the `Nginx` configuration file for simple configuration.

```nginx
server {
    ...
    location / {
        proxy_pass  http://{docsSiteId}.apidog.io;
        proxy_set_header X-Apidog-Docs-Site-ID {docsSiteId};
        # Set your custom domain name to the Host value (Eg. docs.example.com).
        proxy_set_header Host docs.example.com;
        ...
    }
    ...
}
```

Caddy configuration example:

```caddy
:8080 {
    handle_path /* {
        reverse_proxy http://{docsSiteId}.apidog.io {
            header_up X-Apidog-Docs-Site-ID {docsSiteId}
            header_up Host "docs.example.com"
        }
    }
}

```

:::tip[]
`{docsSiteId}` is your Docs Site ID, which can be found in the custom domain panel. Please make sure to enter the correct ID.

<Background>
<img src="https://api.apidog.com/api/v1/projects/544525/resources/355223/image-preview" style="width: 460px"/>
</Background>
:::

2. Configure DNS record for your custom domain name to point to your reverse proxy server.

## Deploying API Documents to a Subdirectory of a Custom Domain

Apidog's `Reverse Proxy`allows API documents to be deployed to a subdirectory of a custom domain. For instance, you can deploy the documentation to the `/api-docs` path on a domain like https://example.com. When users visit https://example.com/api-docs, they will be accessing the online API documentation hosted by Apidog.

### Configuration Steps:

1. On Apidog's `Custom Domain` setting page, enter your custom domain.
2. Select `Reverse Proxy` and enable `Use Subdirectory`, then enter the subdirectory path.
<Background>
![](https://assets.apidog.com/uploads/help/2024/04/29/8ad1f025cf9ca959466013c2d80939b2.png)
</Background>
3. Next, you'll need to modify the configuration file of your web server. Assuming you're using Nginx to proxy your service, you can refer to the following configuration:

- `proxy_pass`: Forward client requests to another server (such as Apidog’s API documentation server).
- `proxy_set_header`: Set request headers sent by the proxy server to the upstream server, ensuring the request is properly handled. 

```nginx
server {
    ...
    location /api-docs/ {
        proxy_pass  http://{docsSiteId}.apidog.io/;

        proxy_set_header X-Apidog-Docs-Site-ID {docsSiteId};

        # Set your custom domain name to the Host value (Eg. docs.example.com).
        proxy_set_header Host docs.example.com;
        ...
    }
    ...
}
```

:::tip[]

- `/api-docs/` is the subdirectory of the custom domain, and it must end with a `/` in the Nginx configuration.
- `http://{docsSiteId}.apidog.io/` must also end with a `/`.
- Replace `{docsSiteId}` with your Apidog doc site ID.
    <Background>
    <img src="https://api.apidog.com/api/v1/projects/544525/resources/355223/image-preview" style="width: 460px"/>
    </Background>

- `docs.example.com` is a sample custom domain. Replace it with your actual custom domain.
- After configuration, you need to restart Nginx on your server.

:::

## Enable HTTPS

Apidog's online documentation supports the HTTPS protocol, which has several advantages over HTTP:

- **Secure data transmission**: HTTPS uses SSL/TLS encryption to ensure the security of data transmission, preventing third parties from intercepting information.

- **SEO optimization**: Search engine crawlers prefer to use HTTPS because it offers better security and privacy protection. Therefore, HTTPS websites may have higher authority in search engine rankings than HTTP websites.

### Steps to Enable HTTPS:
1. Go to the `Publish` page and open the `Custom Domain` tab.
2. Switch on `HTTPS` to enable HTTPS, and optionally, you can enable `Always Use HTTPS` to prevent communication from being hijacked or man-in-the-middle attacks.
<Background>
![](https://api.apidog.com/api/v1/projects/544525/resources/371656/image-preview)
</Background>

## SSL Certificate Management

Once HTTPS is enabled, you can choose how to manage your SSL certificate:

- **Generated by Apidog**: Apidog will automatically generate an SSL certificate.
- **Use Your Own Certificate**: You can upload an SSL certificate and private key issued by a certificate authority(e.g., [Let's Encrypt](https://letsencrypt.org/)).

## Troubleshooting[](#troubleshooting)

If you are having issues setting up your custom domain, please contact us via [Discord](https://discord.gg/ZBxrzyXfbJ).

### Are You Using Apidog Europe?

If you are using Apidog Europe, please ensure that you are using the correct domain for your custom domain setup.

The correct domain for Apidog Europe in previous setup is `{docsSiteId}.eu.apidog.com`.
