# Designing APIs in a Branch

In a newly created sprint branch, there is no content by default. This approach helps developers focus on the changes needed for the current sprint. You can add resources and make modifications using two main methods.

## Choosing Your Approach

| Method | Best For | Key Benefit |
|--------|----------|-------------|
| **Manual Changes** | API-First development | Clear specification before development |
| **OAS Import** | Code-First development | Automatic comparison with main branch |

:::tip[]
Apidog highly recommends the **API-First** approach (manual changes) for increased efficiency and lower collaboration costs.
:::

## Manual Changes

Manually modifying content within a sprint branch allows you to define your API specifications clearly before diving into development.

### Forking Resources from the Main Branch

When you need to modify existing endpoints, schemas, or response components based on current sprint requirements:

1. Use **Fork from main** to create a copy of required resources
2. All parent folders are automatically imported
3. Imported resources are marked with association indicators

<Background>
![Forking resources from main branch](https://assets.apidog.com/help/assets/images/design-branch-01-cc381856d1a3d2a31f0bc8a666253906.png)
</Background>

**Folder hierarchy:**

<Background>
![Imported resources with association indicators](https://assets.apidog.com/help/assets/images/design-branch-02-2ee32b4dd243b6d2888594be599ea4dc.png)
</Background>

**Endpoint cases:**

Endpoint cases are imported along with endpoints by default and also display association indicators.

<Background>
![Imported endpoint cases](https://assets.apidog.com/help/assets/images/design-branch-03-befa9d04a000e6bbbcefbc5c2245d84e.png)
</Background>

### Pulling Latest Changes from Main Branch

While working in a sprint branch, urgent updates may require changes directly in the main branch. To synchronize:

1. You'll receive a notification when associated resources in the main branch are updated

<Background>
![Resources discrepancies notification](https://api.apidog.com/api/v1/projects/544525/resources/348679/image-preview)
</Background>

2. Click the notification to review changes
3. Choose whether to pull updates or retain current sprint branch content

<Background>
![Decide on change updates](https://api.apidog.com/api/v1/projects/544525/resources/348680/image-preview)
</Background>

4. Select desired content and confirm the update

### Creating New Resources

To create new endpoints, schemas, or response components for the current sprint:

1. Use the **New** feature to add resources to the current sprint branch

<Background>
![Creating new resources in sprint branch](https://assets.apidog.com/help/assets/images/design-branch-04-7b0e22577b7221dc960e574bc6cac307.png)
</Background>

2. If the required parent folder doesn't exist, use:
   - **Select Endpoint Folders**: Choose existing folders
   - **New Endpoint Folder**: Create new folders

### Reordering and Adjusting Folder Contents

You can perform the same operations on imported or newly created resources as in the main branch:

**Drag to reorder:**

<Background>
![Reordering folder contents](https://assets.apidog.com/help/assets/images/design-branch-07-23cefd434da89fdaee0aad06ed966f35.png)
</Background>

**Imported folders with indicators:**

<Background>
![Folders with association indicators](https://assets.apidog.com/help/assets/images/design-branch-08-4d8c65267782401240a675017192b1cb.png)
</Background>

**Adjust folder contents:**

<Background>
![Adjusting folder contents](https://assets.apidog.com/help/assets/images/design-branch-09-f7a7e84f4a73a30d690d9808baa1627a.png)
</Background>

### Deleting and Restoring Resources

Sprint branches have a trash feature that works the same as the main branch:

1. Delete resources as needed
2. View deleted resources in **Trash**
3. Restore resources when needed

<Background>
![Deleting and restoring resources](https://assets.apidog.com/help/assets/images/design-branch-10-72c46703e09b500c3b79534d8b0627f2.png)
</Background>

:::warning[]
Repeatedly importing, deleting, and restoring the same main branch resource can lead to unexpected data issues. Minimize these operations to maintain data integrity.
:::

### Mocking, Comparing, and Collaborating

**Unique mock addresses:**

Endpoints in a sprint branch have unique mock addresses specific to that branch, relying entirely on the current sprint branch's endpoint definitions.

<Background>
![Mocking endpoints](https://assets.apidog.com/help/assets/images/design-branch-11-7ce316eca7e2ac3b4a3601f27d087e42.png)
</Background>

**Comparing with main branch:**

Compare sprint branch resources with main branch counterparts to identify specific differences.

<Background>
![Comparing resources](https://assets.apidog.com/help/assets/images/design-branch-12-57e177791cb76edac95d2e86b13fd93b.png)
</Background>

**Collaboration links:**

Share sprint branch endpoints via collaboration links with other project members.

<Background>
![Sharing collaboration links](https://assets.apidog.com/help/assets/images/design-branch-13-23712cf97edf6bf3bd55dfa60cf9950c.png)
</Background>

:::info[]
When clicking a sprint branch endpoint collaboration link while in another branch, the system will prompt you to switch branches. Save any changes in your current branch before switching.
:::

## OAS Import

Import OpenAPI Specification (OAS) files directly into a sprint branch using manual, scheduled, or API import methods.

### Importing OAS into Sprint Branch

1. Ensure the target branch is selected in the top-left corner
2. Navigate to **Project Settings** → **Import Data**
3. Import data into the current branch

<Background>
![Importing OAS into sprint branch](https://api.apidog.com/api/v1/projects/544525/resources/348681/image-preview)
</Background>

**Scheduled imports:**

For automatic OAS imports, select the target branch when creating the [scheduled import](https://docs.apidog.com/scheduled-import-bind-data-sources-633932m0.md).

<Background>
![Scheduling automatic OAS import](https://api.apidog.com/api/v1/projects/544525/resources/348682/image-preview)
</Background>

### Automatic Comparison with Main Branch

When importing OAS into the sprint branch, the processing logic:

**For endpoints:**
1. Compare each endpoint's "Path & Method" in the OAS file with the main branch
2. **If identical**: Endpoint won't be imported
3. **If different**: Endpoint is associated with main branch and imported
4. **If new**: New endpoint is created in sprint branch

**For schemas:**
1. Compare schema names in the OAS file with the main branch
2. **If identical**: Schema won't be imported
3. **If different**: Schema is associated with main branch and imported
4. **If new**: New schema is created in sprint branch

**Import summary:**

After successful import, you'll see an overview of new and modified resources added to the sprint branch.

<Background>
![OAS import logic overview](https://api.apidog.com/api/v1/projects/544525/resources/348683/image-preview)
</Background>

:::tip[]
Resources that are completely unchanged compared to the main branch will not be included in the sprint branch after import, helping developers focus on necessary changes.
:::

