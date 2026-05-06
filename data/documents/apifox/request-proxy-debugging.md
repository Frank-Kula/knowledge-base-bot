# 使用请求代理调试


在 Apifox 内进行接口请求、调试时，可以使用代理的方式对接口实际发起请求，从而避免网络环境原因无法从本地请求到接口等情况。有以下两种方式能够影响在接口调试时，是否使用请求代理。

## 个人请求代理设置

进入一个项目后，在 Apifox 右下角，可以看到请求代理设置。你可以使用以下几种方式来代理你在 Apifox 上发起的接口请求。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/489904/image-preview)
</Background>


当你使用 Apifox 客户端时：

- **使用软件代理：** 从 Apifox 发起的接口请求，使用 [软件设置中的请求代理设置](https://docs.apifox.com/network-proxy.md) 进行代理。注意是在 “接口请求代理配置” 中设置的代理，才会在接口请求时生效。如果软件设置中的 “接口请求代理配置” 选择不使用代理，则接口请求会直接从客户端发送到接口。
  
  
    <Background>

    ![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/489905/image-preview)
    </Background>


- **使用自托管请求代理 Agent （Proxy）：** 从 Apifox 发起的接口请求，使用当前指定的 [自托管请求代理 Agent](https://docs.apifox.com/request-proxy-agent.md) 进行代理。


    <Background>

    ![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/489907/image-preview)
    </Background>


当你使用 Apifox 网页端时：

- **自动选择代理：** Apifox 会根据当前使用的浏览器情况，来自动选择使用浏览器插件 Agent 还是云端 Agent 来代理接口请求。优先会使用浏览器插件 Agent 来代理请求。
  
- **浏览器插件 Agent：** 使用浏览器插件 Agent 来代理接口请求。需要安装[浏览器插件](https://docs.apifox.com/chrome-extension.md)后才可用。
  
- **云端 Agent：** 使用 Apifox 提供的云端请求代理 Agent 来代理接口请求。需要注意这个 Agent 无法访问内网接口。
  
- **使用自托管请求代理 Agent（Proxy）：** 从 Apifox 发起的接口请求，使用当前指定的[自托管请求代理 Agent](https://docs.apifox.com/request-proxy-agent.md)进行代理。



此个人请求代理设置是会保存在云端的，每个项目都会保存针对当前项目的设置，以便下次再调试项目中接口时能够快速使用正确的请求代理设置。


## 不同环境服务下的请求代理设置

进入项目后，可在「环境管理」中，针对不同环境下的服务（前置 URL），统一配置该服务使用的请求代理方式。

一旦服务指定了请求代理，Apifox 中**所有向该服务发起的接口请求**，都会通过对应的代理转发。

该机制适用于**不同服务位于不同网络环境**的场景，例如：

* 内网服务
* 需要特定出口访问的服务
* 依赖代理才能访问的第三方 API

通过在服务层统一配置代理，可以避免每位成员重复、易错地配置个人代理。



### 请求代理的三种方式

在环境服务的「高级设置」中，可为服务选择以下代理方式之一：

* **默认**
  使用当前客户端本地配置的代理设置（右下角的请求代理）。

* **自部署 Proxy**
  通过自部署的 Apifox Proxy 服务转发请求，适合内网访问、统一出口控制或对请求进行修改的场景。

* **通用网络代理**
  使用标准网络代理（如 HTTP / SOCKS5）转发请求，适合已有通用代理基础设施、或需要快速接入代理访问的场景。
  
 

> 代理方式一旦在服务中指定，对该服务下的所有接口请求生效。

<Background>
 
![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/608846/image-preview)
</Background>


### 代理优先级说明


- **“服务” 级代理优先于个人代理设置**
    如果服务中指定了请求代理，则该设置会覆盖成员本地的请求代理配置。即使成员在右下角将请求代理设置为「默认」，向该服务发起请求时，仍会使用服务中配置的代理。

- **仅对端内调试生效**
    服务中配置的请求代理，仅作用于 Apifox 客户端内发起的接口请求。通过分享文档或公开文档站进行调试时，仍会使用分享中配置的「[跨域代理](https://docs.apifox.com/cross-origin-proxy.md)」来实际转发请求。



### 快速查看与管理代理配置

也可以在右下角的请求代理设置中，快速查看当前项目中各环境服务所使用的请求代理配置，便于统一检查与调整。

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/489909/image-preview) 
</Background>


### 配置范围说明

环境服务中指定的请求代理设置：

* 保存在云端
* 对项目内所有成员生效
* 属于**项目级共享配置**

适合用于团队协作中统一管理网络访问方式。

