# Import OpenAPI (Swagger) spec

Apidog supports importing`json` or`yaml` files in`OpenAPI 3.0`,`OpenAPI 3.1` and`Swagger 2.0` data formats.


Apidog supports the import of OpenAPI/Swagger Specification Extensions. Click [this document](https://docs.apidog.com/apidog-openapiswagger-specificaiton-extensions-645605m0.md) to view the API fields supported by Apidog.

During both [Manual import](https://docs.apidog.com/manual-import-633884m0.md) and [Scheduled import](https://docs.apidog.com/scheduled-import-bind-data-sources-633932m0.md), there will be a series of import options, as follows:

<Background>

![CleanShot 2025-11-24 at 11.48.39@2x.png](https://api.apidog.com/api/v1/projects/544525/resources/366351/image-preview)
</Background>

## Import Target Settings

### Target Branch

Select the working branch where you want to import the data (usually defaults to the `main` branch).

### Import Into

You can choose to import new endpoints and data into an existing module within the project, or create a brand new module to store them.

## Endpoint and Case Settings

### Automatically Generate Endpoint Case

If the imported API document does not contain specific test cases, enabling this option allows Apidog to automatically generate a default "Success" case for each endpoint, helping you quickly start testing.

### Import Servers in OpenAPI/Swagger as Environments

If the imported document defines different server addresses, enabling this option will automatically create these addresses as different environments within the project, facilitating easy switching between test targets.

<Background>

![image.png](https://api.apidog.com/api/v1/projects/544525/resources/366352/image-preview)
</Background>


## Security and Auth Handling

**Security Scheme** is a configuration used in API documentation (such as OpenAPI) to describe how an endpoint is authorized.

It tells the client how to carry authentication information when accessing an endpoint, such as a Token, API Key, or OAuth2 authorization.

### Import Security Scheme

When enabled, various security settings defined in the document (such as API Key, Basic Auth, etc.) will be imported into Apidog's Auth configuration.

  - You can choose to set the Auth for the "Root" folder as the global security scheme defined in the OpenAPI spec.

  - For imported endpoints without security defined, you can specify how they should be handled. For example: **Inherit from parent** folder's Auth configuration, or set to **No authentication**.


<Background>

![image.png](https://api.apidog.com/api/v1/projects/544525/resources/366353/image-preview)
</Background>


## Naming Rules and Summary

### When the Endpoint Summary Field is Empty

If an imported endpoint lacks a clear name (`Summary`), Apidog will default to using the endpoint's `operationId` field as the endpoint name. You can also choose to use the path or extract it from the description.


<Background>

![image.png](https://api.apidog.com/api/v1/projects/544525/resources/366354/image-preview)
</Background>


## Resource Conflict Handling

You need to decide how to handle situations where imported data duplicates existing endpoints, schemas, or components in the project.

### Endpoint Conflicts

**While matching the same endpoints (based on Method & Path):**

  * **Overwrite:** The newly imported endpoint will completely replace the old endpoint content.
  * **Keep Both:** Both endpoints will be retained in the project.
  * **Ignore:** The newly imported conflicting endpoint will be ignored.
  * **Merge:** Retains the modified name, Mock rules, parameter descriptions, and response examples of the old endpoint.
  * **Overwrite Selected Fields:** Selected fields will be overwritten, while other unselected fields will retain their existing content.


<Background>

![image.png](https://api.apidog.com/api/v1/projects/544525/resources/366355/image-preview)
</Background>


### Markdown, Schemas, and Components

For conflicts involving Markdown files, Schemas, and Components, similar dropdown options are available, such as choosing "Overwrite" or "Merge".


<Background>

![image.png](https://api.apidog.com/api/v1/projects/544525/resources/366356/image-preview)
</Background>


### Folders Sync

**When the same endpoint is in different folders:**
If an imported endpoint matches an existing one, but their folder information (such as folder name, pre/post-processors) differs between the new and old files, you can choose:

  - **Keep the existing endpoint folder unchanged:** Ignore the folder information in the new file and retain the project's original folder settings.

  - **Update endpoint folder:** Use the folder information from the new file to update the folder the endpoint belongs to in the project.


<Background>

![image.png](https://api.apidog.com/api/v1/projects/544525/resources/366357/image-preview)
</Background>


### Resource Cleanup

Apidog will compare the new imported file with existing resources in the project:

  - **Do not delete:** Old resources in the project that do not exist in the new file will be retained (safe option).

  - **Delete:** Old resources in the project that do not exist in the new file will be removed (sync option, ensuring the project remains fully consistent with the imported source data).


<Background>

![image.png](https://api.apidog.com/api/v1/projects/544525/resources/366358/image-preview)
</Background>


    
## URL Import

When using URL import, please provide the direct URL to the`JSON` or`YAML` data file, not the Base URL of the Swagger UI.



<Background>

![image.png](https://api.apidog.com/api/v1/projects/544525/resources/366378/image-preview)
</Background>

If you are importing using a URL, some URLs may use Basic auth encryption. In this case, you can simply turn on the Basic auth toggle and fill in the username and password.

## Scheduled Import

Open the`Settings` panel, go to`Import Data`, and click on`Scheduled`. You can select multiple data sources here and synchronize them to a specific folders at regular intervals.

:::tip
The`Import Data`option is only visible and accessible to project admins.
:::

<Background>

![automatic-import.png](https://api.apidog.com/api/v1/projects/544525/resources/346453/image-preview)
</Background>
<br>
<Background>
![](https://assets.apidog.com/uploads/help/2023/07/11/f4542f58cfe8339e2a86b3c50fb694a1.png)
</Background>
