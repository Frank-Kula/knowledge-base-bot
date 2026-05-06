# Installing Apidog Chrome Extension

The Apidog Chrome Extension enables you to use Apidog directly in your browser, providing API testing and debugging capabilities without installing the desktop client. However, browser security policies impose certain restrictions that you should be aware of.

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

1. Visit the [Chrome Web Store page](https://chromewebstore.google.com/detail/apidog-browser-extension/dmhljjnonlhapikmelaefohecogokhio)

2. Click **Add to Chrome**

## Permission Configuration (Required in Some Cases)

If a request fails, you may need to manually allow the extension to access specific permissions:

1. Go to `chrome://extensions` and find the Apidog extension
2. Click **Details** and under the **Permissions**, add:

```
http://apidog.com/*
http://app.apidog.com/*
https://apidog.com/*
https://app.apidog.com/*
```

<Background>
![apidog-browser-extension-permission-settings.png](https://api.apidog.com/api/v1/projects/544525/resources/352872/image-preview)
</Background>

## FAQs

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

