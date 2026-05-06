# 动态值

在 Apifox 中调试接口时，如果经常需要在请求参数、请求体中构造值、名称、地址或其他数据，这时“动态值”功能就派上用场了。


动态值允许你在每次发送请求时，根据预定义的规则生成一个新值。这有助于简化调试过程，并确保每个请求包含唯一的数据。


## 应用场景

动态值在 API 测试中有广泛的应用。以下是一些典型示例：

- **模拟真实数据：** 你需要测试你的 API 如何处理不同类型的数据，例如各种格式的用户名、地址或电子邮件地址。使用动态值，你可以轻松生成大量类似于真实场景的测试数据，从而提高测试覆盖率。
- **生成唯一值：** 在某些测试场景中，你需要确保数据的唯一性，例如生成订单号、用户 ID 或交易 ID。动态值可以根据时间戳或随机数生成唯一值，防止数据冲突并确保测试结果准确。
- **简化数据处理：** 不需要为每次测试运行手动修改数据，使用动态值自动生成所需的数据。这可以节省你大量的时间和精力，提高测试效率。


## 使用入门

> Apifox 版本号需 `>=2.6.15`

<br />

1. 在接口中，切换到 “运行” 选项卡。
   
2. 对于要动态化的参数，可以先删除原始值，然后单击值右侧的 <Icon icon="ph-bold-magic-wand"/> **魔棒** 图标。 

    <Background>
    ![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/477670/image-preview)
    </Background>


3. 点击 “**数据生成器**”，然后选择所需的动态值类型，例如`名字`。

 
    <Background>

    ![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/477671/image-preview)
    </Background>


