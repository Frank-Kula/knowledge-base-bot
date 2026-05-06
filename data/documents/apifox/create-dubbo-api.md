# 新建 Dubbo 接口


Dubbo 是一款由阿里巴巴推出并开源的 RPC 框架，在国内的开发者中广泛流行。它支持多种主流网络传输协议和多种序列化格式。


Apifox 的 Dubbo 接口管理功能支持已在业界中广泛使用的「Dubbo 网络传输协议」 + 「Hessian 序列化格式」组合。

:::info[]
若你使用 Dubbo 框架中的其他网络协议和序列化格式，也欢迎扫码加入 Dubbo 交流群内反馈。我们将根据反馈情况，逐步支持更多的网络协议和序列化格式。
<img alt="Dubbo 交流群" src="https://api.apifox.com/api/v1/projects/5097254/resources/485790/image-preview" width="360px" />
:::

## 新建 Dubbo 项目

打开 Apifox，在团队中点击右侧的「新建项目」按钮，然后选择 Dubbo 项目。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/485791/image-preview)
</Background>


输入项目名称并选择 “项目语言” 后完成创建。

## 手动新建 Dubbo 接口

在 Apifox 新建 Dubbo 接口时需要逐个创建 Package、服务和方法。以 `demo/com.dubbo.example.DemoService:1.0.1` 接口为例，新建接口时的对照图如下：


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/485792/image-preview)
</Background>


若该服务配置了版本号和分组，那么在新建接口时还需要在上方栏中进行填写。


<Background>
 
![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/485793/image-preview)
</Background>


### 1. 新建 Package

在 Dubbo 项目中，点击左侧 `+` 号中的「新建 Package」选项。填写 Package 名称，指定目录后完成创建。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/485794/image-preview)
</Background>


### 2. 新建 Service


在 Package 中添加服务（Service）。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/485795/image-preview)
    
    
![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/485796/image-preview)
</Background>


### 3. 新建 Method

在服务中添加方法（Method）。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/485797/image-preview)
</Background>


## 导入 Dubbo 接口

点击 `+` 号下的「导入」按钮进入「导入数据」页；或点击「项目设置」，前往「导入数据」页导入外部 Dubbo 数据。支持 ZooKeeper、Nacos、阿里云 EDAS 三种外部导入渠道。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/485798/image-preview)
</Background>


:::tip[]
Apifox 作为客户端，仅支持导入 `provider`，不支持导入 `consumer`。如果无法导入接口，你仍然可以通过手动新建 Dubbo 接口的方式进行调试。
:::

### 元数据中心配置

Apifox 从元数据中心读取 Dubbo Provider 上报的元数据（Metadata）以完成接口的导入，包括接口列表、请求参数、响应参数、数据模型。

如果 Dubbo 版本低于 2.7，或者没有正确配置元数据中心，那么都无法使用 Apifox 导入元数据中心里的接口。需要注意的是，注册中心和元数据中心是 2 个独立的 Dubbo 配置项，配置文件的相关片段如下：

```properties
# Dubbo Registry 注册中心
dubbo.registry.address=nacos://127.0.0.1:8848
# Dubbo Metadata Report 元数据中心
dubbo.metadata-report.address=nacos://127.0.0.1:8848
```

如需了解更详细的配置，请前往 Dubbo 官方文档的元数据中心章节，查看关于 [Nacos](https://cn.dubbo.apache.org/zh-cn/overview/mannual/java-sdk/reference-manual/metadata-center/nacos/) 和 [ZooKeeper](https://cn.dubbo.apache.org/zh-cn/overview/mannual/java-sdk/reference-manual/metadata-center/zookeeper/) 的更多说明。

### ZooKeeper

在导入页选择 ZooKeeper 类型。根据页面指引，填写 ZooKeeper 地址及端口号。若注册中心配置了鉴权机制，请点击右侧齿轮按钮并填写用户名和密码。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/485799/image-preview)
</Background>


选择 Dubbo 应用，指定导入的目标目录，点击「保存并导入」按钮完成导入。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/485800/image-preview)
</Background>


### Nacos

在导入接口页选择 Nacos 类型。根据页面指引，填写 Nacos 地址及端口号，若注册中心配置了鉴权机制，请点击右侧齿轮按钮并填写用户名和密码。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/485801/image-preview)
</Background>


填写 Dubbo 应用，指定导入的目标目录，点击「保存并导入」按钮完成导入。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/485802/image-preview)
</Background>


### 阿里云 EDAS

在导入接口页选择阿里云 EDAS 类型，开始导入前需新建阿里云配置。点击阿里云配置下拉框中的「新建」按钮。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/485804/image-preview)
</Background>


输入阿里云配置名称、阿里云 Access Key ID、阿里云 Access Key Secret，然后点击「保存」按钮。

:::info[]
Access Key Secret 为敏感信息，仅保存在本地中，不会同步到云端。团队成员之间的数据也不互通，每个团队成员都需要自行手动设置。
:::

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/485805/image-preview)
</Background>

选择已创建好的配置，然后依次填写 EDAS 区域；选择命名空间、应用和目录。轻点「保存并导入」按钮完成导入。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/485806/image-preview)
</Background>


导入成功后，你可以在左侧目录树看到由 Package、服务和方法这三个层级所展开的 Dubbo 接口。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/485807/image-preview)
</Background>


## 常见问题

<Accordion title="从注册中心导入接口时，为什么在下拉列表内无法看到 Dubbo 应用？" defaultOpen>
请依次检查以下内容：

 - Dubbo 版本是否大于等于 2.7
 - Dubbo 是否正确配置了元数据中心
 - 需要给 `Provider` 配置元数据中心，而并非给 `Consumer` 配置元数据中心
 - 如果是 Dubbo 3，确认是否开启了 **“服务级服务发现”**，而不是开启 **“应用级服务发现”**

</Accordion>

<Accordion title="导入 Dubbo 接口时，为什么所展示的 Dubbo 应用数量比注册中心中的要少？" defaultOpen="false">

展示的 Dubbo 应用来自于元数据中心。元数据中心不等于注册中心，里面展示的内容不一定相等。注册中心会展示 `Provider`、`Consumer` 的服务名，而元数据中心将展示 `Provider` 的元数据，包括服务名、请求参数等。
</Accordion>


