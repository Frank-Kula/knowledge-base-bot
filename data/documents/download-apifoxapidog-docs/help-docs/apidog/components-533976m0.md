# Components

Typically in API design, while the successful `200 OK` responses often differ across various endpoints due to distinct output data needs, error responses such as `400 Bad Request` and `404 Not Found` tend to be consistent across different endpoints.

Apidog smartly addresses this commonality with its **Response Component** feature, which allows for the reuse of predefined error responses, making the API documentation process more efficient and the API behavior more consistent.

:::info[OAS Compatibility]
The Response Component feature in Apidog is compatible with [the Components in the OAS](https://swagger.io/docs/specification/describing-responses/).
:::

## Adding a Response Component

In the left directory tree of the `APIs` module, navigate to the **Components** section, then click on **New Response** under **Responses** to create a new response component.

<Background>
<img src="https://api.apidog.com/api/v1/projects/544525/resources/341081/image-preview" style="width: 440px" />
</Background>

Creating a response component is similar to specifying the response section when defining an endpoint in terms of including **HTTP status code**, **Content type**, **Schema**, and **Examples**. For detailed guidance, refer to the Response section in [Endpoint Basics](https://docs.apidog.com/endpoint-basics-533932m0.md).

<Background>
<img src="https://api.apidog.com/api/v1/projects/544525/resources/341089/image-preview" style="width: 640px" />
</Background>

### Unique Feature of Response Component

- **Added in new endpoints by default**: When selected as "Yes", this component will be automatically included in all **new** endpoints added to the project by default.

:::info
Existing endpoints are not affected by this setting.
:::

## Referencing Response Components

In the **Response** section of an endpoint, you can reference a pre-defined response component.

<Background>
<img src="https://api.apidog.com/api/v1/projects/544525/resources/341094/image-preview" style="width: 640px" />
</Background>

**Key points about referenced components:**

- Referenced response components cannot be modified within the endpoint. You must make changes to the original response component. Any modifications made will impact all endpoints referencing this component.
- If you wish to modify a response component that has been referenced in an endpoint, you can **Dereference** it. Dereferencing will turn the response into a regular editable response, and changes to the response component will no longer affect it.

<Background>
<img src="https://api.apidog.com/api/v1/projects/544525/resources/341108/image-preview" style="width: 640px" />
</Background>

- In an endpoint, a component can only be referenced once; multiple instances of the same component cannot coexist within the same endpoint.

### Batch Operations

You can bulk **Add** the existing response components to selected endpoints, or **Remove** this component in bulk from the selected endpoints.

<Background>
<img src="https://api.apidog.com/api/v1/projects/544525/resources/341091/image-preview" style="width: 640px" />
</Background>

**Notes:**
- If the selected endpoint already includes this response component, it will not be added again.
- If the selected endpoint does not contain this response component, the remove action will not take effect.

## Default Response Template

Many companies have a standardized structure for their responses. In such cases, you can leverage the **Default Response Template** to maintain the company's fixed structure as the default response template.

In the left directory tree under the **Components** section, you can access and utilize the **Default Response Template** feature.

<Background>
<img src="https://api.apidog.com/api/v1/projects/544525/resources/341106/image-preview" style="width: 240px" />
</Background>

When a new endpoint is created, the content of this template is used as the initial response.

**Key characteristics:**
- Changes made to the default response template will impact only new endpoints, and existing ones will remain unaffected.
- There exists a single default response template, which cannot be added or removed.
- The initial default response template is a 200 Success Response with a Content type of JSON and a data structure of an empty Object node.

<Background>
<img src="https://api.apidog.com/api/v1/projects/544525/resources/341107/image-preview" style="width: 640px" />
</Background>

## FAQ

**Q: Can I use a response component as the default response?**

A: No, response components are intended for generic error responses like 400, 404, and similar status codes. If you need to use a fixed default response, please use the default response template.

