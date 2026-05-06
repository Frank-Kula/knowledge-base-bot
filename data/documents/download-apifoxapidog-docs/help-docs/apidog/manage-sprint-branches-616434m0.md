# Manage sprint branches

Click `Manage Sprint Branches` in the sprint branch switch next to `APIs`, or navigate to `Settings` -> `Manage Sprint Branches` to access the sprint branch management page. On this page, you can view a complete list of sprint branches used in the project, along with their statistics, and perform various operations on the project's sprint branches.

![Apidog Managing Sprint Branches](https://assets.apidog.com/help/assets/images/manage-branch-01-52dbeb63c5299dd61f1804643c3ca9a8.png)

## Protecting branches

:::warning[]
Currently, only the main branch can be set as protected.
:::

When you hover over a branch, you will see a list of all the available actions for that branch. To enable protection for the current branch, simply click the`Protected`option. Once the branch is protected, direct modifications are not allowed. Any changes must be made through a Merge Request (MR) from another branch and will require approval from a project administrator.

<Background>
![protected-branch.png](https://api.apidog.com/api/v1/projects/544525/resources/348702/image-preview)
</Background>

If you are a project administrator, you can directly modify the contents of a protected branch without needing to submit a merge request. For instructions on how to initiate and review merge requests, [refer to this article](https://docs.apidog.com/merge-sprint-branches-616431m0#merging-sprint-branches-into-protected-main-branch).

## Archiving/Restoring sprint branches

For unarchived sprint branches, clicking on `Archive` will mark the sprint branch as archived. An archived sprint branch indicates that its development lifecycle is complete and it will no longer be used for business purposes. Archived sprint branches will be collapsed in the sprint branch management page and will no longer be displayed in the sprint branch switch at the top right of the folder, making them unavailable for switching.

![Apidog Archiving/Restoring Sprint Branches](https://assets.apidog.com/help/assets/images/manage-branch-02-7f03db5fd0ffc1723f63b5be38b1f99a.png)

If you need to query the content of a previously archived sprint branch and possibly revert to it, you can restore the branch to make it a normal branch again. Once restored, you can switch to this branch using the sprint branch switch and perform any operations as needed.

![Apidog Restoring Sprint Branches](https://assets.apidog.com/help/assets/images/manage-branch-03-e3e9569d487b4feb32f8cbf97f84fb12.png)

## Modifying sprint branches

You can click the `Edit` button to rename a sprint branch or click the `Delete` button to permanently delete it. Please note that deleting a branch removes all its content permanently and cannot be undone, so proceed with caution. We recommend using the `Archive` instead of `Delete` in common circumstances.
