# 客户端中的请求代理


在客户端中可以完全避免跨域限制，但是我们仍然提供了选择请求代理的功能，用以帮助解决一些请求本机网络环境无法访问的接口等场景下的需求。有两种请求代理可以选择：

<table border="1">
  <thead>
    <tr>
      <th>请求代理 Agent</th>
      <th>描述</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>使用软件代理</strong></td>
      <td>从 Apifox 发起的接口请求，使用[软件设置中的请求代理设置](https://docs.apifox.com/5722987m0#接口请求代理配置)进行代理。注意是在“接口请求代理配置”中设置的代理，才会在接口请求时生效。如果软件设置中的“接口请求代理配置”选择不使用代理，则接口请求会直接从客户端发送到接口。</td>
    </tr>
    <tr>
      <td><strong>自托管请求代理 Agent</strong></td>
      <td>从 Apifox 发起的接口请求，使用当前指定的[自托管请求代理 Agent](https://docs.apifox.com/request-proxy-agent.md) 进行代理。</td>
    </tr>
  </tbody>
</table>

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/493018/image-preview)
</Background>


:::tip[]
如果在项目内给[某个环境下的服务 *（前置 URL）* 特别指定了自托管请求代理 Agent](https://docs.apifox.com/5830401m0#不同环境服务下的请求代理设置)，则从 Apifox 网页端、客户端发送给此服务内的接口请求，都将优先使用此处指定的请求代理来实际发送请求，而非个人在右下角设置的请求代理。
:::
