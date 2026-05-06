# 环境管理

在发送 API 请求时，经常需要在开发、测试和生产环境之间切换。Apifox 提供了便捷的环境切换功能——只需在界面右上角选择目标环境即可。

Apifox 环境由两个核心要素构成：
- 第一个是 **“前置 URL”**，用于维护请求的目标地址；
- 第二个是由一组或多组 **“变量”** 组成，这些变量可以在接口或脚本中引用。

切换环境时，前置 URL 和环境变量都会根据当前环境中定义的值进行更新。

## 创建环境

<Steps>
  <Step>
    点击界面右上角的 “环境管理” 按钮 `≡`。
  </Step>
  <Step>
    点击左侧列表最后一项 `新建环境`。
  </Step>
  <Step>
    输入新环境的名称，添加服务前置 URL 和变量。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/480083/image-preview)
</Background>

  </Step>
  <Step>
    点击 `保存`。
  </Step>
  <Step>
要使用新环境，从界面右上角的环境管理中选择它。这样就把它设为当前环境，并将所有变量设置为环境中指定的值。

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/608798/image-preview)
</Background>

      
  </Step>
</Steps>

:::tip[]
Apifox 的 “环境” 概念与 Postman 略有不同。Postman 通常为每个前置 URL 创建一个单独的环境，这样容易模糊环境和前置 URL 之间的界限。

相比之下，Apifox 的环境更直接地反映了开发、测试和生产等实际工作环境，而不是将每个前置 URL 视为一个独立的环境。

例如，在测试环境中，可能同时包含多个服务，如用户服务和订单服务，这些服务应当共享同一个环境，而不应分成独立的 “用户环境” 和 “订单环境”。
:::

## 前置 URL

前置 URL 是 Apifox 环境中的核心功能。在 Apifox 中，接口路径以斜杠（`/`）开头，但不包含前置 URL；在发送接口请求时，需要指定目标前置 URL。这使得环境中的前置 URL 功能变得尤为重要——选择正确的环境是发送请求的前提。

标准的前置 URL 格式以协议开头，**不带**尾部斜杠（`/`），例如：

```js
http://localhost:8001
```
或
```js
http://localhost:8001/v1
```

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/608821/image-preview)
</Background>


每个前置 URL 都对应一个 [模块](https://docs.apifox.com/module.md)。一般情况下，接口都会使用其所在模块的前置 URL 来发送请求。

例如，如果生产环境的默认模块前置 URL 是 `http://abc.com/v1`，而你的接口路径是 `/pet`，那么在生产环境发送请求时，实际发送的请求地址是：

```
http://abc.com/v1/pet
```

:::tip[]
如果接口路径以 `http://` 或 `https://` 开头，前置 URL 就不会被添加到请求中。不过，一般**不推荐**这种做法。
:::

:::tip[BASE_URL 变量]
Apifox 中有一个特殊的环境变量 `BASE_URL`，用于存储当前环境的“默认服务”前置 URL。通常不建议直接使用这个变量。

对于自定义脚本，建议使用 `pm.request.getBaseUrl()` 来获取当前接口的前置 URL，避免使用 `pm.environment.get('BASE_URL')`。因为如果接口没有使用“默认服务”，则可能无法正确获取当前接口的前置 URL。

如果用户手动创建了名为 `BASE_URL` 的环境变量，它将覆盖系统预定义的 `BASE_URL`。

需要注意的是，脚本无法直接修改前置 URL。在脚本中执行 `pm.environment.set('BASE_URL', 'My_url')` 会创建一个名为 `BASE_URL` 的环境变量，而不会改变前置 URL 本身。
:::


## 通过模块来使用多个前置 URL

如果你的项目中的接口，需要使用多个前置 URL，那么你可以配置多个 [模块](https://docs.apifox.com/module.md)。


例如，用户相关的请求指向 `https://user.example.com`，订单相关的请求指向 `https://order.example.com`，商品相关的请求指向`https://product.example.com`你可以按照以下方式具体操作：

<Steps>
  <Step>
    在接口管理的目录树上方，成功添加多个模块。

<Background>
<img src="https://api.apifox.com/api/v1/projects/5097254/resources/542695/image-preview" width="460px"/>
</Background>
  </Step>
  <Step>
在环境管理中，可以看到前置 URL 内可以设置这几个模块的前置 URL，将实际 URL 填写进去并保存；

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/542696/image-preview)
</Background>

  </Step>
  <Step>
    在接口管理中某个模块的 **“根目录”** 页面，可以指定当前模块里的全部接口，使用的前置 URL 具体是哪一个：
    - **默认设置**：默认使用当前所在模块的第一个前置 URL。默认会使用此设置，一般情况下无需修改。

    - **手动指定**：手动指定一个当前所在模块的某个前置 URL 进行使用。在单模块中仍需要使用多个服务（前置 URL）时，可以进行指定。我们**已不推荐这种用法**，一般都建议创建多个模块来满足微服务场景下的需求。
    <Background>

    ![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/542156/image-preview)
    </Background>

    </Step>
  <Step>
      
      在接口管理中，无论是某个模块下的 **“子目录”**，还是具体的 **“接口”** 页面，都可以指定该子目录内所有接口或某个接口所使用的前置 URL。
    - **继承父级**：继承上一级目录设置的前置 URL 使用方式。默认会使用此设置，一般情况下无需修改。
    - **手动指定**：手动指定一个当前所在模块的某个前置 URL 进行使用。在单模块中仍需要使用多个服务（前置 URL）时，可以进行指定。
      
        <Background>
         
        ![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/608812/image-preview)
        </Background>

      我们**已不推荐这种用法**，一般都建议创建多个模块来满足此场景下的需求。

        <Background>

        ![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/542158/image-preview)
        </Background>

      
  </Step>
    
  <Step>
   选择好当前环境后，点击发送即可。无论是接口管理中单个接口请求发送或是自动化测试中运行发送多个请求，都会根据请求关联接口中的前置 URL 设置找到对应的前置 URL 进行实际发送。
  </Step>
  <Step>
每个不同的环境，都会包含项目全部的模块，并且这些模块的前置 URL 在每个环境中都需要进行单独设置。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/542698/image-preview)
</Background>

