# x-apifox-enum



## 用法
用于为 JSON Schema 中的枚举值（enum）添加额外的描述信息，包括枚举值的名称和描述。

## 示例

```json
{
  "type": "string",
  "enum": [
    "1",
    "2"
  ],
  "x-apifox-enum": [
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

以下为历史版本数据，已废弃:

```json
{
  "type": "string",
  "enum": [
    "1",
    "2"
  ],
  "x-apifox": {
    "enumDescriptions": {
        "1": "",
        "2": ""
    }
  }
}
```
