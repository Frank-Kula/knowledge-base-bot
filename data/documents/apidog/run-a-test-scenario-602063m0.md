# Run a Test Scenario

Once you have constructed the test scenario, you can run it to generate a test report.

## Selecting Suitable Running Method

Apidog provides multiple ways to run test scenarios, suitable for different testing requirements.

1. **Local visual execution**: 

This method is initiated from a local machine and is suitable for small-scale, quick testing. It is particularly effective when development and testing occur simultaneously, allowing for real-time monitoring and immediate adjustments.

2. **Local [Apidog CLI](https://docs.apidog.com/introduction-to-apidog-cli-605134m0.md) execution**:

Ideal for handling large-scale data or iterative scenarios, this method offers increased execution speed. It is capable of running offline, which is suitable for environments with restricted resources or those that do not require a graphical user interface.

3. **CI/CD execution**:

This execution style is integrated within the CI/CD pipeline, making it a great option for automated integration and continuous deployment processes. It is especially useful in settings where tests are frequently run to confirm the stability of APIs after each code update.

4. **Self-hosting runner execution**: 

Teams can set up the Apidog Runner on their own servers, leveraging more robust computing resources for testing. This method includes support for scheduled tasks, making it ideal for scenarios that need regular testing or those with significant testing demands.

:::tip
In test scenarios, if environment/global variables are used, the actual values of these variables may differ depending on the execution method chosen, which could lead to inconsistent test results. [Learn more](https://docs.apidog.com/run-a-test-scenario-602063m0.md#rules-for-using-environmentglobal-variables-across-different-running-methods).
:::

Let's start with the local visual execution.

## Getting started

<Steps>
  <Step>
Go to the desired test scenario and select the environment in which you want the requests to run.

<Background>
![Test scenario environment selection interface](https://api.apidog.com/api/v1/projects/544525/resources/343053/image-preview)
</Background>

  </Step>
  <Step>
Click on "Run".
  </Step>
  <Step>
You will see a test report displaying information such as pass rate, execution time, and other data for the current run. You can expand each request to view validations and assertions.

<Background>
![Test report showing pass rate and execution time](https://api.apidog.com/api/v1/projects/544525/resources/343052/image-preview)
</Background>
  </Step>
  <Step>
Click on "more" to inspect the actual request and response details.

<Background>
![Request and response details view](https://api.apidog.com/api/v1/projects/544525/resources/343054/image-preview)
</Background>

:::highlight purple 
Learn more about [test reports](https://docs.apidog.com/test-reports-603898m0.md).
:::
  </Step>
</Steps>

## Run options in test scenarios

When running a test scenario in Apidog, several settings and options can be configured to tailor the test execution to specific requirements. 

<Background>
![Test scenario run options and settings interface](https://api.apidog.com/api/v1/projects/544525/resources/349844/image-preview)
</Background>

Below, we explore the critical aspects of these settings:

### Environment
Specify the service (base URL) to which requests in the scenario should be directed and the variable set to be used. Learn more details at [environments & services](https://docs.apidog.com/environment-management-584758m0.md).

Note that **custom requests** have their own full URL and will **NOT** be directed to the environment set in this context, unlike imported steps.

### Test data
The test scenario supports importing external test data sets. When the test scenario runs, the system will loop through all data sets in the data file and assign the data in the data sets to the corresponding variables, see [data-driven testing](https://docs.apidog.com/data-driven-testing-602987m0.md) for details.

### Iterations
Configure the number of times all steps within the scenario will be executed in a loop. 

If there's a significant amount of data to process, it's recommended to use the Apidog CLI for execution instead of the Apidog client to optimize performance.

### Threads
Execute all steps in multiple threads where data between threads remains isolated to prevent interference. 

Note that this feature is in Beta and may require further performance optimization. For rigorous load testing, it is advised to use the Performance test functionality instead. 
Threads are not supported in the CLI.

### Runs on

The machine that actually consumes hardware resources to run test scenarios. All requests initiated in the test scenarios will be sent from the machine specified here. Therefore, differences in the network environment of the requesting machine may lead to varying test results.

:::note
This setting will not be saved as part of the test scenario's run configuration. Each time, the local machine will be used by default to run the test scenarios. Additionally, this setting will not take effect during batch runs or CLI executions. In these cases, requests will be initiated using the resources of the current machine.
:::

When specifying a machine to run test scenarios, if the test scenario involves files (such as files sending, database connections, external programs, SSL certificates, etc.), all required files must be stored locally on the specified machine for proper functionality.

### Notifications

Enabling this feature will send notifications to specified recipients once the manual test scenario is complete. The notification will include an overview of the test results and a link to the detailed report. You can configure whether to send the notification as soon as the test finishes or only when a failure occurs, helping to minimize unnecessary alerts. Refer to [notification settings](https://docs.apidog.com/notification-settings-616240m0.md) for more detailed information.

### Shared

By enabling the "Share" option on the right side of the`Advanced Settings`, the test report generated after each test scenario run will be automatically shared with other members of the project. You can view all test reports that have been shared within the team under the`Shared`tab in the`Test Reports`section. Refer to [test reports](https://docs.apidog.com/test-reports-603898m0.md) for more details.

If the current test scenario includes steps with endpoints imported from other projects, you can refer to this guide: [Manage the runtime environment of APIs from other projects](https://docs.apidog.com/manage-runtime-environment-of-apis-from-other-projects-603705m0.md)

## Advanced settings
<Background>
![Advanced settings panel for test scenarios](https://api.apidog.com/api/v1/projects/544525/resources/343100/image-preview)
</Background>

### On error
Configure how the test should handle errors, which can include assertion failures, data format validation failures, server errors, etc. The options are:
- **Ignore**: Continue executing the next step when an error occurs (default setting).
- **Continue**: End the current iteration and start the next one when an error occurs.
- **End execution**: Stop the entire run when an error is encountered.

### Delay
Set a pause between sending each step to manage and control the execution speed.

### Save request/responses
By default, Apidog saves every request and response. In cases where requests or responses are significantly large (potentially several MBs), they might take up considerable disk space. You can enable this option to not save every request and response but only save assertion and validation results. 

Alternatively, you can choose to save only failed requests and responses to conserve space.

### Keep variable values
This option is enabled by default, ensuring that the current value of **global** and **environment** variables, when modified during the test, retains the last modified result. If this option is disabled, global and environment variables will not change after the test run; they will retain the value they had before the run. 

Local variables are not affected by this setting and will be cleared after each run.

### Run with stored cookies
In the lower right corner of Apidog, the <Icon icon="material-outline-cookie"/> Cookies icon leads to cookie management. Apidog automatically saves cookies when making API requests. If you want to use the saved cookies during test scenario execution, enable this option.

### Save cookies after run
Similar to above, if you wish to update the saved cookies after executing a test scenario, enable this option.

By configuring these advanced settings in Apidog, you can fine-tune your test executions to meet your specific testing needs, ensuring efficient and precise test runs.

## Runtime settings under test scenario design mode

If you are in the test scenario design mode, the relevant runtime configurations are collapsed to the right side of the "Run" button. Hover the mouse over this settings button to see the detailed runtime configurations for this test scenario.

<Background>
![Runtime configuration settings in design mode](https://api.apidog.com/api/v1/projects/544525/resources/343417/image-preview)
</Background>

## Running Functional Tests

After running functional tests, you will be directed to the test scenario execution page. The pie chart in the image below provides an overview of the test results, updating in real-time as the test scenario runs. Below the pie chart, you’ll find the detailed test steps being executed, with the status of each step displayed during the run.

<Background>
![Functional test execution page with real-time results](https://api.apidog.com/api/v1/projects/544525/resources/349845/image-preview)
</Background>

Once the functional test run is complete, you can click on the relevant endpint to view its metrics and status during the test. This includes the endpoint name, request method, request URL, response status code, response time, response content, data validation, and assertion results. For more details, please refer to [test reports](https://docs.apidog.com/test-reports-603898m0.md).

## Rules for using environment/global variables across different running methods

Environment and global variables are persistent, meaning they can be saved for long-term use across multiple runs or different test scenarios. However, the actual variable values used may vary depending on the selected running method. For example:

*If a test scenario uses an environment variable`Token`, it might run successfully when executed within the client, but fail when run using a self-hosted Runner because the value of the `Token` is incorrect.*

This discrepancy can occur because the actual value of the environment variable `Token` is taken from the locally stored value within the client during execution. However, when running in a self-hosted Runner, the Runner does not have the same locally stored `Token`, leading to a failure.

To address this issue, Apidog provides a set of rules for managing values of the environment/global variable across different run methods:

<table>
  <thead>
    <tr>
      <th>Running Method</th>
      <th>Environment/Global Variable Usage</th>
      <th>Variable Storage Location</th>
    </tr>
  </thead>
  <tbody>
    <!-- Local Execution -->
    <tr>
      <td>Local (Client, Web)</td>
      <td>Uses the <a href="https://docs.apidog.com/using-variables-577908m0.md#initial-and-current-values">current values</a> of the environment/global variables for execution.</td>
      <td>Stored locally. Can be manually modified or updated through pre/post processors. Visible in the <em>Environment Management > Environment/Global Variables > Current Values</em>.</td>
    </tr>
    <!-- CLI, CI/CD Execution -->
    <tr>
      <td>CLI, CI/CD</td>
      <td>
        For real-time online execution:
        <ol>
          <li>Uses the <a href="https://docs.apidog.com/using-variables-577908m0.md#initial-and-current-values">initial values</a> of the environment/global variables for execution **(default)**.</li>
          <li>Specify the use of environment/global variable values stored in a file on the machine running the test scenario via the <code>--variables path</code> option. <span>[Learn more](https://docs.apidog.com/installing-and-running-apidog-cli-605135m0.md#run-online-data-in-real-time)</span>.</li>
        </ol>
        For execution with exported data:
        <ol start="3">
          <li>Uses the environment/global variable values included in the exported file for execution.</li>
        </ol>
      </td>
      <td>
        <ol>
          <li>Initial values are stored in Apidog Cloud and can only be modified manually within the client.</li>
          <li>Stored in the file specified by the <code>--variables path</code> option, allowing manual modification or updates through pre/post processors.</li>
          <li>Stored in the exported file. Can be manually modified or updated through pre/post processors.</li>
        </ol>
      </td>
    </tr>
    <!-- Self-hosted Runner Execution -->
    <tr>
      <td>Self-hosted Runner</td>
      <td>
        <ol>
          <li>Uses the <a href="https://docs.apidog.com/using-variables-577908m0.md#initial-and-current-values">initial values</a> of the environment/global variables for execution **(default)**.</li>
          <li>Uses the locally stored values within the Runner for execution.<span> [Learn more](https://docs.apidog.com/scheduled-tasks-603702m0.md#scheduled-task-details)</span>.</li>
        </ol>
      </td>
      <td>
        <ol>
          <li>Initial values are stored in Apidog Cloud and can only be modified manually within the client.</li>
          <li>Stored within the specified Runner. Can be manually modified or updated through pre/post processors. Visible through the product user interface or in the file within the Runner at <code>/opt/runner/variables</code>.</li>
        </ol>
      </td>
    </tr>
  </tbody>
</table>

## Running test scenarios with endpoints from other projects

When a test scenario includes endpoints imported from other projects, the request URLs for these endpoints during execution are determined by the configuration you set in the`Environment associations`.

For example:

If the "Develop Env" of the current project is associated with the "Prod Env" of another project, When running the test scenario using "Develop Env", the imported endpoint will be sent to the URL from the "Prod Env". All other endpoints will use the URL from the "Develop Env" of the current project.

<Background>
![Environment association configuration for cross-project endpoints](https://api.apidog.com/api/v1/projects/544525/resources/349847/image-preview)
</Background>

## Implementing various tests

The mentioned steps represent the basic execution of a test scenario. When setting up test scenarios, you can incorporate various advanced settings to fulfill diverse testing requirements.

- **[Data-driven testing](https://docs.apidog.com/data-driven-testing-602987m0.md):** Conduct tests using diverse data sets to validate system behavior across various scenarios.
- **[Performance testing](https://docs.apidog.com/performance-testing-603638m0.md):** Evaluate system performance under varying load conditions to assess scalability and responsiveness.
- **[Scheduled tasks](https://docs.apidog.com/scheduled-tasks-603702m0.md):** Establish structured plans detailing scope, approach, and timing of testing activities.
- **[CI/CD integration](https://docs.apidog.com/cicd-in-apidog-609698m0.md):** Automate build, test, and deployment processes to ensure reliable and frequent software releases.
