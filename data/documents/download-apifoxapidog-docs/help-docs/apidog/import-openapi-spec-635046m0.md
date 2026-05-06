# Import OpenAPI Spec

Apidog supports importing `JSON` or `YAML` files in **OpenAPI 3.0**, **OpenAPI 3.1**, and **Swagger 2.0** formats. Support also includes standard [Serialization Extensions](https://docs.apidog.com/apidog-openapi-specificaiton-extensions-645605m0.md).

## Configuration & Scheduling

For detailed configuration settings (Conflict Resolution, Folder Sync, etc.) and automation instructions, please refer to the dedicated guides:

- **[Import Options](https://docs.apidog.com/import-options-633930m0.md)**: Comprehensive guide on all available settings during import.
- **[Scheduled Import](https://docs.apidog.com/scheduled-import-bind-data-sources-633932m0.md)**: How to set up automatic synchronization.

## URL Import Tips

When importing via URL, ensure you provide the **direct URL** to the `JSON` or `YAML` data file.
> ❌ **Incorrect**: `https://petstore.swagger.io/` (The Swagger UI Dashboard)
> ✅ **Correct**: `https://petstore.swagger.io/v2/swagger.json` (The Raw Data File)

<details>
<summary>📷 Visual Reference</summary>
<Background>
![image.png](https://api.apidog.com/api/v1/projects/544525/resources/366378/image-preview)
</Background>
</details>

**(Optional) Basic Auth**: If your OAS file URL is protected behind Basic Auth, toggle the switch and enter credentials during import.
