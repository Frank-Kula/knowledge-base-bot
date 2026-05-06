# x-apidog-maintainer


## Usage

Used to specify the maintainer of the endpoint. The value is the Apidog user's nickname within the team or their username.

## Example

```json
"paths": {
    "/pets": {
        "post": {
            ...   
            "x-apidog-maintainer": "david" // "Nickname within the team" or "username". "Nickname within the team" takes priority; "username" is used only if "nickname within the team" is not configured.
        }
    }
}
```

## Swagger Annotation Example

```java
@Operation(extensions = {
    @Extension(properties = {
            @ExtensionProperty(name = "x-apidog-maintainer", value = "david")})
})
public Response createPet() {...}
```
