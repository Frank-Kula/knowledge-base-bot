# Apidog OpenAPI Specificaiton Extensions

Apidog supports custom OpenAPI/Swagger specification extensions that enhance API design and management capabilities. These extensions allow you to specify additional metadata for your API endpoints, such as folder organization, endpoint status, and maintainer information.

This reference guide documents the custom `x-apidog-*` extensions that can be used in your OpenAPI/Swagger specifications to integrate seamlessly with Apidog's features.

## Specify the Folder to Which an Endpoint Belongs

Apidog will prioritize using the `x-apidog-folder` field to organize endpoints. If this field does not exist, it will use the first value in the `tags` field.

Use slashes `/` to separate multi-level folders. Note that both backslash `\` and forward slash `/` are special characters that require escaping. To represent the character forward slash `/`, please use `\/`, and to represent the character `\`, please use `\\`.

**Example:**

```json
"paths": {
  "/pets": {
     "post": {
         ...
         "operationId": "addPet",     
         "x-apidog-folder": "Pet Store/Pet Information"
     }
  }
}
```

**Swagger Annotation Example:**

```css
@Operation(extensions = {
    @Extension(properties = {
            @ExtensionProperty(name = "x-apidog-folder", value = "Pet Store/Pet Information")})
})
public Response createPet() {...}
```

:::tip[Folder Organization]
Use descriptive folder names to organize your endpoints logically. This improves navigation and helps team members find endpoints quickly.
:::

## Endpoint Status

Check the status of endpoint using the `x-apidog-status` field. This allows you to track the development lifecycle of each API endpoint.

### Available Status Values

| Status | Description |
| ------------------ | ---------------- |
| designing | (Designing) |
| pending | (Pending) |
| developing | (Developing) |
| integrating | (Integrating) |
| testing | (Testing) |
| tested | (Tested) |
| released | (Released) |
| deprecated | (Deprecated) |
| exception | (Exception) |
| obsolete | (Obsolete) |
| to be deprecated | (To be Deprecated) |

**Example:**

```json
"paths": {
    "/pets": {
        "post": {
            ...
            "operationId": "addPet",     
            "x-apidog-status": "released"
        }
    }
}
```

**Swagger Annotation Example:**

```java
@Operation(extensions = {
    @Extension(properties = {
            @ExtensionProperty(name = "x-apidog-status", value = "released")})
})
public Response createPet() {...}
```

:::info[Status Tracking]
Endpoint status helps teams coordinate development efforts and understand which APIs are ready for production use.
:::

## Maintainer

Specify the maintainer for an endpoint using the `x-apidog-maintainer` field. Its value is the nickname or username of the Apidog user within the team.

**Example:**

```json
"paths": {
    "/pets": {
        "post": {
            ...   
            "x-apidog-maintainer": "david"
        }
    }
}
```

**Swagger Annotation Example:**

```typescript
@Operation(extensions = {
    @Extension(properties = {
            @ExtensionProperty(name = "x-apidog-maintainer", value = "david")})
})
public Response createPet() {...}
```

:::warning[Important]
The maintainer value must match an existing team member's username or nickname in Apidog for proper assignment.
:::

