# 调试 Dubbo 接口


## 定义目标服务器地址

开始调试接口前需定义目标服务器地址，你可以通过直连服务器或通过注册中心两种方式进行调试。

### 直连

点击页面右上角的环境配置按钮。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/485812/image-preview)
</Background>


填写服务器地址，然后点击“保存”按钮。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/485814/image-preview)
</Background>


在右上角指定刚刚配置的服务器地址，项目内的其它 Dubbo 接口也将会默认采用该地址。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/485815/image-preview)
</Background>


如果需要单独为每个 Dubbo 接口设置不同的服务器地址，可以点击接口地址栏，选择环境并手动切换服务器地址。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/485816/image-preview)
</Background>


确认服务地址无误后，点击右上角的“调用”按钮。

### 注册中心

:::info[]
Apifox 目前支持的注册中心为： ZooKeeper、Nacos 和阿里云 EDAS。
:::

点击页面右上角的环境配置按钮。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/485818/image-preview)
</Background>


填写注册中心名称，选择类型并填写地址。若注册中心配置了鉴权机制，请点击右侧齿轮按钮并进行高级配置。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/485819/image-preview)
</Background>



在右上角指定刚刚配置的注册中心，项目内的其它 Dubbo 接口也将会默认采用该注册中心地址。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/485820/image-preview)
</Background>


如果需要单独为每个 Dubbo 接口设置不同的注册中心，可以点击接口地址栏，选择环境并手动切换注册中心。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/485821/image-preview)
</Background>


确认服务地址无误后，点击右上角的“调用”按钮。

## 配置参数

### 版本号和分组

若 Dubbo 接口配置了版本号和分组，则需要填写，否则请留空。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/485822/image-preview)
</Background>



### 类名

在接口中需要配置参数的 Java 类名。

- 如果是简单类型，比如 `string`、`java.lang.String`，那么可以不填写类名。Apifox 会自动推断类名。
- 如果是 List 类型，请选择 `java.util.List`。其它集合类型同理，即选择完整名称。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/485823/image-preview)
</Background>


- 如果是自定义 DTO 类型，请填写完整的 DTO 名称，即包含完整 Package 名称。比如要引用 `com.dubbo.example` Package 内名为 `User` 的 DTO，那么需要完整填写 `com.dubbo.example.User`。

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/485824/image-preview)
</Background>


### 消息

消息体格式支持 JSON 格式。在消息体中还可以使用变量，变量的格式为 `{{变量名}}`，并且还支持添加“动态值”。

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/485825/image-preview)
</Background>


你也可以使用系统内置的「自动生成」功能生成请求消息体。使用该功能需提前在接口定义中添加请求参数，系统将根据请求定义自动生成请求体，详细说明请参考[《接口文档 —— 请求定义》](https://docs.apifox.com/dubbo-api-documentation.md)。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/485826/image-preview)
</Background>




### 复杂参数

一般情况下，Apifox 会自动推断字段的类型。但是，可能无法正确推断复杂参数的类型，导致服务端收到消息后序列化失败。这种情况下，需要手动声明字段的 Java 类型。语法为：

```json
{
    "$class": "字段的 Java 类名",
    "$": "字段的值"
}
```

**请求参数是 DTO，DTO 内部存在复杂类型**

假设某一个 DTO 类型内部通过 List 或其他数据结构引用了其它 DTO 类型，调用接口返回了 `java.util.HashMap cannot be cast to xxx.xxx.Dto` 形式的报错，这表示 Apifox 将 DTO 的类型自动推断为 `java.util.HashMap`。而服务器定义的是一个具体的自定义类名，两者不匹配，此时需要在调用时指定字段的类名。 假设 DTO 为：

```java
package com.dubbo.example;

public class Address {
    public String province;
    public String city;
}

public class User {
    public String name;
    public Integer age;
    public List<Address> addresses;
}
```

Dubbo 接口为：

```java
package com.dubbo.example;

public interface DemoService {
    String sayHello(User user);
}
```

那么使用 Apifox 调用 sayHello 方法时，需要手动指定 `addresses` 字段内元素的类名为 `com.dubbo.example.Address`，以避免其类型被自动推断为 `java.util.HashMap`：

```json
{
    "name": "Tom",
    "age": 3,
    "addresses": [
        {
            "$class": "com.dubbo.example.Address",
            "$": {
                "province": "Guangdong",
                "city": "Guangzhou"
            }
        },
        {
            "$class": "com.dubbo.example.Address",
            "$": {
                "province": "Guangdong",
                "city": "Shenzhen"
            }
        }
    ]
}
```

即：


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/485828/image-preview)
</Background>


**请求参数是数组，数组元素是 DTO**

假设 DTO 为：

```java
package com.dubbo.example;

public class Address {
    public String province;
    public String city;
}
```

Dubbo 接口为：

```java
package com.dubbo.example;

public interface DemoService {
    String sayHello(ArrayList<Address> addresses);
}
```

那么使用 Apifox 调用 sayHello 方法时，需要先选择 `java.util.ArrayList` 这个  Java 类名，然后在消息体内手动指定数组元素的类名为 `com.dubbo.example.Address`：

