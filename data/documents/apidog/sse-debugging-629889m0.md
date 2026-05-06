# SSE Debugging

Server-Sent Events (SSE) is a real-time communication technology built upon the HTTP protocol, enabling servers to push updates to clients over a persistent, one-way connection. SSE is commonly used for streaming AI model responses, live notifications, and real-time data feeds.

With SSE, users can instantly see the thought process of reasoning models and generated content as it streams from the server.

## Prerequisites

- Apidog version 2.3.10 or later
- An HTTP endpoint that returns `Content-Type: text/event-stream`

## Initiating an SSE Connection

<Steps>
  <Step title="Create a New Endpoint">
    In Apidog, create a new HTTP project, add a new endpoint, and enter the URL for the AI model's endpoint or SSE server.
  </Step>
  <Step title="Send the Request">
    Upon sending the request, if the response header `Content-Type` includes `text/event-stream`, Apidog automatically parses the returned data as SSE events.
  </Step>
  <Step title="View Real-time Responses">
    View real-time messages in the **Timeline** view of the response panel, where content is displayed in natural language format.
  </Step>
</Steps>

<Background>
![sse-timeline-auto-merge.gif](https://api.apidog.com/api/v1/projects/544525/resources/350377/image-preview)
</Background>

## Auto-Merge Messages

:::info[Version Requirement]
Apidog version 2.7.14 or later required for auto-merge functionality.
:::

Apidog includes built-in support for popular AI models and automatically recognizes and merges streaming responses in the following formats:

| Format | Description |
|--------|-------------|
| **OpenAI API Compatible** | Used by the vast majority of AI model providers |
| **Gemini API Compatible** | Google's Gemini model format |
| **Claude API Compatible** | Anthropic's Claude model format |
| **Ollama API Compatible** | JSON Streaming (NDJSON) format for locally deployed AI models |

When the AI model's response matches any of these formats, Apidog automatically merges message fragments into a complete reply, with content previewed in Markdown format.

<Background>
![apidog-sse-1.gif](https://api.apidog.com/api/v1/projects/544525/resources/355512/image-preview)
</Background>

### Reasoning Model Support

For certain models, such as **DeepSeek R1**, Apidog displays the model's thought process in the timeline, providing a clearer, more intuitive view of AI reasoning.

<Background>
![apidog-sse-2.gif](https://api.apidog.com/api/v1/projects/544525/resources/355513/image-preview)
</Background>

## Customizing Merge Rules

If the **Auto-Merge** feature does not work properly, you can configure custom extraction rules based on your specific use case.

### Configure JSONPath Extraction Rules

When SSE returns JSON content that doesn't conform to built-in recognition rules (OpenAI, Gemini, Claude, etc.), manually configure [JSONPath](https://docs.apidog.com/jsonpath-645606m0.md) to extract the required content.

**Example SSE Response:**

```
data: {"choices":[{"index":0,"message":{"role":"assistant","content":"H"},"logprobs":null,"finish_reason":"stop"}]}

data: {"choices":[{"index":0,"message":{"role":"assistant","content":"i"},"logprobs":null,"finish_reason":"stop"}]}
```

**JSONPath Configuration:**

To extract the `content` field, use:

```
$.choices[0].message.content
```

**JSONPath Breakdown:**

| Component | Description |
|-----------|-------------|
| `$` | Root of the JSON object |
| `choices[0]` | First element of the `choices` array |
| `message.content` | `content` attribute under the `message` object |

**Extracted Result:**

```
Hi
```

### Use Post Processor Scripts

For non-JSON SSE messages, you can:

- Use [post processor scripts](https://docs.apidog.com/post-processor-scripts-593611m0.md) to manually handle the data
- Contact [technical support](https://docs.apidog.com/apidog-support-center-748035m0.md#still-need-help) to provide feedback on the model format you're using for potential built-in support

## FAQ

<Accordion title="What to do if the SSE timeline does not display messages?" defaultOpen>
    
This issue usually occurs when the server's response doesn't follow SSE format guidelines. The standard SSE message format requires:

- Message content must come after `data:`
- Each message must be separated by two newline characters (a blank line between messages)

For more details on the SSE message format, refer to the [MDN documentation - Using Server-Sent Events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events).
</Accordion>

## Learn More

<Card title="How to Use the Deepseek API (R1 & V3)？" href="https://apidog.com/blog/how-to-use-deepseek-api-r1-v3/">
A complete guide to obtaining the DeepSeek API key and debugging the API.
</Card>

