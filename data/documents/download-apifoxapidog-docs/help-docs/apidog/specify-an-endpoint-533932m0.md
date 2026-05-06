# Specify an endpoint

In Apidog, designing and setting up an API endpoint is a foundational step in creating robust and effective APIs. 

It is recommended to design endpoints in compliance with [OpenAPI specifications(OAS)](https://swagger.io/specification/) to ensure smooth compatibility with various tools and services within the OpenAPI ecosystem. Deviating from the OAS may lead to compatibility issues when utilizing OpenAPI-compliant tools and services. 

<Video src="https://www.youtube.com/watch?v=d1GruSSk9Go"></Video>

To create a new endpoint within the `APIs` module, click on the `New Endpoint` button.

<Background>
<img src="https://api.apidog.com/api/v1/projects/544525/resources/365348/image-preview" style="width: 640px" />
</Background>

A clear and complete endpoint should include the following elements:

1. Endpoint path
1. Request method
1. Endpoint metadata
1. Request
1. Response and example


<Tabs>
  <Tab title="Design-first Mode">
<Background>
![image.png](https://api.apidog.com/api/v1/projects/544525/resources/352065/image-preview)
</Background>
  </Tab>
  <Tab title="Request-first Mode">
<Background>

![image.png](https://api.apidog.com/api/v1/projects/544525/resources/352068/image-preview)
</Background>
    
    </Tab>

</Tabs>

:::tip[]
Apidog's endpoint interface has two modes: `Design-first Mode` for API Design-first and `Request-first Mode` for Code-first approaches. You can switch modes at the bottom-left corner of the interface. Learn more about [Design-first Mode/Request-first Mode](https://docs.apidog.com/design-first-mode-request-first-mode-541775m0.md).
:::

## Endpoint path

The endpoint path serves as a specific address where the API can interact with external applications. This is what the client will use to access the API service.
<Background>
    <img src="https://api.apidog.com/api/v1/projects/544525/resources/340938/image-preview" style="width: 640px" />
</Background>

Unlike Postman, Apidog recommends following the OpenAPI specification. Instead of writing the full URL for each endpoint, you only need to enter the Path (for example, /users). The Base URL should be set in the environment, and Apidog will automatically add it in front of the Path when running the endpoint. This means you don’t need to manually include the domain or use variables in the Path.

<Background>

![Apidog endpoint url.png](https://api.apidog.com/api/v1/projects/544525/resources/354198/image-preview)
</Background>

To stay consistent with the OpenAPI standard, Apidog also recommends starting all Paths with a `/`. This keeps your API design clean, organized, and ensures you get the full benefit of Apidog’s features.

<Background>
![Apidog endpoint path.jpg](https://api.apidog.com/api/v1/projects/544525/resources/354119/image-preview)
</Background>

:::tip[Why it is recommended to start paths with `/`]

- Starting paths with / is recommended to adhere to the OAS. Failing to start paths with / can lead to various compatibility issues when using tools within the OpenAPI ecosystem. 
- Additionally, using / at the beginning of paths enables the utilization of URL pattern mock functionality essential for testing and validation purposes in Apidog.
:::

## Request method

The request method determines how the client interacts with the server-side resource. Each method carries its own semantics and dictates the server's response. When designing an API, select the most appropriate request method based on business requirements to effectively carry out the intended operation.

<p style="text-align: center">
    <img src="https://api.apidog.com/api/v1/projects/544525/resources/340939/image-preview" style="width: 140px" />
</p>
    
The following are commonly used API request methods:

1. **GET**: Retrieves specified resources without side effects. It uses query parameters to transmit data.
2. **POST**: Submits data for processing and may have side effects. Data is usually sent in the request body.
3. **PUT**: Updates or replaces specified resources entirely.
4. **DELETE**: Removes specified resources.
5. **OPTIONS**: Inquires about the HTTP methods supported by the target resource.
6. **HEAD**: Similar to GET, but only retrieves the response headers. This is useful for checking resource existence and modifications without downloading the resource content.
7. **PATCH**: Updates partial information of specified resources.
8. **TRACE**: Returns the request received by the server. This method is primarily used for debugging and diagnostic purposes.
9. **CONNECT**: Establishes a tunnel to the server, typically used for proxy server request forwarding.

## Endpoint metadata

In Apidog, endpoints come with default metadata fields that define and manage the API's documentation, accessibility, and lifecycle. 

<Background>
    <img width={640} src="https://api.apidog.com/api/v1/projects/544525/resources/340941/image-preview"/>
</Background>

Here is a concise overview of each default metadata field:

- **Name**
A descriptive name that outlines the endpoint's functionality.
- **Status**
Default status is "Developing". You can modify this under "Endpoint Status" to reflect different stages such as Testing or Production.

:::highlight purple
Learn more about [Endpoint status](doc-539760).
:::
- **Maintainer**
Specifies the Apidog team member responsible for the endpoint. Select a user from your account to assign this role.
- **Tags**
Keywords or phrases that categorize or describe the endpoint. You can type to create new tags or select from existing ones.
- **Service**
The base URL to which the endpoint path is appended. Set by default to "Inherit from parents", but can be manually specified through the environment settings in the interface’s top-right corner.
:::highlight purple
Learn more about [Environments and services](https://docs.apidog.com/environments-variables-in-apidog-577823m0.md).
:::
- **OperationId**
A unique identifier (operationId in OAS) that helps distinguish this operation within the API.
- **Description**
Detailed information about the endpoint's purpose and usage, supporting Markdown for enhanced formatting.

:::highlight purple
Besides the standard metadata fields provided for an endpoint, you have the flexibility to [add custom fields](doc-539702) to further enrich the endpoint's metadata.
:::

## Request

### Request Parameters

Request parameters are options that can be passed with the request to control the return of data or to modify the server's response.

<Background>
    <img src="https://api.apidog.com/api/v1/projects/544525/resources/340942/image-preview" style="width: 640px" />
</Background>

Request parameters include Query Parameters, Path Parameters, Header Parameters, and Body Parameters.

#### Query Parameters
Query parameters are key-value pairs appended to the end of a URL after a question mark '?',  and separated by & as follows: `?id=2&status=available`. They are used to filter, sort, or modify the output of an API endpoint.


:::tip[]
In Apidog, query parameters are described in a separate section for clarity and organization. However, when sending a request, these query parameters are concatenated with the Endpoint path in the manner described above.
:::
  
#### Path Parameters

Path parameters are part of the endpoint's URL itself and are used to identify a specific resource or entity within the API.

In Apidog, Path parameters are denoted using **braces** rather than colons. **Correct example**: `/pets/{id}`, **Incorrect example**: `/pets/:id`.


If you need to use variables in a Path parameter, the recommended approach is to define it as `{parameter}` in the URL, and then use `{{variable}}` for the parameter value. For example:

<TipGood>Recommended: Put the variable in the Path parameter value</TipGood>

<Frame>

![image.png](https://api.apidog.com/api/v1/projects/544525/resources/362849/image-preview)
</Frame>


<TipBad>Not recommended: Put the variable directly in the URL</TipBad>

<Frame> 

![image.png](https://api.apidog.com/api/v1/projects/544525/resources/362848/image-preview)
</Frame>

:::tip[Do not confuse `{parameter}` and `{{variable}}`]

- `{parameter}`: Single curly braces are utilized to represent path parameters in Apidog. Path parameters are placeholders in the URL path that dynamically change to specific values when the API endpoint is accessed.

- `{{variable}}`: Double curly braces are employed in Apidog to include variables within requests. These variables can be substituted with actual values when the request is sent, allowing for dynamic and customizable input in API interactions.

:::

:::tip[Why it is NOT recommended to use `{{variable}}` in the path]

- Using `{{variable}}` does not adhere to the OAS. Following the OAS enables seamless integration with a variety of tools within the OpenAPI ecosystem. 
- Using `{{variable}}` in the path will prevent the usage of URL pattern mock functionality in Apidog.

:::
  
#### Header Parameters
Header parameters provide additional information about the request being made and are typically used for authentication, content type, and other metadata.

:::highlight purple
Learn more about [Header Parameters](https://docs.apidog.com/request-headers-627839m0.md).
:::
  
#### Body Parameters
Body parameters contain the data to be sent in the body of the request, typically used in POST, PUT, and PATCH requests to create or update a resource. The data is usually sent in JSON or XML format. 

:::highlight purple
Learn more about [Body Parameters](https://docs.apidog.com/parameters-and-body-627546m0.md).
:::

### Describe parameters

Parameters should be described with their name, type (string, integer, boolean, etc.), necessity (required or optional), and any default values or constraints.

When describing parameters, the following key properties are commonly used:

1. **Name**: The `name` property specifies the name of the parameter being described. It is a required field and should accurately represent the parameter being defined.

2. **Type**: The `type` property specifies the data type of the parameter's value. Common `type` values include `string`, `number`, `integer`, `boolean`, `array`, `object`, and more. This property helps define the format and structure of the parameter's value, allowing API consumers to understand the expected data format when making requests.

3. **Description**: The `description` property provides a brief explanation or documentation regarding the parameter. It helps users understand the purpose and usage of the parameter.

4. **Required**: The `required` property specifies whether the parameter is mandatory for the API request. It is a boolean value (`true` or `false`) that indicates whether the parameter must be included in the request.

5. **Advanced settings**: The `Advanced settings` property defines the data type, format, and constraints of the parameter. It allows you to provide detailed information about the expected structure and content of the parameter value.

:::highlight purple
You can efficiently modify the advanced settings of parameters using the Type Editor. Learn more about the [Type Editor](doc-534897).
:::

### Schemas

When the body parameter type is `JSON` or `XML`, the data structure needs to be set. The data structure can reference the `Schemas`. 

:::highlight purple
For detailed information about schema, please refer to [Schemas](doc-534897).
:::

## Response and Example

After sending a request to the API, the server returns a response. defining the expected responses and providing illustrative examples are crucial steps that enhance understandability and usability for developers interfacing with your API.

<Background>
    <img src="https://api.apidog.com/api/v1/projects/544525/resources/340944/image-preview" style="width: 640px" />
</Background>

The definition of the returned response mainly includes the following parts:

1. **HTTP status code**: determine all potential response statuses your endpoint might return, including standard responses like 200 (OK), 404 (Not Found), or 500 (Server Error). 
2. **Data format**: Define the format of the response that the API will return for each status code. This could be in `JSON`, `XML`, `HTML`, `Raw`, `Binary` or any other suitable format.
3. **Schema**: For responses carrying data (mainly 200 status), detail the structure of the response payload. This includes specifying types, nested objects, optional fields, and arrays. Clear definitions help client developers understand what data to expect and how to parse it. Only `JSON` and `XML` can configure schemas. 

:::highlight purple
For detailed information about schema, please refer to [Schemas](doc-534897).
:::

4. **Example**: Providing an example response is essential for illustrating how the API behaves in real-world scenarios. An example should ideally be a sample data set returned by the server when the endpoint is hit with a predefined request. It should reflect the structure, data format, and types as defined by the response's schema.

### Add responses

In general, it is recommended to define at least one successful response and one error response for each endpoint in your API documentation. This practice ensures comprehensive coverage of various potential outcomes, providing developers with a clear understanding of how the API behaves under different scenarios.

Click the `+ Add` button in the upper right corner of the `Responses` module to add responses.

<Background>
    <img src="https://api.apidog.com/api/v1/projects/544525/resources/341082/image-preview" style="width: 640px" />
</Background>


Typically in API design, while the successful `200 OK` responses often differ across various endpoints due to distinct output data needs, the error responses such as `400 Bad Request` and `404 Not Found` tend to be consistent across different endpoints. Apidog smartly addresses this commonality with its [Response Component](doc-533976) feature, which allows for the reuse of predefined error responses, making the API documentation process more efficient and the API behavior more consistent.

:::highlight purple
Learn more about [Response components](doc-533976).
:::

If Response Component is not needed, you can opt to `Add Blank Response` for defining unique responses within individual endpoints.

### Add response examples

Click on "Add Example" to include response examples in Apidog.

A single response can accommodate multiple diverse examples. When adding examples, provide a name for the example and the corresponding response data.

#### Automatic Example Generation 
By clicking on `Generate Automatically`, Apidog will generate reasonable response data based on the Response Schema definition. 

<Background>
    <img src="https://api.apidog.com/api/v1/projects/544525/resources/340945/image-preview" style="width: 640px" />
</Background>

## Preview the endpoint

After completing the specification of the endpoint, click on "Save" to save your changes. Then, switch to the "API" tab to preview the endpoint you have just configured.
