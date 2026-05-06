# 运行场景用例

当你完成场景用例的编排后，可以运行它来生成测试报告。

## 选择合适的运行方式

Apifox 提供了多种场景用例运行方式，满足不同的需求：

1. **本地可视化运行**
   - 从本地机器发起，适用于小规模、快速的测试。
   - 适合同时开发和测试，便于实时查看结果和调整。

2. **本地 Apifox CLI 运行**
   - 适合大规模数据或迭代场景，运行速度较快。
   - 支持离线运行，适用于资源有限或不依赖图形界面的情况。

3. **CI/CD 运行**
   - 在 CI/CD 流水线中运行，适用于自动化集成和持续部署流程。
   - 适合频繁运行测试的环境，确保每次代码变更后都能及时验证 API 的稳定性。

4. **自托管 Runner 执行**
   - 团队可以在自己的服务器上部署 Apifox Runner，使用更强大的计算资源来运行测试。
   - 支持定时任务，适用于定期运行场景用例或负载较大的测试需求。


:::tip[]
场景用例中如果使用到了环境/全局变量，那么在选择不同方式运行时，实际使用的变量值可能会不同，导致运行结果不一致。[了解更多](#不同运行方式间使用不同的环境全局变量值的规则)
:::

接下来，我们将从本地可视化运行开始。


## 开始使用

<Steps>
  <Step>
选择一个场景用例，然后选择运行环境。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/481710/image-preview)
</Background>

  </Step>
  <Step>
点击 “运行”。
  </Step>
  <Step>
