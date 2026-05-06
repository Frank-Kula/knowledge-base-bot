# 认证与授权

API 使用身份验证和授权来确保客户端请求安全地访问数据。身份验证用于验证请求发送者的身份，而授权则确认发送者是否有权限访问 API。

如果你在构建 API，可以选择多种身份验证方式；如果你对接第三方 API，所需的授权方式通常由 API 提供商指定。

## Apifox 中的身份验证

某些 API 需要通过数字证书来验证客户端身份。你可以将证书授权机构（CA）或客户端证书添加到 Apifox 中，以便访问需要身份验证的 API。有关更多信息，请访问在 Apifox 中添加和管理 [CA 和客户端证书](https://docs.apifox.com/ca-and-client-certificates.md)。

## Apifox 中的授权

在 Apifox 中，你可以将授权信息附加到任何请求中，授权数据可以通过请求头、请求体或作为请求参数传递。

当你在请求的 **Auth** 模块中输入授权信息时，Apifox 会根据你选择的授权类型自动填充请求的相关部分。

你可以在接口或目录的 **Auth** 模块中选择授权类型，并填写相应的信息。

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/470084/image-preview)
</Background>

有关每种授权类型的详细信息，请访问 [Apifox 支持的授权类型](https://docs.apifox.com/authorization-types.md)。
