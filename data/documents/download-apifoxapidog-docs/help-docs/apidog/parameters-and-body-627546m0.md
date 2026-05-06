# Parameters and Body

When working with APIs, it's essential to understand how to send various types of data with your requests. Apidog provides a user-friendly interface to help you construct and send API requests with different parameters and body data types.

## Parameters

Parameters allow you to send additional information to the server. Apidog supports two main types of parameters: Query params and Path params.

### Query Params

Query parameters are appended to the end of the URL after a question mark (`?`) and are separated by ampersands (`&`). They are used to send optional or additional data to the server.

In Apidog, you have two convenient ways to add query parameters to your API requests:

1. **Directly in the URL**: You can append query parameters directly to the end of the URL in the address bar. For example:
   ```
   https://api.example.com/users?page=1&limit=10
   ```

2. **Using the Query Params section**: Apidog provides a dedicated Query Params section below the URL input field. Here, you can add, edit, and remove query parameters using a user-friendly interface. The parameters you add in this section will be automatically appended to the request URL.

#### Equal Sign in Query Params

In some special cases, query parameters may not appear as key-value pairs. For example, a request URL might be:

```
https://api.example.com/users?available
```

In this case, `available` can serve as a parameter with an empty value. When the value is empty, Apidog automatically omits the equal sign between the key and value.

<Background>
![image.png](https://api.apidog.com/api/v1/projects/544525/resources/343904/image-preview)
</Background>

If you don't want to omit this equal sign, you can manually change it to "Add an equal sign".

### Path Params

Path parameters are part of the URL path itself and are typically used to identify a specific resource. They are denoted by placeholders in the URL, usually enclosed in curly braces `{}`.

**Example:**
```
https://api.example.com/users/{userId}
```

In Apidog, you can define path parameters in the API URL as shown above, and they will appear in the path parameter section below. You can fill in the values for path parameters in the path parameter section, and when the request is sent, `{param}` will be replaced with the actual value. This feature is particularly useful when testing RESTful APIs that use resource identifiers in the URL.

<Background>
![image.png](https://api.apidog.com/api/v1/projects/544525/resources/343903/image-preview)
</Background>

:::tip[]
If you need to use variables in path parameters, the recommended way is to first use `{param}` in the URL, and then use `{{variable}}` in the value of the param.
:::

## Body

The request body is used to send data to the server as part of a POST, PUT, or PATCH request. Apidog supports various body data formats to accommodate different API requirements.

### Body Types Comparison

The following table provides a quick comparison of the available body types:

| **Body Type** | **Content-Type** | **Use Case** | **File Upload Support** |
| --- | --- | --- | --- |
| form-data | multipart/form-data | Form submissions with files | ✓ Yes |
| x-www-form-urlencoded | application/x-www-form-urlencoded | Simple form submissions | ✗ No |
| JSON | application/json | Structured data exchange | ✗ No |
| XML | application/xml | Legacy systems, SOAP APIs | ✗ No |
| raw | Custom (text/plain, etc.) | Custom data formats | ✗ No |
| binary | application/octet-stream | File uploads, binary data | ✓ Yes |
| GraphQL | application/json | GraphQL queries/mutations | ✗ No |
| msgpack | application/msgpack | High-performance data transfer | ✗ No |

### form-data

Form-data is a way to send key-value pairs, similar to submitting an HTML form. This format is particularly useful when you need to upload files along with other data.

<Background>
![image.png](https://api.apidog.com/api/v1/projects/544525/resources/343911/image-preview)
</Background>

The form-data type body will be displayed as `multipart/form-data` in the request. For each parameter in the body, you can choose its type, such as string, integer, etc.

**Sending JSON in form-data**: If you need to send a JSON in form-data, you need to set the parameter type to string, and then fill in the JSON in the string field.

**Sending files**: If you need to send a file in the request, select the type as file, then click "Upload" to choose a local file.

:::tip[]
Apidog only sends the file in the request but does not save the file in the cloud. Therefore, during team collaboration, others can see this request but cannot directly send this file. You need to transfer this file to your colleagues through other means for them to be able to send it.
:::

### x-www-form-urlencoded

This format is similar to query parameters but sent in the request body. It's commonly used for submitting simple forms without file uploads. In Apidog, you can easily add and edit x-www-form-urlencoded data using a key-value interface.

### JSON

JSON is a widely used data format for API requests and responses. You can design the data schema in the **Request → Body → JSON** section of an endpoint.

<Background>
![image.png](https://api.apidog.com/api/v1/projects/544525/resources/364176/image-preview)
</Background>

When designing a JSON data schema, you can use the [**Generate from JSON**](https://docs.apidog.com/generate-schemas-from-json-etc-534963m0.md) feature in Apidog to quickly create the schema instead of adding each field manually.

<details>
<summary>📷 Visual Reference: Generate from JSON</summary>

<Background>
![image.png](https://api.apidog.com/api/v1/projects/544525/resources/364177/image-preview)
</Background>

</details>

When adding fields manually, the default data type is `string`. If you need to add nested fields, change the field type to `object` or `array`.

<details>
<summary>📷 Visual Reference: Adding Nested Fields</summary>

<Background>
![image.png](https://api.apidog.com/api/v1/projects/544525/resources/364178/image-preview)
</Background>

</details>

:::tip[]
If you wish to add comments in JSON, you can enable "JSON with comments support" in Settings → General settings → Feature settings → Advanced settings. When sending JSON, these comments will be automatically removed.
:::

### XML

XML (eXtensible Markup Language) is another common data format used in API communications. Apidog supports XML payloads, allowing you to send structured data in XML format with your API requests.

### raw

The raw option allows you to send any custom data format in the request body. This is useful when working with APIs that expect specific data structures or formats not covered by the other options.

### binary

Binary data can be sent using this option, which is particularly useful when uploading files or working with APIs that expect binary payloads. Apidog allows you to select and send binary files as part of your API requests.

### GraphQL

For APIs using GraphQL, Apidog provides a dedicated GraphQL editor. This feature allows you to construct and send GraphQL queries and mutations, complete with syntax highlighting and autocompletion.

:::info[]
Check out the GraphQL documentation in Apidog for more information on working with GraphQL APIs.
:::

### msgpack

MessagePack (msgpack) is a binary serialization format that's more compact and faster than JSON. Apidog supports sending msgpack data, which is beneficial when working with APIs optimized for performance and reduced data transfer.

