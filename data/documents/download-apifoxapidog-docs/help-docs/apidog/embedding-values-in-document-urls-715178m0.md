# Embedding Values in Document URLs

Enhance collaboration by embedding specific parameter and variable values directly within shared documentation URLs. By default, shared documents contain only API specifications. This feature allows you to share pre-filled values, making it easier for users to test endpoints with specific configurations.

## Parameter Behavior

Parameter values passed via the URL behave differently based on their type:

1. **Environment Variables**: Values set through the URL are applied globally across all endpoints within the document. They persist when navigating between endpoints or opening new tabs, remaining active until explicitly overridden or manually changed

2. **Request Parameters** (Query, Path, Body, Header, Cookie): These values are scoped to the specific endpoint accessed via the URL and don't persist when navigating to other endpoints

## Passing Parameter Values

Two methods are available for embedding parameter values: **Simple Mode** and **Complex Mode**. Simple Mode is more concise and doesn't require URL encoding, but cannot handle bracket characters. Complex Mode supports all characters but requires URL encoding of the parameter data.

### Simple Mode

Simple Mode uses the format `parameterType[parameterName]=value`.

**Example:**

- `https://apidog.com/apidoc/docs-site/538323/api-7312738-run?environment[access_token]=example_value&query[locale]=en-US`

| Parameter Type        | Parameter Value Format | Description                                                 | Behavior                 |
| :-------------------- | :--------------------- | :----------------------------------------------------------- | :----------------------- |
| Query Parameters      | `query[xxx]=yyy`       |                                                              | Current endpoint only    |
| Path Parameters       | `path[xxx]=yyy`        |                                                              | Current endpoint only    |
| Body Parameters       | `body[xxx]=yyy`        | For `form-data` or `x-www-form-urlencoded` body types       | Current endpoint only    |
| Body Parameters       | `body=yyy`             | For other body types (e.g., raw JSON, XML)                   | Current endpoint only    |
| Header Parameters     | `header[xxx]=yyy`      |                                                              | Current endpoint only    |
| Cookie Parameters     | `cookie[xxx]=yyy`      |                                                              | Current endpoint only    |
| Environment Variables | `environment[xxx]=yyy` | Sets the value in the default environment.                  | Persists across endpoints |

### Complex Mode

Complex Mode passes a URL-encoded JSON object as the value of the `params` parameter. This JSON object must be encoded using `encodeURIComponent`. In JavaScript, this can be achieved with: `encodeURIComponent(JSON.stringify({"query":["id",1]}))`.

**Example JSON (before encoding):**

```json
{
    "query": [
        ["id", "value1"],
        ["id", "value2"],
        ["key2", "value3"]
    ],
    "path": [
        ["key1", "value1"],
        ["key2", "value2"]
    ],
    "body": [
        ["aaa", "value1"],
        ["key2", "value2"]
    ],
    "header": [
        ["testHeader", "value1"],
        ["key2", "value2"]
    ],
    "cookie": [
        ["testCookie", "value1"],
        ["key2", "value2"]
    ],
    "environment": [
        ["access_token", "example_value"],
        ["projectId", "1"]
    ]
}
```

**Example URL (after encoding):**

```
https://apidog.com/apidoc/docs-site/538323/api-7312738-run?params=%7B%22query%22%3A%5B%5B%22id%22%2C%22value1%22%5D%2C%5B%22id%22%2C%22value2%22%5D%2C%5B%22key2%22%2C%22value3%22%5D%5D%2C%22path%22%3A%5B%5B%22key1%22%2C%22value1%22%5D%2C%5B%22key2%22%2C%22value2%22%5D%5D%2C%22body%22%3A%5B%5B%22aaa%22%2C%22value1%22%5D%2C%5B%22key2%22%2C%22value2%22%5D%5D%2C%22header%22%3A%5B%5B%22testHeader%22%2C%22value1%22%5D%2C%5B%22key2%22%2C%22value2%22%5D%5D%2C%22cookie%22%3A%5B%5B%22testCookie%22%2C%22value1%22%5D%2C%5B%22key2%22%2C%22value2%22%5D%5D%2C%22environment%22%3A%5B%5B%22access_token%22%2C%22example_value%22%5D%2C%5B%22projectId%22%2C%221%22%5D%5D%7D
```
| Parameter Type       | Parameter Value | Description                                                                                            | Behavior                 |
|:---------------------|:----------------|:-------------------------------------------------------------------------------------------------------|:-------------------------|
| Query Parameters     | `query`         | An array of key-value pairs.                                                                         | Current endpoint only    |
| Path Parameters      | `path`          | An array of key-value pairs.                                                                         | Current endpoint only    |
| Body Parameters      | `body`          | An array of key-value pairs for `form-data` or `x-www-form-urlencoded`; a string for other body types. | Current endpoint only    |
| Header Parameters    | `header`        | An array of key-value pairs.                                                                         | Current endpoint only    |
| Cookie Parameters    | `cookie`        | An array of key-value pairs.                                                                         | Current endpoint only    |
| Environment Variables| `environment`   | An array of key-value pairs. Sets values in the default environment.                                  | Persists across endpoints |

## Passing Environment Variables

To automatically set environment variables for a user, include them in the URL. These variables will persist across all endpoints in the document.

**Examples:**

-   `https://openapi.apidog.io/api-7312738-run?environment[access_token]=example_value`

:::tip[Best Practice]
Environment variables persist across endpoints, while other parameter types (query, path, body, header, cookie) are scoped to the specific endpoint in the URL. This method is best for sharing reusable values across multiple endpoints.
:::

