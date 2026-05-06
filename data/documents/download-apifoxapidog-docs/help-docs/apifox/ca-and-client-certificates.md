# CA 和客户端证书

你可以在 Apifox 中添加和管理证书，以便在发送请求时启用身份验证。

要连接使用双向 TLS（mTLS）的 API，你需要在 Apifox 中添加客户端证书。双向 TLS 是一种身份验证方式，要求客户端和服务器双方都使用证书确认彼此身份。身份确认后，系统将建立加密连接。

此外，你还可以在 Apifox 中添加自定义 CA 证书。如果某个接口使用的是注册在内部证书注册表中的证书，从 Apifox 发送的请求可能会失败，并出现 “SSL 自签名证书” 错误。添加自定义 CA 证书后，你可以在不关闭 SSL 验证的情况下，成功向该接口发送请求。

## 管理证书

在 Apifox 设置中，你可以查看已安装的证书、添加新证书或移除现有证书。

<Steps>
  <Step>
选择右上角的设置图标 <Icon icon="material-outline-settings"/>。
  </Step>
  <Step>
选择 “证书管理” 标签。
      
<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/472872/image-preview)
</Background>

  </Step>
</Steps>


## 添加 CA 证书

为避免在发送请求时出现 “自签名证书” 错误，请将你的自定义 CA 证书添加到 Apifox 中。

<Steps>
  <Step>
打开 CA 证书旁边的切换按钮。
  </Step>
  <Step>
选择你的 CA 证书的 PEM 文件。（PEM 文件可以包含多个 CA 证书。）
  </Step>
</Steps>

## 添加客户端证书

要向使用双向 TLS 身份验证的 API 发送请求，请将客户端证书添加到 Apifox 中。

<Steps>
  <Step>
选择 “添加证书”。
  </Step>
  <Step>
输入证书的主机域名 *（不要包含协议）*。
      
主机字段支持模式匹配。如果输入 `*.example.com`，则所有 `example.com` 的子域名将使用相同的客户端证书。
  </Step>
  <Step>
（可选）输入与域名关联的自定义端口号。如果不指定端口，Apifox 将使用默认的 HTTPS 端口（443）。
  </Step>
  <Step>
选择证书的 CRT 文件和 Key 文件，或选择证书的 PFX 文件。
  </Step>
  <Step>
如果生成客户端证书时使用了密钥，请在框中输入；否则，留空。
  </Step>
  <Step>
选择 “添加”。
      
<Background>
  
![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/472873/image-preview)
</Background>

  </Step>
</Steps>

每个客户端证书都是针对特定域名的。要向更多域名发送请求，需为每个域名添加相应的证书。不要为同一域名添加多个证书，如果为一个域名添加多个证书，Apifox 将使用最后添加的证书。

## 编辑证书

添加后无法编辑证书。要进行更改，首先移除该证书，然后生成新证书并将其添加到 Apifox 中。

## 移除证书

如果不再需要某个证书以发送请求，可以将其移除。

- 要移除 CA 证书，选择证书旁的移除图标。
- 要移除客户端证书，选择证书旁的删除图标。

## 使用证书

添加客户端证书后，你不需要执行额外步骤即可在 Apifox 中使用该证书。当你向配置的域名发起 HTTPS 请求时，Apifox 会自动随请求发送客户端证书。该证书将通过 OpenSSL 处理，Apifox 不会更改证书。

如果你发起 HTTP 请求，Apifox 将不会发送该证书。
