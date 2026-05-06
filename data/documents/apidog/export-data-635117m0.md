# Export Data

Apidog supports exporting APIs into various standard formats including `OpenAPI Specification`, `HTML`, `Markdown`, `Apidog`, and `Postman` to suit different integration and documentation needs.

## How to Export

<Steps>
  <Step>
    **Navigate to Export Settings**
    
    Go to `Settings` -> `Export Data` in the left sidebar.
    
    <details>
    <summary>📷 Visual Reference</summary>

    <Background>
     
    ![CleanShot 2025-11-24 at 15.57.14@2x.png](https://api.apidog.com/api/v1/projects/544525/resources/366364/image-preview)
    </Background>
    </details>
  </Step>

  <Step>
    **Select Data Scope**
    
    Choose to export **All APIs** or select specific **Endpoints/Tags**.
  </Step>

  <Step>
    **Choose Format & Configure**
    
    Select your desired format (e.g., OpenAPI 3.0) and adjust any format-specific settings.
  </Step>
</Steps>

## Supported Formats

| Format | Versions / Notes |
| :--- | :--- |
| **OpenAPI / Swagger** | Supports `3.1`, `3.0`, and `2.0`. Export as `JSON` or `YAML`. Includes support for Apidog Extension fields. |
| **HTML / Markdown** | Generates static documentation. Best for offline sharing. |
| **Apidog** | Native format containing all project data. |
| **Postman** | Exports collections compatible with Postman. |

:::tip[]
For **Offline Documentation**, you can click "Open URL" to view the raw data directly in your browser.
:::

## Advanced Export Options

### 1. Exporting from Sprint Branches
To export data from a specific Sprint Branch:
1.  Switch to the desired branch using the branch selector in the top-left corner.
2.  Go to Export Data. Apidog will export **all data** from the current branch.

> **Note**: This process merges the sprint branch with the main branch in memory to ensure data integrity (resolving references). You cannot select a subset of endpoints when exporting from a sprint branch.

<details>
<summary>📷 Visual Reference</summary>

<Background>

![export-data-from-a-sprint-branch.png](https://api.apidog.com/api/v1/projects/544525/resources/348705/image-preview)
</Background>
</details>

### 2. Custom OpenAPI Configuration
- For advanced OpenAPI exports, you can configure inclusion rules via **Module Name > Overview > Export/Backup API Specification > Add**.
- You can choose to include the `OperationId` field in the export, which is useful for generating code clients. Learn mode about [OperationId](https://docs.apidog.com/endpoint-unique-identification-539790m0.md). 


## FAQ

**Q: Why are some APIs missing from my export?**
A: This usually happens if multiple APIs share the exact same **Method and Path**. The OpenAPI specification requires unique Method+Path combinations. Apidog enforces this rule during export (especially for HTML/Markdown/OpenAPI formats). Unique your endpoints to resolve this. [Learn more about Endpoint Identification](https://docs.apidog.com/endpoint-unique-identification-539790m0.md).

**Q: Why is the API order different in Markdown/HTML exports?**
A: The underlying Swagger/OpenAPI specification usually does not enforce strict ordering. Markdown and HTML exports are generated based on this spec data, which may result in a different sort order than what you see in the Apidog client.

**Q: Can I export to PDF or Word?**
A: Direct export is not supported. We recommend exporting to **Markdown** first, then using a tool like **Typora** or **Pandoc** to convert the Markdown file into PDF, Word, or other formats.

**Q: Are Authentication values exported?**
A: Yes. Apidog exports `Auth` configurations into the `securitySchemes` section of the OpenAPI/Swagger file automatically. No manual step is required.

<Background>
    <img src="https://assets.apidog.com/uploads/help/2023/11/01/4c673dd9c1e15295493fdb17e9986c44.png" style="width: 640px" />
</Background>
