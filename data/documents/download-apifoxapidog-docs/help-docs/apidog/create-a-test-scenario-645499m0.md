# Create a test scenario

When you want to send a series of requests sequentially, you need to create a test scenario.

<Steps>
  <Step>
Switch to the Tests module and click "**New Test Scenario**". Enter a name to continue.
<Background>

![image.png](https://api.apidog.com/api/v1/projects/544525/resources/352124/image-preview)
</Background>
    </Step>
  <Step>
Hover over Add Step and select **Import from endpoint case**.
<Background>

![image.png](https://api.apidog.com/api/v1/projects/544525/resources/352125/image-preview)
</Background>
    </Step>
  <Step>
Select the following two cases in sequence:
a. *Add a new pet to the store (Success)*
b. *Find pet by ID (Pets sold)*

<Background>
    <img src="https://api.apidog.com/api/v1/projects/544525/resources/344576/image-preview" style="width:640px" />
</Background>
    </Step>
  <Step>
Now you can see the two requests you just selected on the interface. Currently, I want to first add a pet, and then use the ID to get the information of the just-added pet.

    </Step>
  <Step>
Click on *Find pet by ID (Pets sold)*, and you'll see the parameters for this request. In the Path param's **petId**, delete the original value, and then click the <Icon icon="ph-bold-magic-wand"/> **magic wand** button in the value box.
<Background>
![image.png](https://api.apidog.com/api/v1/projects/544525/resources/344577/image-preview)
 </Background>
    </Step>
  <Step>
I now want to get the ID of the pet I just added from the return result of the previous step. Select **Retrive pre-step data**, and choose the previous step *Add a new pet to the store (Success)*.
<Background>
    <img src="https://api.apidog.com/api/v1/projects/544525/resources/344578/image-preview" style="width:400px" />
</Background> 
    </Step>
  <Step>
Click the <Icon icon="ph-bold-arrow-square-out"/> button to the right of the JSONPath Expression, and you'll see the **JSONPath Extraction Tool**. In this tool, the left side is the return result of the previous step, and when you enter the JSONPath in the top right, the bottom right will display the extracted result. Now let's enter `$.data.id` in the top right, and you'll see the result is the ID of the pet I just added.
<Background>
      <img src="https://api.apidog.com/api/v1/projects/544525/resources/344579/image-preview" style="width:640px" />
</Background>
    </Step>
  <Step>
Go back to *Retrieve pre-step data* and click **Insert**, and the expression will be written into the Path param of the request.
<Background>
![image.png](https://api.apidog.com/api/v1/projects/544525/resources/344587/image-preview)
</Background>
    </Step>
  <Step>
Click **Save** in the top right, set the environment at the top to Local mock, and then click Run at the top right.
    </Step>
  <Step>
You can see a test report, and click each step to expand the request and response. You can see that the **id** in the path parameter of the second request is just the pet id returned from the first request. In this way, we have completed the data transfer between the requests.
<Background>
![image.png](https://api.apidog.com/api/v1/projects/544525/resources/344580/image-preview)
</Background>
    </Step>
</Steps>


:::tip[]
A test scenario includes a series of requests. These requests can be [imported into the test scenario from endpoint specs or endpoint cases](https://docs.apidog.com/create-a-test-scenario-599311m0.md), and can be [automatically or manually updated as the API spec changes](https://docs.apidog.com/sync-data-from-endpointsendpoint-cases-603709m0.md).

Test scenarios also support [logic components](https://docs.apidog.com/flow-control-conditions-599419m0.md) such as If, for, forEach, etc. You can [pass data between requests](https://docs.apidog.com/pass-data-between-requests-601617m0.md), [dynamically generate request parameters](https://docs.apidog.com/dynamic-values-541766m0.md), and more.
:::

:::tip[]
Based on test scenarios, you can also [view test reports](https://docs.apidog.com/test-reports-603898m0.md), [run performance tests](https://docs.apidog.com/performance-testing-603638m0.md), [manage test data](https://docs.apidog.com/data-driven-testing-602987m0.md), [integrate CI/CD](https://docs.apidog.com/cicd-in-apidog-609698m0.md), and more.
:::

<CardGroup cols={2}>
  <Card title="Next Step" href="https://docs.apidog.com/share-your-api-documentation-645507m0">
    Share your API documentation
  </Card>
</CardGroup>
