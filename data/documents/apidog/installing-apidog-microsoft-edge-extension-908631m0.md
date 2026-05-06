# Installing Apidog Microsoft Edge Extension

The Apidog Microsoft Edge Extension enables you to use Apidog directly in your browser, providing API testing and debugging capabilities without installing the desktop client. However, browser security policies impose certain restrictions that you should be aware of.

## Browser Extension Limitations and Solutions

Browser security policies impose certain restrictions on extensions, limiting their functionality in specific scenarios. Below are the key limitations and their workarounds.

### Restrictions in Browser Extensions

1. **Forbidden Request Headers**

   Some headers, such as `Cookie`, `Host`, `Origin`, `Content-Length` are automatically blocked by browsers. ([View the full list here.](https://developer.mozilla.org/en-US/docs/Glossary/Forbidden_request_header))

2. **Cookie Limitations**
   - Cross-origin requests will be blocked from carrying cookies unless CORS credentials support is configured
   - Browser extensions cannot directly read or manipulate cookies (including automatically attaching cookies to requests)

3. **Special Request Types**

   `GET`/`HEAD` methods cannot include a request body, and local code/database calls are restricted

### Alternative Solutions

✅ Use [Apidog Desktop Client](https://apidog.com/download) (No restrictions)  
✅ Enable [Cloud Agent](https://docs.apidog.com/request-proxy-in-web-835152m0.md) (Bypasses browser limitations)

## Installation Guide

Visit the [Apidog browser extension page on Microsoft Edge](https://microsoftedge.microsoft.com/addons/detail/apidog-browser-extension/baclgjhlijboldpfeeanjjlkldmeeinn?hl=en-US&gl=JP) to directly **Get** the extension.

<Background>
![get-apidog-extension-microsoft-edge.png](https://api.apidog.com/api/v1/projects/544525/resources/352878/image-preview)
</Background>

## Permission Settings

Some browser versions require manual permission adjustments, otherwise requests may fail.

<Background>
![apidog-edge-extension-permission-settings.png](https://api.apidog.com/api/v1/projects/544525/resources/352882/image-preview)
</Background>

## FAQs

<details>
<summary>Why can't I install successfully?</summary>

Check if the extension is compatible with your browser version. Try updating Microsoft Edge to resolve the issue.

</details>

<details>
<summary>Why can't certain headers be sent?</summary>

Browsers automatically block certain headers (e.g., Cookie). To bypass this, use the [Apidog Desktop Client](https://apidog.com/download) or configure the [Cloud Agent](https://docs.apidog.com/request-proxy-in-web-835152m0.md).

</details>

<details>
<summary>Why does a cross-origin request return 403/Forbidden?</summary>

1. Check if the server explicitly rejected the request (e.g., authentication failure, IP restrictions)
2. Configure [CORS Proxy](https://docs.apidog.com/cors-proxy-780225m0.md)
3. Verify if the backend has CORS headers configured, for example:

```http
Access-Control-Allow-Origin: https://your-domain.com
Access-Control-Allow-Credentials: true
```

</details>

<details>
<summary>Why is the GET request body removed?</summary>

Browser standards prohibit `GET` and `HEAD` requests from containing a body. Use `POST` instead or switch to the desktop client for debugging.

</details>

<details>
<summary>Need to call local code/database?</summary>

Browser sandboxing does not support this. You need to use the [Apidog Desktop Client](https://apidog.com/download).

</details>

## Learn More

- [CORS Proxy](https://docs.apidog.com/cors-proxy-780225m0.md)
- [Request proxy in Apidog web](https://docs.apidog.com/request-proxy-in-web-835152m0.md)
- [Request proxy in shared docs](https://docs.apidog.com/request-proxy-in-shared-docs-835153m0.md)
- [Request proxy in Apidog client](https://docs.apidog.com/request-proxy-in-client-835154m0.md)

