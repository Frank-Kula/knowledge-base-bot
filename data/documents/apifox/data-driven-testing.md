# 数据驱动测试

Apifox 支持数据驱动测试，你可以导入 CSV 或 JSON 格式的测试数据，然后在测试步骤中使用这些数据。

## 开始使用

<Steps>
  <Step>
创建场景用例并添加需要的测试步骤。
  </Step>
  <Step>
准备测试数据。测试数据是一个二维表格，每列代表一个变量，每行包含这些字段的值，用于单次场景用例执行。比如，你可以准备下面这样的 CSV 数据：

| name | category | birthday |
|------|----------|-----------|
| 小白 | 猫 | 4/23/2015 |
| 波比 | 狗 | 8/12/2017 |
| 蓝蓝 | 鸟 | 11/2/2016 |
| 糖糖 | 狗 | 3/15/2014 |
| 花花 | 猫 | 6/21/2018 |
| 小墨 | 兔子 | 10/30/2013 |
| 初雪 | 狗 | 12/25/2019 |
| 胖虎 | 狗 | 1/10/2020 |
      

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/481782/image-preview)
</Background>


  </Step>
  <Step>
切换到 “测试数据” 标签页，点击 “新建” 来添加测试数据。

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/481785/image-preview)
</Background>

  </Step>
  <Step>
导入测试数据，添加名称后保存。

![04-testing-apifox.gif](https://api.apifox.com/api/v1/projects/5097254/resources/481791/image-preview)
  </Step>
  <Step>
在测试步骤中添加测试数据变量。测试数据变量名要和二维表格中的列名一致。

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/481792/image-preview)
</Background>

  </Step>
  <Step>
运行测试时，选择要使用的数据集。
<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/481793/image-preview)
</Background>
  </Step>
  <Step>
点击运行，选择要使用的数据集。

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/481796/image-preview)
</Background>


  </Step>
  <Step>
测试报告会显示每个数据集的运行结果。

![05-testing-apifox.gif](https://api.apifox.com/api/v1/projects/5097254/resources/481799/image-preview)
  </Step>
</Steps>

## 测试数据说明

每个场景用例可以维护多组测试数据，运行场景时可以选择使用哪组数据。

测试数据存储在云端，团队成员之间可以同步。

测试数据可以按环境配置，切换环境时会自动使用对应环境的数据集。

比如，你可以为测试环境和开发环境分别维护一组宠物数据，使用相同的变量名。切换环境时，会自动使用对应环境的变量值。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/481802/image-preview)
</Background>


### 编辑测试数据

你可以用 CSV 或 JSON 格式导入/导出测试数据，也可以手动添加和编辑。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/481804/image-preview)
</Background>


### 使用测试数据

你可以用 `{{变量名}}` 把测试数据变量插入到测试步骤的请求参数、请求头、请求体等位置。运行场景用例时，这些变量会被替换成对应的测试数据值。

变量名可以和其他变量重名。当有重名变量时，优先级顺序是：**局部变量 > 测试数据变量 > 环境变量 > 全局变量**。

### 在脚本中使用测试数据

你可以这样在脚本中访问变量：

`pm.iterationData.has(变量名:String)`：函数 → Boolean：检查测试变量是否存在。
`pm.iterationData.get(变量名:String)`：函数 → *：获取测试变量。
`pm.iterationData.replaceIn(变量名:String)`：函数：用实际值替换字符串中的动态变量。
`pm.iterationData.toObject()`：函数 → Object：把所有局部变量转成对象。

## 常见问题


<Accordion title="导入测试数据时出现乱码怎么办？" defaultOpen>
在 Windows 系统中，Excel 默认用 GBK 编码保存 CSV 文件，在其他软件中查看 CSV 时可能会出现乱码。另外，老版本 Excel（比如 Excel 2016）保存 UTF-8 格式的 CSV 文件时，通常不会保存 BOM（字节序标记），这也会导致乱码。

解决方法：

- Windows 系统：把 CSV 重新保存成 `UTF-8` 编码
- macOS 系统：运行 `iconv -f GBK -t UTF-8 xxx.csv > utf-8.csv` 命令转换编码
</Accordion>


