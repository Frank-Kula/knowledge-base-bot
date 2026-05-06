# 什么是 JWT



JWT（JSON Web Tokens，[RFC 7519](https://datatracker.ietf.org/doc/html/rfc7519)）是一种开放标准，用于在网络上安全地传递信息作为 JSON 对象。这些信息可以被验证和信任，因为它们是数字签名的，JWT 可以使用密钥（HMAC 算法）或使用 RSA 或 ECDSA 的公/私钥对进行签名。JWT 通常用于身份验证和信息交换，特别是在 Web 应用程序的单点登录（SSO）场景中很常见。

## JWT 的数据结构

一个 JWT 本质上是一个被编码和加密过的容器，它由三部分组成：头部（header）、载荷（payload）、签名（signature）。头部包含了令牌的元数据和签名算法，载荷包含了需要传输的数据，签名用于验证令牌的完整性。它们使用点号 `.` 分隔，典型的 JWT 的结构如下所示：

```
Header.Payload.Signature
```

### Header（头部）

头部通常包含两部分信息：

- 令牌类型（typ），即 JWT。
- 签名算法（alg），比如 HMAC SHA256 或 RSA。

通常，头部采用 JSON 格式，并且经过 Base64URL 编码。一个典型的头部示例是：

```json
{
  "alg": "HS256",
  "typ": "JWT"
}
```

将此 JSON 进行 Base64 编码，形成 JWT 的第一部分。

```text
ewogICJhbGciOiAiSFMyNTYiLAogICJ0eXAiOiAiSldUIgp9
```

### Payload（载荷）

Payload（载荷）是 JWT 中的第二部分，它包含了声明（Claims），这些 Claims 是关于实体（通常是用户信息）和其他数据的语句。根据 JWT 规范（[RFC 7519](https://datatracker.ietf.org/doc/html/rfc7519)），这些 Claims 分为三种类型：

**1. Registered Claims**（注册声明）：这些是预定义的声明，虽然不是必须的，但是强烈推荐使用，以保证兼容性和互操作性。一些常见的注册声明包括：

- `iss`（Issuer）：令牌的发行者。
- `sub`（Subject）：令牌的主题，通常是令牌所代表的用户或实体。
- `aud`（Audience）：令牌的接收者，表示哪些实体可以使用该令牌。
- `exp`（Expiration Time）：令牌的过期时间，表示令牌在何时之后不再有效。
- `nbf`（Not Before）：令牌生效时间，在此时间之前令牌不可用。通常与 exp 一起使用，用于定义一个令牌的有效期。
- `iat`（Issued At）：令牌的签发时间，表示令牌何时被创建。
- `jti`（JWT ID）：表示 JWT 的唯一标识符。可以用于防止 JWT 重放攻击，每个 JWT 都有一个唯一的 ID。

**2. Public Claims**（公共声明）：这些声明是可以自由定义的，但为了避免与其他声明冲突，最好是使用 URI 形式来定义。公共声明的使用可以根据应用程序的需求来定义各种自定义的声明，例如用户角色、权限等。

**3. Private Claims**（私有声明）：这些是发送方和接收方共享的自定义声明，用于在双方之间传递特定于应用程序的信息。私有声明不受 JWT 规范的限制，可以根据应用程序的需求自由定义。

下面是一个示例 Payload（载荷），包含了注册声明和自定义声明：

```json
{
  "sub": "1234567890",
  "name": "John Doe",
  "admin": true,
  "iat": 1516239022,
  "exp": 1516242622
}
```

在这个示例中，`sub` 是主题（Subject），`name` 是自定义的公共声明，`admin` 表示用户是否为管理员，`iat` 表示令牌的签发时间，`exp` 表示令牌的过期时间。将其进行 Base64 编码，得到 Jwt 的第二部分:

```
ewogICJzdWIiOiAiMTIzNDU2Nzg5MCIsCiAgIm5hbWUiOiAiSm9obiBEb2UiLAogICJhZG1pbiI6IHRydWUsCiAgImlhdCI6IDE1MTYyMzkwMjIsCiAgImV4cCI6IDE1MTYyNDI2MjJ9
```

### Signature（签名）

Signature（签名）是 JWT 中的第三部分，它用于验证令牌的完整性。签名由头部（Header）、载荷（Payload）和密钥共同计算而来，确保令牌在传输过程中不被篡改。

根据 JWT 规范（[RFC 7519](https://datatracker.ietf.org/doc/html/rfc7519)），签名的计算流程如下：

1. 将头部和载荷分别进行 Base64 编码。
2. 使用指定的算法（在头部中指定）对编码后的头部和载荷以及密钥进行签名计算。
3. 将签名结果加入到 JWT 中，形成完整的 JWT 令牌。

由于签名使用了密钥进行计算，因此只有拥有正确密钥的接收方才能够验证签名的有效性。

下面是一个示例，演示了如何对给定的头部和负载数据进行签名计算。假设我们有以下头部和负载数据：

```json
Header: {"alg": "HS256", "typ": "JWT"}
Payload: {"sub": "1234567890", "name": "John Doe", "admin": true, "iat": 1516239022, "exp": 1516242622}
```

假设我们使用 HMAC SHA-256 算法进行签名计算，并且密钥为 "secret"。

1. 将头部和负载数据进行 Base64 编码：

   ```plaintext
   Encoded Header: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9
   Encoded Payload: ewogICJzdWIiOiAiMTIzNDU2Nzg5MCIsCiAgIm5hbWUiOiAiSm9obiBEb2UiLAogICJhZG1pbiI6IHRydWUsCiAgImlhdCI6IDE1MTYyMzkwMjIsCiAgImV4cCI6IDE1MTYyNDI2MjJ9
   ```

2. 将编码后的头部和负载数据以及密钥传入 HMAC SHA-256 算法进行签名计算。假设计算得到的签名为：

   ```text
   ZjQ2NzI4ZTcwYjM3MzQyMTA5OWEzYjZmY2JmYTJhYWJmOWIyMjQ5MzgxYjVkM2ZkOWI1ZjFmZDgyNDA2ZjY4MQ==
   ```

3. 将签名结果加入到 JWT 中，形成完整的 JWT 令牌：
   ```plaintext
   eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.ewogICJzdWIiOiAiMTIzNDU2Nzg5MCIsCiAgIm5hbWUiOiAiSm9obiBEb2UiLAogICJhZG1pbiI6IHRydWUsCiAgImlhdCI6IDE1MTYyMzkwMjIsCiAgImV4cCI6IDE1MTYyNDI2MjJ9.ZjQ2NzI4ZTcwYjM3MzQyMTA5OWEzYjZmY2JmYTJhYWJmOWIyMjQ5MzgxYjVkM2ZkOWI1ZjFmZDgyNDA2ZjY4MQ==
   ```

这就是一个完整的 JWT 令牌，其中包含了头部、负载和签名三个部分。

## JWT 的认证流程

JWT 的使用通常涉及三个步骤：当用户通过用户名和密码完成验证后，服务器将生成一个 JWT，并发送回客户端。客户端（通常是浏览器）将 JWT 存储在本地，并随每个请求一起发送到服务器。服务器通过查看签名来验证 JWT 的真实性，并提取 Payload 中的数据，完成用户的验证或其他任务。

```js

  +---------------------+         +---------------------+        +----------------------+
  |                     |         |                     |        |                      |
  |      用户登录        +--------->     服务器验证       +-------->        返回 JWT      |
  |                     |         |                     |        |                      |
  +----------+----------+         +----------+----------+        +-----------+----------+
              |                              |                              |
              |                              |                              |
              |                              |                              |
              |                              |                              |
              |                              |                              |
              |                              |                              |
              |                              |                              |
              |                              |                              |
              |                              |                              |
              v                              v                              v
  +----------+----------+         +----------+----------+        +-----------+----------+
  |                     |         |                     |        |                      |
  |      用户请求        +--------->    服务器接受请求    +-------->      验证 JWT        |
  |                     |         |                     |        |                      |
  +---------------------+         +---------------------+        +----------------------+

```

## 客户端如何使用 JWT ？

客户端收到服务器返回的 JWT，可以储存在 Cookie 里面，也可以储存在 localStorage。此后，客户端每次与服务器通信，都要带上这个 JWT（通俗的讲叫 Token 凭证）。在发送请求时，可将其携带在请求头（Header）的 Authorization 字段中，下面的示例简单地演示了如何使用 Axios 发送登录请求以获取 JWT，然后使用这个 JWT 发送另一个请求。

```js
// 引入 Axios 库
const axios = require('axios')

// 假设登录函数返回一个包含 JWT 的 Promise
async function login(username, password) {
  const response = await axios.post('https://your-api.com/login', {
    username: username,
    password: password,
  })
  return response.data.token
}

// 使用 JWT 发送请求的示例
async function fetchDataWithJWT(jwt) {
  try {
    const response = await axios.get('https://your-api.com/data', {
      headers: {
        // highlight-next-line
        Authorization: `Bearer ${jwt}`,
      },
    })
    console.log('请求成功:', response.data)
  } catch (error) {
    console.error('请求失败:', error.response.data)
  }
}

// 调用示例
async function main() {
  try {
    // 登录并获取 JWT
    const jwt = await login('username', 'password')

    // 使用 JWT发送请求
    await fetchDataWithJWT(jwt)
  } catch (error) {
    console.error('发生错误:', error)
  }
}

// 调用主函数
main()
```

