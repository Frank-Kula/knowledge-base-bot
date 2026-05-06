# 使用 oneOf / anyOf / allOf 构建组合模式

`oneOf`、`anyOf`、`allOf` 是 JSON Schema 规范中用于定义复合数据结构的关键字，它们本质上是逻辑运算符在数据校验中的应用。Apifox 完全支持这些 JSON Schema 特性，帮助你构建更准确的 API 文档和数据验证规则。

## 基本概念


<AccordionGroup>
  <Accordion title="allOf" defaultOpen>
`allOf` 表示数据必须**同时满足**所有子模式的条件，相当于逻辑运算中的 **AND（与）** 操作。就像生活中的 “既要...又要...”，所有条件都必须同时成立，验证才能通过。
  </Accordion>
  <Accordion title="anyOf">
`anyOf` 表示数据**至少满足**其中一个子模式的条件，也可以同时满足多个，这相当于逻辑运算中的 **OR（或）** 操作。就像生活中的 “要么...要么...或者都要”，只要有任意一个或多个条件满足，验证就会通过。
  </Accordion>
  <Accordion title="oneOf">
`oneOf` 表示数据**恰好满足**其中一个子模式的条件，不能同时满足多个，也不能一个都不满足，这相当于逻辑运算中的 **XOR（异或）** 操作。就像生活中的 “二选一”，只能且必须选择其中一个条件。

  </Accordion>
</AccordionGroup>


## 逻辑对比表

| 关键字 | 逻辑运算 | 满足条件 | 典型场景 |
|--------|----------|----------|----------|
| `allOf` | AND（与） | 必须同时满足所有条件 | 继承、扩展 |
| `anyOf` | OR（或） | 至少满足一个条件 | 可选组合 |  
| `oneOf` | XOR（异或） | 恰好满足一个条件 | 互斥选择 |

## 在 Apifox 中的使用方法

### 1. 通过可视化编辑器使用


<Steps>
  <Step title="步骤一：创建数据模型">
    在项目中点击「数据模型」，然后「新建数据模型」
      
<Background>

![CleanShot 2025-08-05 at 18.19.33@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/552958/image-preview)
</Background>


  </Step>
  <Step title="步骤二：添加组合模式">
    在数据模型编辑面板中，选择类型时点击「组合模式」，选择 `oneOf`、`anyOf` 或 `allOf`，为每个子模式定义具体的数据结构
      
<Background>

![01-schemas.gif](https://api.apifox.com/api/v1/projects/5097254/resources/552963/image-preview)
</Background>

  </Step>
</Steps>


### 2. 通过 JSON Schema 代码编辑

你也可以直接在数据模型的编辑面板中，编辑 JSON Schema 代码来定义这些逻辑组合模式。

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/552964/image-preview)
</Background>



## 在接口文档中应用

### 请求参数定义

在定义接口的请求参数时，你可以使用这些组合模式来描述复杂的参数结构：

<Steps>
  <Step>
    进入接口编辑页面
  </Step>
  <Step>
    在「请求参数」部分选择 Body，选择 json 类型
  </Step>
  <Step>
    在数据结构中，点击「引用模型」，或者根据业务逻辑选择合适的「组合模式」，或者自定义 JSON Schema
     
<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/552968/image-preview)
</Background>

      
  </Step>
</Steps>


### 响应数据定义

同样，你可以在响应数据中使用这些组合模式：


<Steps>
  <Step>
    在「返回响应」部分添加响应示例
  </Step>
  <Step>
    使用组合模式描述不同的响应格式
      
<Background>

![CleanShot 2025-08-05 at 18.49.17@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/552970/image-preview)
</Background>

  </Step>
</Steps>



## 实际使用示例

### allOf 示例（与运算）

使用 `allOf` 可以将多个数据模式组合在一起，要求数据同时满足所有条件。这就像是说 “<span style="color: #999">用户信息必须包含基础信息</span> **AND** <span style="color: #999">联系方式信息</span>”：

