# 使用鉴权组件

## 在目录级别配置鉴权组件


<Steps>
  <Step>
    选择任意一个目录，点击右侧 “Auth” 选项卡，选择鉴权方式为 “鉴权组件”。
      
<Background>

![CleanShot 2025-04-01 at 11.27.00@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/508867/image-preview)
</Background>

  </Step>
  <Step>
    从 “鉴权组件” 下拉菜单中选择需要的鉴权组件。
      
<Background>
<img src="https://api.apifox.com/api/v1/projects/5097254/resources/508960/image-preview" width="540px"/>
</Background>

  </Step>
  <Step>
    如果选择了 OAuth 2.0 鉴权组件，可以进一步选择所需的 Scope。
<Background>
<img src="https://api.apifox.com/api/v1/projects/5097254/resources/508962/image-preview" width="540px"/>
</Background>
  </Step>
</Steps>


目录配置的鉴权组件将应用于该目录下的所有子目录和接口（除非它们有自己的鉴权配置）。

## 在接口级别配置鉴权组件

<Steps>
  <Step>
    选择任意一个接口，点击右侧 “修改接口” 选项卡，在 “请求参数” 的 “Auth” 选项中选择鉴权方式为 “鉴权组件”。
      
<Background>


![CleanShot 2025-04-01 at 11.41.17@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/508886/image-preview)
</Background>

  </Step>
  <Step>
    从 “鉴权组件” 下拉菜单中选择需要的鉴权组件。
      
<Background>
<img src="https://api.apifox.com/api/v1/projects/5097254/resources/508963/image-preview" width="540px"/>
</Background>
  </Step>
  <Step>
    如果选择了 OAuth 2.0 鉴权组件，可以进一步选择所需的 Scope。
<Background>
<img src="https://api.apifox.com/api/v1/projects/5097254/resources/508964/image-preview" width="540px"/>
</Background>
  </Step>
</Steps>

接口级别的鉴权配置优先级高于目录级别。

## 配置鉴权组件默认值

鉴权组件只定义了鉴权的方法，调试接口时还需要输入具体的鉴权值。

调试接口时，每次都填写鉴权值较为麻烦。因此，Apifox 提供“默认鉴权值”功能，配置默认鉴权值之后，调试接口时就可以选择使用默认鉴权值，也可以手动填写新的鉴权值。如果在目录配置了“默认鉴权值”，那么目录下的接口都可以使用这个值，非常便利。

<Steps>
  <Step>
      在鉴权组件列表中，选择组件并配置默认值。
    <Background>
    <img src="https://api.apifox.com/api/v1/projects/5097254/resources/508965/image-preview" width="540px"/>
    </Background>
  </Step>
  <Step>
    根据鉴权类型填写相应的值
   - API Key：填写密钥值
   - Basic Auth：填写用户名和密码
   - Bearer Token：填写令牌
   - OAuth 2.0：填写客户端 ID、客户端密钥等
   - 其它鉴权类型默认值...
  </Step>
</Steps>


## 继承与自定义鉴权值

使用鉴权组件时，你可以选择：

1. **继承上级配置**：使用父级目录或根目录配置的鉴权组件及其默认值

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/508967/image-preview)
</Background>

2. **自定义鉴权值**：保持鉴权组件不变，但使用自定义的认证值


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/508971/image-preview)
</Background>


## 多个鉴权组件的使用

Apifox 支持为一个接口配置多个鉴权组件，这对应于 OpenAPI 规范中的多重认证机制：

- **AND 关系**：必须同时满足所有鉴权要求
- **OR 关系**：满足任一鉴权要求即可

在接口或目录的鉴权设置中，可以通过 `+` 按钮添加多个组件。

<Background>
    <img src="https://api.apifox.com/api/v1/projects/5097254/resources/508972/image-preview" width="540px"/>
</Background>

## 使用组合型鉴权组件

组合型鉴权组件创建完成后，会出现在项目的 “鉴权组件” 列表中。可以在接口或目录的 Auth 配置中引用该组合型鉴权组件，从而实现多层鉴权。


<Steps>
  <Step>
    在项目中找到需要配置鉴权的接口或者目录，进入编辑页面。
  </Step>
  <Step>
    在接口或目录的 Auth 配置区域，选择创建的组合型鉴权组件，Apifox 会自动应用组合型鉴权组件中的所有鉴权规则。
      
<Background>

![CleanShot 2025-05-28 at 15.55.40@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/528743/image-preview)
</Background>

  </Step>
  <Step>
    在接口测试页面，可以看到组合型鉴权组件的基本认证信息。
      
