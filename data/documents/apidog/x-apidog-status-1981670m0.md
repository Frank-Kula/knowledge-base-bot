# x-apidog-status

## Usage

Used to specify the endpoint status.

| Status      | Description      |
| ----------- | ---------------- |
| designing   | Designing        |
| pending     | Pending          |
| developing  | Developing       |
| integrating | Integrating      |
| testing     | Testing          |
| tested      | Tested           |
| released    | Released         |
| deprecated  | To be deprecated |
| exception   | Exception        |
| obsolete    | Obsolete         |

## Example

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

## Swagger Annotation Example

```java
@Operation(extensions = {
    @Extension(properties = {
            @ExtensionProperty(name = "x-apidog-status", value = "released")})
})
public Response createPet() {...}
```
