# Digest Auth

Digest Authentication（摘要认证）是一种用于 HTTP 访问控制的身份验证机制。它与 Basic Auth 类似，但相较于后者 Digest Auth 的认证方式更加安全。

## 基础设置

在 Basic Auth 中，客户端发送用户名和密码的明文形式给服务器，这些凭据可以在网络上传输，并且可能被中间人截获。为了解决这个问题，Digest Authentication 使用了加密算法来保护用户凭据的传输。

## 高级设置

你可以点击 **“更多”** 选项添加更多加密设置。如果配置留空，它们会自动生成。


<Background>
   <div style="text-align: center">
       <img style="width: 340px" src="https://api.apifox.com/api/v1/projects/5097254/resources/472879/image-preview" />
    </div>
</Background>



- **Realm**
  
  目标服务器在响应 Header 中设置的域，用于标识当前正在请求的资源。

- **Nonce**
  
  目标服务器在响应 Header 中指定的唯一字符串。

- **Algorithm**
  
  加密算法。支持 MD5、SHA-256、SHA-256-sess、SHA-512-256、SHA-512-256-sess 等。

- **qop**

   qop 是保护质量（Quality of Protection）的缩写，用于指定摘要认证的质量级别以及摘要算法。

   在 HTTP 头部中，qop 的值可以是以下之一：

    - **auth：** 表示使用身份验证质量保证。
    
    - **auth-int：** 表示使用身份验证质量保证以及完整性保护。

- **Client Nonce**

    Client Nonce（客户端随机数）是客户端生成的一个随机数，用于增加摘要认证的安全性。它包含在客户端发送的摘要认证请求中，并且在每次请求中都会生成一个新的随机数。

- **Opaque**

    Opaque 是服务器返回给客户端的一个随机字符串，用于增强认证的安全性。

