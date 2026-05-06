# How to pass data between test steps?

In automated testing scenarios, passing data between multiple requests is very common. Typical cases include:
- Request 1 is a login request that returns a token; Request 2 uses this token to request other data.
- Request 1 returns an ID; Request 2 performs operations based on this ID.
- Request 1 returns a list; Request 2 uses data from this list.

For such scenarios, Apidog provides two different solutions to handle data passing between requests. You can choose the appropriate solution based on the specific problem at hand.
- **Retrieve pre-step data**: This feature allows you to directly use data from preceding requests in subsequent requests. 
    - The advantage is simplicity, without the need to introduce additional variables.
    - However, it may become slightly cumbersome when data needs to be referenced multiple times.
    - Retrieve pre-step data feature can be ONLY used in the "Tests" module and not in the "APIs" module.
- **Use variables**: Add "Extract Variables" in the pre-processor of the preceding request to store the required data in a variable, and then call this variable in the subsequent requests. 
    - The advantage is convenience when referencing data multiple times, but it may be slightly more complex for single references.
    - Variables can be used both in "Tests" module and "APIs" module.

## Retrieve pre-step data

Let's consider a scenario where Request 1 is a login request that returns a token, and Request 2 uses this token to request additional data.

<Steps>
  <Step>
Add the login request (Request 1) to the test scenario.
    </Step>
  <Step>
Add the query request (Request 2) to the test scenario.
    </Step>
  <Step>
The query parameter for Request 2 needs to include the token returned by Request 1. Click on the "magic wand" icon `🪄` in the token field in the query parameters of Request 2 and select "Retrieve pre-step data".
<p style="text-align:center">
    <img src="https://api.apidog.com/api/v1/projects/544525/resources/343044/image-preview" style="width:640px" />
</p>
    </Step>
  <Step>
Choose Request 1 for data retrieval, select the response body, and use JSONPath to extract the token returned by Request 1, like `$.token`.
<p style="text-align:center">
    <img src="https://api.apidog.com/api/v1/projects/544525/resources/343042/image-preview" style="width:300px" />
</p>

    </Step>
    <Step>
Click Insert, and you'll see `{{$.2.response.body.token}}` inserted as the query param.
<p style="text-align:center">
    <img src="https://api.apidog.com/api/v1/projects/544525/resources/343045/image-preview" style="width:640px" />
</p>
    
    </Step>
    <Step>
Click the "Run" button in the Test scenario to successfully pass the data from Request 1 to Request 2.

    </Step>
</Steps>

:::tip[]
- The feature of "Retrieve pre-step data" is ONLY AVAILABLE in the "Tests" module and not in the "APIs" module. 
- When using "Retrieve pre-step data", the value can ONLY be obtained when the entire test scenario is run together; it cannot be accessed when running individual steps.
:::

### Referencing pre-step data using variable syntax

Using the example of `{{$.2.response.body.token}}` from the previous text:
- '2' represents the step ID, which can be found in each test step.
<p style="text-align:center">
    <img src="https://api.apidog.com/api/v1/projects/544525/resources/343046/image-preview" style="width:300px" />
</p>
- 'response.body' indicates the position of the data from the pre-step. This can include data from the request's header, body, or the response's header or body, among others. See below for specifics.
<p style="text-align:center">
    <img src="https://api.apidog.com/api/v1/projects/544525/resources/343047/image-preview" style="width:300px" />
</p>
- 'token' represents the 'token' data at the next level within the body. You can use JSONPath syntax to extract the desired data.

Pre-step data can be utilized in various parts of the request, such as request parameters, headers, authentication, and more. You can also directly insert the data into the request body, as shown below.
<p style="text-align:center">
    <img src="https://api.apidog.com/api/v1/projects/544525/resources/343051/image-preview" style="width:400px" />
</p>

It's important to note that if you need to use pre-step data in your scripts, you cannot directly reference variables using `{{variable}}` syntax. Instead, you should use `pm.variables.get` to reference pre-step data. For example:
```javascript
var token = pm.variables.get("$.2.response.body.token")
```

### Syntax reference

<table border="1" cellpadding="1" cellspacing="1" style="border-collapse: collapse; border: none;">
  <thead>
    <tr>
      <th style="vertical-align: middle; text-align: left;"> Category </th> 
      <th style="vertical-align: middle; text-align: left;"> Function </th>
      <th style="vertical-align: middle; text-align: left;"> Syntax Example </th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="6">Request</td>
      <td>URL</td> 
      <td>{{$.&lt;step id>.request.url}}</td>
    </tr>
    <tr>
      <td>Path parameter</td>
      <td>{{$.&lt;step id>.request.pathParam.&lt;field name>}}</td> 
    </tr>
    <tr>
      <td>Query</td>
      <td>{{$.&lt;step id>.request.query.&lt;field name>}}</td>
    </tr>
    <tr>
      <td>Header</td>
      <td>{{$.&lt;step id>.request.header.&lt;field name>}}</td>
    </tr>
    <tr>
      <td>Body (form)</td> 
      <td>{{$.&lt;step id>.request.body.&lt;field name>}}</td>
    </tr>
    <tr>
      <td>Body (json)</td>
      <td>{{$.&lt;step id>.request.body.&lt;field path>}}</td>
    </tr>
    <tr>
      <td rowspan="3">Response</td>
      <td>Body</td>
      <td>{{$.&lt;step id>.response.body.&lt;field path>}}</td> 
    </tr>  
    <tr>
      <td>Header</td>
      <td>{{$.&lt;step id>.response.header.&lt;field name>}}</td>
    </tr>
    <tr>
      <td>Cookie</td>
      <td>{{$.&lt;step id>.response.cookie.&lt;field name>}}</td>
    </tr>
    <tr>
      <td rowspan="2">Loop</td>
      <td>Element (array element in ForEach loop)</td>  
      <td>{{$.&lt;loop step id>.element.&lt;field path>}}</td>
    </tr>
    <tr>
      <td>Index</td>
      <td>{{$.&lt;loop step id>.index}}</td>
    </tr>
  </tbody>
</table>

## Use variables to pass data

Let's consider a scenario where Request 1 is a login request that returns a token, and Request 2 uses this token to request additional data.

<Steps>
  <Step>
Add the login request (Request 1) to the test scenario.
    </Step>
  <Step>
In the post processors of Request 1, add an "Extract Variable" action to extract `$.token` as `{{token}}`.
<p style="text-align:center">
    <img src="https://api.apidog.com/api/v1/projects/544525/resources/343049/image-preview" style="width:640px" />
</p>

:::highlight purple
Learn more about [Extract variable](https://docs.apidog.com/extract-variable-588468m0.md).
:::
    </Step>
  <Step>
Add the query request (Request 2) to the test scenario.

    </Step>
  <Step>
Reference the variable `{{token}}` in the query parameters of Request 2.
<p style="text-align:center">
    <img src="https://api.apidog.com/api/v1/projects/544525/resources/343050/image-preview" style="width:640px" />
</p>
    </Step>

    <Step>
Click the "Run" button in the Test scenario to successfully pass the data from Request 1 to Request 2.

    </Step>
</Steps>
