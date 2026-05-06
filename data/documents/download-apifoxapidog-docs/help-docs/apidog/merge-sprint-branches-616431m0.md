# Merge sprint branches

Once endpoint definitions are developed and deployed within a sprint branch, you have the option to merge some or all of the endpoint changes from the sprint branch into the main branch.

## Merging sprint branches

When you are in a sprint branch, you can see the "Merge" button in the branch switch next to `APIs`. You can also see the `Merge to main` button at the right bottom of the `APIs`.

<Background>
![Apidog Merging Sprint Branches Entry Point](https://assets.apidog.com/help/assets/images/merge-branch-01-9a5e6ba2cd272d9ec6a83237c5b5fc21.png)
</Background>

In automated testing, individual test scenarios require separate merging and do not merge automatically with resources in `APIs`. While in a sprint branch, you can find the 'Merge to Main' dropdown option by hovering over the `...` button next to a test scenario in automated testing.

<Background>
![Apidog Merging Test Scenario Entry Point](https://assets.apidog.com/help/assets/images/merge-branch-02-b7b29109605ed74323faf24449e88809.png)
</Background>

## Merging sprint branches into unprotected main branch

If the main branch is not set as`protected`, users with project merge permissions can review the changes and directly merge them into the main branch.

### Overview of pending merges

In `APIs`, clicking the "Merge" button opens the merge overview popup.

<Background>
![Apidog Merge Overview](https://assets.apidog.com/help/assets/images/merge-branch-03-67acadf7d29a5e9f10b738ebddc73dab.png)
</Background>

In this popup, you will see key elements:

- **Filter:** Use the filter to view only the resources in the current sprint branch that have been modified compared to the main branch, or view all resources in the current sprint branch. By default, modified resources are shown to help users focus on changes.
- **Merging Preview:** This section displays the final effect on the main branch directory after merging the current sprint branch. Use this directory to confirm the placement and content of resources post-merge. Resources in the directory are marked with color-coded dots (gray for unchanged, orange for modified, green for new) to indicate their status. Use the checkboxes on the right to select or deselect resources for merging into the main branch.
- **Post-Merge Endpoint Status:** Choose how to adjust the status of the merged resources in the main branch. Options include `Follow the Current Branch`, `Follow Main`, or `Specified Status`.

### Detailed review of pending merges

In the merge overview popup, you can perform additional operations on the folder content to review whether the resources should be merged into the main branch. Clicking a resource expands the popup to show detailed content, aiding in the merge decision.

Different resources have different merge logic and details:

- **New Resources:**

  - New Resources refers to resources created in the current sprint branch, not present in the main branch.
  - If merged, the resource will be created in the main branch at the specified location.
  - Click to view the complete content of this resource, as shown in the image below.

<Background>
  ![Apidog New Resource Details](https://assets.apidog.com/help/assets/images/merge-branch-04-a46190b3083982ddd0bb652a2f3b9e37.png)
</Background>

- **Modified Resources:**

  - Modified Resources refers to resources that is forked from the main branch into the current sprint branch and associated with the main branch resource.
  - If merged, the main branch resource will be overwritten.
  - Click to see the changes of this resource compared with the main branch resource, as well as the complete content, as shown in the image below.

<Background>
  ![Apidog Modified Resource Details](https://assets.apidog.com/help/assets/images/merge-branch-05-b4012c7049c3b0cf03267c26ae1625ef.png)
</Background>

- **Unchanged Resources:**

  - Unchanged Resources refers to resources that is forked from the main branch without any modifications in the current sprint branch.
  - Unchanged resources cannot be selected for merging (and don't need to be).
  - Clicking shows no detailed content for this resource, as shown in the image below.

<Background>
  ![Apidog Unchanged Resource Details](https://assets.apidog.com/help/assets/images/merge-branch-06-9fb76934b428995f51ba15a8f6d6e030.png)
</Background>

Clicking the merge button at the bottom right will merge all selected resources from the folder into the main branch according to the sprint branch settings. Note that if a parent resource is not selected, none of its child resources can be merged individually.

<Background>
![Apidog Merge Confirmation Popup](https://assets.apidog.com/help/assets/images/merge-branch-07-3f7879a2fb2d51e512b944efe9cc412b.png)
</Background>

After merging, a toast message confirms the operation's success, closes the merge popup, and opens a summary popup to review the changes made to the main branch.

<Background>
![Apidog Merge Completion Popup](https://assets.apidog.com/help/assets/images/merge-branch-08-440a1e8e673ec45c5ed58df2d5a8aa8c.png)
</Background>

### Viewing merge details / Reverting merges in the main branch

In the main branch, accessing the `Change History` of a resource displays the content modified through merges, allowing users to view detailed modification. Additionally, users can compare the content with that of other versions, facilitating easy tracking and rollback of changes.

<Background>
![Apidog Main Branch Resource History](https://assets.apidog.com/help/assets/images/merge-branch-09-a7dd28b24df0c6ab76958e3c7d23118e.png)
</Background>

<Background>
![Apidog Main Branch Resource History](https://assets.apidog.com/help/assets/images/merge-branch-10-bc0eccfe261d7954b32b14897024efa7.png)
</Background>

## Merging sprint branches into protected main branch

When merging changes from a sprint branch into a protected main branch, a user with only the editing permissions must create a merge request. The project administrator will then review and approve the request before the changes are applied.

### Creating a merge request

When you click`Merge`in the project, it works just like merging into an unprotected main branch, allowing you to view all the changes in the current branch. From here, you can select the specific resources you want to merge into the main branch. Once selected, click the`Create Merge Request`button at the bottom-right corner to submit the request for review.

<Background>
![create-merge-request.png](https://api.apidog.com/api/v1/projects/544525/resources/348694/image-preview)
</Background>

### Reviewing a merge request

After a merge request is created, reviewers will see a clear notification in `Project Overview`indicating a new merge request has been submitted. To review it, go to`Project Overview`>`Merge Requests`, where you can view a list of requests along with detailed information.

<Background>
![image.png](https://api.apidog.com/api/v1/projects/544525/resources/348695/image-preview)
</Background>

Clicking on a pending merge request allows the reviewer to evaluate the contents of the merge request. They can compare the content before and after the merge in detail and decide whether to approve the request. If they decide to move forward with the merge, they can click the`Merge`button at the bottom right, which will merge all the changes from the current request into the main branch.

<Background>
![merge-request-into-main-branch.png](https://api.apidog.com/api/v1/projects/544525/resources/348696/image-preview)
</Background>

The merging process follows [the same logic as merging into an unprotected main branch.](https://docs.apidog.com/merge-sprint-branches-616431m0#detailed-review-of-pending-merges)

Once the merge is completed, the changes will be merged into the main branch, and there will be an overview table indicating the modifications made to the main branch.

<Background>
![modifacation-overview.png](https://api.apidog.com/api/v1/projects/544525/resources/348697/image-preview)
</Background>

The status of the merge request will also be updated to`Merged`. Clicking on it will show the details of the merged request.

<Background>
![merged-request-status.png](https://api.apidog.com/api/v1/projects/544525/resources/348698/image-preview)
</Background>

### Modifying a submitted merge request

Occasionally, after submitting a merge request, reviewers may request changes or adjustments might be needed before approval. In such cases, you can directly modify the content in the sprint branch. These changes will automatically sync with the existing merge request, eliminating the need to create a new one. The modifications will be indicated on the merge request review page.

<Background>
![modifying-sumitted-merge-request.png](https://api.apidog.com/api/v1/projects/544525/resources/348699/image-preview)
</Background>

### Rejecting a merge request

If the reviewer decides that the merge request is not suitable for the sprint branch, they can click`Reject`on the merge request review page. Once rejected, the merge request will be marked as`Closed`. To make changes and attempt merging again, a new merge request must be created.

<Background>
![image.png](https://api.apidog.com/api/v1/projects/544525/resources/348700/image-preview)
</Background>

Clicking on a closed merge request will show all the details.

<Background>
![closed-merge-request-details.png](https://api.apidog.com/api/v1/projects/544525/resources/348701/image-preview)
</Background>

## Merging automated test scenarios

Automated test scenarios and endpoints are currently merged independently and separately. Test scenarios need to be merged individually, without an overall merge page.

:::warning[Important Notes:]
1. Please merge the resources in APIs first before merging test scenarios. Failing to do so may cause related test scenarios in the main branch to run abnormally after merging.
2. Currently, only project administrators have the ability to merge test scenarios into the protected main branch. However, we plan to implement a new feature that will allow users to submit merge requests for test scenarios, similar to the existing feature for endpoint merge requests. This will make it easier to merge test scenarios into the protected main branch in the future.
:::

When you are in a sprint branch, hover your mouse over the `...` button of a test scenario in automated testing to see the "Merge to Main" option.

<Background>
![Apidog Merging Test Scenario Entry Point](https://assets.apidog.com/help/assets/images/merge-branch-11-d6d79bd02a08dc4c8139c51b842c28fd.png)
</Background>

Clicking this opens the test scenario merge popup, displaying the following information:

- **Basic Information:** Shows the sprint branch test scenario to be merged and the associated main branch test scenario (if any).
- **Last Run Result:** Displays the last manual run result of the test scenario in the sprint branch. Hovering over the icon shows a summary of the results. Testers can use this information to decide whether to proceed with the merge. If the result shows `Untested` or `Failed`, it is recommended to ensure the test scenario passes the test completely before merging.
- **Merge Action:** Options include `Overwrite` and `Add`. If the test scenario was forked from the main branch, it will be merged by overwriting the main branch resource; if the test scenario is new, it will be added to the main branch.

<Background>
![Apidog Test Scenario Merge Popup](https://assets.apidog.com/help/assets/images/merge-branch-12-5667db7445e507e9949321b38c90f692.png)
</Background>
