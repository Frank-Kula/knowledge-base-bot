# Saving Requests as Endpoints

After successfully sending an API request, Apidog can automatically parse the request and response data to create a complete endpoint specification. This powerful feature saves time and ensures your API documentation accurately reflects real-world behavior.

## Parsing the Request into an Endpoint Spec

A successfully sent request, if not yet defined, can be automatically parsed by Apidog into an endpoint specification.

After sending the request, you can click the dropdown next to the **Save** button and select **Save as endpoint** to save it as an endpoint specification.

When you save a request as an endpoint, Apidog intelligently extracts the following information:

- **Request Parameters**: The request params types of the current request will be treated as the request parameter spec in the endpoint, and the current parameter values will be considered as example values for the request parameters.

- **Response Schema**: The response data structure of the current request will be parsed as the response spec, and the response values will be treated as a response example.

:::tip[]
This feature is particularly useful when working with existing APIs or when you want to quickly document an API based on actual request/response data rather than manually defining the schema.
:::

## Extract the Response

Apidog supports extracting responses into the endpoint specification, which can be extracted as **response schema** or **response examples**.

<Background>
<img src="https://api.apidog.com/api/v1/projects/544525/resources/342694/image-preview" style="width: 400px" />
</Background>

This flexibility allows you to choose whether to update the endpoint's schema definition or simply add a new example response for documentation and testing purposes.

:::info[]
Extracting responses as schemas is useful when the API structure has changed, while extracting as examples is better for documenting different response scenarios (success, errors, edge cases).
:::

