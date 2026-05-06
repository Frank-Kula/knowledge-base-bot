# 请求代理 Agent（Proxy）

你可以在具有合适网络环境的机器上部署 Apifox 请求代理 Agent，允许通过该 Agent 代理从 Apifox 客户端、Web 端以及外部分享的文档页发起的接口请求，转发至目标接口。

该功能适用于多种场景，包括但不限于：

- **外部接口调试：** 在对外分享接口文档时，你可以指定使用已部署的请求代理 Agent 来解决跨域请求（CORS）问题。

- **内部网络隔离：** 在需要通过内部网络进行接口调试，且无法直接从本地或其他环境发起请求时，代理 Agent 也能帮助处理接口请求。

- **多环境测试：** 在不同的开发、测试、生产环境中，接口可能有不同的配置或网络要求。请求代理 Agent 可以根据环境差异，帮助统一接口请求的处理方式，减少环境切换时的配置差异问题。

- **跨网络环境调试：** 在不同网络环境之间调试接口时，可能存在网络隔离或防火墙限制，导致无法直接连接到目标接口。通过部署请求代理 Agent，可以跨越这些网络环境限制进行调试。


通过请求代理 Agent，可以应对不同环境和网络要求下的调试需求。



## 准备工作

- 一台服务器，建议 OS 为 Linux
  
- 服务器已安装 [Docker 环境](https://www.docker.com/)，最低版本号需使用 `20.10.0`，推荐 `20.10.13`

## 部署请求代理 Agent

请求代理 Agent 是团队/组织级资源，部署完成后整个团队/组织内的全部项目均可以使用。在 “Apifox 主窗口 -> 团队资源 -> 请求代理 Agent” 页面中，点击新建请求代理 Agent 即可开始向你的团队中部署一个请求代理 Agent。

```javascript
docker pull registry.cn-hangzhou.aliyuncs.com/apifox/apifox-request-proxy-agent && \
docker run --name apifox-request-proxy-agent \
-p 9159:9159 \
-d registry.cn-hangzhou.aliyuncs.com/apifox/apifox-request-proxy-agent
```


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/490005/image-preview)
</Background>


部署时可以使用环境变量来配置基本能力，你可根据你的需求自行选择是否使用。

                
<table>
  <thead>
    <tr>
      <th>
        环境变量
      </th>
      <th>
        描述
      </th>
      <th>
        示例
      </th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>
        SOURCE_IP_WHITELIST
      </td>
      <td>
        允许来源 IP 的列表，用英文逗号分隔。
        <span style="color: gray; font-size: 14px; display: inline-block; width: 270px;">
          因操作系统限制，仅可在 Linux 上使用此变量，并且要同时使用 `--network=host`
        </span>
      </td>
      <td>
        --network=host
        -e SOURCE_IP_WHITELIST=134.34.4.3,123.333.33.0/24
      </td>
    </tr>
    <tr>
      <td>
        SOURCE_IP_BLACKLIST
      </td>
      <td>
        禁用来源 IP 的列表，用英文逗号分隔。
        <span style="color: gray; font-size: 14px;display: inline-block; width: 270px;">
          因操作系统限制，仅可在 Linux 上使用此变量，并且要同时使用 `--network=host`
        </span>
      </td>
      <td>
        --network=host
        -e SOURCE_IP_BLACKLIST=134.34.4.3,123.333.33.0/24
      </td>
    </tr>
    <tr>
      <td>
        DESTINATION_DOMAIN_WHITELIST
      </td>
      <td>
        允许请求目标域名的列表，用英文逗号分隔
      </td>
      <td>
          <span style="display: inline-block; width: 460px;">
        -e DESTINATION_DOMAIN_WHITELIST=xxx.yyy.com,*.yyy.com
          </span>
      </td>
    </tr>
    <tr>
      <td>
        DESTINATION_DOMAIN_BLACKLIST
      </td>
      <td>
        禁用请求目标域名的列表，用英文逗号分隔
      </td>
      <td>
        -e DESTINATION_DOMAIN_BLACKLIST=xxx.yyy.com,*.yyy.com
      </td>
    </tr>
    <tr>
      <td>
        DESTINATION_IP_WHITELIST
      </td>
      <td>
        允许请求目标 IP 的列表，用英文逗号分隔
      </td>
      <td>
        -e DESTINATION_IP_WHITELIST=134.34.4.3,123.333.33.0/24
      </td>
    </tr>
    <tr>
      <td>
        DESTINATION_IP_BLACKLIST
      </td>
      <td>
        禁用请求目标 IP 的列表，用英文逗号分隔
      </td>
      <td>
        -e DESTINATION_IP_BLACKLIST=134.34.4.3,123.333.33.0/24
      </td>
    </tr>
    <tr>
      <td>
        ALLOW_PRIVATE_IP
      </td>
      <td>
        允许请求目标为内网 IP，布尔值，默认为 false
      </td>
      <td>
        -e ALLOW_PRIVATE_IP=false
      </td>
    </tr>
  </tbody>
</table>


:::tip[]
Apifox 请求代理 Agent 是开源的，您可以根据您的场景，对此 Agent 进行二次开发从而满足您的特别需求 *（如：要增加特定的 header 参数等）*。
:::

## 将已部署的请求代理 Agent 添加入 Apifox 中

如果 Apifox 请求代理 Agent 已经在 Docker 上正常运行，则可以回到 Apifox 客户端内将其添加到团队资源中。将 Agent 部署所在服务器的 Host 信息填入之前的弹窗中 *（端口号默认为 `9159`）*，并点击保存，则 Apifox 会自动尝试连接。

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/490007/image-preview)
</Background>



如果连接失败，则会以 Toast 形式告知，并且不允许创建。

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/490009/image-preview)
</Background>


如果连接成功，则会成功在团队中创建这个请求代理 Agent。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/490010/image-preview)
</Background>


部署并在 Apifox 连接到这个请求代理 Agent 并创建成功后，即可在团队中开始使用此请求代理 Agent。

- [在 Apifox 客户端中使用请求代理 Agent 进行调试](https://docs.apifox.com/request-proxy-debugging.md)
- [在接口文档分享页中使用请求代理 Agent 解决跨域（CORS）问题](https://docs.apifox.com/cross-origin-proxy.md)
