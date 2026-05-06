# Redis

:::info[]
连接 Redis 数据库是 Apifox 企业版功能，请添加[企业微信客服](https://docs.apifox.com/siyouhua.md)了解更多信息。
:::

Redis *（Remote Dictionary Server）* 是一个提供键值对（Key-Value）存储能力的**非关系型数据库（NoSQL）**。Redis 将数据保存在内存中，可以在保证低延迟的读取和写入速度的同时，兼顾持久化功能，特别适合需要高性能缓存的应用场景，比如聊天室、排行榜、实时系统等。

## 连接数据库

1. 点击接口中的 “前置/后置操作”，选择 “数据库操作”。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/480342/image-preview)
</Background>


2. 点击 “数据库连接” 下拉框中的 “数据库连接管理” 选项，然后点击右上角的新建按钮。


<Background>
![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/480349/image-preview)
</Background>

3. 选择 Redis 数据库类型，然后填写相对应的连接信息。


<Background>
<img style="width:440px" src="https://api.apifox.com/api/v1/projects/5097254/resources/480369/image-preview"/>
</Background>


:::tip[]
Apifox 重视您的数据安全。**数据库地址、端口、用户名、 密码、数据库名**仅存储在客户端本地，不会同步到云端。即便是同一团队内，成员之间也不会相互同步数据库的连接信息，每个团队成员需要自己手动设置数据库。
:::

## 操作数据库

### 常用操作

对于常用的数据库增删查改操作，Apifox 提供可视化的界面。无需撰写任何代码或者 Redis 命令，你只需在 “操作” 中选择一种操作类型，然后在表单中填写相应的内容即可。例如要获取数据库列表内的单个元素，参考下图选择操作类型后点击发送按钮。

开启了 “控制台打印结果” 后就可以在控制台查看查询到的结果。


<Background>
    <img style="width:640px" src="https://api.apifox.com/api/v1/projects/5097254/resources/480371/image-preview"/>
</Background>


### 进阶命令

如果要进行更加高级的操作，Apifox 也支持直接运行 Redis 高级命令。切换至“运行 Redis 命令” tab 页，然后输入具体的 Redis 命令即可。以上图的查询操作为例，你也可以直接运行等价的 Redis 命令来获取结果：


<Background>
<img style="width:640px" src="https://api.apifox.com/api/v1/projects/5097254/resources/480373/image-preview"/>
</Background>


