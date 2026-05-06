# Adding an Assertion

For saved endpoints, you can add **pre-** and **post-processors** to prepare data or test the endpoint. **Assertions** are a type of post-processor in Apidog that allow you to validate API responses.

## Prerequisites

Before adding assertions, ensure you have:
- At least one saved [endpoint](https://docs.apidog.com/creating-an-endpoint-644726m0.md) that you want to add assertions to
- Basic understanding of JSON and API response structures

## Steps to Add an Assertion

<Steps>
  <Step>
    Click on the **Post Processors** tab.
      <details>
<summary>📷 Visual Reference</summary>
    <Background>
![image.png](https://api.apidog.com/api/v1/projects/544525/resources/369351/image-preview)
    </Background>
      </details>
  </Step>
  <Step>
    Click on **Add PostProcessor** and select **Assertion**.
  </Step>
  <Step>
    Fill in the Assertion form with the validation details. For example, to assert that the response `category id` is positive:
    
    | Field               | Value                     |
    |---------------------|---------------------------|
    | Name                | "id" is a positive integer|
    | Target Object       | Response JSON             |
    | JSONPath Expression | `$.category.id`           |
    | Assertion Rule      | Greater than              |
    | Assertion Value     |         0                 |

:::tip[]
**JSONPath** is a query language for JSON, used to select and extract data from JSON documents. You can click on the 🔨 icon in the JSONPath Expression field to visually extract any JSONPath expression.
:::

    
  </Step>
  <Step>
    Click **Send**, and you will see the Assertion result in the bottom right corner.
      <details>
<summary>📷 Visual Reference</summary>
    <Background>   
![image.png](https://api.apidog.com/api/v1/projects/544525/resources/369353/image-preview)
    </Background>
      </details>
  </Step>
  <Step>
    Click **Save** to save the changes you made.
  </Step>
</Steps>


:::tip[]
- In Apidog, you can visually add assertions, [extract variables](https://docs.apidog.com/extract-variable-588468m0.md), [perform database operations](https://docs.apidog.com/database-operations-in-apidog-588469m0.md), and more. Learn more about [pre and post processors](https://docs.apidog.com/prepost-processors-in-apidog-588246m0.md).

- You can also write assertions or implement other operations using scripts by simply adding a "Custom script". Apidog is compatible with Postman scripts, which can run in Apidog without modification. Learn more about [Scripts](https://docs.apidog.com/use-scripts-in-apidog-593582m0.md).
:::

---

<CardGroup cols={2}>
  <Card title="Next Step" href="https://docs.apidog.com/creating-test-scenarios-645499m0.md">
    Create a test scenario
  </Card>
</CardGroup>
