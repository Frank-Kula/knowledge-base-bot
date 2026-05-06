# 定时任务

你可以通过设置 “定时任务”，定时自动执行已配置好的自动化场景用例，获取任务运行结果，完成定时测试、回归的需求。

:::caution[]
- 定时任务目前处于 Beta 阶段。
- 要运行定时任务，首先需要配置一个[自托管 Runner](https://docs.apifox.com/universal-runner.md)。
- 使用自托管 Runner 运行定时任务，会根据你的团队付费版本有用量限制。[了解更多](https://apifox.com/pricing/)
:::

## 定时任务入口

你可以在自动化测试功能的目录树中，找到定时任务分类。项目中的所有定时任务会以结构树形式展示在此。


<Background>

![CleanShot 2025-01-23 at 13.56.41@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/492362/image-preview)
</Background>

可以在目录树中，添加定时任务或定时任务的目录；以及对某个定时任务/目录做更多的操作。


<Background>
    
![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/492374/image-preview)
    
![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/492375/image-preview)

</Background>

点击定时任务分类，可以在右侧看到以列表形式展示的全部定时任务，及一些基本信息和操作，可以更方便管理。

<Background>

    
![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/492406/image-preview)
</Background>


## 定时任务详情

在目录树上点击一个已有的定时任务，或者新建一个定时任务，则会在右边打开定时任务的详情 tab。


<Background>

![CleanShot 2025-01-23 at 14.00.49@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/492366/image-preview)
</Background>

可以在定时任务详情中进行如下设置：

- **任务名称、说明：** 用来区别定时任务以及说明该定时任务的详细目的。
- **启/停用：** 开启、停止这个定时任务是否按期执行的开关。
- **场景用例：** 定时任务会执行此处选择的一个/多个场景用例，每个场景用例都可以点击展开独立配置其 “运行配置”。
  - 运行环境、测试数据、循环次数、间隔停顿、保存请求/响应内容等都为标准运行配置，需要了解更多[可见此处](https://docs.apifox.com/doc-5632037#场景用例中的运行配置项)。
  - 环境/全局变量值，指定本场景用例中的环境/全局变量，使用何种实际值。有两种选择，详细介绍可以[查看此处](https://docs.apifox.com/5632037m0#不同运行方式间使用不同的环境全局变量值的规则)。当选择使用 Runner 中保存的变量值时，会要求进一步选择需要使用的变量范围。有这个范围的目的是帮助用户更好的根据实际需求分隔变量，避免因为某次定时任务运行，而导致其它的任务因为变量被更改而运行失败。选择完成范围后还可通过产品界面中出现的入口来可视化查看此范围内的变量值。

<table>
  <thead>
    <tr>
      <th>Runner 中的变量范围</th>
      <th>读写环境/全局变量方式</th>
      <th>描述</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>当前场景用例<span style="color: gray; font-size: 14px;display: inline-block; width: 155px;"></span></td>
      <td>
        <ul>
          <li>当前指定运行 Runner 中，此场景用例对应一个文件，在文件中持久化保存此场景用例内设置的环境/全局变量。</li>
          <li>仅当前场景用例可以读取、写入这个文件中的变量。</li> <span style="color: gray; font-size: 14px;display: inline-block; width: 250px;"></span> 
        </ul>
          
      </td>
      <td>
          最小的变量范围，影响面最小。适用于此场景用例上一次运行的结果，要继续提供给下一次此场景用例运行使用的情况。
          
          场景、任务、任务目录的变量文件均保存在 Runner 容器路径 `/opt/runner/variables` 中。<span style="color: gray; font-size: 14px;display: inline-block; width: 250px;"></span>
        </td>
    </tr>
    <tr>
      <td>当前定时任务</td>
      <td>
        <ul>
          <li>当前指定运行 Runner 中，此场景用例所属的定时任务对应一个文件，在文件中持久化保存此定时任务内所有场景用例设置的环境/全局变量。</li>
          <li>当前定时任务中，所有的场景用例可以读取、写入这个文件中的变量。</li>
        </ul>
      </td>
      <td>
          比较推荐使用的变量范围，中等的变量范围，影响面中等。适用于此定时任务中，不同场景用例之间需要传递数据的情况。
        </td>
    </tr>
    <tr>
      <td>当前定时任务目录</td>
      <td>
        <ul>
          <li>当前指定运行 Runner 中，此场景用例所属的定时任务目录对应一个文件，在文件中持久化保存此定时任务目录内所有定时任务中场景用例设置的环境/全局变量。</li>
          <li>当前定时任务目录中，所有的定时任务里的所有场景用例可以读取、写入这个文件中的变量。</li>
        </ul>
      </td>
      <td>
          最大的变量范围，影响面最大，可能因为运行了某个定时任务修改了变量值，而导致其他定时任务运行失败。适用于一组定时任务之间需要传递数据的情况。
        </td>
    </tr>
  </tbody>
</table>


:::tip[] 
场景用例详情中的 “保存变量变化值” 配置需被勾选，才能在定时任务运行过程中，将通过前后置操作设置的环境变量或全局变量保存到指定 Runner 的变量范围内。
:::


- **使用相同运行设置：** 让下方的全部场景用例使用同样的运行配置。
- **运行周期：** 设置该定时任务以什么样的定时周期来进行执行，例如每周日晚上 11 点，或每间隔 6 小时执行一次。
- **运行于：** 具体执行此定时任务的实例。可以通过 Apifox 云端（即将开放）、团队自托管 Runner 来执行定时任务。如果团队部署了多台通用 Runner，可以选择其中一台。
- **通知：** 开启通知即可在此定时任务运行完成后，发送一个通知信息给指定的对象，信息内会有测试总览结果和详情链接。打开后可以设置是只要完成运行即进行通知还是在仅发生失败时进行通知，用以减少无效通知的打扰。通知对象的详细说明请[参考此处](https://docs.apifox.com/notification-targets.md)。

## 定时任务运行

定时任务运行完成后，会将运行结果从 Runner 上传至服务端中，可以在客户端的 “定时任务 - 运行历史” 中查看选择定时任务的所有运行结果详情。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/492373/image-preview)
</Background>


:::tip[]
建议定时任务开启通知，这样即可在运行完成后第一时间收到通知消息，从而及时查看任务运行结果。
:::

