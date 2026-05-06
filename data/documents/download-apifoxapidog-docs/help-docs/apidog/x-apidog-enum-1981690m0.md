# x-apidog-enum

## Usage
Used to add additional descriptive information to enum values in a JSON Schema, including the names and descriptions of the enum values.

## Example

```json
{
  "type": "string",
  "enum": [
    "1",
    "2"
  ],
  "x-apidog-enum": [
    {
      "value": "1", 
      "name": "One",
      "description": "First element" 
    },
    { 
      "value": "2", 
      "name": "One",
      "description": "Second element"
    }
  ]
}
```

The following is historical version data and has been deprecated:

```json
{
  "type": "string",
  "enum": [
    "1",
    "2"
  ],
  "x-apidog": {
    "enumDescriptions": {
        "1": "",
        "2": ""
    }
  }
}
```
