# 在迭代分支中改动 API


在一个新建的迭代分支中，默认是没有任何内容的。这样是为了让研发者更聚焦于本次迭代实际需要改动的内容。目前有两种方式向一个新的迭代分支中添加资源并进行更改：

- **手动更改：** 可以在 Apifox 中手动导入、新建资源，然后进行更改。此方法适合于研发模式为 API-First 的团队，也是 Apifox 非常推荐的研发模式与实践。
  
- **OAS 导入：** 可以直接将 OAS *（OpenAPI Specification，即 OpenAPI 规范，又称 Swagger 定义）* 导入至某个迭代分支中，导入时会自动比对 OAS 中的内容与主分支接口中的内容，从而生成关联资源 / 新建资源。可以多次导入同一个迭代分支从而实现通过 OAS 导入更改迭代分支接口内容。此方法适合于研发模式为 Code-First 的团队。

可根据你的实际场景与需求进行选择。在某个分支中的操作仅影响当前分支中的数据，与主分支、其它分支互不影响。

## 手动更改

在 Apifox 中手动对迭代分支内容进行更改。我们非常推荐通过手动导入、新建的方式来对迭代分支内的资源进行改动，因为优先确定接口定义、然后再进入研发的 API-First 模式，效率更高、协同成本更低。

### 从主分支导入资源

基于你本次迭代的实际需求，需要对现有接口、数据模型、响应组件进行改动升级时，使用“从主分支导入”功能向当前迭代分支上创建这个要调整的资源副本。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/484988/image-preview)
</Background>


导入某个资源后，为了确保资源目录层级的准确，会自动将该资源的所有父级目录一并导入进当前迭代分支目录树中。从主分支导入的资源，在目录树上可以看到明显的关联标识。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/484989/image-preview)
</Background>

目前接口用例的导入，是默认随着接口一并导入至迭代分支的。同样，如果是导入到迭代分支的接口用例，在目录树上也会有关联标识。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/484991/image-preview)
</Background>


### 导入资源拉取主分支最新更改内容

采用了迭代分支的方式进行研发，接口升级，仍然可能存在插入紧急需求等情况需要立即调整线上接口。此时可能绕过当前正在进行的迭代分支，直接在主分支更新了接口内容，导致主分支内容优先于迭代分支内容的情况。针对这个情况，我们提供了“拉取主分支资源”的功能来帮助解决这些场景下的内容冲突问题。



在迭代分支中通过导入创建的资源（即跟主分支有关联的资源），如果关联主分支内容在迭代分支导入之后发生变更的情况，则在迭代分支中访问这个资源的详情时，会被明显提示主分支内容发生变更。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/484992/image-preview)
</Background>


在提示上点击查看功能即可查看变更的详情，并且根据需要选择哪部分内容拉取主分支内容，或仍然保留迭代分支内容。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/484993/image-preview)
</Background>


在详情中选择完成并点击“确认”后，会根据选择来更改迭代分支中相关资源的内容，从而解决因为主分支内容更新而导致的内容冲突。


### 新建资源

基于你本次迭代的实际需求，需要新增接口、数据模型、响应组件来满足业务需求时，使用“新建”功能向当前迭代分支上创建这个新的资源。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/484994/image-preview)
</Background>


迭代分支上的新建功能，与主分支上的新建功能完全一致，你可以在迭代分支中的任一目录下新建一个资源。当你发现迭代分支中没有你新建资源所需要的父级目录时，你可以使用“导入接口目录”或“新建目录”功能来创建一个正确的父级目录后，再新建需要的资源。

**导入接口目录：** 

<Frame>
![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/484995/image-preview)
</Frame>


**新建目录：** 


<Frame>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/484997/image-preview)
</Frame>


### 顺序移动、目录内容调整

基于你本次迭代的实际需求，需要对资源的顺序，或原有目录/新建目录的内容进行调整，你可以直接在已导入/新建至迭代分支中的资源进行和主分支一样的操作，任意调整接口顺序，或修改父级目录的设置。

通过目录树拖动，调整接口顺序前后：

<Frame>
![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/484998/image-preview)
</Frame>


如果为导入，目录也会展示关联标识：


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/484999/image-preview)
</Background>


目录内容也可以任意调整、修改：


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/485003/image-preview)
</Background>


### 资源删除 / 恢复

在迭代分支中，可以任意操作删除资源，并在“回收站”中看到这些被删除的资源并选择恢复，功能与主分支的回收站一致。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/485004/image-preview)
</Background>


如果反复的对同一主分支资源，在迭代分支中进行导入、删除、恢复，可能会发生操作完成的数据不符合预期的情况，请尽量避免这样操作。

### 接口的 Mock、对比、协同

在迭代分支中的接口，会有属于本迭代分支的接口 Mock 地址，实际 Mock 内容也是完全基于当前迭代分支上的接口定义而来的，用以更好的帮助相关角色模拟本次迭代调整过后的接口响应。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/485005/image-preview)
</Background>


你也可以对某个与主分支有关联关系的迭代分支资源上，进行单个资源的对比，查看这个资源与主分支的具体差异。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/485006/image-preview)
</Background>


对于迭代分支中的接口，同样可以复制协作链接发送给其它伙伴，进行协同。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/485008/image-preview)
</Background>


当点击迭代分支接口协作链接时你正处于其它分支时，系统会提示你是否切换分支查看接口。切换之前记得将当前分支的各种改动内容先保存后再切换查看。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/485010/image-preview)
</Background>



## 将 OAS 导入迭代分支

通过各种导入方式（手动、定时、接口等）将 OAS *（OpenAPI Specfinication，又称 Swagger 定义）* 内容直接导入至迭代分支。

### 指定迭代分支后进行导入

确保左上角是处于导入的目标分支中，然后在 “项目设置 ->导入数据” 页面中，即可向当前分支中导入数据。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/485011/image-preview)
</Background>


如果想要定时往迭代分支中导入数据，则在创建定时导入时，选择导入到目标分支即可。


<Background>
<img style="width:540px;" src="https://api.apifox.com/api/v1/projects/5097254/resources/485013/image-preview" />

</Background>


### OAS 内容与主分支内容的自动对比

在将 OAS 导入至迭代分支时，实际的处理逻辑是：

- 识别 OAS 文件内容
  
- 根据 OAS 内各个**接口**的“Path+Method”与主分支包含的接口进行对比：
  - 成功匹配到“Path+Method”的接口，OAS 内容跟主分支内容完全一致，则**不导入**此接口到迭代分支中；
  - 成功匹配到“Path+Method”的接口，OAS 内容跟主分支内容有区别，则导入一个关联主分支的符合 OAS 内容的接口到迭代分支中；
  - 没有匹配到“Path+Method”的接口，则导入一个新的接口到迭代分支中。
  
- 根据 OAS 内各个**数据模型**的“名称”与主分支包含的数据模型进行对比：
  - 成功匹配到“名称”的数据模型，OAS 内容跟主分支内容完全一致，则**不导入**此数据模型到迭代分支中；
  - 成功匹配到“名称”的数据模型，OAS 内容跟主分支内容有区别，则导入一个关联主分支的符合 OAS 内容的数据模型到迭代分支中；
  - 没有匹配到“名称”的数据模型，则导入一个新的数据模型到迭代分支中。

- 导入并生成数据成功，展示成功在迭代分支通过导入新增、修改的各个资源的总览。

    
<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/485019/image-preview)
</Background>


基于 Apifox 迭代分支“让研发者更聚焦于本次迭代实际需要改动的内容”的理念，所以导入后与主分支对比发现完全没有改动的资源，不会生成在迭代分支里。
