# Debugging Cases

Apidog distinguishes between endpoints and debug cases. Each endpoint can have multiple debug cases linked to it. When you update the endpoint's URL or parameters, all related debug cases are automatically updated — no extra effort needed.

In comparison, Postman handles everything as separate, standalone requests. This means if you make a change to a URL or parameter, you’ll need to manually update every affected request one by one.

<Background>
![Endpoint and case comparison](https://api.apidog.com/api/v1/projects/544525/resources/354121/image-preview)
</Background>

## Creating a Debug Case

<Video src="https://www.youtube.com/watch?v=bdOIzLqGVc4"></Video>

When you send a request or debug in the **Run** tab of an endpoint, if you want to save the request permanently, you can click on **Save as case**. This action will preserve the request as a debug case within the endpoint's structure.

<Background>
<p style="text-align: center">
    <img src="https://api.apidog.com/api/v1/projects/544525/resources/361788/image-preview" style="width: 640px" />
</p>
</Background>

You can name the debug case and choose whether to save the response simultaneously.

<Background>
<p style="text-align: center">
    <img src="https://api.apidog.com/api/v1/projects/544525/resources/361790/image-preview" style="width: 440px" />
</p>
</Background>

## What is Saved in Debug Cases

As mentioned earlier, the endpoint specification is saved within the endpoint, while the values are stored in the debug case. Specifically, a debug case includes the following data:

- **Request parameter values**: Covering path parameters, query parameters, header parameters, and body parameters in form-data format.
- **Body content**: In formats like RAW, JSON, XML, etc.
- **Pre- and post-request processors**.
- **Received response details**.
- **Response validation settings**: Indicating whether validation is enabled and specifying which response to validate against.

Therefore, if you modify the specification of a parameter in the endpoint spec, the debug case will be updated in real-time.

## Referencing Debug Cases in Automated Tests

Debug cases can be referenced as test steps in automated test scenarios. When referenced, the request parameters in the debug case will be applied directly to the test step. You can see a clear notification that any changes made to the debug case will automatically update all test steps that reference it.

Click the referencing icon at the top-right corner to view which test scenarios reference the debug case and the total number of test scenarios that use it. This gives you an overview of how it is used in automated tests.

<Background>
![Referencing debug case as test step](https://api.apidog.com/api/v1/projects/544525/resources/348286/image-preview)
</Background>

Clicking a test scenario takes you to the scenario detail page, where related steps using the case are highlighted for easy viewing.

<Background>
![View test scenarios referencing the case](https://api.apidog.com/api/v1/projects/544525/resources/348287/image-preview)
</Background>

Clicking a test step that references the debug case will notify you that any changes will sync with the original case.

<Background>
![Sync notification](https://api.apidog.com/api/v1/projects/544525/resources/348288/image-preview)
</Background>

## Best Practices for Using Debug Cases

1. Define API specifications thoroughly.
2. Create multiple debug cases for each endpoint to cover different conditions.
3. For each debug case, write assertions or other pre- and post-request processors.
4. Reference debug cases in automated tests to compose test scenarios.
5. If there are updates to the API specifications, both the debug cases and test scenarios can be synchronized. You can choose to update test scenarios manually or set them to update automatically.

