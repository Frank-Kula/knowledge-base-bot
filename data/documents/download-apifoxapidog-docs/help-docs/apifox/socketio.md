# Socket.IO 调试

Socket.IO 是一个库，可以在客户端和服务器之间实现低延迟、双向和基于事件的通信。

<Embed src="//player.bilibili.com/player.html?isOutside=true&aid=114120468730768&bvid=BV15S9yYdEho&cid=28737998582&p=1" width="720px" height="405px" />

## 新建 Socket.IO 接口

> Apifox 版本需大于 `2.7.61`

<Steps>
  <Step>
    点击项目左侧的 `+` 按钮，选择 “新建 Socket.IO 接口”
      
<Background>

![CleanShot 2025-11-05 at 16.48.57@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/588585/image-preview)
</Background>

  </Step>
  <Step>
    输入服务器地址 *（示例：`ws://localhost:3000`）*，支持`ws://`或`wss://`协议头
      
    <Background>

    ![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/499769/image-preview)
    </Background>

  </Step>
    <Step>
    点击 “连接” 按钮建立连接
        
<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/499770/image-preview)
</Background>

        
  </Step>
</Steps>

## 监听事件

点击 **“Events”** 标签页，输入需要监听的事件名（如 `new message`）。取消监听事件后，将不再接收该事件消息。
    <Background>
    ![事件订阅截图](https://api.apifox.com/api/v1/projects/5097254/resources/499814/image-preview)
    </Background>

**监听规则：**

- 默认自动监听`message`事件
- 动态增删事件不影响已建立的连接
- 修改事件名会自动关闭原事件监听


## 发送消息

### 事件、参数

<Steps>
  <Step>
    在消息输入区配置：
    - **事件名**：默认为`message`（可自定义，如 `new message`）
    - **参数内容**：支持 JSON、文本格式和 Binary
    
    
:::tip[]
支持发送空消息和没有参数的消息
:::
  </Step>
  <Step>
    点击 “发送” 按钮
  </Step>
  <Step>
    在时间线中查看带有事件标签的发送记录
      
<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/500133/image-preview)
</Background>

  </Step>
</Steps>


### Ack

勾选`Ack`复选框以等待服务端回调，发送请求后可接收回调消息。
    
    
<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/500135/image-preview)
</Background>


### 多参数

点击 **“添加参数”** 可新增多参数标签页。

<Background>
![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/500136/image-preview)
</Background>



发送多参数消息时会在时间线中显示 `x个参数` 标签，点击展开所有参数，右侧 Tab 切换查看。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/500137/image-preview)
</Background>





## 添加握手请求参数


可直接在地址栏或`Params`、`Headers`、`Cookies`中添加请求参数。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/500139/image-preview)
</Background>



## 客户端版本与握手路径


<Steps>
  <Step title="配置入口">
    接口请求 “设置 -> 高级配置”
      
<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/499799/image-preview)
</Background>

  </Step>
  <Step title="客户端版本">
   
默认`v4` ，若服务端为旧版本（如 v2/v3），需手动切换。
      
  </Step>
  <Step title="握手路径">
    默认`/socket.io`，若服务端自定义路径（如 `/custom`），需同步修改。
  </Step>
</Steps>


## 使用变量

可以在 Socket.IO 连接的参数中使用 Apifox 变量，发送消息时会自动将变量替换为实际内容。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/500154/image-preview)
</Background>


## 保存接口

在完成调试后，你可以点击 **“保存”** 按钮将 Socket.IO 接口保存到 HTTP 项目的目录树中，以便团队内的其他成员进行调试或查看接口文档。



## 生成接口文档

你可以对 Socket.IO 接口设定`状态`、`责任人`、`标签`，还可以用`Markdown`格式撰写详细的接口说明。Apifox 支持生成在线接口文档，你可以将文档 URL 分享给团队内部的其他成员。


<Background>

![CleanShot 2025-03-04 at 17.07.59@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/500198/image-preview)
</Background>



## 常见问题


<Accordion title="连接失败怎么办？" defaultOpen>

**检查清单：**
- 服务端是否已启动
- 客户端版本与服务端是否匹配
- 防火墙是否开放对应端口
</Accordion>


<Accordion title="多参数接收不全？" defaultOpen={false}>
**解决方案：**

1. 检查服务端参数处理逻辑，例如：
    
```js
socket.on('event', (...args) => {
  const callback = typeof args[args.length - 1] === 'function' 
    ? args.pop() 
    : null;
  // 处理 args 中的参数
});
```
2. 确认参数顺序与类型
</Accordion>

<Accordion title="ACK 未触发？" defaultOpen={false}>
请检查服务端是否调用 `callback()`
</Accordion>
