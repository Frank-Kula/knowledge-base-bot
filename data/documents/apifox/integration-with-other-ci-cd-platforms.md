# 与其它更多 CI/CD 平台集成


本文档将以数个主流的 CI 平台为例，介绍如何将 Apifox 中的自动化测试任务非常高效地融入至研发团队的持续集成工作流中。


## CircleCI

### 1. 使用 Github 账号初始化 CircleCI 项目

在 Github 账号内，新建一个名为 CircleCI 的公开代码仓库。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/482820/image-preview)
</Background>


前往 [CircleCI](https://circleci.com/) 官网，选择用 Github 账号登录。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/482821/image-preview)
</Background>



选择并关联该仓库。

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/482822/image-preview)
</Background>


关联仓库时还需要按照 CircleCI 的页面要求，在 Github 中的 `deploy keys` 中填入 SSH 公钥，然后将私钥粘贴至 CircleCI 的项目设置内。

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/482823/image-preview)
</Background>


### 2. 生成 CircleCI 流水线代码

选择 CircleCI，Apifox 将自动生成可运行在 CircleCI 流水线内的代码，点击右上角的“复制代码”。

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/482824/image-preview)
</Background>


将代码粘贴至前文所创建的 CircleCI 代码仓库内的配置文件 `.circleci/config.yml` 文件。

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/482825/image-preview)
</Background>


### 3. 自动运行

提交 `.circleci/config.yml` 文件的 commit 后，CircleCI 就会自动运行测试任务。

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/482826/image-preview)
</Background>


## Bitbucket Pipelines

### 1. 初始化 Bitbucket Pipelines

注册并登录 [Bitbucket Pipelines](https://bitbucket.org/)，在 Repositories 页面新建一个代码仓库。

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/482827/image-preview)
</Background>


然后前往代码仓库内新建流水线 Pipeline。

> 新建流水线时需提前绑定 Bitbucket 账号的两步验证码。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/482828/image-preview)
</Background>


### 2. 生成 Bitbucket Pipelines 代码

在 Apifox 的 “自动化测试” 页面中，点击 “新建” CI/CD 环境，选择 Bitbucket Pipelines 并点击“复制代码”。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/482829/image-preview)
</Background>


将代码粘贴至新建的 Bitbucket Pipelines 的流水线配置文件中后触发运行。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/482830/image-preview)
</Background>


### 3. 自动运行

Bitbucket Pipelines 会自动运行测试任务。

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/482831/image-preview)
</Background>


