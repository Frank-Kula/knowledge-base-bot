# Vault Secrets（密钥库）


> [Apifox 商业旗舰版可使用 Vault Secrets（密钥库）功能](https://www.apifox.com/pricing)

使用 Apifox 时，你可以从外部密钥库（例如 HashiCorp Vault、Azure Key Vault 和 AWS Secrets Manager）获取密钥，并在发送请求时像全局变量一样使用它们。

管理员可以为团队和项目配置与外部密钥库的集成，然后用户只需使用 OAuth2.0 登录或输入自己的 Token 即可从外部密钥库获取密钥。

获取的密钥会被加密存储在你的本地客户端中，不会与任何人共享。

## 配置密钥库提供商

- 在团队资源页面上，可以为团队配置多个密钥库提供商。团队的不同项目可以使用不同的提供商。


    <Background>

    ![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/489966/image-preview)
    </Background>

- 在项目中，你可以自定义项目的密钥库提供商，或使用团队提前配置好的提供商。


    <Background>

    ![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/489967/image-preview)
    </Background>


## 链接并获取密钥

- 单击项目右上角环境菜单旁边的按钮，然后在弹出的界面选择 Vault Secrets（密钥库）。
- 输入密钥名，然后单击值输入框以配置外部密钥库中密钥的元数据，例如 Secret Engine、Secret Path 和 Secret Key。请注意，密钥库提供商不同，需要配置的元数据的字段也会不同。

   
    <Background>

    ![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/489970/image-preview)
    </Background>


- 单击「获取密钥」按钮，获取的密钥会被加密存储在你的本地客户端中。


    <Background>

    ![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/489971/image-preview)
    </Background>


## 使用密钥

- 界面内任何可以使用变量的地方，都可以使用密钥，语法为 `{{vault:key}}` 。在全局变量、环境变量中，也可以引用密钥。

    
    <Background>

    ![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/489972/image-preview)
    </Background>


- 在脚本中，你可以使用 `await pm.vault.get("key")` 来获取密钥的值。如果使用 `console.log` 打印该值，该值将会被打码显示。


    <Background>

    ![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/489973/image-preview)
    </Background>


- 密钥的值不会与团队中的其他人共享，但密钥名称和密钥元数据会被共享。因此，团队内的其他成员无需配置密钥元数据，但得通过授权才能获取密钥。这可以在团队协作的便利性和隐私性之间取得平衡。

## 企业使用外部密钥库的优势

- 安全存储密钥：密钥库提供了一种安全的方式来存储 API 密钥、密码、证书和令牌等敏感信息，确保它们免受未经授权的访问。
- 访问控制：密钥库允许组织定义严格的访问控制策略，确保只有授权的用户或服务才能访问特定的密钥。
- 加密：密钥库通常提供内置加密来保护静态和传输中的数据，从而增加额外的安全层。
- 审计和监控：密钥库提供审计和监控功能，以跟踪谁访问了哪个密钥以及何时访问。这有助于合规性和检测任何未经授权的访问尝试。
- 与其他服务集成：密钥库旨在与其他云服务（包括 Apifox）和 DevOps 工具无缝集成，从而可以轻松管理各种环境中的密钥。
- 集中管理：密钥库提供了一种集中方式来管理不同应用程序、服务和环境中的密钥，从而简化了与密钥管理相关的开销。
- 降低风险：通过减少凭证被硬编码到应用程序或泄漏到源代码中的机会，密钥库有助于降低凭证暴露的风险。

## 使用 Apifox 密钥库的先决条件

- 密钥必须已存储在 HashiCorp Vault、Azure Key Vault 或 AWS Secrets Manager 中。
- 你的组织或团队已购买 Apifox 商业旗舰版。


