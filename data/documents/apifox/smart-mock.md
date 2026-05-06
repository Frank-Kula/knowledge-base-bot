# 智能 Mock

Apifox 支持根据接口文档直接生成 Mock 数据，无需额外配置，这就是智能 Mock。

智能 Mock 数据来自以下三个来源：

1. 属性名称中对应的 Mock 表达式  
2. 响应定义中属性的 Mock 字段  
3. 响应定义中的 JSON Schema  

## 根据名称自动生成 Mock 数据

智能 Mock 的核心算法会根据属性的类型和名称自动匹配相应的 Mock 数据。Apifox 内置了一系列匹配规则，当类型和名称符合规则时，就会按照规则生成对应的数据。

你可以在 “项目设置 -> 通用设置 -> 功能设置 -> Mock 设置” 中查看这些内置规则。内置规则通过通配符或正则表达式来匹配名称字符串。


<Background>

![CleanShot 2024-11-29 at 16.59.01@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/480527/image-preview)
</Background>


如果内置规则不能满足需求，你可以创建自定义匹配规则。点击 “新建” 创建新的匹配规则，符合规则条件的属性会根据设置的 Mock 表达式生成数据。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/480529/image-preview)
</Background>


如果属性名称没有匹配到任何规则，系统会根据属性类型生成默认的 Mock 值。

## 根据 Mock 字段生成数据

如果响应定义中某个属性的 Mock 字段有值，这个值会覆盖通过名称生成的 Mock 值。在 Mock 字段中，你可以直接填写固定值，或者写入[动态值表达式](https://docs.apifox.com/dynamic-values.md)语句。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/480533/image-preview)
</Background>


## 根据 JSON Schema 生成数据

生成的 Mock 数据会受到 JSON Schema 的约束。

以下是几个示例：

- 如果一个名为 "name" 的字符串字段自动生成了 "Richard"，但 JSON Schema 限制字符串长度为 3-5 个字符，那么最终的 Mock 数据会变为 "Richa"。
- 如果一个名为 "status" 的字符串字段在 JSON Schema 中设置了枚举值（如 "sold"、"pending"、"available"），那么最终的 Mock 数据将从这三个值中随机选择一个。
- 如果一个整数字段设置了最小值和最大值，最终生成的数据会落在这个范围内。
- 如果一个数组字段设置了最小和最大元素数量，最终生成的数据将符合这些限制。

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/480534/image-preview)
</Background>

总的来说，所有的属性设置都会体现在最终的 Mock 数据中，确保数据始终符合 JSON Schema 的规范。
