# Apifox 中定制化 LLM 二次封装响应

当你的 LLM 经过二次封装，返回结构与原始模型（如 OpenAI/Gemini/Claude）不一致时，Apifox 仍可支持**定制化输出**，主要有两种方式。

---

## 方式一：配置 JSONPath 提取规则（推荐，适用于 JSON 格式 SSE）

若你的封装接口返回的是 **JSON 格式的 SSE**（每行 `data: {...}`），但字段路径与内置格式不同：

1. 在 Apifox 中打开该接口，发送一次请求，确认响应为 `Content-Type: text/event-stream`。
2. 在响应区域的 **「自动合并」** 右侧找到 **JSONPath 输入框**。
3. 根据你的实际响应结构，填写用于提取「最终展示内容」的 **JSONPath**。

**示例：**

- 若每块 SSE 为：`data: {"result":{"text":"你"}}`，则 JSONPath 可填：`$.result.text`
- 若为：`data: {"choices":[{"delta":{"content":"好"}}]}`（类 OpenAI），则填：`$.choices[0].delta.content`
- 若为：`data: {"answer":"大"}`（文档示例中的字段），则填：`$.answer`

保存后，Apifox 会按该路径从每条 SSE 中取出内容并自动合并，在时间线/合并结果中展示。

参考：[Apifox 官方 - SSE 自定义合并规则（JSONPath）](https://docs.apifox.com/sse.md#1-配置-jsonpath-提取规则)

---

## 方式二：后置操作 + 自定义脚本（任意结构 / 非 JSON）

当响应是**非 JSON**，或结构复杂、需要先做转换再展示时，用**后置操作里的自定义脚本**做定制化解析，并用 `pm.visualizer.set()` 控制「可视化」标签页的展示内容。

### 操作步骤

1. 打开接口 → **后置操作** → **添加后置操作** → 选择 **「自定义脚本」**。
2. 在脚本中：
   - 用 `pm.response.text()` 拿到原始 SSE 文本；
   - 按你的封装格式解析（例如按行拆分、取 `data:` 后内容、再按自定义字段拼接）；
   - 将最终要展示的字符串或 HTML 通过 **`pm.visualizer.set(内容)`** 输出到响应的 **「可视化」** 标签页。

### 示例 1：自定义 JSON 结构（例如字段为 `payload.content`）

```js
const text = pm.response.text();
const lines = text.split('\n');
const parts = [];

for (let i = 0; i < lines.length; i++) {
  const line = lines[i];
  if (!line.startsWith('data:')) continue;
  try {
    const data = JSON.parse(line.substring(5).trim());
    // 按你的二次封装结构取内容，例如：
    if (data.payload && data.payload.content) {
      parts.push(data.payload.content);
    }
    // 若有其他结构，例如 data.reply 或 data.chunk，可改为：
    // if (data.reply) parts.push(data.reply);
  } catch (e) {}
}

const result = parts.join('');
pm.visualizer.set(result);
console.log(result);
```

### 示例 2：纯文本 SSE（每行 `data: 某段文字`）

```js
const sseContent = pm.response.text();
const eventLines = sseContent.split('\n');
let mergedContent = '';

eventLines.forEach(line => {
  if (line.trim()) {
    const eventData = line.replace(/^data:\s*/, '');
    mergedContent += eventData;
  }
});

pm.visualizer.set(mergedContent);
console.log('合并后内容：', mergedContent);
```

### 示例 3：需要渲染为 HTML（如 Markdown 转展示）

可结合 Handlebars 模板，把解析后的数据传入「可视化」：

```js
const result = parts.join('');  // 上面解析得到的完整文本
const template = `<pre style="white-space: pre-wrap;">{{content}}</pre>`;
pm.visualizer.set(template, { content: result });
```

只要在脚本里把**你的封装结构**解析成最终字符串或数据，再交给 `pm.visualizer.set()`，即可在 Apifox 里实现**完全定制化的响应展示**。

---

## 小结

| 场景                     | 建议方式                         |
|--------------------------|----------------------------------|
| SSE 为 JSON，字段路径固定 | **方式一**：JSONPath 提取规则    |
| 结构复杂或非 JSON        | **方式二**：后置脚本 + `pm.visualizer.set()` |

因此，**Apifox 可以支持定制化输出**：要么通过 JSONPath 适配你的封装字段，要么通过后置脚本按任意结构解析并设置可视化内容。若你提供一份实际 SSE 响应示例（几条 `data:` 行），可以据此写出对应的 JSONPath 或脚本片段。

---

## 参考文档

- [Apifox - SSE 调试](https://docs.apifox.com/sse.md)（含 JSONPath 与后置脚本说明）
- [Apifox - 后置脚本](https://docs.apifox.com/post-request-scripts.md)
- [Apifox - 响应数据可视化](https://docs.apifox.com/response-data-visualization.md)（`pm.visualizer.set` 用法）
- [Apifox - 如何计算 AI 问答成本](https://docs.apifox.com/5835636m0.md)（含 SSE 拼接与可视化示例）
