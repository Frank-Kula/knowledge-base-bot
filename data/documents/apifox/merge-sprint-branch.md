# 合并迭代分支



在迭代分支内完成 API 定义的开发并且内容成功上线后，可以将分支内的部分/所有接口变更一起合并至主分支。

## 合并迭代分支入口

当你处于某个迭代分支上时，你可以在接口管理中，分支选择器内看到“合并”按钮，也可以在接口管理的目录树下方看到“合并到主分支”按钮。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/485077/image-preview)
</Background>


对于自动化测试功能，测试场景的合并目前是需要单个进行合并的，并且不与接口管理那边的资源一起合并。当你处于某个迭代分支时，在自动化测试中，鼠标 hover 在某个测试场景的“...”按钮上，出现下拉操作“合并到主分支”。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/485078/image-preview)
</Background>


## 合并入非受保护分支

当一个拥有项目合并权限的用户执行合并，合并目标分支为一个没有设置为 “保护” 的分支时，可以在查看改动后直接将改动内容合入目标分支。


### 待合并内容总览

在接口管理中，点击“合并”按钮后，即会打开合并总览的弹窗。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/485079/image-preview)
</Background>


在此弹窗中，可以看到有重要内容：

- **筛选器**，可以使用筛选器来仅查看当前迭代分支中，相较于主分支修改了的资源；或者查看所有处于当前迭代分支中的所有资源。默认查看被改动了的资源，让用户更加聚焦于改动内容。
- **接口管理目录树**，这部分内容是最重要的内容，展示的是将当前迭代分支内容合并至主分支后，主分支目录树的最终效果（被影响的部分）。通过这个目录树来确认合并后的各资源位置、内容是否符合实际情况。目录树上的资源，在后方有 3 种颜色的圆点，用来标记本资源是一个未被改动（灰色圆点）、被修改（橙色圆点）、新增（绿色圆点）的资源。通过在右侧的勾选框中选中/取消选中，来确认本次合并是否想要合并这个资源到主分支中。
- **合并后接口状态**，可以选择合并后如何调整被合并资源在主分支的状态。共有“跟随当前迭代分支”、“跟随主分支”、“指定状态”三种逻辑可选。

### 待合并内容详情审核

在合并总览弹窗中，我们还可以针对目录树上的内容做更多操作，用以满足我们审核资源是否允许合并入主分支。点击某个资源，弹窗会自动展开变宽，这样就可以看到这个资源的内容详情，辅助用户做出是否合并的决策。

不同的资源会有不同的合并逻辑与详情页内容：

- **新增资源：**

  - 指在当前迭代分支中新创建的资源，主分支上没有此资源。
  - 如果选择合并，会在主分支指定位置新创建此资源。
  - 在目录树上点击，可以看到这个资源的完整内容。如下图所示。

  
    <Background>

    ![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/485080/image-preview)
    </Background>


- **修改资源：**

  - 指在当前迭代分支中从主分支上导入的资源，与主分支被导入资源有关联关系。
  - 如果选择合并，会对主分支关联资源内容进行覆盖修改。
  - 在目录树上点击，可以看到这个资源对比主分支资源的改动对比，以及完整内容。如下图所示。

  
    <Background>

    ![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/485081/image-preview)
    </Background>


- **无变动资源：**

  - 指在当前迭代分支中从主分支上导入的资源，与主分支被导入资源有关联关系，但是在当前迭代分支中没有对这个导入资源有任何修改。
  - 没有改动的资源不可选择合入主分支（也没有必要）。
  - 在目录树上点击没有这个资源的任何详情内容展示。如下图所示。

  
    <Background>

    ![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/485082/image-preview)
    </Background>


点击右下角的合并按钮，会将目录树上所有勾选选中的资源按照迭代分支设置位置合并入主分支。如果没有在合并弹窗中勾选选中，则此资源的内容不会一起合并入主分支。需要注意如果不选择合并某个父级资源，则其下方带的所有子级资源不可以单独合并入主分支。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/485083/image-preview)
</Background>


合并完成后，会 toast 提示操作成功，关闭合并操作弹窗页并打开合并完成总结弹窗，可以在此弹窗中了解本次合并实际改动了主分支中的什么资源。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/485084/image-preview)
</Background>


### 在主分支中查看合并详情/撤销合并

