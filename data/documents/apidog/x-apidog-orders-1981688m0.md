# x-apidog-orders

## Usage

Used to control the ordering of various fields within an `object` type, allowing for customization of the field sequence in JSON data structures.

## Example

```json
{
    "properties": {
        "id": { 
            "type": "string"
        },
        "name": {
            "type": "string"
        },
    },
    "x-apidog-orders": [ // Field ordering, used for display
        "id",
        "name"
    ]
}
```
