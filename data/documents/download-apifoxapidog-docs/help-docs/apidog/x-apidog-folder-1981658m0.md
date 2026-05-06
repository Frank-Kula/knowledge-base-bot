# x-apidog-folder

## Usage

Used to specify the folder to which an endpoint belongs.

- Apidog prioritizes the use of the `x-apidog-folder` field. If this field does not exist, the first value in the `tags` field will be used.

- Multi-level folders are separated by a forward slash `/`. Where `\` and `/` are special characters and need to be escaped: `\/` represents the character `/`, and `\\` represents the character `\`.

## Example
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

## Swagger Annotation Example
```java
@Operation(extensions = {
    @Extension(properties = {
            @ExtensionProperty(name = "x-apidog-folder", value = "Pet Store/Pet Information")})
})
public Response createPet() {...}
```
