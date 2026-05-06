# x-apifox-name


## 用法

用于指定响应名称（摘要）。

## 示例

```json
"paths": {
    "/pets": {
        "post": {
            ...
            "responses": {
                "400":{
                   "x-apifox-name": "Bad request",     
                   "description": "Bad Request. The request could not be understood by the server due to malformed syntax. A possible reason might be that the request contains Unicode characters that cannot be processed."
                   ...
               }
            }
        }
    }
}
```
