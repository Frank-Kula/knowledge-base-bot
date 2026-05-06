# 生成请求

在创建或导入 API 之后，可以生成并发送请求以进行调试和校验。

## 生成请求参数

在 Apifox 的 `文档模式` 中，一旦你在 `修改接口` 标签中指定了一个接口，可以点击 `运行` 标签切换到发送请求的界面。在这里，系统会根据你定义的接口自动生成相应的请求。

对于 Path 参数、Query 参数、Headers 信息以及类型为 `form-data` 或 `x-www-form-urlencoded` 的请求体，如果你指定了示例值，这个示例会自动填充到 `运行` 界面的 `参数值` 字段，作为初始请求参数值。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/477593/image-preview)
    

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/477594/image-preview)
</Background>


:::tip[]
如果在 `修改接口` 标签页中修改并保存了参数名称、描述、类型或示例等内容，`运行` 标签页中的相应字段也会随之更新。`修改接口` 标签页中的任何更改都会在整个开发过程中反映出来，保持一致性和准确性。
:::

## 生成请求体

在 Apifox 中，你可以为 `JSON`、`XML` 等类型的请求体自动生成数据，无需手动构建。

### 请求体示例与初始内容

当你在 `修改接口` 标签页中定义了请求体示例时，这些示例会在 `运行` 标签页中作为初始请求体内容出现。如果没有定义示例，请求体字段将保持空白，但你可以通过点击 `自动生成` 来创建符合要求的请求体结构。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/500009/image-preview)
</Background>


### 自动生成选项

> Apifox 版本需大于 `2.7.0`

Apifox 提供了多种数据生成选项，以满足不同场景的需求。你可以在 `自动生成功能` 的下拉菜单中选择不同的生成方式：

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/500010/image-preview)
</Background>


**1. 使用请求示例**

- **行为**：随机选择一个预定义的请求示例
- **适用场景**：快速切换不同业务场景（如正常/异常请求）

**2. 发送时自动变化**

- **行为**：每次发送请求时重新生成 Mock 数据
- **适用场景**：动态数据需求
- **注意**：启用后请求体将不可编辑，请求体内容将锁定为只读状态


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/500019/image-preview)
</Background>



**3. 优先使用字段示例值**

- **行为**：优先填充字段级示例值，无示例时使用 Mock 数据
- **适用场景**：部分字段需要固定值，其他字段动态生成

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/500012/image-preview)
</Background>

**4. 优先使用字段默认值**

- **行为**：优先填充字段级默认值，无默认值时使用 Mock 数据
- **适用场景**：需要保留预设值的调试场景

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/500013/image-preview)
</Background>

**5. 使用 Mock 生成值**

- **行为**：完全基于智能 Mock 规则生成
- **适用场景**：快速生成完整测试数据

**6. 仅生成字段名**

- **行为**：仅生成字段结构，值留空
- **适用场景**：需要手动填写特定值的测试场景




## 插入动态值

可以使用 `动态值` 为请求参数和请求体生成值。这允许动态值在每次发送请求时自动 Mock 并插入到请求中。

在每个请求参数的输入框旁边，你会看到一个 <Icon icon="ph-bold-magic-wand"/> **魔法棒** 图标，点击这个图标将插入一个动态值。

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/477610/image-preview)
</Background>



同样，在请求体中，你可以点击 <Icon icon="ph-bold-magic-wand"/> **插入动态值** 按钮，在 JSON 或 XML 请求体中插入动态值。


<Background>
<p style="text-align: center">
    <img src="https://api.apifox.com/api/v1/projects/5097254/resources/477612/image-preview" style="width: 340px" />
</p>
</Background>



:::highlight purple
了解更多关于[动态值](https://docs.apifox.com/dynamic-values.md)的信息。
:::

## 发送请求

点击 `发送` 来发送请求。
:::highlight purple
了解更多关于[发送请求](https://docs.apifox.com/send-request.md)的信息。
:::
