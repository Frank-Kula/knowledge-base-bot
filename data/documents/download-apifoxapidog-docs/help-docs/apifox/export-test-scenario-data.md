# 导出场景用例数据


场景用例支持导出 `Apifox CLI`、`Postman`、`Jmeter` 格式数据文件，它们可以在本地环境中或外部持续集成流水线中运行，以便更好地与团队中现有的测试工作流相融合。

## 导出配置文件

点击场景用例右侧的`...`按钮，选择需要导出的格式。

<Background>

![CleanShot 2025-05-07 at 11.02.47@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/520848/image-preview)
</Background>


## 使用配置文件

### Apifox CLI

详细说明请参考[运行持续集成](https://docs.apifox.com/apifox-cli.md)。

### Newman 方式（Postman）

详细说明请参考使用参考教程：[《Web API 持续集成：PostMan+Newman+Jenkins（图文讲解）》](https://cloud.tencent.com/developer/article/1368050)。

### JMeter 方式

导出 JMeter 数据后可用于性能测试，但同样也可以用于持续集成。详细说明请参考教程：[《性能测试与持续集成(JMeter+Jenkins)》](https://cloud.tencent.com/developer/article/1116058)。

:::tip[]

由于 JMeter 不支持 JS 脚本，所以 Apifox 导出 JMeter 数据不包含`前置/后置脚本`。

:::

## 了解更多

:::tip[最佳实践]
[Apifox 中自动化测试的场景用例如何批量导入和导出？](https://apifox.com/blog/how-to-batch-import-and-export-test-scenarios/)
:::


