# Configure Multiple Request Body Examples

Apidog supports configuring multiple examples for request bodies of **JSON**, **XML**, **Raw**, and **MsgPack** type. This feature is useful for:

- **Configuring examples for different business scenarios**: For instance, normal requests vs. exception requests.
- **Compliance with OAS 3.0/3.1 specifications**: Supports exporting standard OpenAPI specifications.
- **Quickly switching between examples**: Useful during debugging and automated tests.

<Background>
![Multiple request body examples](https://api.apidog.com/api/v1/projects/544525/resources/351638/image-preview)
</Background>

## Configuring Multiple Request Body Examples

> Apidog version 2.7.0 or later is required.

<Steps>
  <Step title="Create a new request body example">
  - Go to the **Edit** page of your endpoint documentation.
  - Locate the **Request Body** section.
  - Click the **+ Add** button to create a new request body example.

<Background>
![Creating new request body example](https://api.apidog.com/api/v1/projects/544525/resources/351639/image-preview)
</Background>
  </Step>
  <Step title="Configure the request body example">
  - **Example Name (optional)**: If left blank, it will default to `Example 1`, `Example 2`, etc.
  - **Example Value (required)**: Provide the actual example data for the request body.
  - **Description (optional)**: Add a description to explain the example. Supports Markdown formatting for rich text.
  - **OAS Key (optional)**: Used when exporting OpenAPI specifications. If not provided, a serial number will be used instead.
  - **OAS Extensions (custom fields)**: If provided, this will be retained during export.

<Background>
![Configure request body example](https://api.apidog.com/api/v1/projects/544525/resources/351640/image-preview)
</Background>
  </Step>
  <Step title="Save & Use the request body example">
  Once you've saved the example, it becomes available for use. During debugging, you can easily select from different examples to test your endpoints.

<Background>
![Use request body example during debugging](https://api.apidog.com/api/v1/projects/544525/resources/351641/image-preview)
</Background>
  </Step>
</Steps>

:::tip
For request bodies of Raw type, only the first example value is displayed during debugging.
:::

## Extracting Request Parameters as Examples

<Steps>
  <Step title="Extract request parameters as examples">
  While debugging, if you've manually configured the request body and want to save it as an example, simply click: **Extract** > **Extract to "Request Example"**.
 
<Background>
![Extract request parameters as examples](https://api.apidog.com/api/v1/projects/544525/resources/351642/image-preview)
</Background>
  </Step>
  <Step title="Choose the Extraction option">
  You'll be prompted to choose how to save the request parameters:

 - **Overwrite the Example**: Replace a previously saved example.
 - **New Example**: Save it as a brand-new example.

<Background>
![Choose extraction options](https://api.apidog.com/api/v1/projects/544525/resources/351643/image-preview)
</Background>
  </Step>
</Steps>

:::tip
The current debugging value will be automatically filled into the example by default.
:::

## Use Scenarios

### Using Request Body Examples During Debugging

<Steps>
  <Step title="">
  Go to the **Run** page of the endpoint documentation and locate the **Auto-generate** section.
  </Step>
    
  <Step title="">
  Click the dropdown menu to select a request body example. The example will automatically populate.

<Background>
![Switch request body examples during debugging](https://api.apidog.com/api/v1/projects/544525/resources/351646/image-preview)
</Background>
  </Step>
  <Step title="">
  You can switch between examples in real-time and send requests with the selected example.
  </Step>
</Steps>

:::info[Advanced Settings]
Click the dropdown icon next to **Auto-generate** to access the following options:

- **EXAMPLES**: Choose from predefined request body examples.
- **Generate Each Time**: Automatically generate random values based on [mock rules](https://docs.apidog.com/smart-mock-618190m0.md).
- **Auto-generation Preference**: For more advanced configurations, refer to [Generate Requests](https://docs.apidog.com/generating-requests-541765m0.md).
:::

### Documentation Display

- **For single request body example**: Shown in a simplified view without displaying the example name.

<Background>
![Single request body display](https://api.apidog.com/api/v1/projects/544525/resources/351648/image-preview)
</Background>

- **For multiple request body examples**: Allows switching between examples in a side-by-side layout, displaying example names and Markdown descriptions.

<Background>
![Request body examples display](https://api.apidog.com/api/v1/projects/544525/resources/351647/image-preview)
</Background>

:::tip[Display Order]
The display order for request body examples follows this priority:

1. Example Name > OAS Key > Serial Number (auto-incremented from `1`).
2. Non-empty items are displayed first.
:::

## OAS Compliance

### OAS Key

OAS key controls the field names of the examples when exporting OpenAPI specifications.

1. **Configuration**: Fill in the **OAS Key** for the request body examples.

<Background>
![Configuring request body OAS key](https://api.apidog.com/api/v1/projects/544525/resources/351649/image-preview)
</Background>

2. **Export Rules**:

- **When filled**: The provided OAS key is used as the field name within the object `examples`.
- **When not filled**: Serial numbers (starting from `1`) are automatically used as field names.

<Container>
  <Columns>
      <Column>
            **When filled**
      </Column>
      <Column>
        **When not filled:**
      </Column>
  </Columns>
    ---
  <Columns>
      <Column>

        ```json
         "examples": {
           "example1": {
              "value": {
                "name": "Blake Keeling",
                "id": "165061",
                "email": "Blake.Keeling@gmail.com"
              },
              "summary": "example1",
              "description": "This is`example 1`"
            },
            "example2": {
               "value": {
                "name": "Jolie Kutch",
                "id": "138164",
                "email": "Jolie_Kutch@hotmail.com"
              },
              "summary": "example 2",
              "description": "This is`example 2`"
            }
          }       
        ```

      </Column>
      <Column>
         ```json
         "examples": {
            "1": {
              "value": {
                "name": "Blake Keeling",
                "id": "165061",
                "email": "Blake.Keeling@gmail.com"
              },
              "summary": "example1",
              "description": "This is`example 1`"
            },
             "2": {
               "value": {
                "name": "Jolie Kutch",
                "id": "138164",
                "email": "Jolie_Kutch@hotmail.com"
              },
              "summary": "example 2",
              "description": "This is`example 2`"
            }
          }       
        ```

      </Column>
    </Columns>
</Container>

### OAS Extensions

You can add custom OpenAPI Specification (OAS) extensions to examples.

1. **Configuration**: Input JSON key-value pairs in the OAS Extension field.

```json
{
  "x-demo": true,
  "x-scenario": "error_case"
}
```

<Background>
![Add OAS extensions to examples](https://api.apidog.com/api/v1/projects/544525/resources/351679/image-preview)
</Background>

2. **Export Effect**: The custom OAS extensions will be fully preserved and included in the exported OpenAPI specifications.

```json
"examples": {
    "example1": {
      "x-demo": true,
      "x-scenario": "error_case",
      "value": {
         "name": "Blake Keeling",
         "id": "165061",
         "email": "Blake.Keeling@gmail.com"
      },
      "summary": "example1",
      "description": "This is`example 1`"
    }
}
```

## FAQs

<Accordion title="How to Enable Multiple Request Body Examples in Old Projects?" defaultOpen>
No manual action is required! When you add a second request body example to an existing endpoint, the system automatically upgrades the format to support multiple examples.
</Accordion>

<Accordion title="How to Handle Multiple Request Body Examples When Exporting OAS?" defaultOpen={false}>    
The system automatically generates an example object following OAS 3.1 specifications. It uses the **OAS Key** as the unique identifier. If no **OAS Key** is provided, serial numbers (starting from 1) are used instead.
   
<Background>
![Exported OAS specifications](https://api.apidog.com/api/v1/projects/544525/resources/351680/image-preview)
</Background>
</Accordion>

<Accordion title="Will the Order of the Request Body Examples Change in the Exported OAS?" defaultOpen={false}>
No, the order of examples in the exported specifications will match the order in which they were added in Apidog.
</Accordion>

<Accordion title="How to Make Exported Example Names More Friendly?" defaultOpen={false}>
Fill in the **OAS Key** for the request body example (e.g., example1). This name will be used as the example key during export, making it more user-friendly and descriptive.
    
<Container>
  <Columns>
      <Column>
            **Configuration**
      </Column>
      <Column>
        **Exported Example**
      </Column>
  </Columns>
    ---
  <Columns>
      <Column>
        
<Background>
![Request body example OAS key](https://api.apidog.com/api/v1/projects/544525/resources/351681/image-preview)
</Background>

      </Column>
      <Column>

<Background>
![Request body example exported with OAS key](https://api.apidog.com/api/v1/projects/544525/resources/351683/image-preview)
</Background>

      </Column>
    </Columns>
</Container>

</Accordion>

