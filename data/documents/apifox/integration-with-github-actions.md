# 与 Github Actions 集成


## 初始化 Github 流水线

访问 Github 并登录，进入到目标代码仓库中，点击 Github Actions 按钮，轻点 “New workflow” 按钮。

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/482816/image-preview)
</Background>



## 获取 Github Actions 配置代码

在 Apifox 的 **“自动化测试”** 页面中，点击 CI/CD 标签页。指定运行环境、选择是否启用测试数据、指定循环次数与间隔停顿时间后点击右上角的 “保存” 按钮完成初始化。

选择生成可运行在 Github Actions 内的代码，然后点击右上角的 “复制代码”。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/482817/image-preview)
</Background>


登录 Github 后选择一个项目，在代码仓库中的 Actions 页面中新建 workflow，粘贴由 Apifox 自动生成的 Github Actions 代码。如果你的流水线中还内置了其它任务，请根据实际情况妥善修改，确保流水线能够正常运行。

点击 “Commit changes” 按钮后即可自动触发此流水线。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/482818/image-preview)
</Background>

:::tip[]
如果你用的是新版的 CI/CD，请确保将代码中的变量 `$APIFOX_ACCESS_TOKEN` 替换为你自己的 [Access Token](https://docs.apifox.com/api-access-token.md) 。
:::

工作流文件将会保存在你的仓库下的 `.github/workflows/` 路径中。它是源代码的一部分，当你克隆或拉取项目到本地时也会包含它。你可以在本地开发环境中编辑它，并像处理其他文件一样通过 Git 提交更改。

工作流文件的开头通常包含如下语句：

```js
on: [push, pull_request]
```

这表示每当有人推送代码或创建/更新 Pull Request 时，GitHub 将自动触发此工作流。如果你想自定义哪些分支或事件应触发该工作流，可以参考官方文档：
👉 [GitHub Actions: 触发工作流的事件](https://docs.github.com/zh/actions/reference/events-that-trigger-workflows)

## 运行流水线

自动触发 Github Actions 流水线后，可在 Actions 页面查看流水线运行情况，此时你已经将 Apifox 的自动化测试流程集成到 Github Actions 内。并且，工作流将在每次有新代码提交时自动运行。

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/482819/image-preview)
</Background>


