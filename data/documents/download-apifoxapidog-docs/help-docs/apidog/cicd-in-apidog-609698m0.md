# CI/CD in Apidog

Continuous integration and continuous delivery (CI/CD) are essential components of an API development workflow. Apidog provides integration with widely-used CI tools, enabling you to monitor API builds directly within the same platform where you design and test your APIs.

You can execute API test scenarios created in Apidog as part of your CI pipeline using the Apidog CLI.

## Getting Started

<Video src="https://www.youtube.com/watch?v=8i0fXbj5mag"></Video>

<Steps>
  <Step>
[Orchestrate test scenarios](https://docs.apidog.com/create-a-test-scenario-599311m0.md) and debug them until they pass.
    </Step>
  <Step>
Switch to the CI/CD tab, set up environment parameters, test data, and other necessary configurations.

:::highlight purple
Learn more about [configurations of Apidog CLI](https://docs.apidog.com/installing-and-running-apidog-cli-605135m0.md).
:::
    </Step>
  <Step>
Choose your CI/CD platform, and copy the corresponding commands to configure in your CI/CD platform.
      
<Background>
![CI/CD platform selection interface showing various integration options](https://api.apidog.com/api/v1/projects/544525/resources/343415/image-preview)
</Background>
    </Step>
  <Step>
Run the pipeline and get the result in your CI/CD platform.
    </Step>
</Steps>

## CI/CD Platforms Supported

Apidog supports various CI/CD platforms, including:

- **[Github Actions](https://docs.apidog.com/integrate-with-github-actions-1205646m0.md)**
- **[GitLab CI/CD](https://docs.apidog.com/integrate-with-gitlab-609931m0.md)**
- **[Jenkins](https://docs.apidog.com/integrate-with-jenkins-609705m0.md)**
- **Azure Pipelines**
- **Bitbucket Pipelines**
- **CircleCI**
- **Travis CI**
- **[Trigger Test by Git Commit](https://docs.apidog.com/trigger-test-by-git-commit-1210125m0.md)**

If your CI/CD platform is not listed above, you can still configure your CI/CD using the code provided in the "Command Line" option.

