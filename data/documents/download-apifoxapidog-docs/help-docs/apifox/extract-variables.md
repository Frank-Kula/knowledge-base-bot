# 提取变量

Apifox 支持从接口响应中可视化提取值并保存为变量。

## 提取变量

按照以下步骤开始提取变量：


<Steps>
  <Step>
    在运行标签页 *（文档模式）* 或请求标签 *（调试模式）* 中，导航到后置操作。
  </Step>
  <Step>
    悬停在 “添加后置操作” 上并选择 “提取变量”。

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/480040/image-preview)
</Background>

  </Step>
  <Step>
   输入变量名并选择变量类型。
      
选择提取来源，如响应 JSON、响应 XML 或响应文本等。
  </Step>
  <Step>
如果响应是 JSON/XML 格式，你可以使用 [JSONPath/XPath](https://docs.apifox.com/jsonpath.md) 语法解析响应 JSON/XML 的特定部分，并将其保存为变量值。

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/480042/image-preview)
</Background>

  </Step>
  <Step>
发送请求后，变量提取会被执行，你可以在控制台查看日志。

      
<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/480043/image-preview)
</Background>


  </Step>
</Steps>


## 从实际响应中提取变量

想快速从实际响应中提取变量？把鼠标悬停在响应字段上 *（比如在接口响应或自动化测试的测试报告中）* ，然后点击`提取变量`就行了。

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/480144/image-preview)
</Background>

## 提取来源

Apifox 支持从多个数据源提取数据，具体包括：

- **响应文本**：支持用正则表达式提取数据。

- **响应 JSON**：支持用 JSONPath 表达式提取数据。

- **响应 XML**：支持用 XPath 表达式提取数据。

- **响应头**：从响应头名称中提取。

- **响应 cookie**：从 cookie 名称中提取。

- **耗时**：提取请求执行的耗时，用于分析和优化请求响应时间和性能指标。

## JSONPath 提取工具

JSON 是最常用的响应数据格式，而 [JSONPath](https://docs.apifox.com/jsonpath.md) 则是提取 JSON 数据的主流语法。Apifox 提供了可视化的 JSONPath 提取工具，让编写 JSONPath 表达式变得更简单。下面是使用这个工具的具体步骤：

<Steps>
  <Step>
点击 JSONPath 输入框右侧的 <Icon icon="ph-bold-arrow-square-out"/> 图标。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/480148/image-preview)
</Background>

      
  </Step>
  <Step>
在弹出的 [JSONPath](https://docs.apifox.com/jsonpath.md) 提取工具中，左侧显示 JSON 响应。你可以在右上方的 JSONPath 表达式框中输入表达式，下方的结果区域会根据你的表达式动态提取对应的数据。或者可以直接将鼠标悬停在响应字段上进行提取。

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/480149/image-preview)
</Background>

:::tip[]
如果 JSONPath 提取工具的左侧面板为空，需要先发送请求并获取响应，内容才会显示。
:::
  </Step>
  <Step>

如果你的 JSONPath 表达式包含通配符 *（`*`）* 等可能提取多个值的元素，结果会以数组的形式 *（用方括号 `[]` 包裹）* 返回。

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/492478/image-preview)
</Background>

      
      
如果希望提取其中的某个具体值并**去掉数组的方括号**，可以通过开启“**继续提取**”选项，指定一个索引值来直接获取目标值。
      
<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/492479/image-preview)
</Background>


简单来说，“继续提取” 就是为了从提取的数组中选择具体的某个值。
  </Step>
</Steps>