<Background>

![CleanShot 2025-05-28 at 15.56.55@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/528744/image-preview)
</Background>

  </Step>
</Steps>



## 使用 OAuth 2.0 组件时，选择 Scope

根据 OpenAPI 规范，创建 OAuth 2.0 类型的鉴权组件时，需要预先配置全部 Scope。而在接口使用 OAuth 2.0 类型的鉴权组件时，需要选择使用哪些 Scope。

Apifox 为了简化接口配置 Scope 的操作，支持在目录上配置 Scope。配置之后，目录内的接口就会默认使用目录上配置的 Scope。当然，也支持为接口单独配置 Scope。

<Steps>
  <Step>
    在接口的 “Auth” 设置中选择 OAuth 2.0 鉴权组件。
  </Step>
  <Step>
    在 “Scopes” 配置部分，可以看到该组件定义的所有可用 Scope，选择该接口需要的 Scope。
 <Background>
    <img src="https://api.apifox.com/api/v1/projects/5097254/resources/508977/image-preview" width="540px"/>
</Background>     
      
  </Step>
  <Step>
    如果接口继承了父级目录的 OAuth 2.0 配置，也可以点击 “Reset...” 恢复为父级配置的 Scope。
    <Background>
    <img src="https://api.apifox.com/api/v1/projects/5097254/resources/508980/image-preview" width="540px"/>
</Background>        
  </Step>
</Steps>



## 调试使用 OAuth 2.0 鉴权组件的接口

在进行 API 设计时，可以为使用 OAuth 2.0 的接口预先配置默认鉴权值。这样的话，调试接口时就可以直接使用默认鉴权值，而无需为每个接口都获取 Token。

### 在“目录”中获取 Token 作为默认鉴权值

<Steps>
  <Step>
    在项目中选择一个目录，点击右侧 “Auth” 选项卡，选择 OAuth 2.0 鉴权组件，配置所需 Scopes，选择授权类型，点击 “获取 Token” 按钮。
      
<Background>

![CleanShot 2025-04-01 at 16.10.03@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/509018/image-preview)
</Background>

  </Step>
  <Step>
    在弹出的测试面板中：
    - 填写客户端 ID、密钥等必要信息
    - 点击 “继续” 按钮
      
      
<Background>

![CleanShot 2025-04-01 at 17.28.47@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/509036/image-preview)
</Background>

  </Step>
  <Step>
    获取到 Token 后，可以查看 Token 详情和有效期，获取的 Token 可用于该目录下的所有接口测试。
      
<Background>

![CleanShot 2025-04-01 at 17.29.35@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/509037/image-preview)
</Background>

  </Step>
</Steps>

### 在“修改接口”中获取 Token 作为默认鉴权值

<Steps>
  <Step>
    选择需要编辑的接口，点击 “修改接口”，选择并配置 OAuth 2.0 鉴权组件，在配置界面中点击 “获取 Token” 按钮。
      
<Background>

![CleanShot 2025-04-01 at 17.34.25@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/509044/image-preview)
</Background>

      
  </Step>
  <Step>
    在弹出的测试面板中：
    - 填写客户端 ID、密钥等必要信息
    - 点击 “继续” 按钮
    
<Background>

![CleanShot 2025-04-01 at 17.36.33@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/509047/image-preview)
</Background>

    
  </Step>
  <Step>
    - 完成授权流程获取 Token
    - 获取的 Token 将应用于当前接口的调试
    
<Background>

![CleanShot 2025-04-01 at 17.37.41@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/509050/image-preview)
</Background>

  </Step>
</Steps>




### 调试接口时，使用默认鉴权值或者获取新的 Token

**方式一：使用接口默认鉴权值**

运行接口时，在 “Auth” 选项卡选择 “使用接口默认鉴权值”，在接口中获取的 Token 会自动应用于当前请求。

**方式二：获取新的 Token**

<Steps>
  <Step>
    运行接口时，在 “Auth” 选项卡选择 “手动设置”，点击 “获取 Token” 获取新 Token。
      
<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/509055/image-preview)
</Background>

      
  </Step>
  <Step>
    在弹出的测试面板中：
    - 填写客户端 ID、密钥等必要信息
    - 点击 “继续” 按钮
    
<Background>

![CleanShot 2025-04-01 at 17.45.04@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/509056/image-preview)
</Background>

    
  </Step>
  <Step>
    - 完成授权流程获取 Token
    - 获取的 Token 将应用于当前接口的调试
   
  </Step>
</Steps>
