# 常见问题


> **此插件配置过于灵活, 以下均为示例, 需根据实际情况做合适的处理。**



## 如何添加配置文件

- 参考[项目内配置](https://docs.apifox.com/5801720m0.md)



## 如何组织 API 到指定模块、API 分组

- `module` 用于分类 api

- 默认情况下取当前模块名(单模块项目取项目名)
- 默认推荐配置:

```properties
#find module from comment tag
module=#module
```

- 在类上这样注释:

```
/**
 * Mock Apis
 *
 * @module mock
 */
@RestController
@RequestMapping(value = "mock")
public class MockCtrl {
}
    ```


:::highlight purple 💡
更多详细配置可参考[配置文档](https://docs.apifox.com/5801721m0.md)
:::
  


## 怎么设置接口 API 所属文件夹的名称

- 需要在配置文件里要开启这个配置，以下是 `.apifox-helper.properties` 示例

```
# read folder name from tag `folder`
folder.name=#folder
```

- 使用 `@folder` 注释


    <Background>

    ![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/488293/image-preview)
    </Background>


- 也可以进行多级目录注释：


    <Background>

    ![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/488295/image-preview)
    </Background>


:::highlight purple 💡
更多详细配置可参考[配置文档](https://docs.apifox.com/5801721m0.md)
:::


## 如何增加外层的公共返回响应 Response 泛型

- 需要在配置文件里要开启这个配置，以下是 `.apifox-helper.properties` 示例

```
# 假定 公共 ResponseDo 的包名为 com.xxx
method.return=groovy: "com.xxx.ResponseDo<" +  it.returnType() +">"
```

:::highlight purple 💡
更多详细配置可参考[配置文档](https://docs.apifox.com/5801721m0.md)
:::


## 如何忽略 API

- 增加配置:

```
#ignore class or method which has comment tag 'ignore'
ignore=#ignore
```

- 在类上注释@ignore 忽略当前类

```
/**
 * Mock Apis
 *
 * @ignore
 */
@RestController
@RequestMapping(value = "mock")
public class MockCtrl {
}
```

- 在方法上注释@ignore 忽略当前 API

```
/**
 * Mock Apis
 */
@RestController
@RequestMapping(value = "mock")
public class MockCtrl {

     /**
      * Mock String
      * @ignore
      */
     @GetMapping("/string")
     public String mockString() {
         return Result.success("mock string");
     }

}
```



## 如何设置 API/文件夹的名称/描述

- 一般来说:

```
/**
* 第一行注释作为文件夹的标题
* 剩余行注释作为文件夹的描述
*/
@RestController
@RequestMapping(value = "mock")
public class MockCtrl {

  /**
   * 第一行行注释作为 API 的标题
   * 剩余行注释作为 API 的描述
   */
  @GetMapping("/string")
  public String mockString() {
      return Result.success("mock string");
  }
}
```

<!--
- 特殊需求参照:[class.doc](./setting/setting-rule/#class-doc) | [method.doc](./setting/setting-rule/#method-doc) | [api.name](./setting/setting-rule/#api-name)
-->


## 如何在 API/文件夹的描述中说明 API/文件夹被废弃了

- 默认推荐配置如下:

```properties
method.doc[#deprecated]=groovy:"\n「deprecated」" + it.doc("deprecated")
method.doc[@java.lang.Deprecated]=「deprecated」
method.doc[@kotlin.Deprecated]=groovy:"\n「deprecated」" + it.ann("kotlin.Deprecated","message")

method.doc[groovy:it.containingClass().hasDoc("deprecated")]=groovy:"\n「deprecated」" + it.containingClass().doc("deprecated")
method.doc[groovy:it.containingClass().hasAnn("java.lang.Deprecated")]=「deprecated」
method.doc[groovy:it.containingClass().hasAnn("kotlin.Deprecated")]=groovy:"\n「deprecated」 " + it.containingClass().ann("kotlin.Deprecated","message")

```

- 使用注解或者注释标记 API 废弃即可:

```java
/**
* 可以用注解`@Deprecated`来表示 api 废弃
* 也可以用注释`@deprecated`
*
* @deprecated 改用{@link #methodName3(String)}
*/
@Deprecated
@RequestMapping(value = "/pathOfApi2")
public Result methodName2(@RequestBody MockDtoOrVo jsonModel){
  ...
}
```



## 如何在 API 描述中声明 API 需要的权限(javax annotation security)

- 可考虑增加如下配置:

```properties
## security description
method.doc[@javax.annotation.security.RolesAllowed]=groovy:"require role:"+it.ann("javax.annotation.security.RolesAllowed")
```

- 示例:

```java
/**
 * 第一行注释作为文件夹的标题
 * 剩余行注释作为文件夹的描述
 */
@RestController
@RequestMapping(value = "mock")
public class MockCtrl {

    /**
     * 第一行行注释作为 API 的标题
     * 剩余行注释作为 API 的描述
     */
    @GetMapping("/string")
    @RolesAllowed("admin")
    public String mockString() {
        return Result.success("mock string");
    }
}

```


## 如何在 API 描述中声明 API 需要的权限(spring security)

- 可考虑增加如下配置:

````properties
## security description
doc.method[@org.springframework.security.access.prepost.PreAuthorize]=groovy:```
   def preAuthorize = it.ann("org.springframework.security.access.prepost.PreAuthorize")
   if(tool.nullOrBlank(preAuthorize)){
        return
   }
   def role = regex.getGroup1("hasRole\\('(.*?)'\\)",preAuthorize)
   return "require role: $role"
```
````

- 示例:

```java
/**
 * 第一行注释作为文件夹的标题
 * 剩余行注释作为文件夹的描述
 */
@RestController
@RequestMapping(value = "mock")
public class MockCtrl {

    /**
     * 第一行行注释作为 API 的标题
     * 剩余行注释作为 API 的描述
     */
    @GetMapping("/string")
    @PreAuthorize("hasRole('admin')")
    public String mockString() {
        return Result.success("mock string");
    }
}

```

---

## 如何忽略某些字段

- 使用规则: `json.rule.field.ignore`

  - 忽略特定名称的字段:

```properties
## ignore field 'log'
json.rule.field.ignore=log
```

  - 忽略特定类型的字段:

```properties
## ignore field 'log' typed xxx.xxx.Log
json.rule.field.ignore=groovy:it.type().name()=="xxx.xxx.Log"
```

  - 忽略特定限定符的字段:

```properties
#ignore transient field
json.rule.field.ignore=groovy:it.hasModifier("transient")
```



## 如何将指定类型转换为另一种类型处理

- 将`java.time.LocalDateTime`作为`yyyy-mm-dd`形式字符串处理

```properties
#Resolve 'java.time.LocalDateTime' as 'java.lang.String'
json.rule.convert[java.time.LocalDateTime]=java.lang.String
json.rule.convert[java.time.LocalDate]=java.lang.String
```

- 将`java.time.LocalDateTime`作为`timestamp`处理

```properties
#Resolve 'java.time.LocalDateTime' as 'java.lang.Long'
json.rule.convert[java.time.LocalDateTime]=java.lang.Long
json.rule.convert[java.time.LocalDate]=java.lang.Long
```

## 部分接口可能有不同的返回

- 可以使用 `method.doc` 将可能的返回放在方法备注中

_**配置如下:**_

````properties
method.doc[#result]=groovy: it.docs("result").collect{helper.resolveLink(it)}.grep{it!=null}.collect{"可能的返回:\n\n```json\n"+it.toJson(true)+"\n```\n\n"}.join("\n")
````

_**使用如下:**_

```properties
 /**
  * @result {@link UserInfo}
  * @result {@link Result<UserInfo>}
  */
 public Result mockString() {
     ...
 }
```

## 有的字段可能有不同类型的值

- 可以使用 `field.doc` 将可能的类型值放在字段备注中

_**配置如下:**_

````properties
 field.doc[#maybe]=groovy:it.docs("maybe").collect{helper.resolveLink(it)}.collect{"可能是:\n\n```json\n" + it.toJson(true) +"\n```\n\n"}.join("\n")
````

_**使用如下:**_

```properties
 /**
  * @maybe {@link UserInfo}
  * @maybe {@link java.lang.String}
  */
 public Object target;
```

## 如何适配 Mybatis Plus 工程的分页 Page 模型和请求参数？

首先确保插件版本升级至 `>= 1.1.16`，然后可以通过[项目内配置](https://docs.apifox.com/5801720m0.md)规则来实现适配识别。

以下内容里，`Page 模型 = com.baomidou.mybatisplus.extension.plugins.pagination.Page`，注意有些配置是可选的，根据自己的项目代码风格选择即可。

- 如果使用了 Page 模型但接口方法的返回值不识别，先确保使用了 `method.return` 配置，并增加注释 `@response` 如下图

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/488300/image-preview)
</Background>


- 可选，当一个接口的返回的 Page 模型，导致导出接口信息过多且杂乱无章的问题

```properties
json.cache.disable=true
api.param.parse.before=groovy:session.set("isParam",true)
api.param.parse.after=groovy:session.remove("isParam")
json.rule.field.ignore[com.baomidou.mybatisplus.extension.plugins.pagination.Page#records]=groovy:session.get("isParam")
```

- 可选，当一个接口的返回的 Page 模型作为请求参数，想要忽略一些内置的大部分字段，只保留 `current, size`

```properties
field.ignore=groovy:it.defineClass().name() == "com.baomidou.mybatisplus.extension.plugins.pagination.Page" && !["current","size"].contains(it.name())
```

- 可选，当一个接口的返回的 Page 模型的字段 records 实际想在文档字段改为 data，可以添加下面的配置

```properties
field.name=groovy:(it.defineClass().name() == "com.baomidou.mybatisplus.extension.plugins.pagination.Page"&&it.name()=="records")?"data":null
```

> 参考来源 [Github Issue](https://github.com/tangcent/easy-yapi/issues/778)，[其他文章](https://blog.csdn.net/qq_42009500/article/details/125432638)

## 如何开启 javax_validation 分组校验

- 参照 [javax_validation](https://easyyapi.com/framwork/javax_validation.html), 在 Preferences(Settings) > Other Settings > EasyApi >Recommend 中移除勾选`javax.validation`, 勾选`javax.validation(grouped)`

## 如何激活对 com.fasterxml.jackson.annotation.JsonIgnoreProperties 的支持

- 在 Preferences(Settings) > Other Settings > EasyApi >Recommend 中勾选`Jackson_JsonIgnoreProperties`

## 导出时出现 com.xxx.Xxx is to complex. Blocked cause by xxx reached xxx, 如何处理

- 检查错误信息中的类是否不应该出现在请求体/响应中, 可尝试做如下配置:

```properties
# ignore field with type com.xxx.Xxx
field.ignore=groovy:it.type().name()=="com.xxx.Xxx"
```

- 如果此类确实字段繁多, 需要完全解析, 可通过配置放宽解析限制:

```properties
max.deep=8
max.elements=512
```

## 导出时出现 No APIs be found to upload!, 如何处理

- 检查项目依赖是否成功导入，项目能否成功运行


