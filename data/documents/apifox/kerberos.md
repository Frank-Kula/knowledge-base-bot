# Kerberos


Kerberos 是一种网络身份验证协议，最初由麻省理工学院（MIT）开发，广泛用于许多现代计算系统中，尤其是在企业环境中。Kerberos 使用对称加密和可信第三方，即密钥分发中心（Key Distribution Center, KDC），来实现其功能。


IIS 的身份认证如果选择 Windows 身份认证，则会优先使用 Kerberos。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/472895/image-preview)
</Background>


## 前提条件

要使用 Apifox 的 Kerberos 认证功能，请先确认当前电脑是否符合以下条件：
- Windows：已经成功加入域，或者拥有有效的 Kerberos 凭证
- macOS：拥有有效的 Kerberos 凭证
- Linux：拥有有效的 Kerberos 凭证

此外，仅 Apifox 客户端版本支持本功能，网页版无法使用。

## 设置

Kerberos 的认证参数如下：

- SPN
  
  格式为 `HTTP/hostname.domain.local@realm.name`，具体内容请咨询接口的提供方。
