# Handling API Signatures

API signatures are security mechanisms that verify request authenticity and integrity. This guide demonstrates how to automate signature generation in Apidog, eliminating the need to manually retrieve signatures for each request.

## Signature Automation Strategy

Instead of manually accessing a signature endpoint before each request, use Apidog's scripting capabilities to:

1. Create a public script implementing signature logic
2. Automatically generate signatures using request parameters
3. Attach signatures to requests via scripts or environment variables
4. Reference the public script in API preprocessors

## Implementation Approach

### Method 1: Direct Script Modification

Add signature parameters and modify request information directly via scripts without using environment variables.

**Advantages:**
- No environment variable management
- Immediate parameter updates
- Simpler configuration

### Method 2: Environment Variables

Generate the signature and write it to an environment variable, then reference the variable in API parameters.

**Advantages:**
- Reusable across multiple requests
- Easier debugging and monitoring
- Centralized signature management

### Method 3: External Programs

For signatures implemented in other languages, use the `dog.execute` method to call external programs.

## Example: MD5-Based Signature

### Signature Generation Rules

**Step 1: Build the parameter string**

1. Collect all non-empty parameters into set M
2. Sort parameters by ASCII code in ascending order (dictionary order)
3. Concatenate parameters in URL key-value format: `key1=value1&key2=value2...`
4. Result: `stringA`

:::warning[]
**Important rules:**
- Sort parameter names by ASCII code in ascending order
- Empty parameter values are excluded from the signature
- Parameter names are case-sensitive
- The `sign` parameter itself is excluded from the signature
:::

**Step 2: Generate the signature**

1. Concatenate the key at the end of `stringA` to get `stringSignTemp`
2. Apply MD5 algorithm to `stringSignTemp`
3. Convert the result to uppercase to get `signValue`

### Public Script Implementation

```javascript
// Get the key from the environment variable APPKEY
let key = pm.environment.get("APPKEY");

// Store all parameters needed for signature
let param = {};

// Add query parameters
let queryParams = pm.request.url.query;
queryParams.each(item => {
    if (item.value !== '') { // Only non-empty values will be included
        param[item.key] = item.value;
    }
});

// Add body parameters
if (pm.request.body) {
    let formData;
    switch (pm.request.body.mode) {
        case 'formdata':
            formData = pm.request.body.formdata;
            break;
        case 'urlencoded':
            formData = pm.request.body.urlencoded;
            break;
        case 'raw':
            // If there is no JSON-formatted request body, or if the JSON-formatted body is not included in the signature, remove this code block
            let contentType = pm.request.headers.get('content-type');
            if (
                contentType
                && pm.request.body.raw
                && contentType.toLowerCase().indexOf('application/json') !== -1
            ) {
                try {
                    let jsonData = JSON.parse(pm.request.body.raw);
                    /*
                     * If the API parameter extracted from the script includes variables, the variables will not automatically be replaced by their values. To get the actual values, use `pm.variables.replaceIn`:
                     * let body = pm.variables.replaceIn(pm.request.body.raw);
                     * let jsonData = JSON.parse(body);
                     */
                    for (let key in jsonData) {
                        let value = `${jsonData[key]}`; // Note: if the actual value is not string type, modify this code accordingly
                        if (value !== '') { // Only non-empty parameter values will be included
                            param[key] = value;
                        }
                    }
                } catch (e) {
                    console.log('request body is not in JSON format')
                }
            }
            break;
        default:
            break;
    }
    if (formData) {
        formData.each(item => {
            if (item.value !== '') { // Only non-empty parameter values will be included
                param[item.key] = item.value;
            }
        });
    }
}

// Get the keys
let keys = [];
for (let key in param) {
    // Remove the sign parameter
    if (key !== 'sign') {
        keys.push(key);
    }
}

// Sort parameter names by ASCII code in ascending order (dictionary order)
keys.sort();

// Convert to key-value pairs
let paramPair = [];
for (let i = 0, len = keys.length; i < len; i++) {
    let k = keys[i];
    paramPair.push(k + '=' + encodeURIComponent(param[k])) // URL encode
}

// Add key
paramPair.push("key=" + key);

// Concatenate
let stringSignTemp = paramPair.join('&');
// console.log(stringSignTemp);

let sign = CryptoJS.MD5(stringSignTemp).toString().toUpperCase();
// console.log(sign);

// Method 1: Add signature parameter and modify request information directly via scripts (no need to use environment variables)
// View more in documentation: https://apidog.com/help/app/scripts/examples/request-handle/
queryParams.upsert({
    key: 'sign',
    value: sign,
});

// Method 2: Write it into an environment variable. You will need to reference the environment variable in API parameters
// pm.environment.set("SIGN", sign);
```

