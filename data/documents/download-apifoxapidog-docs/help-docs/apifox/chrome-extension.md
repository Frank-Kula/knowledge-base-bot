# Chrome 浏览器扩展安装

## 安装方法

### 方式一：Chrome 应用商店安装

<Steps>
  <Step>
    访问 [Chrome 应用商店页面](https://chrome.google.com/webstore/detail/apifox-browser-extension/eggdlmopfankeonchoflhfoglaakobma?hl=zh-CN)
     
  </Step>
  <Step>
    点击 `添加至 Chrome` 即可
    <Background>

    ![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/546428/image-preview)
    </Background>

  </Step>
</Steps>


### 方式二：本地安装


<Steps>
  <Step title="下载扩展包">
      
<Columns>
  <Column>
    
<Card title="" href="https://file-assets.apifox.com/download/apifox-browser-extension/Apifox-browser-extension.zip">
  <Icon icon="material-outline-cloud_download" size={20}/> 点击下载 Apifox 浏览器扩展 ZIP
</Card>

  </Column>
    <Column>
    
  </Column>

</Columns>
  </Step>
  <Step title="加载扩展">
   - 解压 ZIP 文件
   - 谷歌浏览器地址栏访问<CopyToClipboard>`chrome://extensions`</CopyToClipboard>，开启右上角 **`开发者模式`**
   - 点击 **`加载未打包的扩展程序`**，选择解压后的文件夹即可
      
<Background>
![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/546418/image-preview)
</Background>

<!--
   - 完成后需将 **`开发者模式`** 关闭

<Background>
![安装流程示意图](https://api.apifox.com/api/v1/projects/5097254/resources/488645/image-preview)
</Background>
-->
  </Step>
</Steps>


## 限制说明

受浏览器安全策略限制，以下情况**无法通过浏览器扩展实现**：
- **部分请求头无法修改**  
  像`Cookie`、`Host`、`Origin`、`Content-Length`  这类浏览器保留的请求头，不允许扩展修改或添加（[完整列表](https://developer.mozilla.org/zh-CN/docs/Glossary/Forbidden_header_name)）。
  
- **Cookie 无法自由传递**  
  - 如果跨域请求没有正确配置 CORS，浏览器会自动拦截 Cookie。
  - 浏览器扩展无法直接读取或操作 Cookie （包括发送请求时自动携带 Cookie）
  
- **某些请求受限**  
  比如 `GET` 和 `HEAD` 请求方法不能携带请求体（Body），这会影响一些本地调用或数据库调试的场景。

**替代的解决方案**：  

- 使用 [Apifox 桌面客户端](https://docs.apifox.com/download.md)，可绕过浏览器限制，完整支持上述功能。  
- 启用 [云端 Agent](https://docs.apifox.com/request-proxy-in-web.md)（绕过浏览器限制）



## 权限配置（部分场景需操作）

若请求失败，需手动允许扩展访问以下权限：  
1. 进入 `chrome://extensions`，找到 Apifox 扩展
2. 点击 **`详情`**，在 **`权限`** 选项卡中分别填入：

```js
http://apifox.com/*
http://app.apifox.com/*
https://apifox.com/*
https://app.apifox.com/*
```

<Background>

![权限设置示意图](https://api.apifox.com/api/v1/projects/5097254/resources/488646/image-preview)
</Background>


---

## 常见问题



<Accordion title="为什么某些 Header 无法发送？" defaultOpen>
浏览器强制过滤保留字段（如 `Cookie`），需改用 [Apifox 桌面客户端](https://docs.apifox.com/download.md) 或配置 [云端 Agent](https://docs.apifox.com/request-proxy-in-web.md)。
</Accordion>


<Accordion title="跨域请求返回 403/Forbidden？" defaultOpen={false}>
1. 检查是否是服务器明确拒绝请求（如认证失败、IP 限制等）
    
2. 请配置[跨域代理](https://docs.apifox.com/cross-origin-proxy.md)

3. 检查后端是否配置 CORS 响应头，例如：
```http
Access-Control-Allow-Origin: https://your-domain.com
Access-Control-Allow-Credentials: true
```
</Accordion>

<Accordion title="GET 请求的 Body 被自动删除？" defaultOpen={false}>
浏览器规范禁止 `GET`/`HEAD` 携带 Body，建议改用 `POST` 或使用桌面客户端调试。
</Accordion>


<Accordion title="需要调用本地代码/数据库？" defaultOpen={false}>
浏览器沙箱环境无法支持，需使用 [Apifox 桌面客户端](https://docs.apifox.com/download.md)。
</Accordion>


## 了解更多


<Card title="CORS 代理配置指南" href="https://docs.apifox.com/cross-origin-proxy.md">
</Card>

<Card title="网页端中的请求代理" href="https://docs.apifox.com/request-proxy-in-web.md">
</Card>

<Card title="分享文档中的请求代理" href="https://docs.apifox.com/share-document-proxy.md">
</Card>

<Card title="客户端中的请求代理" href="https://docs.apifox.com/client-side-request-proxy.md">
</Card>


