# 自定义 Mock

Apifox 提供了功能强大的 Mock 功能，让你能够精准控制接口返回响应的 Mock 数据。本文档介绍两种主要的方式来自定义 Mock 数据：

1. **自定义特定字段**：控制响应中的特定字段，其他字段则使用智能 Mock。
2. **完整响应自定义**：通过 Mock 期望定义整个响应内容（支持指定数据、条件数据和动态 Mock 数据）。

## 自定义特定字段

有时，你可能希望为响应中的某些字段定义特定值，同时让 Apifox 自动生成（智能 Mock）其余字段。Apifox 提供了灵活的方式来处理这种情况，下面分别来介绍：

### 1. 直接输入值

在接口定义的 Mock 字段中直接指定固定值，Apifox 将始终为该字段返回这个值，所有未指定的字段将使用 Apifox 的[智能 Mock](https://docs.apifox.com/smart-mock.md) 生成。

**示例：**
<Frame>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/517469/image-preview)
</Frame>

### 2. 使用 Faker.js 动态值

你可以使用 Apifox 的动态值（基于 Faker.js）生成真实的随机数据。使用以下语法：

```
{{$分类.方法}}
```

示例：
- 随机全名：`{{$person.fullName}}`，结果如 `李明`
- 电子邮件地址：`{{$internet.email}}`，结果如 `wang.ming@163.com`
- 产品名称：`{{$commerce.productName}}`，结果如 `高品质塑料自行车`

你可以直接在下拉列表中选择相应的[动态值表达式](https://docs.apifox.com/46262793f0)。
<Frame>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/517473/image-preview)
</Frame>

### 3. 使用带参数的 Faker 方法

你可以为动态值表达式传递参数，以生成更专业化的数据，表达式遵循 Apifox 增强的 Faker.js 语法。  
例如：

- **生成 0 到 10,000 之间的整数：**
  ```
  {{$number.int(min=0,max=10000)}}
  ```
- **生成易读格式的电话号码：**
  ```
  {{$phone.number(style='human')}}
  ```
- **生成 3 的倍数的整数：**
  ```
  {{$number.int(multipleOf=3)}}
  ```
- **从数组中随机选取一个元素：**
  ```
  {{$helpers.arrayElement(['红色','蓝色','绿色'])}}
  ```
- **生成指定范围内的日期（支持自定义格式）：**
  ```
  {{$date.between(from='2024-01-01',to='2024-12-31',format='yyyy-MM-dd')}}
  ```

你可以在[动态值表达式](https://docs.apifox.com/46262793f0)模块文档中查看完整的模块、方法及其参数列表。

### 4. 连接多个动态表达式（生成完整地址示例）

你可以自由组合静态文本和多个动态表达式，生成复杂的字段值。

例如，要在一个字符串中生成真实的完整地址，可以这样写：
```
{{$location.streetAddress}}，{{$location.city}}，{{$location.state}}，{{$location.zipCode}}，{{$location.country}}
```
这将输出类似于以下的结果：
```
"华阳大道188号，成都市，四川省，610000，中国"
```
每个部分都是动态生成的，每次调用 Mock API 时都会创建一个独特且真实的地址。

## 自定义整个 Mock 响应（Mock 期望）

如果你需要返回特定或高度自定义的 Mock 响应，可以使用 “Mock 期望”。这让让你完全控制 Mock 服务返回的内容。

在 “文档模式” 下，可以在接口的 Mock 标签页中设置期望。

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/480977/image-preview)
</Background>

在 “调试模式” 下，也可以在 Mock 标签页中设置期望。

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/480979/image-preview)
</Background>


### 返回指定数据

通过添加一个无参数条件的期望，可以返回固定的数据。

<Steps>
  <Step>
    点击 “新建期望”。
  </Step>
  <Step>
    添加期望名称，“参数条件” 位置留空。
      
    <Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/480984/image-preview)
    </Background>

  </Step>
  <Step>
    在返回数据中填入想要返回的内容并保存。
  </Step>
  <Step>
    复制 Mock URL 来访问这个 API。
  </Step>
