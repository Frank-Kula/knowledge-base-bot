# Microsoft Entra ID



> [Apifox 商业旗舰版可通过 Microsoft Entra ID 进行单点登录（SSO）](https://www.apifox.com/pricing)

## 准备工作

在 Microsoft Entra ID 的后台进行配置之前，请打开 Apifox 组织设置中的 SAML 单点登录页面，开启「需要 SAML 身份验证」开关，并停留在这个页面。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/485615/image-preview)
</Background>


## 配置 Microsoft Entra ID

要配置你的 SAML 应用程序，请执行以下操作：

- 在浏览器中打开 Microsoft Entra ID 后台。
- 前往**企业应用程序**，选择**新建应用程序**。
- 单击**创建你自己的应用程序**，输入应用程序的名称，如 Apifox，然后选择「集成未在库中找到的任何其他应用程序（非库）」。
- 在应用程序的**概述**页面上，复制**应用程序 ID**，并将其粘贴到 Apifox 中的 **Issuer** 字段。
- 在应用程序的**概述**页面，点击**设置单一登录**，然后选择 **SAML** 作为单一登录方法。
- 复制 Apifox 中的**断言使用者服务 URL**，并将其粘贴到 Microsoft Entra ID 中基本 SAML 配置的**回复 URL（断言使用者服务 URL）**。
- 在 Microsoft Entra ID 中的 SAML 证书下载证书（Base64），用 Visual Studio Code 等代码编辑器打开它，复制文件中的文本，并将其粘贴到 Apifox 中的**证书**。
- 复制 Microsoft Entra ID 中的**登录 URL**，并将其粘贴到 Apifox 中的**登录 URL**。
- 保存 Microsoft Entra ID 和 Apifox 的这些配置。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/485616/image-preview)
</Background>


现在，你已经完成了 SAML 单点登录的配置。不过，还有一个步骤，那就是需要确定谁可以使用 SSO 登录 Apifox，然后把这些人添加到你刚刚在 Microsoft Entra ID 管理门户中创建的**企业应用程序**中。

## 测试你的 SAML 配置

现在你可以返回 Apifox 的主窗口，点击侧边栏中的组织名称，然后点击右侧的单点登录入口。请测试是否可以正常登录。

