# 通用 Runner


Apifox 通用 Runner 可以理解为是一个自动化程序，可以托管在独立服务器上。它能够执行 Apifox 内的`自动化测试定时任务`、`定时导入接口文档`、`返回 Mock 响应结果`等工作。

## 准备工作

- 宿主机（服务器或本地电脑）需已安装 [Docker 环境](https://www.docker.com/)
- Docker 最低版本需使用 `20.10.0`，推荐 `20.10.13`


## 快速上手

本章节将为你介绍如何在服务器上部署通用 Runner。

### 1. 部署通用 Runner

前往 Apifox 的“团队资源”页，点击“部署通用 Runner”按钮。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/485379/image-preview)
</Background>


### 2. 获取部署 Runner 命令

点击部署通用 Runner 按钮后，在弹出框中复制部署通用 Runner 的命令，你可以根据需要定义命令，支持自定义服务器 OS、暴露端口、挂载数据目录等。以下是对这些设置的详细说明：


1. **服务器 OS**：指定了 Docker 容器运行的操作系统。包括 Linux、macOS 和 Windows，选择正确的操作系统是确保 Docker 容器能够正确运行的关键。
2. **Docker 镜像**：提供了三种版本，分别是通用版、精简版和自定义版本。若你的「自定义脚本」需要调用外部程序，请根据不同版本所包含的语言环境选择合适的镜像进行安装。

   - **通用版**：包含 Runner 的所有功能，并内置以下外部程序的语言环境：Node.js 18、Java 21、Python 3、PHP 8。
   - **精简版**：包含 Runner 的所有功能，仅内置 Node.js 18 语言环境。
   - **自定义**：包含 Runner 的所有功能，并支持自定义外部程序的语言环境。你可以通过创建自己的 Dockerfile，根据需求添加或移除相关环境。

3. **暴露端口**：Docker 容器默认不会将内部端口暴露给外部访问。通过 `-p` 参数，你可以将容器内部的端口映射到宿主机的端口上，使得外部可以访问容器提供的服务。例如，`-p 80:4524`表示将容器内部的 4524 端口映射到宿主机的 80 端口。
4. **挂载数据目录**：使用`-v`参数可以将宿主机的目录挂载到容器内部，这样容器就可以访问和操作宿主机上的文件（数据库配置、外部程序等）。例如，`-v "/opt/runner":/opt/runner`表示将宿主机的`/opt/runner`目录挂载到容器的`/opt/runner`目录。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/485380/image-preview)
</Background>


:::tip[]
部署命令因为包含 token 信息，基于数据安全考量，一个部署命令只会在产品端展示一次。每次点击部署时都会生成新的命令。

**请将此命令**保存在本地，后续 Runner 需要升级时，可以直接使用保存的命令来进行升级。
:::



### 3. 在服务器上部署 Runner

将已复制的部署命令粘贴至服务器的终端上，然后将会自动开始安装 Runner。

:::tip[]

你可以通过环境变量来修改部署 Runner 的属性，使得能够更加匹配你的实际使用场景。阅读 [Runner 运行环境](https://docs.apifox.com/runner-environment.md)了解更多信息。

:::


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/485382/image-preview)
</Background>


安装完成后，终端将会打印出相关信息。如果报错，可以根据报错详情进行故障排除。如果依然无法解决，请[联系我们](https://docs.apifox.com/contact-us.md)并进行反馈。

### 4. 在服务器上查看 Runner 状态

你可以通过 Docker 客户端查看容器的运行状态。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/485383/image-preview)
</Background>


也可以在终端内使用 `docker ps` 命令，查看容器的运行情况。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/485384/image-preview)
</Background>


### 5. 在 Apifox 中查看已部署的通用 Runner

确认服务器上的 Runner 容器部署完成并启用后，返回 Apifox。你可以在 “团队资源 -> 通用 Runner” 页查看到这个 Runner 已部署完成并连接上 Apifox。

> 如果已在服务器上成功部署通用 Runner，但是在 Apifox 客户端中并没有显示，请点击“通用 Runner”右侧的刷新按钮刷新页面后再次查看。

你可以在 Apifox 中对 Runner 进行改名、添加描述以及删除操作，让你的团队成员能够更好的使用这个 Runner；也可以停用/重启 Runner。已暂停的 Runner 将不会再执行指定的相关定时任务，也无法再新创建相关的任务并指定此 Runner 执行。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/485385/image-preview)
</Background>


关于 Runner 的状态信息见下表说明：

