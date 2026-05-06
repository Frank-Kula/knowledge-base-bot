# Introduction to Schema

Schema, a fundamental concept in [OpenAPI Specification (OAS)](https://swagger.io/specification/), is also commonly referred to as a Data Model. A schema defines the expected data types and properties of API request and response objects.

[JSON Schema](https://json-schema.org/) serves as the standard adopted by Apidog for modeling the data structures employed by your API.

With schemas, you can:

- Define standard data structures (such as an Order object).
- Integrate schemas with automatically generated examples.
- Leverage data structures repeatedly throughout your API projects.

## Purpose of Schema in Apidog

Within Apidog, schemas play a pivotal role in:

| Purpose | Description |
|---------|-------------|
| **Designing APIs** | By defining schemas early in the design phase, developers can visualize and refine the data structures that their APIs will handle. |
| **Mocking Services** | Apidog utilizes defined schemas to generate mock responses, allowing developers to simulate API behavior and front-end interaction even before the actual implementation. |
| **Documentation** | Accurate and comprehensive API documentation is automatically generated based on the schemas, facilitating clear communication with API consumers about the expected data formats and structures. |
| **Debugging** | Schemas are used to validate the responses in API debugging, ensuring that the API responses adhere to the defined data models. |

## Create a Schema

Consider the scope of your schema: Will the data be utilized across multiple API sections or APIs, or is it specific to a single use case?

If the data structure is intended for multiple uses, creating a schema facilitates centralized management and consistency.

You can [add a schema](https://docs.apidog.com/create-a-new-schema-534954m0.md) under the **"Schemas"** directory.

## Build the Schema

Leverage the user-friendly Schema Editor in Apidog to effectively [build schemas](https://docs.apidog.com/build-a-schema-534897m0.md) that align with the JSON Schema specifications.

<Background>
<img src="https://api.apidog.com/api/v1/projects/544525/resources/340995/image-preview" style="width: 640px" />
</Background>

You can also build schemas by [importing from database tables or JSON/JSON schema data](https://docs.apidog.com/generate-schemas-from-json-etc-534963m0.md).

## Apply the Schema

Upon establishing a reusable schema, navigate to the endpoints to reference the schemas in request or response bodies, or in other schemas. By referencing a shared data model, you can maintain consistency and streamline the integration of the data model across various components of your API design.

