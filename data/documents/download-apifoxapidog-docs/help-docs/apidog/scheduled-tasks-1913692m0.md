# Scheduled tasks

# Scheduled tasks

Test suites support setting up scheduled tasks to achieve unattended automated monitoring.

## Create a scheduled task

Enter the test suite's `Scheduled Tasks` tab and click `+ New`.

- **Run Cycle**: Set a schedule for the task, such as every Sunday at 11 PM or every 6 hours.
- **Run On**: The machine that actually consumes hardware resources to run the test suite. All requests initiated in the test suite will be sent from the machine specified here, so different test results may occur due to different network environments of the requesting machine.
- **Notification**: When the task fails (or completes), send notifications through third-party integrations (such as Slack, Teams, Webhook, Jenkins, Email).

<Background>
![image.png](https://api.apidog.com/api/v1/projects/544525/resources/369741/image-preview)
</Background>

## Scheduled tasks list

In the `Tests` folder tree, the `Scheduled Tasks` section displays all scheduled tasks created across all test suites in the current project. From this list, you can easily view and manage tasks, including enabling or disabling them.

<Background>

![image.png](https://api.apidog.com/api/v1/projects/544525/resources/369754/image-preview)
</Background>


## Run Scheduled Tasks

Once a scheduled task is completed, its results are automatically uploaded from the Runner to the server. You can access all the detailed results of schedule tasks in the "Scheduled Tasks - Run History" within the Apidog client.

:::tip[]
It is recommended to enable notifications for scheduled tasks. This allows you to receive notification messages immediately when the test execution is completed, ensuring you can promptly review the results.
:::
