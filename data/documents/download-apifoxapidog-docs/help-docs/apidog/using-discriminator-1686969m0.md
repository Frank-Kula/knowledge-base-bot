# Using Discriminator

In certain scenarios, a single object may have multiple structural forms. For example, a book can be either an eBook or a paperback. In such cases, the **discriminator** field can be used to distinguish between different schema types.

The **discriminator** is usually used in combination with `oneOf` or `anyOf` to indicate that "the value of a specific field determines the concrete type of the object".

| Property | Description |
|----------|-------------|
| **propertyName** | Specifies the field name used to differentiate types. |
| **mapping** | Defines the mapping between field values and the corresponding schemas. |

## Configuring in Apidog

### Method 1: Using JSON Schema

<Steps>
  <Step title="Configure oneOf via Visual Interface">
Open the request or response editor of the API. Select the field you want to define as a "Schema Composition" field. Click **Advanced Settings** > **Schema Composition** > **oneOf**, and reference the schema you want to combine in `oneOf`, such as `eBook` and `Paperback`.

<Background>
![Configuring oneOf](https://api.apidog.com/api/v1/projects/544525/resources/364298/image-preview)
</Background>
  </Step>
  <Step title="Add discriminator via JSON Schema">
    Click **JSON Schema** in the editor to switch to code mode.

<Background>
![Switching to JSON Schema code mode](https://api.apidog.com/api/v1/projects/544525/resources/364325/image-preview)
</Background>

Add the `discriminator` configuration, for example:

```js
"discriminator": {
    "propertyName": "type",
    "mapping": {
        "ebook": "#/definitions/10331225",
        "paperback": "#/definitions/10331226"
    }
}
```

Replace `10331225` and `10331226` with the IDs of your actual schema. You can see these IDs when opening the JSON Schema configuration panel.

<Background>
![Schema IDs in JSON Schema panel](https://api.apidog.com/api/v1/projects/544525/resources/364300/image-preview)
</Background>
  </Step>
  <Step title="Verify the Result">
After saving, Apidog will automatically recognize different types based on the `type` field. When you [Publish Docs](https://docs.apidog.com/publishing-documentation-sites-631325m0.md), the API documentation will correctly display the differentiated types.

<Background>
![Discriminator in published docs](https://api.apidog.com/api/v1/projects/544525/resources/364259/image-preview)
</Background>
  </Step>
</Steps>

### Method 2: Importing OpenAPI File

Write the definition into an OpenAPI YAML or JSON file, for example:

```yaml
components:
  schemas:
    Book:
      discriminator:
        propertyName: type
        mapping:
          ebook: '#/components/schemas/eBook'
          paperback: '#/components/schemas/Paperback'
      properties:
        type:
          type: string
          description: Book type
```

**Full definition example:**

```yaml
openapi: 3.0.3
info:
  title: Book Example with Discriminator
  version: 1.0.0

components:
  schemas:
    Book:
      type: object
      properties:
        type:
          type: string
          description: Book type

    eBook:
      allOf:
        - $ref: '#/components/schemas/Book'
        - type: object
          properties:
            fileFormat:
              type: string
              description: File format of the eBook (e.g. PDF, EPUB)
          required:
            - fileFormat

    Paperback:
      allOf:
        - $ref: '#/components/schemas/Book'
        - type: object
          properties:
            pageCount:
              type: integer
              description: Number of pages in the book
          required:
            - pageCount

    BookUnion:
      oneOf:
        - $ref: '#/components/schemas/eBook'
        - $ref: '#/components/schemas/Paperback'
      discriminator:
        propertyName: type
        mapping:
          ebook: '#/components/schemas/eBook'
          paperback: '#/components/schemas/Paperback'

paths:
  /books:
    get:
      summary: Get a book example
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/BookUnion'
```

Then, in Apidog, choose **Import OpenAPI File**.

<Background>
![Importing OpenAPI file](https://api.apidog.com/api/v1/projects/544525/resources/364260/image-preview)
</Background>

After importing, Apidog will automatically recognize the `discriminator` and correctly map types in schema and endpoint definitions. When you [Publish Docs](https://docs.apidog.com/publishing-documentation-sites-631325m0.md), the API documentation will correctly display the differentiated types.

<Background>
![Discriminator after import](https://api.apidog.com/api/v1/projects/544525/resources/364261/image-preview)
</Background>

