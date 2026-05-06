# 全局/环境/模块/临时变量

变量是 Apifox 中保存和复用数据的重要功能。通过设置变量，你可以在不同环境、接口和脚本中灵活使用相同的值，提升工作效率。

## 什么是变量

变量是数据的符号化表示，避免重复手动输入相同的值。

例如，多个接口使用同一个 token 时，将其设为变量 `{{my_token}}`，在接口中直接引用。当 token 变化时，只需更新变量值，所有引用该变量的地方会自动同步。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/480031/image-preview)
</Background>

变量可用于 URL、请求头、参数值、请求体等任何地方，也可以在自动化测试中传递数据。

## 变量类型与优先级

Apifox 支持以下变量类型：团队全局变量、项目全局变量、模块变量、环境变量、测试数据变量、临时变量。

优先级：**`临时 > 测试数据 > 环境 > 模块 > 项目全局 > 团队全局`**。

例如，如果定义了一个名为 `id` 的环境变量和一个同名的模块变量，执行接口时将使用环境变量的值。

:::tip[]
Apifox 中的变量以字符串形式存储。存储对象或数组时需要用 `JSON.stringify()` 转换，读取时用 `JSON.parse()` 解析。
:::

### 全局变量

全局变量允许在项目内的所有接口、脚本和环境之间共享数据，可在环境管理页左上方设置。有两种类型：


- **项目中共享的全局变量**

    在整个项目内共享使用，适用于项目内接口间的变量流转。例如登录接口提取 token 到项目全局变量中，再给后续业务接口作为鉴权使用。
    
    
    <Background>

    ![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/489167/image-preview)
    </Background>

- **团队中共享的全局变量**

    在整个团队内共享使用，适用于跨项目的变量流转。比如登录项目获取的 token 给其他项目使用。
    
    <Background>
    ![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/489168/image-preview)
    </Background>

:::highlight purple 💡
1. 在项目的环境管理页面中，仅能查看已有的团队全局变量，以及修改这些已有变量的本地值，**不可以**添加、删除团队全局变量和修改现有变量的变量名与远程值。
   
2. 在运行接口时，通过使用[前后置操作](/doc-5580997#pmglobals)提取、设置变量到团队全局变量，仅能修改已有变量的本地值，**不可以**添加、删除团队全局变量和修改现有变量的变量名与远程值。
  
3. 如想进行此类操作，需要拥有团队管理员权限并在[“团队资源 -> 团队变量”](https://docs.apifox.com/team-variables.md)页中进行操作。

:::

### 模块变量

在模块中设置的变量，Postman 导入的 Collection 变量需要导入到此模块变量中。


<Background>

![CleanShot 2025-08-15 at 16.40.38@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/556294/image-preview)
</Background>




### 环境变量

**环境变量**使你能够根据特定环境 （如本地开发、测试或生产环境）调整工作配置。切换环境时，当前环境的环境变量值将生效。每次只能激活一个环境。

<Background>

![CleanShot 2025-08-15 at 16.43.31@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/556299/image-preview)
</Background>


### 测试数据变量

**测试数据变量**来源于外部 CSV 或 JSON 文件，用于测试场景或 Apifox CLI 中的数据驱动测试。这些变量值仅在测试运行期间有效。

<Background>

![CleanShot 2025-08-15 at 16.46.10@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/556302/image-preview)
</Background>


### 临时变量

**临时变量**仅在单个接口或测试场景的运行期间有效，运行结束后会消失。它适用于临时覆盖其他类型的变量，并且不会在执行后保留值。

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/556306/image-preview)
</Background>



## 远程值和本地值

每个变量都有一个远程值和一个本地值。

- **远程值：** 保存在 Apifox 服务器上，与团队成员同步共享的值。适合团队协作，会被团队成员访问。

- **本地值：** 仅保存在本地设备，不与服务器同步，也不会共享给团队成员。适合存储密码、token 等敏感信息。


    <Background>

    ![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/480037/image-preview)
    </Background>


当本地值为空时，将使用远程值；一旦设置了本地值，将优先使用本地值。点击本地值旁的链接图标 `🔗` 可重新绑定到远程值。

:::tip[]
- 由于 `本地值` 仅存储在本地，使用清理软件清除 Apifox 文件缓存时，可能会导致 `本地值` 被删除，请谨慎操作。
- 更换设备时，`本地值` 不会随账号自动迁移。你可以通过导出和导入环境功能来迁移本地值。
- 如果使用 Apifox Web 版，`本地值` 存储在浏览器的数据中。
:::

### 在 Apifox CLI 中使用变量 

在 Apifox 客户端设置好自动化测试的测试场景后，你可以在任何机器上使用 Apifox CLI 运行该场景。

需要注意的是，在客户端运行时使用的是变量的 `本地值`，而在 CLI 中运行时使用的是变量的 `远程值`。如果客户端和 CLI 的运行结果不同或出现错误，通常是由于这一差异导致的。

:::highlight purple
了解更多关于 [Apifox CLI](https://docs.apifox.com/install-and-run-cli.md) 的信息。
:::


## 设置变量

设置变量的方法有多种，具体取决于变量值的来源。包括在环境管理中设置、通过前后置操作提取、执行数据库操作或自定义脚本设置。

### 方法 1：在 “环境管理” 中设置

你可以在 “环境管理” 弹窗中设置全局变量和环境变量的值，步骤如下：

<Steps>
  <Step>
    点击界面右上角的 “环境管理” 按钮 `≡`
  </Step>
  <Step>
    切换到 “全局变量” 或特定环境
  </Step>
  <Step>
    添加变量名、远程值和本地值
  </Step>
  <Step>
    点击`保存`
      
<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/556348/image-preview)
</Background>

  </Step>
</Steps>

:::tip[]
变量的**远程值**只能在 “环境管理” 中设置。使用脚本时，只能设置变量的本地值而不能设置远程值。
:::

### 方法 2：通过 “提取变量” 设置

Apifox 支持可视化提取接口响应中的值并保存为变量。步骤如下：

<Steps>
  <Step>
    在运行标签页（文档模式）或请求标签页（调试模式）中，导航到后置操作
  </Step>
  <Step>
    光标悬停在 “添加后置操作” 上并选择 “提取变量”

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/480040/image-preview)
</Background>

  </Step>
  <Step>
   输入变量名并选择变量类型。
      
