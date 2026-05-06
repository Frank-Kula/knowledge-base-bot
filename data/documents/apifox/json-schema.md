# JSON Schema 介绍



## 如何描述 JSON ？

JSON (JavaScript Object Notation) 缩写，JSON 是一种数据格式，具有简洁、可读性高、支持广泛的特点。JSON 有以下基本数据类型

```js
// # 1. object
{ "key1": "value1", "key2": "value2" }

// # 2. array
[ "first", "second", "third" ]

// # 3. number
42

// # 4. string

"This is a string"

// # 5. boolean

true 

false

// # 6. null

null
```

在其它语言中也有类似的内建数据类型，但是由于 JavaScript 的广泛应用，而 JSON 作 为 JavaScript 原生的数据类型，具备更加广泛的支持。

有了上面列举的基本数据类型，JSON 能非常灵活的表示任意复杂的数据结构。举个例子：

```json
  {
      "name": "George Washington",
      "birthday": "February 22, 1732",
      "address": "Mount Vernon, Virginia, United States"
  }
```

如何描述上面 JSON 对象呢？

首先，它是一个 `object`；

其次，它拥有 `name`、`birthday`、`address` 这三个字段

并且，`name` 、`address` 的字段值是一个字符串 `String`，`birthday` 的值是一个日期。

最后，将上面的信息如何用 JSON 来表示？如下：

```json
  {
      "type": "object",
      "properties": {
           "name": { "type": "string" },
           "birthday": { "type": "string", "format": "date" },
           "address": { "type": "string" }
      }
  }
```

