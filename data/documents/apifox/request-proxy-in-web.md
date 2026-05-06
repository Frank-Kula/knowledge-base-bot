# 网页端中的请求代理

当你在网页端中登录 Apifox，进入项目并对 API 发送请求时，可能会碰到跨域 *（CORS）* 限制。Apifox 提供了多种请求代理 Agent，来帮助用户解决此问题：

<table border="1">
  <thead>
    <tr>
      <th>请求代理 Agent</th>
      <th>描述</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="4"><strong>云端 Agent</strong></td>
      <td>✅ 无需安装</td>
    </tr>
    <tr>
      <td>✅ 支持发送 HTTPS 请求</td>
    </tr>
    <tr>
      <td>❌ 需要连接到 Apifox 云端使用</td>
    </tr>
    <tr>
      <td>❌ 无法访问私有或本地网络环境</td>
    </tr>
    <tr>
      <td rowspan="3"><strong>浏览器扩展</strong></td>
      <td>✅ 本地安装</td>
    </tr>
    <tr>
      <td>✅ 支持发送 HTTPS 请求</td>
    </tr>
    <tr>
      <td>❌ 需要下载 [Apifox 浏览器扩展](https://docs.apifox.com/chrome-extension.md)</td>
    </tr>
    <tr>
      <td rowspan="4"><strong>自托管请求代理 Agent</strong></td>
      <td>✅ 部署于自托管服务器</td>
    </tr>
    <tr>
      <td>✅ 支持发送 HTTPS 请求</td>
    </tr>
    <tr>
      <td>❌ 需要服务器部署</td>
    </tr>
    <tr>
      <td>❌ 受到部署服务器的网络环境限制，可能无法访问本地网络环境</td>
    </tr>
  </tbody>
</table>

你可以在项目页面右下角 “请求代理” 处选择你当前使用哪个请求代理 Agent，默认会选中 “自动”。在自动模式时，如果你安装了浏览器扩展，则会使用浏览器扩展实际发送请求；如果没有，则会使用云端 Agent 实际发送请求。

<Background>

![CleanShot 2025-02-05 at 14.33.14@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/493017/image-preview)
</Background>




