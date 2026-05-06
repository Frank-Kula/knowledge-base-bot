# 全局参数


全局参数是允许你定义一些在整个项目中通用的参数，这些参数可以在所有 API 请求中自动携带，从而提高接口测试的效率和一致性。

## 使用步骤

1. 点击页面右上侧的 “环境管理”，进入全局参数配置界面
   
    <Background>

    ![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/488389/image-preview)
    </Background>

2. 选择需要添加参数的类型 （Header/Cookie/Query/Body）
3. 填写参数信息（参数名、类型、默认值等）
4. 启用/禁用参数开关
5. 保存配置



## 参数配置说明

### 参数类型

全局参数支持以下几个位置：

1. Header（请求头）
2. Cookie（Cookie 信息）
3. Query（URL 查询参数）
4. Body（请求体参数）



### 基本属性

- **参数名**：参数的标识符，在请求中的实际名称
- **类型**：参数的数据类型（如 string、number 等）
- **默认值**：参数的预设值，推荐设置为`{{变量}}`形式
- **默认启用**：通过开关控制参数是否生效
- **说明**：参数用途的描述信息

    
<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/488390/image-preview)
</Background>




### 特殊标记

- `*` 号标记表示该参数为必填项

## 使用示例

以图中展示的 `ACCESS_TOKEN` 为例：

- 位置：Header（请求头）
- 参数名：ACCESS_TOKEN
- 类型：string（字符串）
- 默认值：`{{ACCESS_TOKEN}}`，该值从环境变量中读取
- 用途：接口鉴权凭证

   
<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/488391/image-preview)
</Background>


在接口中发送请求后，即可在响应控制台的 “实际请求” 中查看携带的参数信息。

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/488392/image-preview)
</Background>


## 注意事项

1. 全局参数的优先级低于接口级别的参数配置
2. 添加新参数时注意检查参数名称是否重复
3. 参数类型要与实际使用场景相匹配
4. 敏感信息建议使用环境变量或其他安全方式管理

## 常见问题解答


<Accordion title="如何临时禁用某个全局参数？" defaultOpen>
直接切换参数右侧的启用/禁用开关即可。
    
<Frame>
![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/493067/image-preview)
</Frame>

</Accordion>

<Accordion title="全局参数和环境变量的区别是什么？" defaultOpen>
全局参数主要用于 API 请求中固定的参数配置，而环境变量更适合管理在不同环境下会变化的配置信息。
</Accordion>



