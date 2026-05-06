# 什么是 OAuth 1.0



OAuth 1.0 是一种开放授权协议，允许用户授予第三方应用程序访问其受保护资源的权限，而无需共享其密码或其他敏感信息。它是一种授权机制，用于用户在不泄露其密码的情况下，让第三方应用程序访问其在线账户。OAuth 1.0 的规范在 [RFC 5849](https://datatracker.ietf.org/doc/html/rfc5849) 中定义。

## OAuth 1.0 术语

OAuth 1.0 保障安全性的关键在于每一步请求都需要客户端进行签名，以确保请求的合法性。请求通常包括消费者的密钥、令牌密钥（如果有）、时间戳、随机数、请求方法和请求 URL 等，通过特定算法生成一个签名。这样，即使请求被截获，没有相应的密钥信息也很难被伪造。根据 RFC 5849 规范，一般 OAuth 1.0 授权时涉及到的字段主要包括：

1. **消费者 Key (Consumer Key)**: 标识 OAuth 消费者的唯一标识符。
2. **消费者密钥 (Consumer Secret)**: 用于验证 OAuth 消费者身份的密钥。
3. **令牌 (OAuth Token)**: 用于表示用户和 OAuth 服务提供者之间的授权关系的令牌。
4. **令牌密钥 (Token Secret)**: 与令牌相关联的密钥，用于验证令牌的有效性。
5. **签名方法 (Signature Method)**: 用于生成签名的方法，例如 HMAC-SHA1。
6. **签名 (Signature)**: 使用 OAuth 令牌密钥对请求参数进行签名，以确保请求的完整性和安全性。
7. **时间戳 (Timestamp)**: 用于防止重放攻击的时间戳。
8. **随机字符串 (Nonce)**: 用于防止重放攻击的随机字符串。
9. **版本 (OAuth Version)**: OAuth 协议的版本号，通常为 "1.0"。
10. **回调地址(Callback URL)**: 在授权过程中，用于将用户重定向到你的应用程序，以进行授权成功后的处理。
11. **Verifier（验证器）**: 用于在 OAuth 授权流程中交换访问令牌时验证用户身份。
12. **Realm（域）**: 用于指定受保护资源所属的范围或领域，它提供了关于受保护资源所在位置或所属身份域的信息。

## OAuth 1.0 的授权流程

OAuth 1.0 协议定义了几种角色：

1. **资源拥有者（Resource Owner）**：通常是指服务的使用者，即最终用户。
2. **客户端（Client）**：想要访问资源拥有者信息的第三方应用。
3. **资源服务器（Resource Server）**：存放用户资源的服务器。
4. **授权服务器（Authorization Server）**：在 OAuth 1.0 中，授权服务器与资源服务器可以是同一个服务器，负责处理与授权相关的所有请求。

其授权流程大概分为以下几个步骤：

1. **临时凭证获取（Temporary Credentials Acquisition）**：

   - 客户端（第三方应用）向授权服务器发起请求，要求一个临时凭证（类似于未来要换取访问令牌的“预授权”令牌）。
   - 通常需要提供消费者密钥（Consumer Key，向服务提供商注册时获得）来验证客户端的身份。
   - 授权服务器回应一个未经授权的临时凭证。

2. **资源拥有者授权（Resource Owner Authorization）**：

   - 客户端将资源拥有者引导到授权服务器的登陆和授权页面。
   - 资源拥有者同意授予权限后，授权服务器会将资源拥有者重定向回客户端，提供一个认证标记。

3. **令牌凭证交换（Token Credentials Exchange）**：
   - 客户端使用从授权服务器获得的认证标记和临时凭证回到授权服务器，请求换取一个访问令牌（Token Credentials）。
   - 如果验证成功，授权服务器会发放访问令牌和访问令牌密钥，客户端可以使用这些信息访问资源服务器上受保护的资源。

以下是 OAuth 1.0 授权流程的简要示意图：

```js
+-------------------+                                +----------------------+
|     Client        |                                |    授权服务器         |
|   (第三方应用)     |                                |   及资源服务器        |
+-------------------+                                +----------------------+
         |                                                      |
         |                                                      |
         |   1. 客户端请求临时凭证                                |
         |----------------------------------------------------->|
         |                                                      |
         |                                                      |
         |   2. 服务器颁发未授权的临时凭证                        |
         |<-----------------------------------------------------|
         |                                                      |
         |                                                      |
         |   3. 客户端源拥有者登录并授权                          |
         |----------------------------------------------------> |
         |                                                      |
         |                                                      |
         |   4. 资源拥有者授权后，服务器使用认证标记重定向回客户端   |
         |<-----------------------------------------------------|
         |                                                      |
         |                                                      |
         |   5. 客户端使用认证标记和临时凭证请求访问令牌            |
         |----------------------------------------------------->|
         |                                                      |
         |                                                      |
         |   6. 服务器验证后颁发访问令牌                          |
         |<-----------------------------------------------------|
         |                                                      |
         |                                                      |
         |   7. 客户端使用访问令牌访问受保护的资源                 |
         |----------------------------------------------------->|
         |                                                      |

```

## OAuth 1.0 的授权示例

假设有一个应用程序希望通过 OAuth 1.0 协议来获取用户的资源，而服务提供者（Service Provider）是一个虚构的社交媒体平台，以下步骤是 OAuth 1.0 授权的基本流程。

### 1.注册应用程序

首先，应用程序需要在服务提供者的开发者平台上注册，获取到 Consumer Key 和 Consumer Secret。

- 涉及的参数：

  - Consumer Key: 应用程序的唯一标识符。
  - Consumer Secret: 用于验证应用程序身份的密钥。

- 示例：

  - Consumer Key: abc123
  - Consumer Secret: xyz789

### 2.获取临时令牌（Request Token）

应用程序向服务提供者发送请求，请求获取临时令牌。这个请求中包含了消费者的凭证（Consumer Key）以及签名等信息。

- 涉及的请求参数：
  - oauth_consumer_key: abc123
  - oauth_signature_method: HMAC-SHA1
  - oauth_timestamp: 时间戳
  - oauth_nonce: 随机字符串
  - oauth_signature: 使用 Consumer Secret 生成的签名
- 示例请求：
  ```js
  POST /oauth/request_token HTTP/1.1
  Host: serviceprovider.com
  Authorization: OAuth oauth_consumer_key="abc123", oauth_signature="SIGNATURE", ...
  ```
- 示例响应：
  ```js
  oauth_token=TEMP_TOKEN&oauth_token_secret=TEMP_TOKEN_SECRET
  ```

### 3.重定向用户进行授权

应用程序将用户重定向到服务提供者的授权页面，要求用户授权访问其资源。在重定向的 URL 中包含了临时令牌以及回调地址。

- 涉及的请求参数：
  - oauth_token: TEMP_TOKEN
  - oauth_callback: YOUR_CALLBACK_URL
- 示例 URL：
  ```js
  https://serviceprovider.com/oauth/authorize?oauth_token=TEMP_TOKEN&oauth_callback=YOUR_CALLBACK_URL
  ```

### 4.用户授权

用户在服务提供者的授权页面上登录并确认授权请求。

### 5.获取访问令牌（Access Token）

用户授权完成后，服务提供者将用户重定向回应用程序提供的回调地址，并携带授权后的临时令牌和 Verifier。

- 涉及的参数：

  - oauth_token: TEMP_TOKEN
  - oauth_verifier: VERIFIER

- 示例回调 URL：
  ```js
  YOUR_CALLBACK_URL?oauth_token=TEMP_TOKEN&oauth_verifier=VERIFIER
  ```

### 6.交换临时令牌和 Verifier 获取访问令牌

应用程序使用之前获取的临时令牌和 Verifier，结合 Consumer Secret 发送请求，向服务提供者请求获取访问令牌。

- 涉及的请求参数：
  - oauth_consumer_key: abc123
  - oauth_token: TEMP_TOKEN
  - oauth_verifier: VERIFIER
  - oauth_signature_method: HMAC-SHA1
  - oauth_timestamp: 时间戳
  - oauth_nonce: 随机字符串
  - oauth_signature: 使用 Consumer Secret 和 TEMP_TOKEN_SECRET 生成的签名
- 示例请求：
  ```js
  POST /oauth/access_token HTTP/1.1
  Host: serviceprovider.com
  Authorization: OAuth oauth_consumer_key="abc123", oauth_token="TEMP_TOKEN", oauth_verifier="VERIFIER", oauth_signature="SIGNATURE", ...
  ```
- 示例响应：
  ```js
  oauth_token=ACCESS_TOKEN&oauth_token_secret=ACCESS_TOKEN_SECRET
  ```

### 7.访问受保护资源

现在，应用程序可以使用获取到的访问令牌来访问用户的受保护资源。

