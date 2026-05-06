# Webhook 调试

Webhook 是一种用于**接收事件通知的 HTTP 接口**。当某个特定事件发生后，系统会主动向预设的地址（即 Webhook URL）发送 HTTP 请求，通常用于通知外部系统相关状态的变更或异步处理结果。

常见使用场景包括：

- 支付平台通知订单支付结果；

- 第三方登录服务推送登录状态；

- 异步任务完成后推送处理结果。


虽然从技术上看，Webhook 本质上就是一个 HTTP 接口，但它的使用方式是**由系统主动请求外部地址**，与普通接口 “由使用者调用系统” 的方向恰好相反。


## 新建 Webhook 接口


<Steps>
  <Step>
    在 Apifox 项目中，点击项目左侧的`+`按钮，选择 “新建 Webhook” 接口。
      
<Background>

![CleanShot 2025-11-05 at 16.50.34@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/588591/image-preview)
</Background>

  </Step>
  <Step>
    新建后，在编辑界面填写以下信息：
    - **请求方式：** 一般为 `POST`
    - **Webhook Name**：Webhook 名称，会显示在接口文档中，导出 OpenAPI 文件时也会作为接口标识使用，例如：`order`
    - **调试 URL（可选）**：用于发送测试请求的实际地址，只用于调试，**不会出现在接口文档中**。
    - **其他信息：** 如请求 Body 等

<Background>

![CleanShot 2025-07-16 at 12.10.34@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/546090/image-preview)
</Background>

  </Step>
  <Step >
    相关信息填写后保存即可
  </Step>
</Steps>



## 调试 Webhook 接口

Webhook 调试的目的是模拟事件触发，验证外部服务是否能正常接收到请求。

将 Webhook URL 填写到地址栏的 “调试 URL” 中，然后点击 “发送” 按钮，即可模拟 Webhook 调用。

<Background>

![CleanShot 2025-07-16 at 12.18.55@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/546094/image-preview)
</Background>


## Webhook 接口文档

Webhook 接口会在文档中展示接口名称、请求方式、请求体结构等信息，用于告诉使用者：系统在某个事件发生时，会向指定地址发送什么内容。

“调试 URL” 不会出现在接口文档中，只用于测试用途。

在导出的 OpenAPI 文件中，Webhook 接口会出现在 `webhooks` 字段中，与普通接口的 `paths` 字段区分开。

<Background>

![CleanShot 2025-07-16 at 12.29.01@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/546098/image-preview)
</Background>



## 常见问题


<Accordion title="为什么推荐 Webhook 在文档中单独定义？" defaultOpen>
在 OpenAPI 3.1 规范中，普通接口通过 `paths` 字段描述，而 Webhook 类型接口则需要通过 `webhooks` 字段单独定义。这样做是为了清晰地区分：

* **普通接口：** 由外部调用，用于发起操作或查询；
* **Webhook 接口：** 由系统触发，用于推送通知或回调结果。

因此，在 Apifox 中，Webhook 可以被**作为一种独立的接口类型进行定义**，以更准确地表达接口的行为方向，并确保导出的 OpenAPI 文件结构符合规范要求。

**示例对比：**

```yaml
paths:
  /orders:
    get:
      summary: 获取订单列表
      responses:
        '200':
          description: 成功响应

webhooks:
  orderPaid:
    post:
      summary: 支付成功回调通知
      requestBody:
        content:
          ...
```

* `/orders` 是一个普通接口，供使用者调用。
* `orderPaid` 是一个 Webhook，表示当订单支付成功时，系统会发送通知请求，调用外部提供的 URL。


</Accordion>


<Accordion title="Webhook 是不是普通接口？" defaultOpen={false}>
Webhook 就是 “HTTP 形式的回调”，用于不同系统之间通过网络通知结果。本质是回调，实质是系统之间的事件通知机制。
    
由于调用方向和使用场景完全不同，OpenAPI 3.1 规范建议将其单独定义。在 Apifox 中也做了区分，以便更好地组织接口文档和支持 Webhook 测试。
</Accordion>


<Accordion title="调试 URL 会出现在接口文档中吗？" defaultOpen={false}>
不会。调试 URL 仅用于调试，文档展示和 OpenAPI 导出中不会包含该项。
</Accordion>





