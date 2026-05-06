# Contract Testing

Contract Testing is used to validate whether the actual API response conforms to the specification defined in the API documentation (OpenAPI). By performing consistency checks on content such as the status code and response structure, it allows for the timely discovery of inconsistencies between the implementation and the documentation during the development, debugging, and testing phases, ensuring stable and reliable API behavior between services.

Apidog's Response Validation (Contract Test) capability is deeply integrated with the API documentation. It can be used during **API Requests**, in **Debug Cases**, **Test Cases**, and **Automation Test Steps**. It is a foundational feature that is enabled by default.

## Enable Response Validation

Response Validation can be enabled by module and used at different stages based on business needs. The relevant toggle is located in **"Settings -> Response Validation Settings"**.

<Background>
![CleanShot 2025-11-18 at 17.27.01@2x.png](https://api.apidog.com/api/v1/projects/544525/resources/366109/image-preview)
</Background>


### API Requests and Debug Cases

When enabled, the "Validate Response" feature is available in the "Request" and "Debug Case" views within the APIs module, used for verifying response consistency during the debugging phase.

<Background>
![CleanShot 2025-11-18 at 17.31.18@2x.png](https://api.apidog.com/api/v1/projects/544525/resources/366110/image-preview)
</Background>


### Test Cases

When enabled, "Validate Response" can be executed in **"Test Cases"** within the APIs module to verify API behavior during manual testing.

<Background>
![CleanShot 2025-11-18 at 17.39.22@2x.png](https://api.apidog.com/api/v1/projects/544525/resources/366113/image-preview)
</Background>


### Automation Test Steps

When enabled, "Validate Response" can be added as a **Test Step** in the Tests module, incorporating Response Validation into the complete automated testing workflow.

<Background>
![CleanShot 2025-11-18 at 17.41.39@2x.png](https://api.apidog.com/api/v1/projects/544525/resources/366114/image-preview)
</Background>


## Validate Response Content

Apidog's Response Validation will automatically perform the following checks based on the OpenAPI specification defined in the API documentation:

### Validate HTTP Status Code of Response

Checks whether the HTTP status code of the actual response is consistent with the status code defined in the documentation. For example:

* Documentation defines 200, but the actual return is 204
* Documentation defines multiple possible values (e.g., 200, 201, 400, 403), validating against the allowed range

If inconsistent, a validation failure will be reported.

<Background>
![CleanShot 2025-11-18 at 17.45.17@2x.png](https://api.apidog.com/api/v1/projects/544525/resources/366116/image-preview)
</Background>

<Background>
![CleanShot 2025-11-18 at 17.45.56@2x.png](https://api.apidog.com/api/v1/projects/544525/resources/366117/image-preview)
</Background>


### Validate Schema of Response Body

Validates the following content based on the Data Schema defined in the documentation:

* Whether a field is required
* Whether a field's value is `null`
* Whether the field type is correct
* Whether required fields are present
* Whether the structure of Arrays and Objects conforms to the documentation
* Whether enum values are valid
* ...

This is the core validation capability of Response Validation.

<Background>
![CleanShot 2025-11-18 at 17.49.17@2x.png](https://api.apidog.com/api/v1/projects/544525/resources/366118/image-preview)
</Background>


### Control of Additional Properties in Objects

For Object-type fields:

* If `additionalProperties` is not set in the documentation, you can choose whether to allow the actual response to contain extra fields not defined in the documentation.
* If `additionalProperties` is set, it validates the allowance of extra fields according to the documentation's rules.

This capability allows for either relaxed or strict control over the response structure to adapt to the API constraint requirements of different teams.

<Background>
![CleanShot 2025-11-18 at 17.50.39@2x.png](https://api.apidog.com/api/v1/projects/544525/resources/366119/image-preview)
</Background>
    

<Background>
![CleanShot 2025-11-18 at 17.51.17@2x.png](https://api.apidog.com/api/v1/projects/544525/resources/366120/image-preview)
</Background>

