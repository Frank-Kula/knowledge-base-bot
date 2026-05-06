# 通知对象



通过创建通知对象，来让某些特定操作触发时，以指定的渠道和设置来进行通知。通知对象中包含对象名称、通知渠道以及渠道内的具体配置。因为通知渠道之间的配置差异较大，以下分渠道来介绍具体的配置方法。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/485391/image-preview)
</Background>


## 企业微信

支持发送通知事件到企业微信群聊机器人，通过在企业微信中`开启群聊机器人`，配置群聊机器人的 Webhook URL，可以将事件消息发送到企业微信群聊。

<br />

**配置字段说明**

| **配置字段** | **是否必填** | **说明**                           |
| ------------ | ------------ | ---------------------------------- |
| 名称         | 是           | 标明该通知对象的特点               |
| 服务 URL     | 是           | 企业微信群聊机器人中的 Webhook URL |

<br />

**绑定企业微信群聊机器人**

项目管理员可使用第三方集成功能，将企业微信群聊机器人与 Apifox 中的项目通知事件关联，以实现在企业微信群聊中推送相关的接口变更、文档变更、自动化测试完成等通知。

1. 在「电脑端 -> 企业微信」应用的群聊的聊天信息设置中，点击`添加群机器人`。


    <Background>

    ![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/485392/image-preview)
    </Background>


2. 复制 Webhook 地址：

 
    <Background>

    ![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/485393/image-preview)
    </Background>


3. 将 Webhook 粘贴到通知对象中点击保存后，即完成绑定。

<br />

当选择的事件被触发时，将在企业微信群聊中收到通知。

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/485394/image-preview)
</Background>


## 钉钉

支持发送通知事件到钉钉群聊机器人，通过在钉钉中`开启群聊机器人`，配置群聊机器人的 Webhook URL，可以将事件消息发送到钉钉群聊。

<br />

**配置字段说明**

| **配置字段** | **是否必填** | **说明**                                                                 |
| ------------ | ------------ | ------------------------------------------------------------------------ |
| 名称         | 是           | 标明该通知对象的特点                                                     |
| 服务 URL     | 是           | 钉钉群聊机器人中的 Webhook URL                                           |
| 加签密钥     | 否           | 创建钉钉群聊机器人时，可自动生成机器人的签名，若开启签名，请输入签名内容 |

<br />

**绑定钉钉群聊机器人**

项目管理员可使用第三方集成功能，将钉钉群聊机器人与 Apifox 中的项目通知事件关联，以实现在钉钉群聊中推送相关的接口变更、文档变更、自动化测试完成等通知。

1. 在「电脑端 -> 钉钉应用」的群设置中，点击智能群助手，并添加`自定义机器人`。


    <Background>

    ![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/485395/image-preview)


    ![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/485396/image-preview)
    </Background>


     在弹出的界面中，选择“自定义”机器人。
 

    <Background>

    ![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/485397/image-preview)
    </Background>

2. 配置`安全设置`，如加签：
 

    <Background>

    ![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/485398/image-preview)
    </Background>


3. 完成后，设置 Webhook：


    <Background>

    ![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/485399/image-preview)
    </Background>


4. 将 Webhook 、密钥粘贴到通知对象中点击保存后，即完成绑定。

<br />

当选择的事件被触发时，将在钉钉群聊中收到通知：


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/485400/image-preview)
</Background>



## 飞书

支持发送通知事件到飞书群聊机器人，通过在飞书中`开启群聊机器人`，配置群聊机器人的 Webhook URL，可以将事件消息发送到飞书群聊。

<br />

**配置字段说明**

| **配置字段** | **是否必填** | **说明**                                                                 |
| ------------ | ------------ | ------------------------------------------------------------------------ |
| 名称         | 是           | 标明该通知对象的特点                                                     |
| 服务 URL     | 是           | 飞书群聊机器人中的 Webhook URL                                           |
| 加签密钥     | 否           | 创建飞书群聊机器人时，可自动生成机器人的签名，若开启签名，请输入签名内容 |

<br />

**绑定飞书群聊机器人**

项目管理员可使用第三方集成功能，将飞书群聊机器人与 Apifox 中的项目通知事件关联，以实现在飞书群聊中推送相关的接口变更、文档变更、自动化测试完成等通知。

