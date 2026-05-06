# CLI 命令选项

Apifox CLI 是一个强大的命令行工具，允许开发人员在终端、CI/CD 流程中运行 Apifox 中的自动化测试。

## 基础语法

```bash
apifox <command> [options]
```

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/620387/image-preview)
</Background>

## 身份验证

在访问你的私有项目前，需要先登录或设置 [访问令牌](https://docs.apifox.com/api-access-token)。

| 命令 | 说明 | 示例 |
| :--- | :--- | :--- |
| `login` | 使用令牌登录，令牌会持久化到本地。 | `apifox login --with-token <您的令牌>` |
| `logout` | 退出登录。 | `apifox logout` |
| `whoami` | 显示当前登录的用户信息。 | `apifox whoami` |

**示例场景：首次登录**
```bash
# 获取令牌后运行
apifox login --with-token APS-xxxxxxxxxxxxxx
```

## 项目管理

管理和查看你账户下的所有项目。

| 命令 | 说明 | 示例 |
| :--- | :--- | :--- |
| `project list` | 列出所有项目（ID、名称、描述）。 | `apifox project list` |
| `project view` | 查看特定项目的详细配置。 | `apifox project view <projectId>` |

**示例场景：查找项目 ID**
```bash
# 获取所有项目列表
apifox project list
```

## 环境管理

查看项目关联的环境配置信息，如前置 URL (Base URL) 和服务设置。

| 命令 | 说明 | 示例 |
| :--- | :--- | :--- |
| `environment list` | 列出项目下的所有环境。 | `apifox environment list --project <projectId>` |
| `environment view` | 查看特定环境的配置详情（前置 URL 等）。 | `apifox environment view <envId> --project <projectId>` |

**示例场景：查看环境的前置 URL**
```bash
# 查看项目 123456 下环境 20933137 的具体配置
apifox environment view 20933137 --project 123456
```

## 自动化测试

你可以快速查询并执行定义的测试流程。

| 命令 | 说明 | 示例 |
| :--- | :--- | :--- |
| `test-scenario list` | 列出项目的所有场景用例。 | `apifox test-scenario list --project <projectId>` |
| `test-scenario run` | 运行指定的场景用例。 | `apifox test-scenario run <id> --project <pid>` |
| `test-suite list` | 列出项目的所有测试套件。 | `apifox test-suite list --project <projectId>` |
| `test-suite run` | 运行指定的测试套件。 | `apifox test-suite run <id> --project <pid>` |

**示例场景：直接运行场景用例**
```bash
# 运行项目 123456 下的场景 789，并指定环境 555
apifox test-scenario run 789 --project 123456 --environment 555
```

## 核心运行命令：`apifox run`

这是最常见的用法，通常直接从 **Apifox 客户端 -> 自动化测试 -> CI/CD** 面板中复制生成的命令。

### 常用命令示例 (从客户端复制)

**1. 使用 Access Token 运行在线场景：**
```bash
apifox run --access-token $APIFOX_ACCESS_TOKEN -t 637132 -e 358171 -r cli,html --upload-report
```
*   `-t`: 场景用例 ID
*   `-e`: 运行环境 ID
*   `-r`: 报告格式
*   `--upload-report`: 执行完后自动同步报告到云端

**2. 运行本地导出的 JSON 文件：**
```bash
apifox run ./examples/sample.apifox-cli.json -r cli,html
```

### 运行参数表说明

```bash
apifox run -h
```

| 参数 | 描述 | 默认值 |
|------|------|--------|
| `--access-token <token>` | 设置鉴权令牌 | - |
| `-t, --test-scenario <id>` | 指定场景用例 ID | - |
| `-f, --test-scenario-folder <id>` | 指定场景用例目录 ID | - |
| `--test-suite <id>` | 指定测试套件 ID | - |
| `--project <id>` | 项目 ID | - |
| `-e, --environment <id>` | 环境 ID | - |
| `-r, --reporters [reporters]` | 指定报告类型 (cli, html, json, junit) | `["cli"]` |
| `--out-dir <path>` | 输出报告目录 | `./apifox-reports` |
| `--out-file <name>` | 输出报告文件名（不含后缀）。支持变量: `{SCENARIO_NAME}`, `{FOLDER_NAME}`, `{GENERATE_TIME}` | `apifox-report-{timestamp}` |
| `--out-json-failures-separated` | 开启 JSON 报告时，将失败详情单独导出 | - |
| `-n, --iteration-count <n>` | 设置循环次数 | - |
| `-d, --iteration-data <path>` | 设置循环数据 (JSON/CSV) 或数据 ID | - |
| `--on-error <behavior>` | 设置错误处理方式 (`ignore`, `continue`, `end`) | - |
| `--global-var <key=value>` | 设置全局变量。支持设置多个。 | - |
| `--env-var <key=value>` | 设置环境变量。支持设置多个。 | - |
| `--variables <path>` | 指定包含变量的本地文件路径 | - |
| `--notification <ids>` | 运行完成后通知指定对象 ID (逗号分隔) | - |
| `--notification-failed-event <ids>` | 仅失败时通知指定对象 ID | - |
| `--external-program-path <path>` | 指定外部脚本/程序的所处目录 | 当前目录 |
| `--database-connection <path>` | 指定数据库配置文件的所处路径 | - |
| `--ignore-redirects` | 阻止自动重定向 | - |
| `--silent` | 开启静默模式，不输出至控制台 | - |
| `--color <on\|off\|auto>` | 控制台彩色输出开关 | `auto` |
| `--delay-request [ms]` | 请求之间的停顿间隔 | 0 |
| `--timeout-request [ms]` | 接口请求超时时间 | 0 |
| `--timeout-script [ms]` | 脚本执行超时时间 | 0 |
| `-k, --insecure` | 关闭 SSL 校验 | - |
| `--ssl-client-cert-list <path>` | 指定客户端证书配置路径 (JSON) | - |
| `--upload-report` | 将本次测试报告上传至云端查看 | - |
| `-b, --bigint` | 兼容 BigInt 类型 | `false` |
| `--verbose` | 显示详细的请求/响应信息 | - |
| `--lang <zh \|en>` | 设置 CLI 语言 | `zh` |

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/620403/image-preview)
</Background>

