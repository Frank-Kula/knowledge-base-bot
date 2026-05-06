# Merging Sprint Branches

Once endpoint definitions are developed and deployed within a sprint branch, you can merge some or all of the changes into the main branch.

## Accessing Merge Functions

### For APIs

**Option 1:** Click **Merge** in the branch switch next to **APIs**

**Option 2:** Click **Merge to main** at the right bottom of **APIs**

<Background>
![Merging sprint branches entry point](https://assets.apidog.com/help/assets/images/merge-branch-01-9a5e6ba2cd272d9ec6a83237c5b5fc21.png)
</Background>

### For Test Scenarios

Test scenarios require separate merging and do not merge automatically with resources in APIs.

While in a sprint branch, hover over the **...** button next to a test scenario in automated testing to see the **Merge to Main** option.

<Background>
![Merging test scenario entry point](https://assets.apidog.com/help/assets/images/merge-branch-02-b7b29109605ed74323faf24449e88809.png)
</Background>

## Merging into Unprotected Main Branch

If the main branch is not protected, users with project merge permissions can review changes and directly merge them into the main branch.

### Overview of Pending Merges

Clicking **Merge** opens the merge overview popup with key elements:

| Element | Description |
|---------|-------------|
| **Filter** | View only modified resources or all resources in the current sprint branch |
| **Merging Preview** | Displays final effect on main branch directory after merging |
| **Resource Status** | Color-coded dots (gray: unchanged, orange: modified, green: new) |
| **Post-Merge Status** | Choose how to adjust merged resource status: Follow Current Branch, Follow Main, or Specified Status |

<Background>
![Merge overview](https://assets.apidog.com/help/assets/images/merge-branch-03-67acadf7d29a5e9f10b738ebddc73dab.png)
</Background>

### Detailed Review of Pending Merges

Click a resource to expand the popup and show detailed content for merge decision-making.

#### New Resources

- Resources created in the current sprint branch, not present in the main branch
- If merged, the resource will be created in the main branch at the specified location
- Click to view complete content

<Background>
![New resource details](https://assets.apidog.com/help/assets/images/merge-branch-04-a46190b3083982ddd0bb652a2f3b9e37.png)
</Background>

#### Modified Resources

- Resources forked from the main branch and associated with main branch resources
- If merged, the main branch resource will be overwritten
- Click to see changes compared with main branch resource and complete content

<Background>
![Modified resource details](https://assets.apidog.com/help/assets/images/merge-branch-05-b4012c7049c3b0cf03267c26ae1625ef.png)
</Background>

#### Unchanged Resources

- Resources forked from the main branch without modifications
- Cannot be selected for merging (and don't need to be)
- No detailed content shown

<Background>
![Unchanged resource details](https://assets.apidog.com/help/assets/images/merge-branch-06-9fb76934b428995f51ba15a8f6d6e030.png)
</Background>

:::warning[]
If a parent resource is not selected, none of its child resources can be merged individually.
:::

**Merge confirmation:**

<Background>
![Merge confirmation popup](https://assets.apidog.com/help/assets/images/merge-branch-07-3f7879a2fb2d51e512b944efe9cc412b.png)
</Background>

**Merge completion:**

After merging, a summary popup shows changes made to the main branch.

<Background>
![Merge completion popup](https://assets.apidog.com/help/assets/images/merge-branch-08-440a1e8e673ec45c5ed58df2d5a8aa8c.png)
</Background>

### Viewing Merge Details and Reverting Merges

In the main branch, access **Change History** of a resource to:
- View content modified through merges
- Compare content with other versions
- Track and rollback changes

<Background>
![Main branch resource history](https://assets.apidog.com/help/assets/images/merge-branch-09-a7dd28b24df0c6ab76958e3c7d23118e.png)
</Background>

<Background>
![Resource history comparison](https://assets.apidog.com/help/assets/images/merge-branch-10-bc0eccfe261d7954b32b14897024efa7.png)
</Background>

## Merging into Protected Main Branch

When merging into a protected main branch, users with editing permissions must create a merge request for administrator review and approval.

### Creating a Merge Request

1. Click **Merge** in the project
2. View all changes in the current branch
3. Select specific resources to merge
4. Click **Create Merge Request** at the bottom-right

<Background>
![Creating merge request](https://api.apidog.com/api/v1/projects/544525/resources/348694/image-preview)
</Background>

### Reviewing a Merge Request

Reviewers see a notification in **Project Overview** indicating a new merge request.

**To review:**
1. Go to **Project Overview** → **Merge Requests**
2. View list of requests with detailed information

<Background>
![Merge requests list](https://api.apidog.com/api/v1/projects/544525/resources/348695/image-preview)
</Background>

3. Click a pending merge request to evaluate contents
4. Compare content before and after merge
5. Click **Merge** to approve and merge changes

<Background>
![Merge request review](https://api.apidog.com/api/v1/projects/544525/resources/348696/image-preview)
</Background>

**Merge completion:**

<Background>
![Modification overview](https://api.apidog.com/api/v1/projects/544525/resources/348697/image-preview)
</Background>

**Merged status:**

<Background>
![Merged request status](https://api.apidog.com/api/v1/projects/544525/resources/348698/image-preview)
</Background>

### Modifying a Submitted Merge Request

After submitting a merge request, if changes are needed:

1. Directly modify content in the sprint branch
2. Changes automatically sync with the existing merge request
3. No need to create a new request
4. Modifications are indicated on the review page

<Background>
![Modifying submitted merge request](https://api.apidog.com/api/v1/projects/544525/resources/348699/image-preview)
</Background>

### Rejecting a Merge Request

If a merge request is not suitable:

1. Click **Reject** on the merge request review page
2. Request is marked as **Closed**
3. To make changes and merge again, create a new merge request

<Background>
![Rejecting merge request](https://api.apidog.com/api/v1/projects/544525/resources/348700/image-preview)
</Background>

**Closed request details:**

<Background>
![Closed merge request details](https://api.apidog.com/api/v1/projects/544525/resources/348701/image-preview)
</Background>

## Merging Automated Test Scenarios

Automated test scenarios and endpoints are merged independently and separately. Test scenarios need individual merging without an overall merge page.

:::warning[Important Notes]
1. **Merge APIs first**: Merge resources in APIs before merging test scenarios. Failing to do so may cause related test scenarios in the main branch to run abnormally.
2. **Administrator access**: Currently, only project administrators can merge test scenarios into protected main branches. A feature for merge requests for test scenarios is planned for the future.
:::

**Merging test scenarios:**

Hover over the **...** button of a test scenario in automated testing to see the **Merge to Main** option.

<Background>
![Merging test scenario](https://assets.apidog.com/help/assets/images/merge-branch-11-d6d79bd02a08dc4c8139c51b842c28fd.png)
</Background>

**Test scenario merge popup displays:**

| Information | Description |
|-------------|-------------|
| **Basic Information** | Sprint branch test scenario and associated main branch scenario (if any) |
| **Last Run Result** | Last manual run result (hover for summary). Ensure scenario passes before merging |
| **Merge Action** | Overwrite (if forked from main) or Add (if new) |

<Background>
![Test scenario merge popup](https://assets.apidog.com/help/assets/images/merge-branch-12-5667db7445e507e9949321b38c90f692.png)
</Background>

