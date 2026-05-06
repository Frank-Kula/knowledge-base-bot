# Add an assertion

In our saved endpoint case, we can also add pre/post operations to prepare data or test this endpoint.

<Steps>
  <Step>
Switch to **Post processors**.
    </Step>
  <Step>
Hover over **Add PostProcessor**, select **Assertion**.
<Background>
![CleanShot 2024-08-28 at 14.44.26@2x.png](https://api.apidog.com/api/v1/projects/544525/resources/344572/image-preview)
</Background>
    </Step>
  <Step>
In this case, I want to assert that if the response "id" is a positive integer.
So fill in the Assertion form:
**Name**: "id" is a positive integer
**Target Object**: Response JSON
**JSONPath expression**: `$.category.id`
**Assertion**: Greater than 0

    </Step>
  <Step>
Click **Send**, and you will see the Assertion result in the bottom right corner.
<Background>
![image.png](https://api.apidog.com/api/v1/projects/544525/resources/344573/image-preview)
</Background>     
    </Step>
  <Step>
Click "Save" to save the endpoint case.
    </Step>
</Steps>


:::tip[]
- In Apidog, you can visually [add assertions](https://docs.apidog.com/add-an-assertion-645440m0.md), [extract variables](https://docs.apidog.com/extract-variable-588468m0.md), [perform database operations](https://docs.apidog.com/database-operations-in-apidog-588469m0.md), and more. Learn more about [pre and post processors](https://docs.apidog.com/prepost-processors-in-apidog-588246m0.md).

- You can also write assertions or implement other operations using scripts by simply adding a "Custom script". Apidog is compatible with Postman scripts, which can run in Apidog without modification. Learn more about [Scripts](https://docs.apidog.com/use-scripts-in-apidog-593582m0.md).
:::

<CardGroup cols={2}>
  <Card title="Next Step" href="https://docs.apidog.com/create-a-test-scenario-645499m0">
    Create a test scenario
  </Card>
</CardGroup>
