# Validating Responses

In Apidog, after sending a request within an endpoint, Apidog automatically validates whether the response conforms to the schema based on the endpoint's specification.

<Background>
<p style="text-align: center">
    <img src="https://api.apidog.com/api/v1/projects/544525/resources/342696/image-preview" style="width: 640px" />
</p>
</Background>

## Validate Rules

### Scope of Validation

- **HTTP Status Code:** Returned by the API.
- **Data Format:** Of the returned content (`JSON`, `XML`, `HTML`, `Raw`, `Binary`, `No-Content`, `MsgPack`, `Event-Stream`).
- **Schemas:** Only `JSON` and `XML` can configure schemas. For detailed explanation of data structure, please refer [Schemas](/api-design/schema).

| Validation Item | Property type | Validation Prompt Example |
| :--- | :--- | :--- |
| Required key existence | All | `$ should have required property "code"` |
| Value type matches spec | All | `$.data.id should be integer` |
| Non-null key must not have null value | All | `$.data.id should be integer` |
| Enumerated value within range | String, Integer, Number | `$.data.status should be equal to one of predefined values` |
| Numeric value within range | Integer, Number | `$.data.id should be >= 0` |
| Numeric value follows multiple requirement | Integer, Number | `$.data.quantity should be a multiple of 10` |
| String length within range | String | `$.data.name should not be shorter than 3 characters` |
| String matches pattern | String | `$.data.name should match pattern "^[A-Za-z]"` |
| Array element count within range | Array | `$.data.tags should not have more than 2 items` |

### What to Do Next

If the above points are consistent, it will display "Response Data Structure validated!". This means that the actual API return values are consistent with the API documentation specification, eliminating the need for manual verification and improving the efficiency.

<Background>
<p style="text-align: center">
    <img src="https://api.apidog.com/api/v1/projects/544525/resources/342697/image-preview" style="width: 340px" />
</p>
</Background>

When you encounter the corresponding prompts on the right, you can follow the prompts to solve the issue.

There are generally two types of problems: the first is when the server's response is incorrect, in which case the backend needs to be modified to align with the specification; the second is when the API specification is incorrect, requiring modification of the endpoint spec.

By utilizing the automatic validation feature, you can eliminate the need to manually write scripts to validate responses. Furthermore, when there are changes to the API specification, the validation will also automatically adjust accordingly.

### Validating Other Responses

By default, Apidog validates the first response in the endpoint, typically a 200 response. However, an endpoint may return multiple different responses with different schemas. In such cases, you can choose which response to validate in the validation area's top right corner.

<Background>
<p style="text-align: center">
    <img src="https://api.apidog.com/api/v1/projects/544525/resources/342698/image-preview" style="width: 340px" />
</p>
</Background>

You also have the option to toggle the "validate" feature off by clicking the switch in front of the response. This change only applies to the current endpoint.

## Validate Additional Properties

As the actual business upgrades, additional properties may be added to the response. In such cases, Apidog allows users to determine whether to allow additional fields.

For example, there is an API for querying user information, and the previous return fields were `name` and `phone`. Therefore, the data structure was specified like:

<Background>
![](https://assets.apidog.com/uploads/help/2024/03/20/6deaf89e510b1d7a7223c59f49ace86f.png)
</Background>

With the business upgrade, a new `city` field was added to this API, but the API spec was not updated. According to default validation mechanism, no error will be reported, meaning that adding additional fields is allowed by default.

<Background>
![](https://assets.apidog.com/uploads/help/2024/03/20/c4d6e0de9374223c3074dfdfe5ba2145.png)
</Background>

However, for more strict development scenarios, if the return value contains additional fields that do not match the definition, the response validation should also report an error. In this case, you can achieve the desired behavior by following these steps:

1. Modify the response in the API spec. In the advanced settings of the `object`, configure "additionalProperties" to "Deny", which will only take effect for the current API.

<Background>
<p style="text-align: center">
    <img src="https://api.apidog.com/api/v1/projects/544525/resources/342701/image-preview" style="width: 340px" />
</p>
</Background>

2. If you want to disallow additional fields for all API in the project, you can go to **Settings** → **Response Validate Settings** and turn off **Allow Objects to Have additionalProperties**.

<Background>
![](https://api.apidog.com/api/v1/projects/544525/resources/342699/image-preview)
</Background>

3. After completing the configuration, when sending the request again, the response validation mechanism will report an error, indicating that additionalProperties are not allowed.

<Background>
![](https://assets.apidog.com/uploads/help/2024/03/20/ddc8a2f53039b27be519404cbc82b715.png)
</Background>

## Validation Settings

The "Validate Response" switch is turned on by default, and you can adjust it in the "Verification Response Settings" in the project settings interface. This setting only takes effect for all APIs in the current project and does not affect the saved `Endpoint Cases`.

<Background>
![](https://assets.apidog.com/uploads/help/2024/04/26/e29fc63df9977ed5f88ab1c33275b962.png)
</Background>

If you only requires manual assertions or post-scripts and do not need Apidog to validate response consistency with the API specification, you can disable the validation function for specific modules.

<Background>
![](https://assets.apidog.com/uploads/help/2024/04/26/560f853170daa566d9fbebd695e80c82.png)
</Background>

### Validate Response Content

The validate response contains "HTTP Status", "Header", "Body", you can adjust it in the "Validate Response Content" in the project settings. This setting only takes effect for all API in the current project and does not affect the saved `Endpoint Cases`.

<Background>
![](https://assets.apidog.com/uploads/help/2024/04/26/f39271c9eda57fccf54bbf1241161818.png)
</Background>

