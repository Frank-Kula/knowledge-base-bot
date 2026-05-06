# Scheduled Import (Bind Data Sources)

**Scheduled Import** automatically synchronizes your API specifications from external sources into Apidog at regular intervals. This feature is ideal for teams that maintain their API specs in external systems (like Git repositories or Swagger endpoints) but want to leverage Apidog's powerful debugging and testing capabilities without manual re-imports.

With Scheduled Import, you can:
- **Maintain a single source of truth** for your API specs in your preferred version control system
- **Automatically sync changes** at customizable intervals (every 30 minutes, hourly, daily, etc.)
- **Import from multiple sources** including GitHub, GitLab, Azure DevOps, and direct URLs
- **Keep your team aligned** with the latest API changes without manual intervention 

## How to Configure

<Steps>
  <Step>
    **Navigate to Settings**
    
    Go to `Settings` -> `Import Data` -> `Scheduled Import (Bind Data Sources)`.
  </Step>
  
  <Step>
    **Create Data Source**
    
    Click "**New**" to add a configuration.
  </Step>

  <Step>
    **Configure Settings**
    
    Fill in the data source details (URL, Frequency, etc.). Go to the next section for details on binding a git repository. 
      </Step>
  
  <Step>
    **Save and Activate**
    
    Click **Save**. The import will now run automatically based on your frequency settings.
  </Step>
</Steps>

:::tip[]
Apidog supports creating multiple data sources within a single project, each synchronizing and importing into different folders.
:::

## Binding Git Repository

Apidog supports binding git repositories from: 
- Github
- GitLab and
- Azure DevOps

To bind a git repository follow these steps. 
<Steps> 
<Step> 
    Select the **Git Repository** option on the **Bind Data Sources** dialog box and create a repository connection.
    <Background>
![image.png](https://api.apidog.com/api/v1/projects/544525/resources/371140/image-preview)
</Background>
</Step>
    
<Step> 
    After selecting your preferred version control platform, follow the instructions to give Apidog access to your repositories. 
</Step>
<Step> 
    When you're redirected back to Apidog, select your **Organization** and **Repository**, then click **Save**. 
<Background>
![image.png](https://api.apidog.com/api/v1/projects/544525/resources/371141/image-preview)
</Background>
</Step>
<Step>
    Finally, select the **Branch** and the **OpenAPI Spec** file and complete the binding process.
</Step>
</Steps>


## Configuration Reference

| Setting | Description |
| :--- | :--- |
| **Import frequency** | How often Apidog checks for and imports updates from your data source. Options include every 30 minutes, hourly, daily, or custom intervals. |
| **Source format** | The specification format of your API file. Supported formats: `OpenAPI` (Swagger), `ApiDoc`, or `Apidog` native format. |
| **Source URL** | The direct HTTP(S) link to your API specification file. Example: `https://petstore.swagger.io/v2/swagger.json`. Must be publicly accessible or protected with Basic Auth. |
| **Runs on** | The execution environment for the import task. Choose `Local Client` (runs when your app is open) or `Runner` (runs on a self-hosted server 24/7). |
| **Basic auth** | Username and password credentials if your Source URL is protected by HTTP Basic Authentication. Leave empty for public URLs. |

:::highlight purple
For more import options, refer to [Import options](https://docs.apidog.com/import-options-633930m0.md).
:::

## Execution Modes

Scheduled imports require an execution environment to run the fetch command. Choose the mode that best fits your workflow:

### 1. Local Client (Default)
The import runs **only when your Apidog desktop app is open**. 
- **Requirement**: You must have the project open with write permissions.
- **Limitation**: If you close the app or the project, updates will pause until you open it again.
- **Network**: Can access internal network URLs if your computer can access them.

:::info[]
Opening the project in the **Apidog Web App** also triggers the scheduled import. However, due to browser security restrictions, the Web App may not be able to access internal network URLs.
:::

### 2. Self-hosted Runner
The import runs on a server where you have deployed an Apidog Runner.
- **Benefit**: Runs 24/7 regardless of whether you are online.
- **Use Case**: Best for teams needing consistent updates without manual intervention.


:::info[]
Learn more about deploying a [Self-hosted Runner](https://docs.apidog.com/general-runner-755233m0.md).
:::

## Advanced: Import to Sprint Branches

You can target specific sprint branches for your import. By default, data imports to the **Main Branch**.

For detailed workflow, refer to [Importing data into sprint branches](https://docs.apidog.com/designing-apis-in-a-branch-616423m0.md#import-oas-into-sprint-branch).
