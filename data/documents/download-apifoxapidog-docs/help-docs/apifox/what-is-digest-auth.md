# 什么是 Digest Auth


Digest Auth（摘要认证），全称 Digest Access Authentication，是一种用于网络协议中的安全验证机制，它提供了比[基本认证](https://docs.apifox.com/what-is-basic-auth.md)（Basic Authentication）更安全的方式来管理网页或网络服务的用户验证。这种认证机制主要用于通过 HTTP 协议进行通信的场景中，是 HTTP 认证的一种方式，该规范被定义在 [RFC 7616](https://datatracker.ietf.org/doc/html/rfc7616) 中。

## Digest Auth 的工作原理

1. **客户端请求访问资源：** 当用户尝试访问一个受保护的资源时，客户端（通常是浏览器）会发送一个请求到服务器。

2. **服务器响应：** 如果资源需要认证，服务器会返回一个 401 未授权响应，并在响应头中包含一个 `WWW-Authenticate` 字段，该字段提供了进行下一步加密操作所需的数据，如域（Realm）、一个随机数（Nonce），以及其他可选参数。

3. **客户端计算摘要并发送：** 客户端使用用户名、密码和从服务器接收到的数据（比如：Realm、Nonce），生成一个加密的摘要（Digest）。这个过程通常涉及到哈希函数，如 MD5。客户端再次发送请求，附带 Authorization 头，其中包含摘要以及相关的认证信息。

4. **服务器验证：** 服务器接收到客户端的响应后，会用同样的方法计算摘要值，如果计算结果与客户端发送的摘要值匹配，则认证成功；否则，认证失败。

```js

客户端                                                 服务器
  |                                                     |
  | ----------- 1. 请求访问受保护资源 ----------------->  |
  |                                                     |
  |                                                     |
  | <---------- 2. 401 未授权，发送 challenge ---------  |
  |            包含随机数（nonce）和域（realm）           |
  |                                                     |
  |                                                     |
  | ----------- 3. 发送认证摘要 ---------------------->  |
  |             包含用户名、摘要值等                      |
  |                                                     |
  |                                                     |
  |<----------  4. 认证结果 -------------------------    |
  |              认证成功/失败                           |
  |                                                     |

```

## WWW-Authenticate 的响应头字段

在 HTTP Digest Auth（摘要认证）中，服务器通过 `WWW-Authenticate` 首部字段向客户端发出认证请求。根据 [RFC 7616](https://datatracker.ietf.org/doc/html/rfc7616) 规范，该字段包含若干参数，用于定义认证所需的具体细节。常见的字段及其描述如下：

- **realm：** 指定了受保护资源所在的域（realm），客户端通常会显示该信息，以提示用户输入正确的凭据。
- **nonce：** 一个唯一的随机字符串，用于防止[重放攻击](https://zh.wikipedia.org/wiki/%E9%87%8D%E6%94%BE%E6%94%BB%E5%87%BB)。服务器生成 nonce 值，并在每次需要进行身份验证时发送给客户端，客户端使用它来计算摘要。
- **algorithm：** 指定用于计算消息摘要的算法。常见的包括 MD5、MD5-sess、SHA-256 等。
- **qop：** 指定质询保护的类型（Quality of Protection），常见值为`auth`，表示身份验证质询。
- **nc (nonce count)：** 这是一个十六进制的计数器，表示客户端使用同一 `nonce` 值发送请求的次数。每次发送请求时，计数器的值都会增加。这确保了每个请求都是唯一的，从而阻止重放攻击。
- **cnonce (client nonce)：** 这是由客户端生成并发送的一个随机字符串，与服务器的 nonce 一起工作，增强了认证过程的安全性。客户端 nonce 确保了客户端生成的请求具有独特性，并可能参与生成响应中的摘要。
- **opaque：** 一个字符串，由服务器生成，并作为一个参数提供给客户端，客户端必须将其原样返回。通常用于增加安全性，防止攻击者获取敏感信息。
- **domain：** 指定了受保护资源的范围，即可以使用此认证机制的 URI 范围。
- **stale：** 指示服务器之前发送的 nonce 是否过期，当设置为 true 时，表示之前提供的认证信息已过期，需要客户端重新认证。

服务器向客户端提供认证所需的各项参数，下面是一个示例`WWW-Authenticate`响应头字段：

```js
HTTP/1.1 401 Unauthorized
WWW-Authenticate: Digest realm="example.com",
                   qop="auth,auth-int",
                   nonce="dcd98b7102dd2f0e8b11d0f600bfb0c093",
                   opaque="5ccc069c403ebaf9f0171e9517f40e41",
                   stale="false",
                   algorithm=MD5
```

在这个示例中，服务器向客户端提供了`realm`、`qop`、`nonce`、`opaque` 和 `stale` 这些字段，用于协助客户端进行 Digest Auth（摘要认证）。

在客户端响应服务器的`WWW-Authenticate`请求时，客户端将这些值包含在 Authorization 头字段中，形式大致如下：

```js
Authorization: Digest username="user",
               realm="example.com",
               nonce="dcd98b7102dd2f0e8b11d0f600bfb0c093",
               uri="/dir/index.html",
               qop=auth,
               nc=00000001,
               cnonce="0a4f113b",
               response="6629fae49393a05397450978507c4ef1",
               opaque="5ccc069c403ebaf9f0171e9517f40e41"
```

## 客户端如何使用 Digest Auth？

在客户端使用 HTTP Digest Auth（摘要认证）通常涉及几个步骤，一般情况下你需要手动处理认证过程，即需要自行处理服务器的挑战（challenge），计算响应值（response），再发起请求。以下一个基本的示例说明如何在 JavaScript 中处理摘要认证，使用 Axios 作为 HTTP 客户端库。注意，以下代码不是即插即用的完整实现，但展示了核心逻辑。

### 1.发送初步请求，获取 challenge 参数

```javascript
import axios from 'axios'

// 初始请求资源URL
const url = 'http://example.com/protected'

// 第一次请求，预期会失败并获得 401 和 WWW-Authenticate 头
axios.get(url).catch((error) => {
  if (error.response && error.response.status === 401) {
    const wwwAuthenticate = error.response.headers['www-authenticate']
    const authDetails = parseWWWAuthenticate(wwwAuthenticate)
    performDigestAuth(authDetails, url)
  }
})

// 解析认证头信息的函数
function parseWWWAuthenticate(header) {
  const parts = header.split(',')
  const details = {}
  parts.forEach((part) => {
    const [key, value] = part.split('=')
    details[key.trim()] = value.replace(/"/g, '')
  })

  return details
}
```

### 2.使用认证参数和用户信息计算响应，发起认证请求

```javascript
function performDigestAuth(authDetails, url) {
  // 认证参数 authDetails 中包含realm, nonce等
  const username = 'your_username'
  const password = 'your_password'

  const cnonce = generateCNonce()
  const nc = '00000001' // Nonce count, 多次请求时递增
  const response = calculateDigestResponse(
    authDetails,
    username,
    password,
    cnonce,
    nc,
  )

  // 构造 Authorization 头
  const authHeader = `Digest username="${username}", realm="${authDetails.realm}", nonce="${authDetails.nonce}", uri="${url}", response="${response}", opaque="${authDetails.opaque}", qop=${authDetails.qop}, nc=${nc}, cnonce="${cnonce}"`

  // 使用摘要认证信息再次发起请求
  axios
    .get(url, {headers: {Authorization: authHeader}})
    .then((response) => {
      console.log('Authenticated Request Successful', response.data)
    })
    .catch((error) => {
      console.log('Authenticated Request Failed', error)
    })
}

function generateCNonce() {
  return Math.random().toString(36).substring(7)
}

function calculateDigestResponse(authDetails, username, password, cnonce, nc) {
  // 需要根据RFC 7616实现摘要计算
  // 示例仅为演示目的
  // 通常会涉及到MD5或其他散列函数生成response
  return 'Calculated response hash here'
}
```

在实际实现中，你需要根据 [RFC 7616](https://datatracker.ietf.org/doc/html/rfc7616) 设定的公式和方法，正确生成 response 值。这包括使用合适的散列函数（如 MD5）计算 HA1、HA2，最后计算 response 值。还应该处理 `auth-int` 中的实体主体散列处理（如果使用了 qop=auth-int）。