```json
[
    {
        "$class"： "com.dubbo.example.Address",
        "$": {
            "province": "Guangdong",
            "city": "Guangzhou"
        }
    },
    {
        "$class"： "com.dubbo.example.Address",
        "$": {
            "province": "Guangdong",
            "city": "Shenzhen"
        }
    }
]
```

即：


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/485829/image-preview)
</Background>


### 多参数

若接口存在多个入参，那么可以点击左侧的“添加参数”按钮，添加多个参数。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/485830/image-preview)
</Background>


### 映射关系

Java 和 JSON 的数据类型存在着映射关系，如下表所示：

| Java                                                                                       | JSON    | JSON 示例                |
| ------------------------------------------------------------------------------------------ | ------- | ------------------------ |
| boolean, java.lang.Boolean                                                                 | boolean | `true, false`            |
| char, java.lang.Character                                                                  | string  | `"\u0066", "f"`          |
| java.lang.String                                                                           | string  | `"Hello World!"`         |
| byte, java.lang.Byte, short, java.lang.Short, int, java.lang.Integer, long, java.lang.Long | integer | `1, -10, 0`              |
| float, java.lang.Float, double, java.lang.Double                                           | float   | `1.1, -10.0, 0`          |
| java.math.BigDecimal                                                                       | object  | `{"value": 1.1}`         |
| `java.util.List<V\>, java.util.Set<V\>, dataType[]`                                          | array   | `[v, …]`                 |
| `java.util.Map<K,V>, DTO, POJO`                                                              | object  | `{"k": v, …}`            |
| enum                                                                                       | object  | `{"name": "ENUM_VALUE"}` |
| java.util.Date, java.sql.Date, java.sql.Timestamp, java.sql.Time                           | string  | `"2020-01-01 00:00:00"`  |
| java.time.LocalDateTime, java.time.LocalTime                                               | string  | `"2020-01-01T00:00:00"`  |
| java.time.LocalDate                                                                        | string  | `"2020-01-01"`           |



## 调用接口

点击右上角的「调用」按钮，即可得到接口的返回结果。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/485831/image-preview)
</Background>


## 校验响应

如果 Dubbo 接口具备有效的响应定义，那么在调用接口后，Apifox 会自动对响应进行校验，与 HTTP 接口的调试体验保持一致。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/485833/image-preview)
</Background>


## 前后置操作

> [Apifox 商业专业版可使用 Dubbo 的前后置操作功能](https://apifox.com/pricing)


Dubbo 接口支持在调试接口时执行前后置，包括断言、提取变量、数据库操作、自定义脚本、公共脚本、等待时间，与 HTTP 接口的调试体验保持一致，具体可以参考 HTTP 的[前后置操作](https://docs.apifox.com/pre-post-processors.md)帮助文档。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/485834/image-preview)
</Background>


由于 Dubbo 接口与 HTTP 接口的一些基本概念存在不同，因此使用自定义脚本时，一些方法存在差异，而大部分方法与 HTTP 相同。需要注意的是以下方法：

### pm.request
- `pm.request.attachments`：对 RpcContext 的 Attachment 进行操作，语法与 pm.request.headers 相同
- `pm.request.params`：对请求参数进行操作，拥有 2 个方法
  - `get(index)`：获取请求参数
  - `set(index, object)`：设置请求参数

### pm.response
- `pm.response.json()`：将响应转换为 JavaScript 对象
- `pm.response.text()`：将响应转换为纯文本


## 常见问题

<Accordion title="传递 Long 类型的数字时，为什么服务端所收到的数字后面几位是错误的？" defaultOpen>
请使用 JSON 字符串传递 Long 类型的数字，即把数字使用双引号包裹起来，但是类名依旧保持 `java.lang.Long`。数字后面出现错误的原因是较大的数字超出了 JSON 的整数范围。
    
如果 DTO 中的一个字段是 Long 格式，请将该字段的 Java 类型声明为 `java.lang.Long`，如下：
```json
{
    "name": "Apifox",
    "timestamp": {
        "$class": "java.lang.Long",
        "$": "1735660800000"
    }
}
```
</Accordion>


<Accordion title="当 JSON 对象内部的字段是日期、对象或其他非简单类型时，为什么服务端会出现序列化错误？" defaultOpen={false}>
当日期类型使用 JSON 字符串表示时，Apifox 无法准确推断它对应着 Java 的哪一种日期类型。此时需要手动声明字段的 Java 类型，比如下面的例子，将 `update_time` 字段的 Java 类型声明为 `java.util.Date`：

```json
{
    "name": "Apifox",
    "update_time": {
        "$class": "java.util.Date",
        "$": "2020-01-01 00:00:00"
    }
}
```
</Accordion>


<Accordion title="请求参数中包含数组时，为什么会出现 `java.lang.String cannot be cast to XXX` 报错？" defaultOpen={false}>

**可能原因 1：数组的最后一个元素末尾有多余逗号**

报错截图：


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/485835/image-preview)
</Background>


删除多余逗号即可解决此问题。

**可能原因 2：没有正确遵循 DTO 数组格式**

具体正确代码示例请参考[请求参数是数组，数组元素是 DTO](#复杂参数)。
</Accordion>



