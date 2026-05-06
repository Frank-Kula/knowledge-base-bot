# NTLM


NTLM（NT 本地身份验证）是微软开发的一种基于 HTTP 请求的认证协议，它使用了 NTLMv1 和 NTLMv2 算法来生成签名，保障请求的完整性和真实性，防止请求被篡改或伪造。如需了解更多关于 NTLM Authentication 的信息，请访问[官方文档](https://docs.microsoft.com/zh-cn/windows/security/threat-protection/security-policy-settings/network-security-lan-manager-authentication-level)。


<Background>
![](https://cdn.apifox.cn/uploads/help/202403281824129.png)
</Background>


## 基础设置

NTLM Authentication 的基础认证参数如下：

- **Username**

  用于标识当前请求的用户名。

- **Password**

  用于标识当前请求的密码。


## 高级设置

你可以点击“更多”选项添加更多签名参数。如果配置留空，它们会自动生成。

- **Domain**

  用于标识当前请求的域名。

- **Workstation**

  用于标识当前请求的工作站。


    <Background>
    ![](https://cdn.apifox.cn/uploads/help/202403281828349.png)
    </Background>