这个表示就是一个 [JSON Schema](https://json-schema.apifox.cn/) ，JSON Schema 用于描述 JSON 数据。

相同的数据，可能有不同的表示，比如下面的两种表示，包含的信息量基本是一致的：

```js
  // # 1. 表示一
  {
  "name": "George Washington",
  "birthday": "February 22, 1732",
  "address": "Mount Vernon, Virginia, United States"
  }

  // # 2. 表示二
  {
      "first_name": "George",
      "last_name": "Washington",
      "birthday": "1732-02-22",
      "address": {
          "street_address": "3200 Mount Vernon Memorial Highway",
          "city": "Mount Vernon",
          "state": "Virginia",
          "country": "United States"
      }
  }
```

在特定的应用场景中，应用程序对数据的结构要求是确定的，出于对数据描述的规范化需 求，需要用 [JSON Schema](https://json-schema.apifox.cn/) 来规范化。使用 JSON Schema 可以描述 JSON 数据所包含的字 段、以及字段值的类型，以及依赖关系等。

相同信息量的数据，采用不同的形式来表达，用 JSON Schema 来描述也是不一样的，表示二的 JSON Schema 如下：

```json
  {
      "type": "object",
      "properties": {
           "first_name": { "type": "string" },
           "last_name": { "type": "string" },
           "birthday": { "type": "string", "format": "date-time" },
           "address": {
           "type": "object",
           "properties": {
               "street_address": { "type": "string" },
               "city": { "type": "string" },
               "state": { "type": "string" },
               "country": { "type" : "string" }
           }
          }
      }
  }
```

从上面的描述，可以很自然的想到 [JSON Schema](https://json-schema.apifox.cn/) 可以用来做数据校验，比如前后端先把数 据接口约定好，写好 JSON Schema，等后端把接口输出完毕，直接用 JSON Schema 来对接 口做验收。

关于 JSON Schema 的应用，对 [JSON Schema](https://json-schema.apifox.cn/) 有过了解的人可以直接跳到第三、四部分。

接下来对 JSON Schema 做一些举例说明。

## JSON Schema 示例

### 1. 空 schema

```json
{}
```

以下都是合法的 JSON

```js
42

"I'm a string"

[{"an": "aaa","bbb":{"nest":"data"}}]
```

### 2. type 指定 JSON 数据类型

```js
{ "type": "string" }
"I'm a string"

42 

{ "type": "number" }

42

"42"
type` 的可能取值: `string` 、`number` 、`object`、 `array`、 `boolean`、 `null
```

### 3. type 可以包含多个类型

```js
{ "type": ["number", "string"] }
"I'm a string" // 合法

42  // 合法

["Life", "the universe", "and everything"] // 不合法
```

### 4. string 限定长度

```js
{
    "type": "string",
    "minLength": 2,
    "maxLength": 3
}
"AA" // 合法
"AAA" // 合法
"A"  // 不合法
"AAAA" // 不合法
```

### 5. string 模式匹配

```js
{
  "type": "string",
  "pattern": "^(\\([0-9]{3}\\))?[0-9]{3}-[0-9]{4}$"
}
"555-1212" // ok

"(888)555-1212" // ok

"(888)555-1212 ext. 532" // not ok

"(800)FLOWERS" // not ok
```

### 6. string 值的枚举

```js
{
    "type": "string",
    "enum": ["red", "amber", "green"]
}
"red" // ok

"blue" // not ok: blue 没有在 enum 枚举项中
```

### 7. integer

integer 一定是整数类型的 number

```js
{ "type": "integer" }
42 // ok
1024 // ok
```

### 8. multipleOf 数字倍数

```js
{ "type": "number", "multipleOf": 2.0 }
42 // ok
21 // not ok
```

### 9. number 限定范围

```js
{
    "type": "number",
    "minimum": 0,
    "maximum": 100,
    "exclusiveMaximum": true
}
```

`exclusiveMaximum` 为 `true` 表示不包含边界值 `maximum`，类似的还有 `exclusiveMinimum` 字段.

### 10. object 不允许有额外的字段

```js
{
    "type": "object",
    "properties": {
        "number": { "type": "number" },
        "street_name": { "type": "string" },
        "street_type": { 
             "type": "string",
             "enum": ["Street", "Avenue", "Boulevard"]
        }
    },
    "additionalProperties": false
}
{ "number": 1600, "street_name": "Pennsylvania", "street_type": "Avenue" } // ok
{ "number": 1600, "street_name": "Pennsylvania", "street_type": "Avenue","direction": "NW" } // not ok
```

因为包含了额外的字段 `direction`，而 schema 规定了不允许额外的字段 `"additionalProperties": false`

### 11. object 允许有额外的字段，并限定类型

```js
{
    "type": "object",
    "properties": {
    "number": { "type": "number" },
    "street_name": { "type": "string" },
    "street_type": { 
        "type": "string",
        "enum": ["Street", "Avenue", "Boulevard"]
    }
    },
    "additionalProperties": { "type": "string" }
}
{ "number": 1600, "street_name": "Pennsylvania", "street_type": "Avenue","direction": "NW" } // ok

{ "number": 1600, "street_name": "Pennsylvania", "street_type": "Avenue", "office_number": 201 } // not ok
  额外字段 `"office_number": 201` 是 number 类型，不符合 schema
```

### 12. object 必填字段

```js
{
     "type": "object",
     "properties": {
          "name": { "type": "string" },
          "email": { "type": "string" },
          "address": { "type": "string" },
          "telephone": { "type": "string" }
     },
     "required": ["name", "email"]
}
// ok
{
  "name": "William Shakespeare",
  "email": "bill@stratford-upon-avon.co.uk"
}
```

多出字段也是 ok 的

```js
// ok
{
    "name": "William Shakespeare",
    "email": "bill@stratford-upon-avon.co.uk",
    "address": "Henley Street, Stratford-upon-Avon, Warwickshire, England",
    "authorship": "in question"
}
```

少了字段，就是不行

```js
// not ok
{
    "name": "William Shakespeare",
    "address": "Henley Street, Stratford-upon-Avon, Warwickshire, England",
}
```

### 13. object 指定属性个数

```js
{
    "type": "object",
    "minProperties": 2,
    "maxProperties": 3
}
{ "a": 0, "b": 1 } // ok
{ "a": 0, "b": 1, "c": 2, "d": 3 } // not ok
```

### 14. Dependencies 依赖

```js
  略复杂，不提供示例
```

### 15. Object 属性的模式匹配

```js
{
    "type": "object",
    "patternProperties": {
         "^S_": { "type": "string" },
         "^I_": { "type": "integer" }
    },
    "additionalProperties": false
}
{ "S_25": "This is a string" } // ok

{ "I_0": 42 } // ok
// not ok
{ "I_42": "This is a string" }

{ "keyword": "value" }
```

### 16. array 数组

```js
// ok
{ "type": "array" }
[1, 2, 3, 4, 5]
[3, "different", { "types" : "of values" }]
// not ok:
{"Not": "an array"}
```

### 17. array 指定数组成员类型

```js
{
    "type": "array",
    "items": {
        "type": "number"
    }
}
[1, 2, 3, 4, 5] // ok
[1, 2, "3", 4, 5] // not ok
```

### 18. array 指定数组成员类型，逐个指定

```js
{
"type": "array",
     "items": [{
          "type": "number"
          },{
          "type": "string"
          },{
          "type": "string",
          "enum": ["Street", "Avenue", "Boulevard"]
          },{
          "type": "string",
          "enum": ["NW", "NE", "SW", "SE"]
     }]
}
// ok
[1600, "Pennsylvania", "Avenue", "NW"]

[10, "Downing", "Street"] // 缺失一个也是可以的

[1600, "Pennsylvania", "Avenue", "NW", "Washington"] // 多出一个也是可以的
// not ok
[24, "Sussex", "Drive"]
["Palais de l'Élysée"]
```

### 19. array 指定数组成员类型，逐个指定，严格限定

```js
{
    "type": "array",
    "items": [{
        "type": "number"
        },
        {
        "type": "string"
        },
        {
        "type": "string",
        "enum": ["Street", "Avenue", "Boulevard"]
        },
        {
        "type": "string",
        "enum": ["NW", "NE", "SW", "SE"]
        }
    ],
    "additionalItems": false
}
[1600, "Pennsylvania", "Avenue", "NW"] // ok

[1600, "Pennsylvania", "Avenue"] // ok

[1600, "Pennsylvania", "Avenue", "NW", "Washington"] // not ok 多出了字段就是不行
```

### 20. array 数组长度限制

```js
{
   "type": "array",
   "minItems": 2,
   "maxItems": 3
}
[1, 2] // ok

[1, 2, 3, 4] // not ok
```

### 21. array element uniqueness 数组元素的唯一性

```js
{
    "type": "array",
    "uniqueItems": true
}
[1, 2, 3, 4, 5] // ok
[1, 2, 3, 3, 4] // not ok:出现了重复的元素 3
```

### 22. boolean

```js
{ "type": "boolean" }
true // ok
0 // not ok
```

### 23. null

```js
{ "type": "null" }
null // ok

"" // not ok
```

### 24. schema 的合并

string 类型，最大长度为 5 ；或 number 类型，最小值为 0

```js
{
    "anyOf": [
       { "type": "string", "maxLength": 5 },
       { "type": "number", "minimum": 0 }
    ]
}

`anyOf` 包含了两条规则，符合任意一条即可
"short"  // ok
42 // ok
"too long" // not ok 长度超过 5 
-5 // not ok 小于了 0
```

### 25. allOf、oneOf

```js
  `anyOf` 是满足任意一个 Schema 即可，而 `allOf` 是要满足所有 Schema
  `oneOf` 是满足且只满足一个
```

### 26. oneOf

```js
{
    "oneOf": [
        { "type": "number", "multipleOf": 5 },
        { "type": "number", "multipleOf": 3 }
    ]
}
10 // ok
15 // not ok 因为它既是 3 又是 5 的倍数
```

上面的 schema 也可以写为：

```js
{
    "type": "number",
    "oneOf": [
        { "multipleOf": 5 },
        { "multipleOf": 3 }
    ]
}
```

### 27. not

```js
{ "not": { "type": "string" } }
```

只要是非 string 类型即可

```js
42 // ok
{"key" : "value"} // ok
"This is a string" // not ok
```


