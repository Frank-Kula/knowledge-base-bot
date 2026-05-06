# How to schedule test tasks in Apidog?

You can set up "Scheduled Tasks" to automatically run configured automated test scenarios at specified times, obtain task execution results, and meet the requirements for scheduled testing and regression.

:::tip[]
- Scheduled tasks is in Beta right now.
- To run scheduled tasks, you first need to configure a [self-hosted Runner](https://docs.apidog.com/616389m0.md).
- The number of times you can run scheduled tasks depends on the plan you have subscribed to. You can find the details on the [Apidog pricing page](https://apidog.com/pricing/).
:::

## Accessing the scheduled tasks list

To access the "Scheduled Tasks" list, navigate to the Tests module and click on "Scheduled Tasks." Here, you can view and manage all scheduled tasks for the current project. The list includes important information such as:

- **Number of Executions:** The total number of times this scheduled task has been executed.
- **Enable:** Tasks are enabled by default. If disabled, the task will no longer execute automatically.
- **Next Run Time:** The next scheduled execution time, based on the configured schedule.

![Scheduled Tasks List](https://assets.apidog.com/uploads/help/2024/06/24/ab4fff55e6fcc6242171b329d5ccbd3c.png)

## Creating a new scheduled task

When creating a new scheduled task, you need to set the following information:

- **Task Name and Description:** Used to distinguish scheduled tasks and explain the detailed purpose of the task.
- **Test Scenario:** The scheduled task will execute one or more selected test scenarios. Each scenario can have its own execution settings.
- **Run Mode:** Set the timing cycle for executing this scheduled task, such as every Sunday at 11 PM, or every 6 hours.
- **Runs On:** Specify the instance that will execute this scheduled task. It can be executed through Apidog Cloud (coming soon) or via a [self-hosted Runner](https://docs.apidog.com/616389m0.md). If the team has deployed multiple general-purpose Runners, you can choose one of them.
- **Notification:** Enable notifications to send execution results to relevant people via specified channels. For emails, project members' addresses are auto-completed, but you can also enter addresses of non-project members.

![Creating a New Scheduled Task](https://assets.apidog.com/uploads/help/2024/06/24/a7542d6b347d215df8ddb3c62416e83c.png)

## Executing scheduled tasks

Once a scheduled task is completed, notifications will be sent to relevant personnel through the specified channels, and the execution results will be saved on the task's execution results page. You can check the "Run History" page for detailed information on the scheduled tasks.

![Run History](https://assets.apidog.com/uploads/help/2024/06/24/2c174fcfb918607ec26564c0d54ca726.png)

