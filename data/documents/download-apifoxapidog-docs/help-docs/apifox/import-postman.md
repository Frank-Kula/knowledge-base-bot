# 导入 Postman

## 概念对照

理解 Postman 和 Apifox 之间的概念关联，可以有效避免导入数据时出现不一致的情况。

在 Postman 中，`Collection` 对应 Apifox 中的 `项目`。因此，Postman Collection 中的变量相当于 Apifox 项目中的全局变量。
<Frame>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/514512/image-preview)
</Frame>


Postman 中管理的 API 使用变量来存储前置 URL *（通常是根域名）*，而在 Apifox 中，前置 URL 是独立存储在 “环境管理” 中的 “服务” 里的。


<Frame >
![CleanShot 2024-09-20 at 18.26.41@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/466610/image-preview)
</Frame>




## 接口示例说明

假设你在 Postman 里有一个名为 `Apifox Echo` 的 Collection（集合），这个集合里设置了两个变量：

- `baseUrl`：用来定义服务的地址
- `name`：作为 query 参数传递

如下图所示：

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/486860/image-preview)
</Background>

这个集合里面有一个 GET 请求，格式如下：

```http
GET {{baseUrl}}/get?name={{name}}
```

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/486861/image-preview)
</Background>


现在，我们需要把这个 Collection（集合）导出，然后导入到 Apifox。当然，如果你已经在 Postman 里有现成的 Collection，也可以直接用你自己的 Collection。


## 导出 Postman 数据

### 导出 Collection


<Steps>
  <Step>
    打开 Postman 左侧 Collections
  </Step>
  <Step>
    点击要导出的集合 `···` → `Export`
      <Background>
    ![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/486862/image-preview)
    </Background>
  </Step>
  <Step>
    选择格式：Collection v2.1
      
<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/486864/image-preview)
</Background>
  </Step>
    <Step>
    点击 Export → 保存为 `.json`
  </Step>
</Steps>

### 导出 Environment（可选）

<Steps>
  <Step>
    打开 Postman 左侧 Environments
  </Step>
    <Step>
    找到目标环境 → `···` → `Export`
  </Step>
    <Step>
    保存为 `.json` 文件
  </Step>
</Steps>

### 导出 Workspace 数据/Data Dumps（可选）

Postman 提供了导出整个 Workspace 的方式，称为 **Data Dump**，可将全部 Collections、Environments、Globals 批量打包为一个 JSON 文件。

**导出步骤：**

<Steps>
  <Step>
    点击右上角头像 → 进入 `Settings`  
  </Step>
    <Step>
    切换到 `Account` 标签页
  </Step>
    <Step>
    点击 `Export Data` → 选择要导出的数据类型（如 Collections、Environments）
  </Step>
    <Step>
    点击 `Request Data Export` 
  </Step>
    <Step>
    稍后将通过邮件收到下载链接（有效期 2 天）
  </Step>
</Steps>



:::tip[注意]
Data Dump 主要用于备份和 Postman 内部恢复场景，不推荐用于迁移至 Apifox。建议优先使用单独导出 Collection 和 Environment 的方式。
:::



## 导入 Postman 数据

### 导入 Collection

打开 Apifox 中的“项目设置”面板，点击“导入数据”，选择 Postman 并上传文件。


<Background>

![CleanShot 2025-11-25 at 17.55.43@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/597499/image-preview)
</Background>


你可以在导入预览页中查看 `Collection` 下的所有接口。为了无缝迁移，需要在“环境”页中勾选与 `Collection` 同名的环境，然后点击“确定导入”按钮。


<Background>


![CleanShot 2025-11-25 at 17.56.57@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/597500/image-preview)
</Background>


导入完成后，你可以在 API 文档页看到 `name` 参数，以及在环境管理中看到 `baseUrl` 中的链接地址。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/486867/image-preview)
</Background>


调试接口时，选择相对应的环境。前缀 URL 将自动拼接在路径之前，与 Postman 相一致。

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/486868/image-preview)
</Background>

### 导入 Environment（可选）

<Steps>
  <Step>
    打开 Apifox，在项目中进入 “项目设置 → 导入数据” 页面  
  </Step>
    <Step>
    选择 Postman → 上传导出的 Postman Environment `.json` 文件
        
  </Step>
    <Step>
    导入后可在接口调试时切换对应环境

  </Step>
</Steps>


### 导入 Workspace 数据/Data Dumps（可选）

<Steps>
  <Step>
    打开 Apifox，在项目中进入 “项目设置 → 导入数据” 页面  
  </Step>
    <Step>
    选择 Postman → 上传解压后的文件/文件夹
  </Step>
    <Step>
    导入后可在接口调试时切换对应环境（Collection 目前只支持选择一个）
        
  </Step>
   <Step>
    **目前不建议使用 Data Dump 来迁移数据**。推荐你分别导入：

    - Collection：对应 Apifox 项目及接口结构
    - Environment：对应 Apifox 环境配置

  </Step>
</Steps>


:::tip[]
更详细的教程，请参考这篇最佳实践：[之前使用 Postman 来管理 API，如何迁移到 Apifox？](https://apifox.com/blog/migrate-from-postman-to-apifox/)
:::
