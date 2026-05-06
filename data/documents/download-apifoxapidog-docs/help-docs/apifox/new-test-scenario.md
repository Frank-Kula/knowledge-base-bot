# 新建场景用例


:::tip[]
原「**测试场景**」已更名为「**场景用例**」。更名仅为概念澄清，功能和使用方式不受影响。
:::

在 Apifox 自动化测试中，场景用例是最基本的单元，类似于 Postman 中的 Flows 或 自动化集合运行。当你需要通过逻辑编排构建复杂的业务流程、处理步骤间的数据产出与传递时，可以创建一个场景用例。

场景用例支持按顺序组织请求，并提供了逻辑编排（If、For、Wait）、动态参数、步骤间数据传递以及自动生成测试报告等核心能力，同时支持通过 CLI 集成到 CI/CD 流水线。


## 新建场景用例

在项目中点击左侧菜单栏中的 “自动化测试”，点击搜索栏右侧的 `+` 号按钮，选择所归属的目录与设置优先级后完成创建。


<Background>

![CleanShot 2026-02-09 at 12.21.34@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/622956/image-preview)
</Background>


若希望调整场景用例的所在目录，可以在创建场景用例时点击 “目录” 中的 “新建目录” 按钮或选择已有目录进行调整。


<Background>

    <img src="https://api.apifox.com/api/v1/projects/5097254/resources/622957/image-preview" style="width: 340px" />

</Background>


你也可以给场景用例设置标签，在左上角的搜索框中通过标签来搜索场景用例。

<Background>

    <img src="https://api.apifox.com/api/v1/projects/5097254/resources/481581/image-preview" style="width: 340px" />

</Background>


## 在场景用例中添加测试步骤

创建场景用例后可以在其中添加测试步骤。测试步骤中支持导入接口、接口用例、自定义请求和从 cURL 导入接口，并且你还可以在步骤中设置测试条件等附加操作。

进入场景用例后，点击 “添加步骤” 并添加接口。你可以选择 “从接口导入” 和 “从接口用例导入”。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/481584/image-preview)
</Background>


### 从接口导入

你可以从当前项目中导入接口作为场景用例的步骤。导入接口时有两种同步模式：“手动同步” 和 “自动同步”。具体说明请参阅[从接口/用例同步数据](https://docs.apifox.com/sync-from-endpoint-or-test-case.md)。

- **手动同步**

  在此模式下，项目内的 “接口文档” 发生数据变化时，测试步骤中的接口数据不会自动更新。只有当测试人员点击 “手动同步” 按钮时，测试步骤中的接口数据才会与接口文档中的数据同步。如果测试步骤中的接口数据发生了变化，点击 “手动同步” 按钮后，数据不会同步回接口文档，而是重新抓取接口文档中的数据并与之同步。

- **自动同步**

  在此模式下，当项目内的 “接口文档” 数据发生变化时，测试步骤中的接口数据将自动更新。

  
    <Background>

    ![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/481587/image-preview)
    </Background>


> 如果你需要在一个场景用例中测试其它项目的接口，可以参考[跨项目导入接口/用例](https://docs.apifox.com/import-apis-or-cases-cross-projects.md)。

### 从接口用例导入

你可以选择从当前项目或其他项目导入接口用例。导入接口用例时有两种模式：分别是 **“复制”** 和 **“引用”** 模式。

- **复制**

    以 “复制” 方式导入接口用例时，接口用例中的参数也会一并复制到测试步骤中，且与原项目内的接口用例数据相互独立。两者的改动互不影响。

- **引用**

    以 “引用” 方式导入接口用例时，将直接使用原项目内的接口用例进行请求。

  
    <Background>

    ![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/481588/image-preview)
    </Background>


  如果是从接口用例引用的测试步骤，点击进入这个步骤后，会显示一个明确的提示。这个提示会告知你：修改当前步骤的内容不仅会影响原始的接口用例，还会同时影响所有引用了该接口用例的其他测试步骤。

  
    <Background>

    ![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/481590/image-preview)
    </Background>




### 添加自定义请求

在业务流程中，可能会遇到需要调用外部项目接口的情况，例如调用第三方支付接口。你可以在测试步骤中添加自定义请求，自定义请求可以是任意 HTTP 请求类型，包括常见的 GET、POST、PUT、DELETE 等。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/481593/image-preview)
</Background>


### 从 cURL 导入

在实际业务流程中，许多 API 请求以 `cURL` 命令行的形式呈现。你可以将 cURL 请求一键导入到测试步骤中。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/481595/image-preview)
</Background>


### 流程控制条件

你可以在场景用例中新增[流程控制条件](https://docs.apifox.com/flow-control-conditions.md) *（如分组、条件分支、ForEach 循环、For 循环和等待时间）*，以应对更复杂的场景用例和流程配置需求，最终通过自动化测试功能解决复杂场景的测试工作。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/481596/image-preview)
</Background>


### 从其它场景用例导入

你可以将当前项目中其他场景用例的测试步骤或流程控制条件复制导入到当前场景用例。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/481597/image-preview)
</Background>


### 引用其它场景用例

你可以在场景用例中引用其他场景用例，将其作为一个测试步骤。以下是该功能的适用场景：

1. 当业务流程中有一些公共且可复用的步骤时，可以将这些步骤组合成一个小型场景用例，然后在其他较大的场景用例中直接引用。
   
2. 如果需要执行全产品的主流程回归测试，可以在一个场景用例中引用各个子场景用例进行组装，从而实现一键测试全部主流程，完成回归工作。


    <Background>

    ![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/481598/image-preview)
    </Background>


:::caution[]
为防止出现无限循环或场景用例无法正常停止的情况，该功能不可引用当前场景用例本身。
:::


## 编排场景用例

点击任意测试步骤即可进入编排模式。在该模式下，你将拥有更大的操作页面 *（点击左上角的放大图标可将页面方放大）*，便于更高效地填写每个测试步骤的详细内容。页面左侧显示场景用例的整体流程，右侧显示选中测试步骤的详细信息。接口请求和流程组件将根据其类型展示不同的详情。


你可以在此模式中使用“⬆️”“⬇️”按键来快速切换选中的测试步骤。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/481609/image-preview)
</Background>


在编排模式中，你可以同时编辑多个步骤，并通过点击左上角的 “全部保存” 按钮一次性保存所有步骤的详细信息。如果某个步骤的详细内容未保存，该步骤将在左侧列表中标记一个小圆点。请务必注意并及时保存已填写的内容。







