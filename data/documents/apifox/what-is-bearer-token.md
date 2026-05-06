# 什么是 Bearer Token



Bearer Token 是一种用于身份验证的访问令牌，它授权持有者（Bearer）访问资源的权限。当你向服务器发送请求时，你可以在请求头中携带 `Bearer Token`，服务器会根据这个 Token 来验证你的身份并授权你所请求的操作。

## Bearer Token 的工作原理

当用户成功登录后，服务器会生成一个`Bearer Token`并返回给客户端，客户端随后在发起请求时，会在 HTTP 头部包含这个 Token。`Bearer Token` 在请求头中以 Bearer 关键字加上令牌本身的形式发送，格式通常为`Authorization: Bearer <token>`。服务器接收到请求后，会检查请求头中的 Authorization 字段，如果它以 Bearer 关键字开头，服务器就会提取出后面的令牌，并使用令牌来验证请求的合法性和授权级别，确认无误后提供请求的资源。

```Javascript

+-----------------------------+         +-----------------------------+
|                             |         |                             |
|         用户登录             |         |   服务器生成 Bearer Token    |
|                             |         |                             |
+-----------------------------+         +--------------+--------------+
             |                                         |
             v                                         v
+-----------------------------+         +--------------+--------------+
|                             |         |                             |
|                             |         |                             |
|        客户端发起请求        +--------->   Bearer Token 发送给客户端  |
|                             |         |                             |
|                             |         |                             |
+-----------------------------+         +--------------+--------------+
                                                       |
                                                       v
                                        +--------------+--------------+
                                        |                             |
                                        |                             |
                                        |     客户端发起请求并携带      |
                                        |       Bearer Token          |
                                        |                             |
                                        |                             |
                                        +--------------+--------------+
                                                       |
                                                       v
                                        +--------------+--------------+
                                        |                             |
                                        |                             |
                                        |     服务器接收请求并验证      |
                                        |         Bearer Token        |
                                        |                             |
                                        |                             |
                                        +--------------+--------------+
                                                       |
                                                       v
                                        +--------------+--------------+
                                        |                             |
                                        |                             |
                                        |  服务器返回资源给客户端       |
                                        |                             |
                                        |                             |
                                        +--------------+--------------+

```

## 客户端如何使用 Bearer Token？

在发送请求时，将其携带在请求头（Header）的 Authorization 字段中，其字段值为 Bearer 关键字加上令牌本身，以下以 JavaScript 的 Axios 库为例：

```js
const axios = require('axios')

const url = 'https://api.example.com/data' // 替换为你要访问的 API 地址
const token = 'your_bearer_token' // 替换为你的 Bearer Token

axios
  .get(url, {
    headers: {
      // highlight-next-line
      Authorization: 'Bearer ' + token,
    },
  })
  .then(function (response) {
    console.log('请求成功:', response.data)
  })
  .catch(function (error) {
    console.error('请求失败:', error)
  })
```

:::tip[如何在 Apifox 中使用 Bearer Token？]
参考：[登录态（Auth）如何处理](https://docs.apifox.com/5802184m0.md)
:::
