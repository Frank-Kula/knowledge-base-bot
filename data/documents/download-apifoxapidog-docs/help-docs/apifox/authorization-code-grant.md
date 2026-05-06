# 授权码授权类型



授权码授权类型（Authorization Code Grant Type）可能是你在使用 OAuth 2.0 时最常见的一种授权类型。它被 Web 应用程序和原生应用程序（如 iOS 或 Android）所使用，用于在用户授权应用程序之后获取访问令牌。

## 授权码授权类型的工作原理


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/486119/image-preview)
</Background>


上述示例图表说明了 OAuth 授权码授予流程中发生的交互。

1. 用户尝试访问应用程序（客户端）。
2. 客户端应用程序调用授权服务器的 `authorize` 端点。
3. 授权服务器响应重定向 URI，如果有的话，用户将被重定向到授权页面。
4. 用户通过其身份源（如用户名密码）进行身份验证并同意。
5. 授权服务器颁发授权码（code）。
6. 客户端应用程序使用在上一步提供的授权码请求身份验证到令牌端点，使用配置的身份验证方法和在前一步提供的授权码。
7. 授权服务器验证授权码（code）、客户端 ID 和客户端密钥。
8. 授权服务器返回访问令牌。
9. 客户端应用程序从资源服务器请求受保护资源，并提交在上一步收到的令牌（Token）。
10. 资源服务器验证令牌并响应请求的资源。

## 授权码授权类型的实际应用

### 获取用户的权限

OAuth 的目的是让用户授予应用程序有限的访问权限。应用程序首先需要确定它正在请求哪些权限，然后将用户导航到浏览器以获取他们的许可。为了开始授权流程，应用程序一般会构造如下所示的 URL，并打开一个属于该 URL 的浏览器窗口。

```js
https://authorization-server.com/auth
 ?response_type=code
 &client_id=29352915982374239857
 &redirect_uri=https%3A%2F%2Fexample-app.com%2Fcallback
 &scope=create+delete
 &state=xcoiv98y2kd22vusuye3kch
```

以下是每个查询参数的解释：

- `response_type=code` ：这告诉授权服务器（Authorization Server）正在启动授权码流程。
- `client_id` ：应用程序的公共标识符（客户端 ID），开发者在注册应用程序时获得。
- `redirect_uri` ：告诉授权服务器在用户同意请求后将用户进行重定向的回调地址。
- `scope` ：一个或多个用空格分隔的字符串，指示应用程序正在请求哪些权限。你正在使用的特定 OAuth API 将定义其支持的范围。
- `state` ：应用程序生成一个随机字符串，并将其包含在请求中。然后应用程序应检查用户授权应用程序后返回的相同值，这用于防止 CSRF 攻击。

当用户访问此 URL 时，授权服务器将向他们显示一个提示，询问他们是否想要授权此应用程序的请求。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/486120/image-preview)
</Background>


### 重定向回应用程序

如果用户同意了请求，授权服务器会在浏览器中重定向回应用程序指定的回调地址（redirect_uri），并在请求的 URL 上携带`code` 和 `state`。

例如，用户将被重定向回一个类似以下的 URL：

```js
https://example-app.com/redirect
 ?code=g0ZGZmNjVmOWIjNTk2NTk4ZTYyZGI3
 &state=xcoiv98y2kd22vusuye3kch
```

`state` 值将是应用程序最初在请求中设置的相同值，应用程序应检查重定向中的状态是否与其最初设置的状态相匹配，这可以防止 CSRF 和其他相关攻击。`code` 是授权服务器生成的授权码，此授权码的生命周期相对较短，通常持续时间为 1 到 10 分钟，具体取决于 OAuth 服务提供者。

### 通过授权码获取访问令牌

现在应用程序已经有了授权码（code），它可以用来获取访问令牌。

应用程序通过向授权服务器发送 POST 请求，请求获取访问令牌，在发起请求时，请求 Body 的类型为`Content-Type: application/x-www-form-urlencoded`。请求一般包含以下参数：

- `grant_type=authorization_code` : 这告诉授权服务器目前 OAuth 2.0 使用的类型是授权码授权类型。
- `code` - 应用程序在重定向中收到的授权码。
- `redirect_uri` - 请求代码时使用的相同重定向 URI。某些 API 不需要此参数，因此你需要仔细查看你要访问的特定 API 的文档。
- `client_id` - 应用程序的客户端标识符（客户端 ID）。
- `client_secret` - 应用程序的客户端密钥。这确保了获取访问令牌的请求仅来自应用程序，而不是可能拦截授权码的潜在攻击者。

授权服务器将验证请求中的所有参数，确保授权码（code）未过期，并且客户端 ID 和密钥匹配。如果一切正常，它将生成一个访问令牌（access_token）并在响应中返回，类似下面的响应。

```js
HTTP/1.1 200 OK
Content-Type: application/json
Cache-Control: no-store
Pragma: no-cache

{
  "access_token":"MTQ0NjJkZmQ5OTM2NDE1ZTZjNGZmZjI3",
  "token_type":"bearer",
  "expires_in":3600,
  "refresh_token":"IwOGYzYTlmM2YxOTQ5MGE3YmNmMDFkNTVk",
  "scope":"create delete"
}
```

以上就是授权码授权类型的整个流程，应用程序现在有了一个访问令牌（access_token），可在进行其它 API 请求时使用。

## 何时使用授权码流程

授权码流程最适用于 Web 和移动应用程序，由于授权码授权需要额外的步骤来交换授权码以获取访问令牌，因此它提供了额外的安全层，这在隐式授权类型中不存在。

如果你在移动应用程序或任何其他类型的应用程序中使用授权码流程，但无法存储客户端密钥，则还应该使用 [PKCE 模式](https://docs.apifox.com/authorization-code-grant-with-pkce.md)，该扩展提供了对授权码可能被拦截的其他攻击的保护。

