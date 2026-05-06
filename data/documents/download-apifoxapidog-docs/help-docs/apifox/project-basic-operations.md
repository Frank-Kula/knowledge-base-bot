# 项目基本操作

在 Apifox 中，你可以创建和管理多个项目，以便更好地组织和管理接口。

## 创建项目

团队所有者或团队管理员可通过 “团队项目 -> 新建项目」 -> 新建”，创建新的项目。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/485337/image-preview)
</Background>


## 项目概览

进入到一个已创建项目中，可以在 “接口管理 -> 项目概览” 页中，看到该项目的重要信息和统计信息。


### 接口用例 / 测试场景覆盖

可以在这个模块内查看当前项目的全部接口，以及接口用例与测试场景的覆盖情况。通过这些统计数字可以直观、量化的了解到当前项目中的接口是否被合理测试，以及接口质量是否更加可靠。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/485338/image-preview)
</Background>


其中，核心数据：

- **接口用例覆盖率**，带有接口用例的接口数/总接口数，主要用来查看单个接口是否有被接口用例覆盖；
- **平均每个接口带有的用例数**，接口用例总数/总接口数，主要用来查看接口的用例整体完善程度；
- **不带用例的接口数**，主要用来查看未被接口用例覆盖的接口数量；
- **测试场景覆盖率**，被测试场景关联的接口数/总接口数，主要用来查看接口被自动化测试所覆盖的情况；
- **不被测试场景覆盖的接口数**，主要用来查看还没有被自动化测试覆盖的接口数量。


:::tip[]
注意：此处数据的计算是异步的，因此会有延迟。如果发现数据有异常可以等待一段时间后再刷新确认。
:::

## 编辑项目

团队所有者 / 管理员进入到已创建的项目中，在 “项目设置 -> 基础设置 -> 编辑” 中更换项目的名称或者项目图标。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/485339/image-preview)
</Background>


## 克隆项目

**克隆项目**：通过 “项目设置 -> 基础设置 -> 克隆”，可克隆项目到当前团队或其他团队。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/485340/image-preview)
</Background>


## 移动项目

**移动项目**：通过 “项目设置 -> 基础设置 -> 移动项目”，将项目移动到其他团队。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/485341/image-preview)
</Background>


## 删除项目

**删除项目**：通过 “项目设置 -> 基础设置 -> 删除”，将项目彻底删除。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/485342/image-preview)
</Background>


:::caution[]
务必谨慎，删除后项目不可以找回。
:::

