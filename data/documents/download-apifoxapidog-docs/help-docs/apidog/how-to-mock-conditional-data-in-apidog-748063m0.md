# How to mock conditional data in Apidog?

If you want an endpoint to return specific data, you can use mock expectations.
In `DESIGN` mode, you can set expectations in the "Advanced mock" tab of the endpoint.
<p style="text-align: center">
    <img src="https://api.apidog.com/api/v1/projects/544525/resources/343622/image-preview" style="width: 640px" />
</p>

In `DEBUG` mode, you can set expectations in the "Mock" tab.
<p style="text-align: center">
    <img src="https://api.apidog.com/api/v1/projects/544525/resources/343621/image-preview" style="width: 640px" />
</p>

Apidog supports returning different mock data based on different request parameters.

When adding multiple mock expectations with different conditions, the mock engine will match the expectation conditions based on the request parameters. It will return the first matching mock expectation, following the order from top to bottom.

If none of the mock expectations match, the mock data will be returned according to the Mock method priority set in Project Settings - Feature Settings - Mock Settings.

You can choose which request parameters to use as conditions in the Param conditions. It supports query, path, header, cookie, and body parameters as conditions. Fill in the parameter's name and condition, and the Response below will be returned when this condition is met.
<p style="text-align: center">
    <img src="https://api.apidog.com/api/v1/projects/544525/resources/343619/image-preview" style="width: 640px" />
</p>

- When setting multiple conditions, they are treated as an intersection of these conditions.
- When selecting body parameters, you need to fill in the JSON path of the target property in the name field.
- Body parameters only support JSON, not XML.
- Parameter conditions do not support the use of `{{variables}}`.
- The actual request body must match the API spec if the body is chosen as the parameter location for expectation criteria. For example, if the body request type is form-data in API spec, the parameter needs to be placed in form-data when mocking.
- You can add IP conditions to make certain responses effective only for specified IPs.
