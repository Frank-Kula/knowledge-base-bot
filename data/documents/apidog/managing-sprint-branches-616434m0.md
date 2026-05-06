# Managing Sprint Branches

Sprint branch management allows you to view, protect, archive, and modify sprint branches within your project.

## Accessing Sprint Branch Management

**Option 1:** Click **Manage Sprint Branches** in the sprint branch switch next to **APIs**

**Option 2:** Navigate to **Settings** → **Manage Sprint Branches**

On the management page, you can:
- View a complete list of sprint branches
- See branch statistics
- Perform various operations on branches

<Background>
![Sprint branch management page](https://assets.apidog.com/help/assets/images/manage-branch-01-52dbeb63c5299dd61f1804643c3ca9a8.png)
</Background>

## Protecting Branches

:::warning[]
Currently, only the main branch can be set as protected.
:::

When you hover over a branch, you'll see available actions. To enable protection:

1. Click the **Protected** option
2. Once protected, direct modifications are not allowed
3. Changes must be made through a Merge Request (MR) from another branch
4. Requests require approval from a project administrator

<Background>
![Protected branch option](https://api.apidog.com/api/v1/projects/544525/resources/348702/image-preview)
</Background>

:::info[]
Project administrators can directly modify protected branches without submitting a merge request.
:::

For instructions on initiating and reviewing merge requests, see [Merging Sprint Branches](https://docs.apidog.com/merging-sprint-branches-616431m0.md#merging-sprint-branches-into-protected-main-branch).

## Archiving and Restoring Sprint Branches

### Archiving Branches

Archiving indicates that a sprint branch's development lifecycle is complete and it will no longer be used for business purposes.

**To archive a branch:**
1. Click **Archive** next to the branch
2. Archived branches are collapsed in the management page
3. Archived branches no longer appear in the sprint branch switch

<Background>
![Archiving sprint branches](https://assets.apidog.com/help/assets/images/manage-branch-02-7f03db5fd0ffc1723f63b5be38b1f99a.png)
</Background>

### Restoring Branches

If you need to query content from a previously archived sprint branch:

1. Click **Restore** next to the archived branch
2. The branch becomes a normal branch again
3. You can switch to this branch using the sprint branch switch
4. Perform any operations as needed

<Background>
![Restoring sprint branches](https://assets.apidog.com/help/assets/images/manage-branch-03-e3e9569d487b4feb32f8cbf97f84fb12.png)
</Background>

## Modifying Sprint Branches

### Renaming Branches

Click the **Edit** button to rename a sprint branch.

### Deleting Branches

Click the **Delete** button to permanently delete a branch.

:::warning[]
**Important:** Deleting a branch removes all its content permanently and cannot be undone. Proceed with caution.

We recommend using **Archive** instead of **Delete** in most circumstances.
:::

