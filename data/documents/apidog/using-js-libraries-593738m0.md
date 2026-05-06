# Using JS Libraries

Apidog's scripting engine supports both built-in libraries (available immediately) and external libraries (dynamically loaded via npm).

## Built-in Libraries

You can `require` these libraries directly in your scripts without any setup.

### Encode and Decode

| Library | Version | Description |
|---------|---------|-------------|
| [atob](https://www.npmjs.com/package/atob) | v2.1.2 | Base64 decode. |
| [btoa](https://www.npmjs.com/package/btoa) | v1.2.1 | Base64 encode. |
| [crypto-js](https://www.npmjs.com/package/crypto-js) | v3.1.9-1 | An Encoding / decoding library, including the common encoding and decoding methods (Base64, MD5, SHA, HMAC, AES, etc.). You can only require the entire module, not a submodule of the class library. View the documentation here for more details. |
| [jsrsasign](https://www.npmjs.com/package/jsrsasign) | 10.3.0 | RSA encryption / decryption. Only Apidog version 1.4.5 or later is supported. |

### Assertion

| Library | Version | Description |
|---------|---------|-------------|
| [chai](http://chaijs.com/) | v4.2.0 | BDD / TDD assertion library. |

### Tools

| Library | Version | Description |
|---------|---------|-------------|
| [postman-collection](http://www.postmanlabs.com/postman-collection/) | v3.4.0 | Postman Collection library. |
| [cheerio](https://cheerio.js.org/) | v0.22.0 | A subset of jQuery. |
| [lodash](https://lodash.com/) | v4.17.11 | JS Utilities Library. |
| [moment](http://momentjs.com/docs/) | v2.22.2 | Date libraries (not including locales). |
| [uuid](https://www.npmjs.com/package/uuid) | - | Generate UUID. |
| [xml2js](https://www.npmjs.com/package/xml2js) | v0.4.19 | Convert XML into JSON. |
| [csv-parse/lib/sync](https://csv.js.org/parse/api/sync/) | v1.2.4 | Parse CSV. |

### JSONSchema Validators

| Library | Version | Description |
|---------|---------|-------------|
| [tv4](https://github.com/geraintluff/tv4) | v1.3.0 | JSONSchema validator. |
| [ajv](https://www.npmjs.com/package/ajv) | v6.6.2 | JSONSchema validator. |

### Built-in NodeJS Modules

| Library | Version | Description |
|---------|---------|-------------|
| [path](https://nodejs.org/api/path.html) | - | Path module for handling file paths. |
| [assert](https://nodejs.org/api/assert.html) | - | Assertion testing module. |
| [buffer](https://nodejs.org/api/buffer.html) | - | Buffer module for binary data. |
| [util](https://nodejs.org/api/util.html) | - | Utility functions module. |
| [url](https://nodejs.org/api/url.html) | - | URL parsing and resolution module. |
| [punycode](https://nodejs.org/api/punycode.html) | - | Punycode encoding module. |
| [querystring](https://nodejs.org/api/querystring.html) | - | Query string parsing module. |
| [string-decoder](https://nodejs.org/api/string_decoder.html) | - | String decoder module. |
| [stream](https://nodejs.org/api/stream.html) | - | Stream module for streaming data. |
| [timers](https://nodejs.org/api/timers.html) | - | Timer functions module. |
| [events](https://nodejs.org/api/events.html) | - | Event emitter module. |


## Usage Examples

### SHA256 Encryption

```js
// SHA256 Encryption with Base64 Output
// Define the message to be encrypted
const message = "Hello, World!";

// Encrypt using the SHA256 algorithm
const hash = CryptoJS.SHA256(message);

// Output the encrypted result as Base64
const base64Encoded = CryptoJS.enc.Base64.stringify(hash);

// Print the result
console.log("SHA256: " + base64Encoded);
```

### HMAC-SHA256 Encryption

```js
// HMAC-SHA256 Encryption with Base64 Output
// Define the message and the secret key
const message = "Hello, World!";
const secretKey = "MySecretKey";

// Encrypt using the HMAC-SHA256 algorithm
const hash = CryptoJS.HmacSHA256(message, secretKey);

// Output the encrypted result as Base64
const base64Encoded = CryptoJS.enc.Base64.stringify(hash);

// Print the result
console.log("HMAC-SHA256: " + base64Encoded);
```

### Base64 Encoding

```js
// Define the message to be encoded
const message = "Hello,ApiDog!";

// Encode the message using CryptoJS for Base64
const wordArray = CryptoJS.enc.Utf8.parse(message);
const base64Encoded = CryptoJS.enc.Base64.stringify(wordArray);

// Print the encoded result
console.log("Base64: " + base64Encoded);
```

### Base64 Decoding

**String Decoding:**

```js
// Base64 encoded string (typically extracted from response data)
let encodedData = {
    "data": "SGVsbG8sQXBpRG9nIQ=="
};

// Decode the Base64 encoded data
let decodedData = CryptoJS.enc.Base64.parse(encodedData.data).toString(CryptoJS.enc.Utf8);

// Print the decoded result
console.log(decodedData); // "Hello,ApiDog!"
```

**JSON Decoding:**

You can set the decoded JSON data as the response body using the `pm.response.setBody()` method.

```js
// Import CryptoJS library
const CryptoJS = require("crypto-js");

// Get the Base64 encoded string from the response
let encodedData = pm.response.text();

// Decode the Base64 encoded data
let decodedData = CryptoJS.enc.Base64.parse(encodedData).toString(CryptoJS.enc.Utf8);

// Parse the decoded JSON string
let jsonData = JSON.parse(decodedData);

// Set the parsed JSON data as the response body
pm.response.setBody(jsonData);

// Print the result
console.log(jsonData);
```

### AES Encryption

```js
// Import CryptoJS library
const CryptoJS = require("crypto-js");

// Assume this is the value of the `password` field we want to encrypt, obtained from environment variables
const password = pm.environment.get("password");

// Use secure key and IV (for demonstration purposes, ensure to protect these sensitive details in real applications)
const key = CryptoJS.enc.Utf8.parse('mySecretKey12345'); // Ensure it's 16/24/32 bytes
const iv = CryptoJS.enc.Utf8.parse('myIVmyIVmyIVmyIV'); // Ensure it's 16 bytes

// AES encryption
const encrypted = CryptoJS.AES.encrypt(password, key, {
    iv: iv,
    mode: CryptoJS.mode.CBC,
    padding: CryptoJS.pad.Pkcs7
}).toString();

// Set the encrypted password as a new variable to be used in the request body
pm.environment.set("encryptedPassword", encrypted);
```

### AES Decryption

Assuming an AES encrypted ciphertext with ECB mode and Pkcs7 padding, the AES decryption script example is as follows:

```js
// Import CryptoJS library
const CryptoJS = require('crypto-js');

// Base64 encoded AES encrypted ciphertext (typically extracted from response data)
const ciphertext = "qvK7eVXu94S1dy4sLC+jrQ==";

// Decryption key, ensure it's 16/24/32 bytes (typically read from environment variables)
const key = CryptoJS.enc.Utf8.parse('1234567891234567');

// AES decryption
const decryptedBytes = CryptoJS.AES.decrypt(ciphertext, key, {
    mode: CryptoJS.mode.ECB, // Decryption mode
    padding: CryptoJS.pad.Pkcs7 // Padding scheme
});

// Convert the decrypted byte array to a UTF-8 string
const originalText = decryptedBytes.toString(CryptoJS.enc.Utf8);

// Print the decrypted text
console.log(originalText); // "Hello,Apidog!"
```

### RSA Encryption

```js
// Import jsrsasign library
const jsrsasign = require('jsrsasign');

// Define the public key (typically read from environment variables)
const publicKey = `
-----BEGIN PUBLIC KEY-----
...Public Key...
-----END PUBLIC KEY-----
`;

// Encrypt using the public key
const plaintext = "Hello,Apidog!";
const pubKeyObj = jsrsasign.KEYUTIL.getKey(publicKey);

const encryptedHex = jsrsasign.KJUR.crypto.Cipher.encrypt(plaintext, pubKeyObj);
console.log("Encrypted Ciphertext:", encryptedHex);
```

### RSA Decryption

```js
// Import jsrsasign library
const jsrsasign = require('jsrsasign');

// Define the private key (typically read from environment variables)
const privateKeyPEM = `
-----BEGIN PRIVATE KEY-----
...Private Key...
-----END PRIVATE KEY-----
`;

// Define the ciphertext (typically extracted from response data)
const ciphertext = '...';

// Decrypt
const prvKeyObj = jsrsasign.KEYUTIL.getKey(privateKeyPEM);
const decrypted = jsrsasign.KJUR.crypto.Cipher.decrypt(ciphertext, prvKeyObj);
console.log(decrypted);
```

Below is a complete example of simple RSA encryption and decryption (Note: The `jsrsasign` version is 10.3.0; syntax may not be compatible with other versions). This example can be run in a Node.js environment and adapted for encryption or decryption operations in Apidog:

```js
const rsa = require('jsrsasign');

// Generate RSA key pair
const keypair = rsa.KEYUTIL.generateKeypair("RSA", 2048);
const publicKey = rsa.KEYUTIL.getPEM(keypair.pubKeyObj);
const privateKey = rsa.KEYUTIL.getPEM(keypair.prvKeyObj, "PKCS8PRV");

console.log("Public Key:", publicKey);
console.log("Private Key:", privateKey);

// Encrypt with public key
const plaintext = "Hello,Apidog!";
const pubKeyObj = rsa.KEYUTIL.getKey(publicKey);

const encryptedHex = rsa.KJUR.crypto.Cipher.encrypt(plaintext, pubKeyObj);
console.log("Encrypted Ciphertext:", encryptedHex);

// Decrypt with private key
const prvKeyObj = rsa.KEYUTIL.getKey(privateKey);

const decrypted = rsa.KJUR.crypto.Cipher.decrypt(encryptedHex, prvKeyObj);
console.log("Decrypted Plaintext:", decrypted);
```


<Background>

![image.png](https://api.apidog.com/api/v1/projects/544525/resources/357476/image-preview)
</Background>



:::tip TIP

When using a built-in library, you can only require the entire module; submodules cannot be required individually.

```json
// A correct example.
var cryptoJs = require("crypto-js");
console.log(cryptoJs.SHA256("Message"));

// A wrong example.
var SHA256 = require("crypto-js/sha256");
console.log(SHA256("Message"));
```

:::

## External Libraries (npm)

You can load any pure JavaScript library from npm using `$$.liveRequire`.

:::note
This requires an active internet connection to download the package.
:::

**Single Library:**
```javascript
$$.liveRequire("camelcase", (camelCase) => {
    console.log(camelCase("foo-bar")); // "fooBar"
});
```

**Multiple Libraries:**
```javascript
$$.liveRequire(["camelcase", "md5"], (camelCase, md5) => {
    console.log(camelCase("hello-world"));
    console.log(md5("message"));
});
```

