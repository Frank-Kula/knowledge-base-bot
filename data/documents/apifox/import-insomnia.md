# 导入 Insomnia

Insomnia 是由老牌的 API 服务提供商 Kong 所开源的一款桌面端应用程序，提供 API 设计、调试及测试功能。Apifox 支持导入 Insomnia 平台上的接口数据。

## 导出 Insomnia 数据

如果未登录 Insomnia，点击左侧列表顶部的 “Scratch Pad”，然后轻点 “Export” 按钮。

<Background>
<img alt="未登录 Insomnia" src="https://api.apifox.com/api/v1/projects/5097254/resources/468179/image-preview" width="300px"/>
</Background>


如果已登录 Insomnia，点击左侧列表的顶部的 “Collection”，然后轻点 “Export” 按钮。

<Background>
<img alt="已登录 Insomnia" src="https://api.apifox.com/api/v1/projects/5097254/resources/468183/image-preview" width="300px" />
</Background>



选择需要导出的接口。

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/468185/image-preview)
</Background>


最后指定导出 Insomnia V4 格式。

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/468186/image-preview)
</Background>


## 导入 Insomnia 数据


打开 Apifox 中的 “项目设置” 面板，然后选择 Insomnia 文件进行导入。


<Background>

![CleanShot 2024-09-29 at 11.14.52@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/468187/image-preview)
</Background>



如果需要保留路径中的完整URL，请打开 “接口路径保留前置URL” 开关。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/468211/image-preview)
</Background>



如果需要导入 Insomnia 中的环境，请在 Apifox 中指定具体的环境。指定后 Insomnia 的环境将会被导入并作为 Apifox 的环境变量，而不是前置 URL。


<Background>
![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/468212/image-preview)
</Background>


