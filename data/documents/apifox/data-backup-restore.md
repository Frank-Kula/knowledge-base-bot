# 数据备份与恢复

在 Apifox 中，你可以将数据导出为多种格式，包括 OpenAPI Specification、HTML、Markdown 等，未来的更新还会增加更多格式。建议定期备份并采取安全的存储方式，以防止意外情况下数据丢失。

## 导出数据

Apifox 支持导出单个接口、接口集合或整个项目的数据。

1. 打开 “项目设置”，在左侧找到 “导出数据” 选项卡。

   
<Background>

![CleanShot 2024-12-23 at 14.04.43@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/485693/image-preview)
</Background>


   这里你会看到各种导出参数。比如，我们建议 OpenAPI 导出时选择 3.1 版本。

2. 选择要导出的接口：

   - **导出单个接口：** 点击 “导出部分接口”，通过标签选择需要的 API，然后确认。
   
    <Background>

    ![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/485701/image-preview)
    </Background>


   - **导出接口集合：** 点击 “导出部分接口”，选择需要的目录，然后确认。

     
    <Background>

    ![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/485703/image-preview)
    </Background>


3. 选择要应用的环境，比如开发环境或测试环境。

  
    <Background>

    ![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/485705/image-preview)
    </Background>


4. 根据需要，选择导出为 JSON 文件或通过公开链接发布。

   
    <Background>

    ![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/485708/image-preview)
    </Background>


## 恢复数据

如果不小心删除了数据或需要回滚，可以从回收站和变更历史记录中恢复数据。

### 从回收站恢复数据

1. 点击页面右下角的回收站图标。

   
    <Background>

    ![CleanShot 2024-12-23 at 14.14.00@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/485711/image-preview)
    </Background>


2. 选择要恢复的数据，支持批量操作。

3. 点击 “恢复” 按钮。

   
    <Background>

    ![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/485717/image-preview)
    </Background>


### 从变更历史恢复数据

1. 对于有变更历史的接口，打开该接口并点击右上角的 “历史记录” 图标。

   
    <Background>

    ![CleanShot 2024-12-23 at 14.16.43@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/485718/image-preview)
    </Background>


2. 对比修改前后的版本，选择要恢复的版本。

3. 点击 “还原此版本” 按钮。

  
    <Background>

    ![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/485719/image-preview)
    </Background>


:::tip[]
从变更历史恢复会创建新版本，而从回收站恢复则会还原原始版本。
:::

定期备份数据很重要，这样可以防止数据丢失，确保在意外情况下能访问到重要信息。

<!--
## 数据删除解决方案

操作失误在所难免，我们随时提供帮助。系统会保留完整的备份，可以根据需要恢复过去 30 天内任意时间点的数据快照。如果需要恢复数据，请发邮件到 support@apifox.com 联系我们。

-->
