# 创建鉴权组件

Apifox 提供了丰富的鉴权组件类型，支持的鉴权方式包括：

1. **API Key** - 通过 Header、Query 或 Cookie 传递密钥验证
2. **Bearer Token** - 使用携带令牌的 Authorization: Bearer 头部验证
3. **JWT** - JSON Web Token 格式的令牌验证
4. **Basic Auth** - 基本身份验证，使用用户名和密码
5. **Digest Auth** - 摘要认证，比基本认证更安全
6. **OAuth 2.0** - 开放授权标准，支持多种授权流程
7. **OAuth 1.0** - OAuth 的早期版本，采用不同签名方式
8. **Hawk Authentication** - 基于 HMAC 的认证协议
9. **AWS Signature** - 亚马逊 AWS 服务的签名认证方式
10. **Kerberos** - 网络认证协议，基于票据的认证
11. **NTLM Authentication** - 微软开发的认证协议
12. **Akamai Edgegrid** - Akamai API 平台的认证方式
13. **Customize** - Apifox 不支持的鉴权组件，将被归为此类


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/508835/image-preview)
</Background>

## 通过界面创建鉴权组件

<Steps>
  <Step>
    在项目中，定位到左侧菜单栏的 “组件库 -> 鉴权组件” 位置，点击 “新建鉴权组件”。
      
<Background>

![CleanShot 2025-04-01 at 10.32.26@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/508842/image-preview)
</Background>

  </Step>
  <Step>
    选择鉴权组件类型，填写名称和相关配置。
      
    <Background>

    ![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/508844/image-preview)
    </Background>

  </Step>
   <Step>
    点击 “保存” 完成创建
       
<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/508946/image-preview)
</Background>

  </Step>
  <Step>
    在鉴权组件的编辑界面，点击页面底部的 “高级配置”，系统会显示当前鉴权组件对应的 OAS 代码，支持 JSON 和 YAML 两种格式查看。
<Background>

![CleanShot 2025-04-01 at 18.32.52@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/509075/image-preview)
</Background>

    你可以在这里直接编辑 Schema，实现更复杂的配置定义，系统会根据你修改的 Schema 更新鉴权组件配置。
       

  </Step>
</Steps>



## 通过导入 OAS 创建鉴权组件

当你导入包含 Security Schemes 定义的 OpenAPI 文件时，Apifox 会自动识别并创建对应的鉴权组件，这些组件会出现在项目的 “鉴权组件” 列表中。

你可以在导入 OAS 文件时设置 Security 与 Auth 的关联方式：
<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/596121/image-preview)
</Background>



## 创建组合型鉴权组件

> Apifox 版本需 ≥ 2.7.12


在某些场景下，可能需要同时使用多个鉴权组件来验证请求。例如，一个接口可能既需要通过 API Key 验证，又需要通过 Bearer Token 验证。这种情况下，可以创建一个组合型鉴权组件，将多个鉴权组件组合在一起。


<Steps>
  <Step>
    在项目中，定位到左侧菜单栏的 “组件库 -> 鉴权组件” 位置。点击 “新建鉴权组件”，然后选择 “组合型鉴权组件”。
      
<Background>

![CleanShot 2025-05-28 at 15.31.19@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/528700/image-preview)
</Background>


  </Step>
  <Step>
    **名称**：为组合型鉴权组件命名，便于后续管理和识别。
    **鉴权组件**：从下拉菜单中选择需要组合的鉴权组件。可以选择多个鉴权组件，并且支持添加更多组件。
    
<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/528710/image-preview)
</Background>

      
  </Step>
  <Step>
    完成配置后，点击 “保存” 按钮完成创建。
  </Step>
   <Step>
    
<CardGroup cols={2}>
  <Card title="使用组合型鉴权组件" href="https://docs.apifox.com/use-security-schemes.md#使用组合型鉴权组件">
  </Card>
</CardGroup>
  </Step>
</Steps>


:::tip[]
组合型鉴权组件默认是“且”关系，即所有选定的鉴权组件都需要同时满足。如果需要实现“或”关系，可以直接在接口中引用多个鉴权组件，而无需创建组合型鉴权组件。
:::


## 创建 OAuth 2.0 鉴权组件

OAuth 2.0 是一种常用的授权框架，Apifox 对其提供了全面支持。创建 OAuth 2.0 鉴权组件时，需要配置以下内容：

1. **授权类型（Grant Type）**：支持 Authorization Code、Implicit、Client Credentials、Password
2. **URL 配置**：根据选择的授权类型，配置相应的 URL
   - Auth URL（授权地址）
   - Access Token URL（获取令牌地址）
   - Refresh URL（刷新令牌地址，可选）
   - Callback URL（回调地址，也称为 Redirect URL）
3. **Scope 配置**：定义应用可请求的权限范围
   - 添加 Scope 名称和描述
   - 为不同的授权类型配置不同的 Scope 集合


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/509031/image-preview)
</Background>

4. 点击 “测试” 鉴权组件按钮，在弹出的测试面板中，填写客户端 ID、密钥等必要信息，即可测试 OAuth 2.0 相关配置信息的准确性。


<Background>

![CleanShot 2025-04-01 at 17.23.37@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/509032/image-preview)
</Background>



