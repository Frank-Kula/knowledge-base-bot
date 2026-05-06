# SSE 调试

SSE *（Server-Sent Events）* 是一种基于 HTTP 协议的实时通信技术，广泛应用于 AI 大模型的流式响应场景。它通过建立客户端和服务器之间的持久单向连接，使服务器能够向客户端推送实时消息，让用户即时看到 AI 的思考过程和生成内容。


<Tabs>
  <Tab title="DeepSeek R1">
    <Embed src="//player.bilibili.com/player.html?isOutside=true&aid=114029334896304&bvid=BV1EUA6eVENk&cid=28468184412&p=1" width="720px" height="405px" />
  </Tab>
  <Tab title="Ollama 本地部署的 QwQ-32B">
        <Embed src="//player.bilibili.com/player.html?isOutside=true&aid=114142262334534&bvid=BV1jSRnYaEUa&cid=28804644874&p=1" width="720px" height="405px" />
  </Tab>
</Tabs>

## 发起 SSE 连接

> Apifox 版本需大于 `2.3.10`


<Steps>
  <Step title="新建接口">
    在 Apifox 中新建一个 HTTP 项目，并在项目中新建 HTTP 接口，填写 AI 模型的接口地址。
      
<Background>

![CleanShot 2025-12-30 at 14.04.18@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/608772/image-preview)
</Background>

  </Step>
  <Step title="设计 SSE 接口（可选）">
    设计 API 时，支持将响应类型配置为 SSE（`text/event-stream`），并可按 SSE 规范设计流式返回结构，
  为 `string` 类型字段配置 Content Schema，用于描述每个事件中实际返回的数据格式。
     
<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/608775/image-preview)
</Background>

  </Step>
  <Step title="发送请求">
    发送请求后，当接口返回的 `Content-Type` 包含 `text/event-stream` 时，Apifox 会自动将返回的数据解析为 SSE 事件。
      
<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/498888/image-preview)
</Background>

  </Step>
  <Step title="查看实时响应">
      可在响应面板的「时间线」视图中查看实时消息内容，支持自然语言展示响应。
      
<Background>

