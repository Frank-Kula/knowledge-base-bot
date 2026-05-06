# x-apifox-mock



## 用法

用于指定在生成 Mock 数据时所使用的规则。它可以通过指定生成的 Mock 数据格式，来确保 API 的 Mock 数据符合特定需求。

## 示例

```json
{
    "properties": {
        "id": { 
            "type": "string"
        },
        "name": {
            "type": "string",
            "x-apifox-mock": "{{$person.name}}"
        }
    }
}
```
