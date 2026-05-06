# 自定义域名

Apifox 支持为在线文档站配置自定义域名，便于对外展示项目文档。你可以将文档站绑定到自己的域名（例如 `docs.example.com`），代替默认的 `xx.apifox.cn` 地址。

Apifox 提供两种方式配置自定义域名：

- **方式一：通过 CNAME 配置域名解析**

- **方式二：通过自有服务器中转**

在使用自定义域名前，请确保该域名已完成 ICP 备案（中国大陆服务器适用）。


## CNAME 方式

CNAME（Canonical Name）记录，也叫 “别名记录”，是 DNS 记录类型之一，用于将一个域名别名指向另一个规范域名。


### 获取 CNAME 值

进入 “分享文档 -> 发布文档站” 的发布设置页面，点击 “自定义域名” 标签页找到对应的 CNAME 值并进行复制。


<Background>

![CleanShot 2025-07-09 at 11.23.17@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/543760/image-preview)
    

![CleanShot 2025-07-09 at 11.25.55@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/543767/image-preview)
</Background>

Apifox 会根据你的域名备案情况，提供多个可选的 CNAME 地址：

- **域名已在阿里云备案**：使用`xxxxxxx.n1.apifox.cn`

- **域名已在腾讯云备案**：使用`xxxxxxx.n2.apifox.cn`

- **使用香港服务器节点（无需备案，速度略慢）**：使用`xxxxxxx.nx.apifox.cn`

如果你希望快速上线文档站，且没有备案的域名，可选择 Apifox 提供的香港服务器节点，无需备案，仅需配置 CNAME 即可访问。

:::tip[]
CNAME 地址请以 Apifox 自定义域名页面中显示的为准，每个项目显示的地址会有所不同。
:::

### 添加 CNAME 记录

添加 CNAME 记录需要在 “域名厂商” 内进行配置，比如在阿里云、腾讯云、新网等厂商中购买的域名。你需要前往对应的管理控制台添加域名解析。


<Steps>
  <Step>
    
    在域名控制台中找到你的 “域名解析” 页面，例如：

    - 阿里云：在控制台页面的左侧，产品与服务栏中选择**域名**。

    - 腾讯云：在控制台的云产品中，搜索并选择**云解析**。

    - DNSPOD：在控制台页面左侧，选择**域名**。

    其他域名厂商请参考该产品文档的说明或咨询该产品的售后。
      
  </Step>
  <Step>
    在域名产品的列表中找到对应的 “主域名”，点击域名后面的 “解析设置” 或 “解析” ，进入解析设置页。
  </Step>
  <Step>
    选择 “添加记录”，依次填写**主机记录**、**记录类型**以及**记录值**，其它可设为默认值。

<Background>
<img src="https://api.apifox.com/api/v1/projects/5097254/resources/484908/image-preview" alt="添加 CNAME 记录" width="560px" />
</Background>
      
| 参数说明 | 填写说明 | 备注                   |
| -------- | ---------------------------------------------------------------------------------------------------------------------------- | -------------------------- |
| 记录类型 | 选择 CNAME 类型  |  <div style="width: 80px">必选</div>   |
| <div style="width: 70px">主机记录</div> | 一般是指子域名的前缀 （如需创建子域名为 `docs.example.com` ，主机记录输入 **`docs`**；如需实现 `example.com`，主机记录输入 **`@`** ) | 子域名前缀   |
| 解析线路 | 保持默认 | 	可按需调整 |
| 记录值   | 粘贴从 Apifox 获取的 CNAME 地址| 必选|
| TTL      | 保持默认| 	可按需调整 |

  </Step>
</Steps>



### 启用 HTTPS

Apifox 支持为自定义域名开启 HTTPS 加密访问，保障安全与可信度。

在「自定义域名」设置页面中开启 **启用 HTTPS**，你也可以开启 **始终使用 HTTPS**，避免用户通过 HTTP 访问文档。


### SSL 证书

启用 HTTPS 后，你可以选择：

- **使用 Apifox 自动生成的证书**（推荐）

