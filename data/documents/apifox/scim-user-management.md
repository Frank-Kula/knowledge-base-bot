# SCIM 用户管理



> [Apifox 商业旗舰版可使用 SCIM 功能](https://www.apifox.com/pricing)

使用 Apifox 时，可以在组织级别配置 SCIM。Apifox 的 SCIM 支持与 SCIM 协议兼容的身份提供商 (IdP)，比如 Microsoft Entra ID（原 Azure Active Directory）。

当管理者在 IdP 中添加或移除用户时，这些更改将同步到 Apifox 的组织成员中。

## SCIM 功能

Apifox 支持以下 SCIM 功能：

- **添加用户：** 向组织中添加 SSO 身份。如果 Apifox 用户使用组织中的身份进行 SSO 登录，Apifox 账户将与 SSO 身份关联，并且该账户将变为激活状态。未激活的用户不会占用席位。

- **移除用户：** 如果企业管理员从 IdP 中删除了用户，并且该用户的 SSO 身份已与 Apifox 账户关联。那么，该用户将从相应的 Apifox 组织中移除。

Apifox 不支持以下 SCIM 功能：

- 更新用户（Update users）

- 组（Groups）

但是，Apifox 支持通过 SAML 将身份提供商 (IdP) 中的用户组映射到 Apifox 中的团队。详细信息请查看：[将组映射到团队](https://docs.apifox.com/map-groups-to-teams.md)。

## 配置 SCIM

配置并保存 SAML 后，你可以启用 SCIM：

- 点击“生成 SCIM Token”按钮。

- 复制“SCIM Token”并填写到你的身份提供商 (IdP) 的后台中。

- 复制“SCIM API 端点 URL”并填写到你的身份提供商 (IdP) 的后台中。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/485619/image-preview)
    
    
![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/485620/image-preview)
</Background>


接下来，你需要转到身份提供商的后台进行配置。了解更多详细信息请查看：

- [Microsoft Entra ID](https://docs.apifox.com/scmi-microsoft-entra-id.md)

## 企业使用 SCIM 的优势

- **简化身份管理：** 自动完成用户账户的配置和撤销配置，减少手动流程带来的管理负担和错误。

- **提高安全性：** 确保员工离职或更改角色时，及时撤销用户访问权限，降低未经授权访问的风险。

- **可扩展性：** 支持跨多种应用的大规模用户管理，使其非常适合拥有众多基于云服务的成长型组织。

- **互操作性：** 提供标准化的身份管理方法，允许不同身份系统和应用之间的无缝集成。

- **增强合规性：** 通过维护准确且最新的用户记录，促进更轻松地跟踪和报告访问控制，帮助遵守法规要求。

- **提高生产力：** 减少 IT 部门在日常任务上花费的时间，使他们能够专注于更具战略性的工作。

## 使用 Apifox 进行 SCIM 的先决条件

- 身份提供商 (IdP) 必须支持 SCIM 协议。

- 已在 Apifox 中设置组织并订阅了商业旗舰版付款计划。

- 组织已在使用 SAML 认证。

