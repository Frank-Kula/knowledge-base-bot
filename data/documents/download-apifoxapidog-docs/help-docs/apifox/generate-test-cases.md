# 生成测试用例

:::tip[关于 AI 功能]

1. AI 功能默认关闭，你需要手动 [启用 AI 功能](https://docs.apifox.com/enable-ai-features) 才可以开始使用（请确保 Apifox 版本`≥2.7.37`）。

2. AI 功能免费提供，但不内置 AI 模型，你需要自行 [添加 AI 模型](https://docs.apifox.com/enable-ai-features#%E9%85%8D%E7%BD%AE-ai-%E4%BE%9B%E5%BA%94%E5%95%86) 并配置对应的 API Key。
:::

可以让 AI 基于当前接口文档快速生成大量测试用例，用以验证单接口的功能响应、规范、稳定和安全情况。同时，可按照用例分组、用例类型管理用例。

你可以在某个接口文档页中，切换至 “测试用例” 标签下，可以看到 “通过 AI 生成” 的功能入口，点击即可开始使用。


<Background>

![CleanShot 2025-09-23 at 10.50.41@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/576193/image-preview)
</Background>


## 配置生成用例

点击 “通过 AI 生成” 的功能入口后，从右侧会滑出生成用例的配置窗口。你可以按照正向、负向、边界值、安全性及其相关小项，勾选你需要生成的用例类型。

<Background>

![CleanShot 2025-09-23 at 10.55.41@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/576197/image-preview)
</Background>



## 配置鉴权凭证

如果本接口存在鉴权方式，配置时将引用 “鉴权凭证”，此时你可以更改合适的鉴权值。密钥值将在本地加密后传递给 AI 供应商，生成用例后本地自动解密，方便快速验证有效鉴权值的同时保障信息安全。

<Background>

![CleanShot 2025-09-23 at 10.58.50@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/576200/image-preview)
</Background>


## 输入更多要求及其他

正式生成前，你可以在底部输入框，输入更多生成要求，以加强生成准确性。同时，在窗口左下角，可配置生成数量，最大支持一次性生成 80 条用例。右下角可以变更大语言模型和供应商。


<Background>

![CleanShot 2025-11-26 at 18.34.04@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/597950/image-preview)
</Background>

可以先编辑确认用例列表和描述，再生成用例详情。

<Background>
![](https://cdn.apifox.cn/uploads/help/202511251444192.gif)
</Background>

基于当前的接口测试用例，通过 AI 补充生成更多测试用例。

<Background>
![](https://cdn.apifox.cn/uploads/help/202511251612916.gif)
</Background>



## 生成并采纳用例

点击生成，AI 基于接口文档和配置要求，正式开始生成用例。生成完成，点击具体用例，可以展开查看用例请求参数、修改用例名、调整分组。


<Background>
![](https://cdn.apifox.cn/uploads/help/202509231126705.gif)
</Background>



点击 “运行”，可以通过响应确定用例是否符合预期。点击 “采纳”，本用例将复制至接口文档的 “测试用例” 标签下。点击 “废弃”，视为不需要本用例。你可以全选或按需勾选用例，批量执行上述操作。


<Background>

![CleanShot 2025-09-23 at 11.30.47@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/576211/image-preview)
</Background>




:::tip[]
使用技巧：同时开启多个生成任务，通过不同模型、供应商、配置要求，快速对比和验证生成效果，高效采纳用例。
:::