4. 点击 “插入” 将[动态值表达式](https://docs.apifox.com/dynamic-value-expressions.md)插入到参数中。

  
    <Background>

    ![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/477672/image-preview)
    </Background>



5. 点击 “发送”，你可以在 “实际请求” 中看到发送的实际名称。
      
 
    <Background>

    ![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/477673/image-preview)
    </Background>


6. 再次发送请求，将动态生成一个新的名字。
  
:::tip[]
旧版的动态值表达式是形如`{% mock 'name' %}`的形式，这种使用方式后续将会废弃。建议你将 Apifox 升级到最新版本，并开始使用新版的[动态值表达式](https://docs.apifox.com/dynamic-value-expressions.md)。
:::

## 在 JSON 请求体中使用动态值

如果需要发送 JSON 请求体，并且 JSON 中的某些值需要动态生成，你也可以使用动态值。

<br />

1. 找到一个带有 JSON 请求体的 POST 接口，并切换到**运行**选项卡。
  
2. 在 JSON 请求体中，单击 “**自动生成** -> **仅生成字段名**”，你将获得在 API 文档中定义的属性名称。

   
    <Background>

    ![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/477674/image-preview)
    </Background>

    
3. 将光标定位在正确的位置，单击 “**动态值**”，然后选择 “**数据生成器**”。

   
    <Background>

    ![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/477675/image-preview)
    </Background>

    
4. 选择适当的数据类型，然后单击 “**插入**”。

5. 为所有字段添加值。

6. 单击 “发送”。你可以在 “**实际请求**” 部分中看到实际发送的 JSON 请求体。
      
  
    <Background>

    ![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/477677/image-preview)
    </Background>

      
7. 如果再次发送请求，动态值将生成新的 JSON 请求体。
  


## 在自定义表达式中使用动态值

如果需要自定义一串信息，并且信息中有一些值需要动态生成，你还可以单击 “自定义表达式” 并输入[动态值表达式](https://docs.apifox.com/dynamic-value-expressions.md)。自定义表达式是遵循 [Nunjucks](https://mozilla.github.io/nunjucks/templating.html) 模板引擎语法的，你可以查阅他们的文档。

1. 单击 “动态值” 图标，然后选择 “**自定义表达式**” 以打开输入框。

   
    <Background>

    ![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/477678/image-preview)
    </Background>

    
2. 通过拼接等方法输入 “动态值表达式” 来生成预期内容，你可以在下方实时预览生成的信息。
      
  
    <Background>

    ![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/477679/image-preview)
    </Background>

    
3. 单击 “插入”，你可以在参数值部分看到自定义表达式。
      
  
    <Background>

    ![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/477680/image-preview)
    </Background>


4. 除此之外，你还可以使用 [Nunjucks](https://mozilla.github.io/nunjucks/templating.html) 模板引擎语法来辅助生成。
   例如：

    ```js
       {% for i in range(0, 20) %}
          {
              "id": {{i}},
              "firstname": "{{$person.firstName}}",
              "lastname": "{{$person.lastName}}"
          }{% if i!=19 %},{% endif %}
      {% endfor %}
    ```

  
    <Background>

    ![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/477682/image-preview)
    </Background>

    这将生成 20 个随机用户数据，其中包含随机的名字和姓氏。
  
    <Background>

    ![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/477683/image-preview)
    </Background>



:::tip[]
常见的自定义表达式，你可以到[动态值表达式](https://docs.apifox.com/dynamic-value-expressions.md)模块查看更多详情。
:::



## 手动插入动态值

在需要插入动态值的输入字段中，你可以输入 `{{$` 来触发动态值列表。


<Background>
 
![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/477684/image-preview)
</Background>


你可以使用以下方法快速定位所需的变量：
   - **完整输入：** 准确输入完整的动态值名称，例如 `$timestamp`。
   - **模糊匹配：** 输入部分关键词，例如 `time`，系统会自动过滤并显示匹配的动态值。

选择目标动态值将其插入到输入字段中。


## 数据生成器

使用数据生成器，你可以根据需要生成任何自定义数据。


将鼠标悬停在参数输入字段上，单击出现的魔棒图标以打开 “数据生成器” 面板。

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/477685/image-preview)
</Background>


你可以在面板中使用两种方法找到所需的动态值：

   - **按变量类型搜索：** 通过选择动态值类型（例如日期、字符串、数字等）快速定位所需的变量范围，提高搜索效率。
        <Background>
        ![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/477686/image-preview)
        </Background>

   - **按关键词搜索：** 在顶部的 “类型” 输入框中输入关键词（例如时间、字符串等），系统会自动过滤并显示匹配的动态值，方便你快速定位。
        <Background>

        ![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/477687/image-preview)
        </Background>


选择所需的动态值后，你可以通过以下操作对其进行进一步的细化，以满足更精细的数据生成需求：


   - **添加方法：** 一些动态值支持附加方法，例如 `{{$date.now}}` 可以使用 `addDays` 方法添加天数以生成特定日期的数据。

        <Background>

        ![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/477688/image-preview)
        </Background>


   - **添加处理函数：** 所有动态值结果都可以使用函数进行处理，例如，使用 `md5` 函数对字符串进行加密以生成满足安全要求的测试数据。

        <Background>

        ![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/477689/image-preview)
        </Background>


“表达式” 区域清楚地显示你当前选择的动态值类型、方法和函数，方便你进行检查和修改。


“预览” 区域实时显示动态值生成的示例数据。单击 “预览” 区域末尾的 “刷新” 按钮可以生成新的示例数据，方便你查看数据生成的效果。


单击 “预览” 区域中的示例数据可以自动复制内容，方便你将其粘贴到需要的位置。

## 固定值

用于将一段固定文本包裹在“动态值”语法中，便于在其后添加处理函数。常见用途包括对常量值进行 **MD5 加密**、**Base64 编码**、**字母大小写转换** 等操作。

使用时，只需填写原始值，并在语法中手动添加所需的处理函数，系统会在执行时自动完成加密或转换。

<Background>
<img src="https://api.apifox.com/api/v1/projects/5097254/resources/579932/image-preview" style="width: 360px;" />
</Background>



如果仅需填写常量值且无需任何处理，建议直接写入文本，无需使用“固定值”。



## 在自定义脚本中使用动态值

Apifox 支持在自定义脚本中生成动态值。你可以使用 `pm.variables.replaceInAsync(variableName: String): function` 方法将字符串中的“动态值表达式”替换为实际生成的值。该方法返回一个 Promise，因此在调用时需要配合 `await` 使用。

以下是一个生成随机姓名的示例：

```js
// 定义一个包含动态值表达式的字符串
let stringWithVariable = "Hello, {{$person.fullName}}";

// 使用 replaceInAsync 方法替换 {{$person.fullName}} 占位符
let realValueString = await pm.variables.replaceInAsync(stringWithVariable);

console.log(realValueString); // 输出类似 "Hello, John Doe"
```

在脚本运行时，`{{$person.fullName}}` 会被自动替换为一个真实的姓名。


<Background>
![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/494952/image-preview)
</Background>


:::info[]
- 想了解更多关于 `pm.variables` 的使用方法，请查阅 [pm.variables 文档](https://docs.apifox.com/5580997m0#pmvariables)。
- 如需查看所有支持的动态值表达式及其用法，请参考 [动态值表达式文档](https://docs.apifox.com/5778140m0)。
:::


## 设置数据语言/国家

Apifox 的动态值支持生成不同语言的示例数据，以满足你在多语言环境中的测试需求。操作方法如下：

1. 打开 “数据生成器” 面板。
   
2. 对于 “日期” 和 “时间” 以外的动态值类型，单击动态值类型右上角的切换组件，然后选择相应的目标语言即可。

  
    <Background>

    ![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/477690/image-preview)
    </Background>


3. 对于 “日期” 和 “时间” 的动态值类型，你可以使用 `format` 和 `locale` 方法指定语言和格式。

    <Background>

    ![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/477691/image-preview)
    </Background>


## 强大的日期操作和格式化

Apifox 不仅仅提供丰富的日期和时间动态值，它还致力于简化你的开发过程。以下是你可以轻松实现的一些功能：

- **灵活的时间调整：** 使用 `add` 方法，你可以轻松地根据当前时间添加或减去时间单位。例如，`{{$date.now|addHours(-3)}}` 将返回比当前时间早 3 小时的日期。 

  
    <Background>

    ![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/477692/image-preview)
    </Background>



* **多样化的日期格式化：** 使用 `format` 方法，你可以根据需要将日期格式化为不同的格式。例如，`{{$date.now|formatISO}}` 将根据 ISO 8601 标准格式化日期。 

    <Background>

    ![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/477693/image-preview)
    </Background>


* **精确的时区控制：** 通过设置 `timezone` 参数，你可以轻松控制日期的时区。例如，`{{$date.now|format('yyyy-MM-dd HH:mm:ss',timezone='America/Port-au-Prince')}}` 将返回 `UTC+8:00` 时区中当前时间对应的日期。 

  
    <Background>

    ![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/477694/image-preview)
    </Background>



## 常见动态值

为了帮助你更好地使用 Apifox 动态值，我们整理了完整的动态值清单和示例说明。你可以点击[动态值表达式](https://docs.apifox.com/dynamic-value-expressions.md)模块查阅，快速找到你需要的动态值及其使用方法。

:::tip[]
你也可以在 Apifox 内，将鼠标悬停在动态值表达式上，查看该动态值的简要说明和示例。 
:::


