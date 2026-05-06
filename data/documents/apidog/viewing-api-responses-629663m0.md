# Viewing API Responses

The Apidog response viewer provides comprehensive tools to examine and verify API responses. After sending a request, you can analyze response details including the response body (in multiple view formats), headers, cookies, network information, and performance metrics. This guide explains how to use the response viewer effectively.


## Response Body Views

Apidog offers multiple views to help you interpret response data effectively. Each view serves a specific purpose for analyzing different types of responses.

| View | Purpose | Best For | Key Features |
|------|---------|----------|--------------|
| **Pretty** | Formatted, readable display | JSON/XML responses | Syntax highlighting, collapsible sections, clickable links |
| **Raw** | Unformatted text display | Identifying minification, debugging formatting | Plain text area, no processing |
| **Preview** | Rendered HTML output | HTML responses, debugging visual errors | Sandboxed iframe rendering |
| **Visualize** | Custom data visualization | Complex data analysis | Custom visualization code via post-request scripts |

### Pretty View

This view formats JSON or XML responses for improved readability. It highlights links and allows collapsing of large sections for easier navigation.

<Background>
<img src="https://api.apidog.com/api/v1/projects/544525/resources/344029/image-preview" style="width: 640px" />
</Background>

:::tip[Force JSON Formatting]
To enable automatic formatting of the response body in Apidog, the response should include the correct `Content-Type` header. However, if you receive a response with a different `Content-Type` header, you can force JSON formatting manually.
:::

### Raw View

The Raw view displays the unformatted response body in a text area, useful for identifying minification or examining the exact response content without any processing.

### Preview View

Preview renders the response in a sandboxed iframe, helpful for debugging HTML errors and seeing how the response would appear in a browser.

<Background>
<img src="https://api.apidog.com/api/v1/projects/544525/resources/344030/image-preview" style="width: 640px" />
</Background>

For binary responses, you can select the down arrow next to "Send" and select "Send and Download" to save the response locally.

### Visualize View

This view renders data according to custom visualization code you add to the post-request scripts, enabling you to create charts, graphs, and other visual representations of your response data.

:::info
Learn more about [Visualizing responses](https://docs.apidog.com/visualizing-responses-597452m0.md).
:::

## Response Headers

Headers appear as key-value pairs in the Headers tab, showing all HTTP headers returned by the server. This includes standard headers like `Content-Type`, `Cache-Control`, and any custom headers your API returns.

## Response Cookies

The Cookies tab displays server-sent cookies with detailed information about each cookie.

| Cookie Attribute | Description |
|------------------|-------------|
| **Name** | The cookie's identifier |
| **Value** | The data stored in the cookie |
| **Domain** | The domain to which the cookie applies |
| **Path** | The URL path where the cookie is valid |
| **Expires/Max-Age** | When the cookie will expire |
| **HttpOnly** | Whether the cookie is accessible only via HTTP |
| **Secure** | Whether the cookie is sent only over HTTPS |

:::info
Learn more about [Managing Cookies](https://docs.apidog.com/managing-cookies-629770m0.md) in Apidog.
:::

## Network Information

Apidog displays comprehensive network details to help you understand the request-response cycle and identify performance issues.

### Response Code

The response code returned by the API is prominently displayed. Hover over it for a brief description of what the status code means.

### Performance Metrics

Apidog calculates and displays the response time and size, with detailed breakdowns available on hover. This helps you:

- Identify slow endpoints
- Monitor response payload sizes
- Optimize API performance

### Connection Details

View network details such as local and remote IP addresses, helping you verify connections and troubleshoot network-related issues.

<Background>
<img src="https://api.apidog.com/api/v1/projects/544525/resources/344031/image-preview" style="width: 640px" />
</Background>

