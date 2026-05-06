# 生成接口文档


本节将详细介绍如何利用 Apifox helper 来生成全面且精确的接口文档。

![](https://cdn.apifox.cn/uploads/help/202401101156728.png)

## 1. 配置控制器类

首先，我们需要正确配置控制器类。在类级别的 Javadoc 中，我们可以定义文件名称和项目归属：

```java
/**
 * 文件名称
 * @module 归属项目
 */
@RestController
@RequestMapping(value = "/pathOfCtrl")
public class MockCtrl { ... }
```

- `@RestController` 注解表明这是一个 RESTful Web 服务的控制器。
- `@RequestMapping(value = "/pathOfCtrl")` 定义了该控制器的基本 URL 路径。
- 类级 Javadoc 注释用于生成 API 的分类信息及项目模块归属。
  - 注释的第一行将作为文件名称，如果使用 “父目录/文件名称” 的格式编写，将自动生成对应的文件夹结构，实现文档的层次化组织。
  - `@module` 标签指定 API 所属的项目。

## 2. 定义 API 方法

对于每个 API 方法，我们需要提供详细的 Javadoc 注释：

```java
/**
 * api名称
 * api描述
 * @param param1 参数1的名称或描述
 * @param param2 参数2的名称或描述
 * @return 响应描述
 */
@RequestMapping(value = "/pathOfApi1")
public Result methodName1(long param1,long param2){
    // 方法实现
}
```



### 方法名称

- 方法名（如`methodName1`）通常用作 API 操作的标识符。



### 路径

- 路径由类级别的`@RequestMapping`和方法级别的`@RequestMapping`（或`@GetMapping`, `@PostMapping`等）组合而成。
- 完整路径：`/pathOfCtrl/pathOfApi1`



### HTTP 方法

- 默认为 GET
- 可通过`@RequestMapping(method = RequestMethod.POST)`或直接使用`@PostMapping`等指定



### 请求参数

- 从方法参数和 Javadoc 的`@param`标签中提取
- `@RequestParam(required = false)` 表示可选参数
- `defaultValue` 属性指定默认值


### 响应

- 从`@return` Javadoc 标签中提取响应描述

## 3. 请求体参数

对于使用请求体的 API，我们可以这样定义：

```java
/**
 * 默认使用`query`,
 * 对于`@RequestBody`将使用`application/json`
 */
@RequestMapping(value = "/pathOfApi2")
public Result methodName2(@RequestBody MockDtoOrVo jsonModel){
    // 方法实现
}
```

- 默认使用`query`
- 当使用`@RequestBody`注解时，Apifox helper 会自动识别并设置 Content-Type 为`application/json`。

## 4. API 废弃标记

可以使用`@Deprecated`注解或`@deprecated` Javadoc 标签来标记将废弃的 API：

```java
/**
 * @deprecated
 */
@Deprecated
@RequestMapping(value = "/pathOfApi2")
public Result methodName2(@RequestBody MockDtoOrVo jsonModel){
    // 方法实现
}
```

## 示例

以下是一个 Java 代码示例，以及与之相对应的 API spec：

### 代码示例

```java
/**
 * 用户管理
 * 处理用户相关的操作，包括创建、查询和更新用户信息
 *
 * @module 用户系统
 */
@RestController
@RequestMapping(value = "/api/users")
public class UserController {

    /**
     * 创建新用户
     * 根据提供的用户信息创建一个新的用户账户
     *
     * @param userInfo 包含用户信息的对象，包括用户名、邮箱、密码和用户类型
     * @return 创建成功的用户信息
     */
    @PostMapping
    public Result createUser(@RequestBody UserInfo userInfo) {
        // 方法实现
    }

    /**
     * 获取用户信息
     * 根据用户ID获取详细的用户信息
     *
     * @param userId 要查询的用户ID
     * @return 用户详细信息
     */
    @GetMapping("/{userId}")
    public Result getUserInfo(@PathVariable Long userId) {
        // 方法实现
    }

    /**
     * 更新用户信息
     * 更新指定用户的信息
     *
     * @param userId 要更新的用户ID
     * @param userInfo 包含更新信息的用户对象
     * @return 更新后的用户信息
     */
    @PutMapping("/{userId}")
    public Result updateUser(@PathVariable Long userId, @RequestBody UserInfo userInfo) {
        // 方法实现
    }

    /**
     * 删除用户
     * 删除指定的用户账户
     *
     * @param userId 要删除的用户ID
     * @return 操作结果
     * @deprecated
     */
    @Deprecated
    @DeleteMapping("/{userId}")
    public Result deleteUser(@PathVariable("userId") Long userId) {
        // 方法实现
    }

    /**
     * 停用用户账户
     * 将指定用户账户设置为非活动状态，而不是永久删除
     *
     * @param userId 要停用的用户ID
     * @return 操作结果
     * @see #deleteUser(Long)
     */
    @PostMapping("/{userId}/deactivate")
    public Result deactivateUser(@PathVariable("userId") Long userId) {
        // 方法实现
    }
}
```

### 生成的 API Spec（OpenAPI 3.0）

```yaml
openapi: 3.0.0
info:
  title: 用户管理
  description: 处理用户相关的操作，包括创建、查询和更新用户信息
  version: 1.0.0
tags:
  - name: 用户系统
paths:
  /api/users:
    post:
      summary: 创建新用户
      description: 根据提供的用户信息创建一个新的用户账户
      tags:
        - 用户系统
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/UserInfo'
      responses:
        '200':
          description: 创建成功的用户信息

  /api/users/{userId}:
    get:
      summary: 获取用户信息
      description: 根据用户ID获取详细的用户信息
      tags:
        - 用户系统
      parameters:
        - name: userId
          in: path
          required: true
          schema:
            type: integer
            format: int64
          description: 要查询的用户ID
      responses:
        '200':
          description: 用户详细信息

    put:
      summary: 更新用户信息
      description: 更新指定用户的信息
      tags:
        - 用户系统
      parameters:
        - name: userId
          in: path
          required: true
          schema:
            type: integer
            format: int64
          description: 要更新的用户ID
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/UserInfo'
      responses:
        '200':
          description: 更新后的用户信息

    delete:
      summary: 删除用户
      description: 删除指定的用户账户
      deprecated: true
      tags:
        - 用户系统
      parameters:
        - name: userId
          in: path
          required: true
          schema:
            type: integer
            format: int64
          description: 要删除的用户ID
      responses:
        '200':
          description: 操作结果

  /api/users/{userId}/deactivate:
    post:
      summary: 停用用户账户
      description: 将指定用户账户设置为非活动状态，而不是永久删除
      tags:
        - 用户系统
      parameters:
        - name: userId
          in: path
          required: true
          schema:
            type: integer
            format: int64
          description: 要停用的用户ID
      responses:
        '200':
          description: 操作结果

components:
  schemas:
    UserInfo:
      type: object
      properties:
        username:
          type: string
          description: 用户名
        email:
          type: string
          description: 用户的电子邮件地址
        password:
          type: string
          description: 用户密码
        userType:
          type: string
          enum: [ADMIN, REGULAR, GUEST]
          description: 用户类型
```