## CLI 中的文件上传

在处理需要上传文件的接口时，要注意：Apifox 只保存本地文件路径，而实际文件是存在你的本地电脑或运行 CLI 的机器上的。这在不同机器上通过 CLI 运行测试时可能会出问题。

要解决这个问题，按照下面的步骤操作：

<Steps>
  <Step>
先将需要的文件复制或上传到运行 CLI 的机器上。
  </Step>
  <Step>
**把该文件路径复制下来。** 例如：`/var/www/myapp/uploads/apifox-xiangmu.jpg`
      ![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/482799/image-preview)
  </Step>
  <Step>
然后在 Apifox 的自动化测试里定位到需要上传文件的接口，点击 “批量编辑” 按钮。
![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/482800/image-preview)
  </Step>
    <Step>
将上传到 CLI 机器上的 “文件路径” 填入到格式中 “参数值” 的位置即可。
![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/482801/image-preview)
  </Step>  
    <Step>
除此之外，还可以把文件路径放到环境变量的 “远程值” 那里，然后在 “批量编辑” 中通过变量的方式引用。
![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/482802/image-preview)
  </Step>  
</Steps>

:::tip[]
注意，如果你想在本地再次运行这个场景用例，需要把参数值中的文件路径改回本地机器上的路径。
:::

## CLI 中的数据库操作

当你的场景用例包含数据库操作时，因为数据库配置是保存在本地而不是云端，需要额外步骤：

<Steps>
  <Step>
