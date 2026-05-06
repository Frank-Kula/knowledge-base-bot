# 请求参数编码解码

Apifox 提供了多种配置选项，以优化你的 API 请求。这些设置让你能够根据需求自定义 Apifox 在发送请求时的行为。

## 自定义请求设置

要配置自定义设置，可以选择请求的 **“设置”** 标签，然后开启或关闭特定设置。每个设置都会在发送请求时对其效果进行说明。例如，你可以开启 SSL 证书验证或禁用 URL 编码。


<Background>
 
![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/470078/image-preview)
</Background>


## 请求 URL 编码

Apifox 会解析并编码请求的 URL，以提高成功调用 API 的可能性。它会将 URL 中的字符进行编码，转换为更符合 API 所要求的格式。

Apifox 支持以下三种编码方式：

- WHATWG
- RFC 3986
- 关闭自动编码

### WHATWG

这是现代浏览器采用的编码方法，比较宽松，保留了更多的原始字符。例如，它不会对波浪号（~）进行编码，空格会转换为`+`而不是 `%20`。

### RFC 3986

这是 IETF（互联网工程任务组）定义的更严格标准。它会对更多字符进行编码，包括 WHATWG 标准下未编码的字符。例如，它会对波浪号进行编码，空格会转换为 `%20` 而非 `+`。

### 关闭自动编码

此选项会将 URL 按原样发送，不进行任何编码。如果你已手动编码 URL，或者想测试服务器如何处理未编码的 URL，这个选项会很有用。但请注意，这可能会导致 URL 中的特殊字符或空格出现问题。

## 参数编码解码

选择参数文本后右键点击，可以对参数进行 `EncodeURIComponent` 编码或 `DecodeURIComponent` 解码，也可以将其存入变量。

<Background>
![](https://cdn.apifox.cn/uploads/help/202411291746511.gif)
</Background>


