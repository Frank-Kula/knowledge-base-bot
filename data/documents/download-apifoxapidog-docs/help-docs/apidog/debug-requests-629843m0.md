# Debug Requests

When API requests don't behave as expected, Apidog provides powerful debugging tools to help you diagnose and resolve issues quickly. This guide explains how to use the Apidog Console to troubleshoot problems and outlines common issues with their solutions.

## Actual Request

After sending a request, you can switch to the **Actual Request** tab to view the complete details of what was actually sent to the server, including the request URL, headers, and body.

<Background>
<img src="https://api.apidog.com/api/v1/projects/544525/resources/344035/image-preview" style="width: 640px" />
</Background>

This view is particularly useful for verifying that variables, parameters, and authentication details were correctly resolved before the request was sent.

If you continue scrolling down, you can also see the client code for sending this request using various programming languages, which helps you implement the same request in your application.

<Background>
<img src="https://api.apidog.com/api/v1/projects/544525/resources/344036/image-preview" style="width: 640px" />
</Background>

## Debugging in the Console

You can use the console to output logs at any time during request execution, helping you locate issues in your requests or scripts. Apidog supports the following console methods:

```javascript
console.log()    // General logging
console.info()   // Informational messages
console.warn()   // Warning messages
console.error()  // Error messages
console.clear()  // Clear console output
```

:::tip[]
Variable extraction, database operations, and other automated processes will automatically output their results to the console, providing visibility into script execution.
:::

## Common Issues

The following table outlines common problems you might encounter when sending requests and their solutions:

| **Problem** | **Solution** |
| --- | --- |
| Connectivity | If Apidog is unable to send your request, it is possible that there are connectivity problems. To check, try opening a webpage in your web browser. |
| Firewalls | Some firewalls might be set up to block connections that are not from browsers. In this case, you will need to contact your network administrators for Apidog to function properly. |
| Proxy settings | If you are using a proxy server to send requests, verify your configuration. By default, Apidog uses the proxy settings that are set up in your operating system's network settings. The Apidog Console will provide debugging details concerning proxy servers. |
| SSL certificates | You might encounter difficulties with HTTPS connections. You can disable SSL certificate verification in Settings by clicking on the settings icon and then navigating to Settings > General. If that doesn't resolve the issue, your server could be utilizing a client-side SSL connection, which can be configured by clicking on the settings icon and then going to Settings > Certificates. Utilize the Apidog Console to ensure that the correct SSL certificate is sent to the server. Learn more about managing certificates. |
| Client certificates | Client certificates may be necessary for your API server. You can add a client certificate in Settings by clicking on the settings icon and then going to Settings > Certificates. |
| Incorrect request URLs | If you are using variables or path parameters in your request, double-check that the final address is accurate by checking the Postman Console, which displays the URL your request was sent to upon execution. Unresolved request variables can lead to incorrect server addresses. |
| Incorrect protocol | Make sure you are using the correct protocol (http:// or https://) in your URL. |
| Short timeouts | If a short timeout is configured in Apidog, the request may timeout before completion, resulting in an error. To avoid this, increase the Request timeout in Settings by clicking on the settings icon and then navigating to Settings > General. |
| Invalid responses | If your server sends responses with encoding errors or invalid headers, Apidog may struggle to interpret them. |
| TLS version | Apidog supports TLS version 1.2 and above, which may not be compatible with older browsers or operating systems. |
| Apidog errors | It is possible that Apidog is sending incorrect requests to your API server. You can verify this by checking your server logs, if they are accessible. If you suspect this is happening, contact the Apidog team via the GitHub issue tracker. |
| Unresolved variables | An unresolved variable is not defined in an available scope for the request in which it is used.|
| CORS | If the Apidog web application encounters issues sending your request, it could be due to a cross-origin resource sharing (CORS) error. Ensure you are using the appropriate Apidog Agent for your request. You can also ultilize Apidog Client to avoid CORS problem.|

:::info[]
For most debugging scenarios, the **Actual Request** tab and the **Console** provide all the information you need to identify and fix issues with your API requests.
:::

