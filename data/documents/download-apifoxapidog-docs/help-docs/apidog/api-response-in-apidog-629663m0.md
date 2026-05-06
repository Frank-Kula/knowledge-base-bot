# API response in Apidog

The Apidog response viewer provides comprehensive tools to visualize and verify API responses. Apidog allows you to examine response details, including test results, network information, response size, response time, and security alerts.

## Response Body

Apidog's Body tab offers several views to help you interpret the response:

### Pretty
This view formats JSON or XML responses for improved readability. It highlights links and allows collapsing of large sections for easier navigation.

<p style="text-align: center">
    <img src="https://api.apidog.com/api/v1/projects/544525/resources/344029/image-preview" style="width: 640px" />
</p>

:::tip Force JSON formatting
To enable automatic formatting of the response body in Apidog, the response should include the correct `Content-Type` header. 
However, if you receive a response with a different `Content-Type` header,  you can force JSON formatting manually. 
:::

### Raw
The Raw view displays the unformatted response body in a text area, useful for identifying minification.

### Preview
Preview renders the response in a sandboxed iframe, helpful for debugging HTML errors. 

<p style="text-align: center">
    <img src="https://api.apidog.com/api/v1/projects/544525/resources/344030/image-preview" style="width: 640px" />
</p>

For binary responses, you can select the down arrow next to "Send" and select "Send and Download" to save the response locally.

### Visualize
This view renders data according to custom visualization code you add to the post-request scripts. 

:::highlight purple
Learn more about [Visualizing responses](https://docs.apidog.com/visualizing-responses-597452m0.md).
:::

## Cookies

The Cookies tab displays server-sent cookies, including name, value, domain, path, and other details.

:::highlight purple
Learn more about [Create and send cookies](https://docs.apidog.com/create-and-send-cookies-629770m0.md) in Apidog.
:::

## Headers

Headers appear as key-value pairs in the Headers tab. 

## Network Information

Apidog displays network details such as local and remote IP addresses. 

The response code returned by the API is prominently displayed. Hover over it for a brief description.

Apidog calculates and displays the response time and size, with detailed breakdowns available on hover.

<p style="text-align: center">
    <img src="https://api.apidog.com/api/v1/projects/544525/resources/344031/image-preview" style="width: 640px" />
</p>

