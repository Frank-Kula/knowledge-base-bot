# 请求历史


## 查看接口请求历史

在 **“接口管理”** 中调试接口时，系统会自动保存请求和响应内容，这些数据以快照的形式存储在本地或浏览器中。

你可以通过左侧边栏的 **“请求历史”** 功能查看这些接口请求的历史记录，便于回溯或再次调试。


<Background>

![CleanShot 2025-01-14 at 16.12.01@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/489921/image-preview)
</Background>

可直接在请求历史中修改参数并点击 “发送” 按钮，重新调试接口。

:::tip[]
- 请求历史保存在个人本地 tab 页，仅自己可见。如需与项目成员共享，需将该请求 “分享”。

- 如果请求数据（请求 + 响应）大于 2MB，快照不会保存，但可通过 “分享” 功能将结果上传云端。

- 本地客户端请求历史上限为 500 条，存储于本地；Web 端调试的历史数据保存在浏览器 Storage 中，数量上限同为 500 条。

- 各端、各设备的本地请求历史数据相互独立。
:::

如果使用了变量，快照中将保留变量的引用效果。点击 **“实际请求”** 可查看本次请求的实际值。


<Background>

![CleanShot 2025-01-14 at 16.15.42@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/489929/image-preview)
</Background>

再次调试含变量的请求历史时，变量替换优先级为：**临时变量 ＞ 环境变量 ＞ 项目全局变量 > 团队全局变量**。[了解变量优先级](https://docs.apifox.com/global-environment-session-variables.md)

## 分享请求结果 / 请求历史

需要与团队成员同步某次请求结果时，可点击返回结果右上角的 “分享” 按钮，生成分享链接。


<Background>

![CleanShot 2025-01-14 at 16.24.58@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/489935/image-preview)
</Background>

项目成员通过链接可跳转到 “请求历史 -> 共享” 模块，查看被分享的请求结果并发起调试，也可直接在项目中访问 “请求历史 -> 共享” 查看所有共享历史。


<Background>

![CleanShot 2025-01-14 at 16.27.15@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/489937/image-preview)
</Background>


:::tip[]
共享的请求历史会上传至云端，便于团队协作。
:::

## 另存为接口用例

如果某次请求结果符合预期，可将其另存为接口用例，方便后续调试。点击请求历史右上角的 **“保存为用例”**，重命名用例后，可在 **“接口管理”** 中查看。



<Background>

![CleanShot 2025-01-14 at 16.31.07@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/489938/image-preview)
</Background>



:::tip[]
接口用例保存的是当前接口的请求参数设置，供后续或其他成员调试使用。详见[保存为用例](https://docs.apifox.com/api-test-cases.md)模块。
:::


## 另存为接口

在[快捷请求](https://docs.apifox.com/quick-request.md)中发起的请求记录支持保存为接口。在请求历史中找到对应记录，点击右上角的 “保存为接口”。


<Background>

![CleanShot 2025-01-14 at 16.36.18@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/489941/image-preview)
</Background>

填写接口名称并选择目录。如关闭 “保留完整 URL 路径”，需在[环境管理](https://docs.apifox.com/environments-and-services.md)中设置接口的前置 URL。