1. 在「电脑端 -> 飞书应用」的群聊设置中，点击`群机器人`，并点击`添加机器人`。

 
    <Background>

    ![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/485401/image-preview)

    ![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/485402/image-preview)
    </Background>


2. 选择`自定义机器人`并添加。


    <Background>

    ![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/485403/image-preview)
    </Background>


3. 复制 Webhook 地址：
 

    <Background>

    ![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/485404/image-preview)
    </Background>


4. 若启用了签名校验，复制`签名`：

    <Background>

    ![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/485405/image-preview)
    </Background>


5. 将 Webhook 、密钥粘贴到通知对象中点击保存后，即完成绑定。

<br />

点击保存后，即完成绑定。当选择的事件被触发时，将在飞书群聊中收到通知：


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/485406/image-preview)
</Background>

## Teams

支持发送通知到 Microsoft Teams，让 Teams 中的 [Workflow](https://support.microsoft.com/en-us/office/create-incoming-webhooks-with-workflows-for-microsoft-teams-8ae491c7-0394-4861-ba59-055e33f75498) 使用此消息作为 Trigger 来做下一步工作，例如在社群或频道中创建新的帖子，从而及时了解到 Apifox 的事件通知。

<br />

具体来说，你可以配置一个 Workflow 中的 Webhook Trigger，当 Apifox 中指定的某些通知事件（如接口变更、文档变更或自动化测试完成等）被触发时，Apifox 会向这个 Trigger 中的 HTTP POST URL 发送 POST 请求，携带事件消息。

<br />

**配置字段说明**

| **配置字段** | **是否必填** | **说明**                                                                                                                                                    |
| ------------ | ------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 名称         | 是           | 标明该通知对象的特点                                                                                                                                        |
| HTTP POST URL     | 是           | Workflow 中 Webhook Trigger 接收请求的 URL 地址                                                                                                            
<br />


**使用 Workflow 功能将 Apifox 中的消息创建帖子到频道中**

1. 在「Microsoft Teams -> Workflow」中，点击`创建`，并可以直接点击`Post to a channel when a webhook request is received`从此模板中快速创建。


<Background>
![CleanShot 2025-03-13 at 14.56.06@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/502466/image-preview)
</Background>


2. 设置好 flow 的名称和选择正确的账号后，点击`Next`


<Background>
![CleanShot 2025-03-13 at 15.00.34@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/502469/image-preview)
</Background>


3. 选择需要收到通知的社群与频道，并点击`Create flow`


<Background>
![CleanShot 2025-03-13 at 15.02.39@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/502471/image-preview)
</Background>


4. Flow 创建成功后，会展示此 flow 中 Trigger 下的 HTTP POST URL，可以直接点击复制。当然也可后续在 flow 中找到 Trigger 步骤内的此 HTTP POST URL。


<Background>
![CleanShot 2025-03-13 at 15.04.16@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/502473/image-preview)

    ![CleanShot 2025-03-13 at 15.11.06@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/502477/image-preview)
</Background>




5. 将 Workflow 中的 HTTP POST URL 粘贴在 Apifox 新创建的`通知对象`中。



<Background>
![CleanShot 2025-06-10 at 10.48.01@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/532945/image-preview)
</Background>



6. 设置一个`通知事件`并关联此 Teams 通知对象


<Background>

![CleanShot 2025-06-10 at 10.50.45@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/532946/image-preview)
</Background>


7. 当此通知事件被触发，则会通过上述流程中创建好的 Workflow 自动向指定频道中创建一条帖子。


<Background>
![CleanShot 2025-03-13 at 15.16.37@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/502482/image-preview)
</Background>



## Webhook

你的 HTTP 服务器可以作为一个 Webhook 接收器，接收来自 Apifox 的事件通知。

<br />

具体来说，你可以配置一个 HTTP 服务器的 URL 地址，当 Apifox 中指定的某些通知事件（如接口变更、文档变更或自动化测试完成等）被触发时，Apifox 会向这个 URL 发送 POST 请求，携带事件消息。

<br />

**配置字段说明**

| **配置字段** | **是否必填** | **说明**                                                                                                                                                    |
| ------------ | ------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 名称         | 是           | 标明该通知对象的特点                                                                                                                                        |
| 服务 URL     | 是           | HTTP 服务器接收请求的 URL 地址                                                                                                                              |
| 签名令牌     | 否           | 使用 [HMAC SHA1](https://en.wikipedia.org/wiki/HMAC) 加密算法，以令牌作为密钥对发送内容加密，并以十六进制显示结果（配置令牌时生效），消息将包含前缀 `sha1=` |

<br />


举个例子，假如你的服务端有一个名为 `POST http://127.0.0.1:8080/webhook` 的 API 可接收入参，你可以将这个路径配置到 Apifox 中，如果有加密密钥，也一并填入，配置完毕后保存即可。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/485407/image-preview)
</Background>


现在，你可以在 Apifox 项目中做一些操作，以测试是否成功。当事件被触发时，Apifox 将发送类似以下的信息到指定的服务端 URL ：

```json
{
  "event": "API_UPDATED",
  "title": "接口修改提醒",
  "content": "所在团队：A 项目团队  \n所在项目：宠物商店  \n迭代分支名称：main  \n接口名称：获取顾客信息  \n接口路径：GET /user/208010884  \n状态：开发中  \n责任人：--  \n  \n修改者：Ring  \n修改时间：2024-05-13 23:40:36"
}
```
服务端拿到这些信息后，可以将其美化展示。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/485408/image-preview)
</Background>




