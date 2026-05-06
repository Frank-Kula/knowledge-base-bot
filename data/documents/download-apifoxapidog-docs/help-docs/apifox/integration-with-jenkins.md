# 与 Jenkins 集成


## 安装 Jenkins

Jenkins 是一款自动化构建工具，可以帮助开发人员在软件开发过程中自动化构建、测试和部署应用程序。关于 Jenkins 的安装方法，可以参考 [Jenkins 官方文档](https://www.jenkins.io/download/)，里面有各个系统的详细安装教程。


以下是 Linux 系统中的安装示例：

1. 添加 Jenkins GPG 公钥：

```
wget -q -O - https://pkg.jenkins.io/debian/jenkins.io.key | sudo apt-key add -
```

2. 将 Jenkins 源添加到 APT 软件源列表中：

```
sudo sh -c 'echo deb http://pkg.jenkins.io/debian-stable binary/ > /etc/apt/sources.list.d/jenkins.list'
```

3. 更新 APT 软件包列表：

```
sudo apt-get update
```

4. 安装 Jenkins：

```
sudo apt-get install jenkins
```

5. 启动 Jenkins 服务：

```
sudo systemctl start jenkins
```

<br />

安装完成后在 Web 浏览器中输入 `http://localhost:8080` 或 `http://{你的公网IP}:8080` 来访问 Jenkins 控制台。控制台提供了 Web 界面以便你管理和配置 Jenkins 服务。

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/482781/image-preview)

<br />

如需了解更多有关于 Jenkins 的说明，请[查看 Jenkins 官网](https://www.jenkins.io/download/)。

## 配置 NodeJS 环境

运行 Apifox CLI 前需确保 Node.js 版本号 `>= v16`，因此需要先在 Jenkins 环境中配置 NodeJS 依赖。

:::tip[]
更具体的操作步骤请参考这篇最佳实践：[如何将 Apifox 的自动化测试与 Jenkins 集成？](https://apifox.com/blog/integration-with-jenkins)
:::

1、打开 Jenkins 插件管理中找到 NodeJS 插件，安装并重启。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/482783/image-preview)
</Background>


2、在全局工具配置中新建 NodeJS，填写 NodeJS 别名（比如 `nodejs18`）、版本号 *（需 `>= v16`）* 和包名 `apifox-cli`。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/482784/image-preview)
</Background>


若 Jenkins 宿主机已经安装好 Apifox-CLI，希望直接在 Node 环境运行任务，那么可以参考下图的 Node 配置并填写宿主机的 Node 路径。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/482785/image-preview)
</Background>




你可以通过以下两种方式在 Jenkins 中触发 Apifox 自动化测试。

1. 在可视化流水线中添加配置 *（Freestyle Project）*
2. 将嵌入式代码集成至流水线 *（Pipeline）*


## 运行 CLI 命令

### 可视化配置流水线

打开 Apifox，在持续集成详情页中获取 CLI 命令。若 Jenkins 环境具备联网条件，可以选择使用「实时运行在线数据」命令；如果不具备联网条件，那么需要先导出 CLI 的 json 数据文件至环境中，再通过 CLI 执行。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/482786/image-preview)
</Background>


在项目配置页面，找到 “构建环境 *（Build Environment）*” 选项，勾选 “Provide Node & npm bin/ folder to PATH”，并选择你在 “全局工具配置 *（Tools）*” 中设置的 NodeJS 版本 *（如 `nodejs18`）*。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/482788/image-preview)
</Background>


构建环境设置好以后，找到 “构建步骤（Build Steps）” 选项，点击 “添加构建步骤（Add build step）”，选择 “Execute Shell” *（如果是 Windows 系统，选择 “Execute Windows Batch Command”）*。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/482789/image-preview)
</Background>


在 “命令” 输入框中粘贴 Apifox CLI 命令并保存。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/482790/image-preview)
</Background>


在项目中点击 “Build Now（立即构建）” 即可运行。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/482791/image-preview)
</Background>


<br />

### 将嵌入式代码集成至流水线

轻点「CI/CD」 Tab 页并获取嵌入代码，将它粘贴至 Jenkins 的配置文件中。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/482792/image-preview)
</Background>


将代码直接粘贴至 Jenkins 流水线配置中，即可嵌入至已有的持续集成工作流。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/482793/image-preview)
</Background>


这里的`nodejs18`就是上文中设置的 NodeJS 别名，请填写你的实际别名。并且，请确保在代码中将变量`$APIFOX_ACCESS_TOKEN`替换为你实际可用的 Access Token。你也可以在 Jenkins 的「Dashboard -> Manage Jenkins -> System」中添加一个名为`APIFOX_ACCESS_TOKEN`的环境变量，并将其值设置为你的 Access Token。这样，在执行流水线时，系统将能够读取到你的 Access Token。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/482795/image-preview)
</Background>


上述的代码也可以简化成下面这样的，把安装 Apifox CLI 的脚本去掉，这样就不需要每次执行构建任务时都安装一遍`apifox-cli`，从而减少构建时间和资源消耗。这是因为预先在 “全局工具配置 *（Tools）*” 中设置了 NodeJS 和全局 npm 包 *（也就是 apifox-cli）*，它确保了在构建过程中可以直接使用已安装的工具。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/482797/image-preview)
</Background>


在项目中点击 “Build Now *（立即构建）*” 即可运行。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/482798/image-preview)
</Background>




## 常见问题


<Accordion title="在 Jenkins 流水线内上传接口文档失败怎么办？" defaultOpen>
1. 确保运行 Jenkins 主机有足够的磁盘空间。
2. 确保 Jenkins 任务的执行用户有足够的权限。
3. 将需要上传的文件拷贝至 Jenkins 主机内的文件地址，并且在 CLI 命令中指定相同的文件地址路径。
</Accordion>

<Accordion title="有文件上传时如何获取文件？" defaultOpen={false}>
可以事先将需要的文件上传到运行 CLI 的机器上 *（也就是运行 Jenkins 所在的宿主机）*，例如这个图像文件：`apifox-xiangmu.jpg`，可将其路径复制下来。

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/482799/image-preview)



然后在 Apifox 的自动化测试里定位到需要上传文件的接口，点击 “批量编辑” 按钮。


![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/482800/image-preview)

将上传到 CLI 机器上的 “文件路径” 填入到格式中 “参数值” 的位置即可，这样在构建时就会自动根据 “文件路径” 获取到实际文件。


![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/482801/image-preview)

除此之外，还可以把文件路径放到环境变量的 “远程值” 那里。


![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/482802/image-preview)

然后在 “批量编辑” 中通过变量的方式引用该文件路径，这样也可以在构建时通过文件路径获取到实际文件。


![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/482803/image-preview)

</Accordion>

<Accordion title="想要定时构建怎么设置？" defaultOpen={false}>

Apifox 目前已支持使用定时任务，具体可参考帮助文档的[定时任务](https://docs.apifox.com/scheduled-tasks.md)模块，这种方式会更友好且方便。


如果要在 Jenkins 中设置定时任务，可以通过配置项目的 “构建触发器（Build Triggers）” 来实现，并使用类似于 Unix 的cron表达式来指定构建的时间和频率。


在 Jenkins 的项目配置页面，找到 “构建触发器（Build Triggers）” 模块，勾选 “定期构建（Build periodically)” 选项，在出现的文本框中输入cron表达式来定义构建的时间和频率，关于corn表达式的使用这里不具体赘述。


![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/482804/image-preview)
</Accordion>


