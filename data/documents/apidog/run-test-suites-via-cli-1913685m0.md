# Run Test Suites Via CLI

## Selecting A Suitable Running Method

Apidog provides multiple ways to run test suites, suitable for different testing requirements.

1. **Local Visual Execution**:

- This method is initiated from a local machine and is suitable for small-scale, quick testing.
- It is particularly effective when development and testing occur simultaneously, allowing for real-time monitoring and immediate adjustments.

2. **Local [Apidog CLI](https://docs.apidog.com/introduction-to-apidog-cli-605134m0.md) Execution**:

- Ideal for handling large-scale data or iterative scenarios, this method offers increased execution speed. 
- It is capable of running offline, which is suitable for environments with restricted resources or those that do not require a graphical user interface.

3. **CI/CD Execution**:

- This execution style is integrated within the CI/CD pipeline, making it a great option for automated integration and continuous deployment processes. 
- It is especially useful in settings where tests are frequently run to confirm the stability of APIs after each code update.

4. **Self-Hosting Runner Execution**: 

- Teams can set up the Apidog Runner on their own servers, leveraging more robust computing resources for testing. 
- This method includes support for scheduled tasks, making it ideal for scenarios that need regular testing or those with significant testing demands.

:::tip
In test suites, if environment/global variables are used, the actual values of these variables may differ depending on the execution method chosen, which could lead to inconsistent test results. [Learn more](https://docs.apidog.com/run-a-test-scenario-602063m0#rules-for-using-environmentglobal-variables-across-different-running-methods).
:::

## Running Apidog CLI

To run test suites using the [Apidog CLI](https://docs.apidog.com/introduction-to-apidog-cli-605134m0.md), you first need to create and orchestrate a test suite. Then, you can run the test suite from the command line using the Apidog CLI and get the test results and test report.

<Steps>
  <Step>
In a test suite, switch to the CI/CD tab.

<Background>
![](https://api.apidog.com/api/v1/projects/544525/resources/369743/image-preview)
</Background>

  </Step>
  <Step>
Configure parameters such as run environment and notification method. Each configuration in the interface will be reflected in real-time in the CLI command generated below.
  </Step>
  <Step>
In the CI/CD provider section, select CLI command line or other platforms.
  </Step>
  <Step>
Click the "Add access token" button and then "Generate token"  for CLI call authentication. [Learn more](https://docs.apidog.com/api-access-token.md).

  </Step>
  <Step>
Click to copy the command, paste it into the command line and execute it to see the test execution process and test report.

<Background>
![CleanShot 2026-01-13 at 15.48.13@2x.png](https://api.apidog.com/api/v1/projects/544525/resources/369750/image-preview)
</Background>


:::tip[]
Note: For the command to run successfully, you need to first install [Apidog CLI](https://docs.apidog.com/installing-and-running-apidog-cli-605135m0.md). If already installed, you need to update it to the latest version.
:::
  </Step>
</Steps>

## About Variables and Local Configuration Files (Optional)

In some scenarios, CLI execution requires local configuration files:

- **Environment / Global Variables**

    If you choose "Export current values for use", you need to place the exported variable file in the CLI execution machine and specify the file path through `--variables <path>`.
    
    For the difference between "Use initial Values" and "Export current values for use", refer to: [Rules for using environment/global variables across different running methods](https://docs.apidog.com/run-a-test-scenario-602063m0#rules-for-using-environmentglobal-variables-across-different-running-methods).

- **Database Connection**

    If the test uses locally saved "database connections", the interface will guide you to export the configuration file and use it in CLI through `--database-connection <path>`.

    :::tip[]
    It is recommended to save "database connection" details in variable form, so that no additional `--database-connection <path>` is needed when running CLI, and it is also more convenient for collaboration and maintenance.  [Learn more](https://docs.apidog.com/database-connection-880098m0.md).
    :::


## CLI Test Report

After running the CLI, you will get a command-line test report containing the execution statistics of the test suite, as well as validation and assertion information for failed requests.


<Background>

![CleanShot 2026-01-13 at 15.52.03@2x.png](https://api.apidog.com/api/v1/projects/544525/resources/369752/image-preview)

</Background>


In the folder where the CLI is run, you can also find the `/apidog-reports/` folder, which contains HTML-formatted CLI test reports.


<Background>
<img src="https://api.apidog.com/api/v1/projects/544525/resources/369753/image-preview" style="width:540px"/>
</Background>


## Command Options

Apidog CLI provides rich configuration options to customize the execution of test suites. For details, see [CLI Command Options](https://docs.apidog.com/apidog-cli-options-609656m0.md).

## Using Apidog CLI in CI/CD

Apidog CLI supports integration with various pipeline tools such as Jenkins, GitLab, GitHub Actions, etc. To learn more, see [CI/CD Integration](https://docs.apidog.com/cicd-in-apidog-609698m0.md).
