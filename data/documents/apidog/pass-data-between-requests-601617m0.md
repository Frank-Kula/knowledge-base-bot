# Pass Data Between Requests

In automated testing scenarios, passing data between multiple requests is very common. Typical cases include:
- Request 1 is a login request that returns a token; Request 2 uses this token to request other data.
- Request 1 returns an ID; Request 2 performs operations based on this ID.
- Request 1 returns a list; Request 2 uses data from this list.

For such scenarios, Apidog provides two different solutions to handle data passing between requests. You can choose the appropriate solution based on the specific problem at hand.

| Method | Advantages | Limitations | Availability |
|--------|------------|-------------|--------------|
| **Retrieve pre-step data** | Simple, no additional variables needed | Slightly cumbersome when data needs to be referenced multiple times | Tests module only |
| **Use variables** | Convenient for multiple references | Slightly more complex for single references | Tests and APIs modules |

## Retrieve Pre-Step Data

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
<Background>
<img src="https://api.apidog.com/api/v1/projects/544525/resources/343044/image-preview" style="width:640px" />
</Background>
    </Step>
  <Step>
Choose Request 1 for data retrieval, select the response body, and use JSONPath to extract the token returned by Request 1, like `$.token`.
<Background>
<img src="https://api.apidog.com/api/v1/projects/544525/resources/343042/image-preview" style="width:300px" />
</Background>

    </Step>
    <Step>
Click Insert, and you'll see `{{$.2.response.body.token}}` inserted as the query param.
<Background>
<img src="https://api.apidog.com/api/v1/projects/544525/resources/343045/image-preview" style="width:640px" />
</Background>
    
    </Step>
    <Step>
Click the "Run" button in the Test scenario to successfully pass the data from Request 1 to Request 2.

    </Step>
</Steps>

:::tip[]
- The feature of "Retrieve pre-step data" is ONLY AVAILABLE in the "Tests" module and not in the "APIs" module. 
- When using "Retrieve pre-step data", the value can ONLY be obtained when the entire test scenario is run together; it cannot be accessed when running individual steps.
:::

### Referencing Pre-Step Data Using Variable Syntax

Using the example of `{{$.2.response.body.token}}` from the previous text:
- '2' represents the step ID, which can be found in each test step.
<Background>
<img src="https://api.apidog.com/api/v1/projects/544525/resources/343046/image-preview" style="width:300px" />
</Background>
- 'response.body' indicates the position of the data from the pre-step. This can include data from the request's header, body, or the response's header or body, among others. See below for specifics.
<Background>
<img src="https://api.apidog.com/api/v1/projects/544525/resources/343047/image-preview" style="width:300px" />
</Background>
- 'token' represents the 'token' data at the next level within the body. You can use JSONPath syntax to extract the desired data.

Pre-step data can be utilized in various parts of the request, such as request parameters, headers, authentication, and more. You can also directly insert the data into the request body, as shown below.
<Background>
<img src="https://api.apidog.com/api/v1/projects/544525/resources/343051/image-preview" style="width:400px" />
</Background>

It's important to note that if you need to use pre-step data in your scripts, you cannot directly reference variables using `{{variable}}` syntax. Instead, you should use `pm.variables.get` to reference pre-step data. For example:
```javascript
var token = pm.variables.get("$.2.response.body.token")
```

### Syntax Reference

| Category | Function | Syntax Example |
|----------|----------|----------------|
| **Request** | URL | `{{$.<step id>.request.url}}` |
| | Path parameter | `{{$.<step id>.request.pathParam.<field name>}}` |
| | Query | `{{$.<step id>.request.query.<field name>}}` |
| | Header | `{{$.<step id>.request.header.<field name>}}` |
| | Body (form) | `{{$.<step id>.request.body.<field name>}}` |
| | Body (json) | `{{$.<step id>.request.body.<field path>}}` |
| **Response** | Body | `{{$.<step id>.response.body.<field path>}}` |
| | Header | `{{$.<step id>.response.header.<field name>}}` |
| | Cookie | `{{$.<step id>.response.cookie.<field name>}}` |
| **Loop** | Element (array element in ForEach loop) | `{{$.<loop step id>.element.<field path>}}` |
| | Index | `{{$.<loop step id>.index}}` |

## Use Variables to Pass Data

Let's consider a scenario where Request 1 is a login request that returns a token, and Request 2 uses this token to request additional data.

<Steps>
  <Step>
Add the login request (Request 1) to the test scenario.
    </Step>
  <Step>
In the post processors of Request 1, add an "Extract Variable" action to extract `$.token` as `{{token}}`.
<Background>
<img src="https://api.apidog.com/api/v1/projects/544525/resources/343049/image-preview" style="width:640px" />
</Background>

:::highlight purple
Learn more about [Extract variable](https://docs.apidog.com/extract-variable-588468m0.md).
:::
    </Step>
  <Step>
Add the query request (Request 2) to the test scenario.

    </Step>
  <Step>
Reference the variable `{{token}}` in the query parameters of Request 2.
<Background>
<img src="https://api.apidog.com/api/v1/projects/544525/resources/343050/image-preview" style="width:640px" />
</Background>
    </Step>

    <Step>
Click the "Run" button in the Test scenario to successfully pass the data from Request 1 to Request 2.

    </Step>
</Steps>

## FAQ

**Q: Why am I not able to successfully reference pre-step data?**

A: Firstly, make sure you're now in "Tests" module. "Referencing pre-step data" feature is available only in Tests module but not APIs module.

If you're now surely in Tests module, switch to the "Actual Request" tab to confirm whether the pre-step data referenced in the request has been successfully incorporated. 

If the reference in the actual request still appears as `{{$.n.response.body.abc}}` instead of showing actual data, it indicates that the reference has not been applied. 

In this case, consider the following common reasons:
1. Have you run the entire test scenario instead of just a single step? Referencing pre-step data requires running the complete test scenario for it to take effect.
2. Verify if the step ID is correct and corresponds to the step you intend to reference.
3. Ensure that the JSONPath used matches the data source accurately.

