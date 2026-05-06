# 断言

断言在接口测试中至关重要，它用于校验接口请求的响应是否符合预期。在 Apifox 中，你可以通过可视化界面轻松创建断言，非常的方便。

## 在后置操作里添加断言

<Steps>
  <Step>
    在运行标签页 *（文档模式）* 或请求标签页 *（调试模式）* 中，找到后置操作。
  </Step>
  <Step>
    把鼠标悬停在 “添加后置操作” 上，然后选择 “断言”。

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/480123/image-preview)
</Background>

  </Step>
  <Step>
选择你要断言的对象，可以是接口响应中的各种元素，比如响应头、响应正文或状态码。你可以选择想要校验的特定元素，跟你预期的结果进行对比 *（比如：`$.data.status`）* 。注意，根对象用`$`表示，对象和数组都适用。

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/480129/image-preview)
</Background>

  </Step>

  <Step>
如果断言对象在 JSON 正文中，用 [JSONPath](https://docs.apifox.com/jsonpath.md) 来提取想要的值。
  </Step>
  <Step>
根据你的测试需求设置断言条件。你可以定义各种比较，比如等于、不等于、包含、不包含、大于、小于等。
      
在断言值字段里，你可以输入固定值，或者用`{{变量}}`格式的动态变量。
  </Step>
  <Step>
点击发送按钮执行接口请求。你可以在右侧面板查看断言的结果。

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/480136/image-preview)
</Background>

  </Step>
</Steps>

:::tip[]
在 Apifox 中执行断言时，所有数据都会自动转换为**字符串**进行比较。这虽然简化了大多数情况，但也可能导致一些问题，例如 `4` 不等于 `4.0`。对于需要更精确控制的数据比较，你可以通过[自定义脚本](https://docs.apifox.com/scripts.md)来手动编写断言，解决这些细节问题。
:::

## 基于实际响应设置断言

可以直接在返回响应中 *（接口运行、测试报告等位置均可）* hover 某个响应字段，点击右边的设置断言 icon，即可基于当前的实际响应快速设置断言。

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/480137/image-preview)
</Background>

## 用脚本做断言

在 Apifox 中，你可以使用`pm.test`语法通过脚本创建断言。Apifox 兼容 Postman 脚本，让你可以无缝使用现有脚本。

:::highlight purple
想了解更多关于[脚本](https://docs.apifox.com/scripts.md)的内容。
:::