<table>
  <thead>
    <tr>
      <th>状态</th>
      <th>说明</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="color: green;">已启动 / Started</td>
      <td>Runner 在服务器的容器中正常启用并与 Apifox 保持通信中，可以处理 Apifox 下发的相关任务。</td>
    </tr>
    <tr>
      <td style="color: red;">已停用 / Stopped</td>
      <td>Runner 在 Apifox 中手动停用，但是在服务器的容器中正常运行并保持通信。此时不会处理 Apifox 下发的各类任务，新的任务也不可指定停用的 Runner 执行。可以在 Apifox 中手动启用来让此 Runner 重新恢复已启动状态。</td>
    </tr>
    <tr>
      <td style="color: gray;">已离线 / Offline</td>
      <td>Runner 与 Apifox 通信中断，无法处理 Apifox 下发的任务。可能原因为 Runner 容器已在服务器中停止运行，服务器与 Apifox 服务端通信异常等。此时可以通过恢复 Runner 容器运行并确保与 Apifox 通信没有问题，来让此 Runner 重新恢复已启动状态。</td>
    </tr>
  </tbody>
</table>

你可以在一个团队中部署多个通用 Runner，团队成员在创建需要使用自托管 Runner 的任务时，就可以从多个 Runner 中选择一个来执行。

## 服务器 Host 配置