你会看到一个测试报告，显示当前运行的通过率、耗时时间和其它数据。你可以点击每个测试步骤来查看校验和断言结果，并查看实际的请求和响应详情。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/481711/image-preview)
</Background>
:::highlight purple 
了解更多关于[测试报告](https://docs.apifox.com/test-reports.md)的信息。
:::
  </Step>

</Steps>


## 场景用例中的运行配置项

在 Apifox 中运行场景用例时，可以配置多个设置和选项来根据特定要求运行测试。


<Background>
<img style="width: 340px" src="https://api.apifox.com/api/v1/projects/5097254/resources/481760/image-preview" />
</Background>




### 通用配置

你可以在场景用例右侧的 tab 页中调整以下设置：

- **运行环境**

  测试步骤中每个接口的运行链接（前置 URL），详情见[环境与服务](https://docs.apifox.com/environments-and-services.md)。

- **测试数据**

  场景用例支持导入外部测试数据集。当场景用例运行时，系统会循环运行数据文件里所有的数据集，并且会将数据集里的数据赋值对应的变量，详情见[数据驱动测试](https://docs.apifox.com/data-driven-testing.md)。

- **循环次数**

  循环次数是指整个场景用例完整执行的轮次。

- **线程数**

  线程数指的是同时并发运行场景用例的线程数，每个线程都会按顺序运行选中的所有步骤。注意这是一个处于 Beta 阶段的功能，可能会出现预期之外的问题。

- **运行于**

  实际消耗硬件资源运行场景用例的机器。所有场景用例中发起的请求，会从这里指定的机器发起，所以有可能因为请求机器的网络环境不同导致产生不同的测试结果。
  
    :::caution[]
    此设置不会保存为场景用例的运行配置中，每次都是默认使用本机运行场景用例。并且这个设置不会在批量运行、CLI 运行时生效，使用以上方式运行时还是消耗当前机器资源发起请求。

    :::
  指定机器发起场景用例运行，如果该场景用例中使用了文件（请求发送文件、数据库连接、外部程序、SSL 证书等），则需要将所有要用到的文件存放在指定机器本地才可正常使用。

- **通知**

  是否在手动运行本场景用例完成之后，发送一个通知信息给指定的对象，信息内会有测试总览结果和详情链接。打开后可以设置是只要完成运行即进行通知还是在仅发生失败时进行通知，用以减少无效通知的打扰。通知对象的详细说明请[参考此处](https://docs.apifox.com/notification-targets.md)。

- **共享**

  点击高级设置右侧的“共享”选项后，每次运行场景用例后的测试报告都将会自动共享给项目内的其它成员。你可以在“测试报告”中的“共享” tab 页中查看所有已在团队内共享的测试报告。有关于测试报告的内容，详细说明请参考[《查看测试报告》](https://docs.apifox.com/test-reports.md)。



如果当前场景用例步骤中存在从其它项目导入的接口，那么你可以参考[管理其它项目接口的运行环境](https://docs.apifox.com/manage-cross-project-environments.md)。

### 高级设置

在高级设置中，你还可以调整：

- **遇到错误时的策略**

  当某个测试步骤执行出错时，例如出现断言错误、数据格式校验错误或服务器错误等情况，系统根据预设的策略进行处理，提供以下 3 种策略：

  - 忽略：跳过当前异常步骤，继续执行后续步骤。
  - 跳到下一轮循环：结束当前循环测试，跳转到下一轮循环测试。
  - 结束运行：停止测试，并标记为失败。

- **间隔停顿**

  前一个测试步骤运行完成后，停顿一段时间，再运行下一个步骤。

- **保存请求 / 响应详情**

  开启后将保存接口的实际请求、请求响应 headers 与 bodies，但数据过多有可能会影响性能，你可以选择保存“全部请求”或“仅失败请求”。

- **保存变量变化值**

  场景用例运行结束后，将测试过程中有变化的环境/全局变量值保存至项目中的环境/全局变量。

- **使用全局 Cookie**

  1. 如果使用全局 Cookie，则在场景用例中，所有接口的请求都将带上全局 Cookie。
  2. 如果不使用全局 Cookie，则在场景用例中，每个接口的请求都将带上自己的 Cookie。

- **保存 Cookie 到全局**

  场景用例运行结束后，将已变化的 Cookie 值保存至当前项目内的全局 Cookie 中。


<Background>
<img style="width: 340px" src="https://api.apifox.com/api/v1/projects/5097254/resources/481761/image-preview" />
</Background>


## 在编排模式中调整运行配置

如果你进入了编排模式，相关的运行配置被收起到 “运行” 按钮的右侧。将鼠标 Hover 在此设置按钮上，即可看到本场景用例的详细运行配置。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/481762/image-preview)
</Background>


## 运行功能测试

运行功能测试后将进入场景用例运行页。下图中的饼状图显示运行结果总览，并且在场景用例的运行过程中实时变化；饼状图下面是具体执行的测试步骤，在运行中将会显示每个测试步骤的执行情况。

功能测试运行结束后，你可以点击相关接口以查看该接口在测试过程中的各项指标和状态，包括接口名称、请求方式、请求地址、响应状态码、响应时间、响应内容、据校验及断言情况等。详细说明请参考[《查看测试报告》](https://docs.apifox.com/test-reports.md)。


<Background>

![CleanShot 2024-12-06 at 10.34.33@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/481766/image-preview)
</Background>

## 不同运行方式间，使用不同的环境/全局变量值的规则

因为环境与全局变量支持持久化，可以长期保存在某个位置，用以跨单次运行或跨不同场景用例使用。所以如果你在某个场景用例中使用到了环境/全局变量，那么在选择不同方式运行时，实际使用的变量值可能会不同。**例如：**

*场景用例中使用了环境变量 Token，在客户端内发起运行已经完全成功，但是同样内容使用自托管 Runner 运行会发生报错，因为环境变量 Token 的值不正确。*


这个例子发生的可能原因是，环境变量 Token 的实际值，在客户端内运行时是使用了客户端内保存的本地值；然而在自托管 Runner 内运行时，Runner 内并没有保存跟客户端一样的 Token 本地值，导致运行失败。

为了解决这个问题，Apifox 提供了一套在不同运行方式间使用不同规则来使用环境/全局变量值的规则：

<table>
  <thead>
    <tr>
      <th>运行方式</th>
      <th>环境/全局变量使用方式</th>
      <th>环境/全局变量保存位置</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>本地发起运行（客户端、Web 端）<span style="color: gray; font-size: 14px;display: inline-block; width: 145px;"></span></td>
      <td>使用环境/全局变量的<a href="https://docs.apifox.com/5537409m0#远程值和本地值">本地值</a>实际运行。<span style="color: gray; font-size: 14px;display: inline-block; width: 260px;"></span></td>
      <td>保存在本地，可以手动修改、通过运行前后置操作修改。可通过 “环境管理 - 环境/全局变量 - 本地值” 可视化查看。<span style="color: gray; font-size: 14px;display: inline-block; width: 260px;"></span></td>
    </tr>
    <tr>
      <td>CLI、CI/CD 运行</td>
      <td>
        选择实时在线运行：
        <ol>
          <li>使用环境/全局变量的<a href="https://docs.apifox.com/doc-5537409#%E8%BF%9C%E7%A8%8B%E5%80%BC%E5%92%8C%E6%9C%AC%E5%9C%B0%E5%80%BC">远程值</a>实际运行 *（默认）*。</li>
          <li>通过使用 `--variables <path>` 选项来指定使用在运行场景用例机器内的文件中保存的环境/全局变量值实际运行。<span>[了解更多](https://docs.apifox.com/5637752m0#运行在线数据)</span></li>
        </ol>
        选择导出数据运行：
        <ol start="3">
          <li>使用导出文件中，包含的环境/全局变量值实际运行。</li>
        </ol>
      </td>
      <td>
        <ol>
          <li>远程值保存在 Apifox 云端，仅能通过在客户端内手动更改。</li>
          <li>保存在选项 `--variables <path>` 中指定 path 文件内的环境/远程变量值。可以手动在文件中修改、通过运行前后置操作修改。</li>
          <li>保存在导出文件内的环境/全局变量值。可以手动修改、通过运行前后置操作修改。</li>
        </ol>
      </td>
    </tr>
    <tr>
      <td>自托管 Runner 运行</td>
      <td>
        <ol>
          <li>使用环境/全局变量的<a href="https://docs.apifox.com/doc-5537409#%E8%BF%9C%E7%A8%8B%E5%80%BC%E5%92%8C%E6%9C%AC%E5%9C%B0%E5%80%BC">远程值</a>实际运行 *（默认）*。</li>
          <li>使用保存在 Runner 中的本地值实际运行。<span>[了解更多](https://docs.apifox.com/5635614m0#定时任务详情)</span></li>
        </ol>
      </td>
      <td>
        <ol>
          <li>远程值保存在 Apifox 云端，仅能通过在客户端内手动更改。</li>
          <li>保存在指定的 Runner 内的变量范围中，可以手动修改、通过运行前后置操作修改。可通过产品界面上的引导可视化查看，也可在 Runner 容器 `/opt/runner/variables` 下的文件内查看。</li>
        </ol>
      </td>
    </tr>
  </tbody>
</table>

:::tip[] 
如果需要在 Apifox 客户端中可视化查看、修改 Runner 中保存的环境/全局变量本地值，则需要配置相关 Runner 的 [Serverhost](https://docs.apifox.com/5714000m0#%E6%9C%8D%E5%8A%A1%E5%99%A8-host-%E9%85%8D%E7%BD%AE) 才能够实现。因为此查看与修改操作是直接由客户端发起，通过 Serverhost 直连到 Runner 的。
:::



## 运行包含其它项目接口的场景用例

运行场景用例时，如果场景用例中包含了从其它项目中导入的接口，那么这些接口的运行环境中的请求地址将会从 “环境关联” 中的预设前置 URL 中获取。

例如当场景用例指定了使用 **“正式环境”** ，当测试步骤运行到从 **“医疗问答信息系统”** 项目内导入的接口时，将会按照环境关联页中所指定正式环境：`http://www.nhc.gov.cn` 发起请求，其它接口则按照 “正式环境” 内预设的地址发起请求。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/481764/image-preview)
</Background>