## Jenkins

支持发送通知事件到 Jenkins 服务，通过配置 Jenkins 的 Webhook URL，可以将事件消息发送到 Jenkins。

<br />

**配置字段说明**

| **配置字段** | **是否必填** | **说明**                                                                                                                         |
| ------------ | ------------ | -------------------------------------------------------------------------------------------------------------------------------- |
| 名称         | 是           | 标明该通知对象的特点                                                                                                             |
| 服务 URL     | 是           | Jenkins [Generic Webhook Trigger](https://plugins.jenkins.io/generic-webhook-trigger/) 插件中配置的URL                           |
| 签名令牌     | 否           | 将通过请求头 Authorization Bearer 方式发送给 [Generic Webhook Trigger](https://plugins.jenkins.io/generic-webhook-trigger/) 插件 |


1. 在插件市场搜索“Generic Webhook Trigger”插件，安装即可，安装完毕重启 Jenkins 服务。
 

    <Background>

    ![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/485409/image-preview)
    </Background>


2. 在 Jenkins-Dashboard 中新建一个视图：


    <Background>

    ![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/485410/image-preview)
    </Background>


3. 点击进入上一步创建的视图，进入「Configure -> Build Triggers」，选择 `Generic Webhook Trigger`。Webhook URL 即 `http://{{您的服务器地址}}/generic-webhook-trigger/invoke`。
 

    <Background>

    ![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/485411/image-preview)
    </Background>


4. 支持自定义 Token：


    <Background>

    ![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/485412/image-preview)
    </Background>


5. 将 Webhook URL、Token 粘贴到通知对象中点击保存后，即完成绑定。

<br />

点击保存后，即完成绑定。当选择的事件被触发时，将自动触发 Jenkins 发起一次构建行为，并在构建历史记录中查看消息：


<Background>
 
![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/485413/image-preview)
</Background>




## Email

支持通过邮件方式发送通知邮件到指定邮箱中。目前通知对象中为邮件渠道的，仅支持 自动化测试运行完成、持续集成运行完成、定时任务运行完成 这三种类型的操作使用。

<br />

**配置字段说明**

| **配置字段** | **是否必填** | **说明**                                                                                                               |
| ------------ | ------------ | ---------------------------------------------------------------------------------------------------------------------- |
| 名称         | 是           | 标明该通知对象的特点                                                                                                   |
| 通知邮箱地址 | 是           | 点击即可输入希望接受通知的邮箱地址。可以快速选择项目成员的邮箱地址，也可以手动输入一个邮箱地址。能够输入多个邮箱地址。 |

<br />

输入邮箱完成并点击保存后，即完成设置。当选择的事件被触发时，将在邮箱中收到通知：


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/485414/image-preview)
</Background>



