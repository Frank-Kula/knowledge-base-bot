# 管理用户账号



> [Apifox 商业旗舰版可使用单点登录（SSO）功能](https://www.apifox.com/pricing)

## 通过单点登录加入组织

当新用户通过 SSO 成功登录 Apifox 时，如果组织内有可用席位，新用户将自动加入相应的组织。

单点登录有 2 种方法：

- 通过浏览器直接访问组织的 SAML 身份验证页面。该 URL 的格式为 `https://apifox.com/orgs/{org-name}/sso`，请用真实的组织名称替换`{org-name}`。
- 如果组织所有者配置了「允许的电子邮件域名」，用户可以在登录页面点击「使用 SSO 登录」，然后输入企业邮箱，以访问 SAML 身份验证页面。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/485607/image-preview)
</Background>


当用户通过 SSO 登录自动加入组织时，默认情况下会授予他们组织成员权限，但不会把他们分配给组织内的任何团队。组织所有者需要为这些成员手动分配相应的团队，使他们能够访问团队内的项目。

- [管理组织成员](#管理组织成员)
  
## 添加现有的用户账号

如果某人已经拥有 Apifox 帐户，组织所有者可以邀请他们加入组织内的团队。一旦他们接受邀请，就会加入你的组织并被分配到相应的团队。


<Background>
 
![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/485608/image-preview)
</Background>

## 管理组织成员

组织所有者可以查看组织成员的个人资料，包括他们关联的单点登录身份。此外，也可以将组织成员分配到团队。组织成员只有被分配到某个团队，才能访问该团队中的项目。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/485609/image-preview)
</Background>


