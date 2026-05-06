# OAuth 2.0


Apifox 可以直接按照 OAuth 2.0 规范生成 token，并将其附加到请求内，无需在其他工具中生成后再粘贴过来，非常方便。


<Background>
![](https://cdn.apifox.cn/uploads/help/202403281705865.png)
</Background>


:::tip[系列教程]
- [使用 Apifox 配置 OAuth 2.0 并直接获取访问令牌](https://apifox.com/blog/oauth-2/)
- [使用 Github 的 OAuth 2.0 服务登录第三方网站](https://apifox.com/apiskills/how-to-use-github-oauth2/)
- [使用钉钉的 OAuth 2.0 服务进行登录并获取 Token](https://apifox.com/apiskills/how-to-use-dingding-oauth2/)
- [使用 Google 谷歌 OAuth 2.0 服务登录第三方网站](https://apifox.com/apiskills/how-to-use-google-oauth2/)
- [使用 Facebook 脸书 OAuth 2.0 服务登录第三方网站](https://apifox.com/apiskills/how-to-use-facebook-oauth2/)
- [使用 Twitter 推特 OAuth 2.0 服务登录第三方网站](https://apifox.com/apiskills/how-to-use-twitter-oauth2/)
:::


## 基础设置

按照 OAuth 2.0 规范生成 Token，首选需要选择授权模式。不同的授权模式下所需的配置内容和获取 Token 的流程也不同，支持以下五种授权模式：

- Authorization Code
- Authorization Code(With PKCE)
- Implicit
- Password Credentials
- Client Credentials

### Authorization Code

必填项：

- **Auth URL**
  
  登录页的 URL，一般在第三方 OAuth 2.0 服务的后台内获取。

- **Access Token URL**
  
  通过 Code 获取 Token 的 URL，一般在第三方 OAuth 2.0 服务的后台内获取。

- **Callback URL**
  
  登录成功后的回调 URL，也叫 Redirect URL，一般是自己业务的域名。需要提前将其录入第三方 OAuth 2.0 服务的后台。

- **Client ID**

  又称为 App ID，一般在第三方 OAuth 2.0 服务的后台内获取。

- **Client Secret**
  
  又称为 App Secret，一般在第三方 OAuth 2.0 服务的后台内获取。

填写完必填项之后，点击“获取 Token”按钮，就会弹出登录页面。在登录页面内完成登录流程后，登录页面会自动关闭，并自动获取 Token。


<Background>
![](https://cdn.apifox.cn/uploads/help/202403291601824.png)
</Background>


获取 Token 成功后，界面上会展示 Token 内容及其有效期。有了 Token 后就可以点击“发送”按钮，已生成的 Token 就会自动附加到 `Authorization Header` 内，添加至 `Bearer` 的前缀后发送出去。

### 选择使用 Access Token 或 ID Token

如果 OAuth 2.0 服务同时返回了 `Access Token` 和 `ID Token`，Apifox 会默认使用 `Access Token`。如果希望切换至 `ID Token`，那么可以在“使用的 Token 类型”选项中切换至 `ID Token`。


<Background>
![](https://cdn.apifox.cn/uploads/help/202403291621284.png)
</Background>


### 刷新 Token

如果 OAuth 2.0 返回了 `Refresh Token`，将会出现「刷新 Token」按钮。如果 Token 过期了，点击“刷新 Token” 按钮即可直接获取新的 Token，而不会弹出登录窗口。


<Background>
![](https://cdn.apifox.cn/uploads/help/202403291622376.png)
</Background>


### 重新获取 Token

如果 OAuth 2.0 没有返回 Refresh Token，那么当 Token 过期后，可以点击“重新获取 Token”按钮，在弹出的登录窗口重新进行登录流程。


<Background>
![](https://cdn.apifox.cn/uploads/help/202403291624522.png)
</Background>


### 更换登录账号

一般来说，OAuth 2.0 服务的登录页面会记录用户的登录状态。重新获取 Token 时默认会使用上一次登录的账号。如果希望更换账号，则可以点击“清除 Cookies”按钮，再点击“获取 Token”。


<Background>
![](https://cdn.apifox.cn/uploads/help/202403291632802.png)
</Background>


## 高级设置

你可以点击**“更多”**选项添加更多加密设置。如果配置留空，它们会自动生成。

- **Scope**

    Scope 是 OAuth 2.0 授权范围，用于限制访问的资源范围。

- **State**

    State 是 OAuth 2.0 授权请求的附加参数，可以用来防止跨站请求伪造（Cross-Site Request Forgery，CSRF）攻击。

- **Credentials**
  
  提供 `Send as Basic Auth header` 和 `Send client credentials in body` 两种方式。

- **Refresh Token URL**

    如果你希望 Refresh Token URL 与 Access Token URL 有所差异，可以该选项配置。

  
    <Frame>
      ![](https://cdn.apifox.cn/uploads/help/202403291659573.png)
    </Frame>


- **Http Authorization 前缀**

    一般为 `Bearer`，你也可以按照实际需求进行调整。

    
    <Background>
    ![](https://cdn.apifox.cn/uploads/help/202403291635557.png)
    </Background>


