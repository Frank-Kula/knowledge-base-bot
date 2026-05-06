# 跨域代理


如果用户想要在发布文档站中调试接口，则很有可能碰到浏览器的[跨域请求（CORS）](https://baike.baidu.com/item/%E8%B7%A8%E6%9D%A5%E6%BA%90%E8%B5%84%E6%BA%90%E5%85%B1%E4%BA%AB?fromModule=lemma_search-box)问题。通过给此 “发布文档站” 设置跨域代理即可帮助解决这个问题。用户从此文档站页面中发起的全部接口请求，都将会通过指定的请求代理 Agent，来代理发起请求。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/489881/image-preview)
</Background>

## 代理类型

可以在跨域代理详情中，根据你的实际场景和使用需求，来设置使用具体某个跨域代理：

- **云端 Agent：** 使用 Apifox 提供的云端请求代理 Agent 来代理从此分享页中发起的接口请求。需要注意这个 Agent 无法访问内网接口。

- **浏览器扩展：** 使用用户在自己浏览器中安装的浏览器扩展作为 Agent 来发起请求。如果用户没有安装浏览器扩展则会在页面引导其安装扩展来发起请求。

- **不使用代理：** 不使用跨域代理，请求将从用户浏览器直接发起到接口。需要注意接口服务端的配置以避免跨域问题。

- **自托管请求代理 Agent：** 使用某个团队中部署的[自托管请求代理 Agent](https://docs.apifox.com/request-proxy-agent.md)来代理从此分享页中发起的接口请求。

## 如何选择代理类型？
- **公网接口**：优先使用云端 Agent
- **内网接口**：选择浏览器扩展 Agent（简单场景）或自托管 Agent（高安全要求）


## 常见问题


<Accordion title="为什么浏览器扩展无法携带 Cookie？" defaultOpen>
浏览器安全策略禁止扩展修改 `Cookie` 等保留字段（[完整列表](https://developer.mozilla.org/zh-CN/docs/Glossary/Forbidden_header_name)）。如需携带 Cookie，建议使用[云端 Agent](https://docs.apifox.com/request-proxy-in-web.md) 或 [Apifox 桌面客户端](https://docs.apifox.com/download.md)。
</Accordion>





## 了解更多

<Card title="网页端中的请求代理" href="https://docs.apifox.com/request-proxy-in-web.md">
</Card>

<Card title="分享文档中的请求代理" href="https://docs.apifox.com/share-document-proxy.md">
</Card>

<Card title="客户端中的请求代理" href="https://docs.apifox.com/client-side-request-proxy.md">
</Card>