选择提取来源，如响应 JSON、响应 XML 或响应文本等。
  </Step>
  <Step>
如果响应是 JSON/XML 格式，你可以使用 [JSONPath/XPath](https://docs.apifox.com/jsonpath.md) 语法解析响应 JSON/XML 的特定部分，并将其保存为变量值。

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/480042/image-preview)
</Background>

  </Step>
  <Step>
发送请求后，变量提取会被执行，你可以在控制台查看日志，然后在相关的 “环境管理” 中查看该变量。

      
<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/480043/image-preview)
</Background>


  </Step>
</Steps>

:::highlight purple 
了解更多关于[提取变量](https://docs.apifox.com/extract-variables.md)的信息。
:::

### 方法 3：在 “脚本” 中设置

你可以在前置/后置请求脚本中以编程方式设置变量。需要通过 `set` 方法设置变量。以下是示例代码：

```js
pm.environment.set('variable_key', 'variable_value');
```

以下是更多关于 `set` 的语法：


1. **环境变量**

```javascript
// 设置环境变量
pm.environment.set('variable_key', 'variable_value');

// unset 环境变量
pm.environment.unset('variable_key');
```

环境变量支持数组、对象、字符串等形式存储，你可以参考以下代码将对象或数组 *（非字符串）* 写入环境变量。

```javascript
var array = [1, 2, 3, 4];
pm.environment.set('array', JSON.stringify(array));

var obj = { a: [1, 2, 3, 4], b: { c: 'val' } };
pm.environment.set('obj', JSON.stringify(obj));
```

读取的时候，需要使用 `JSON.parse` 逆转换。

```javascript
try {
  var array = JSON.parse(pm.environment.get('array'));
  var obj = JSON.parse(pm.environment.get('obj'));
} catch (e) {
  // 处理异常
}
```

2. **全局变量**

- **项目中共享的全局变量**

```javascript
// 设置全局变量
pm.globals.set('variable_key', 'variable_value');

// unset 全局变量
pm.globals.unset('variable_key');
```

- **团队中共享的全局变量**

```javascript
// 设置全局变量
pm.globals.set('variable_key', 'variable_value', 'TEAM');

// unset 全局变量
pm.globals.unset('variable_key', 'TEAM');
```

3. **临时变量**

```javascript
// 设置临时变量
pm.variables.set('variable_key', 'variable_value');

// unset 临时变量
pm.variables.unset('variable_key');
```

4. **模块变量**


```js
// 设置模块变量
pm.moduleVariables.set('variable_key', 'variable_value');

// Postman 兼容方法，效果相同
pm.collectionVariables.set('variable_key', 'variable_value');

```

:::highlight purple 📌
了解更多关于[脚本语法](https://docs.apifox.com/postman-script-api.md)的信息。
:::

### 方法 4：将 “数据库数据” 设置为变量

Apifox 提供了一个特殊功能：连接数据库获取数据，将其设置为变量，并在接口中使用。步骤如下：

<Steps>
  <Step>
    在运行标签页（文档模式）或请求标签页（调试模式）中，导航到后置操作。
  </Step>
  <Step>
    悬停在 “添加后置操作” 上并选择 “数据库操作”。
      

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/480051/image-preview)

</Background>



  </Step>
  <Step>
   为数据库操作命名并设置[数据库连接](https://docs.apifox.com/database.md)。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/480064/image-preview)
</Background>

  </Step>
  <Step>
输入 SQL 命令。命令中支持使用变量，如 `{{variables}}`。

  </Step>
  <Step>
设置 **“提取结果到变量”**，支持使用 JSONPath，这样会将查询到的数据库数据存储到环境变量或者其他类型的变量中。也可以开启 “控制台打印结果” 开关，以将结果打印到控制台。

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/568771/image-preview)
</Background>

  </Step>
  <Step>
点击发送请求，你可以在控制台查看数据库操作的结果。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/480067/image-preview)
</Background>

  </Step>
