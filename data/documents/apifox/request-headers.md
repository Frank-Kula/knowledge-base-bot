# 请求头

一些 API 要求在请求中包含特定的请求头，以提供有关请求的元数据。你可以在 Apifox 中配置请求头，同时 Apifox 会根据需要自动添加请求头。

## 配置请求头

可以在请求的 Headers 标签中设置请求头。输入所需的任何键值对，Apifox 会将其与请求一起发送。光标聚焦到输入框时会有常用选项的提示，以帮助你快速完成设置，例如 `Content-Type`。

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/470058/image-preview)
</Background>


## 自动生成的请求头

Apifox 会自动添加某些请求头。点击请求的 Headers 标签顶部的 `Hidden` 选项，可以查看 Apifox 将跟随请求发送的信息。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/470063/image-preview)
</Background>


将鼠标悬停在请求头上可以查看其详细信息。Apifox 会指明该请求头为何被添加，以及如何在需要时停用或覆盖请求头的值。

你可以在 **Authorization** 标签、请求的 **Body**、请求域的 **Cookies**、设置以及某些情况下的 **Headers** 标签中修改请求头。如果需要导航到应用的不同部分，Apifox 会在右侧显示相关链接。

要在 **Headers** 标签中停用自动生成的请求头，请取消勾选相应的复选框。若要覆盖自动生成的请求头值，取消勾选自动生成条目旁的复选框，然后添加一个新的条目，填写请求头的名称和所需的值。

如果同一个请求头有多个条目，Apifox 会指示哪些条目将被覆盖。优先使用你在 **Headers** 中显式添加的请求头，或通过其他请求部分 *（如 **Authorization**）* 间接添加的请求头。被覆盖的请求头将显示为 `~~Authorization~~`。

对于 `Content-Length` 和 `Content-Type` 请求头，Apifox 会根据 Body 标签中的数据在发送请求时自动计算其值。不过，你也可以覆盖这两个值。
