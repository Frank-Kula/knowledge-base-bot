# Run Test Suites Locally

## Selecting A Suitable Running Method

Apidog provides multiple ways to run test suites, suitable for different testing requirements.

1. **Local Visual Execution**: 

- This method is initiated from a local machine and is suitable for small-scale, quick testing.
- It is particularly effective when development and testing occur simultaneously, allowing for real-time monitoring and immediate adjustments.

2. **Local [Apidog CLI](https://docs.apidog.com/introduction-to-apidog-cli-605134m0.md) execution**:

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

## Execution Configuration in Test Suite

When running test suites in Apidog, you can configure multiple settings and options to run tests according to specific requirements.


<Background>

![image.png](https://api.apidog.com/api/v1/projects/544525/resources/372738/image-preview)
</Background>

### General Configuration

You can adjust the following settings in the run configuration on the right side of the test suite:

- **Environment**

  Specify the service (base URL) to which requests in the scenario should be directed and the variable set to be used. For details, see [Environment Management](https://docs.apidog.com/environment-management-584758m0.md).

- **Run Mode** 

  Test suites support two run modes:

  - **Serial:** Executes test scenarios one by one in order. Suitable for scenarios with dependencies or resource-constrained environments.
  
  - **Parallel:** Executes multiple test scenarios simultaneously. The system automatically determines the optimal concurrency based on available machine resources. Suitable for large-scale regression testing to significantly shorten execution time.

- **Run On**

  The machine that actually consumes hardware resources to run test suites. All requests initiated in the test suites will be sent from the machine specified here. Therefore, differences in the network environment of the requesting machine may lead to varying test results.
  
    :::caution[]
    This setting will not be saved as part of the test suite's run configuration. Each time, the local machine will be used by default to run the test suites. Additionally, this setting will not take effect during batch runs or CLI executions. In these cases, requests will be initiated using the resources of the current machine.
    :::
    
When specifying a machine to run test suites, if the test suite involves files (such as files sending, database connections, external programs, SSL certificates, etc.), all required files must be stored locally on the specified machine for proper functionality.

- **Notification**
  
  Enabling this feature will send notifications to specified recipients once the manual test suites is complete. The notification will include an overview of the test results and a link to the detailed report. You can configure whether to send the notification as soon as the test completes or only when a failure occurs, helping to minimize unnecessary alerts. Refer to [notification settings](https://docs.apidog.com/notification-settings-616240m0.md) for more detailed information.
  
## Parallel Run

When the number of scenarios in a test suite grows to hundreds, serial run becomes a bottleneck. A full regression test that takes an hour can delay releases and slow down incident detection.

Switching the run mode to "Parallel" allows the system to execute multiple scenarios at once. The concurrency is managed automatically based on machine resources. A test that originally took 60 minutes can be shortened to under 30 minutes without modifying any test logic.

<Background>
![test-suite-parallel-run.gif](https://api.apidog.com/api/v1/projects/544525/resources/372722/image-preview)
</Background>

### Dependency Isolation

During parallel run, each test scenario runs in an independent context to ensure:

- Shared variables in one scenario do not affect others.
  
- Environmental states do not interfere between scenarios.


:::tip[]
If there are actual dependencies between scenarios (e.g., Scenario B needs data created by Scenario A), it is recommended to merge them into a single test scenario and use sequential steps to orchestrate the execution order.
:::
  
  
