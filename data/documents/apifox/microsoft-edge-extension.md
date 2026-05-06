# Microsoft Edge 浏览器扩展安装

## 安装方法

打开 Microsoft Edge 浏览器，去到 [Microsoft Edge 外接程序](https://microsoftedge.microsoft.com/addons/detail/apifox-browser-extension/haklpcemfcccpoeaibpbgacinnbfafbl)，你可以直接在 Microsoft 里获取该外接扩展。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/488647/image-preview)
</Background>

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


## 权限设置

部分浏览器版本，需要手动修改相关权限，否则会请求失败。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/488648/image-preview)
</Background>



## 常见问题

<Accordion title="为什么我安装不成功?？" defaultOpen>
你需要检测插件与你的浏览器版本是否兼容，可升级 Microsoft Edge 浏览器版本来解决。
</Accordion>

<Accordion title="为什么某些 Header 无法发送？" defaultOpen={false}>
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



