# Other Examples

## Sending API Requests (`pm.sendRequest`)

You can send asynchronous HTTP requests within your script.

```javascript
pm.sendRequest("https://api.apidog.com/health", function (err, response) {
    if (err) {
        console.log(err);
    } else {
        console.log("Health Check Status:", response.json().status);
    }
});
```

## Decoding Base64 Data

If your API returns Base64 encoded data, you can decode it using the built-in `crypto-js` library.

```javascript
var cryptoJs = require("crypto-js");

// Assume response body contains base64 string
var base64Content = pm.response.text();

// Decode
var parsed = cryptoJs.enc.Base64.parse(base64Content);
var decodedString = cryptoJs.enc.Utf8.stringify(parsed);

console.log(decodedString);
```

## Converting XML to JSON

If an API returns XML, but you prefer to work with JSON:

```javascript
var xml2js = require("xml2js");

var xml = "<root><name>Apidog</name></root>";

xml2js.parseString(xml, function (err, result) {
    console.log(result.root.name); // Output: Apidog
});
```

