# Akamai EdgeGrid


Akamai EdgeGrid 是 Akamai 开发的一种基于 HTTP 请求的认证协议，它使用了签名算法来生成签名，保障请求的完整性和真实性，防止请求被篡改或伪造。如需了解更多关于 Akamai EdgeGrid 的信息，请访问[官方文档](https://developer.akamai.com/legacy/introduction/Client_Auth.html)。


<Background>
![](https://cdn.apifox.cn/uploads/help/202403281832268.png)
</Background>


## 基础设置

Akamai EdgeGrid 的基础认证参数如下：

- **Access Token**

  用于标识当前请求的访问令牌。

- **Client Token**
  
  用于标识当前请求的客户端令牌。

- **Client Secret**

  用于标识当前请求的客户端密钥。

## 高级设置

如果你还需要添加更多自定义选项，点击“更多”按钮进行填写。如果配置留空，它们会自动生成。

- **Nonce**
  
  由客户端生成的随机字符串。

- **Timestamp**
  
  时间戳，用于防止时间窗口之外的请求。

- **Base URL**

  用于标识当前请求的 API 目标地址。

- **Headers to Sign**

  选择要签名的请求头。


<Background>
![](https://cdn.apifox.cn/uploads/help/202403281838805.png)
</Background>


