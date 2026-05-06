# Modifying Requests

You can use **Pre-request Scripts** to dynamically modify request parameters (Headers, Query Params, Body) before the request is sent.

:::warning[]
Modifying headers and query parameters is only possible in **Pre-request Scripts**. You cannot modify the request in Post-request scripts.
:::

## Header Parameters

### Add or Update Header
```javascript
// Add a header
pm.request.headers.add({
    key: "X-Client-Version",
    value: "1.0.0"
});

// Upsert (Update if exists, else Add)
pm.request.headers.upsert({
    key: "Authorization",
    value: "Bearer " + pm.variables.get("token")
});
```

### Remove Header
```javascript
pm.request.headers.remove("X-Old-Header");
```

## Query Parameters

### Add or Update Query Param
```javascript
var query = pm.request.url.query;

// Add parameter
query.add({
    key: "page",
    value: "1"
});

// Upsert parameter
query.upsert({
    key: "sort",
    value: "desc"
});
```

## Body Parameters

You can modify the request body (JSON) before sending.

```javascript
// 1. Get current body
var bodyConfig = pm.request.body.toJSON();
var rawBody = bodyConfig.raw;

// 2. Parse JSON
try {
    var bodyJson = JSON.parse(rawBody);

    // 3. Modify data
    bodyJson.timestamp = new Date().getTime();
    bodyJson.nonce = Math.random().toString(36).substring(7);

    // 4. Update request body
    pm.request.body.update(JSON.stringify(bodyJson, null, 2));
    
    console.log("Updated Body:", pm.request.body.raw);
} catch (e) {
    console.error("Error parsing body:", e);
}
```

:::tip
Always ensure your script is placed **after** the "Variable Substitution" step if you need to read variables that were just substituted, or **before** if you are setting variables for substitution. For modifying the body, typically you do this before the request is sent.
:::