对于包含数据库操作的场景用例，在命令行生成界面点击 “下载数据库配置文件”。
<Background>
![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/482761/image-preview)
</Background>
  </Step>
  <Step>
下载该文件（如 `database-connections.json`），并放在运行 CLI 的目录下。
  </Step>
  <Step>
在命令中包含 `--database-connection` 选项。示例：
```js
apifox run --access-token ****** -t 123456 -e 123456 -r html,cli --database-connection ./database-connections.json
```
  </Step>
</Steps>

## 将本地 CLI 测试报告上传到云端

只需在命令末尾加上 `--upload-report` 参数：

<Steps>
  <Step>
在命令执行时加入参数：
```bash
apifox run --access-token $APIFOX_ACCESS_TOKEN -t 637132 -r html,cli --upload-report
```  
  </Step>
  <Step>
查看上传的报告：
- 打开 Apifox 自动化测试面板中的 “测试报告”
- 找到 “共享” 栏目
<Background>
![](https://api.apifox.com/api/v1/projects/5097254/resources/482767/image-preview)
</Background>
  </Step>
</Steps>

## CLI 中使用外部脚本/程序

可以通过 `--external-program-path` 引用外部脚本：

```bash
apifox run ... --external-program-path ./scripts
```
这个例子中，CLI 会引用 `./scripts` 目录下的程序。如果没有指定层级，默认是当前 CLI 执行目录。

1. **本地路径**：建议按类别整理脚本文件，放在特定目录下并在 CLI 命令中指定。
2. **云端代码仓库**：在 CI/CD 工作流中先拉取脚本到本地，再在 CLI 命令中指定实际路径。

## SSL

Apifox CLI 支持传入客户端证书。

### 使用单个 SSL 客户端证书 

* `--ssl-client-cert` 

  指定 SSL 客户端公钥证书的路径 

* `--ssl-client-key` 

  指定 SSL 客户端私钥证书的路径（可选） 
  
* `--ssl-client-passphrase`

  指定 SSL 客户端证书密码（可选）

### 使用 SSL 客户端证书配置文件（支持多个证书）

* `--ssl-client-cert-list` 

  指定 SSL 客户端证书列表的 JSON 文件路径。例如：`ssl-client-cert-list.json`

    ```json 
    ssl-client-cert-list.json
    
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

此选项支持根据 URL 或主机名设置不同的 SSL 客户端证书。它的优先级高于 `--ssl-client-cert`、`--ssl-client-key` 和 `--ssl-client-passphrase` 选项。如果 URL 在列表中没有匹配项，会使用这些选项作为后备选项。

## HTTP/2

CLI 可以通过 `--preferred-http-version` 参数配置使用特定的协议版本发送请求。

协议版本参数值：

1. `"HTTP/2"` - HTTP/2 应用层协议协商（ALPN），仅支持 HTTPS 请求
2. `"HTTP/2-with-prior-knowledge"` - 已知的 HTTP/2
3. `"HTTP/1"` - HTTP/1.1

参数支持以下配置方式：

1. 为 HTTPS 和 HTTP 请求设置不同的协议版本：
   ```
   --preferred-http-version="https=HTTP/2,http=HTTP/2-with-prior-knowledge"
   ```

2. 为 HTTPS 和 HTTP 设置相同的协议版本：
   ```
   --preferred-http-version="HTTP/1"
   ```

3. 为 HTTPS 和 HTTP 设置 HTTP/2（不支持的值会自动忽略）：
   ```
   --preferred-http-version="HTTP/2"
   ```
   
## 常见问题 (FAQ)

<Accordion title="如何解决 “Invalid character in header content['Authorization']” 这个错误？" defaultOpen>
这个错误通常是因为 Authorization 请求头中包含了非法字符，比如中文、换行符或多余的空格。请确认 Authorization 的值中 没有中文以及特殊符号，并且格式符合要求。
</Accordion>