</Steps>

:::highlight purple
了解更多关于[数据库操作](https://docs.apifox.com/database.md)的信息。
:::



## 使用变量

### 通过 `{{}}` 引用

在 Apifox 中，你可以通过双大括号`{{}}`引用项目中的变量。例如，要在接口的认证设置中引用名为 `my_token` 的变量，只需将变量名用双大括号包裹，如：`{{my_token}}`。

当你运行接口时，Apifox 会解析该变量并用其当前值进行替换。

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/480069/image-preview)
</Background>


例如，在引用了变量的请求 URL 中：

```json
http://127.0.0.1/pet/findByStatus?status={{CurrentStatus}}
```

运行请求时，Apifox 会使用 `CurrentStatus` 变量的存储值。如果 `CurrentStatus` 的值是 "available"，发送的请求 URL 会包含查询参数：
```json
http://127.0.0.1/pet/findByStatus?status=available
```

你可以在 “实际请求” 标签中查看组装后的请求。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/480075/image-preview)
</Background>


在请求体中引用变量时，可以像这样：

```json
{ 
    "status" : "{{CurrentStatus}}"
    "quantity" : {{TotalPet}}
}
```

:::tip[]
- 在 JSON 格式中使用字符串类型的变量时，需要加上双引号。对于其他类型的变量，则无需加双引号，如上例所示。
- 双大括号有时可能会触发 JSON 格式错误的警告，但这些警告可以忽略。
:::

变量可以在请求 URL、参数、请求头、认证设置、请求体等地方使用。

有时，你可能会看到 “未解析的变量” 提示，这表示该变量在环境或全局变量中未定义。但这并不一定是问题的根源。如果你是在后置操作中提取变量或使用脚本设置变量，可能在请求运行前还未获取到其值。如果是临时变量，它们在执行后会过期，这也可能导致变量值不可用。为了确认是否存在问题，你可以先发送请求进行验证。

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/480076/image-preview)

</Background>


### 读取变量的子元素值

如果变量的值是对象或数组形式，可以通过 `{{变量名.属性名}}` 或 `{{变量名[0].属性名}}` 读取变量中的字段值。例如：

1. **对象变量 `user` 如下：**

```js
{
  "id": 1,
  "name": "jack"
}
```

- 在接口参数中，可以用 `{{user.name}}` 引用 user 对象的 name 字段
- 在自定义脚本中，可以用 `pm.variables.get("user.name")` 引用 user 对象中的 name 字段

2. **数组变量 `user` 如下：**

```js
[
  {
    id: 1,
    name: "jack",
  },
];
```

- 在接口参数中，可以用 `{{user[0].name}}` 引用 user 数组第一个元素的 name 字段
- 在自定义脚本中，可以用 `pm.variables.get("user[0].name")` 引用 user 数组第一个元素的 name 字段

使用 `{{user.name}}` 这样的方式读取变量（对象或数组）中的字段值遵循 JSONPath 语法规范。你可以用变量名替换 JSONPath 中的 `$` 符号。