![apifox-deepseek-api-01.gif](https://api.apifox.com/api/v1/projects/5097254/resources/495408/image-preview)
</Background>

  </Step>
</Steps>


## 消息自动合并

> Apifox 版本需大于 `2.7.14`

Apifox 内置了对主流 AI 模型的支持，可以自动识别并合并以下格式的流式响应：

- 兼容 OpenAI API 格式的响应 *（DeepSeek、豆包、通义千问、腾讯混元、文心一言等绝大多数 AI 模型的 API 都兼容该格式）*
- 兼容 Gemini API 格式的响应
- 兼容 Claude API 格式的响应
- 兼容 Ollama API 格式的响应 *（使用 Ollama 本地部署的 AI 模型使用该格式）*

只要你调用的 AI 模型返回格式与以上任一种格式相匹配，Apifox 都会自动将消息片段合并为完整的回复内容。自动合并消息内容后，可以预览 Markdown 格式的内容。

<Background>

![apifox-sse.gif](https://api.apifox.com/api/v1/projects/5097254/resources/528182/image-preview)
</Background>


对于某些特殊模型，如 DeepSeek R1、QwQ-32B，Apifox 还支持在时间线中展示模型的思考过程，让你更直观地了解 AI 的推理过程。

<Background>

![apifox-deepseek-api-02.gif](https://api.apifox.com/api/v1/projects/5097254/resources/495431/image-preview)
</Background>



## 自定义合并规则

如果自动合并功能未能正常工作，可以根据实际情况采取以下措施：

### 1. 配置 JSONPath 提取规则

当 SSE 返回的事件内容是 **JSON 格式**，但不符合 OpenAI、Gemni、Claude 等内置的识别规则时，你可以手动配置 [JSONPath](https://docs.apifox.com/jsonpath.md) 来提取所需内容。例如下面的原始 SSE 响应 *（经过格式化）*：


```json

data: {
        "choices": [
            {
                "delta": {
                    "content": "大",
                    "role": "assistant"
                },
                "index": 0
            }
        ],
        "created": 1740637581,
        "model": "deepseek-r1-250120"
      }

data: {
        "choices": [
            {
                "delta": {
                    "content": "白菜",
                    "role": "assistant"
                },
                "index": 0
            }
        ],
        "created": 1740637581,
        "model": "deepseek-r1-250120"
      }
```

对于这个 JSON 结构，要提取 content 字段的内容，正确的 JSONPath 配置应是：

`$.choices[0].delta.content`

这个 JSONPath 表达式的含义是：
- `$` 表示 JSON 的根节点
- `choices[0]` 表示选择 choices 数组的第一个元素
- `delta.content` 表示在该元素下 delta 对象的 content 属性

这个配置将提取出内容：
```
大白菜
```

将 JSONPath 表达式填入「自动合并」右侧的输入框中即可。

<Background>

![CleanShot 2025-02-27 at 18.19.21@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/498889/image-preview)
</Background>


### 2. 使用后置脚本处理

对于**非 JSON 格式**的 SSE 消息，可以：

- 使用[后置脚本](https://docs.apifox.com/post-request-scripts.md)手动处理。
- 联系[技术支持](https://docs.apifox.com/contact-us.md)反馈你使用的模型格式，我们会考虑添加对该格式的内置支持。


例如某个 AI 接口返回的 SSE 消息是纯文本格式，而不是 JSON 数据。每个事件片段可能只是一些简单的文本行，例如：

```js
data: 你
data: 好
```
在 Apifox 中，你可以编写如下自定义脚本来处理这些文本数据：


```js
// 获取返回的 SSE 事件流内容
const sseContent = pm.response.text();

// 假设每行文本代表一个事件片段，我们可以简单地按行分割并处理
const eventLines = sseContent.split('\n');

// 存储合并后的事件内容
let mergedContent = '';

// 处理每个事件片段，去除空行并合并
eventLines.forEach(line => {
    if (line.trim()) {
        // 提取 'data: ' 后面的内容并合并
        let eventData = line.replace(/^data:\s*/, '');
        mergedContent += eventData;
    }
});

// 将结果显示在 body 的 "Visualize" 标签页
pm.visualizer.set(mergedContent);
// 最后，将合并后的数据输出
console.log("合并后的事件流：", mergedContent);
```

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/498892/image-preview)
</Background>


这个脚本将会把每个事件片段按行分割，将处理后的内容显示在 body 的 "Visualize" 标签页，并打印到控制台。你可以根据实际需要进一步修改处理逻辑，进行更复杂的文本解析。


:::tip[]
无论选择哪种方式，都建议先仔细分析 API 的响应格式，以确保正确配置合并规则。
:::

## 常见问题

<Accordion title="SSE 时间线没有显示消息，如何处理？" defaultOpen>

如图所示的问题：

<Background>
<img alt="SSE FAQ" src="https://api.apifox.com/api/v1/projects/5097254/resources/469979/image-preview" width="500px" />
</Background>

这通常是因为服务器返回的响应内容不符合 SSE 格式规范。标准的 SSE 消息格式要求：
- 消息内容需要放在 `data:` 之后
- 每条消息之间要用两个换行符分隔（即消息之间空一行）

详细的 SSE 消息格式说明请参考[《MDN 文档 - 使用服务器发送事件》](https://developer.mozilla.org/zh-CN/docs/Web/API/Server-sent_events/Using_server-sent_events)。

</Accordion>

## 了解更多

<Card title="如何调用 DeepSeek API（R1 & V3）？" href="https://apifox.com/apiskills/deepseek-api-debugging/">
获取 DeepSeek API 密钥并调试 API 的完整指南
</Card>

