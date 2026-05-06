# Spec-first Mode (Beta)


Apidog's **Spec-first Mode** is designed for teams that prefer a native Git workflow. It allows you to design your API specifications using YAML or JSON files and keeps them in a seamless, two-way sync with your connected Git repository. 

## Creating a Spec-first Project

<Steps>
  <Step>
    In the main window, click the **+ New Project** button. Select the **General** category at the top, and then choose **Spec-first Mode**.
  </Step>
  <Step>
    Scroll down to the **Connect with Git Repository** section and authorize your preferred Git provider (e.g., GitHub or GitLab).
  </Step>
  <Step>
    Select the target **Organization**, the specific **Repository** you want to link, and the **Main branch** for synchronization.
  </Step>
  <Step>
    Enter a **Project Name** and configure your team permissions, then click **Create**.
      
<Background>
 
![image.png](https://api.apidog.com/api/v1/projects/544525/resources/374624/image-preview)
</Background>

  </Step>
</Steps>

## The Specs Workspace: Code-Driven Design

The biggest difference you'll notice in Spec-first Mode is the introduction of the **Specs** module in the left sidebar. This transforms Apidog from a visual form editor into a dedicated IDE for your API specifications.

* **File-Based Management:** Instead of filling out visual forms, you manage raw `.json` or `.yaml` files directly. The central code editor provides syntax highlighting, validation, and auto-completion for OpenAPI and Swagger formats.
* **Real-time Directory Parsing:** As you write or modify your code in the editor, the left sidebar automatically parses your file and generates a visual, navigable outline of your API endpoints (e.g., Paths, Components).
* **Sync Status:** You can easily monitor the connection state with your repository by checking the sync indicator at the bottom-left corner of the sidebar (e.g., "Synced just now").

<Background>

![CleanShot 2026-03-31 at 16.53.12@2x.png](https://api.apidog.com/api/v1/projects/544525/resources/374625/image-preview)
</Background>


## Committing and Pushing Changes

Spec-first Mode integrates standard Git version control operations directly within the Apidog interface, ensuring your Apidog project and your remote Git repository are always aligned.

<Steps>
  <Step>
    After making changes to your specification files, click the **Commit & Push** button located at the top right of the workspace.
  </Step>
  <Step>
    The **Push to Git repo** modal will appear. Review the list of modified, added, or deleted files under the "Changes" section.
  </Step>
  <Step>
    Enter a descriptive **Commit Message** explaining your updates.
  </Step>
  <Step>
    Click **Push** to commit and sync your changes directly to your remote repository branch. If you want to revert your current unpushed edits, you can select **Discard all changes** instead.
      
<Background>
  
![CleanShot 2026-03-31 at 17.21.53@2x.png](https://api.apidog.com/api/v1/projects/544525/resources/374633/image-preview)
</Background>

  </Step>
</Steps>
