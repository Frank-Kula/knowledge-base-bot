# Orchestrate Test Suite

After creating a test suite, you need to add test content. Apidog provides flexible "Static" and "Dynamic" modes to meet different test management needs.

## Importing Test Content

In the test suite details page under the `Orchestration` tab, click `+ Add Endpoint Test Case` or `+ Add Test Scenario`. In the popup selection window, you can switch between `Static` or `Dynamic` mode.

<Background>
![image.png](https://api.apidog.com/api/v1/projects/544525/resources/369682/image-preview)
</Background>

### 1. Static Mode

Static mode is used to precisely specify the test items to be executed.

**🎯 Core Logic**

The system records the specific test cases' IDs you select. Even if new test cases are added to the source category,  the execution scope of this suite will not change, ensuring controllability of test results.

**🚀 Best Use Scenarios**
- **Bug Fix Verification (Hotfix)**: Select 3-5 test cases strongly related to the bug, form a "verification package", quickly verify the fix result, without wasting time running unrelated cases.
- **Core Business Stabilization (Core Path)**: For extremely core and stable processes like "order-payment". We don't want monitoring alerts triggered because a newcomer accidentally added an incomplete test case.
- **Old Version Compatibility Testing**: Select a batch of old endpoint test cases specifically for verifying old version client compatibility.

**⚠️ Maintenance Characteristics**
- **High Maintenance Cost**: If new cases need to be included in this specialized test, they must be manually added.

### 2. Dynamic Mode

Dynamic mode is used to automatically filter test items to be executed through rules.

**🎯 Core Logic**

The system saves **"Filter Rules" (Scope & Filter)**. Each time it runs, the system scans the entire project in real time and includes all the latest cases that meet the criteria into the execution plan.

**🚀 Best Use Scenarios**
- **Module-Level Regression Test**: Set the "Trading Center" folder as the source folder. Testers only need to write new cases in the folder, and the suite will automatically include them when running.
- **Smoke Test**: Create a dynamic suite with the rule `Priority = P0`. Run before each release to automatically cover all key cases marked as P0.
- **Version Iteration Verification**: Use the tag feature, set the rule to `Tag = v2.5.0`. After development is complete, run this suite to verify all new features for this version.

**⚠️ Maintenance Characteristics**
- **Zero Maintenance Cost**: Once the rules are configured, there is no need to maintain the suite itself afterwards, only maintain the case attributes (location, tags, priority).

## Adjust Execution Order

Imported content will be displayed in a list, and you can **drag** the list items to adjust the execution order.

For items added "statically", you can use `Edit` to delete test cases individually or delete the entire group.

<Background>
![image.png](https://api.apidog.com/api/v1/projects/544525/resources/369683/image-preview)
</Background>

For groups added "dynamically", you can only delete the entire group or edit filter criteria, and cannot delete individual items within the group.

<Background>
![image.png](https://api.apidog.com/api/v1/projects/544525/resources/369685/image-preview)
</Background>


## Advanced Config

On the right side of the test suite design page, you can expand `Advanced Config` to have more granular control over how the test suite runs.

<Background>
![image.png](https://api.apidog.com/api/v1/projects/544525/resources/369724/image-preview)

![image.png](https://api.apidog.com/api/v1/projects/544525/resources/369723/image-preview)
</Background>

### Environment

- **Definition**: By default, inherits the run environment already set in the test suite. If an environment is specified here, that environment configuration will take priority during execution.

- **Use Case**: Suitable for scenarios where you need to reuse the same set of test steps in different environments.

### Test Data

Used to specify whether to use test data during execution.

- **No Test Data**: Test steps execute only once, not running [data-driven testing](https://docs.apidog.com/data-driven-testing-602987m0.md).

- **Use Test Data**: Run multiple times based on test data, commonly used for parameterized testing.

### On Error

Configure how the test should handle errors, which can include assertion failures, data format validation failures, endpoint request exceptions, server errors, etc.

- **Ignore**: Continue executing subsequent steps when an error occurs, without interrupting the current run.

- **Continue**: When an error occurs, skip the remaining steps of the current round and directly enter the next execution round.

- **End execution**: Immediately terminate subsequent steps once an error occurs.

### Iterations

- **Definition**: The number of times each thread loops through all steps.
- **Use Case**: Commonly used for stability verification or simple stress testing scenarios.

### Delay

- **Definition**: Set how many milliseconds (ms) to wait after each test step completes before executing the next step.
- **Use Case**: Prevent triggering rate-limiting or circuit breaker mechanisms on the target server due to high request frequency, ensuring smooth test execution.

### Save Request/Responses

- **Definition**: Control whether the test report includes detailed data of requests and responses (such as Header, Body, etc.).

- **Options**:
    - **All:** Save complete details of all steps regardless of pass/fail. Large data volume, suitable for deep debugging.
    - **Only Failed:** Only save details for steps that failed during execution. Recommended, saves storage space and facilitates quick identification of failure reasons.
    - **Do Not Save:** Do not save any details; only record pass/fail status and duration.

### Environment/Global Variable Values
  - Environment/Global variable values specify which actual values to use for environment/global variables in this test scenario. There are two choices. Detailed information can be [viewed here](https://docs.apidog.com/run-a-test-scenario-602063m0#rules-for-using-environmentglobal-variables-across-different-running-methods). When choosing to use variable values saved in Runner, you will be required to further select the variable scope to use.
  
    The purpose of this scope is to help users better separate variables according to actual needs, avoiding situations where one scheduled task run causes other tasks to fail due to variable changes. After selecting the scope, you can also view the variable values within this scope through the entry that appears in the product interface.

<table>
  <thead>
    <tr>
      <th>Variable Scope in Runner</th>
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
        The smallest variable scope with minimal impact. Suitable for cases where the results of the previous run of this test scenario need to be used in the next run.
 Variable files for test scenarios, tasks, and task folders are all saved in the Runner container path `/opt/runner/variables`.
          <span style="color: gray; font-size: 14px;display: inline-block; width: 250px;"></span>
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
          <li>In the current specified Runner, the scheduled task folder has a file to store environment/global variables that can be used across all its scheduled tasks and test scenarios.</li>
          <li>All test scenarios in all scheduled tasks within the current folder can read and write variables in this file.</li>
        </ul>
      </td>
      <td>
        The largest variable scope with the most significant impact. It is possible that running a certain scheduled task modifies the variable value, leading to the failure of other scheduled tasks.  Suitable when data needs to be shared across multiple tasks in the same folder.
      </td>
    </tr>
  </tbody>
</table>
