# 创建和发送 Cookie

Apifox 的 Cookie 管理器允许你查看和修改与各种域名相关联的 Cookies，并在发起请求时使用它们。

## 关于 Cookie

Cookie 是从网站发送到用户浏览器的数据，并存储在用户的计算机上。它们为网站提供了一种记住用户状态信息 *（如在线商店的购物车）* 或记录用户浏览活动的机制。Cookie 通常包含两部分：网站名称和唯一的用户 ID。

当你返回网站时，它可以读取存储的 Cookie，记住你的信息和偏好，从而调整网站内容。如果没有 Cookie，你将需要重新登录或重新创建购物车。

## 使用 Cookie 管理器

在 Apifox 界面的右下角，你可以看到一个 “<Icon icon="material-outline-cookie"/> Cookie 管理” 按钮。点击此按钮可以打开 “Cookie 管理器” 窗口，在该窗口中，你可以查看所有与不同域名相关的 Cookie。
<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/472938/image-preview)
</Background>

## 创建 Cookie

要为某个域名创建新的 Cookie，点击 “**+ 新建**” 按钮。

Apifox 支持以下属性配置：

- **域名** - Cookie 发送的目标域名 *（不包括协议）*。
- **Cookie 名** - Cookie 的名称。
- **Cookie 值** - Cookie 的值。
- **Path** - 限制 Cookie 发送的 URL 路径。如果路径为 `/`，Cookie 会随所有该域名的请求一起发送。
- **Expires** - 指定 Cookie 失效的日期和时间。
- **MaxAge** - 设置 Cookie 的过期时间 *（以秒为单位）*。
- **HttpOnly** - 表示 Cookie 不能通过客户端脚本 *（如 JavaScript）* 访问，只能在请求的 Cookie 头中发送。此属性不影响 Apifox 的功能。
- **Secure** - 示 Cookie 仅通过 HTTPS 安全连接发送。

点击 “确定” 后，Cookie 将被保存到 Apifox 的 Cookie 管理器中，并关联到对应的域名。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/472946/image-preview)
</Background>



## 编辑或删除 Cookie

要修改现有的 Cookie，点击 “编辑” 按钮进行更改并保存。

要删除 Cookie，点击该 Cookie 旁边的 “删除” 按钮。

如果要清除所有保存的 Cookies 和域名，可以点击右上角的 “清空” 按钮。

## 随请求发送 Cookie

每当你向某个域名发起请求时，如果该域名关联有 Cookie，Apifox 会自动在请求的 **“Header”** 标签中添加 Cookie 信息。如果你看不到 Cookie，请选择 “隐藏” 以显示自动生成的头信息。

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/472944/image-preview)
</Background>


:::tip[]
你无法直接修改 Header 标签中的 Cookie 头信息。请使用 Cookie 管理器来修改 Cookie，或者删除 Cookie 并手动设置请求头。Apifox 会在发送请求之前自动将 Cookie 管理器中的 Cookie 与 Header 标签中的 Cookie 合并。
:::
