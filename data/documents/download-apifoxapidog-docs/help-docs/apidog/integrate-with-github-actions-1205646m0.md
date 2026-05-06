# Integrate with Github Actions

Apidog supports running automated tests in any CI/CD pipeline through a simple CLI command. Whether you're using GitHub Actions, GitLab CI, Jenkins, or a custom webhook handler, you can trigger Apidog tests automatically whenever your Git repository is updated.

### Prerequisites

- A GitHub account and repository
- An Apidog account with test scenarios created
- Access to generate Apidog access tokens

## How It Works

The integration is based on a simple principle: Git Webhook + CLI Execution.

When a Git event (like a push or pull request) occurs, your CI/CD tool receives the event and runs the apidog run command to execute your test scenarios.

This guide uses GitHub Actions as an example—because it's widely used and requires no additional infrastructure. But the same approach applies to other platforms.

This setup is ideal for:

- Automatically running API tests on every push or pull request

- Monitoring specific branches (e.g. main, develop)

- Supporting pre-deployment checks and regression testing

- Ensuring consistent test execution in your CI workflows

Now let's walk through the setup using GitHub Actions.



## Step 1: Initialize a GitHub Workflow

1. Go to [GitHub](https://github.com/) and log in to your account.
2. Navigate to your target repository.
3. Click on the **"Actions"** tab in the top navigation bar.
4. If this is your first time setting up Actions in the repo, click **"New workflow"** to create one.

<Background>
![GitHub Actions tab showing the new workflow button](https://api.apidog.com/api/v1/projects/544525/resources/357058/image-preview)
</Background>
    
<Background>
![GitHub workflow creation interface](https://api.apidog.com/api/v1/projects/544525/resources/357057/image-preview)
</Background>



## Step 2: Generate GitHub Actions Configuration in Apidog

1. In Apidog, open your project and go to the **"Tests"** page.
2. Switch to the **"CI/CD"** tab.
3. Configure the test environment, decide whether to enable test data, and set the loop count and delay interval. 
4. Select **"GitHub Actions"**, then click **"Copy"**.

<Background>
![Apidog CI/CD configuration tab with GitHub Actions selected](https://api.apidog.com/api/v1/projects/544525/resources/357055/image-preview)
</Background>



## Step 3: Paste and Commit the Workflow in GitHub

1. Return to your GitHub repository and open the **Actions** page.
2. Create a new workflow and paste the configuration code copied from Apidog.
3. If you already have an existing CI pipeline, you can merge the Apidog test configuration into it.
4. Click **"Commit changes"** to save and enable the workflow.

<Background>
![GitHub workflow editor with Apidog configuration pasted](https://api.apidog.com/api/v1/projects/544525/resources/357062/image-preview)
</Background>

:::tip[]
Please make sure to replace the variable `$APIDOG_ACCESS_TOKEN` in the code with your actual [Access Token](https://docs.apidog.com/api-access-token.md).
:::

The workflow file will be saved in your repository under `.github/workflows/`.
It is part of your source code and will be included when you clone or pull the project locally.You can edit it in your local development environment and commit changes through Git like any other file.

<Background>
![GitHub repository file structure showing the workflows directory](https://api.apidog.com/api/v1/projects/544525/resources/357060/image-preview)
</Background>

The top of the workflow file contains a line like:

```yaml
on: [push, pull_request]
```
This tells GitHub to automatically trigger the workflow whenever someone pushes code or opens/updates a pull request.It's a shorthand syntax equivalent to a more verbose version, and works well for most CI scenarios.

If you want to customize which branches or events should trigger the workflow, you can refer to the official documentation:
👉 [GitHub Actions: Events that trigger workflows](https://docs.github.com/en/actions/writing-workflows/choosing-when-your-workflow-runs/events-that-trigger-workflows)


## Step 4: Run the Workflow and View Results

Once configured, the GitHub Actions workflow will automatically run whenever there is a new code commit. You can monitor the workflow's status and test results on the **Actions** page.

<Background>
![GitHub Actions execution results showing test status](https://api.apidog.com/api/v1/projects/544525/resources/357061/image-preview)
</Background>