在主分支中，点击某个资源的“历史记录”功能，即可看到该资源是被本次合并操作修改内容，并且可以看到修改的详情，还能够与某个其它版本的内容进行对比，从而帮助用户进行内容的回溯与回滚。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/485085/image-preview)
    
    
![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/485086/image-preview)
</Background>



## 合并入受保护分支

当一个拥有项目接口等资源编辑权限的用户，需要将某个迭代分支的调整内容合并入一个已设置为“保护”的分支时，可以创建合并请求，由项目管理员进行审核后实际合入目标分支。

### 创建合并请求

在项目中点击“合并”之后，会与合并入未被保护分支效果一样，看到当前分支所有的改动资源。可以在此处选择需要合并入目标分支的资源，然后点击右下角“创建合并请求”按钮，提交一个合并请求给审核人员进行合并请求审核。


<Background>
<img src="https://api.apifox.com/api/v1/projects/5097254/resources/485087/image-preview" width="540px" />
</Background>



### 审核已提交的合并请求

已经创建了合并请求之后，审核人员可在“项目概览”中，看到明显的提示有人提交了合并请求。进入“项目概览 -> 合并请求”页，即可看到合并请求列表及更多信息。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/485088/image-preview)
</Background>


点击一条待审核的合并请求，即可对合并请求的内容进行审核。可以详细对比合并前后的内容并决定是否接受本次合并请求。如果选择接受，则点击右下角“合并”按钮，当前请求合并中的全部内容将被合并入目标分支。


<Background>
 
![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/485089/image-preview)
</Background>


合并的具体逻辑与合并入一个非保护分支的合并逻辑一致，详情请看[待合并内容详情审核](#待合并内容详情审核)模块。

合并完成后，合并请求的内容会被合入主分支，会有一个目标分支被修改内容的表格总览。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/485090/image-preview)
</Background>


同时合并请求本身的状态会被标记为“已合并”，点击可以查看本次已合并的合并请求详情。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/485091/image-preview)
</Background>


### 已提交待审核的合并请求内容修改

有时在提交合并请求后，审核人员还未进行实际审核，或审核后发现内容可能需要进行一些改动后才可以合入目标分支，这时可能需要对原内容进行一些改动。我们可以直接修改分支中的内容并保存，之前合并请求中的内容会自动同步这些改动，而无需再次重新发起合并请求。修改的内容会在合并请求审核页中有相关提示。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/485092/image-preview)
</Background>


### 拒绝合并请求

审核人员认为此次合并请求不适合合入目标分支时，可以在审核合并请求页面选择“拒绝”合并请求。拒绝后这个合并请求的状态将会被标记为“已关闭”。如果需要修改内容并再次进行合并时，需要重新发起合并请求。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/485094/image-preview)
</Background>


点击一条已关闭的合并请求可以看到详情。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/485095/image-preview)
</Background>


## 自动化测试场景的合并

自动化测试中，测试场景的合并目前仍然与接口管理内容的合并是互相独立的。测试场景的合并需要一个个资源进行合并，没有整体合并的页面。

:::warning[]
1. 请先将接口管理中的资源进行合并，完成后再合并测试场景。否则可能会产生合并后主分支的相关测试场景运行异常。
2. 目前，针对于已设置保护的分支进行测试场景合并，仅能**项目管理员**执行合并操作。后续会增加与接口管理类似的提交合并请求功能，来实现测试场景合入受保护分支。
:::

当你处于某个迭代分支时，在自动化测试中，鼠标 hover 在某个测试场景的“...”按钮上，出现下拉操作“合并到主分支”。


<Background>
 
![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/485096/image-preview)
</Background>


点击后会打开测试场景合并弹窗，会看到有如下信息：
- **基本信息:** 展示要合并的迭代分支测试场景，与主分支上被合并的测试场景（如有关联）。
- **最近运行结果:** 迭代分支上的测试场景最后一次手动运行的结果，鼠标 hover 标识上会展示结果概览信息。测试人员可以通过这个信息来判断是否确认执行合并。如果运行结果是“未测”、“失败”时，建议先返回并确保测试场景运行完全通过后，再执行合并。
- **合并方式:** 有“覆盖”与“新增”两种合并方式。如果测试场景是从主分支复制导入，则会有关联关系，合并时会根据关联关系对主分支资源执行覆盖合并；如果测试场景是新增的，则合并时会在主分支新增此测试场景。
  

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/485097/image-preview)
</Background>




