# 发送接口请求

当接口创建完成后，即可发起请求。

<Steps>
  <Step>
在 **“文档模式”** 下，切换到 **“运行”** 标签页。
  </Step>
  <Step>
在右上角选择环境为 **“本地 Mock”**。
:::tip[]
发送接口请求时，使用 “本地 Mock” 环境会根据响应结构自动生成数据。

👉 [了解更多 Mock 数据的知识](https://docs.apifox.com/smart-mock.md)
:::
  </Step>
  <Step>
点击 **“发送”** 按钮以发送请求。
  </Step>
  <Step>
你可以在**返回响应**区域查看请求的结果。
<Background>
    <img width="640px" src="https://api.apifox.com/api/v1/projects/5097254/resources/465536/image-preview" />
</Background>
  </Step>
  <Step>
切换到 **“实际请求”** 以查看实际发送的请求。
<Background>
    <img width="640px" src="https://api.apifox.com/api/v1/projects/5097254/resources/465537/image-preview" />

   
</Background>
  </Step>
  <Step>
点击 **“发送”** 按钮右侧的 **“保存为用例”**，可以将此请求保存为接口用例，方便之后直接发起请求或在自动化测试中引用接口用例。
<Background>
    
      <img width="640px" src="https://api.apifox.com/api/v1/projects/5097254/resources/465538/image-preview" />

    
</Background>
  </Step>
      <Step>          
        <CardGroup cols={2}>
          <Card title="下一步" href="https://docs.apifox.com/add-assertions.md" target="_self">
            添加断言
          </Card>
        </CardGroup>
    </Step>
</Steps>



:::tip[]
如果你需要向测试环境、开发环境或生产环境发送接口请求，请将对应服务的 URL 填入右上角环境管理中的 “前置 URL”。了解更多[环境配置](https://docs.apifox.com/environments-and-services.md)的知识。


<Background>
    <img width="640px" src="https://api.apifox.com/api/v1/projects/5097254/resources/465541/image-preview" />
</Background>
    

如果你不想在发送接口请求前定义接口文档，也可以直接使用[快捷请求](https://docs.apifox.com/quick-request.md)。
:::


