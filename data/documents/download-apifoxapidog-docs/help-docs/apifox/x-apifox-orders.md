# x-apifox-orders


## 用法

用于控制 object 类型中各个字段的排序，允许自定义 JSON 数据结构中字段的顺序。

## 示例

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
    "x-apifox-orders": [ //字段排序，展示的时候使用
        "id",
        "name"
    ]
}
```