- **手动填写证书内容和私钥**（可使用第三方机构如 [Let's Encrypt](https://letsencrypt.org/) 提供的证书）


<Background>
<img src="https://api.apifox.com/api/v1/projects/5097254/resources/484915/image-preview" width="560px" />
</Background>

### 验证域名可访问性

当你配置完自定义域名，并完成 CNAME 和 HTTPS 设置后，点击 “保存” 即可。Apifox 会自动校验你的 CNAME 配置是否正确。

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/543827/image-preview)
</Background>

你可以通过访问自己的域名（如 `https://docs.example.com`）来验证文档是否已经可以正常访问。如果页面已正常显示文档内容，说明配置成功，即使 Apifox 界面仍显示“待校验”，也可以忽略提示，刷新项目页面后状态将更新。

如果访问失败，请检查以下几点：

- 是否正确设置了 CNAME，并等待了解析生效（通常 5~10 分钟）；

- 是否选择了与你备案情况匹配的 CNAME 地址；

- 是否在域名平台中启用了 HTTPS（如使用了自有证书）；

- 是否使用了受信任的 SSL 证书（浏览器是否提示“连接不安全”）；

- 是否开启了“启用 HTTPS”和“强制使用 HTTPS”等配置项。

### 常见问题

<Accordion title="自定义域名一直显示未生效怎么办？" defaultOpen>
  首先，配置 CNAME 一般需要 10 分钟左右才生效，请耐心等待，也可以刷新一下项目。如果长时间未生效，可能是以下原因导致：

  - CNAME 配置不成功，请前往域名管理界面，确认 CNAME 是否正确配置。
  - 域名尚未完成备案。
</Accordion>

<Accordion title="如何检查 CNAME 配置是否正确？" defaultOpen={false}>
- Linux 使用 `dig` 命令检查域名解析是否正常。  
```shell
dig [你的自定义域名]
```
    
