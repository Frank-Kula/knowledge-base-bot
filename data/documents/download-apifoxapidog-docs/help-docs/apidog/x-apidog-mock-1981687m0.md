# x-apidog-mock


## Usage

Used to specify the rules for generating mock data. It ensures that the API's mock data meets specific requirements by specifying the format of the generated mock data.

## Example

```json
{
    "properties": {
        "id": { 
            "type": "string"
        },
        "name": {
            "type": "string",
            "x-apidog-mock": "{{$person.name}}"
        }
    }
}
```
