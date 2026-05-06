# 为组织配置单点登录



> [Apifox 商业旗舰版可使用单点登录（SSO）功能](https://www.apifox.com/pricing)

## 创建组织

你可以在主界面的侧边栏点击「组织」，然后点击「新建组织」，并输入组织的展示名称。

需要注意的是，如果你之前已经在 Apifox 创建了一个团队，并且希望将该团队置于组织的统一管理之下，则需要在创建新组织时选择这个现有团队，该团队的计费将被委托给组织。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/485423/image-preview)
</Background>


创建组织后，系统将生成一个由纯数字组成的默认名称。该名称是这个组织的唯一标识符，用于与单点登录相关的 URL。你可以将其修改为一个更容易被组织成员记住的名称。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/485425/image-preview)
</Background>


## 配置 SAML 单点登录

成功创建组织后，你可以点击「SAML 单点登录」进入单点登录的配置页。请执行以下操作：

- 开启「需要 SAML 身份验证」开关
- 从身份提供商（IdP）复制并填写「登录 URL」
- 从身份提供商（IdP）复制并填写「Issuer」
- 从身份提供商（IdP）获取证书，并在此处粘贴其内容
- 点击「保存」按钮，搞定，你已成功为组织启用了单点登录
在开启 SAML 身份验证后，组织的成员必须通过 SAML 身份提供商（IdP）进行身份验证才能访问企业的资源。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/485426/image-preview)
</Background>


需要注意的是，上述步骤的前提条件是你已经在身份提供商（IdP）的后台完成了相关配置。请参阅文档的相应部分，并按照其中概述的步骤操作：

- [Microsoft Entra ID (原 Azure Active Directory)](https://docs.apifox.com/microsoft-entra-id.md)

## 配置允许的电子邮件域名

你可以配置允许的电子邮件域名，拥有符合这些域名的电子邮件地址的任何人都可以通过单点登录加入你的组织。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/485427/image-preview)
</Background>


