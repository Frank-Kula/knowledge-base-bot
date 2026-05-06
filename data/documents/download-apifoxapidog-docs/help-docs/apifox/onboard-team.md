# 团队入驻

你可以按照下面的步骤来创建一个团队，建议先和团队管理员以及 IT 团队对接，把 Apifox 的安装部署和权限管理配置好。然后再进行团队设置，包括邀请成员、分配角色和创建项目资源等。


## 和 IT 团队对接

每个公司引入新软件的流程都不太一样，你需要和 IT 团队确认以下几点：

- IT 团队可能需要在设备管理策略中添加 Apifox 的白名单。你可以把[下载链接](https://docs.apifox.com/download.md)发给 IT 团队，方便他们设置。

- 如果公司网络有代理，需要在 Apifox 中配置代理信息。找 IT 团队要到代理配置后，你可以这样设置：


    :::note[]
    **已登录用户：** 点击右上角的 “⚙设置 -> 网络代理”
    **未登录用户：** 在登录界面左下角设置代理
    :::

- 如果公司有防火墙，IT 团队需要把这些域名加入白名单，确保 Apifox 能正常同步数据：

    ```js
    *.apifox.com
    *.apifox.cn
    ```
 

## 团队设置

首先要确定谁是团队管理员。团队管理员注册账号后可以[创建团队](https://docs.apifox.com/team-basic-operations.md)，自动成为这个团队的 “团队所有者”。

**团队所有者**有这些权限：
- 修改团队信息
- 创建项目
- 管理成员
- 设置权限
- 管理订阅和付款
- 转让和解散团队

一个团队可以包含多个成员和项目。管理员可以给不同成员分配不同项目的权限。


## 成员管理

**团队所有者**可以设置**团队管理员**，让他们负责邀请和管理其他成员。

团队管理员可以通过邮件或邀请链接[邀请成员](https://docs.apifox.com/team-member-management.md)加入团队，还可以设置成员对项目的默认权限，比如管理员、编辑者、只读或禁止访问。

Apifox 里的[团队权限和项目权限](https://docs.apifox.com/member-roles-and-permissions.md)是两套东西：
- **团队权限：** 管理整个团队，包括团队设置、成员管理等。角色有团队所有者、团队管理员、团队成员和游客。

    <Background>

    <img src="https://api.apifox.com/api/v1/projects/5097254/resources/485300/image-preview" width="460px"/>
    </Background>

- **项目权限：** 管理具体项目，设置成员在项目中的权限。角色有管理员、编辑者、只读成员、禁止访问以及自定义权限。

    <Background>
    <img src="https://api.apifox.com/api/v1/projects/5097254/resources/485302/image-preview" width="460px"/>

    </Background>

## 创建项目

Apifox 中的项目对应一个 OpenAPI Spec *（又称 OpenAPI/Swagger规范）*，除此之外，还包括测试用例、API 文档、请求用例和项目配置。

和 Postman 对比的话，Postman 的 Workspace 对应 Apifox 的团队，Collection 对应 Apifox 的项目。

Apifox 有三种项目类型，HTTP 项目、gRPC 项目和 Dubbo 项目，这三种目前不能混用：

- HTTP 项目：支持 REST API、SOAP/WebService、GraphQL、WebSocket 和 SSE 等常见 HTTP API 的调试。

- gRPC 项目：专门用来调试 gRPC 接口。

- Dubbo 项目：专门用来调试 Dubbo 接口。

只有**团队所有者**和**团队管理员**才能创建项目。[创建项目](https://docs.apifox.com/project-basic-operations.md)时可以选择项目类型，设置其他成员的默认权限。


## 数据迁移

Apifox 支持导入十多种格式的数据，可以轻松导入各种常见 API 格式。

[从 Postman 导入](https://docs.apifox.com/import-postman.md)时，因为数据结构不同，Postman 的请求会变成 Apifox 的用例，`base URL` 会保存在环境管理的服务模块中。不过这不影响在 Apifox 中正常使用这些请求，Postman 的脚本也能直接运行。想了解更多迁移相关内容，可以看[这篇博客](https://apifox.com/blog/migrate-from-postman-to-apifox/)。

如果要在 Apifox 项目之间迁移数据，用项目设置里的 “导出数据” 功能可以导出 Apifox 格式的文件，然后在目标项目中导入。Apifox 格式包含了完整的项目信息，不要用 OpenAPI 格式迁移 Apifox 项目，因为可能会丢失 API 文档以外的数据。

Apifox 和私有化部署版本之间的数据不互通，也要用**导出 Apifox 格式**的方式迁移。

## 项目初始配置

建议在项目开始时就配置好这些设置，方便后续团队协作：

1. **项目语言**：Apifox 区分 “项目语言” 和 “界面语言”。项目语言是项目内容用的语言，界面语言是软件界面显示的语言。创建项目时要选好项目语言，项目里的一些初始内容会用这个语言。

2. **默认响应模板**：如果公司有统一的响应格式，可以设为 “默认响应模板”。这样新建的接口都会用这个默认响应，保持一致性。

   > 在 “接口管理 -> 组件库 -> 默认响应模版” 中设置默认响应模板

3. **响应组件**：一般来说，项目里各个接口的错误响应都差不多（比如 400、404）。你可以把这些常见的错误响应设为 “响应组件” 并默认启用，这样新建的 API 就会自带这些配置好的响应。

4. **API 状态**：Apifox 提供了一些内置的 API 状态，你可以根据公司需求自定义。用这些状态可以标记和追踪项目中每个 API 的进度或状态。

   > 在 “项目设置 - 功能设置 - 接口功能设置” 中设置接口状态。

## 集成功能

Apifox 能和很多常用工具集成，让 API 开发更顺畅：

1. **[CI/CD 集成](https://docs.apifox.com/cicd.md)**：Apifox 可以通过命令行运行，能和 Jenkins、Github、Gitlab 等 CI/CD 工具集成，实现 API 测试和部署的自动化。

2. **[数据库集成](https://docs.apifox.com/database.md)**：Apifox 支持在前后置操作中执行 SQL 查询，还能从数据库表结构生成接口数据模型。支持 MySQL、SQL Server、Oracle、MongoDB 等多种数据库。

3. **[消息通知集成](https://docs.apifox.com/notification-targets.md)**：可以把 API 的创建、修改、删除等动态推送到飞书、钉钉、企业微信、邮箱或支持 Webhook 的工具，及时通知团队成员接口的变化。

Apifox 还有更多外部工具集成功能等你探索，这些集成能让 API 开发和协作更高效。

## 熟悉 Apifox 功能

Apifox 有详细的文档帮助团队了解各项功能。新手建议先看看 [Apifox 入门指南](https://docs.apifox.com/5092448m0.md)，了解基础功能。

<!--
不同角色的成员可以看对应的使用指南：

- [API 设计者：设计 API](https://docs.apifox.com/5093626m0.md)
- [后端开发：调试 API](https://docs.apifox.com/5093741m0.md)
- [前端开发：Mock API](https://docs.apifox.com/5093821m0.md)
- [测试工程师：测试 API](https://docs.apifox.com/5094372m0.md)
-->
