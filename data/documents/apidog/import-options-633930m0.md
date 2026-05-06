# Import Options

During both [Manual import](https://docs.apidog.com/manual-import-633884m0.md) and [Scheduled import](https://docs.apidog.com/scheduled-import-bind-data-sources-633932m0.md), you can customize how data is processed using the **Import Options**.

<Background>

![CleanShot 2025-11-24 at 11.48.39@2x.png](https://api.apidog.com/api/v1/projects/544525/resources/366351/image-preview)
</Background>

## General Settings

### Target & Destination

| Option | Description |
| :--- | :--- |
| **Basic Auth** | Used for URL imports requiring username/password authentication. |
| **Target Branch** | Select the specific branch to import data into (defaults to `main`). |
| **Import Into** | Choose to import into an existing folder/module or create a new one. |
| **Auto Generate Case** | If enabled, Apidog automatically creates a "Success" test case if the spec lacks examples. |

### Environment Importing
If your OpenAPI/Swagger file defines multiple servers, enable **Import Servers as Environments** to automatically create matching environments in Apidog.

<details>
<summary>📷 Visual Reference</summary>
<Background>
![image.png](https://api.apidog.com/api/v1/projects/544525/resources/366352/image-preview)
</Background>
</details>

## Security & Naming

### Security Schemes
Control how `securitySchemes` from OpenAPI are handled.

- **Global Auth**: Map the spec's global security to the Root folder's auth in Apidog.
- **Undefined Auth**: Decide behavior for endpoints with no specific security (e.g., "Inherit from parent" or "No auth").

<details>
<summary>📷 Visual Reference</summary>
<Background>
![image.png](https://api.apidog.com/api/v1/projects/544525/resources/366353/image-preview)
</Background>
</details>

### Endpoint Naming
If an endpoint lacks a descriptive `Summary` field, you can choose a fallback sources for the name:
- `operationId` (Default)
- `URL Path`
- `Description` extraction

<details>
<summary>📷 Visual Reference</summary>
<Background>
![image.png](https://api.apidog.com/api/v1/projects/544525/resources/366354/image-preview)
</Background>
</details>

## Conflict Resolution

When imported data matches existing data (based on Method & Path), use these rules to decide the outcome.

### Endpoint Conflicts

| Strategy | Behavior |
| :--- | :--- |
| **Overwrite** | Completely replaces the old endpoint with the new data. |
| **Keep Both** | Creates a duplicate; both old and new exist side-by-side. |
| **Ignore** | Skips the new endpoint; keeps the old one unchanged. |
| **Merge** | Smart update: retains manual changes like Name, Mock rules, and Descriptions while updating the definition. |
| **Overwrite Selected** | Only updates specific fields you select, preserving others. |

<details>
<summary>📷 Visual Reference</summary>
<Background>
![image.png](https://api.apidog.com/api/v1/projects/544525/resources/366355/image-preview)
</Background>
</details>

### Other Resources (Schemas / Docs)
For Markdown docs, Schemas, and Components, similar **Overwrite** vs **Merge** options apply.

<details>
<summary>📷 Visual Reference</summary>
<Background>
![image.png](https://api.apidog.com/api/v1/projects/544525/resources/366356/image-preview)
</Background>
</details>

## Advanced Sync Logic

### Folder Synchronization
When an imported endpoint matches an existing endpoint in the project, but their folder locations differ:
- **Keep existing folder**: Ignores the folder path in the imported file. The endpoint remains in its current folder in Apidog.
- **Update endpoint folder**: Moves the endpoint to the folder structure defined in the imported file.

<details>
<summary>📷 Visual Reference</summary>
<Background>
![image.png](https://api.apidog.com/api/v1/projects/544525/resources/366357/image-preview)
</Background>
</details>
    
### Resource Cleanup
Decide what happens to resources that existed in the project but are **missing** from the new import file.

- **Do not delete** (Safe): Keeps orphaned resources in your project.
- **Delete** (Sync): Removes any resource not present in the new file. **Use with caution** to maintain an exact mirror of the spec.

<details>
<summary>📷 Visual Reference</summary>
<Background>
![image.png](https://api.apidog.com/api/v1/projects/544525/resources/366358/image-preview)
</Background>
</details>

