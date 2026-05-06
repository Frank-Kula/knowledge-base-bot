# Microsoft Entra ID


要为你的组织配置 SCIM 与 [Microsoft Entra ID](https://www.microsoft.com/en-gb/security/business/identity-access/microsoft-entra-id/)（原 Azure Active Directory），你必须拥有 Microsoft Entra ID 和 Apifox 的管理员访问权限。

## 准备工作

在 Microsoft Entra ID 仪表板中做配置工作之前，请导航到 Apifox 组织设置中的 SAML 单点登录页面。点击 **生成 SCIM Token** 按钮，并在接下来的步骤中保持此页面打开。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/485623/image-preview)
</Background>


## 修改 SSO 的声明

为了支持 SCIM 配置，你需要修改 SSO 的独特用户标识符声明：

- 在浏览器中打开你的 Microsoft Entra ID 管理门户。
- 转到 **企业应用程序** 并打开你想要配置的应用程序。
- 在应用程序的 **概述** 页面，点击 **设置单点登录**。
- 按以下方式设置 **唯一用户标识符（名称标识符）** 声明：
  
  - **名称标识符格式** 设置为 `永久`。
  - **源属性** 设置为 `user.objectid`。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/485624/image-preview)
    
![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/485625/image-preview)
</Background>


## 配置 SCIM

按照以下步骤配置你的 SCIM：

- 在浏览器中打开你的 Microsoft Entra ID 管理门户。
- 转到 **企业应用程序** 并打开你想要配置的应用程序。
- 在应用程序的 **概述** 页面，点击 **预配用户账户**。

  
    <Background>

    ![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/485627/image-preview)
    </Background>

- 点击 **开始**。


    <Background>
    ![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/485642/image-preview)
    </Background>


- 为 **预配模式** 选择 **自动**，然后复制并填写 Apifox 页面上的信息，之后点击测试连接。测试结果将显示在右上角。如果没有问题，保存设置。

  
    <Background>

    ![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/485629/image-preview)
    </Background>


- 保存后，你可以配置 **映射**。首先 **关闭** “组映射（Groups）”。

  
    <Background>

    ![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/485630/image-preview)
    </Background>


- 然后配置 “用户映射（Users）”。

  
    <Background>

    ![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/485631/image-preview)
    </Background>


- 删除 `externalId`。

  
    <Background>

    ![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/485632/image-preview)
    </Background>


- 编辑第一个属性，使其具有以下设置：
  
  - **源属性** 为 `objectId`
  - **目标属性** 为 `externalId`
  - **匹配优先级** 为 `1`

  
    <Background>

    ![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/485634/image-preview)


    ![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/485635/image-preview)
    </Background>




- 添加一个新的映射：
  
  - **源属性** 为 `userPrincipalName`
  - **目标属性** 为 `userName`


    <Background>

    ![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/485636/image-preview)
    </Background>


- 然后删除其他项目，仅保留以下项。


    <Background>

    ![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/485637/image-preview)
    </Background>

- 保存设置，然后返回配置主页并点击 **启动预配**。

  
    <Background>

    ![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/485639/image-preview)
    </Background>


- 过一会儿，配置结果将会显示。

  
    <Background>

    ![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/485640/image-preview)
    </Background>


## 测试你的 SCIM 和 SAML 配置

返回 Apifox，你可以看到未激活的用户。

- 一旦这些未激活的成员使用 SSO 登录，他们的状态将变为正常，并占用付费席位。
- 处于未激活状态的用户不会占用付费席位。
- 根据 Azure 的规则，大约每 40 分钟同步一次。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/485641/image-preview)
</Background>

