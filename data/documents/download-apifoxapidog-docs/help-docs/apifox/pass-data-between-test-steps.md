# 测试步骤间传递数据

在自动化测试场景中，多个测试步骤之间传递数据是很常见的。典型场景包括：
- 测试步骤 1 是登录接口，返回 token；测试步骤 2 使用这个 token 请求其他数据。
- 测试步骤 1 返回一个 ID；测试步骤 2 基于这个 ID 进行操作。
- 测试步骤 1 返回一个列表；测试步骤 2 使用这个列表中的数据。

针对这类场景，Apifox 提供了两种不同的解决方案来处理测试步骤之间的数据传递。你可以根据具体问题选择合适的方案：

1.  **读取前置步骤的运行结果**

    该功能允许你在后续测试步骤中直接使用前一个步骤的结果。
    - 优点：操作简便，无需引入额外变量。
    - 缺点：当数据需要多次引用时，可能会显得繁琐。
    - 注意：该功能仅适用于 “自动化测试” 模块，不能在 “接口管理” 模块中使用。
 
2. **使用变量传递数据**

    在前一个测试步骤的后置操作中，通过 “提取变量” 存储数据，并在后续步骤中引用这些变量。
    
    - 优点：便于在多次引用数据时使用，但对于单次引用来说，可能稍显复杂。
    - 缺点：需要手动管理变量，增加了一些配置的复杂度。
    - 注意：变量可以在 自动化测试 和 接口管理 模块中使用。

## 读取前置步骤的运行结果

我们以一个场景为例，测试步骤 1 是登录接口返回 token，测试步骤 2 使用这个 token 请求其他数据。

<Steps>
  <Step>
把登录接口 *（测试步骤 1）* 添加到测试场景中。
    </Step>
  <Step>
把查询接口 *（测试步骤 2）* 添加到测试场景中。
    </Step>
  <Step>
测试步骤 2 的 “Query 参数” 需要包含测试步骤 1 返回的 token。点击测试步骤 2 “Query 参数” 中 token 字段的魔法棒图标，选择 “读取前置步骤的运行结果”。

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/481623/image-preview)
</Background>

    </Step>
  <Step>
选择从测试步骤 1 获取数据，选择响应体，使用 [JSONPath](https://docs.apifox.com/jsonpath.md) 表达式提取测试步骤 1 返回的 token，比如 `$.token`。

      
<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/481625/image-preview)
</Background>


    </Step>
    <Step>
点击插入，可以看到查询参数中插入了 `{{$.1.response.body.token}}`。

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/481627/image-preview)
</Background>

    
    </Step>
    <Step>
点击测试场景中的 “运行” 按钮，就能成功地把数据从测试步骤 1 传递到测试步骤 2。你可以在测试报告的 “实际请求页” 中查看
        
<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/481629/image-preview)
</Background>


    </Step>
</Steps>

:::tip[]
- “读取前置步骤的运行结果” 功能只能在 “自动化测试” 模块使用，不能在 “接口管理” 模块使用。
- 使用 “读取前置步骤的运行结果” 时，只有运行整个测试场景才能获取到值，单独运行某个步骤是无法获取的。
:::

### 通过变量语法引用前置步骤数据

除了使用 “读取前置步骤的运行结果” 来引用数据，你还可以通过变量语法来实现这一功能。以上文的 `{{$.1.response.body.token}}` 为例：

- 表达式里的 `1` 表示步骤 ID，可以在每个测试步骤中找到。

    <Background>
    <p style="text-align:center">
        <img src="https://api.apifox.com/api/v1/projects/5097254/resources/481632/image-preview" style="width:340px" />
    </p>
    </Background>


- 表达式里的 `response.body` 表示前置步骤数据的位置。可以包括请求的 header、body，或者响应的 header、body 等数据。具体见下文。

    <Background>

    ![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/481633/image-preview)
    </Background>

- 表达式里的 `token` 表示 body 中下一层级的 `token` 字段数据。你可以使用 JSONPath 语法提取想要的数据。

前置步骤数据可以在请求的各个部分使用，比如请求参数、请求头等。你也可以直接把数据插入到请求体中，如下图所示。


<Background>
<p style="text-align:center">
    <img src="https://api.apifox.com/api/v1/projects/5097254/resources/481635/image-preview" style="width:640px" />
</p>
</Background>



