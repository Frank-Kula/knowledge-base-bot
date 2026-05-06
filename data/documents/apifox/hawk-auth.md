# Hawk Authentication

Hawk Authentication 是一种基于 HTTP 请求的认证协议，旨在提供简单、灵活且安全的身份验证机制。


<Background>
![](https://cdn.apifox.cn/uploads/help/202403281719321.png)
</Background>


## 基础设置

Hawk 的基础认证参数如下：

- **Hawk Auth ID**
  
  用于标识当前请求的身份验证 ID。

- **Hawk Auth Key**
  
  用于标识当前请求的身份验证密钥。

- **Algorithm**

  用于创建消息验证代码的算法，支持 SHA-256、SHA-1 等。

## 高级设置

你可以点击 **“更多”** 选项添加更多加密设置。如果配置留空，它们会自动生成。

- **User**

  用于标识当前请求的用户。

- **Nonce**
  
  由客户端生成的随机字符串。

- **ext**

  与 API 请求一起发送的任何特定于应用程序的信息。

- **app**

  凭据绑定应用程序，避免攻击者冒用颁发给其它人的凭据。

- **dlg**

  颁发凭据的应用程序 ID。

- **Timestamp**

  时间戳，用于防止时间窗口之外的请求。

- **Include payload hash**

  勾选后将包括负载哈希值。

