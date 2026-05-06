# 什么是 Basic Auth



Basic Auth，也称为 HTTP 基本认证（HTTP Basic Authentication），是一种用于 HTTP 协议的简单认证机制，HTTP 基本认证由互联网工程任务组（IETF）在 [RFC 7617](https://datatracker.ietf.org/doc/html/rfc7617) 中定义。在 Basic Auth 中，客户端在发送请求时，将用户名和密码以 Base64 编码的形式包含在请求头的 Authorization 字段中发送给服务器，服务器收到请求后，会解码 Authorization 字段并验证用户名和密码。

## Basic Auth 的工作原理

1. **客户端请求**：当客户端访问一个保护的资源时，如果没有提供认证信息，服务器会返回一个 401 Unauthorized 状态和一个 `WWW-Authenticate` 响应头，指示客户端需要通过何种认证机制进行认证。例如:

   ```js
   WWW-Authenticate: Basic realm="Access to the staging site", charset="UTF-8"
   ```

2. **编码认证信息**：客户端收到 401 响应后，会提示用户输入用户名和密码。然后，客户端将用户名和密码以 `username:password` 的形式拼接成一个字符串，再将这个字符串通过 Base64 编码方式编码成一个编码字符串。

3. **发送认证请求**：编码后的字符串被置于 HTTP 的 `Authorization` 请求头中并重新发送请求，格式如下：

   ```
   Authorization: Basic [encoded_string]
   ```

   其中 `[encoded_string]` 是 Base64 编码后的字符串。

4. **服务器认证**：服务器接收到包含认证信息的请求后，解码 Base64 编码字符串，提取用户名和密码，然后验证这些凭据。如果认证通过，则服务器会处理请求并返回所请求的资源。如果认证失败，它可以再次返回 401 状态码。

```js

客户端                                              服务器
  |                                                  |
  |------------- 发送请求（未认证） --------------->   |
  |                                                  |
  |                                                  |
  |<----------- 401 Unauthorized  ---------------    |
  |         (WWW-Authenticate: Basic)                |
  |                                                  |
  |                                                  |
  |----------- 提示用户输入用户名密码 -------------    |
  |                                                  |
  |                                                  |
  |----------- 编码认证信息（Base64） ------------>    |
  |                                                  |
  |                                                  |
  |--------------- 发送认证请求 ------------------>   |
  |      (Authorization: Basic [encoded_string])
  |                                                  |
  |                                                  |
  |<---------------- 服务器认证 ------------------    |
  |              （验证用户名和密码）                  |
  |                                                  |
  |                                                  |
  |-------------- 处理请求或返回 401 -------------    |
  |                                                  |

```

## 客户端如何使用 Basic Auth？

在客户端使用 `Basic Auth` 时，通常需要在 HTTP 请求的头部中添加一个字段来传递用户名和密码，这个字段的名称是`Authorization`，它的值是 `Basic`加上用户名和密码的 Base64 编码。下面是一个使用 JavaScript 的 Axios 库发送 `Basic Auth` 请求的例子：

```javascript
const axios = require('axios')

// 设置用户名和密码
const username = 'your_username'
const password = 'your_password'

// 构造认证信息
const credentials = `${username}:${password}`

// 对认证信息进行 Base64 编码
const encodedCredentials = Buffer.from(credentials).toString('base64')

// 发送请求
axios
  .get('https://api.example.com/data', {
    headers: {
      // highlight-next-line
      Authorization: `Basic ${encodedCredentials}`,
    },
  })
  .then((response) => {
    // 处理响应数据
    console.log('Response:', response.data)
  })
  .catch((error) => {
    // 处理错误
    console.error('Error:', error)
  })
```

## 安全性和限制

尽管 Basic Auth 是 HTTP 认证中最直接的一种方式，但它存在一些明显的安全风险：

- **明文问题**：Base64 是一种编码方式，而不是加密方式。任何人在拦截 HTTP 请求的情况下可以轻松地解码并获取用户名和密码。
- **不提供认证状态的持续性**：每次请求都需要发送用户名和密码，这可能会导致凭据被多次暴露。

因此，Basic Auth 通常不推荐用于传输敏感信息或在不安全的网络（如互联网）中使用，除非连接通过 SSL/TLS（如 HTTPS）来确保传输层的安全。

