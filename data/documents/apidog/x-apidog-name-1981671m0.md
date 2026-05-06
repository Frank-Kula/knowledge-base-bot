# x-apidog-name


## Usage

Used to specify the response name (summary).

## Example

```json
"paths": {
    "/pets": {
        "post": {
            ...
            "responses": {
                "400":{
                   "x-apidog-name": "Bad request",     
                   "description": "Bad Request. The request could not be understood by the server due to malformed syntax. A possible reason might be that the request contains Unicode characters that cannot be processed."
                   ...
               }
            }
        }
    }
}
```
