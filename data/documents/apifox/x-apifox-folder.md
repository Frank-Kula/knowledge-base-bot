# x-apifox-folder


## 用法

用于指定某个接口所属目录。

- Apifox 会优先使用 `x-apifox-folder` 字段，如不存在该字段，则会使用 `tags` 字段里的第一个值。

- 多级目录使用斜杠`/`分隔。其中`\`和`/`为特殊字符，需要转义，`\/`表示字符`/`，`\\`表示字符`\`。

## 示例
```json
"paths": {
    "/pets": {
        "post": {
            ...
            "operationId": "addPet",   
            "x-apifox-folder": "宠物店/宠物信息"
        }
    }
}
```

## Swagger 注解示例
```java
@Operation(extensions = {
    @Extension(properties = {
            @ExtensionProperty(name = "x-apifox-folder", value = "宠物店/宠物信息")})
})
public Response createPet() {...}
```

