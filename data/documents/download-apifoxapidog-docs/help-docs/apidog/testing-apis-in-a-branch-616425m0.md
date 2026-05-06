# Testing APIs in a Branch

In a newly created sprint branch, automated testing starts with no predefined content. To test and validate content, add test scenarios via forking or creating new ones.

:::tip[Best Practice]
Finalize necessary changes to endpoint resources in the APIs section first before organizing test scenarios for automated testing. This aligns with typical development workflows.
:::

## Forking Test Scenarios from Main Branch

The system automatically identifies and selects test scenarios that include endpoints already forked into the sprint branch, making it easier for testers to filter and import them.

<Background>
![Forking test scenarios from main branch](https://assets.apidog.com/help/assets/images/test-branch-01-2f7fde299e8b02f689d1fbaf8feff9a8.png)
</Background>

**Automatic folder hierarchy:**

All parent folders of forked resources are automatically included in the current sprint branch folder. Forked resources display visible association indicators, similar to resources in APIs.

<Background>
![Forked test scenarios with indicators](https://assets.apidog.com/help/assets/images/test-branch-02-f2171b0f0b62e029764d06e62d703cb6.png)
</Background>

## Creating New Test Scenarios

When new endpoints are added to the current sprint, create new test scenarios to validate them:

1. Use the **New** feature to add test scenarios to the current sprint branch

<Background>
![Creating new test scenarios](https://assets.apidog.com/help/assets/images/test-branch-03-bef0662f3d2b3f5cf78098d450f17929.png)
</Background>

## Designing Test Scenarios

In forked or newly created test scenarios, you can organize steps similarly to the main branch. The UI clearly indicates whether a test step uses resources from the sprint branch or the main branch.

<Background>
![Organizing test scenarios](https://assets.apidog.com/help/assets/images/test-branch-04-9625393e1abf37afe3dd6fb3a715fdfe.png)
</Background>

**Focus on impacted steps:**

Concentrate on steps impacted by the current sprint branch resources. Fill in new request parameters based on modified endpoint documentation to quickly set up complete test scenarios.

<Background>
![Configuring test steps](https://assets.apidog.com/help/assets/images/test-branch-05-c6a41028f122e931d4c8c65f42536fa1.png)
</Background>

**Test step annotations:**

Three types of test steps show their association with branch resources:
- **Import from endpoints**
- **Import from endpoint cases**
- **Reference other test scenario**

Each step is annotated to show association with either main branch or current sprint branch resources.

<Background>
![Test step annotations](https://assets.apidog.com/help/assets/images/test-branch-06-029da2300bcf59c76c212c4917f46db9.png)
</Background>

## Running Test Scenarios

Once test scenarios are created and designed, run them to start the testing process.

**Execution logic:**
- **Sprint branch resources**: Uses data from the sprint branch (e.g., modified response data schema for validation)
- **Main branch resources**: Uses data from the main branch

<Background>
![Running test scenarios](https://assets.apidog.com/help/assets/images/test-branch-07-4f59a724bdcd48be70facdc426c1ce33.png)
</Background>

