# 通知

Apifox 的通知功能主要分为两大板块：**个人账号通知** 和 **项目级消息通知**。

个人账号通知（位于右上角设置中）专注于与你直接相关的互动，例如接口评论中的`@`提及、回复等，通过站内信和邮件提醒你处理。


而项目级消息通知（位于项目设置中）则服务于团队协作，可将接口变更、测试结果等关键事件自动推送到第三方平台（如飞书、钉钉群机器人），实现团队信息同步自动化。

本文介绍的是个人账号通知，**项目级消息通知请查看[「通知设置 - 消息通知」](https://docs.apifox.com/message-notifications)** 文档。

## 如何开启通知

<Steps>
  <Step>
    点击界面右上角的“设置图标”，选择「通知」选项
      
<Background>

![CleanShot 2025-09-10 at 17.08.20@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/572350/image-preview)
</Background>

  </Step>
  <Step>
    分别配置「站内信」和「邮件」通知偏好：
   - 使用复选框选择你希望接收通知的事件类型
   - 点击「全选」可一次性选择所有事件
   - 取消勾选则不再接收该类事件的通知
      
      
<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/572375/image-preview)
</Background>

  </Step>
</Steps>


## 通知类型

### 站内信通知

当触发指定事件时，系统会给你推送一条新通知。例如：

<Background>
<img style="width: 460px;" src="https://api.apifox.com/api/v1/projects/5097254/resources/572273/image-preview"/>
</Background>


### 邮件通知
当触发指定事件时，系统会向你绑定的邮箱发送一封通知邮件。例如：

<Background>
<img style="width: 460px;" src="https://api.apifox.com/api/v1/projects/5097254/resources/572272/image-preview"/>
</Background>

## 可配置的触发事件

以下事件可供你选择接收通知：

- **我负责的资源有新评论**：当你负责的接口、文档等资源收到新评论时
- **我创建的资源有新评论**：当你创建的接口、文档等资源收到新评论时  
- **被提及**：当其他用户在评论中`@`你时
- **被回复**：当其他用户回复你的评论时
- **被解决**：当你提出的问题被标记为已解决时


建议至少开启一种通知方式，确保重要信息不被遗漏，对于需要及时响应的关键事件（如被提及），建议同时开启站内信和邮件通知。

