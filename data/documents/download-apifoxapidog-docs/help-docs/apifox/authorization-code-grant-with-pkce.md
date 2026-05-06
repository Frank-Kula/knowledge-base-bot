# 授权码授权类型，带有 PKCE


当客户端（通常是移动或 JavaScript 应用程序）需要访问受保护的资源时，将使用授权码授权类型的 PKCE 标准（Authorization Code Grant Type，With PKCE），该 OAuth 2.0 规范在 [RFC 7636](https://datatracker.ietf.org/doc/html/rfc7636) 中定义。

## 什么是带有 PKCE 的授权码授权类型

该流程与常规授权码授权类型（Authorization Code Grant Type）类似，但客户端必须生成一个 code，该 code 将成为客户端和授权服务器之间通信的一部分，此 code 可以防止恶意用户执行的截获攻击。

PKCE 流程在授权码授权类型的基础上增加了三个参数：

- **code_verifier**（表单参数）：包含一个随机字符串，将授权请求与令牌请求相关联。
- **code_challenge**（查询参数）：包含从`code_verifier`派生的字符串，该字符串在授权请求中发送，并且需要稍后使用`code_verifier`进行验证。
- **code_challenge_method**（查询参数）：包含用于导`code_challenge`的方法。

## PKCE 的工作原理


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/486121/image-preview)
</Background>


上面的示例图解说明了在 PKCE 下进行 OAuth 授权码授予流程时发生的交互。

1. 用户尝试访问客户端应用程序。
2. 客户端应用程序生成`code_verifier`并将其转换为`code_challenge`。
   - `code_verifier`是一个随机密钥，用于防止授权码被拦截。`code_verifier`由客户端应用程序为每个授权请求生成，并根据预先为客户端应用程序设置的`code_challenge_method`转换为`code_challenge`。在可能的情况下，必须将`code_challenge_method`的值设置为`S256`。
3. 客户端应用程序调用授权服务器的`authorize`端点，并在授权请求中发送`code_challenge`。
   - 必须为客户端应用程序配置至少一个重定向 URI。当应用程序具有多个重定向 URI 时，对`authorize`端点的请求必须始终包括`redirect_uri`参数。
   - 除了请求外，客户端应用程序还发送`code_challenge`和`code_challenge_method`。
4. 授权服务器使用重定向 URI 进行响应，用户被重定向到授权页面（如果有的话）。
5. 用户使用其身份源（比如用户名密码）进行身份验证并给予同意。
6. 授权服务器颁发授权码。
7. 客户端应用程序使用上一步中提供的授权码向`token`端点请求身份验证。
   - 向授权服务器的请求还必须包括与发送到授权端点的请求中相等的`code_challenge`，这是成功发放令牌的强制要求之一。
8. 授权服务器验证授权码`code_verifier`和`code_challenge`。
   - 如果以下条件成立：
     - 授权码有效
     - 在步骤 3 和 7 中发送的`code_verifier`和`code_challenge`的值相等（成对），则
9. 授权服务器返回令牌。
10. 客户端应用程序向资源服务器请求受保护资源，并提交其在上一步中收到的令牌。
11. 资源服务器验证令牌并响应所请求的资源。

以上就是 OAuth 2.0 PKCE 的工作原理。

