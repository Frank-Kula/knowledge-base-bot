# 页面布局

Apifox 的主界面大致可以分为以下几个部分：

- 头部区域 
- 侧边栏 
- 工作区 
    - 目录树 
    - 标签页 
    - 环境选择器
- 底部区域

<Background>

![CleanShot 2024-09-14 at 16.13.44@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/465721/image-preview)
</Background>


## 头部区域

头部包含以下主要功能模块：
<Frame>
![CleanShot 2024-09-14 at 16.15.20@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/465722/image-preview)
</Frame>

- <Icon icon="material-outline-home"/> **主窗口**
    进入个人主页，展示你加入的团队及其成员、项目、权限、订单、组织和 API Hub 等信息。

- **项目标签**
    每个标签代表一个项目，点击即可切换；点击项目名称左侧按钮可在新窗口打开项目。

- <Icon icon="ph-bold-arrows-clockwise"/> **刷新**
    重新加载当前项目数据，同时关闭所有打开的标签。

- <Icon icon="material-outline-settings"/> **设置**
    调整本地客户端的设置（如外观、网络代理等），这些设置仅影响当前客户端。

- <Icon icon="ph-bold-bell"/> **通知**
    显示团队活动的提醒信息。

- **头像**
    账号设置，可以设置基本账户信息、访问令牌 (Access tokens) 等。

## 侧边栏

<Frame>
  <img src="https://api.apifox.com/api/v1/projects/5097254/resources/465724/image-preview" style="width: 100px" />
</Frame>

侧边栏包含以下功能模块：

- **项目图标**
    点击跳转到[团队与项目](https://docs.apifox.com/management-center.md)。

- **接口管理**
    Apifox 的核心界面，你可以在这里 [新建接口](https://docs.apifox.com/create-api.md)、[发送接口请求](https://docs.apifox.com/send-api-request.md)、[新建数据模型](https://docs.apifox.com/create-data-schema.md)、编写 [Markdown](https://markdown.apifox.cn/) 等。

- **自动化测试**
    如果你需要批量发送请求 *（类似运行 Postman 的 Collection）* 或编排接口之间的数据关系和逻辑，可以在自动化测试中[新建测试场景](https://docs.apifox.com/new-test-scenario.md)。基于测试场景，你还可以查看[测试报告](https://docs.apifox.com/test-reports.md)、[运行性能测试](https://docs.apifox.com/performance-testing.md)、[管理测试数据](https://docs.apifox.com/data-driven-testing.md)、[集成 CI/CD](https://docs.apifox.com/cicd.md) 等。

- **分享文档**
    一旦创建接口，可以在该模块中[分享给其他同事](https://docs.apifox.com/quick-share.md)，或者[发布文档站](https://docs.apifox.com/publish-documentation-site.md)。发布文档站可以[自定义文档域名](https://docs.apifox.com/custom-domain.md)、[调整页面结构](https://docs.apifox.com/page-layout-settings.md)以及[自定义 URL](https://docs.apifox.com/seo-settings.md) 等。

- **请求历史**
    在请求历史中可以查看并重新发送所有已发送的请求。

- **项目设置**
    所有与当前项目相关的设置，包括基本设置、功能设置、通知设置、项目资源和项目数据的导入/导出。

- **邀请成员**
    邀请其他用户加入当前项目。

## 工作区

### 目录树

<p style="text-align: center">
    <Frame>
    <img src="https://api.apifox.com/api/v1/projects/5097254/resources/486824/image-preview" style="width: 240px" />
    
    </Frame>
</p>

目录树从上到下包括以下功能模块：

- **分支与版本**
    默认显示主分支，你可以切换到其它分支，或者新建分支、管理分支。

- **搜索与过滤**
    你可以搜索和过滤接口。注意，目前只能搜索接口名称，无法搜索目录名称或用例名称。

- **新建**
    你可以创建各种类型的元素，如接口、快捷请求、数据模型、Markdown 等。

- **项目概览**
    项目的整体视图，包括项目统计、接口用例覆盖情况等。

- **接口**
    以目录结构组织的接口和接口用例，Markdown 和 WebSocket 等也可以包含在其中。

- **数据模型**
    以目录结构组织的数据模型。

- **组件库**
    可复用的数据模型，可设置默认响应模板以及响应组件。

- **快捷请求**
    以目录结构组织的接口请求，类似于 Postman 的 Collection。


### 标签页

点击目录树中的任何元素会打开一个标签页。

标签页包括以下类型：
- 接口
- 数据模型
- 响应组件
- Markdown
- 目录
- 快捷请求
- WebSocket
- 项目概览
- 新建...

单击打开标签页时，标题显示为斜体，此时点击目录树其它元素会覆盖当前标签，适合浏览场景。

修改标签内容后，标题变为常规字体，此时点击目录树其它元素会打开新标签，适合编辑场景。

若不希望标签被覆盖，可双击打开标签，使其直接显示为常规字体。

标签页的右侧有两个按钮：
- <Icon icon="ph-bold-plus"/> **`新建...`**: 可以创建各种类型的元素。
- <Icon icon="material-outline-more_horiz"/> **`更多 (More)`**: 你可以关闭所有标签、关闭当前标签或关闭除当前标签之外的所有标签。

## 底部区域

<Frame>
![CleanShot 2025-03-20 at 15.30.39@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/505398/image-preview)
</Frame>

从左到右，底部区域包含以下功能：

- <Icon icon="ph-bold-arrow-line-left"/> **折叠/展开**
    可以折叠或展开左侧目录树。
    
- <Icon icon="ph-bold-check-circle"/> **在线状态**
    显示当前是否在线。如果离线，团队同步将出现问题。
    
- <Icon icon="ph-bold-network"/> **Agent**
    Apifox Web 独有的功能，允许你选择代理发送请求。
    
- <Icon icon="ph-bold-cookie"/> **Cookie 管理**
    Cookie 管理器，可以存储当前的 Cookies。

- <Icon icon="ph-bold-trash"/> **回收站**
    删除的接口、用例、数据模型、响应组件、测试场景、定时任务等会进入回收站，30 天后自动删除。

- <Icon icon="solar-bold-chat-round-dots"/> **文档 & 交流群**
    可打开帮助文档或加入交流群。
