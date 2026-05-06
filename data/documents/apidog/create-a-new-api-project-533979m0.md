# Create a New API Project

In Apidog, each project corresponds to an API Specification or an OpenAPI Specification (OAS) file. You can create a new API project or import an existing one from the **Home** > **My Teams** > **Projects** section of the Apidog app.

## Creating a Project

<Steps>
  <Step>
  In the **main window**, click the **+ New Project** button at the top right.
  </Step>
  <Step>
  Select the project category at the top: **General** or **gRPC**. 

<Background>
<img src="https://api.apidog.com/api/v1/projects/544525/resources/374621/image-preview" style="width:640px" />
    
</Background>

  - **General**: Choose this for most APIs. It supports HTTP(s), WebSocket, Socket.IO, Webhook, Markdown, and more.
  - **gRPC**: Select this for APIs that use the gRPC protocol. Learn more about [gRPC projects](https://docs.apidog.com/grpc-629868m0.md).
  </Step>
  <Step>
    *(If you selected General)* Choose your preferred project mode. Apidog offers two distinct workflows: **General Mode** and **Spec-first Mode**. Follow the instructions below based on your selection.
  </Step>
</Steps>

### General Mode
Best for GUI-based workflows. It includes a Visual API Editor for API design, debugging, testing, and auto-generated docs. You can also back up auto-generated OpenAPI Specs to a Git repository.

<Steps>
  <Step>
    Select **General Mode**.
  </Step>
  <Step>
    Enter a name for your project.
  </Step>
  <Step>
    **(Optional)** Check the **Including Examples** option to create a project with sample data from the PetStore example.
  </Step>
  <Step>
    **(For teams with multiple users)** Set permissions for other team members during project creation. For more information, see [Member permissions settings](https://docs.apidog.com/member-roles-permission-settings-616186m0.md).
  </Step>
  <Step>
    **(Optional)** Set the **Project language**. For more information, see [Language settings](https://docs.apidog.com/language-settings-640826m0.md).
  </Step>
</Steps>

### Spec-first Mode (Beta)
Ideal for a native Git workflow. Design API specs using an OpenAPI Spec Editor (YAML/JSON files) and keep them in seamless two-way sync with your Git repository.

<Steps>
  <Step>
    Select **Spec-first Mode**.
  </Step>
  <Step>
    Scroll down to the **Connect with Git Repository** section.
  </Step>
  <Step>
    Click either **Connect to GitHub** or **Connect to GitLab SaaS** to link your repository and configure your sync settings.
  </Step>
  <Step>
    **(For teams with multiple users)** Set permissions for other team members. For more information, see [Member permissions settings](https://docs.apidog.com/member-roles-permission-settings-616186m0.md).
  </Step>
</Steps>
:::tip[Learn More]
For a deep dive into the code-driven Specs workspace, real-time directory parsing, and Git commit workflows, check out our detailed guide on [Spec-first Mode](https://docs.apidog.com/spec-first-mode-beta-2058268m0.md).
:::


## Import Existing APIs

If you already have an API Specification, you can initiate the import process either from the **Team** > **Projects** section by selecting **Import Project**, or directly within an existing project by clicking the large **➕** sign and choosing **Import**. This is ideal for migrating existing API data into Apidog.

<Steps>
  <Step>
    Click **"Import Project"**.
  </Step>
  <Step>
    Choose the type of data you wish to import. 

<Background>
![Import data type selection](https://api.apidog.com/api/v1/projects/544525/resources/358111/image-preview)
</Background>
  </Step>
 <Step>
    Upload the file or paste the data URL (OpenAPI/Swagger formats only).
  </Step>   
  <Step>
    Apidog will automatically recognize and parse the content based on the selected format. You'll be able to preview the data before importing. Choose what you want to import and configure the import logic. Then confirm to create and import the project.

<Background>
![Import preview and configuration](https://api.apidog.com/api/v1/projects/544525/resources/358115/image-preview)
</Background>
  </Step>  
 <Step>
    Once the import is complete, your new project will be ready to use.
  </Step>  
</Steps>

:::tip[Learn More]
For detailed information about the import process, see the [Import Guidelines](https://docs.apidog.com/manual-import-633884m0.md).
:::
