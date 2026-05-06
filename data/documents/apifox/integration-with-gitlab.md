# 与 Gitlab 集成


## 初始化 Gitlab 流水线

访问 Gitlab 并登录，点击左侧导航栏中的 “Projects”，然后点击 “New project” 按钮。

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/482807/image-preview)
</Background>


进入项目后，在 “Build” 部分，轻点 “Pipelines editor” 新建流水线。

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/482808/image-preview)
</Background>


## 获取 Gitlab 流水线代码

在 Apifox 的 **“自动化测试”** 页面中，点击 CI/CD 标签页。指定运行环境、选择是否启用测试数据、指定循环次数与间隔停顿时间后点击右上角的 “保存” 按钮完成初始化。选择生成可运行在 Gitlab CI 流水线内的代码，然后点击右上角的 “复制代码”。

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/482810/image-preview)
</Background>


粘贴至 Gtilab 的 Pipeline editor 内，然后点击 “Commit changes” 触发流水线。如果你的流水线中还有内置了其它任务，请根据实际情况妥善修改以确保流水线能够正常运行。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/482812/image-preview)
</Background>


## 运行流水线

流水线开始运行后，你将会在终端内看到运行的日志情况，此时你已将 Apifox 自动化测试步骤融入进了 Gitlab CI 流水线中。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/482813/image-preview)
</Background>

