# Save the request as an endpoint

## Parsing the request into an endpoint spec

A successfully sent request, if not yet defined, can be automatically parsed by Apidog into an endpoint specification.

After sending the request, you can click the dropdown next to the "Save" button and select "Save as endpoint" to save it as an endpoint specification.

- The request params types of the current request will be treated as the request parameter spec in the endpoint, and the current parameter values will be considered as example values for the request parameters.

- The response data structure of the current request will be parsed as the response spec, and the response values will be treated as a response example.

## Extract the response

Apidog supports extracting responses into the endpoint specification, which can be extracted as `response schema` or `response examples`.

<p style="text-align: center">
    <img src="https://api.apidog.com/api/v1/projects/544525/resources/342694/image-preview" style="width: 400px" />
</p>
