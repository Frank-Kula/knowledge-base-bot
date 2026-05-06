# Managing Projects



In Apidog, projects are the core workspace where you design, test, and document your APIs. This guide covers creating, managing, and organizing projects within your team.

## Creating a Project

To create a new project, navigate to your team and click the **New Project** button. You can customize the project name and icon in the **Basic Settings** section under **Settings**.

<details>
<summary>📷 Visual Reference</summary>

<Background>
![](https://assets.apidog.com/help/assets/images/managing-project-1-5b9ed8b53731cdb64d59814aa7bcd010.png)
</Background>

</details>

## Project Overview

In an existing project, you can view key information and statistics on the **Overview** page under **APIs**.

### Endpoint Case/Test Scenario Stats

This section displays all the endpoints of the current project and provides statistics on testing coverage. It shows the percentage of endpoints that have associated test steps, as well as the percentage that have been tested within test scenarios. These statistics are valuable for evaluating the thoroughness of the API testing and their overall reliability.

<Background>
![test-coverage-data.png](https://api.apidog.com/api/v1/projects/544525/resources/348293/image-preview)
</Background>

**Core Data:**

- **Coverage of endpoint case**: The number of endpoints with associated cases / Total number of endpoints. This is mainly used to check if individual endpoints have corresponding cases.
- **Average cases per endpoint**: The total number of cases / Total number of endpoints. This is mainly used to assess the overall completeness of endpoint cases.
- **Endpoints without cases**: This shows the number of endpoints that have no cases.
- **Coverage of test scenario**: The number of endpoints covered in test scenarios / Total number of endpoints. This is mainly used to assess the extent to which endpoints are covered by automated tests.
- **Endpoints not covered by any test scenario**: This shows the number of endpoints that are not yet covered by automated tests.

:::info
Data calculation is asynchronous, so there may be a delay. If discrepancies occur, refresh after a moment to confirm.
:::

## Editing the Project

The team owner/administrator enters the created project and changes the project name or project icon in **Settings** → **Basic Settings**.

<details>
<summary>📷 Visual Reference</summary>

<Background>
![](https://assets.apidog.com/uploads/help/2023/07/12/c866a5e3f67e77ddc63da497918ca382.png)
</Background>

</details>

## Cloning the Project

To clone a project from current team to another team, click **Settings** → **Basic Settings** → **Clone Project**.

<details>
<summary>📷 Visual Reference</summary>

<Background>
![](https://assets.apidog.com/uploads/help/2023/07/12/3db0a24d97575540db24c13c9971b4a0.png)
</Background>

</details>

## Moving the Project

To move a project to another team, click **Settings** → **Basic Settings** → **Move Project**.

<details>
<summary>📷 Visual Reference</summary>

<Background>
![](https://assets.apidog.com/uploads/help/2023/07/12/b5e319f64db87b289db40d66fc7dfb52.png)
</Background>

</details>

## Deleting the Project

To delete a project completely, go to **Settings** → **Basic Settings** → **Delete**.

<details>
<summary>📷 Visual Reference</summary>

<Background>
![](https://assets.apidog.com/uploads/help/2023/07/12/0615592337bee8bded01b7dccf88a994.png)
</Background>

</details>

:::danger
You must be cautious - projects deleted will not be retrievable.
:::

