# 分享文档中的请求代理


当你将项目中的文档使用自定义分享，或公开文档的方式发布给第三方用户使用时，可以在发布设置中选择此发布出去的在线文档，使用何种请求代理。跟网页端需要使用请求代理的原因一致，分享文档中选择使用代理的原因也是为了避免跨域 *（CORS）* 限制。有以下几种模式可以选择：

<table border="1">
  <thead>
    <tr>
      <th>请求代理 Agent</th>
      <th>描述</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>云端 Agent</strong></td>
      <td>使用 Apifox 提供的云端请求代理 Agent 来代理从此分享页中发起的接口请求。需要注意这个 Agent 无法访问内网接口。</td>
    </tr>
    <tr>
      <td><strong>浏览器扩展</strong></td>
      <td>使用用户在自己浏览器中安装的[浏览器扩展](https://docs.apifox.com/chrome-extension.md)作为 Agent 来发起请求。如果用户没有安装浏览器扩展则会在页面引导其安装扩展来发起请求。</td>
    </tr>
    <tr>
      <td><strong>不使用代理</strong></td>
      <td>不使用跨域代理，请求将从用户浏览器直接发起到接口。需要注意接口服务端的配置以避免跨域问题。</td>
    </tr>
    <tr>
      <td><strong>自托管请求代理 Agent</strong></td>
      <td>使用某个团队中部署的[自托管请求代理 Agent](https://docs.apifox.com/request-proxy-agent.md) 来代理从此分享页中发起的接口请求。</td>
    </tr>
  </tbody>
</table>

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/489881/image-preview)
</Background>

