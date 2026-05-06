# 语言设置


为了更好的支持国际化团队的开发工作，Apifox 支持独立调整软件语言、项目语言以及文档语言三种设置。

## 软件语言

`软件语言` 表示软件工具界面上的语言。点击右上角 `设置 - 通用 - 软件语言` 进行调整，变更只会影响本地使用，不会影响团队其他人员，也不会影响已发布的`在线文档`中的网页语言。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/485679/image-preview)
</Background>


不过你也许会发现即使将软件语言切换至英语后，项目中的部分内容的语言仍未修改，这时候就需要调整 “项目语言”。

## 项目语言

`项目语言` 表示项目内自动生成的默认名称的语言，包含 `接口用例`、`返回响应`、`响应示例`、`Markdown 文档` 的默认名称以及`测试数据` 的默认数据集名称。


点击 “项目设置 -> 基础设置 -> 项目语言” 进行修改。


<Background>

![CleanShot 2024-12-23 at 13.53.04@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/485684/image-preview)
</Background>


仅**项目管理员**有权限前往项目设置进行修改。修改项目语言后，当前项目中的团队成员会使用同一套 `项目语言`，包括已发布的 `在线文档` 中的文档语言设置也会跟随 `项目语言`。

:::tip[]
接口文档内已有的的数据不会被自动翻译，需手动进行修改。
:::

**新建项目时指定项目语言**

管理员也可以在不影响 “软件语言” 的前提下指定项目语言。新建项目时，可以将`项目语言`指定为其它语言。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/485685/image-preview)
</Background>


如果你勾选 `包含示例数据` 选项，那么项目中的示例数据会根据 `项目语言` 生成对应语言的数据。

## 文档语言

文档语言指的是在线 API 文档上的默认语言，将会影响网页的 `lang` 属性。你可以在点击 `分享文档 -> 基础设置 -> 语言` 进行调整。


<Background>

![CleanShot 2024-12-23 at 13.57.12@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/485689/image-preview)
</Background>


