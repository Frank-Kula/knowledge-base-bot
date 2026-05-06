# 新建测试场景

当你想要有序地发送一系列请求时，你需要创建一个测试场景。

<Steps>
  <Step>
切换到 **“自动化测试”** 模块，在页面中点击 “**新建测试场景**”，输入一个名称后继续。
      
<Background>

![CleanShot 2025-11-05 at 15.23.33@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/588468/image-preview)
</Background>

    </Step>
  <Step>
鼠标光标悬停在 **“添加步骤”** 上，选择 **“从接口用例导入”**。
    </Step>
  <Step>
按顺序选择以下两个用例：
- a. 新建宠物信息（成功）
- b. 查询宠物详情（已售）

<Background>
    <img src="https://api.apifox.com/api/v1/projects/5097254/resources/465672/image-preview" width="640px"/>
</Background>

    </Step>
  <Step>
现在你可以在界面上看到刚才选择的两个测试用例。目前，我想先添加一个宠物，然后用这个宠物的 ID 获取刚刚添加的宠物信息。

    </Step>
  <Step>
点击 “查询宠物详情 *（已售）*”，你会看到这个接口的参数。如果有引用关系，可以先解除引用，然后在 Path 参数的 `petId` 中，删除原有值，接着点击参数值框中的 <Icon icon="ph-bold-magic-wand"/> **魔法棒** 图标。
<Background>
![CleanShot 2024-09-14 at 14.33.32@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/465680/image-preview)
 </Background>
    </Step>
  <Step>
我现在想从上一步的返回结果中获取刚刚添加的宠物的 ID。选择 **“读取前置步骤的运行结果”**，然后选择之前的测试步骤 “新建宠物信息 *（成功）*”。
      
<Background>
    <img src="https://api.apifox.com/api/v1/projects/5097254/resources/465681/image-preview" style="width:360px"/>
    
</Background> 
    </Step>
  <Step>
点击 [JSONPath](https://docs.apifox.com/jsonpath.md) 表达式右侧的 <Icon icon="ph-bold-arrow-square-out"/> 按钮，你会看到 **JSONPath 提取工具**。在这个工具中，左侧是前一步的返回结果，输入 JSONPath 表达式到右上角，右下角会显示提取的结果。现在在右上角输入 `$.data.id`，你会看到的结果是刚刚添加的宠物的 ID，点击 “确定” 即可保存。
<Background>
      
![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/465683/image-preview)
</Background>
    </Step>
  <Step>
点击 **“插入”** 按钮，表达式会被写入到接口的 Path 参数中。
<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/465690/image-preview)
</Background>
    </Step>
  <Step>
点击右上角的 **“保存”** 按钮，并将环境设置为本地 Mock，然后点击界面右上角的 **“运行”** 按钮。
    </Step>
  <Step>
你可以看到测试报告，点击每个步骤可以展开请求和响应。你会发现第二个请求的路径参数中的 `id` 就是第一个请求返回的宠物 ID。这样，我们就完成了测试步骤 *（接口或接口用例）* 之间的数据传递。
<Background>
![CleanShot 2024-09-14 at 14.45.11@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/465695/image-preview)
</Background>
    </Step>
        <Step>          
        <CardGroup cols={2}>
          <Card title="下一步" href="https://docs.apifox.com/share-api-documentation.md" target="_self">
            分享 API 文档
          </Card>
        </CardGroup>
    </Step>
</Steps>

:::tip[]
一个测试场景包括一系列测试步骤。这些测试步骤可以从[接口或接口用例中导入到测试场景](https://docs.apifox.com/sync-from-endpoint-or-test-case.md)，并可以[在接口文档发生变化时自动或手动更新](https://docs.apifox.com/sync-from-endpoint-or-test-case.md)相应的参数。

测试场景还支持[流程控制条件](https://docs.apifox.com/flow-control-conditions.md)如 If、for、forEach 等。你可以在[测试步骤间传递数据](https://docs.apifox.com/pass-data-between-test-steps.md)、[动态生成请求参数](https://docs.apifox.com/dynamic-values.md)。

基于测试场景，你还可以查看[测试报告](https://docs.apifox.com/test-reports.md)、[运行性能测试](https://docs.apifox.com/performance-testing.md)、[管理测试数据](https://docs.apifox.com/data-driven-testing.md)、[集成 CI/CD](https://docs.apifox.com/cicd.md) 等。
:::

