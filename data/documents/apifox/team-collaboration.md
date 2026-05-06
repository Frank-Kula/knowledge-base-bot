# 团队协作



## 多人协作 & 实时同步

接口文档的实时协作能力有助于提高研发团队的工作效率，降低反复沟通的成本。接口管理中的 HTTP 接口和数据模型模块支持多人在线实时协作，当其他人保存数据后，当前页面将自动更新由其它团队成员所作出的变更。

![](https://cdn.apifox.cn/uploads/help/202401181713215.gif)

### 适用场景

在以下场景，新的接口文档会自动同步给团队内的成员，无需手动全局刷新：

-   在应用内修改并保存接口后
-   使用 Apifox Helper（IDEA 插件）上传接口后
-   定时导入 Swagger/OpenAPI 文件后

### 功能亮点

和其他同类产品相比，Apifox 的多人协作功能具备以下显著特点：

- 实时展示编辑者的头像，谁正在编辑同一个接口，一目了然
- 字段级协作，有效避免内容冲突
- 如果内容有冲突，编辑时就知道，可以提前解决并继续编辑
- 细粒度的冲突处理，可以同时保留双方的部分内容
- 接口文档拥有历史记录和回收站，支持还原到旧版本，不怕误修改
- 自动导入和 IDEA 插件也是实时协作的一部分，导入后会自动更新


## 协作链接

“协作链接” 功能可以让团队内的成员快速定位接口并展开协作。

:::tip[]
协作链接仅用于团队内部分享，非团队成员无法打开协作链接。
:::

### 复制协作链接

轻点接口右侧菜单栏中的 “复制协作链接” 按钮，即可生成一个协作链接。将它发给其他团队成员，打开链接后即可直接在 Web 端中定位到对应的接口。


<Background>

![CleanShot 2024-12-20 at 17.18.04@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/485376/image-preview)
</Background>


### 更改打开方式

协作链接支持在客户端和 Web 端中打开。若你希望通过客户端定位接口，可以前往 [Web 端](https://app.apifox.com/main)，轻点 “设置”⚙ 图标，在 “通用” 处开启 “总是在桌面端打开协作链接” 按钮。

> macOS 的设置按钮位于页面右上角，Windows 的设置按钮位于页面左下角。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/485377/image-preview)
</Background>


访问协作链接后将自动唤起客户端。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/485378/image-preview)
</Background>

