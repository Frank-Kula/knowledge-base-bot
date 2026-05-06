# x-apifox-status


## 用法

用于指定接口状态。

| 状态        | 说明   |
| ----------- | ------ |
| designing   | 设计中 |
| pending     | 待确定 |
| developing  | 开发中 |
| integrating | 联调中 |
| testing     | 测试中 |
| tested      | 已测完 |
| released    | 已发布 |
| deprecated  | 将废弃 |
| exception   | 有异常 |
| obsolete    | 已废弃 |

## 示例

```json
"paths": {
    "/pets": {
        "post": {
            ...
            "operationId": "addPet",     
            "x-apifox-status": "released"
        }
    }
}
```

## Swagger 注解示例

```java
@Operation(extensions = {
    @Extension(properties = {
            @ExtensionProperty(name = "x-apifox-status", value = "released")})
})
public Response createPet() {...}
```