```json
{
  "allOf": [
    {
      "description": "基础用户信息",
      "type": "object",
      "properties": {
        "id": { "type": "integer" },
        "name": { "type": "string" }
      },
      "required": ["id", "name"]
    },
    {
      "description": "联系方式信息", 
      "type": "object",
      "properties": {
        "email": { "type": "string", "format": "email" },
        "phone": { "type": "string" }
      },
      "required": ["email"]
    }
  ]
}
```

**结果：** 最终数据必须包含 id、name、email 字段，phone 可选。所有子模式的约束条件都会被合并执行，如下图所示：

<Background>

![02-schemas.gif](https://api.apifox.com/api/v1/projects/5097254/resources/553174/image-preview)
</Background>


### anyOf 示例（或运算）

使用 `anyOf` 提供多种可选的验证路径，用户可以选择任意一种或多种方式。这就像是说 “<span style="color: #999">用户可以通过用户名密码</span> **OR** <span style="color: #999">邮箱密码</span> **OR** <span style="color: #999">手机号验证码来登录</span>”：

```json
{
  "type": "object",
  "properties": {
    "login": {
      "anyOf": [
        {
          "description": "用户名密码登录",
          "properties": {
            "username": { "type": "string" },
            "password": { "type": "string" }
          },
          "required": ["username", "password"]
        },
        {
          "description": "邮箱密码登录",
          "properties": {
            "email": { "type": "string", "format": "email" },
            "password": { "type": "string" }
          },
          "required": ["email", "password"]
        },
        {
          "description": "手机号验证码登录",
          "properties": {
            "phone": { "type": "string" },
            "verifyCode": { "type": "string" }
          },
          "required": ["phone", "verifyCode"]
        }
      ]
    }
  }
}
```

**结果：** 用户可以提供任意一种或多种登录方式的信息，只要至少满足一种即可通过验证，如下图所示：


<Background>
![03-schemas.gif](https://api.apifox.com/api/v1/projects/5097254/resources/553176/image-preview)

</Background>


### oneOf 示例（异或运算）

使用 `oneOf` 确保用户只能选择一种支付方式，不允许同时提供多种。这就像是说 “<span style="color: #999">支付方式必须是信用卡</span> **XOR** <span style="color: #999">PayPal</span> **XOR** <span style="color: #999">银行转账中的一种，且只能是一种</span>”：

```json
{
  "type": "object", 
  "properties": {
    "payment": {
      "oneOf": [
        {
          "description": "信用卡支付",
          "type": "object",
          "properties": {
            "type": { "const": "credit_card" },
            "cardNumber": { "type": "string" },
            "expiryDate": { "type": "string" }
          },
          "required": ["type", "cardNumber", "expiryDate"],
          "additionalProperties": false
        },
        {
          "description": "PayPal支付", 
          "type": "object",
          "properties": {
            "type": { "const": "paypal" },
            "email": { "type": "string", "format": "email" }
          },
          "required": ["type", "email"],
          "additionalProperties": false
        },
        {
          "description": "银行转账",
          "type": "object", 
          "properties": {
            "type": { "const": "bank_transfer" },
            "accountNumber": { "type": "string" },
            "routingNumber": { "type": "string" }
          },
          "required": ["type", "accountNumber", "routingNumber"],
          "additionalProperties": false
        }
      ]
    }
  }
}
```

**结果：** 用户必须且只能选择一种支付方式，不能同时提供多种，也不能一种都不提供，如下图所示：


<Background>

![04-schemas.gif](https://api.apifox.com/api/v1/projects/5097254/resources/553202/image-preview)
</Background>



在选择组合模式时，先明确你的业务逻辑：

- 需要组合**继承**多个模式 → 使用 `allOf`（与运算）
- 需要灵活的**可选**组合 → 使用 `anyOf`（或运算）  
- 需要严格的**互斥**选择 → 使用 `oneOf`（异或运算）

