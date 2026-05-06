# Postman Scripts Reference

Apidog's scripting engine uses the `pm` object to access data about the request, response, and variables. This method is compatible with Postman.

## `pm` Object
The `pm` object has the following main properties. 

| Property | Data Type | Description |
|----------|-----------|-------------|
| `pm.info.eventName` | String | The type of scripts that is currently running (preprocessor script or postprocessor script). |
| `pm.info.iteration` | Number | The number of the current iteration (only valid in test collections). |
| `pm.info.iterationCount` | Number | The number of total iterations (only valid in test collections). |
| `pm.info.requestName` | String | The name of the current API running. |
| `pm.info.requestId` | String | The ID of the current API running. |

### Sending Requests (`pm.sendRequest`)

`pm.sendRequest:Function`

`pm.sendRequest` is used to send asynchronous HTTP/HTTPS requests in scripts.

- This method accepts a request parameter compatible with collection SDK- and a callback function parameter. The callback has 2 arguments. The first is an error and the second is a response compatible with the collection SDK. View more information in the [Collection SDK documentation](http://www.postmanlabs.com/postman-collection/Request.html#~definition).
- You can use it in both preprocessor and postprocessor scripts.

```js
// GET example
pm.sendRequest("https://postman-echo.com/get", function(err, res) {
  if (err) {
    console.log(err);
  } else {
    pm.environment.set("variable_key", "new_value");
  }
});

// Request Parameters Example
const echoPostRequest = {
  url: "https://postman-echo.com/post",
  method: "POST",
  header: {
    headername1: "value1",
    headername2: "value2",
  },
  // body: x-www-form-urlencoded
  body: {
    mode: "urlencoded",
    urlencoded: [
      { key: "account", value: "apidog" },
      { key: "password", value: "123456" },
    ],
  },
};
pm.sendRequest(echoPostRequest, function(err, res) {
  console.log(err ? err : res.json());
});

// Assert on the return result
pm.sendRequest("https://postman-echo.com/get", function(err, res) {
  if (err) {
    console.log(err);
  }
  pm.test("response should be okay to process", function() {
    pm.expect(err).to.equal(null);
    pm.expect(res).to.have.property("code", 200);
    pm.expect(res).to.have.property("status", "OK");
  });
});
```

For more references, please visit:

- [Request JSON ](http://www.postmanlabs.com/postman-collection/Request.html#~definition)structure
- [Response ](http://www.postmanlabs.com/postman-collection/Response.html)structure

### pm.variables

`pm.variables:`view[ Variable SDK](https://www.postmanlabs.com/postman-collection/Variable.html) documentation here.

Local variables.The priority of different variables is as follows: 

`Local Variables` > `Environment Variables` > `Global Variables Shared within Project` > `Global Variables Shared within Team`.

- `pm.variables.has(variableName:String):function → Boolean`: Check whether a temporary variable exists.
- `pm.variables.get(variableName:String):function → *`: get a temporary variable.
- `pm.variables.set(variableName:String, variableValue:String):function → void`: set a temporary variable.
- `pm.variables.replaceIn(variableName:String):function`: Replaces "dynamic variables" within a string (e.g., {{variable_name}}) with actual values. Example:
```
// Define a string containing a dynamic variable
let stringWithVariable = "Hello, {{username}}";

// Use the replaceIn method to replace the {{username}} placeholder
let realValueString = pm.variables.replaceIn(stringWithVariable);

// Output the replaced value
console.log(realValueString); // Output: "Hello, john_doe"
```
- `pm.variables.replaceInAsync(variableName:String):function`: Replaces "dynamic value expressions" within a string (e.g., {{$person.fullName}}) with actual values. This method returns a Promise, so you need to use await when calling it. Example:
```
// Define a string containing a dynamic value expression
let stringWithVariable = "Hello, {{$person.fullName}}";

// Use the replaceInAsync method to replace the {{$person.fullName}}
let realValueString = await pm.variables.replaceInAsync(stringWithVariable);
```  
- `pm.variables.toObject():function → Object`: get all local variables as objects.

### pm.iterationData

`pm.iterationData:`

Test Data Variables

We currently do not support setting test data variables directly in scripts, since test data is managed separately. However, you can access the variables in scripts as shown below:

- `pm.iterationData.has(variableName:String):function → Boolean`: Check whether a test variable exists.
- `pm.iterationData.get(variableName:String):function → *`: get a test variable.
- `pm.iterationData.replaceIn(variableName:String):function`: replace dynamic variables in a string with their actual values, for example, `{{variable_name}}`.
- `pm.iterationData.toObject():function → Object`: get all local variables as objects.

### pm.environment

- `pm.environment.name:String`: the environment name.
- `pm.environment.has(variableName:String):function → Boolean`:Check whether an environment variable exists.
- `pm.environment.get(variableName:String):function → *`: get an environment variable.
- `pm.environment.set(variableName:String, variableValue:String):function`:set an environment variable.
- `pm.environment.replaceIn(variableName:String):function`: replace dynamic variables in a string with their actual values, for example, `{{variable_name}}`.
- `pm.environment.toObject():function → Object`: get all local variables as objects.
- `pm.environment.unset(variableName:String):function`: unset an environment variable.
- `pm.environment.clear():function`: clear all environment variables under the current environment.

TIP the operations mentioned above only read and write current values; they do not read or write remote values.

### pm.moduleVariables

`pm.moduleVariables: Object`

Used to manage the **Current Value** of module-level variables.

* `pm.moduleVariables.has(variableName: String): function → Boolean`
  Checks whether a specific module variable exists.

* `pm.moduleVariables.get(variableName: String): function → *`
  Retrieves the value of a specific module variable.

* `pm.moduleVariables.set(variableName: String, variableValue: String): function`
  Sets the value of a specific module variable.

* `pm.moduleVariables.replaceIn(variableName: String): function`
  Replaces `{{variable}}` placeholders within a string with their actual values.

* `pm.moduleVariables.toObject(): function → Object`
  Returns all module variables as a key-value object.

* `pm.moduleVariables.unset(variableName: String): function`
  Deletes a specific module variable.

* `pm.moduleVariables.clear(): function`
  Clears all module variables within the current module.

**Example:**

```js
pm.moduleVariables.set("token", "abc123");
console.log(pm.moduleVariables.has("token")); // true
console.log(pm.moduleVariables.get("token")); // abc123
console.log(pm.moduleVariables.replaceIn("Token is {{token}}")); // Token is abc123
console.log(pm.moduleVariables.toObject());
pm.moduleVariables.unset("token");
```

> **Compatibility Note:**
> `pm.collectionVariables` works the same way as `pm.moduleVariables` and can be used interchangeably.


### pm.globals

- `pm.globals.has(variableName:String):function → Boolean`: Check whether a global variable exists.

- `pm.globals.get(variableName:String，variableScope:String):function → *`: get a global variable. Use 'PROJECT' (default) or 'TEAM' to specify the variable's scope.

- `pm.globals.set(variableName:String，variableValue:String， variableScope:String):function`: set a global variable. Use 'PROJECT' (default) or 'TEAM' to specify the variable's scope.

- `pm.globals.replaceIn(variableName:String):function`: replace dynamic variables in a string with their actual values, for example, `{{variable_name}}`.

  > In order to get the value of a request parameter that contains a variable in preprocessor scripts, use `pm.globals.replaceIn` to replace the variable with the real value.

- `pm.globals.toObject():function → Object`: get all global variables as objects.

- `pm.globals.unset(variableName:String，variableScope:String):function`: unset a global variable. Use 'PROJECT' (default) or 'TEAM' to specify the variable's scope.

- `pm.globals.clear():function`: clear all global variables under the current environment.

:::tip 
1. All operations above affect only`current values`, not`initial values`.
2. When using set with the 'TEAM' scope, it will only update the current value of an existing team variable. If the team variable doesn't exist, it will not be created. Instead, the variable will be treated as a local variable.
:::

### pm.request

`pm.request`: view [Request SDK](https://www.postmanlabs.com/postman-collection/Request.html) documentation here.

`request` is the API request object. In the preprocessor script, it is the request that will be sent. In the postprocessor script, it is the request that has already been sent.

`request` includes the following information:

- `pm.request.url`:[Url](http://www.postmanlabs.com/postman-collection/Url.html): the URL of the current request.
- `pm.request.getBaseUrl()`: Retrieves <code>BASE URL</code> selected by the current runtime environment. This feature is supported after version 2.1.39.
- `pm.request.headers`:[HeaderList](http://www.postmanlabs.com/postman-collection/HeaderList.html): the header list of the current request.
  - `pm.request.method`:String: the method of the current request, such as GET, POST, etc.
- `pm.request.body`: [RequestBody](http://www.postmanlabs.com/postman-collection/RequestBody.html): the body of the current request.
- `pm.request.headers.add({ key: headerName:String, value: headerValue:String}):function`: Add a header with a key, headerName, in the current request.
- `pm.request.headers.remove(headerName:String):function`: Delete a header with a key, headerName, in the current request.
- `pm.request.headers.upsert({ key: headerName:String, value: headerValue:String}):function`: Upsert a header with a key, headerName, in the current request. If the key already exists, it will be modified.

> The following API can only be used in`postprocessor scripts`.

### pm.response

`pm.response`: view [Response SDK documentation ](https://www.postmanlabs.com/postman-collection/Response.html) here.

Use `pm.response` to access return response information in postprocessor scripts.

pm.response includes the following information:

- `pm.response.code:Number`
- `pm.response.status:String`
- `pm.response.headers`:[HeaderList](http://www.postmanlabs.com/postman-collection/HeaderList.html)
- `pm.response.responseTime:Number`
- `pm.response.responseSize:Number`
- `pm.response.text():Function → String`
- `pm.response.json():Function → Object`

### pm.cookies

pm.cookies: view [CookieList SDK documentation](https://www.postmanlabs.com/postman-collection/CookieList.html) here.

Cookies is the list of cookies under the domain name of the current request.

- `pm.cookies.has(cookieName:String):Function → Boolean`
  Check whether the cookie value of a cookieName exists.
- `pm.cookies.get(cookieName:String):Function → String`
  Get cookie value from cookieName.
- `pm.cookies.toObject:Function → Object`
  Get all cookies under the current domain as an object.
- `pm.cookies.jar().clear(pm.request.url)`
  Clear all cookies.

:::tip TIP
  pm.cookies is the cookie returned after the API request, not the cookie sent by the API request.
:::

### pm.test

```js
pm.test(testName:String, specFunction:Function):Function
```

This function is used to assert whether a result meets expectations.

The example below can be used to determine whether a response is correct.

```js
pm.test("response should be okay to process", function() {
  pm.response.to.not.be.error;
  pm.response.to.have.jsonBody("");
  pm.response.to.not.have.jsonBody("error");
});
```

You can run an async test using `done`(an optional parameter) in a callback function.

```js
pm.test("async test", function(done) {
  setTimeout(() => {
    pm.expect(pm.response.code).to.equal(200);
    done();
  }, 1500);
});
```

- `pm.test.index():Function → Number`
  Get the total number tests from a specific location.

### pm.expect

```js
pm.expect(assertion:*):Function → Assertion
```

`pm.expect` is an assertion method. View ChaiJS expects BDD library documentation here.

This method is designed to assert data in response or variables. For more pm.expect examples, please visit[ Assertion library examples](https://learning.postman.com/docs/writing-scripts/script-references/test-examples/).

### pm.response.to.have.\*

- `pm.response.to.have.status(code:Number)`
- `pm.response.to.have.status(reason:String)`
- `pm.response.to.have.header(key:String)`
- `pm.response.to.have.header(key:String, optionalValue:String)`
- `pm.response.to.have.body()`
- `pm.response.to.have.body(optionalValue:String)`
- `pm.response.to.have.body(optionalValue:RegExp)`
- `pm.response.to.have.jsonBody()`
- `pm.response.to.have.jsonBody(optionalExpectEqual:Object)`
- `pm.response.to.have.jsonBody(optionalExpectPath:String)`
- `pm.response.to.have.jsonBody(optionalExpectPath:String, optionalValue:*)`
- `pm.response.to.have.jsonSchema(schema:Object)`
- `pm.response.to.have.jsonSchema(schema:Object, ajvOptions:Object)`

### pm.response.to.be.\*

You can use the built-in`pm.response.to.be`for quick assertions.

- `pm.response.to.be.info`
  Check whether the status code is 1XX.
- `pm.response.to.be.success`
  Check whether the status code is 2XX.
- `pm.response.to.be.redirection`
  Check whether the status code is 3XX.
- `pm.response.to.be.clientError`
  Check whether the status code is 4XX.
- `pm.response.to.be.serverError`
  Check whether the status code is 5XX.
- `pm.response.to.be.error`
  Check whether the status code is 4XX or 5XX.
- `pm.response.to.be.ok`
  Check whether the status code is 200.
- `pm.response.to.be.accepted`
  Check whether the status code is 202.
- `pm.response.to.be.badRequest`
  Check whether the status code is 400.
- `pm.response.to.be.unauthorized`
  Check whether the status code is 401.
- `pm.response.to.be.forbidden`
  Check whether the status code is 403.
- `pm.response.to.be.notFound`
  Check whether the status code is 404.
- `pm.response.to.be.rateLimited`
  Check whether the status code is 429.
