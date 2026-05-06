# Build a Schema

## Utilizing the Schema Editor

The Schema Editor is a powerful tool that aids in designing and modeling the data structures your API utilizes. It is based on [JSON Schema](https://json-schema.org/) and is utilized for designing `JSON` or `XML` data structures.

Utilize the Schema Editor to:

- Develop API request and response bodies tailored for specific API endpoints.
- Construct data models that are applicable across one or several APIs.

<Background>
<img src="https://api.apidog.com/api/v1/projects/544525/resources/340995/image-preview" style="width: 640px" />
</Background>

Every schema begins with a root object. To build a schema, add properties to this root object.

### Building a Schema

<Steps>
  <Step title="Add Properties">
    Click on the **+** (Add a child node) sign next to the root object to introduce new properties.
  </Step>
  <Step title="Name Your Property">
    Enter the name (or key) for the property.
  </Step>
  <Step title="Select Property Type">
    Choose common data types or select references to predefined schemas.
  </Step>
  <Step title="Advanced Settings">
Utilize the Type Editor to assign data types, such as default values and formats, for each property.
  </Step>
  <Step title="Manage Properties">
    Rearrange properties by moving, copying, or deleting them. You can also embellish properties with descriptions and mark them as required.
  </Step>
</Steps>

:::tip[Alternative Methods]
You can also create new schemas by importing from database tables or JSON schema files. Learn more about [Generate Schemas from JSON etc.](https://docs.apidog.com/generate-schemas-from-json-etc-534963m0.md).
:::

## Property Type

In alignment with the JSON Schema standard, the Apidog Schema Editor supports the following basic data types:

| Type | Description |
|------|-------------|
| **null** | Represents a JSON "null" value. |
| **boolean** | Represents a "true" or "false" value, corresponding to the JSON "true" or "false" value. |
| **object** | Represents an unordered collection of key-value pairs, corresponding to the JSON "object" value. |
| **array** | Represents an ordered list of values, corresponding to the JSON "array" value. |
| **number** | Represents an arbitrary-precision, base-10 decimal number value, corresponding to the JSON "number" value. |
| **string** | Represents a string of Unicode characters, corresponding to the JSON "string" value. |

:::tip[Array Data Type]
When using the `array` data type, a sub-level `ITEMS` property will be automatically generated. It specifies the data type of the **elements** within the array.

<Background>
<img src="https://api.apidog.com/api/v1/projects/544525/resources/341012/image-preview" style="width: 640px" />
</Background>
:::

<Background>
<img src="https://api.apidog.com/api/v1/projects/544525/resources/341011/image-preview" style="width: 240px" />
</Background>

In addition to the standard data structures mentioned earlier, the Apidog Schema Editor also supports the following:

- **Reference other schemas**: Ability to reference and reuse schemas defined elsewhere within the API documentation.
- **any**: Represents a value that can be of any data type.
- **Schema Composition**: Allows for combining multiple schemas to create complex data structures.
- **Customization**: Enables users to customize and tailor the schema to meet specific requirements and data modeling needs.

### Referencing Other Schemas

You can utilize the "Reference other schemas" feature to reference previously defined schemas.

<Background>
<img src="https://api.apidog.com/api/v1/projects/544525/resources/341015/image-preview" style="width: 400px" />
</Background>

After referencing another schema, you can view the referenced schema in the Schema Editor.

<Background>
<img src="https://api.apidog.com/api/v1/projects/544525/resources/341016/image-preview" style="width: 640px" />
</Background>

**Key points about referenced schemas:**

- Any modifications made to the original schema will be reflected in the referencing schema.
- The referenced schema cannot be directly edited; to make changes, you can:
    - Click the schema name to navigate to the original schema to edit.
    - By clicking **Dereference** on the schema, the schema will transform into a series of independent properties, allowing you to edit them individually.
    - If you need to modify a specific property's definition independently, you can choose to **Dereference** that property, allowing for individual modifications. Any changes to the original schema will not affect the dereferenced property.
- In cases where not all properties of the referenced schema are required in the endpoint, you can click **Hide** to conceal unnecessary properties.

### Schema Composition

If a property in your data structure can have multiple possible data types, you can use Schema Composition to combine multiple schemas.

<Background>
<img src="https://api.apidog.com/api/v1/projects/544525/resources/341018/image-preview" style="width: 640px" />
</Background>

Apidog supports the following composition keywords:

| Keyword | Description |
|---------|-------------|
| **allOf (AND)** | Specifies that the property must adhere to all the schemas defined in the composition. |
| **anyOf (OR)** | Specifies that the property can conform to any of the schemas listed in the composition. |
| **oneOf (XOR)** | Specifies that the property must adhere to one and only one of the schemas defined in the composition. |

After selecting Schema Composition, sub-properties named "0" and "1" will appear under the property, representing each schema within the composition. You can modify the schema type for each sub-property and add additional schemas as needed.

In the API documentation, Schema Composition will be displayed like this:

<Background>
<img src="https://api.apidog.com/api/v1/projects/544525/resources/344562/image-preview" style="width: 600px" />
</Background>

You'll notice the two optional objects under OneOf. If you want to display their names as shown in the image, you need to enter the names in the **title** field in the Type editor.

<Background>
<img src="https://api.apidog.com/api/v1/projects/544525/resources/344561/image-preview" style="width: 600px" />
</Background>

### Customization

By choosing "Customize," you can directly edit the JSON Schema within the editor.

<Background>
<img src="https://api.apidog.com/api/v1/projects/544525/resources/341020/image-preview" style="width: 400px" />
</Background>

## Property Settings

For each property, there are several buttons located next to the data type:

<Background>
![Property settings buttons](https://api.apidog.com/api/v1/projects/544525/resources/341021/image-preview)
</Background>

| Button | Description |
|--------|-------------|
| **\*** | Indicates if the property is required. |
| **N** | Specifies if the property allows for null values. |
| **Settings** | Allows you to edit advanced settings in the Type Editor. |

### Type Editor

The Type Editor visually describes a property in alignment with JSON Schema.

<Background>
<img src="https://api.apidog.com/api/v1/projects/544525/resources/341022/image-preview" style="width: 400px" />
</Background>

Once these advanced settings are configured, they will take effect in the following areas:

1. When adding response examples, you can click to auto-generate based on the settings.
2. They will be displayed in the API documentation.
3. In the request body, you can click to auto-generate based on the settings.
4. Upon sending a request, the returned data will be automatically validated against the settings.
5. In the mock service, response data will be generated based on the settings.

### Enumerated Property

For `String`, `Integer`, and `Number` types, Apidog supports enum. By toggling the enum switch, you can add enum values and descriptions. Additionally, you can perform Bulk Edit for enum values.

<Background>
<img src="https://api.apidog.com/api/v1/projects/544525/resources/341023/image-preview" style="width: 400px" />
</Background>

### Mock

In addition to the advanced settings in the property, you can specify mock content for fields by filling in mock values. Mock values take precedence over the settings in advanced settings.

- Mock values support [Faker.js](https://fakerjs.dev/api/) syntax, allowing you to choose the desired faker data directly from the dropdown options.
- Mock values can also be entered as fixed values.

<Background>
<img src="https://api.apidog.com/api/v1/projects/544525/resources/341026/image-preview" style="width: 640px" />
</Background>

### XML Settings

For XML data, the Type Editor in Apidog offers additional XML Settings. You can enable the **XML** switch, configure properties such as tag name, namespace, etc., and preview the corresponding XML structure.

<Background>
<img src="https://api.apidog.com/api/v1/projects/544525/resources/341025/image-preview" style="width: 400px" />
</Background>

### HashMap, Dictionary, Array

HashMap, also known as Map, dictionary, or associative array. It is a collection of key-value pairs, where the key names can be any content, rather than predefined.

The OpenAPI specification supports defining a HashMap with string keys. This is done by setting the element type to `object`, and then using the `additionalProperties` keyword to specify the type of the values in the key-value pairs.

Suppose there is a user information query API, and the returned data format has the following requirements:

1. The returned data is an object
2. The child elements of the object are key-value pairs of a HashMap
3. The user ID is the key, and the user information is the value

**To define this in Apidog:**

<Steps>
  <Step>
    Create a new schema and name it "UserProfiles".
  </Step>
  <Step>
    In the "UserProfiles", specify the root node as an "object" type. Then click **Advanced Configuration**, set **additionalProperties** to **Allow**, and click the **Settings** button on the right.

<Background>
![HashMap configuration](https://assets.apidog.com/uploads/help/2024/03/19/318cd38b0608f2a421748017103a1868.png)
</Background>
  </Step>
  <Step>
    In the pop-up, add the required user information, with the user's name and email as fields of the object. It saves automatically.

<Background>
![Adding user information fields](https://assets.apidog.com/uploads/help/2024/03/19/69391ed141ef5441a146a17c9e7a9ae1.png)
</Background>
  </Step>
  <Step>
    In the API documentation's responses, reference the schema at the root node and select "user profiles" that you just created.

<Background>
![Referencing user profiles schema](https://assets.apidog.com/uploads/help/2024/03/19/8a65f58cfc991b5494527d64c5f2fa61.png)
</Background>
  </Step>
  <Step>
    Click save, and then you can see the defined schema and example values in the return response example within the API documentation.

<Background>
![Schema example in API documentation](https://assets.apidog.com/uploads/help/2024/03/19/7558105858bbb8f9055fcc30b7b8d3e9.png)
</Background>
  </Step>
</Steps>

### Objects with additionalProperties

As the actual development work iterates, the objects returned by the API may have additionalProperties compared to the originally defined object. According to the OpenAPI specification, this situation can also be handled using the **"additionalProperties"** feature.

Suppose there is now a user information query API, where the originally defined response fields when querying user information by user ID were `name` and `email`. Now, with the system upgrade, you want to include other fields.

When editing the API documentation, you can define it as follows: In the root node of the data model, click **Advanced Settings**, set **additionalProperties** to **Allow**, and set the field value type to **any**.

<Background>
![Setting additionalProperties](https://assets.apidog.com/uploads/help/2024/03/19/a4e3ead74ecf395f290675f171061033.png)
</Background>

Then you can see the defined data structure and example values in the API documentation.

<Background>
![Data structure with additionalProperties](https://assets.apidog.com/uploads/help/2024/03/20/412782301877637e6ab75f4d4536aa3e.png)
</Background>

### Tuples

Typically, the internal elements of an array must be of the same type, while tuples can contain different types of data. If you want to define a tuple that includes both string and integer types, such as data like `(0,"A",2,"C")`, you can set the element type to `array` in the data model, then set the type of `items` to `anyOf` in the combination pattern, and then add child elements of type `string` and `integer` respectively.

:::tip
If you want to generate multiple elements when generating examples, please specify the minimum and maximum number of elements in the advanced settings of the root node.
:::

<Background>
![Defining tuples](https://assets.apidog.com/uploads/help/2024/03/19/2aeb4a0cb155aa1a38e201f813bf34c3.png)
</Background>

After saving, click **Generate Automatically** in the API documentation to see the defined data structure and example values.

<Background>
![Tuple example values](https://assets.apidog.com/uploads/help/2024/03/20/99017a5c0d3319d5e49fc596a5fd3974.png)
</Background>

You can also see the example values of the tuple in the return response in the documentation.

<Background>
![Tuple in documentation](https://assets.apidog.com/uploads/help/2024/03/20/855494b519ef95b82a1d1645a980d691.png)
</Background>

## Tools

The Schema Editor in Apidog provides several highly useful tools.

<Background>
<img src="https://api.apidog.com/api/v1/projects/544525/resources/341024/image-preview" style="width: 640px" />
</Background>

| Tool | Description |
|------|-------------|
| **Generate from JSON etc.** | This tool allows you to automatically generate schemas from JSON, XML data, and other sources, or directly from database table structures. Learn more about [Generate schemas from JSON etc.](https://docs.apidog.com/generate-schemas-from-json-etc-534963m0.md). |
| **Preview** | This tool creates mock data that adheres to the schema definition, providing a preview of the expected data. |
| **Generate code** | This tool can produce data structure definition code in various programming languages. Learn more about [Generate code](https://docs.apidog.com/generating-code-541770m0.md). |
| **JSON Schema** | This tool allows direct editing of JSON schemas for fine-tuning and customization. |

## FAQ

**Q: If a string property has multiple enumerated values and is used in various locations, how can this enum be consistently referenced throughout?**

A: You can define this property as a standalone schema consisting of a single property, enabling it to be consistently referenced across different parts of the API documentation.

<Background>
<img src="https://api.apidog.com/api/v1/projects/544525/resources/341053/image-preview" style="width: 640px" />
</Background>

