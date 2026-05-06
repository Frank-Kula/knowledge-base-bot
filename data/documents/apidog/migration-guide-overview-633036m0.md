# Migration Guide Overview

Apidog supports importing data from various API specifications and testing tools to facilitate seamless migration.

## Supported Formats

### API Specifications
| Format | Description |
| :--- | :--- |
| **[OpenAPI(Swagger) spec](https://docs.apidog.com/import-openapi-spec-635046m0.md)** | Import OpenAPI 3.0 or Swagger 2.0 specifications commonly used for defining RESTful APIs. |
| **[apiDoc](https://docs.apidog.com/import-from-apidoc-635052m0.md)** | Import API documentation generated from code comments using apiDoc. |
| **RAML** | RESTful API Modeling Language. |
| **WSDL** | Web Services Description Language for SOAP services. |
| **WADL** | Web Application Description Language. |
| **Google Discovery** | Google APIs Discovery Service format. |
| **I/O Doc** | I/O Docs format. |

### API Clients & Data Tools
| Tool / Format | Description |
| :--- | :--- |
| **[Postman](https://docs.apidog.com/import-from-postman-635043m0.md)** | Migrate collections and environments from Postman. |
| **[Insomnia](https://docs.apidog.com/import-from-insomnia-635047m0.md)** | Import data exported from Insomnia REST Client. |
| **[cURL](https://docs.apidog.com/import-curl-635068m0.md)** | Import API requests via raw cURL commands. |
| **[.har file](https://docs.apidog.com/import-har-file-635056m0.md)** | Import HTTP Archive format files captured from browser network tabs or other tools. |
| **JMeter** | Import Apache JMeter script files. |
| **Apidog** | Import project data from other Apidog projects. |

<Background>

![image.png](https://api.apidog.com/api/v1/projects/544525/resources/366292/image-preview)
</Background>

## Import Methods

You can import data either manually or setup automatic updates.

### [Manual Import](https://docs.apidog.com/manual-import-633884m0.md)
Ideal for one-time migrations. Upload your files or paste data directly to bring your API projects into Apidog.

### [Scheduled Import](https://docs.apidog.com/scheduled-import-bind-data-sources-633932m0.md)
Best for keeping Apidog in sync with external sources. If you maintain your API spec (like OpenAPI) in a git repository or separate file URL, use this to automatically pull updates into Apidog for debugging and testing.

## Additional Capabilities

### [Import Markdowns](https://docs.apidog.com/import-markdowns-635070m0.md)
Apidog supports batch importing of Markdown documents for documentation purposes (Note: Markdown is not recognized as an API specification structure).

### [Export Data](https://docs.apidog.com/export-data-635117m0.md)
Need to move data out? Apidog supports exporting your APIs to:
*   `OpenAPI Specification`
*   `HTML`
*   `Markdown`
*   `Apidog` format

