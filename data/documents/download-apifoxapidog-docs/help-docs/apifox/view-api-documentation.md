# 查看 API 文档

在浏览器中打开复制的链接，就能看到 Apifox 的在线 API 文档了。

每个 API 都会展示为单独的页面，包含以下几个部分：
- 接口描述信息
- 调试
- 请求参数
- 示例代码
- 返回响应

<Background>

![CleanShot 2024-12-19 at 14.18.30@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/484787/image-preview)
</Background>

## 接口描述信息

这部分展示了 API 的各种基本信息，比如 URL、请求方式、修改时间、描述等。你可以在生成文档时选择要显示哪些字段。

- **接口状态**
已发布状态的 API 不会显示状态标签；其他状态（比如 “开发中”）的 API 会在名称后面显示状态标签。被标记为 “将废弃” 的 API 在左侧目录树中会显示一条删除线，如 “~~接口名称~~”。

    <Background>
    <p style="text-align: center">
        <img src="https://api.apifox.com/api/v1/projects/5097254/resources/484788/image-preview" style="width: 640px" />
    </p>

    </Background>

- **接口描述**
接口描述中的 Markdown 内容会显示在元数据的底部。

## 调试

点击后会展开调试面板，你可以在这里发送请求、修改参数，还可以切换请求的环境。这里可用的环境就是创建文档时选择的那些环境。

:::tip[]
如果你在创建文档时选择了云端 Mock 环境，相当于给文档阅读者开启了一个简单的沙箱环境。
:::

发送请求后，你可以在页面上看到响应结果和实际发送的请求内容。

<Background>
<p style="text-align: center">
    <img src="https://api.apifox.com/api/v1/projects/5097254/resources/484790/image-preview" style="width: 440px" />
</p>
    
</Background>


:::highlight green 📌
[Apifox 发布文档/快捷分享中，如何让使用者修改请求的 Base URL ？](https://docs.apifox.com/6598703m0)
:::

### 使用变量

如果请求示例中用到了`{{variables}}`变量，阅读者在使用 “调试” 功能时，需要先设置这些变量的值才能发送请求。

<Background>
<p style="text-align: center">
    <img src="https://api.apifox.com/api/v1/projects/5097254/resources/601881/image-preview" style="width: 440px" />
</p>
   
</Background>


:::highlight green 📌
[如何在 Apifox 在线文档中共享 Header（如 Token）？](https://docs.apifox.com/7110742m0)
:::

### 鉴权配置

你可以在项目内的接口或者目录层级的 Auth 中配置鉴权方式，可以使用 [鉴权组件](https://docs.apifox.com/security-schemes)，也可以自行设置。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/601884/image-preview)
</Background>

配置鉴权信息后，比如使用 Bearer Token 鉴权，你会在 **“在线文档”** 面板顶部看到一个 “鉴权” 区域，在这里可以直接输入 Token 值。

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/601885/image-preview)
</Background>

这种配置方式最大的好处是可以在不同接口间共享鉴权信息。如果多个接口引用相同的鉴权组件或鉴权类型，只需要在一个地方输入鉴权信息，其他接口就可以自动复用。


<Background>
![apifox-03-正确配置Auth.gif](https://api.apifox.com/api/v1/projects/5097254/resources/601886/image-preview)
</Background>


这些鉴权凭证会加密后保存在浏览器的本地存储（LocalStorage）中，并按浏览器会话（Session）进行管理；在同一会话内，它们可以在多个窗口和标签页之间共享。一旦关闭浏览器，会话结束，这些凭证也会自动失效。

更具体地说：本地存储（LocalStorage）里的鉴权数据是加密后的内容，而用于解密的密钥保存在会话 Cookie 中。 本地存储（LocalStorage）的数据会长期存在，但只要浏览器关闭，会话 Cookie 中的密钥就会失效，这些加密数据就无法再被解密读取，因此下次访问时需要重新填写鉴权信息。


## 请求参数

参数和请求体的规范说明。Apifox 支持两种参数展示样式，你可以在 **项目设置 **-** 功能设置 **-** 接口功能设置** 中选择现代风格或经典风格。

<Background>

![CleanShot 2024-12-19 at 14.26.48@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/484794/image-preview)
</Background>

## 示例代码

各种编程语言的请求示例代码。你可以在创建文档时选择是否显示这个模块。

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/484795/image-preview)
</Background>

如果不需要示例代码模块，可以不勾选。

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/550727/image-preview)
</Background>


## 返回响应

响应规范和响应示例，与 Apifox 客户端中的内容一致。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/484797/image-preview)
</Background>


## 导出
如果你在创建文档时选择了 “允许导出数据”，阅读者就能在文档右下角和底部看到导出选项。


<Background>
<p style="text-align: center">
    <img src="https://api.apifox.com/api/v1/projects/5097254/resources/484799/image-preview" style="width: 200px" />
</p>
</Background>



阅读者可以选择 “克隆”或“导出”。“导出”支持 OAS、HTML、Markdown 和 Apifox 格式。