:::highlight purple 💡
查看[JSONPath](https://docs.apifox.com/jsonpath.md)的详细信息。
:::


### 在脚本中使用变量

在脚本中使用变量时，不能直接使用 `{{变量}}` 语法。需要先通过 `get` 方法将变量值赋给一个新的变量。以下是示例代码：

```js
var name = pm.environment.get("variable");
```

以下是更多关于 `get` 的语法：


1. **环境变量**

```javascript
// 获取环境变量
var variable_key = pm.environment.get('variable_key');

```

环境变量支持数组、对象、字符串等形式存储，你可以参考以下代码将对象或数组 *（非字符串）* 写入环境变量。

```javascript
var array = [1, 2, 3, 4];
pm.environment.set('array', JSON.stringify(array));

var obj = { a: [1, 2, 3, 4], b: { c: 'val' } };
pm.environment.set('obj', JSON.stringify(obj));
```

读取的时候，需要使用 `JSON.parse` 逆转换。

```javascript
try {
  var array = JSON.parse(pm.environment.get('array'));
  var obj = JSON.parse(pm.environment.get('obj'));
} catch (e) {
  // 处理异常
}
```

2. **全局变量**

- **项目中共享的全局变量**

```javascript
// 获取全局变量
var variable_key = pm.globals.get('variable_key');
```

- **团队中共享的全局变量**

```javascript
// 获取全局变量
var variable_key = pm.globals.get('variable_key', 'TEAM');
```

3. **临时变量**

```javascript
// 获取临时变量
var variable_key = pm.variables.get('variable_key');

```

4. **模块变量**


```js
// 获取模块变量
var variable_key = pm.moduleVariables.get('variable_key');

// Postman 兼容方法，效果相同
var variable_key = pm.collectionVariables.get('variable_key');
```




### 打印变量值

在发送请求时，你可以把变量值打印到 Apifox 控制台。

要在脚本中打印变量值，使用以下语法：

```js
console.log(pm.variables.get("variable_key"));
```

点击响应区域的控制台标签可以查看打印的结果。

### 使用测试数据变量

在 Apifox 中，如果需要发送多组数据作为请求参数，可以使用 “测试数据变量” 功能。在自动化测试场景中，你可以导入 CSV 或 JSON 格式的数据，并通过 `{{变量名}}` 引用这些数据变量，其中变量名对应 CSV 中的列名。

选择测试场景中的数据集后，运行时 `{{变量}}` 会被替换为实际数据。每行数据对应一次请求执行，测试报告中将显示每次运行的请求和响应。

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/480078/image-preview)

:::highlight purple 
更多信息请参考[数据驱动测试](https://docs.apifox.com/data-driven-testing.md)指南。
:::

### 使用“动态值”表达式

Apifox 支持在自定义脚本中生成动态值，使用`pm.variables.replaceInAsync(variableName:String):function`方法将以真实的值替换字符串里包含的“动态值表达式”。该函数返回 Promise，调用时需加 await。

一个生成随机姓名的示例如下：
```js
// 定义一个包含动态值表达式的字符串
let stringWithVariable = "Hello, {{$person.fullName}}";

// 使用 replaceInAsync 方法替换掉 {{$person.fullName}} 占位符
let realValueString = await pm.variables.replaceInAsync(stringWithVariable);
console.log(realValueString)
```
`{{$person.fullName}}` 在脚本运行时生成了一个真实值。
<Background>
![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/494952/image-preview)
</Background>

:::info[]
更多 pm.variables 的用法请参考 <a href="/5580997m0#pmvariables">pm.variables</a> 。
更多动态值的介绍请参考 [动态值](https://docs.apifox.com/dynamic-values.md)。
:::




## 常见问题

**我可以在 Mock 中引用变量吗？在哪些场景可以使用变量？**

变量只有在发送请求时才会被转换为实际值。因此，变量可以在某些场景中使用，但在其他场景中则无法使用。

可以使用变量的场景包括：

- **接口**：可以直接在接口的请求参数、请求体、路径和 Auth 等地方使用 `{{变量}}`。
- **前置和后置脚本**：在这些脚本中，使用 `pm.environment.get("变量名")` 或类似语句引用变量，但不能直接使用 `{{变量}}`。
- **测试场景**：由于测试场景中的请求会被发送，因此使用方式与接口和脚本相同，可以在请求中使用 `{{变量}}`。

不能使用变量的场景包括：

- **接口文档**：请求的默认值、响应的默认值以及 Mock 数据中都不能使用变量。
- **Mock**：高级 Mock 和 Mock 脚本不支持使用变量。


:::tip[]
不要将一个变量的值设置为另一个变量，这可能导致变量值无法正确解析。

关键点在于，变量只有在实际发送请求时才会被解析。因此，变量不能用于接口文档的静态部分或 Mock 场景，因为这些场景并不涉及请求的发送。
:::
