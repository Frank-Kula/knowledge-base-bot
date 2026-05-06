# 消息通知


Apifox 支持在执行某些特定操作时，触发生成一条通知信息给指定的对象。


可以通过将通知集成到第三方应用平台，当项目成员触发对应的通知事件时，将通知实时发送到第三方应用平台，如飞书群聊机器人；也可通过 Webhook 或邮件等渠道进行通知。目前已支持的通知渠道有：
- 企业微信
- 钉钉
- 飞书
- Teams
- Webhook
- Jenkins
- Email

仅项目管理员可以设置项目的通知设置。目前通知对象中为邮件渠道的，仅支持 **自动化测试运行完成、持续集成运行完成、定时任务运行完成** 这三种类型的操作使用。

<Background>

![CleanShot 2025-06-10 at 10.41.24@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/532943/image-preview)
</Background>

