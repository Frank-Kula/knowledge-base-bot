# 在迭代分支中测试 API



在一个新建好的迭代分支中，自动化测试功能中也默认没有内容的。如果需要对迭代分支的内容进行测试与验证，需要在当前迭代分支中通过导入或新建的方式加入测试场景进行测试。我们建议优先在接口管理中将需要变动的接口资源调整完毕后，再进入自动化测试功能中开始整理测试场景（这也是符合大部分实际研发流程的）。

## 从主分支导入测试场景

支持从主分支导入测试场景。如果主分支中的接口已经导入到迭代分支，并且这些接口已经被包含在主分支的某些测试场景中，系统在导入时会自动选中这些相关场景，方便测试人员筛选导入。这样，测试人员只需在原有测试场景的基础上进行修改，就能快速完成当前迭代的自动化测试场景编写。当然，你也可以手动选择导入主分支上的其他测试场景。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/485024/image-preview)
</Background>


导入的测试场景，为了确保资源目录层级的准确，会自动将该资源的所有父级目录一并导入进当前迭代分支目录树中。从主分支导入的资源，在目录树上可以看到明显的关联标识，这点与接口管理中的资源是一样的。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/485026/image-preview)
</Background>


## 新建测试场景

基于你本次迭代的实际需求，特别是增加了新的接口时，可能需要建立一个新的测试场景来测试新产生的接口。使用“新建”功能向当前迭代分支上创建这个新的测试场景。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/485027/image-preview)
</Background>


## 编排迭代分支测试场景

在迭代分支的某个已经导入/新建的测试场景中，可以进行与主分支测试场景一样的步骤编排。因为构成一个测试场景的请求步骤，大概率要同时涉及当前迭代分支未改动的、被改动的接口，因此，在迭代分支的测试场景内编排时，界面上会通过 UI 明显区别这个测试步骤使用的是当前迭代分支内的资源，还是主分支的资源。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/485028/image-preview)
</Background>


一般情况下，在一个测试场景中只需要重点关注当前迭代分支资源影响改动的步骤，点击进入步骤后基于改动后的接口文档填写新的请求参数，即可快速编排好完整的测试场景，进行针对迭代分支内容的测试。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/485029/image-preview)
</Background>


跟接口关联、跟接口用例保持引用关系、引用测试场景，这三个类型的测试步骤，都会标记是关联使用的主分支还是当前迭代分支的资源。点击查看这些步骤的详情时也能够看出他们关联的资源处于哪个分支上。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/485030/image-preview)
</Background>


## 运行测试场景

迭代分支上的测试场景新建并编排完成后，即可点击运行来运行测试场景，开始测试。测试场景运行的规则也与前端展示的规则一致，如果步骤显示的是关联迭代分支中的资源，则会使用迭代分支的数据（例如使用迭代分支中接口新改动的响应数据结构来做响应校验）；如果步骤显示的是关联主分支中的资源，则会使用主分支的数据。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/485031/image-preview)
</Background>


