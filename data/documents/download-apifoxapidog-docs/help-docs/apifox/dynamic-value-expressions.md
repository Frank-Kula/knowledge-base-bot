# 概述


动态值表达式 *（或称为“动态变量”）* 允许你在调试接口时自动生成或构造一些特定的数据，如用户名、地址等。这些动态值可以根据预定义的规则在每次发送请求时生成新的值，从而简化调试过程，并确保每个请求都包含唯一的数据。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/487604/image-preview)
</Background>


Apifox 动态值基于 [Faker.js v9.0.0-rc.1](https://v9.fakerjs.dev/) 构建，针对 API 测试工作流程进行了增强和优化。Apifox 在保留 Faker.js 强大功能的同时，为生成逼真的测试数据提供了更直观、更高效的体验。如果你已经熟悉 Faker.js，那么过渡到 Apifox 动态值将会轻而易举。

## 全面的动态值库

为了便于参考，Apifox 为每个动态值类别提供了带有示例的文档，其结构与 Faker.js 相同：


- [航空公司（Airline）](https://docs.apifox.com/5589658m0.md)
- [动物（Animal）](https://docs.apifox.com/5589662m0.md)
- [颜色（Color）](https://docs.apifox.com/5589666m0.md)
- [商业（Commerce）](https://docs.apifox.com/5589669m0.md)
- [公司（Company）](https://docs.apifox.com/5589672m0.md)
- [数据库（Company）](https://docs.apifox.com/5589675m0.md)
- [数据类型（Datatype）](https://docs.apifox.com/5589677m0.md)
- [日期（Date）](https://docs.apifox.com/5589680m0.md)
- [金融（Finance）](https://docs.apifox.com/5589683m0.md)
- [食物（Food）](https://docs.apifox.com/5589685m0.md)
- [Git](https://docs.apifox.com/5589688m0.md)
- [黑客（Hacker）](https://docs.apifox.com/5589689m0.md)
- [辅助函数（Helpers）](https://docs.apifox.com/5589690m0.md)
- [图片（Image）](https://docs.apifox.com/5589695m0.md)
- [网络（Internet）](https://docs.apifox.com/5589698m0.md)
- [地点和位置（Location）](https://docs.apifox.com/5589700m0.md)
- [随机文本单词（Lorem）](https://docs.apifox.com/5589703m0.md)
- [音乐（Music）](https://docs.apifox.com/5589733m0.md)
- [数字（Number）](https://docs.apifox.com/5589760m0.md)
- [人物（Person）](https://docs.apifox.com/5589761m0.md)
- [电话（Phone）](https://docs.apifox.com/5589763m0.md)
- [科学（Science）](https://docs.apifox.com/5589766m0.md)
- [字符串（String）](https://docs.apifox.com/5589794m0.md)
- [系统（System）](https://docs.apifox.com/5589800m0.md)
- [车辆（Vehicle）](https://docs.apifox.com/5589801m0.md)
- [单词（Word）](https://docs.apifox.com/5589803m0.md)

## Apifox 动态值的主要增强功能

以下是使 Apifox 动态值更加强大和用户友好的主要变化：


### 1. 简化的表达式语法，方便访问

Apifox 使用简洁直观的语法来调用动态值：

- **Faker.js:** `faker.finance.accountName()`
- **Apifox:** `{{$finance.accountName}}`

只需在 Apifox 中输入 `{{%` 即可触发自动补全，轻松浏览可用的动态值。



### 2. 优化的对象和数组输出 - 提高灵活性

Apifox 通过为最初在 Faker.js 中返回对象或数组的方法返回 JSON 字符串来简化数据处理，从而可以直接访问特定值：

**示例 1：提取机场数据**

- **Faker.js:** `faker.airline.airport()` 返回一个对象： 

```js
 faker.airline.airport() // { name: 'Dallas Fort Worth International Airport', iataCode: 'DFW' } 
```

- **Apifox:** 直接访问特定字段：


```js
    `{{$airline.airportName}}`  //'Dallas Fort Worth International Airport'
    `{{$airline.airportIataCode}}`  // 'DFW'
```

**示例 2：处理多个日期**

- **Faker.js:**  `faker.date.betweens()` 返回一个数组： 


```js
faker.date.betweens({ from: '2020-01-01T00:00:00.000Z', to: '2030-01-01T00:00:00.000Z', count: { min: 2, max: 5 }})
// [
//   2021-12-19T06:35:40.191Z,
//   2022-09-10T08:03:51.351Z,
//   2023-04-19T11:41:17.501Z
// ]
```

- **Apifox:** 返回 JSON 字符串化数组，以便于数据处理：


```js
{{$date.betweens(from='2020-01-01T00:00:00',to='2030-01-01',min=2,max=5)}}  // ["2020-10-14 00:48:27","2021-10-25 22:46:34","2027-03-06 02:33:22","2028-04-22 20:13:40","2029-12-31 14:45:59"]
```




### 3. 增强型区域设置控制，用于生成本地化数据

Apifox 提供了对区域设置的增强控制，以便生成特定于区域的数据：

- **函数级设置：**  为每个动态值函数单独定义区域设置。
- **项目级默认值：**  为整个 Apifox 项目设置默认区域设置。
- **日期格式覆盖：**  在与日期相关的函数中使用 `format` 方法来应用特定于区域的格式覆盖。


### 4.  常用用例的预设参数 - 简化工作流程

Apifox 通过为常用方法提供预设参数（可根据需要自定义）来提高效率：

- `{{$helpers.fromRegExp('[A-Z0-9]{4}-[A-Z0-9]{4}')}}`  // 生成与正则表达式匹配的字符串
- `{{$helpers.arrayElement(['abc','123'])}}`  // 从数组中随机选择一个元素
- `{{$helpers.arrayElements(['abc','123'])}}`  // 从数组中选择多个随机元素
- `{{$helpers.replaceSymbols('##??**')}}`  // 用随机字符替换特殊符号
- `{{$helpers.slugify('abc 123')}}`  //  生成 URL 友好的 slug

<br />

### 5. 扩展的动态值库，提供更广泛的覆盖范围

Apifox 通过新的类别和方法丰富了你的数据生成功能：

- **新类别：`food`** 用于生成各种与食物相关的数据。示例：`{{$food.vegetable}}` 
- **新方法：**
    - `{{$date.timeZone}}` 用于生成时区数据。
    - `{{$music.album}}` 用于创建逼真的音乐专辑名称。
    - `{{$music.artist}}` 用于生成艺术家姓名。
- **增强型方法参数：**
   -   `{{$phone.number(style='human')}}` 用于生成人类可读的电话号码，例如：(555) 123-4567。
   -   `{{$number.int(multipleOf=3)}}` 用于生成可被指定数字整除的整数。


### 6.  无限拼接 - 释放你的创造力

Apifox 允许你无限制地无缝组合模拟数据和动态值，从而提供最终的灵活性，使你能够创建丰富而逼真的测试场景。


### 7.  扩展的日期功能，用于强大的日期操作

Apifox 扩展了日期相关的函数，增加了用于格式化、偏移量计算等的新参数，以满足各种复杂测试需求。







