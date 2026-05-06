# 安装和运行 CLI

Apifox CLI 是一个命令行工具，用来运行 Apifox 的场景用例。使用前需要先装好 Node.js，再装 Apifox CLI，然后即可进行测试。

## 安装 Apifox CLI

Apifox CLI 是基于 Node.js 开发的，所以得先装好 [Node.js](https://nodejs.org/en/download/package-manager/)，要求 Node.js 版本不能低于 `v16`。

在系统上全局安装 Apifox CLI，这样就能在任何地方运行它。


<Tabs>
   <Tab title="国内镜像源">
    ```bash
    npm i -g apifox-cli@latest --registry=https://registry.npmmirror.com/
    ```
  </Tab>
  <Tab title="npm 源命令">
   ```bash
   npm install -g apifox-cli
   ```
  </Tab>
</Tabs>



可以通过以下命令确认是否安装成功。

<Tabs>
  <Tab title="macOS / Linux">
    ```bash
    node -v && apifox -v && which node && which npm && which apifox
    ```
如果安装成功，运行上面的命令后会直接显示版本号和安装路径。

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/481928/image-preview)
</Background>


  </Tab>
  <Tab title="Windows">
请在 Windows 的 cmd（命令提示符） 中运行以下命令，不要在 PowerShell 中执行：
    ```bash
    node -v && apifox -v && where node && where npm && where apifox

    ```
   如果安装成功，运行上面的命令后会直接显示版本号和安装路径。


<Background>


![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/612074/image-preview)
</Background>

  </Tab>
</Tabs>


<Accordion title="安装命令一直卡住，没有进度，也没有报错？" defaultOpen>
如果你在执行 Apifox CLI 安装命令时，发现命令一直卡住、没有任何输出，也没有报错，通常是网络或权限相关问题。

建议直接将「完整命令 + 终端输出」交给 AI，让其协助判断具体原因。
</Accordion>



## 更新 Apifox CLI

用下面的命令可以升级 Apifox CLI。

```bash
npm install apifox-cli@latest -g
```

## 运行 Apifox CLI

要用 Apifox CLI 跑场景用例，得先创建并编排好场景用例。之后就能像在图形界面一样，在命令行中运行场景用例并得到测试报告。

Apifox CLI 支持两种运行方式：

1. **运行在线数据**：适合实时场景
2. **导出数据运行**：适合离线场景

### 运行在线数据

<Steps>
  <Step>
在场景用例中，切换到 CI/CD 标签页。

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/482009/image-preview)
</Background>

  </Step>
  <Step>
配置运行环境、测试数据、循环次数、间隔停顿时间等。界面上更改不同的值，会影响下方生成的实际命令。
- 运行环境，影响 `-e <environmentId>`
- 测试数据，影响 `-d <testDataId>`
- 循环次数，影响 `-n <n>`
- 间隔停顿，影响 `--delay-request <n>`
- 环境/全局变量值，如果选择 “导出本地值使用”，则可以在界面发现导出入口将当前项目的环境/全局变量本地值导出到文件内，并且影响 `--variables <path>`。需要将这个导出文件放到 CLI 运行机器内，并将此文件路径填入 `--variables <path>` 中。关于 “使用远程值” 和 “导出本地值使用” 的区别，[在此处了解更多](https://docs.apifox.com/5632037m0#不同运行方式间使用不同的环境全局变量值的规则)。
-       如果你的场景用例中同时使用了保存在本地的数据库连接配置，则产品界面会引导导出配置到本地文件，并且影响 `--database-connection <path>`。需要将这个导出文件放到 CLI 运行机器内，并将此文件路径填入 `--database-connection <path>` 中。
      
:::tip[]
建议数据库连接配置，使用变量形式保存，这样可以协同使用并且**无需**在 CLI 运行时增加`--database-connection <path>`选项。[了解更多](https://docs.apifox.com/database-connections.md)
:::
  </Step>
  <Step>
在 CI/CD 平台中，选择 “CLI 命令行”。
  </Step>
  <Step>
点击 “添加 Access Token” 按钮，然后 “生成 Token”。

:::highlight purple 
了解更多关于[访问令牌](https://docs.apifox.com/api-access-token.md)的信息。
:::
  </Step>
  <Step>
点击命令复制。
  </Step>
  <Step>
把命令粘贴到命令行中运行，即可在命令行看到测试报告。
  </Step>
</Steps>

### 导出数据运行

<Steps>
  <Step>
在场景用例中，切换到 CI/CD 标签页。
  </Step>
  <Step>
配置运行环境、测试数据、循环次数、间隔停顿时间等。
  </Step>
  <Step>
在 CI/CD 平台中，选择 “CLI 命令行”，然后切换到 “导出数据运行”。

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/482018/image-preview)
</Background>

  </Step>
  <Step>
把场景用例导出成 JSON 文件。
  </Step>
  <Step>
复制下方显示的命令。
  </Step>
  <Step>
把命令粘贴到命令行中运行，即可看到命令行测试报告。
  </Step>
</Steps>

:::tip[]
第二步中，在界面内的设置如 “运行在线数据” 一样会自动影响下方 CLI 使用的选项及值。需要注意的是通过此种方式运行，环境/全局变量使用的是随场景用例一起导出的文件内的值。[在此处了解更多](https://docs.apifox.com/5632037m0#不同运行方式间使用不同的环境全局变量值的规则)。
:::

## CLI 测试报告

跑完 CLI 后，你会得到一份命令行测试报告，包含场景用例的执行统计数据，以及失败请求的验证和断言信息。


<Background>

![CleanShot 2024-12-06 at 18.17.22@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/482020/image-preview)
</Background>


在运行 CLI 的文件夹里还能找到 `/apifox-reports/` 目录，里面有 HTML 格式的 CLI 测试报告。


<Background>
![CleanShot 2024-12-06 at 18.21.03@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/482023/image-preview)
</Background>


## 命令选项

Apifox CLI 提供了丰富的配置选项来自定义测试集合的运行。详情可以看  [CLI 命令选项](https://docs.apifox.com/cli-command-options.md)。

## 在 CI/CD 中使用 Apifox CLI

Apifox CLI 支持和各种流水线工具集成，比如 Jenkins、GitLab、GitHub Actions 等。想了解更多可以看看 [CI/CD 集成](https://docs.apifox.com/cicd.md)。
