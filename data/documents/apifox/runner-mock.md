# 自托管 Runner Mock


Runner Mock 适用于内网或专有网络需要能够提供 Mock 服务的场景，实际请求发送至 Runner 所在服务器上，然后由 Runner 提供 Mock 服务返回 Mock 结果。



建议团队、项目管理员在部署完成 [Runner](https://docs.apifox.com/universal-runner) 后，按照以下步骤进行操作：

## 1. 配置服务器 host

点开 “团队资源 -> 通用 Runner” 选项，将 Runner 所在服务器的`公网 IP`或`域名`配置到已部署的 Runner 服务的 “服务器 Host” 中。需要注意的是，协议头 *（http/https）* 和端口号 *（默认 4524）* 在配置时都需要携带上。


<Tabs>
  <Tab title="示例一">
   
    ```js
    https://runner.example.com:443
    ```
  </Tab>
  <Tab title="示例二">

    ```js
    http://127.0.0.1:80
    ```
  </Tab>

</Tabs>


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/481068/image-preview)
</Background>


## 2. 检查 Runner Mock 环境

在项目的 “环境管理” 中可以检查是否已经配置了 Runner Mock 环境，如果配置了，则会显示在环境列表中。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/481069/image-preview)
</Background>


## 3. 使用 Runner Mock 环境

在接口请求时，选择环境为新建的 Runner Mock 以发送请求，即可获得从 Runner 服务器返回的 Mock 结果。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/481070/image-preview)
</Background>

## 常见问题


<Accordion title="Runner Mock 是否支持 HTTPS？如何开启？" defaultOpen>
是的，Runner Mock 支持通过 HTTPS 提供服务。但需要注意：

- Runner 本身不内置 HTTPS 证书或自动申请功能；

- 只要你配置的域名本身已启用 HTTPS，并且可正常访问（例如通过 Nginx 等反向代理绑定了证书），就可以直接使用。

✅ 你只需要在 “服务器 Host” 中填写 `https://你的域名:端口`，就可以通过 HTTPS 请求 Runner Mock 服务，无需对 Runner 进行额外配置。例如：
    
<Frame>
![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/516846/image-preview)
</Frame>


</Accordion>


