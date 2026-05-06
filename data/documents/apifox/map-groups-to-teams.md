# 将组映射到团队



Apifox 不支持使用 SCIM 创建或删除组。但是，通过 SAML 将身份提供商（IdP）的组映射到 Apifox 组织中的团队是支持的。

## 修改 SSO 声明

为了支持通过 SAML 进行组映射，你需要添加一个 SSO 组声明：

- 在浏览器中打开你的 Microsoft Entra ID 管理门户。
- 转到 **企业应用程序** 并打开你的企业应用程序。
- 在应用程序的 **概述** 页面上，点击 **设置 SAML 单一登录**，并编辑 **属性与索赔**。

    
<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/485611/image-preview)
</Background>


- 点击 **添加组声明**，选择 **所有组**，勾选 **自定义组声明名称**，并将 “姓名” 设置为 “groups”。

 
<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/485612/image-preview)
</Background>


完成此设置后，当用户使用 SSO 登录时，Apifox 可以获取用户所属组的唯一标识符（对象 ID）。此外，Apifox 不会获取 Azure 中任何组的任何信息。

## 配置映射

接下来，我们可以配置组与团队之间的映射：

- 打开 Microsoft Entra ID 的 **组** 页面，你可以看到每个组都有一个 **姓名** 和 **对象 ID**。

<Background>
 
![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/485613/image-preview)
</Background>

- 在 Apifox 组织设置中打开 SAML 组页面，然后粘贴 Azure 组的名称和 ID。
- 设置该 Azure 组成员在每个 Apifox 团队中的权限。

  
<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/485614/image-preview)
</Background>


当用户使用 SSO 登录时，将根据配置授予相应的团队访问权限。
