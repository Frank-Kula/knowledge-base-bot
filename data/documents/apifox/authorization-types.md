# 支持的授权类型

Apifox 提供了非常多的 **授权类型**。你可以在接口的 **Auth** 部分的 **类型** 菜单中选择授权类型。**Auth** 可以应用于接口、目录和根目录级别。

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/472875/image-preview)
</Background>


## 从父级继承

“从父级继承”是 Apifox 的默认授权类型。当请求的授权类型设置为 “从父级继承” 时，它将继承父目录的授权设置，直到根目录为止。

## No Auth

如果选择 **无授权 (No Auth)**，Apifox 将不会包含任何授权信息。对于无需授权的请求，只需在 Auth 标签的 “类型” 下拉菜单中选择 “No Auth”。

## API Key

对于 API 密钥授权，你需要在请求头或查询参数中提供键值对。选择 “类型” 下拉菜单中的 “API Key”，然后输入你的键名 *（Key）* 和键值 *（Value）*，并选择将其添加到 **Header** 或 **Query Params**。为了增强安全性，建议将值存储在变量中。


<Background>
<img src="https://api.apifox.com/api/v1/projects/5097254/resources/472877/image-preview" width="560px"/>
</Background>


Apifox 会自动将必要的信息附加到你的请求头或 URL 查询字符串中。

## Bearer Token

Bearer Token 授权 *（例如 JSON Web Tokens，JWT）* 通过请求头中的访问密钥进行身份验证。选择 “类型” 列表中的 “Bearer Token”，并在 Token 字段中输入你的 API 密钥。为了更好的安全性，建议使用变量来存储和引用该令牌。

Apifox 将以以下格式将令牌添加到 Authorization 头中：
```
Bearer <你的 API 密钥>
```

<Background>
<img src="https://api.apifox.com/api/v1/projects/5097254/resources/491659/image-preview" width="560px"/>
</Background>

对于自定义前缀，可以使用 API Key 选项，并将 “Authorization” 作为键。

## JWT

Apifox 还支持 JWT 令牌的生成。选择 “类型” 选项中的 “JWT”。

你可以指定是否将令牌添加到 **Request Header** 或 **Query Param**，选择算法 *（HS、RS、ES 或 PS 变体，使用 SHA）*，并输入所需的秘密或私钥。将有效 Payload 数据以 JSON 格式输入。

高级设置允许你配置 HTTP Authorization 前缀和自定义 JWT Header。

## Basic Auth

Basic Auth 授权要求将验证过的凭证与请求一起发送。选择  “类型” 下拉列表中的 “Basic Auth”，并输入你的 API 用户名和密码。为了增强安全性，建议将这些信息存储在变量中。

Apifox 将在 Authorization 头中包含一个 Base64 编码的凭证字符串，格式如下：
```
Basic <Base64 编码的用户名和密码>
```

## 其他授权类型

Apifox 还支持以下授权类型：

- [Digest Auth](https://docs.apifox.com/digest-auth.md)
- [OAuth 1.0](https://docs.apifox.com/oauth1.md)
- [OAuth 2.0](https://docs.apifox.com/oauth2.md)
- [Hawk Authentication](https://docs.apifox.com/hawk-auth.md)
- [Kerberos](https://docs.apifox.com/kerberos.md)
- [NTLM](https://docs.apifox.com/ntlm.md)
- [Akamai EdgeGrid](https://docs.apifox.com/akamai-edgegrid.md)
