# Apidog OpenAPI/Swagger Specificaiton Extensions

## Specify the Folder to Which an Endpoint Belongs

1. Apidog will prioritize using the `x-apidog-folder` field. If this field does not exist, it will use the first value in the `tags` field.

2. Use slashes `/` to separate Multi-level folders. Note that both backslash `\` and forward slash `/` are special characters that require escaping. To represent the character forward slash `/`, please use `\/`, and to represent the character `\`, please use `\\`.

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

Swagger annotation example:

```CSS
@Operation(extensions = {
    @Extension(properties = {
            @ExtensionProperty(name = "x-apidog-folder", value = "Pet Store/Pet Information")})
})
public Response createPet() {...}
```

## Endpoint Status

Check the status of endpoint: `x-apidog-status`

| **Status**         | **Description**  |
| ------------------ | ---------------- |
| (Designing)        | designing        |
| (Pending)          | pending          |
| (Developing)       | developing       |
| (Integrating)      | integrating      |
| (Testing)          | testing          |
| (Tested)           | tested           |
| (Released)         | released         |
| (Deprecated)       | deprecated       |
| (Exception)        | exception        |
| (Obsolete)         | obsolete         |
| (To be Deprecated) | to be deprecated |

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

Swagger annotation example:

```java
@Operation(extensions = {
    @Extension(properties = {
            @ExtensionProperty(name = "x-apidog-status", value = "released")})
})
public Response createPet() {...}
```

## Maintainer

Maintainer for the specified endpoint: `x-apidog-maintainer`. Its value is the nickname or username of the Apidog user within the team.

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

**Swagger Annotation Example**

```typerscript
@Operation(extensions = {
    @Extension(properties = {
            @ExtensionProperty(name = "apidog-maintainer", value = "david")})
})
public Response createPet() {...}
```
