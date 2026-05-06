# 在线文档中的鉴权组件

## 文档中的鉴权信息展示

Apifox 生成的 API 文档会显示接口使用的鉴权组件信息：

- **单个鉴权组件**

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/509064/image-preview)
</Background>

- **多个鉴权组件**

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/509065/image-preview)
</Background>



## OAuth 2.0 的文档展示

对于 OAuth 2.0 鉴权组件，文档会显示更详细的信息：

- 授权类型（Grant Type）
- 相关 URL（Authorize URL、Token URL 等）
- 可用的 Scope 及其描述
- 接口要求的特定 Scope

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/509064/image-preview)
</Background>


## 在在线文档调试接口

得益于鉴权组件将鉴权的模版和鉴权的值进行了分离，出于隐私保护的角度，在在线文档调试接口时，用户必须手动填写鉴权信息。即使目录或接口配置了默认鉴权值，也无法在在线文档中使用。

<Steps>
  <Step>
    访问在线文档
  </Step>
  <Step>
    在右上角 Auth 设置中填写相应的鉴权值
  </Step>
  <Step>
    填写后的鉴权值将应用于文档中当前接口的调试
  </Step>
</Steps>


<Background>

![CleanShot 2025-04-01 at 18.10.19@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/509072/image-preview)
</Background>


