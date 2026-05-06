# Post Processor Scripts

Post-processor scripts are executed after the API response is received. They are primarily used for verifying response data (assertions) and extracting data into variables for future use.

## Use Cases & Examples

### Writing Assertions
Validate that the response meets expectations.

```javascript
// pm.response.to.have Example
pm.test("Return status code 200", function() {
  pm.response.to.have.status(200);
});

// pm.expect() Example
pm.test("The current environment is the production environment", function() {
  pm.expect(pm.environment.get("env")).to.equal("production");
});

// response assertions Example
pm.test("No error in return result", function() {
  pm.response.to.not.be.error;
  pm.response.to.have.jsonBody("");
  pm.response.to.not.have.jsonBody("error");
});

// pm.response.to.be* Example
pm.test("No error in return result", function() {
  // assert that the status code is 200
  pm.response.to.be.ok; // info, success, redirection, clientError,  serverError, are other variants
  // assert that the response has a valid JSON body
  pm.response.to.be.withBody;
  pm.response.to.be.json; // this assertion also checks if a body  exists, so the above check is not needed
});
```

### Extracting Variables
Parse the response and save data to variables.

```javascript
// Parse JSON response
var jsonData = pm.response.json();

// Save token to environment variable
pm.environment.set("token", jsonData.token);
```

:::highlight purple
For more detailed assertion examples, see **[Assertion Scripts](https://docs.apidog.com/assertion-scripts-593739m0.md)**.
:::