填写服务器地址以让 Apifox 实现自托管 Mock、Runner 请求等功能，详细配置请参考[自托管 Runner Mock](https://docs.apifox.com/runner-mock.md) 模块。

## 在 Runner 中保存文件

使用 Runner 执行接口请求、运行测试场景、定时任务等任务时，可能会需要一些本地文件提供数据来支持任务执行。例如：

- 在自定义脚本中调用其它编程语言
- 在前后置操作中有用到数据库连接
- 发起请求时需要使用 SSL 证书等

此时可将需要使用的文件保存在 Docker 容器中的指定目录下。当 Runner 在执行相关任务时就会根据设定的任务需求在指定目录下读取文件内容，确保任务完成。


可以按照下表将对应格式与内容的文件放到指定目录下进行使用：

| 使用内容                                                                                     | 示例目录路径或文件名                                  |
| -------------------------------------------------------------------------------------------- | ----------------------------------------------------- |
| [其它编程语言](https://docs.apifox.com/call-external-programs.md) | `/opt/apifox/runner/external-programs/`                |
| [数据库](https://docs.apifox.com/database.md)连接配置文件           | `/opt/apifox/runner/database/database-connections.json` |
| [SSL 证书](https://en.wikipedia.org/wiki/Public_key_certificate)列表文件                     | `/opt/apifox/runner/ssl/ssl-client-cert-list.json`      |

示例路径中， `/opt/apifox/runner` 为默认挂载目录，可在部署界面或容器内使用 `-v` 命令更改。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/485386/image-preview)
</Background>


以下是数据库连接配置文件的内容示例：

```json
{
  "19731": {
    "configs": {
      "default": {
        "username": "accountname",
        "password": "123456",
        "host": "192.168.0.0"
      }
    },
    "id": 19731,
    "name": "Database Name",
    "type": "mysql",
    "projectId": 1320441,
    "description": "Dummy data.",
    "createdAt": "2022-09-27T07:51:09.000Z",
    "updatedAt": "2024-05-09T11:38:07.000Z",
    "deletedAt": null
  }
}
```

:::tip[]
- 建议使用云端数据库连接配置来让 Runner 中运行带数据库连接的测试场景更高效。
- 你可以参考[CLI 命令选项](https://docs.apifox.com/cli-command-options.md)查看从 Apifox 客户端中导出配置文件的方法。

:::


SSL 证书列表文件的内容示例：

```json
[
  {
    "name": "domain1",
    "matches": ["https://test.domain1.com/*", "https://www.domain1/*"],
    "key": {"src": "./client.domain1.key"},
    "cert": {"src": "./client.domain1.crt"},
    "passphrase": "changeme"
  },
  {
    "name": "domain2",
    "matches": ["https://domain2.com/*"],
    "key": {"src": "./client.domain2.key"},
    "cert": {"src": "./client.domain2.crt"},
    "passphrase": "changeme"
  }
]
```

## 升级&重新部署 Runner

当我们发布了 Runner 的更新版本，你可以在客户端 Runner 界面上，看到有升级提示 icon。点击即可进行 Runner 的升级，用来安装并使用 Apifox 提供的新版本 Runner。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/485387/image-preview)
</Background>


点击升级，会提示要停止现有正在运行的 Runner 容器。注意：容器停止后，定时任务以及在客户端下发到此 Runner 的任务也不再会被执行。


<Background>
<img src="https://api.apifox.com/api/v1/projects/5097254/resources/485388/image-preview" alt="停止 Runner 容器" width="460px" />
</Background>



点击确认后，Apifox 会自动将 Runner 容器停用，并且在界面上弹出新 Runner 的部署命令。按照第一次部署的流程重新再操作部署一次 Runner。部署成功后，即可以使用到最新版的 Runner。客户端内已配置的定时任务不会因为 Runner 升级而需要重新指定 Runner。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/485389/image-preview)
</Background>


当 Runner 发生问题，并且在 Q&A 中未找到类似问题的说明或者按照说明并没有解决问题，可以重新部署 Runner 来尝试解决问题。在某个 Runner 的更多操作中，点击“重新部署”即可。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/485390/image-preview)
</Background>


后续操作流程与上述升级 Runner 基本一致，请注意重新部署 Runner 也需要停止 Runner 容器的运行。



## 常见问题


<Accordion title="发生问题了，需要查询 Runner 日志用以定位？" defaultOpen>
1. 使用 `docker ps` 命令找到出问题的 Runner 信息；
2. 使用 Runner 信息和以下命令来获取到有效日志从而定位问题：
  ```bash
  # 查看容器ID为 abc123 的最近100行日志，推荐
  docker logs --tail 100 abc123

  # 查看过去5分钟内的日志
  docker logs --since 5m abc123

  # 查看某个时间点前5分钟的日志
  docker logs --until 2023-10-01T00:00:00 abc123
  docker logs --until 5m abc123

  # 查看容器ID为 abc123 的容器日志，数据可能很多，不建议
  docker logs abc123
  ```
</Accordion>


<Accordion title="Runner 挂掉/掉线/无法执行任务了怎么办？" defaultOpen={false}>
1. **首先需要找到相关信息用以定位问题：**
   
-  a. 相关操作信息 *（昨天还好，今天早上定时任务不执行了 / 我看到掉线了 / 运行不了我下发的任务）*；

-  b. 打开开发者工具 *（Windows `alt+7+8`，Mac `option+command+i`）*，下发一个测试场景运行任务到有问题 Runner，然后提供接口信息；

-  c. 查询 Runner 日志 *（方法见上一个问题）*。

2. **解决问题：**
   
-  a. 如果从上述信息自己已发现问题所在，确认非 Apifox bug 导致，可按照问题原因自行解决；如果是 Runner 相关的问题原因，**可尝试重新部署**；

-  b. 如果从上述信息看不出什么原因，可以通过 Apifox 交流群进行反馈。

</Accordion>


<Accordion title="Runner 跑完定时任务之后，设置的通知渠道没有按预期收到通知？" defaultOpen={false}>
1. **确认定时任务有无实际执行完成：**
   
-  a. 查看端内此定时任务有无按预期执行完成的报告；

-  b. 查询 Runner 日志（方法见上一个问题）。

2. **如果定时任务执行正常，Runner 日志看起来也正常，则确认通知配置没有问题：**
  
-  a. 查看通知配置是否已保存在定时任务中了；

-  b. 查看定时任务中配置的条件、通知对象是否正常；

-  c. 尝试手动触发任务立即执行，看看结果怎样。

</Accordion>


<Accordion title="Runner 报错信息：No runner privilege，该怎么处理？" defaultOpen={false}>

有两种可能的问题原因：

1. 在点击部署生成命令后，又关闭弹窗并重新点击了部署导致生成了新的 token 从而导致复制去运行的命令失效。解决方案：
   
-  a. 在左上角点击其它团队，然后再切换回当前需要部署 runner 的团队；

-  b. 重新点击生成命令，复制后运行，**并确保运行完成前不再点击部署生成新的命令**。

2. 使用变量 teamId 导致的 id 数据异常。这是个 bug，目前最新版已修复。如果仍然碰到的话，解决方案：
   
- a. 在左上角点击其它团队，然后再切换回当前需要部署 runner 的团队；

- b. 重新点击生成命令，复制后运行，**并确保运行完成前不再点击部署生成新的命令**。
</Accordion>

<Accordion title="如何在服务器实例中删除已安装的 Runner？" defaultOpen={false}>

首先需要删除容器，命令如下：

1. 查看容器：`docker ps -a`
2. 停止容器：`docker stop <container_id>`
3. 删除容器：`docker rm <container_id>`
    
![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/493167/image-preview)
    
然后删除镜像，命令如下：

1. 查看镜像：`docker images`
2. 删除镜像：`docker rmi <image_id>`

    
![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/493168/image-preview)
    
这样，就把部署在服务器实例中的 Runner 删除干净了。
</Accordion>


