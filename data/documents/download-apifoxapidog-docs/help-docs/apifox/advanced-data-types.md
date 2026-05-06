# 高级数据类型


## HashMap、字典、关联数组

HashMap，也被称为 Map、字典或关联数组。它是一组键值对，其中键的名称可以是任意内容，而不是预先定义好的。

OpenAPI 规范支持定义键类型为字符串的 HashMap。方法是把元素类型设定为 `object`，然后使用 `additionalProperties` 关键字来指定键值对中属性值的类型。

假设现在有一个用户信息查询接口，返回的数据格式有以下要求：

1. 返回的数据是一个对象
2. 对象的子元素是一个 HashMap 键值对
3. 用户 ID 为键，用户信息为值

在 Apifox 中编辑 API 文档时，可以这样定义：

- 新建数据模型，并将其命名为 `UserProfiles`
- 在 `UserProfiles` 数据模型中，指定根节点为 `object` 类型。然后点击“高级配置”，将额外字段配置为“允许”，轻点右侧的“配置”按钮。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/488709/image-preview)
</Background>

- 在弹出的界面内，添加符合要求的用户信息，用户姓名和邮箱用作 object 的字段。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/488710/image-preview)
</Background>

- 在 API 文档的返回响应中，根节点引用该数据模型。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/488711/image-preview)
</Background>

- 点击保存，然后你可以在接口文档内的返回响应示例中看到符合定义的数据结构和示例值。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/488713/image-preview)
</Background>

## 包含额外字段的对象

随着实际开发工作的迭代，接口返回的对象可能较之前原定对象多出额外的字段。根据 OpenAPI 规范，这种情况也可以使用 **“额外字段”** 功能进行处理。

假设现在有一个用户信息查询接口，通过用户 ID 查询用户信息时，原定的响应返回字段为 `name` 和 `email`。现随着系统升级，希望包含其它字段。

在编辑 API 文档时，可以这样定义：在数据模型的根节点中，点击“高级设置”，将“额外字段”设置为允许，字段值的类型设置为 "any"。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/488715/image-preview)
</Background>


然后你可以在 API 接口文档中看到符合定义的数据结构和示例值。

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/488716/image-preview)
</Background>

## 元组

通常情况下，数组的内部元素必须为同一种类型，而元组则可以包含不同类型的数据。如果希望定义一个元组，里面的值同时包含 string 和 integer 类型，即诸如 `(0,"A",2,"C")` 这样的数据，那么可以在数据模型中，将元素类型设定为 `array`，然后把 `items` 的类型设定为组合模式中的 `anyOf`, 再依次添加类型为 `string` 和 `integer` 的子元素。

> 如果你希望在生成示例时生成多个元素，请在根节点的高级设置中指定最小和最大元素个数。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/488717/image-preview)
</Background>


保存后，在 API 文档中点击自动生成数据，即可看到符合定义的数据结构和示例值。


<Background>
 
![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/488718/image-preview)
</Background>


在文档中的返回响应内也可以看到元组的示例值。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/488719/image-preview)
</Background>


