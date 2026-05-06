# 导出数据

Apifox 支持将 API 导出为多种数据格式，包括 `OpenAPI Specification`、`HTML`、`Markdown`、`Apifox`和 `Postman`。

## 导出数据

进入左侧菜单栏的 “设置 -> 导出数据” 选项，选择你想要的导出数据格式，然后点击 “导出” 按钮。

<Background>

![CleanShot 2025-11-24 at 15.31.46@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/596941/image-preview)
</Background>

你可以选择一次性导出所有 API，也可以选择特定的 API 进行导出。导出时还可以按标签进行分组，针对特定的 API 进行导出。

<Background>

![CleanShot 2025-11-24 at 15.33.16@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/596943/image-preview)
</Background>


对于 `OpenAPI Specification`，我们支持的版本为 `3.1`、`3.0` 和 Swagger `2.0`，可以导出为 `YAML` 或 `JSON` 格式，并且会包含 **[Apifox 扩展的 OpenAPI 字段](https://docs.apifox.com/apifox-openapi-swagger-extension.md)**，导出时可以根据 Tags 字段作为目录进行分组。

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/596951/image-preview)
</Background>

此外，你还可以将数据导出为离线文档。点击 “打开 URL” 即可直接在浏览器中查看原始内容。

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/596956/image-preview)
</Background>


## OperationID

`OperationId` 是用来唯一标识 OpenAPI/Swagger 规范中的某个 API 操作的标识符。在导出 `OpenAPI` 格式时，可以设置 `OperationId` 属性，该标识符将包含在导出的 Operation 对象的 `OperationId` 中。

<Background>

![CleanShot 2024-09-20 at 17.50.17@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/466594/image-preview)
    
![CleanShot 2024-09-20 at 17.50.55@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/466595/image-preview)
</Background>

## 自定义导出 OAS


<Steps>
  <Step>
    点击 “项目概览 -> API 规范 -> 设置/添加”
      
    <Background>

![CleanShot 2025-03-31 at 11.28.00@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/508373/image-preview)
    </Background>

  </Step>
  <Step>
    在打开的页面中，即可添加自定义导出内容。
<Background>

![CleanShot 2025-03-31 at 11.03.33@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/508354/image-preview)
</Background>

  </Step>
</Steps>


## 了解更多


<Card title="导出测试场景数据" href="/5629572m0">
测试场景支持导出 `Apifox CLI`、`Postman`、`Jmeter` 格式数据文件，它们可以在本地环境中或外部持续集成流水线中运行，以便更好地与团队中现有的测试工作流相融合。
</Card>



:::tip[最佳实践]
[Apifox 中自动化测试的测试场景如何批量导入和导出？](https://apifox.com/blog/how-to-batch-import-and-export-test-scenarios/)
:::


## 常见问题


<Accordion title="为什么导出的 API 数量减少了？" defaultOpen>
  当多个 API 使用相同的方法和路径时，可能会发生这种情况。HTML 和 Markdown 是通过 OpenAPI 数据转换导出的，OpenAPI 不支持多个 API 共享相同的方法和路径。
</Accordion>


<Accordion title="为什么导出到 Markdown 和 HTML 时 API 顺序混乱？" defaultOpen={false} >
OpenAPI 中的 Swagger 规范对 API 的排序或分组没有明确支持，因此导出到 Markdown 和 HTML 时可能会出现顺序混乱的情况。要获得有序的导出，建议使用 Apifox 的原生格式。
</Accordion>

<Accordion title="为什么当多个 API 使用相同的 URL 时，导出的 API 数量减少了？" defaultOpen={false} >
OpenAPI 规范不允许多个 API 共享相同的方法和路径，请确保每个 API 使用唯一的 URL。有关确保 API 唯一标识符的更多信息，请参阅[接口唯一标识](https://docs.apifox.com/api-unique-identifier.md)。HTML 和 Markdown 的导出是通过 OpenAPI 进行的，受到相同的限制。
</Accordion>

<Accordion title="如何将文档导出为 PDF/Word？" defaultOpen={false} >
Apifox 目前不支持直接导出为 PDF 或 Word 格式，但你可以先导出为 Markdown 格式，然后使用外部工具进行转换。比如，Typora 可以将 Markdown 转换为 PDF、Word、Epub 等格式。


:::tip[]
具体可参考这篇文章《[如何将 Markdown 转为其它格式](https://apifox.com/blog/how-to-export-interface-documents-to-pdf-word-in-apifox/)》。
:::
</Accordion>

<Accordion title="为什么多个 API 只有一个导出成功？" defaultOpen={false} >
1. 确保没有多个 API 使用相同的方法和路径。
2. OpenAPI 规范禁止不同的 API 共享相同的方法和路径配置。更多信息请参阅[接口唯一标识](https://docs.apifox.com/api-unique-identifier.md)。
3. 通过 OpenAPI 数据转换为 HTML 或 Markdown 时，可能会导致问题。
</Accordion>


<Accordion title="如何导出 Auth 信息？" defaultOpen={false} >
Apifox 会自动将 `Auth` 值导出到 Swagger 格式文件中，无需额外设置。在 Swagger 格式文件中的 `securitySchemes` 部分可以找到这些值。
</Accordion>

