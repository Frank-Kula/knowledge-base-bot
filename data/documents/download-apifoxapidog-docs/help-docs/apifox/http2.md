# HTTP/2

HTTP/2 是 HTTP 协议的第二个主要版本，于 2015 年正式发布，优化了网页加载性能，减少网络延迟，以适应当代网络需求。



## 开启兼容开关
 
你可以直接在 HTTP 项目内调试 HTTP/2 接口，但需要确保已在 “项目设置 -> 功能设置 -> 高级设置” 中开启兼容 HTTP/2 开关。


<Background>
    
![CleanShot 2024-10-12 at 18.17.20@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/470079/image-preview)
</Background>


开启兼容开关后，请求 HTTP/2 接口时，Apifox 会自动将请求协议升级为 HTTP/2。

HTTP/2 示例接口：

```js
https://http2.pro/api/v1
```


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/470080/image-preview)
</Background>


## 更多设置

你可以在 “项目设置 -> 功能设置 -> 高级设置” 内手动选定相关设置。建议使用 Apifox 的默认配置，以保证最大程度的兼容性。

<Background>
    
![CleanShot 2024-10-12 at 18.17.20@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/470079/image-preview)
</Background>

完整配置选项说明：

- **HTTPS**
  
  `HTTP/2 应用层协议协商`：**默认选项**，Apifox 会尝试使用 HTTP/2 协议建立连接，并使用 HTTP/2 协议发送请求；当接口不支持时将自动退回至 HTTP/1.1。

  `HTTP/1.1`：即仍采用原 HTTP 的连接方式，不使用 HTTP/2 协议。

- **HTTP**
  
  `HTTP/1.1`：**默认选项**，以 HTTP/1.1 协议建立连接，并使用 HTTP/1.1 协议发送请求。

  `HTTP/2 先验知识`：建立 h2c 连接，如果接口不支持 HTTP/2 协议则直接连接失败，不会自动退回 HTTP/1.1。

