# OAuth 1.0

OAuth 1.0 是一种基于 OAuth 协议的授权机制，它允许第三方应用访问受保护资源。例如，作为 A 产品的用户，你可以直接使用 A 产品的账号登录 B 平台的系统，而不用暴露你在 A 平台的账号和密码才能完成登录。

OAuth 1.0 还使用了签名（Signature）来验证请求的完整性和真实性，以及时间戳（Timestamp）和随机数（Nonce）来防止重放攻击。此外，OAuth 1.0 中的令牌和密钥只有授权的应用程序和服务提供商才知道。

## 基础设置

在 “Auth” 页中，选择 “OAuth 1.0” 作为授权方式，并填写以下信息：

- **添加位置**

    支持 `Request Body/Request URL` 和 `Request Header`，你可以选择请求体或请求头。

- **Signature Method**

    签名方法，支持 `HMAC-SHA1`, `HMAC-SHA256`, `HMAC-SHA512`, `RSA-SHA1`, `RSA-SHA256`, `RSA-SHA512`, `PLAINTEXT` 算法。

- **Consumer Key**

    服务提供商分配给应用程序的唯一标识符。

- **Consumer Secret**

    由平台给应用程序分配的秘钥。

- **Access Token**

    访问令牌是用户授权后由服务提供商颁发的令牌，用于访问用户的受保护资源。它允许应用程序代表用户进行受限的操作，而无需用户提供他们的用户名和密码。

- **Token Secret**

    令牌密钥是与访问令牌相关联的秘密字符串。它与消费者密钥密钥一样，用于在 OAuth 1.0 握手期间创建签名，以确保请求的完整性和安全性。
    
<Background>
 ![](https://cdn.apifox.cn/uploads/help/202403281704160.png)
</Background>


## 高级设置

你可以点击 **“更多”** 选项添加更多加密设置。如果配置留空，它们会自动生成。


<Background>
![](https://cdn.apifox.cn/uploads/help/202403291533280.png)
</Background>


- **Callback URL**

    回调 URL 是 OAuth 1.0 授权流程的最后一步，它是用户在第三方应用授权后，服务提供商将用户重定向到的 URL。

- **Verifier**

    验证器是 OAuth 1.0 授权流程的中间步骤，它是由服务提供商生成的随机字符串，用于验证用户是否授权第三方应用访问其资源。

- **Timestamp**
  
    时间戳是 OAuth 1.0 请求中的一个参数，它用于防止重放攻击。它是一个 Unix 时间戳，表示请求发起的时间。

- **Nonce**

    随机数是 OAuth 1.0 请求中的一个参数，它用于防止重放攻击。它是一个随机字符串，用于唯一标识一次请求。

- **Version**
  
  默认情况下不需要更改。

- **Realm**
  
  用于标识受保护资源所属的安全域或范围。

除了以上选项，你还可以选择是否开启 `Include body hash` 和 `Add empty parameters to signature` 选项。

