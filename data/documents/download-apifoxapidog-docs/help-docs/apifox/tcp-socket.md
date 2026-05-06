# Socket 接口功能简介


Socket 是一种传输层协议的接口，它使得用户更加方便地使用 TCP/IP 协议进行网络通信。Socket 接口提供了创建 TCP/IP 连接、数据传输、关闭连接等基本操作，允许应用程序通过网络连接进行双向通信。

Socket 接口面向数据流，它提供了一套函数和参数，允许开发者创建、配置和管理套接字（socket）对象以及与其相关联的操作。

## 示例场景

假设我们有一个“宠物商店”的项目，其中有一个 Socket 服务“宠物资料服务”，服务器的地址为:`dev.server.com`，端口为：`9001`。

该服务提供以下接口：

1. 新建宠物资料
2. 修改宠物资料
3. 查询宠物资料
4. 删除宠物资料

本文以新建宠物资料接口作为示例，演示如何使用 Apifox 设计并管理此接口。

## 快速开始

### 1. 新建服务

进入 Apifox 项目后，点击左侧搜索框旁边的 + 号按钮，轻点 “TCP（Socket）” 选项。

<Background>

![CleanShot 2025-01-15 at 16.43.51@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/490451/image-preview)
</Background>

填写宠物资料服务相关信息：


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/490454/image-preview)
</Background>


### 2. 创建接口

在 “宠物资料服务” 中添加接口：


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/490456/image-preview)
</Background>


填写接口相关信息。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/490459/image-preview)
</Background>


#### 设置前置操作

使用[报文数据处理器](https://docs.apifox.com/message-data-processor.md)对实际发送请求前对输入的数据进行处理。例如进行以下操作：

- 计算内容长度并添加到包头
- 计算 XML 字节长度并添加到包头。

#### 设置返回结果

你还可以使用[报文数据处理器](https://docs.apifox.com/message-data-processor.md)对接口返回的数据进行处理后再展示：

1. 去除包头 *(指定包头长度)*：去除返回数据里的包头 *（展示的时候不需要）*。

2. XML 转 JSON *(可表单展示)*：将返回包体里的 XML 转成 JSON 方便查看。


<Background>
 
![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/490485/image-preview)
</Background>


### 3. 运行接口

切换至接口的“运行” tab 页，可以看到“报文内容”通过表单方式输入。可填写拟新建的宠物信息，点击“发送”并查看返回结果。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/490492/image-preview)
</Background>


### 4. 保存为用例

接口运行无误后，点击右上方 “保存为用例” 按钮方便重复使用。

## 更多功能

Socker 服务同样支持[断言](https://docs.apifox.com/assertions.md)、[提取变量](https://docs.apifox.com/extract-variables.md)、[前置脚本](https://docs.apifox.com/pre-request-scripts.md)与[后置脚本](https://docs.apifox.com/post-request-scripts.md)等功能。

## 报文示例

### 请求报文

```
00000187<?xml version="l.0" encoding="UTF-8"?><data><name>Kitty 猫</name><photoUrl>http://dummyimage.com/400x400</photoUrl><tags>花斑</tags><categoryId>12</categoryId><status>pending</status></data>
```

报文说明：

1. 前`8`位`0000187`为包头，存储包体的字节长度。
2. 剩余部分为包体，为`XML`格式。
   1. XML 中`<data>`节点存储需要新建的宠物资料数据。



### 返回报文

```
00000230<?xml version="l.0" encoding="UTF-8"?><data><errorCode>0</errorCode><data><name>Kitty 猫</name><photoUrl>http://dummyimage.com/400x400</photoUrl><tags>花斑</tags><categoryId>12</categoryId><status>pending</status></data></data>
```

报文说明：

1. 前`8`位`00000217`为包头，存储包体的字节长度。
2. 剩余部分为包体，为`XML`格式。
   1. XML 中`<errorCode>`节点表示状态码，`0`表示操作成功。
   2. XML 中`<data>`节点存储新建成功的宠物资料数据。

