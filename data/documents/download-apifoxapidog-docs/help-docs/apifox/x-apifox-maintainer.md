# x-apifox-maintainer


## 用法

用于指定接口的责任人，其值为 Apifox 用户在团队内的昵称，或者用户名。

## 示例

```json
"paths": {
    "/pets": {
        "post": {
            ...   
            "x-apifox-maintainer": "david" // "团队内昵称"或“用户账户名”，优先使用“团队内昵称”，未配置“团队内昵称”时才使用“用户账户名”
        }
    }
}
```

## Swagger 注解示例

```java
@Operation(extensions = {
    @Extension(properties = {
            @ExtensionProperty(name = "x-apifox-maintainer", value = "david")})
})
public Response createPet() {...}
```
