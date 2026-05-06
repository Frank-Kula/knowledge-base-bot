# Specify a new endpoint


An Endpoint represents a specific API endpoint or route. It's the core building block for defining, testing, and documenting an API in Apidog.

Apidog provides an intuitive UI for API designers to specify their APIs. Let's walk through an example:

## Creating an Endpoint

This example demonstrates how to create an endpoint for querying user information by ID.

<Steps>
  <Step>
  **Create a New API:** Open a new tab and click `New API`.
      
<Background>      

![CleanShot 2025-11-05 at 16.57.21@2x.png](https://api.apidog.com/api/v1/projects/544525/resources/365346/image-preview)
</Background>     
    </Step>
<Step>
  **Define the Request Path:** 
      In the API path field, enter `/category/{id}`. This sets up the base for the **Request** section. 
   - **Name:**  Get category by id
   - **Path params:**
     - **Name:** id
     - **Type:** integer
     - **Example:** 1
 
<Background>
![specify api](https://api.apidog.com/api/v1/projects/544525/resources/344526/image-preview)
</Background>
:::tip[]
If your interface does not match the image above, please switch to `Design-first Mode`.
    
![image.png](https://api.apidog.com/api/v1/projects/544525/resources/352123/image-preview)
:::
    </Step>
  <Step>
  **Define the Response Structure:**
    - Scroll to the `Responses` section.
    - In the 'OK(200)' response, hover over the '+' icon and click to create a child node named "data".
<Background>      
![schema-reference](https://assets.apidog.com/help/assets/images/specify-a-New-API-3-2d5491bc4bc24a94701ca098e18d177e.png)
</Background>
    </Step>
  <Step>
  **Use a Schema Reference:**
    - Hover over the 'data' node.
    - Click the type `String` to change it to 'Schema Reference'.
    - Choose "Category" (or your relevant schema) from the list. 
<Background>      
![schema-reference](https://api.apidog.com/api/v1/projects/544525/resources/344527/image-preview)
</Background>
    </Step>
  <Step>
  **Add a Response Example:**
    - Scroll to the `Response Examples` section.
    - Click `Add Example`.
<Background>
![image.png](https://api.apidog.com/api/v1/projects/544525/resources/344528/image-preview)
</Background>
    </Step>
  <Step>
  **Generate Example Data:**
    - Name the example 'Success'.
    - Click `Auto-generate` to populate the response data based on your defined structure.
    - Click `OK` to add the example.
<Background>
![image.png](https://api.apidog.com/api/v1/projects/544525/resources/344529/image-preview)
</Background>
    </Step>
  <Step>
  **Save Your Endpoint:** Click `Save` to finalize your API specification. 
<Background>
![image.png](https://api.apidog.com/api/v1/projects/544525/resources/344530/image-preview)
</Background>
    </Step>
</Steps>

## Related

### Importing Existing APIs

You can import an existing OAS file instead of creating a new endpoint from scratch. 
:::tip[]

For details, see [Import data](https://docs.apidog.com/migration-guide-overview-633036m0.md).
:::

### Using Schemas
For commonly used data structures, define them as **Schemas**. You can then reference these Schemas in your endpoint requests or responses. 
:::tip[]
Learn more about [Schemas](https://docs.apidog.com/introduction-to-schema-533975m0.md).
:::

<CardGroup cols={2}>
  <Card title="Next Step" href="https://docs.apidog.com/send-an-api-request-645415m0">
    Make a request to the endpoint
  </Card>
</CardGroup>
