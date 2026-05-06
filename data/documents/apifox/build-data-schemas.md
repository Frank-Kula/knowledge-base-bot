# 构建数据模型

## 编辑数据模型

Apifox 提供可视化的数据模型编辑组件，用于设计 API 中的 `JSON` 或 `XML` 数据结构，基于 [JSON Schema](https://json-schema.org/) 标准构建。

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/476151/image-preview)

</Background>

每个数据模型从一个根对象开始，你可以向其添加参数，逐步构建结构。

**构建步骤：**

<Steps>
  <Step title="添加参数">
    点击对象旁的 `+` 图标，添加子参数。
     
<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/551531/image-preview)
</Background>

  </Step>
  <Step title="命名参数">
    输入参数名称（键名）。
  </Step>
  <Step title="选择类型">
    选择数据类型，或引用已有的数据模型。
  </Step>
  <Step title="设置属性">
    配置默认值、格式、是否必填等信息。
  </Step>
  <Step title="管理结构">
    拖动排序、复制、删除字段，添加描述等。
  </Step>
</Steps>

:::highlight purple
你还可以通过导入数据库表结构或 JSON 数据来创建模型：[查看方法](https://docs.apifox.com/generate-from-json.md)
:::


## 参数类型说明

Apifox 支持以下 JSON Schema 类型：

* **null**：`null` 值
* **boolean**：布尔值 (`true` / `false`)
* **object**：键值对对象
* **array**：数组
* **number**：数字类型
* **string**：字符串

此外，还支持：

* **引用数据模型**：复用已定义的其他数据模型
* **any**：可为任意类型
* **组合模式**：支持 `allOf`、`anyOf`、`oneOf` 等组合方式
* **自定义**：手动编写 JSON Schema

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/551532/image-preview)
</Background>


### 引用数据模型

你可以在模型中嵌套引用其他数据模型，适用于公共结构复用。

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/476155/image-preview)

</Background>

引用模型后：

* 原始模型更新后，引用模型也会同步更新
* 引用字段不可直接编辑，如需修改，可：

  * 点击模型名跳转原始模型编辑
  * 点击「解除关联」转为独立字段，可自由编辑
  * 解除后，原始模型的修改将不再影响此字段

你还可以通过「隐藏字段」禁用部分非必填参数。

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/476157/image-preview)

</Background>



### 数据模型组合

当一个字段可能有多种结构时，可使用组合模式：

* `allOf`：满足全部结构
* `anyOf`：满足其中任意一个
* `oneOf`：仅满足一个结构

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/476161/image-preview)

</Background>

组合后，名为“0”和“1”的子参数将显示在该参数下，可分别配置。

API 文档中也会以对应格式展示组合结构。

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/476167/image-preview) 

</Background>


### 自定义 JSON Schema

如需更灵活控制结构，可切换到「自定义」，手动编辑 JSON Schema：

<Background>
    <p style="text-align: center">
    <img src="https://api.apifox.com/api/v1/projects/5097254/resources/476172/image-preview" style="width: 340px" />
    </p>
</Background>



## 参数设置

每个参数旁会显示多个按钮：

<Frame>
![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/476173/image-preview)
</Frame>

* `*`：是否为必填
* `N`：是否允许为 `null`
* `设置`：打开类型编辑器，配置更多参数属性

### 可配置项

* 默认值
* 示例值
* 枚举值
* 常量
* 最小长度
* 最大长度
* 正则表达式约束
* XML 设置（如开启 XML 模式）
* 其他...

<Background>
    <p style="text-align: center">
    <img src="https://api.apifox.com/api/v1/projects/5097254/resources/476174/image-preview" style="width: 340px" />
    </p>
</Background>

配置项将应用于：

1. 自动生成请求/响应示例
2. API 文档展示结构
3. 请求体自动填充
4. 响应校验
5. Mock 服务生成数据



### 枚举设置

支持为 `string` / `integer` / `number` 类型添加枚举值，并设置每项描述，支持批量编辑：

<Background>
    <p style="text-align: center">
    <img src="https://api.apifox.com/api/v1/projects/5097254/resources/476179/image-preview" style="width: 340px" />
    </p>
</Background>


:::tip[]
了解更多：
- [数组如何配置枚举？](https://docs.apifox.com/6802030m0)
- [如何定义公共的枚举？](https://docs.apifox.com/5837930m0)
:::


### Mock 值

你可以为字段指定 Mock 值，用于生成 Mock 数据：

* 可输入固定值
* 可使用 [Faker.js](https://fakerjs.dev/api/) 表达式，支持下拉选择

Mock 值优先于类型设置中的默认生成规则。

<Background>
![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/476181/image-preview)
</Background>



### XML 设置

启用 XML 模式后，可设置标签名、命名空间、是否为属性等。

<Background>
![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/476186/image-preview)
</Background>

---

## 其他功能


* **从 JSON/XML/数据库生成**：[快速构建数据模型](https://docs.apifox.com/generate-from-json.md)
* **预览**：展示基于数据模型的自动生成示例
* **生成代码**：可以生成多种编程语言中的数据结构定义代码，了解更多关于[生成代码](https://docs.apifox.com/generate-code.md)的信息
* **JSON Schema 编辑器**：支持直接查看和修改底层结构

<Background>
![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/476190/image-preview)
</Background>


## 常见问题

<Accordion title="多个地方用到相同枚举，怎么保持一致？" defaultOpen>
建议将该参数封装为单独的数据模型，在多个接口中引用，确保统一。
</Accordion>