## Example: Translation API Signature

### Signature Generation Rules

**Step 1: Concatenate the string**

Concatenate the following values in order:
- `appid`: Application ID
- `q`: Text to be translated (UTF-8 encoding)
- `salt`: Random number
- `key`: Platform-assigned key (available in management console)

Result: `appid + q + salt + key`

**Step 2: Generate the signature**

Apply MD5 algorithm to the concatenated string to get a 32-bit lowercase signature.

:::warning[]
**Important notes:**
- Text to be translated (`q`) must be in UTF-8 encoding
- When concatenating `appid+q+salt+key`, do NOT apply URL encoding to `q`
- After the signature is generated, apply URL encoding to `q` before sending the HTTP request
:::

### Example Request

```javascript
// Example: Translate "apple" from English to Japanese
// Request parameters:
q=apple
from=en
to=ja
appid=2015063000000001
salt=1435660288
// Platform assigned key: 12345678

// Generate sign:
// 1. Concatenate string 1
// Concatenate appid=2015063000000001+q=apple+salt=1435660288+key=12345678
// Result: 2015063000000001apple143566028812345678

// 2. Generate the signature sign
// Use MD5 algorithm on string 1 to get the 32-bit lowercase sign
// Before using MD5, string 1 needs to be in UTF-8 encoding
sign=md5(2015063000000001apple143566028812345678)
sign=f89f9594663708c1605f3d736d01d2d4

// Complete request:
http://xxx/api/trans/vip/translate?q=apple&from=en&to=zh&appid=2015063000000001&salt=1435660288&sign=f89f9594663708c1605f3d736d01d2d4
```

### Public Script Implementation

```javascript
// Get query params
var queryParams = pm.request.url.query;

// Get q from query params
var q = queryParams.get("q");

// Get the value of environment variables APPID and SECRET_KEY
var appid = pm.environment.get("APPID");
var secretKey = pm.environment.get("SECRET_KEY");

// Generate a random number between 32768 and 65536
var salt = parseInt(Math.random() * 32769 + 32768, 10);

// Convert the random number into a string
salt = salt.toString();
console.log(salt);

// Concatenate a string using appid+q+salt+secretKey
var str = appid + q + salt + secretKey;
console.log(str);

// Use MD5 algorithm on the string to generate sign
var sign = CryptoJS.MD5(str).toString();

// Method 1: Add salt and sign in the query parameters for the API (no need to use environment variables)
// View documentation here: https://apidog.com/help/app/scripts/examples/request-handle/
queryParams.upsert({
  key: "salt",
  value: salt,
});
queryParams.upsert({
  key: "sign",
  value: sign,
});

// Method 2: Write salt and sign in environment variables. You will need to reference the environment variables in API parameters
// pm.environment.set("SALT", salt);
// pm.environment.set("SIGN", sign);
```

## Best Practices

| Practice | Description |
|----------|-------------|
| **Use Environment Variables** | Store sensitive keys in environment variables, not in scripts |
| **Validate Parameters** | Check for required parameters before generating signatures |
| **Log for Debugging** | Use `console.log()` to debug signature generation issues |
| **Handle Edge Cases** | Account for empty values, special characters, and encoding |
| **Centralize Logic** | Use public scripts to avoid duplicating signature logic |
| **Test Thoroughly** | Verify signature generation with known test cases |