这是因为在大多数团队中，测试和开发环境都有对应不同的前置 URL。通过为每个环境设置相应的前置 URL，当你在右上角切换环境时，所有接口请求都会被发送到正确的服务。在实践中，这是最高效的设计方式。

  </Step>
</Steps>

:::tip[]
创建项目时的第一个模块为默认模块，当在一些特殊情况获取不到正确的前置 URL 时，是会返回此默认模块的前置 URL 的。
:::

## 添加环境变量

向环境添加变量时，可以为变量指定远程值（共享）和本地值（仅保存在电脑本地）。

:::highlight purple
了解更多[使用变量](https://docs.apifox.com/global-environment-session-variables.md)的信息。
:::

## 切换环境

Apifox 在工作台右上角的环境管理中显示当前环境。每当你发送请求或执行脚本时，Apifox 都会使用所选环境中变量的当前值。

要切换到不同的环境，只需从环境管理中选择即可。


<Background>
<p style="text-align: center">
    <img src="https://api.apifox.com/api/v1/projects/5097254/resources/480104/image-preview" style="width: 240px" />
</p>
</Background>



## 环境迁移

在 Apifox 中，变量的远程值会在团队内同步，而本地值仅存储在本地。这意味着，当你在另一台电脑上使用 Apifox 时，无法访问之前设置的本地值。

为了解决这个问题，Apifox 提供了环境迁移功能。你可以将环境中的服务和变量导出为 JSON 文件，并在另一台电脑上导入。操作步骤如下：

<Steps>
  <Step>
    在环境管理中，将鼠标悬停在环境列表旁的 `...` 上，点击 “导出” 以获取 JSON 文件。

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/480107/image-preview)
</Background>

  </Step>
  <Step>
在另一台电脑上，打开环境管理，将鼠标悬停在环境列表旁的 `...` 上，点击 “导入”，并选择要导入的 JSON 文件。
  </Step>
  <Step>
你也可以导入[从 Postman 导出](https://docs.apifox.com/import-postman.md)的环境。
    </Step>
</Steps>

## 环境可见范围

有时，你可能需要创建仅供个人使用的变量，不希望对他人可见。这时，你可以创建一个**私有环境**。

在环境的右上角，你可以设置环境的可见范围。默认是共享的，而你可以将自己创建的环境设为仅自己可见。但是，你无法更改他人创建的环境的可见性。


<Background>
<p style="text-align: center">
    <img src="https://api.apifox.com/api/v1/projects/5097254/resources/480108/image-preview" style="width: 640px" />
</p>
</Background>



:::tip[]
私有环境与其他环境共用相同的服务列表。在私有环境中添加或删除服务会同时影响所有环境。
:::


