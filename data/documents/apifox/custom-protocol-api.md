# 通用接口文档

通用接口文档用于管理**自定义协议的接口文档**。

通过该功能，可以为不同类型的协议（如 UDP、Kafka、RabbitMQ、RocketMQ 等）统一建立接口说明，集中管理在 Apifox 中。

通用接口文档与 HTTP 接口文档一样，支持目录树展示、搜索筛选、批量管理、在线分享，方便团队协作与对外展示。


## 新建通用接口文档


<Steps>
  <Step>
    在接口管理中点击 **“新建 -> 通用接口文档”**。
      
<Background>

![CleanShot 2025-11-05 at 16.43.31@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/588575/image-preview)
</Background>

  </Step>
  <Step>
    选择协议类型（可选 Thrift、Kafka 等，或点击 **“管理协议”** 添加自定义协议）。
      
<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/577227/image-preview)
</Background>

协议里会有一些默认模版供选择。
  
<Background>
<img src="https://api.apifox.com/api/v1/projects/5097254/resources/577230/image-preview" style="width: 360px;" />  
    
![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/577232/image-preview)

</Background>

      
  </Step>
  <Step>
    填写以下信息：

   * **唯一标识**：接口的唯一 ID，用于区别不同接口（和 HTTP 接口里的 URL 路径类似）。
   * **接口名称**：接口的中文或英文名称。
   * **基本信息**：状态、标签、责任人等基本信息。
   * **文档详情**：支持 **Markdown** 格式，灵活编写接口描述、使用说明、示例等内容。
      
<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/577297/image-preview)
</Background>

  </Step>
    
    
      <Step>
    保存后，即可看到该协议的接口文档。
<Background>
![CleanShot 2025-09-26 at 13.55.32@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/577300/image-preview)
</Background>

  </Step>

    
</Steps>


## 分享通用接口文档

通用接口文档同样支持“在线分享”，方便团队协作与对外展示。

可以复制“协作链接”以在项目内协作。


<Background>
![CleanShot 2025-09-26 at 14.00.00@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/577302/image-preview)
</Background>

也可以在“分享文档 -> 快捷分享”中，圈选接口的分享范围，选择是否分享通用接口文档。
<Background>

![CleanShot 2025-09-26 at 14.02.09@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/577307/image-preview)
</Background>

