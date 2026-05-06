# Design API in a branch

In a newly created sprint branch, there is no content by default. This approach helps developers focus on the changes needed for the current sprint. There are two main ways to add resources and make modifications within a sprint branch.

- **Manual Changes:** You can manually import or create resources in Apidog and make the necessary changes. This method is ideal for teams following an API-First development approach, which Apidog highly recommends for its effectiveness.
 
- **OAS Import:** Alternatively, you can import an OpenAPI Specification (OAS) directly into a sprint branch. During the import process, Apidog automatically compares the OAS content with the endpoints in the main branch, allowing it to generate associatd or new resources. You can also import the modified OAS multiple times into the same sprint branch to update its content. This method is ideal for teams that prefer a Code-First development approach.

You should choose the method that best fits your particular scenario and requirements. Changes in one sprint branch only affect its data and have no impact on the main branch or other branches.

## Manual changes

Manually modifying content within a sprint branch is highly recommended. This method, which involves picking or creating resources manually, helps you define your endpint specifications clearly before diving into development, leading to increased efficiency and lower collaboration costs.

### Forking resources from the main branch

When you need to modify and upgrade existing endpoints, schemas, or response components based on the requirements of the current sprint, use the `Fork from main` to create a copy of the required resources in the current sprint branch.

<Background>
![Apidog Importing Resources from Main Branch](https://assets.apidog.com/help/assets/images/design-branch-01-cc381856d1a3d2a31f0bc8a666253906.png)
</Background>

When importing a resource, all its parent folders will automatically be imported into the current sprint branch folder, ensuring an accurate folder hierarchy. Imported resources from the main branch will be marked with visible association indicators in the folder.

<Background>
![Apidog Importing Resources from Main Branch](https://assets.apidog.com/help/assets/images/design-branch-02-2ee32b4dd243b6d2888594be599ea4dc.png)
</Background>

Currently, endpoint cases are imported along with the endpoints by default into the sprint branch. Similarly, imported endpoint cases will also have association indicators in the folder.

<Background>
![Apidog Importing Resources from Main Branch](https://assets.apidog.com/help/assets/images/design-branch-03-befa9d04a000e6bbbcefbc5c2245d84e.png)
</Background>

### Pulling the latest changes from the main branch

While working in a sprint branch, urgent requests may occasionally require immediate updates to live endpoints. In such cases, changes might need to be made directly in the main branch. This can result in discrepancies between the updated main branch and the sprint branch. To address this, you can synchronize by pulling the latest changes from the main branch into your sprint branch.

If resources in the main branch associated with the sprint branch are updated, you will receive a clear notification when accessing those resources in the sprint branch.

<Background>
![resources-discrepancies-notification.png](https://api.apidog.com/api/v1/projects/544525/resources/348679/image-preview)
</Background>

Clicking the notification allows you to review the changes and choose whether to pull updates from the main branch or retain the current sprint branch.

<Background>
![decide-change-updates.png](https://api.apidog.com/api/v1/projects/544525/resources/348680/image-preview)
</Background>

After reviewing, select the desired content and confirm the update. This process ensures that the sprint branch is updated appropriately, resolving any conflicts caused by main branch updates.

### Creating new resources

When you need to create new endpoints, schemas, or response components to meet business requirements for the current sprint, use the `New` feature to add these new resources to the current sprint branch.

<Background>
![Apidog Creating New Resources in Sprint Branch](https://assets.apidog.com/help/assets/images/design-branch-04-7b0e22577b7221dc960e574bc6cac307.png)
</Background>

The create feature in the sprint branch functions the same as it does in the main branch. You can create a resource in any folder within the sprint branch. If you find that the required parent folder for your new resource does not exist in the sprint branch, you can use the `Select Endpoint Folders` or `New Endpoint Folder` feature to create the necessary parent folder before creating the required resource.

**Select Endpoint Folders:** ![Apidog Select Endpoint Folders](https://assets.apidog.com/help/assets/images/design-branch-05-bca066c258600d3f27983d756e380773.png)

**New Endpoint Folder:** ![Apidog New Endpoint Folder](https://assets.apidog.com/help/assets/images/design-branch-06-50d83d344d5936ef39fb7694055f4100.png)

### Reordering and adjusting folder contents

During a sprint, you might need to reorder resources or modify the contents of existing or new folders to meet current requirements. In the sprint branch, you can perform the same operations on imported or newly created resources as in the main branch. This includes reordering endpoints or changing parent folder settings. Adjust the endpoint order by dragging items in the folder tree to maintain an organized structure.

Adjusting endpoint order by dragging:

<Background>
![Apidog Reordering and Adjusting Folder Contents](https://assets.apidog.com/help/assets/images/design-branch-07-23cefd434da89fdaee0aad06ed966f35.png)
</Background>

If imported, folders will also display association indicators:

<Background>
![Apidog Reordering and Adjusting Folder Contents](https://assets.apidog.com/help/assets/images/design-branch-08-4d8c65267782401240a675017192b1cb.png)
</Background>

Content in folders can be freely adjusted and modified:

<Background>
![Apidog Reordering and Adjusting Folder Contents](https://assets.apidog.com/help/assets/images/design-branch-09-f7a7e84f4a73a30d690d9808baa1627a.png)
</Background>

### Deleting/restoring resources

In a sprint branch, you can delete resources at will and see the deleted resources in the `Trash` where you can choose to restore them. This feature works the same as the trash in the main branch.

<Background>
![Apidog Deleting/Restoring Resources](https://assets.apidog.com/help/assets/images/design-branch-10-72c46703e09b500c3b79534d8b0627f2.png)
</Background>

Repeatedly importing, deleting, and restoring the same main branch resource in a sprint branch can lead to unexpected data issues. To maintain data integrity and avoid potential problems, it's best to minimize these operations whenever possible.

### Mocking, comparing, and collaborating on endpoints

Endpoints in a sprint branch will have a unique mock address specific to that branch. The mock content relies entirely on the endpoint definitions within the current sprint branch, allowing relevant team members to accurately simulate the responses of the modified endpoints for the sprint.

<Background>
![Apidog Mocking, Comparing, and Collaborating on APIs](https://assets.apidog.com/help/assets/images/design-branch-11-7ce316eca7e2ac3b4a3601f27d087e42.png)
</Background>

You can compare a sprint branch resource with its main branch counterpart to identify specific differences between them.

<Background>
![Apidog Mocking, Comparing, and Collaborating on APIs](https://assets.apidog.com/help/assets/images/design-branch-12-57e177791cb76edac95d2e86b13fd93b.png)
</Background>

Sprint branch endpoints can also be shared via collaboration links, which can be sent to other project members for collaboration.

<Background>
![Apidog Mocking, Comparing, and Collaborating on APIs](https://assets.apidog.com/help/assets/images/design-branch-13-23712cf97edf6bf3bd55dfa60cf9950c.png)
</Background>

When you click on a sprint branch endpoint collaboration link while in another branch, the system will prompt you to switch branches to view the endpoint. Be sure to save any changes in your current branch before making the switch.

<Background>
![Apidog Mocking, Comparing, and Collaborating on APIs](https://assets.apidog.com/help/assets/images/design-branch-14-691dfc760d4a507d82105e4d090faf4c.png)
</Background>

## OAS import

You can import OAS (OpenAPI Specification, also known as Swagger Specifications) directly into a sprint branch using various methods, such as manual, scheduled, or API imports.


### Import OAS into sprint branch

To import OAS into the sprint branch, ensure that the target branch is selected in the top-left corner. Then, go to the`Project Settings > Import Data`page, and import data into the current branch.

<Background>
![import-OAS-into-sprint-branch.png](https://api.apidog.com/api/v1/projects/544525/resources/348681/image-preview)
</Background>

If you want to schedule automatic OAS imports into the sprint branch, select the target branch during the creation of the [scheduled import](https://docs.apidog.com/scheduled-import-bind-data-sources-633932m0.md).

<Background>
![schedule-automatic-OAS-import.png](https://api.apidog.com/api/v1/projects/544525/resources/348682/image-preview)
</Background>

### Automatic comparison of OAS with the main branch

When importing OAS into the sprint branch, the processing logic follows these steps:

- Identify OAS file content
- Compare each endpoint's "Path & Method" in the OAS file with those in the main branch:
  - If the "Path & Method" matches and the OAS content is identical to that in the main branch, the endpoint won’t be imported into the sprint branch.
  - If a matching "Path + Method" is found but the OAS content differs from the main branch, the endpoint will be associated with the main branch and imported into the sprint branch.
  - If no matching "Path + Method" is found, a new endpoint will be created in the sprint branch.
- Compare schema name in the OAS file with those in the main branch:
  - If the schema name matches and the OAS content is identical, the schema will not be imported into the sprint branch.
  - If a matching schema name is found but the OAS content differs, the schema will be associated with the main branch and imported into the sprint branch.
  - If no matching schema name is found, a schema will be created in the sprint branch.
- If the import is successful, you will see an overview of the new and modified resources added to the sprint branch.

<Background>
![OAS-import-logic.png](https://api.apidog.com/api/v1/projects/544525/resources/348683/image-preview)
</Background>

In line with Apidog's goal of helping developers focus on the necessary changes for each sprint, any resources that are found to be completely unchanged compared to the main branch will not be included in the sprint branch after the import.


