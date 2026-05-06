# 云端 Mock

云端 Mock 是为需要高可用 API 的团队提供的一项重要功能。与只能在本地电脑运行的本地 Mock 不同，云端 Mock 提供了一个持久且随时可访问的解决方案。下面是云端 Mock 的主要特点和使用场景：

1. **全项目成员可访问**：所有项目成员共享同一个云端 Mock 地址，便于协作并保持一致性。
2. **持续可用**：云端 Mock 全天候在线，不受项目成员电脑开关机状态的影响。
3. **适合公开 API 文档**：可以为面向公众的 API 文档创建沙箱环境。
4. **非生产数据来源**：为非生产环境提供可靠的数据来源。

## 开启云端 Mock

要为你的项目开启云端 Mock，需要：

1. 在项目中打开 “项目设置”
2. 选择 “功能设置 -> Mock 设置”
3. 启用 “云端 Mock”


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/481062/image-preview)
</Background>


## 使用云端 Mock

开启后，你可以通过以下方式使用云端 Mock：

1. 访问任一接口，在 Mock 标签页的 “Mock 地址” 中点击 “云端” 标签获取云端 Mock 地址。
2. 点击 “快捷请求” 按钮立即获取响应数据。
3. 对于 GET 请求，可以直接在浏览器中访问云端 Mock 地址，查看响应数据。

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/488012/image-preview)
</Background>



## 访问权限

云端 Mock 支持通过 Token 鉴权进行访问控制：

1. 进入 “项目设置 -> 功能设置 -> Mock 设置”
2. 将访问权限设置为 “Token 鉴权”

使用带鉴权的云端 Mock：

1. 在请求地址中加入 token：
   ```js
   https://mock.apifox.com/m1/2689726-0-default/users?apifoxToken=GdfNrEm6lxM9nDGGIMCWC1OPSiZ6hGOi
   ```

2. 对于快捷请求，在 Header 参数中添加 `apifoxToken` 参数

3. 对于 form-data 和 x-www-form-urlencoded 请求，在 Body 参数中添加 `apifoxToken` 参数

通过使用云端 Mock，团队可以确保在 API 开发和测试过程中拥有稳定且始终可用的 Mock 接口。这种方式不仅简化了协作流程，完善了文档体系，还为非生产环境提供了可靠的数据来源。
