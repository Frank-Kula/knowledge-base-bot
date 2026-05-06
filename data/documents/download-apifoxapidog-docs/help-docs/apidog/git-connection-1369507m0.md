# Git Connection

:::info
Please ensure that your Apidog version is `≥2.7.29`.
:::

Apidog supports automatically backing up the **OpenAPI / Swagger files** for each module in a project to a Git repository. GitHub, GitLab, and Azure DevOps are currently supported. Backups are performed **during off-peak hours at night** (the exact time is not fixed and is randomly scheduled during idle periods).

## Creating a Git Repository Connection

1. Navigate to **Settings** → **Git Connections**

<details>
<summary>📷 Visual Reference</summary>

<Background>
![CleanShot 2025-08-14 at 12.28.01@2x.png](https://api.apidog.com/api/v1/projects/544525/resources/371718/image-preview)
</Background>
    
</details>

2. Click **New**, then log in to the corresponding source code management platform after being redirected.

3. Fill in the configuration details according to your selected platform.

<details>
<summary>📷 Visual Reference</summary>

<Background>
![image.png](https://api.apidog.com/api/v1/projects/544525/resources/371717/image-preview)
</Background>

</details>

4. Save the repository connection configuration.

## Enabling Automatic Backup

1. In the module you want to back up, go to **Overview** → **API Specification** and add an OAS.

<details>
<summary>📷 Visual Reference</summary>

<Background>
![CleanShot 2025-12-23 at 17.36.02@2x.png](https://api.apidog.com/api/v1/projects/544525/resources/371719/image-preview)
</Background>

</details>

2. Enable **Backup to Git Repository**.

3. Configure the following settings:
   - **Git Repository Connection** (select a previously created connection)
   - **Git Branch**
   - **Target File Path** (the location where the OpenAPI Spec file will be stored in the repository)

<details>
<summary>📷 Visual Reference</summary>

<Background>
![CleanShot 2025-08-14 at 12.34.34@2x.png](https://api.apidog.com/api/v1/projects/544525/resources/371720/image-preview)
</Background>

</details>

Once saved, the system will automatically push the **OpenAPI Spec file** for that module to the specified Git repository during a random off-peak time at night.

<details>
<summary>📷 Visual Reference</summary>

<Background>
![CleanShot 2025-08-14 at 12.37.00@2x.png](https://api.apidog.com/api/v1/projects/544525/resources/360011/image-preview)
</Background>

</details>

## Import OpenAPI/Swagger Files

You can import OpenAPI/Swagger files from remote repositories on a regular basis. In **Settings → Bind Data Sources**, select **Git Repository** as the data source and bind your remote repository. For detailed explanation, check the **[Scheduled Import](https://docs.apidog.com/scheduled-import-bind-data-sources-633932m0.md)** page.

