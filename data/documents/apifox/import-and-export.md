# 导入导出数据

Apifox 支持导入以下 API 数据格式文件，方便进行数据迁移：

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/486841/image-preview)
</Background>

- **[OpenAPI/Swagger](https://docs.apifox.com/import-openapi-swagger.md)**
- **[Postman](https://docs.apifox.com/import-postman.md)**
- **[cURL](https://docs.apifox.com/import-curl.md)**
- **[Apipost](https://docs.apifox.com/import-apipost.md)**
- **[Eolink](https://docs.apifox.com/import-eolink.md)**
- **[.har 文件](https://docs.apifox.com/import-har.md)**
- **[Insomnia](https://docs.apifox.com/import-insomnia.md)**
- **[Java 项目代码](https://docs.apifox.com/apifox-idea-plugin.md)**
- **[knife4j](https://docs.apifox.com/import-knife4j.md)**
- **[apiDoc](https://docs.apifox.com/import-apidoc.md)**
- **[WSDL ](https://docs.apifox.com/import-wsdl.md)**
- **[NEI](https://docs.apifox.com/import-nei.md)**
- **[Apizza](https://docs.apifox.com/import-apizza.md)**
- **[小幺鸡（docway）](https://docs.apifox.com/import-docway.md)**
- **[Markdown](https://docs.apifox.com/import-markdown.md)**
- **YApi**
- **JMeter**
- **RAML**
- **I/O Doc**
- **WADL**
- **Google Discovery**
- **RAP2**
- **DOClever**
- **SosoApi**
- **ShowDoc**
- **EasyDoc**
- **.proto 文件**
- **Apifox**

你可以手动导入数据，或者通过定时导入来完成。

## 手动导入
如果你之前使用的是其他工具，现在想迁移到 Apifox，可以使用[手动导入](https://docs.apifox.com/manual-import.md)功能。

## 定时导入

如果你的 API 定义 *（<Tooltip tip="也称 OpenAPI/Swagger 规范，在 Apifox 中表示接口文档。">API specification</Tooltip>）* 文件维护在 Apifox 之外，但又希望使用 Apifox 进行 API 调试、测试和文档管理，可以使用[定时导入](https://docs.apifox.com/scheduled-import.md)功能。

## 导入 Markdown

Apifox 支持批量导入 Markdown 文档，但不支持将 Markdown 识别为 API 定义 *（<Tooltip tip="也称 OpenAPI/Swagger 规范，在 Apifox 中表示接口文档。">API specification</Tooltip>）* 。了解更多关于[导入 Markdown](https://docs.apifox.com/import-markdown.md) 的信息。

## 导出数据

Apifox 支持将 API 导出为 <Tooltip tip="也称 OpenAPI/Swagger 规范">OpenAPI Specification</Tooltip>、`HTML`、`Markdown` 和 `Apifox` 等格式。了解更多关于[导出数据](https://docs.apifox.com/export-data.md)的信息。
