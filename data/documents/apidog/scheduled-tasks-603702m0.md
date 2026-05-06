# Scheduled Tasks

You can set up "Scheduled Tasks" to automatically run configured automated test scenarios at specified times, obtain task execution results, and meet the requirements for scheduled testing and regression.

:::tip[]
- Scheduled tasks is in Beta right now.
- To run scheduled tasks, you first need to configure a [Self-hosted Runner](https://docs.apidog.com/self-hosted-runner-755230m0.md).
- The number of times you can run scheduled tasks depends on the plan you have subscribed to. You can find the details on the [Apidog pricing page](https://apidog.com/pricing/).
:::

## Accessing the scheduled tasks

To access the "Scheduled Tasks", navigate to the Tests module and click on "Scheduled Tasks." Here, you can find that all the scheduled tasks are organized in a clear, structure folder format.

<Background>
![accessing-scheduled-tasks-apidog.png](https://api.apidog.com/api/v1/projects/544525/resources/349856/image-preview)
</Background>

You can easily create new scheduled tasks or folders to group tasks within the folder tree.

<Background>
![scheduled-tasks-creation-settings.png](https://api.apidog.com/api/v1/projects/544525/resources/349859/image-preview)
</Background>

Additionally, you can perform actions like editing or deleting specific tasks or folders.

<Background>
![editting-scheduled-tasks.png](https://api.apidog.com/api/v1/projects/544525/resources/349860/image-preview)
</Background>

Clicking on `Scheduled Tasks` will display a list of all tasks on the right-hand side. This list includes basic details and management options, providing a more streamlined way to handle your tasks.

<Background>
![checking-all-scheduled-tasks.png](https://api.apidog.com/api/v1/projects/544525/resources/349861/image-preview)
</Background>

## Scheduled task details

Clicking on an existing scheduled task or creating a new one will open task details on the right.

<Background>
![configuring-scheduled-tasks-settings.png](https://api.apidog.com/api/v1/projects/544525/resources/349862/image-preview)
</Background>

In the scheduled task details, you can configure the following settings:

- **Task Name and Description:** Used to distinguish the scheduled task and describe its purpose in detail.
- **Enable/Disable:** Use the toggle switch to activate or deactivate the scheduled task as needed.
- **Test Scenarios:** Choose one or more test scenarios for the scheduled task to execute. Each test scenario can be expanded to configure its runtime settings independently.
  - `Environment`, `test data`, `iterations`, `delay`, and `saving requests/responses` are standard runtime configurations.[ Learn more about these settings here](https://docs.apidog.com/run-a-test-scenario-602063m0.md#run-options-in-test-scenarios).
  - **Environment/Global Variable Value:** Specify the actual values of the environment or global variables used in this test scenario. There are two options, and [detailed explanations can be found here](https://docs.apidog.com/run-a-test-scenario-602063m0.md#rules-for-using-environmentglobal-variables-across-different-running-methods). When selecting to use variables saved in the Runner, you will need to further define the variable scope. This helps segment variables based on actual needs and prevents task failures caused by variable conflicts during execution. Once the scope is defined, you can `check the current test scenario variables stored in Runner` visually in the user interface.

<Background>
![scheduled-tasks-test-scenatrio-settings.png](https://api.apidog.com/api/v1/projects/544525/resources/349863/image-preview)
</Background>

Here are three options to define the environment/global variable scope:

<Background>
![environment-global-variable-scope.jpg](https://api.apidog.com/api/v1/projects/544525/resources/349865/image-preview)
</Background>

<table>
  <thead>
    <tr>
      <th>Environment/Global Variable Scope</th>
      <th>Read/Write Environment/Global Variables</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Share only in the current test scenario<span style="color: gray; font-size: 14px;display: inline-block; width: 155px;"></span></td>
      <td>
        <ul>
          <li>In the current specified Runner, this test scenario has a dedicated file to store its environment/global variables persistently.</li>
          <li>Only the current test scenario can read and write variables in this file.</li> <span style="color: gray; font-size: 14px;display: inline-block; width: 250px;"></span> 
        </ul>
      </td>
      <td>
        The smallest variable scope with minimal impact. Suitable for cases where the results of the previous run of this test scenario need to be used in the next run.<span style="color: gray; font-size: 14px;display: inline-block; width: 250px;"></span>
      </td>
    </tr>
    <tr>
      <td>Share across all test scenarios in the current scheduled task</td>
      <td>
        <ul>
          <li>In the current specified Runner, the scheduled task has a file to store environment/global variables that can be used across all its test scenarios.</li>
          <li>All test scenarios in the current scheduled task can read and write variables in this file.</li>
        </ul>
      </td>
      <td>
        A recommended variable scope with moderate impact. Suitable for cases where data needs to be shared between different test scenarios within the same scheduled task.
      </td>
    </tr>
    <tr>
      <td>Share across all scheduled tasks in the current scheduled task folder</td>
      <td>
        <ul>
          <li>In the current specified Runner, the scheduled task folder has a file to store environment/global variables that can be used across all its schedule tasks and test scenarios.</li>
          <li>All test scenarios in all scheduled tasks within the current folder can read and write variables in this file.</li>
        </ul>
      </td>
      <td>
        The largest variable scope with the most significant impact. It is possible that running a certain scheduled task modifies the variable value, leading to the failure of other scheduled tasks.  Suitable when data needs to be shared across multiple tasks in the same folder.
      </td>
    </tr>
  </tbody>
</table>

:::tip
The`Keep variable values`option in the test scenario design page must be enabled to ensure that any changing environment/global variables set via pre/post processors during execution are saved to the specified variable scope within the Runner.
:::

- **Use same execution config:** Apply the same runtime configuration to all test scenarios within the task below.
- **Run Cycle:** Set a schedule for the task, such as every Sunday at 11 PM or every 6 hours. 
- **Runs on:** Specify where the task will run, such as via Apidog Cloud (coming soon) or a self-hosted Runner. If multiple Runners are deployed within the team, you can choose one.
- **Notification:** Enable notifications to send task results to designated recipients upon completion. Configure notifications to trigger after every run or only in case of failures, minimizing unnecessary alerts. Refer to [notification settings](https://docs.apidog.com/notification-settings-616240m0.md) for more details.


## Executing scheduled tasks

Once a scheduled task is completed, its results are automatically uploaded from the Runner to the server. You can access all the detailed results of schedule tasks in the "**Scheduled Tasks - Run History**" within the Apidog client.

<Background>
![run-history-scheduled-tasks.png](https://api.apidog.com/api/v1/projects/544525/resources/349866/image-preview)
</Background>

:::tip
It is recommended to enable notifications for scheduled tasks. This allows you to receive notification messages immediately when the test scenario is completed, ensuring you can promptly review the results.
:::
