# Test APIs in a branch

In a newly created sprint branch, automated testing starts with no predefined content. To test and validate the content, you need to add test scenarios via forking or creating new ones. It's best to finalize the necessary changes to the endpoint resources in the endpoints first before organizing test scenarios for automated testing, aligning with typical development workflows.

## Forking test scenarios from the main branch

You can fork test scenarios from the main branch seamlessly. If the endpoints in the main branch have already been forked into the sprint branch and are included in some test scenarios, the system will automatically select these related scenarios during import. This makes it easier for testers to filter and import them. Testers can then simply modify the existing test scenarios to quickly complete the automated test scenarios for the current sprint. Additionally, you can manually select and import other test scenarios from the main branch as needed.

![Apidog Forking Test Scenarios from the Main Branch](https://assets.apidog.com/help/assets/images/test-branch-01-2f7fde299e8b02f689d1fbaf8feff9a8.png)

To ensure the accuracy of the resource folder hierarchy, all parent folders of the forked resource will be automatically included in the current sprint branch folder. Forked resources from the main branch will have visible association indicators in the folder, similar to resources in APIs.

![Apidog Forking Test Scenarios from the Main Branch](https://assets.apidog.com/help/assets/images/test-branch-02-f2171b0f0b62e029764d06e62d703cb6.png)

## Creating new test scenarios

Based on the requirements of the current sprint, especially when new endpoints are added, you might need to create new test scenarios to validate these new endpoints. Use the `New` feature to add new test scenarios to the current sprint branch.

![Apidog Creating New Test Scenarios](https://assets.apidog.com/help/assets/images/test-branch-03-bef0662f3d2b3f5cf78098d450f17929.png)

## Designing Test Scenarios in the Sprint Branch

In a forked or newly created test scenario within the sprint branch, you can organize steps similarly to those in the main branch. Since these steps might involve both unchanged and modified endpoints, the UI will clearly indicate whether a test step uses resources from the sprint branch or the main branch, ensuring clarity and consistency.

![Apidog Arranging Test Scenarios](https://assets.apidog.com/help/assets/images/test-branch-04-9625393e1abf37afe3dd6fb3a715fdfe.png)

Generally, in a testing scenario, it's crucial to concentrate on the steps impacted by the resources of the current sprint branch. After clicking into the steps, fill in the new request parameters based on the modified endpoint documentation, and you can quickly set up a complete test scenario and conduct tests on the sprint branch.

![Apidog Arranging Test Scenarios](https://assets.apidog.com/help/assets/images/test-branch-05-c6a41028f122e931d4c8c65f42536fa1.png)

The three types of test steps, namely,`Import from endpoints`, `Import from endpoint cases` and `Reference other Test Scenario`, will be annotated to show their association with either main branch resources or current sprint branch resources. When you click to view the details of these steps, you can also see which branch their associated resources are on.

![Apidog Arranging Test Scenarios](https://assets.apidog.com/help/assets/images/test-branch-06-029da2300bcf59c76c212c4917f46db9.png)

## Running test scenarios

Once the test scenarios in the sprint branch are created and designed, you can run them to start the testing process. The rules for running test scenarios follow the same logic as the front-end display. If a step shows it is associated with sprint branch resources, it will use data from the sprint branch (e.g., using the modified response data schema in the sprint branch for response validation). If a step shows it is associated with main branch resources, it will use data from the main branch.

![Apidog Running Test Scenarios](https://assets.apidog.com/help/assets/images/test-branch-07-4f59a724bdcd48be70facdc426c1ce33.png)
