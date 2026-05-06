# General Runner

The Apidog Self-hosted Runner can be understood as an automated program that can be hosted on a standalone server. It can execute tasks within Apidog, such as scheduled automated tests, scheduled API document imports, and returning mock response results.

## Preparation

- The host machine (server or local PC) must have [Docker](https://www.docker.com/) installed.
- The minimum required Docker version is `20.10.0`, version `20.10.13` is recommended.

## Quick Start

This section will guide you on how to deploy General Runner on your server.

### 1. Deploy General Runner

Navigate to the **Apidog Home** page, select your desired team, and then click on **Resources** on the right. From there, click on **Deploy General Runner** to get started.

<Background>
![team-resources-general-runner.png](https://api.apidog.com/api/v1/projects/544525/resources/348516/image-preview)
</Background>


### 2. Get the Runner Deployment Command

Upon clicking the **Deploy General Runner**, copy the deployment command for the General Runner from the pop-up window. You can customize the command as needed, supporting custom server OS, exposed ports, mount data directory, and more. Below is a detailed explanation of these settings:

- **Server OS**: Specifies the operating system for the Docker container. This includes Linux, macOS, and Windows. Selecting the correct operating system is crucial for ensuring that the Docker container operates properly.
- **Docker Image**: Three versions are available: `General`, `Slim`, and `Custom`. If your "custom script" needs to call external programs, choose the appropriate image for installation based on the required environment:
  - **General**: Contains all features of the Runner and comes pre-installed with the following language environments: Node.js 18, Java 21, Python 3, and PHP 8.
  - **Slim**: Contains all features of the Runner but only pre-installs Node.js 18.
  - **Custom**: Contains all features of the Runner and supports custom language environments for external programs. You can create your own Dockerfile to add or remove environments as needed.
- **Exposed Port**: By default, Docker containers do not expose internal ports for external access. Using the `-p` parameter, you can map an internal port of the container to a port on the host machine, allowing external access to services provided by the container. For example, `-p 80:4524` maps the container's internal port 4524 to port 80 on the host machine.
- **Mount Data Directory**: The `-v` parameter allows you to mount directories from the host machine to the container, enabling the container to access and manipulate files on the host (e.g., database configurations or external programs). For example, -v "/opt/runner":/opt/runner mounts the host's `/opt/runner` directory to the container's `/opt/runner` directory.

<details>
<summary>📷 Visual Reference</summary>

<Background>
![image.png](https://api.apidog.com/api/v1/projects/544525/resources/361347/image-preview)
</Background>

</details>

:::tip
The deployment command contains token information and will be displayed only once for data security reasons. A new command will be generated each time you click **Deploy General Runner**.

Please save the command locally, as you can use it for future Runner upgrades.
:::

### 3. Deploy Runner on the Server

Paste the copied deployment command into the server's terminal, and the Runner installation will start automatically.

:::tip
You can modify the deployment properties of the Runner through environment variables to better match your actual usage scenarios. Read [runner deployment environment](https://docs.apidog.com/runner-deployment-environment-616391m0.md) for more information.
:::

<details>
<summary>📷 Deployment Steps</summary>

<Background>
![](https://assets.apidog.com/uploads/help/2024/06/21/bf2fb22752b19bbb1045ab5cabc93552.png)
</Background>

</details>

After the installation is complete, the terminal will print relevant information. If there is an error, you can troubleshoot it based on the error details. If you still can't solve it, please [contact us](https://discord.gg/nrGjBTnxZH) and provide feedback.

### 4. View Runner Status on the Server

You can view the running status of the container through the Docker client.

<details>
<summary>📷 Visual Reference</summary>

<Background>
![](https://assets.apidog.com/uploads/help/2024/06/21/ee30935683ee6f9afc9bea775b5c8834.png)
</Background>

</details>

You can also use the `docker ps` command in the terminal to view the running status of the container.

<details>
<summary>📷 Visual Reference</summary>

<Background>
![](https://assets.apidog.com/uploads/help/2024/06/21/51b8eb4647a100bf52de632e8367e538.png)
</Background>

</details>

### 5. View Deployed General Runner at Apidog

After confirming that the Runner container on the server has been deployed and enabled, return to Apidog. You can see that the Runner has been deployed and connected to Apidog in **Team Resources** → **General Runner**.

:::info[]
If the General Runner has been successfully deployed on the server, but it is not displayed in the Apidog client, please click the refresh button on the right side of "General Runner" to refresh the page and check again.
:::

You can rename, add descriptions, and delete the Runner so that your team members can better use this Runner; you can also stop/restart the Runner.

The suspended Runner will no longer execute the specified scheduled tasks, nor will it be able to create new related tasks and specify this Runner to execute.

<details>
<summary>📷 Visual Reference</summary>

<Background>
![](https://assets.apidog.com/uploads/help/2024/06/21/2d0f12b29f2e4f3e170b698401c2aeb1.png)
</Background>

</details>

Refer to the table below for the status explanation of the Runner:

<table>
  <thead>
    <tr>
      <th>Status</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="color: green;">Started</td>
      <td>The Runner is enabled normally in the container on the server, maintains communication with Apidog, and can handle related tasks issued by Apidog.</td>
    </tr>
    <tr>
      <td style="color: red;">Stopped</td>
      <td>The Runner is manually stopped in Apidog but continues to run normally in the container on the server and maintains communication. It will not process tasks issued by Apidog, and new tasks cannot specify a stopped Runner for execution. You can manually enable it at Apidog to restore the Runner to the started state.</td>
    </tr>
    <tr>
      <td style="color: gray;">Offline</td>
      <td>The Runner is disconnected from Apidog and cannot process tasks. This may be due to the Runner container stopping on the server or communication issues between the server and Apidog. To restore the Runner, ensure the Runner container is running and there are no communication problems with Apidog, allowing the Runner to restore to the started state.</td>
    </tr>
  </tbody>
</table>

You can deploy multiple General Runners within a team. When creating tasks that require self-hosted Runners, team members can choose from the available Runners.

## Saving Files in Runner

When using Runner to execute tasks such as endpoint requests, test scenarios, and scheduled tasks, certain local files may be required to support task execution. Examples include:
- Calling other programming languages in custom scripts
- Using database connections in Pre/Post Processors
- Using SSL certificate when sending a request

To accommodate this, save the necessary files in the specified directory within the Docker container. When the Runner executes related tasks, it will read the file content from the specified directory according to the task requirements to ensure successful completion.

Refer to the following table to place files with the appropriate formats and content into the specified directory for use:

| Use Content | Specified Directory Path (or File Name) | Example Docker Command |
|-------------|----------------------------------------|------------------------|
| [Other Programming Languages](https://docs.apidog.com/calling-other-programming-languages-593730m0.md) | /app/external-programs/ | -v /Users/xxx/runner/packages/api-test/external-programs:/app/externalPrograms |
| [Database](https://docs.apidog.com/database-operations-in-apidog-588469m0.md) Connection Configuration File | /app/database/database-connections.json | -v /Users/xxx/runner/packages/api-test/database/database-connections.json:/app/database/database-connections.json |
| [SSL Certificate](https://en.wikipedia.org/wiki/Public_key_certificate) List File | /app/ssl/ssl-client-cert-list.json | -v /Users/xxx/runner/packages/api-test/ssl/ssl-client-cert-list.json:/app/ssl/ssl-client-cert-list.json |

:::info[]
You can refer to [This Page](https://docs.apidog.com/installing-and-running-apidog-cli-605135m0.md) to see how to export the configuration file from the Apidog client.
:::

## Upgrading & Redeploying the Runner

### Upgrading the Runner

When a new version of the Runner is released, an upgrade icon will appear in the desktop Runner UI. Click the icon to install the latest version provided by Apidog.

<details>
<summary>📷 Visual Reference</summary>

<Background>
![runner-user-interface.png](https://api.apidog.com/api/v1/projects/544525/resources/348227/image-preview)
</Background>

</details>

Clicking on **Upgrade** will prompt you to stop the currently running Runner container. Please note that once the container is stopped, scheduled tasks and any tasks sent to this Runner from the client will no longer be executed.

<details>
<summary>📷 Visual Reference</summary>

<Background>
![update-prompt.png](https://api.apidog.com/api/v1/projects/544525/resources/348228/image-preview)
</Background>

</details>

After you confirm the upgrade, Apidog will automatically stop the current Runner container and provide a command to deploy the new version. [Follow the initial deployment steps](https://docs.apidog.com/general-runner-755233m0.md#quick-start) to redeploy the Runner. Once the deployment is successful, you'll be using the latest version. Note: Existing scheduled tasks in the client will remain unaffected and do not need to be reassigned.

<details>
<summary>📷 Visual Reference</summary>

<Background>
![update-general-runner.png](https://api.apidog.com/api/v1/projects/544525/resources/348229/image-preview)
</Background>

</details>

### Redeploying the Runner

If the Runner encounters an issue and you can't find a resolution in the Q&A section, or the instructions don't help, consider redeploying the Runner. To do this, navigate to the **More Actions** section for the specific Runner and click on **Redeploy**.

<details>
<summary>📷 Visual Reference</summary>

<Background>
![redeploy-the-runner.png](https://api.apidog.com/api/v1/projects/544525/resources/348230/image-preview)
</Background>

</details>

The redeployment process is the same as [upgrading one above](https://docs.apidog.com/general-runner-755233m0.md#upgrading-the-runner). Note: Redeploying will also stop the Runner container.

## Q&A

<Accordion title="1. How to Check Runner Logs to Diagnose an Issue?" defaultOpen>
  - Use the `docker ps` command to locate the problematic Runner.
- Use the following commands to view the logs:
```yaml
# View the last 100 lines of logs for container abc123 (Recommended):
docker logs --tail 100 abc123

# View logs from the past 5 minutes:
docker logs --since 5m abc123

# View logs from 5 minutes before a specific timestamp:
docker logs --until 2023-10-01T00:00:00 abc123
docker logs --until 5m abc123

# View all logs (Not recommended as the data may be large):
docker logs abc123
```
</Accordion>


<Accordion title="My Runner is Down/Disconnected or Can't Execute Tasks. What Should I Do?">
  Step 1: Gather information to diagnose the issue:
- Look for error patterns or operational details
- Open developer tools (Alt+7+8), send a test scenario to the problematic Runner, and record the endpoint details
- Review Runner logs to look for any error messages or clues

Step 2: Resolve the issue:
- If you can identify the problem and it's not caused by an Apidog bug, fix it yourself
- If you can't pinpoint the issue, contact the Apidog community for further assistance
</Accordion>


<Accordion title="Why Didn't I Receive Notifications After the Runner Completed the Scheduled Task?">
  Step 1: Verify Task Completion:
- Check if a test report for the scheduled task is available in the Apidog client
- Review the Runner logs for any issues

Step 2: Check notification configuration:
- Ensure the notification settings are saved within the scheduled task
- Double-check that the conditions and recipients are correctly configured
- Try manually triggering the task to confirm if the notifications are sent properly
</Accordion>


<Accordion title="What Does 'No Runner Privilege' Error Mean and How to Fix It?">
  There are two possible causes for this error:

- **The Deployment Command Was Regenerated**: If you generated the command, closed the popup, and then clicked again, a new token could invalidate the previous one. To fix this:
  - Switch to another team at the top-left corner, then return to the team where the Runner deployment is needed
  - Regenerate the deployment command, copy it, and run it. **Ensure you don't click to regenerate again until the process completes.**

- **ID Data Error with `teamId` Variable**: This is a known bug that has been fixed in the latest version. If the issue persists:
  - Switch to another team at the top-left corner, then return to the team where the Runner deployment is needed
  - Regenerate the deployment command, copy it, and run it. **Ensure you don't click to regenerate again until the process completes.**
</Accordion>
