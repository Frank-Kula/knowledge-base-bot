# 密码凭证授权类型


## 什么是资源所有者密码凭证授权类型

资源所有者密码凭证授权类型（Resource Owner Password Credentials Grant Type）旨在直接通过用户名和密码交换获取访问令牌。因此，它要求用户与客户端应用之间有很高的信任度，而且仍然需要采取额外措施来减轻可能存在的漏洞和复杂性。考虑到 OAuth 2.0 的最佳实践，不建议使用 ROPC。

## 资源所有者密码凭证（ROPC）流程是什么

根据 [OAuth 2.0 授权框架 RFC6749](https://datatracker.ietf.org/doc/html/rfc6749#section-1.3.3) 的定义，资源所有者密码凭证授权（也称为 _ROPC_）可以直接通过客户端提供的最终用户凭证向授权服务器获取访问令牌。只有当资源所有者与客户端之间存在高度信任度时才应使用凭据（例如，客户端是设备操作系统的一部分或是具有高权限的应用程序）。

## 使用 ROPC 流程获取令牌

## ROPC 的工作原理


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/486125/image-preview)
</Background>


1. 客户端通过调用令牌端点请求令牌。

2. 授权服务器验证用户凭证。

3. 当用户凭证有效时，授权服务器返回访问令牌（Access Token）和标识令牌（ID Token）。

5. 用户得到认证。