</Steps>


### 返回条件数据

Apifox 支持根据不同的请求参数返回不同的 Mock 数据。

当添加多个带有不同条件的 Mock 期望时，Mock 引擎会根据请求参数匹配条件，并按照从上到下的顺序返回第一个匹配的 Mock 期望。

如果没有匹配到任何 Mock 期望，Mock 数据将根据“项目设置 -> 功能设置 -> Mock 设置”中定义的 Mock 优先级返回。

在设置参数条件时，可以选择哪些请求参数作为条件。支持的条件包括 query、path、header、cookie 和 body 参数。填写参数名和条件后，当条件满足时，系统将返回对应的响应内容。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/480985/image-preview)
</Background>

- 设置多个条件时，这些条件会作为交集处理，只有当多个参数同时匹配时，才会匹配到该期望。
- 选择 body 参数时，可以在参数名一栏填写目标字段的 JSONPath 表达式：
    - 第一层属性既可以通过属性名直接匹配，也可以使用 JSONPath 语法进行匹配。
    - 深层属性只能通过 [JSONPath](https://docs.apifox.com/jsonpath.md) 语法进行匹配。
- body 参数仅支持 JSON 格式，不支持 XML 格式。
- 参数条件不支持使用 `{{变量}}`。
- 如果将 body 作为期望条件，实际请求体必须与接口定义匹配。例如，如果接口定义的请求体类型是 form-data，则在 Mock 时参数应放在 form-data 中。
- 可以添加 IP 条件，使某些响应仅对指定的 IP 生效。

### 返回动态 Mock 数据

Mock 期望支持返回动态数据。这个功能支持使用 [Faker.js](https://fakerjs.dev/) 和 [Nunjucks](https://mozilla.github.io/nunjucks/) 语法。

比如下面这段代码：

```json
{
    "data": [
        {% for i in range(0, 20) %}
        {% if i>1 %},{% endif %}
        {
            "id": {{i}},
            "firstname": "{{$person.firstName}}",
            "lastname": "{{$person.lastName}}"
        }
        {% endfor %}
    ],
    "success": true
}
```

这段代码会生成一个响应：
- 包含 20 个数据对象的数组
- 每个对象都有一个 “id”（0 到 19）、一个随机生成的 “firstname” 和一个随机生成的 “lastname”
- “success” 字段设为 true


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/481007/image-preview)
</Background>



`{{$ ... }}` 语法使用 [Faker.js](https://fakerjs.dev/) 生成随机的真实数据，不过与原生语法不同的是，Apifox 将其变成了 `{{$ ... }}` 的引用方式，与原生语法的对比如下：
- **Faker.js**: `faker.person.firstName()`
- **Apifox**: `{{$person.firstName}}`

`{% for ... %}` 语法来自 [Nunjucks](https://mozilla.github.io/nunjucks/)，让你可以创建循环并生成多个数据。

这种方法使你能够创建动态且真实的 Mock 数据，每次请求的返回结果都会有所变化，从而更准确地模拟真实 API 的行为。


:::tip[]
示例中的 `{{i}}` 不是 Apifox 变量，而是 Nunjucks 变量。Mock 期望中不能使用 Apifox 变量。
:::


## 更多功能

- 可以给 Mock 期望添加自定义 Headers。这样就能在 Mock 响应中模拟特定的 HTTP header。

    <Background>

    ![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/481019/image-preview)
    </Background>


- 在 Mock 期望的 “更多设置” 标签页，可以配置额外的响应属性：
   - HTTP 状态码：可以为响应设置自定义的 HTTP 状态码（默认是 200）。这样就能模拟各种 API 响应场景，包括错误状态
   - 响应延迟：可以为响应设置延迟。这个功能对测试应用如何处理较慢的 API 响应很有用

    <Background>

    ![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/481022/image-preview)
    </Background>


- 在期望列表中，你可以通过开关控制每个期望值在本地 Mock 和云端 Mock 环境中的启用状态。


    <Background>

    ![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/481023/image-preview)
    </Background>


