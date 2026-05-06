# Manual Import

If you were originally using other tools and now want to migrate to Apidog, you can use the **Manual Import** feature.

## Where to Import?

You can access the import feature from the following locations:

- **Project Settings**: Go to `Settings` -> `Import Data`.
- **API List (Directory Tree)**: Click the `+` button next to the search bar and select `Import`.
- **Team Page**: Click the `Import Project` button on the project list page.
<!--
<Background>

![CleanShot 2025-11-21 at 18.03.40@2x.png](https://api.apidog.com/api/v1/projects/544525/resources/366289/image-preview)
</Background>
-->


## How to Manually Import
<Steps>
    <Step>
    **Select Data Format**
    Choose the format that matches your existing data (e.g., OpenAPI, Postman, cURL).
    </Step>
    <Step>
    **Upload or Paste Data**
    Upload a file or paste the raw text/URL according to the selected format.
  </Step>
  <Step>
    **Preview and Confirm**
    Apidog will parse the file and show a preview. You can select specific endpoints to import.
    <!-- <Background>
    ![CleanShot 2025-11-21 at 18.05.45@2x.png](https://api.apidog.com/api/v1/projects/544525/resources/366290/image-preview)
    </Background> -->
    :::highlight purple
    To customize how data is merged (e.g., overwrite vs. skip duplicates), check the [Import Options](https://docs.apidog.com/import-options-633930m0.md).
::: 
  </Step>
  <Step>
    **Complete Import**
    Click "Confirm" to finish. Your data will now be available in the project.
  </Step>
</Steps>



    

## Advanced: Importing to Sprint Branches

By default, data is imported into the **Main Branch**. If you are using Version Control, you can import directly into a specific **Sprint Branch**. 

The target branch is determined by the branch currently selected in the top-left corner of the app.


For more details, refer to [OAS imports into branches](https://docs.apidog.com/designing-apis-in-a-branch-616423m0.md#oas-import).
