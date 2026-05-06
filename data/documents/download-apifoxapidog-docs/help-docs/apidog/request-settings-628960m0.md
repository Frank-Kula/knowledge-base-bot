# Request Settings

Apidog allows you to configure a variety of settings for your API requests. These settings enable you to customize Apidog's behavior when sending a request, ensuring compatibility with different API requirements and testing scenarios.


## Configuring Custom Request Settings

To configure custom settings, select the **Settings** tab of your request, then toggle the setting on or off. Each setting provides a description of its effect when sending the request.

For example, you can turn on SSL certificate validation or turn off URL encoding for a request.

:::tip[]
Most requests work well with Apidog's default settings. Only modify these settings when you need specific behavior for testing or compatibility purposes.
:::

## Encoding Your Request URLs

Apidog parses and encodes the URL of your request to maximize the chances of a successful API call. Apidog encodes the characters in the URL and maps them to a representation that your API is most likely to accept.

### URL Encoding Methods

The following table compares the three available URL encoding methods:

| **Method** | **Standard** | **Character Handling** | **Use Case** |
| --- | --- | --- | --- |
| **WHATWG** | Modern web browsers | More lenient, preserves more characters (e.g., tildes `~`), converts spaces to `+` | **Default**. Best for modern web APIs |
| **RFC 3986** | IETF standard | Stricter encoding, encodes more characters including tildes, converts spaces to `%20` | Legacy systems requiring strict compliance |
| **No encoding** | None | Sends URL as-is without any encoding | Pre-encoded URLs or testing unencoded behavior |

### WHATWG

This is the encoding method used by modern web browsers. It's more lenient and preserves more characters in their original form. For example, it doesn't encode tildes (`~`) or spaces (which are converted to `+` signs instead of `%20`).

### RFC 3986

This is a stricter standard defined by the Internet Engineering Task Force (IETF). It encodes more characters, including those that WHATWG leaves unencoded. For instance, it will encode tildes and convert spaces to `%20` instead of `+`.

### No Encoding

This option sends the URL as-is, without any encoding. This can be useful if you've already encoded the URL manually or if you're testing how a server handles unencoded URLs. However, it may cause issues with special characters or spaces in the URL.

:::warning[]
Using **No encoding** may result in request failures if your URL contains special characters or spaces that the server cannot interpret correctly.
:::

