# 什么是 API Key



API Key（应用程序接口密钥）是一种用于识别和验证应用程序或用户身份的唯一标识，它通常是由服务提供商或开发平台提供的一串字符串，一般由字母、数字或特殊字符组成。API Key 主要用于控制访问权限，确保只有经授权的用户或开发者能够使用 API 提供的数据或服务。

## API Key 的作用

| 基本用途 | 描述 |
| --- | --- |
| 身份验证 | API Key 用于验证发送请求的客户端是否被授权访问 API 资源。 |
| 访问控制 | 服务提供商可以根据 API Key 对客户端的访问进行限制和管理，如调用频率、可用功能等。 |
| 数据统计与计费 | 通过对 API Key 的跟踪和分析，服务提供商能够了解 API 的使用情况，进行数据统计，并根据使用量对客户进行计费。 |

## 客户端如何使用 API Key？

### 添加到请求头

将 API Key 添加到 API 请求的头部（Header），例如将其添加到请求头的 `Authorization` 字段中：

```js
const apiKey = 'YOUR_API_KEY'

fetch('https://api.example.com/data', {
  headers: {
    // highlight-next-line
    Authorization: `Bearer ${apiKey}`,
  },
})
  .then((response) => response.json())
  .then((data) => console.log(data))
```

### 添加到特定请求头

有些 API 提供商会要求将 API Key 直接插入请求头中，并且可能要求使用特定的命名。例如，如果 API 提供商要求将 API Key 添加到请求头的 `X-API-Key` 字段中，你可以这样做：

```js
const apiKey = 'YOUR_API_KEY'

fetch('https://api.example.com/data', {
  headers: {
    // highlight-next-line
    'X-API-Key': apiKey,
  },
})
  .then((response) => response.json())
  .then((data) => console.log(data))
```

### 添加到请求 URL

将 API Key 直接添加到 API 请求的查询参数（Query Parameter）中，即请求 URL 上，例如：

```js
const apiKey = 'YOUR_API_KEY'

// highlight-next-line
fetch(`https://api.example.com/data?api_key=${apiKey}`)
  .then((response) => response.json())
  .then((data) => console.log(data))
```

### 添加到请求体

对于某些 API，特别是需要 POST 或 PUT 请求时，可以将 API Key 作为请求体的一部分发送，例如：

```js
const apiKey = 'YOUR_API_KEY'

fetch('https://api.example.com/data', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    // highlight-next-line
    apiKey: apiKey,
  }),
})
  .then((response) => response.json())
  .then((data) => console.log(data))
```

## 服务器端验证

API 服务接收到携带 API Key 的请求后，会将其与服务器端存储的 Key 进行比对。如果 Key 有效且具有相应权限，则允许请求访问相应的资源或功能；否则，会拒绝请求并返回错误信息。以下是验证 API Key 的基本流程：

**1）API 服务接收请求：** 当 API 服务收到一个请求时，它会检查该请求是否携带了 API 密钥。API 密钥通常包含在请求的头部、查询参数或请求体中。

**2）与服务器端存储的密钥比对：** 一旦 API 服务接收到携带 API 密钥的请求，它会将该密钥与服务器端存储的密钥进行比对。通常情况下，服务器会维护一个存储 API 密钥的数据库或其他存储机制。

**3）验证密钥的有效性和权限：** 在比对密钥之后，API 服务会验证密钥的有效性以及密钥所关联的权限。这意味着 API 服务会检查该密钥是否存在于服务器端存储中，并且是否具有足够的权限来执行请求所需的操作。

**4）允许或拒绝请求：** 如果 API 密钥有效且具有相应的权限，API 服务将允许请求访问相应的资源或功能。否则，如果密钥无效或没有足够的权限，API 服务将拒绝请求，并返回相应的错误信息。

这种服务器端验证机制确保了只有经过授权的用户或应用程序才能访问 API 的资源或功能，从而确保了 API 的安全性和可靠性。

