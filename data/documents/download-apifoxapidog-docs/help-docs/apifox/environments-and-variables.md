# 环境和变量

在 Apifox 中，变量作为动态占位符，可在多个接口的请求参数和脚本中复用。在运行接口时，Apifox 会自动引用变量的当前值。通过将变量存储在环境中，可以轻松切换测试环境以适应不同的工作场景。

## 快速入门

以下是创建和使用变量的快速指南：

<Steps>
  <Step>
    打开一个项目，比如预安装在 Apifox 中的默认 “示例项目”。
  </Step>
  <Step>
    找到并点击界面右上角的环境管理图标 `≡`。
  </Step>
  <Step>
    进入 `全局变量` 区域，创建一个名称为 `my_variable` 的新变量，初始值为 `123`。

    <Background>

    ![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/478928/image-preview)
    </Background>

  </Step>
  <Step>
    点击 `保存` 按钮。
  </Step>
  <Step>
    打开一个接口，比如 “查询宠物详情”，切换到 `运行` 选项卡。
  </Step>
  <Step>
    找到 Path 参数 "petId"，将 `{{my_variable}}` 添加为其值。
  </Step>
  <Step>
    将鼠标悬停在变量名上，以查看其当前值和作用域。

    <Background>

    ![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/478932/image-preview)
    </Background>

  </Step>
  <Step>
    点击 `≡` 图标旁边的环境下拉菜单，切换到 `本地 Mock` 环境。
  </Step>
  <Step>
    点击 `发送` 执行请求。
  </Step>
  <Step>
    你会在界面下半部分看到响应。通过切换到 “实际请求” 选项卡，可以查看实际发送的请求，其中变量被替换为对应的实际值。
      
    <Background>

    ![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/478950/image-preview)
    </Background>


  </Step>
</Steps>

:::highlight purple
要深入了解 Apifox 中的变量，请访问[使用变量](https://docs.apifox.com/global-environment-session-variables.md)。
:::

## 创建和切换环境

“环境” 是开发团队常用的术语，用于区分不同的工作场景，例如“开发环境”、“测试环境” 或 “生产环境”，每个环境对应一台或多台服务器。当客户端选择特定环境时，所有请求都会发送到该环境的服务器。切换环境后，请求则会自动定向至对应的新服务器组。

:::highlight purple
了解更多关于[环境与服务](https://docs.apifox.com/environments-and-services.md)的信息。
:::
