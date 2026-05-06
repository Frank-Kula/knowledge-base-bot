# 生成数据模型


本节重点介绍如何利用 Apifox helper 生成全面且精确的数据模型，包括模型名、字段名、字段说明、中文名、枚举等关键信息。

## 1. 定义数据模型类

首先，我们需要在 Java 中定义一个数据模型类。这个类通常是一个简单的 POJO (Plain Old Java Object) 或 DTO (Data Transfer Object)。例如:

```java
public class UserInfo {
    // 字段定义
}
```

## 2. 添加字段和 Javadoc 注释

在类中添加字段，并为每个字段添加 Javadoc 注释。这些注释将被 Apifox helper 用来生成数据模型的每个字段的说明信息。

```java
public class UserInfo {

    /**
     * 用户ID
     */
    private Long id;

    /**
     * 用户名
     */
    private String username;

    /**
     * 用户邮箱
     */
    private String email;

    /**
     * 用户类型 枚举说明
     * @see UserType
     */
    private String userType;

    // ... 其他字段
}
```

## 3. 使用注解增强字段信息

可以使用各种注解来提供额外的字段信息，这些信息会被 Apifox helper 识别并包含在生成的数据模型中。

```java
public class UserInfo {

    /**
     * 用户ID
     */
    @NotNull
    private Long id;

    /**
     * 用户名
     */
    @NotBlank
    private String username;

    /**
     * 用户邮箱
     */
    @Email
    private String email;

    /**
     * 用户类型
     * @see UserType
     */
    @NotNull
    private String userType;

    /**
     * 用户状态
     * @deprecated 将在下一个版本移除
     */
    @Deprecated
    private String status;

    // ... 其他字段
}
```

## 4. 定义枚举类型

对于枚举字段，可以创建一个单独的枚举类，并在字段的 Javadoc 中使用`@see`标签引用它。

```java
public enum UserType {
    ADMIN,
    REGULAR,
    GUEST
}
```

然后在`UserInfo`类中引用这个枚举。

```java
public class UserInfo {
    // ... 其他字段

    /**
     * 用户类型
     * @see UserType
     */
    private String userType;

    /**
    * 默认枚举实现
    */
    private UserType userTypeEnum;

    // ... 其他字段
}
```

## 5. 使用中文名和详细说明

在 Javadoc 注释中，可以提供字段的中文名和更详细的说明。


首先设置中文名规则`field.schema.title=#titleName`，此规则的意思是当你使用`@titleName`的`javadoc`注释时它的值作为中文名上传至 Apifox。

```java
public class UserInfo {

    /**
     * userId
     * @titleName 用户ID
     */
    @NotNull
    private Long id;

    /**
     * userName
     * @titleName 用户名
     */
    @NotBlank
    private String username;

    /**
     * email
     * @titleName 电子邮箱
     */
    @Email
    private String email;

    // ... 其他字段
}
```

## 6. 指定字段的默认值或示例值

可以在 Javadoc 中使用特殊的标记来指定字段的默认值或示例值。


默认值规则`field.defaultValue=#default`，示例值规则`field.example=#example`，此规则的意思是当你使用`@default`的`javadoc`注释时它的值作为默认值，使用`@example`的`javadoc`注释时它的值作为示例值。

```java
public class UserInfo {

    /**
     * 用户年龄
     * @default 18
     */
    private int age;

    /**
     * 用户积分
     * @example 100
     */
    private int points;

    // ... 其他字段
}
```

## 7. 嵌套对象和集合

对于复杂的数据结构，可以使用嵌套对象和集合。

```java
public class UserInfo {

    // ... 其他字段

    /**
     * 用户地址
     */
    private Address address;

    /**
     * 用户角色列表
     */
    private List<Role> roles;

    // ... 其他字段
}

public class Address {
    /**
     * 街道
     */
    private String street;

    /**
     * 城市
     */
    private String city;

    // ... 其他字段
}

public class Role {
    /**
     * 角色ID
     */
    private Long id;

    /**
     * 角色名称
     */
    private String name;

    // ... 其他字段
}
```

## 8. 生成数据模型

从以上的代码生成数据模型如下。

```yaml
openapi: 3.0.0
components:
  schemas:
    UserInfo:
      type: object
      required:
        - id
        - username
        - email
        - userType
      properties:
        id:
          type: integer
          format: int64
          description: 系统生成的唯一标识符
        username:
          type: string
          description: 用户登录系统时使用的名称，必须唯一
        email:
          type: string
          format: email
          description: 用户的联系邮箱，用于接收系统通知
        userType:
          $ref: '#/components/schemas/UserType'
        age:
          type: integer
          description: 用户年龄
          default: 18
        points:
          type: integer
          description: 用户积分
          example: 100
        status:
          type: string
          description: 用户状态
          deprecated: true
        address:
          $ref: '#/components/schemas/Address'
        roles:
          type: array
          items:
            $ref: '#/components/schemas/Role'

    UserType:
      type: string
      enum:
        - ADMIN
        - REGULAR
        - GUEST

    Address:
      type: object
      properties:
        street:
          type: string
          description: 街道
        city:
          type: string
          description: 城市

    Role:
      type: object
      properties:
        id:
          type: integer
          format: int64
          description: 角色ID
        name:
          type: string
          description: 角色名称
```