- Windows 系统需要安装 `dig` 命令，参考此文档安装：[安装 dig 命令](https://bbs.sangfor.com.cn/forum.php?mod=viewthread&tid=139699)  

命令运行后，查看 `ANSWER SECTION` 部分是否与 Apifox 上的信息配置一致，例如：  

<Background>
<img src="https://api.apifox.com/api/v1/projects/5097254/resources/494322/image-preview" width="460px" />
</Background>

国内服务器都需要备案 *（香港服务器除外）*，可在 [ICP 备案查询](https://beian.miit.gov.cn/#/Integrated/recordQuery) 查询域名是否备案。  

</Accordion>


<Accordion title="Apifox 自定义域名的 SSL 证书生成失败怎么办？" defaultOpen={false}>
    
- **情况一：** 证书生成失败，请检查 CNAME 配置是否正确。 
- **情况二：** 证书生成成功，但域名无法访问，可能是你的电脑配置问题。建议换一台电脑或使用手机测试，若问题仍然存在，请联系[技术支持](https://docs.apifox.com/contact-us.md)解决。

**无法访问的电脑配置检查：**  
1. 确认电脑时钟设置是否正确。  
2. 访问 [ISRG Root X1 证书验证](https://valid-isrgrootx1.letsencrypt.org/) 确认设备是否信任 ISRG Root X1 证书。

</Accordion>


## 自有服务器中转方式

> Apifox 版本号需 ≥ 2.2.19。

除了使用 CNAME 方式以外，Apifox 还支持使用自有服务器中转功能来实现自定义域名访问 API 在线文档。

- 使用 Nginx 等 Web 服务器做简单配置即可实现，即 `Web` 服务器代理。
- 使用阿里云、腾讯云、七牛云等云厂商的全站加速服务 (DCDN) 。即全站加速服务将您的域名代理到指定的地址且正确设置请求头后即可成功访问域名从而展现您的项目文档。

<br />

### Web 服务器

你可以使用 `Nginx` 来代理您的服务从而使用自有服务器中转功能。

- 在 `Nginx` 中可以使用 `proxy_pass` 命令，这个命令用于将请求转发到其他服务器。

- 在 `Nginx` 中可以使用 `proxy_set_header` 命令，这个命令用于设置代理服务器发送给上游服务器的请求头。

例如，你可以在 `Nginx` 配置文件中添加如下内容来进行简单配置。

```nginx
server {
    ...
    location / {
        proxy_pass  http://{docsSiteId}.n3.apifox.cn;
        proxy_set_header X-Apifox-Docs-Site-ID {docsSiteId};
        proxy_set_header Original-Host docs.example.com;
        ...
    }
    ...
}
```

:::tip[]
`{docsSiteId}` 为你的文档站 `id`，即自定义域名面板显示的 `Docs Site ID`，请确保填写正确的 `id`。

<Background>
<img src="https://api.apifox.com/api/v1/projects/5097254/resources/525414/image-preview" style="width: 460px;"/>
</Background>
:::

### 全站加速（CDN）服务

你可以使用阿里云、腾讯云、七牛云等云厂商的全站加速服务（DCDN）配置源站和自定义回源 `HTTP` 头从而来使用自有服务器中转功能。

- 在全站加速服务中可以添加你的加速域名，并执行以下三个操作：
  1. 配置源站信息，选择源站类型为域名且正确配置域名为：`{docsSiteId}.n3.apifox.cn`
  2. 回源 HOST 配置选择或设置为加速域名，即您的 `自定义域名`
  3. 在回源配置中添加自定义回源 `HTTP` 请求头：
  - 参数：`X-Apifox-Docs-Site-ID`
  - 取值：`{docsSiteId}`

:::tip[]
`{docsSiteId}` 为你的文档站 `id`，即自定义域名面板显示的 `Docs Site ID`，请确保填写正确的 `id`。
:::

### 阿里云

如下为配置示例，实际参数需要改为软件内对应的值：

1. 添加域名。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/608329/image-preview)
</Background>


2. 回源 HOST 配置。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/484917/image-preview)
</Background>


3. 设置回源 HTTP 请求头。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/608377/image-preview)
</Background>


### 腾讯云

如下为配置示例，实际参数需要改为软件内对应的值：

1. 添加域名和回源 HOST 配置。


<Background>
 
![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/608420/image-preview)
</Background>


2. 参考[设置回源 HTTP 请求头](https://cloud.tencent.com/document/product/228/45078)，添加 `X-Apifox-Docs-Site-ID` 请求头。

### 七牛云

如下为配置示例，实际参数需要改为软件内对应的值：

1. 添加域名和回源 HOST 配置。


<Background>
<img src="https://api.apifox.com/api/v1/projects/5097254/resources/608421/image-preview" width="560px" />

</Background>


2. 设置回源 HTTP 请求头，需要通过[七牛云控制台](https://portal.qiniu.com/cdn/domain)提交工单的方式设置回源 HTTP 请求头。

## 嵌入至自有域名的子目录

> Apifox 版本号需 ≥ 2.5.24。

Apifox 支持使用自有服务器的中转功能，可以将 API 在线文档嵌入至自定义域名的子目录。

在 **“自定义域名”** 选项页内，填写自定义域名 *(如：`example.com`)*。然后点击 **“自有服务器中转”**，启用 **“使用子目录”**，并输入子目录名称 *(如：`api-docs`)*。



<Background>
<img src="https://api.apifox.com/api/v1/projects/5097254/resources/488875/image-preview" alt="嵌入至自有域名的子目录" width="560px" />
</Background>


接下来，你需要修改自有 Web 服务器 *（例如：Nginx）* 的配置文件，参考以下内容进行配置：

- 在 `Nginx` 中可以使用 `proxy_pass` 命令，这个命令用于将请求转发到其他服务器。
- 在 `Nginx` 中可以使用 `proxy_set_header` 命令，这个命令用于设置代理服务器发送给上游服务器的请求头。

Nginx 配置文件示例代码：

```nginx
server {
    ...
    location /api-docs/ {
        proxy_pass  http://{docsSiteId}.n3.apifox.cn/;
        proxy_set_header X-Apifox-Docs-Site-ID {docsSiteId};
        proxy_set_header Original-Host docs.example.com;
        ...
    }
    ...
}
```

:::tip[]
- `/api-docs` 为你的自定义域名下的子目录，请根据你的文档地址自行修改，尾部一定要添加斜杠 `/`，见上述示例代码。
- `http://{docsSiteId}.n3.apifox.cn` 尾部也需添加斜杠 `/`，见上述示例代码。
- `{docsSiteId}` 为你的文档站 `id`，即自定义域名面板显示的 `Docs Site ID`，请确保填写正确的 `id`。
:::


