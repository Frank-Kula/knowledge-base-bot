# 添加断言

在我们保存的接口用例中，我们还可以添加 “前置/后置操作” 来获取数据或测试该接口。

<Steps>
  <Step>
切换到 **“后置操作”**。
    </Step>
  <Step>
将鼠标悬停在 **“添加后置操作”** 上，选择 **“断言”**。
<Background>
     <img src="https://api.apifox.com/api/v1/projects/5097254/resources/465555/image-preview" />
</Background>
    </Step>
  <Step>
    在这种情况下，我想要验证响应中的 `id` 是否是一个正整数。

    所以填写 “断言” 表单：

    - **断言名称**: `id` 是正整数
    - **断言对象**: Response JSON
    - **JSONPath 表达式**: `$.data.id`
    - **断言**: 大于 0

    </Step>
  <Step>
点击 **“发送”**，你会在右下角看到断言的结果。
<Background>
![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/465561/image-preview)
</Background>     
    </Step>
  <Step>
点击 “保存” 按钮以保存接口用例。
    </Step>
    <Step>          
        <CardGroup cols={2}>
          <Card title="下一步" href="https://docs.apifox.com/create-test-scenario.md" target="_self">
            新建测试场景
          </Card>
        </CardGroup>
    </Step>
</Steps>


:::tip[]
在 Apifox 中，你可以通过可视化方式[添加断言](https://docs.apifox.com/assertions.md)、[提取变量](https://docs.apifox.com/extract-variables.md)、[执行数据库操作](https://docs.apifox.com/database.md)等。了解更多关于[前置和后置操作](https://docs.apifox.com/pre-post-processors.md)的知识。

你也可以通过添加 “自定义脚本” 来编写断言或实现其它操作。Apifox 支持 Postman 脚本，这些脚本可以在 Apifox 中直接运行而无需修改。了解更多关于[脚本](https://docs.apifox.com/scripts.md)的信息。
:::