要注意的是，如果你需要在脚本中使用前置步骤数据，不能直接用 `{{variable}}` 语法引用变量，而是要使用 `pm.variables.get` 引用前置步骤数据。比如：
```javascript
var token = pm.variables.get("$.1.response.body.token")
```

### 语法参考

<table border="1" cellpadding="1" cellspacing="1" style="border-collapse: collapse; border: none;">
  <thead>
    <tr>
      <th style="vertical-align: middle; text-align: left;">类别</th> 
      <th style="vertical-align: middle; text-align: left;">功能</th>
      <th style="vertical-align: middle; text-align: left;">语法示例</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="6">请求</td>
      <td>URL</td> 
      <td>{{$.&lt;step id>.request.url}}</td>
    </tr>
    <tr>
      <td>路径参数</td>
      <td>{{$.&lt;step id>.request.pathParam.&lt;field name>}}</td> 
    </tr>
    <tr>
      <td>查询参数</td>
      <td>{{$.&lt;step id>.request.query.&lt;field name>}}</td>
    </tr>
    <tr>
      <td>请求头</td>
      <td>{{$.&lt;step id>.request.header.&lt;field name>}}</td>
    </tr>
    <tr>
      <td>请求体（form）</td> 
      <td>{{$.&lt;step id>.request.body.&lt;field name>}}</td>
    </tr>
    <tr>
      <td>请求体（json）</td>
      <td>{{$.&lt;step id>.request.body.&lt;field path>}}</td>
    </tr>
    <tr>
      <td rowspan="3">响应</td>
      <td>响应体</td>
      <td>{{$.&lt;step id>.response.body.&lt;field path>}}</td> 
    </tr>  
    <tr>
      <td>响应头</td>
      <td>{{$.&lt;step id>.response.header.&lt;field name>}}</td>
    </tr>
    <tr>
      <td>Cookie</td>
      <td>{{$.&lt;step id>.response.cookie.&lt;field name>}}</td>
    </tr>
    <tr>
      <td rowspan="2">循环</td>
      <td>元素（ForEach 循环中的数组元素）</td>  
      <td>{{$.&lt;loop step id>.element.&lt;field path>}}</td>
    </tr>
    <tr>
      <td>索引</td>
      <td>{{$.&lt;loop step id>.index}}</td>
    </tr>
  </tbody>
</table>


## 使用变量传递数据

假设有一个测试场景，其中测试步骤 1 是调用登录接口并返回一个 token，而测试步骤 2 则使用这个 token 来请求其他数据。

<Steps>
  <Step>
把登录接口 *（测试步骤 1）* 添加到测试场景中。
    </Step>
  <Step>
在测试步骤 1 的后置操作中，添加一个 “提取变量” 的操作，把 `$.token` 提取为 `{{token}}`。

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/481640/image-preview)
</Background>


:::highlight purple
了解更多[提取变量](https://docs.apifox.com/extract-variables.md)。
:::
    </Step>
  <Step>
把查询接口 *（测试步骤 2）* 添加到测试场景中。

    </Step>
  <Step>
在测试步骤 2 的 Query 参数中引用变量 `{{token}}`。

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/481641/image-preview)
</Background>

    </Step>

    <Step>
点击测试场景中的 “运行”按钮，就能成功地把数据 *（提取出来的 token）* 从测试步骤 1 传递到测试步骤 2。

    </Step>
</Steps>

## 常见问题


<Accordion title="为什么我无法成功引用前置步骤数据？" defaultOpen>
首先，确认你是在 **“自动化测试”** 模块中使用此功能。`“读取前置步骤的运行结果”` 只在自动化测试模块有效，不能在接口管理模块使用。

如果你已经在自动化测试模块，请切换到测试报告，查看具体某个接口的 “实际请求” 标签页，确认请求中引用的前置步骤数据是否已成功填充。

如果实际请求中显示的仍是 `{{$.n.response.body.abc}}` 而非实际数据，说明引用未生效。

常见原因如下：
1. **是否运行了整个测试场景？** 引用前置步骤数据需要运行完整的测试场景才能生效，单独运行某个步骤不会生效。
2. **步骤 ID 是否正确？** 请确保引用的步骤 ID 与目标步骤对应。
3. **JSONPath 是否准确？** 确认使用的 [JSONPath](https://docs.apifox.com/jsonpath.md) 与数据源结构匹配。
</Accordion>


## 了解更多
:::tip[]
如需更详细的操作教程，可以查看我们的最佳实践[《Apifox 测试步骤之间如何传递数据》](https://docs.apifox.com/6822783m0.md)
:::
