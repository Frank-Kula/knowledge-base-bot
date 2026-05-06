# Mock Scripts

Mock scripts enable you to create intelligent mock responses with logical relationships between request parameters and response data. This feature is essential when you need mock data that maintains contextual accuracy or reflects request values.

## Use Cases

Mock scripts are ideal for scenarios requiring logical data relationships:

:::highlight purple
**Common Examples**
- Returning a user ID in the response that matches the requested ID (e.g., request ID 1001 → response includes ID 1001)
- Ensuring temporal consistency (e.g., end time is always after start time)
- Calculating related fields (e.g., total price based on quantity and unit price)
- Reflecting request parameters in the response payload
:::

## How Mock Scripts Work

Mock scripts process data through a five-step workflow:

<Steps>
  <Step>
    Smart mock or other mock features generate an initial response
  </Step>
  <Step>
    Mock script accesses the `$$.mockResponse` and `$$.mockRequest` objects
  </Step>
  <Step>
    JavaScript logic retrieves and processes data from these objects
  </Step>
  <Step>
    The `$$.mockResponse.setBody` method updates the response with modified data
  </Step>
  <Step>
    Mock engine returns the final processed response
  </Step>
</Steps>

:::caution[]
Mock scripts **only work with Smart mock**. They do not apply to mock expectations or response examples.
:::

## Using Mock Scripts

### Enabling and Writing Scripts

<Steps>
  <Step>
    Navigate to the **Mock** tab where the Mock Script section appears at the bottom
    <Background>
    ![image.png](https://api.apidog.com/api/v1/projects/544525/resources/352097/image-preview)
    </Background>
  </Step>
  <Step>
    Toggle on the script switch
  </Step>
  <Step>
    Write your script in the editor and save
    <Background>
    ![image.png](https://api.apidog.com/api/v1/projects/544525/resources/343631/image-preview)
    </Background>
  </Step>
</Steps>

## Script Reference

### Basic Example

```js
// Get mock data from Smart Mock
var responseJson = $$.mockResponse.json();

// Modify the paged data from responseJson
// Set page as the page in request parameter
responseJson.page = $$.mockRequest.getParam("page");

// Set total as 120
responseJson.total = 120;

// Write the modified json into $$.mockResponse
$$.mockResponse.setBody(responseJson);
```

**What this script does:**
1. Retrieves the initial automatically generated mock response
2. Modifies the response by:
   - Setting `page` to match the requested page parameter
   - Setting a fixed `total` value of 120
3. Updates the mock response with these changes

### $$.mockRequest Object

The `$$.mockRequest` object represents the incoming request. It's similar to Postman's [`pm.request`](https://docs.apidog.com/postman-scripts-reference-593586m0.md#pmrequest) object with additional features.

**Key Methods:**

| Method/Property | Description |
|-----------------|-------------|
| `getParam(key)` | Retrieves parameters from any location (query, body, etc.) |
| `headers` | Access HTTP headers |
| `cookies` | Access cookie values |
| `body` | Access request body |
| `formdata` | Access form-data parameters |
| `urlencoded` | Access URL-encoded parameters |

**Usage Examples:**

```javascript
// Get request parameters from any location
var userId = $$.mockRequest.getParam("userId");

// Get specific header values
var headerUserId = $$.mockRequest.headers.get("userId");

// Get cookie values
var cookieUserId = $$.mockRequest.cookies.get("userId");

// Get JSON data from request body
var requestJsonData = $$.mockRequest.body.toJSON();

// Get string data from request body
var requestStringData = $$.mockRequest.body.toString();

// Get form-data from request body
var formDataUserId = $$.mockRequest.formdata.get("userId");

// Get URL-encoded data from request body
var urlencodedUserId = $$.mockRequest.urlencoded.get("userId");
```

### $$.mockResponse Object

The `$$.mockResponse` object represents the response being sent back. It's similar to Postman's [`pm.response`](https://docs.apidog.com/postman-scripts-reference-593586m0.md#pmresponse) object with additional control methods.

**Key Methods:**

| Method | Parameters | Description |
|--------|------------|-------------|
| `setBody(body)` | any | Sets the response body |
| `setCode(code)` | number | Sets HTTP status code |
| `setDelay(duration)` | number (ms) | Adds response delay (simulates latency) |
| `json()` | - | Retrieves response as JSON |
| `headers` | - | Access/modify response headers |

**Usage Examples:**

```javascript
// Get the auto-generated response
var responseJsonData = $$.mockResponse.json();

// Set body with JSON object
$$.mockResponse.setBody({ id: "1", name: "Apple" });

// Set body with string
$$.mockResponse.setBody("Hello World!");

// Set HTTP status code
$$.mockResponse.setCode(200);

// Set response delay (3 seconds)
$$.mockResponse.setDelay(3000);

// Get HTTP status code
var statusCode = $$.mockResponse.code;

// Get HTTP header value
var myHeader = $$.mockResponse.headers.get("X-My-Header");

// Set HTTP header
$$.mockResponse.headers.set("X-My-Header", "hello");
```

## FAQ

<Accordion title="Q: How to use Apidog variables in mock scripts?" defaultOpen>

**A:** Mock scripts **cannot use Apidog variables**. 

Variables are a feature of the Apidog client, but the mock engine runs independently and cannot access client-side variables.

</Accordion>

<Accordion title="Q: How to use log statements in mock scripts?">

**A:** Mock scripts **do not provide logging functionality**. 

The console is a client-side feature, but the mock engine operates separately and cannot output logs to the client console.

</Accordion>

<Accordion title="Q: Why can't I use the pm object in mock scripts?">

**A:** The `pm` object is **not available in mock scripts**.

Mock scripts execute on the mock server, while pre/post scripts execute on the Apidog client. These are completely different execution environments with different available objects and syntax.

</Accordion>

<Accordion title="Q: Do mock scripts work with mock expectations?">

**A:** No, **mock scripts only work with Smart mock**.

When a mock expectation is matched, the mock script will not execute. Mock scripts do not apply to mock expectations or response examples.

</Accordion>

