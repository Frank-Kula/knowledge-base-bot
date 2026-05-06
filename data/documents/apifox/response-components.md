# 响应组件

在 API 设计中，成功的 `200 OK` 响应因不同接口输出的数据需求各不相同，而类似 `400 Bad Request` 和 `404 Not Found` 这样的错误响应则往往在不同接口中保持一致。

Apifox 针对这种共性提供了 “响应组件” 功能，能够重复使用预定义的错误响应，让 API 文档编写更高效，同时保证 API 行为一致性。

:::highlight purple
Apifox 的响应组件与 [OAS 规范中的组件](https://swagger.io/docs/specification/describing-responses/)兼容。
:::

## 添加响应组件

在 `接口管理` 模块的左侧目录树中，找到 `组件库` 部分，在 `响应组件` 下点击 “新建响应” 以创建新的响应组件。


<Background>
![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/476086/image-preview)
</Background>


创建响应组件类似于在定义 API 时指定响应部分，需要包括 `HTTP 状态码`、`内容格式`、`响应数据结构` 和 `示例`。具体指导可参考[新建接口](https://docs.apifox.com/create-an-api.md)中的响应部分。

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/476088/image-preview)
</Background>


响应组件的独特功能：
- **新增接口时默认添加**：如果选择“是”，该组件将默认添加到所有新创建的接口中。

:::highlight purple
已存在的接口不会受此设置影响。
:::

## 引用响应组件

在接口的 `响应` 部分，可以引用预定义的响应组件。


<Background>
  ![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/476090/image-preview)
</Background>


- 引用的响应组件无法在接口内修改。必须在原始响应组件中进行更改，且更改会影响所有引用该组件的接口。
- 如果希望修改引用的响应组件，可以选择 `解绑`，这样组件将变为普通的可编辑响应，后续更改不会影响已取消引用的内容。


    <Frame>
    ![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/476091/image-preview)
    </Frame>


- 在一个接口内，组件只能引用一次，不能存在多个同一组件的实例。

### 批量操作

可以批量将已存在的响应组件 `添加` 到选定的接口，或批量从选定的接口中 `移除`。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/476094/image-preview)
</Background>

- 如果所选接口已包含该响应组件，则不会重复添加。
- 如果所选接口未包含该响应组件，移除操作将不生效。

## 默认响应模板

许多团队在响应结构上都有标准化要求。可以利用默认响应模板功能，保持团队内固定的响应结构作为默认模板。

在左侧目录树的 `组件库` 模块中，可以找到并使用 `默认响应模板` 功能。


<Background>
<p style="text-align: center">
    <img src="https://api.apifox.com/api/v1/projects/5097254/resources/476096/image-preview" style="width: 240px" />
    
</p>
</Background>



创建新接口时，该模板的内容将作为初始响应。

- 更改默认响应模板只会影响新接口，已存在的接口不受影响。
- 默认响应模板仅存在一个，无法添加或删除。

初始的默认响应模板是 `200` 成功响应，内容类型为 JSON，数据结构为一个空的 Object 节点。

<Background>
![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/476095/image-preview)
</Background>


## 常见问题

<Accordion title="我可以将响应组件用作默认响应吗？" defaultOpen>
不可以。响应组件旨在用于通用的错误响应，例如 400、404 等状态码。如果需要使用固定的默认响应，请使用 “默认响应模板”。
</Accordion>

