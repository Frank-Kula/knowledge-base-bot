# 管理其它项目接口的运行环境


## 首次关联其它项目的接口运行环境

当你选择了某个其它项目并首次导入该项目的数据作为测试步骤时，为了确保这些步骤能够正常运行，避免出现不按预期使用服务（前置 URL）的问题发生，产品页面将引导你进行 **“环境关联”** 设置，将这个其它项目的环境，与当前项目的环境关联起来。

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/481824/image-preview)
</Background>


## 管理其它项目接口的运行环境

其它项目的接口被导入到本项目中作为场景用例的步骤，这些被导入的其它项目与本项目的环境关联关系，可以在环境关联功能中查看。

-   入口 1：在测试步骤导入其它项目的接口时，点击 **“环境关联”** 进行管理。

    <Background>

    ![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/481825/image-preview)
    </Background>


-   入口 2：若当前场景用例内已导入了其它项目的接口，在功能测试的运行环境下会出现提示并可以点击进行管理。


    <Background>

    ![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/481826/image-preview)
    </Background>


    进入环境关联功能后即可看到所有被导入的其它项目，同时还可以看到它们与本项目的环境关联关系和具体服务（前置 URL）。


    <Background>

    ![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/481827/image-preview)
    </Background>


## 其它项目导入步骤的权限控制

点击 Apifox 首页里的 **“成员/权限”**  tab 页查看或管理团队成员的权限。如果你没有目标项目的只读及以上权限，那么你无法点击进入详情查看或编辑从该项目导入的接口/接口用例。

### 查看/编辑其它项目导入接口的步骤详情

导入其它项目的接口至测试步骤时，操作者需具备目标项目 **“只读”** 及以上的编辑权限。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/481831/image-preview)
</Background>

若不具备相对应的权限，则无法查看或编辑该接口。

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/481833/image-preview)
</Background>


### 运行含有其它项目接口的场景用例

若希望运行含有其它项目接口的场景用例，则操作者需要具备**所有**被导入的其它项目的 **“只读”及以上** 的编辑权限。若不具备某个项目的访问权限则无法运行场景用例。

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/481835/image-preview)
</Background>


## 手动同步其它项目的环境关联数据

为确保数据一致，如果其它项目中的接口或运行环境发生了变动与更新，你可以点击 **“查看这些步骤的运行方式 -> 立即同步”** 按钮更新当前场景用例内的跨项目数据。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/481836/image-preview)
</Background>


