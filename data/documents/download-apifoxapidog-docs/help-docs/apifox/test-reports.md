# 测试报告

自动化测试运行结束后将输出一份测试报告，你可以在此处直观地看到哪些接口没有通过测试。

点击 “测试报告” 标签页，可以查看当前场景用例的历史测试报告。为了方便测试人员快速区分，功能测试报告左侧会标记分支图标 <Icon icon="ph-bold-git-branch"/>，性能测试报告则标记仪表盘图标 <Icon icon="undefined-dashboard-3-line"/>。你还可以通过下拉筛选快速分类。


<Background>

![CleanShot 2024-12-05 at 13.58.18@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/481544/image-preview)
</Background>


## 查看功能测试报告详情

点击相应的功能测试报告列表项，可以查看测试报告详情。

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/481545/image-preview)
</Background>

点击相应的接口可查看执行结果。
<Background>
![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/481547/image-preview)
</Background>



## Debug 调试

在每个接口的详情中，你能看到这个接口的请求和响应信息。你也可以点击 “调试此步骤” 重新发送这个接口。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/481549/image-preview)
</Background>


:::tip[]
使用 “调试此步骤” 时，如果你用到了 “前置测试步骤” 生成的变量值，此时是无法获取这个变量值的，只能使用变量当前的值。
:::


## 查看性能测试报告

性能测试报告记录了测试过程中的各项关键性能测试指标，包括接口请求总数、每秒接口请求数、平均响应时间、最大/最小响应时间和请求失败率。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/481551/image-preview)
</Background>


点击 “请求失败率” 检查接口的失败请求，分析可能的错误原因。你还可以点击筛选栏中筛选接口。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/481552/image-preview)
</Background>


性能测试会发出大量请求，所以只对错误请求进行分类展示，不记录详细的错误信息和单个请求详情。如果发现意外错误，请先运行 “功能测试” 并解决所有问题，然后再运行 “性能测试”。

## 导出和分享报告

测试报告支持导出 HTML 格式。测试任务完成后，点击 “导出报告” 按钮即可。

:::tip[]
性能测试报告不支持导出。
:::

测试报告支持分享。进入测试报告后，点击右侧的 “分享” 按钮，生成链接发给其他人。

<Background>
 
![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/481558/image-preview)
</Background>



如果你能访问这份报告的请求/响应详情，可以勾选 “同时分享请求/响应详情” 选项，分享测试报告中的所有请求/响应详情。其他用户打开链接后可以直接看到测试报告的详细内容，提高团队协作效率。

点击分享测试报告后，本地的测试报告数据会上传到云端。


其他团队成员可以在 “测试报告” 的 “共享” 页面中查看所有已分享的测试报告。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/481561/image-preview)
</Background>


如果 “同时分享请求/响应详情” 按钮变灰，说明这份测试报告的详情无法与其他项目成员分享。

详情无法分享的原因可能是：

- 使用了 CLI 运行，但没有带上选项：`--upload report detail`，报告保存在了 CLI 执行机器的本地
- 运行并生成测试报告前没有保存详情
- 当前测试报告是其他项目成员生成的

## 了解更多


<Card title="导出场景用例数据" href="/5629572m0">
场景用例支持导出 `Apifox CLI`、`Postman`、`Jmeter` 格式数据文件，它们可以在本地环境中或外部持续集成流水线中运行，以便更好地与团队中现有的测试工作流相融合。
</Card>



:::tip[最佳实践]
[Apifox 中自动化测试的场景用例如何批量导入和导出？](https://apifox.com/blog/how-to-batch-import-and-export-test-scenarios/)
:::

