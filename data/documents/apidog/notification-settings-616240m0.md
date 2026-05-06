# Notification Settings

## Notification Overview

Apidog enables you to integrate with third-party applications to send notifications to designated recipients when certain events occur. When a specific event is triggered, notifications are sent in real-time to platforms like Slack. Supported notification channels currently include:

- Slack
- Teams
- Webhook
- Jenkins
- Email

Only **project admins** can configure the notification settings. Currently, email notifications are only available for the following events:

- Automated test completed/failed
- Continuous integration completed/failed
- Scheduled tasks completed/failed

## Notification Targets

Notification targets are recipients who receive messages through a specific channel when certain events happen.

To set up notifications, firstly you need to create a notification target by specifying a name, selecting a channel, and configuring its settings. Each channel has a unique setup process. The sections below will walk you through configuring them step by step.

<details>
<summary>📷 Visual Reference</summary>

<Background>
![notification-settings.png](https://api.apidog.com/api/v1/projects/544525/resources/350626/image-preview)
</Background>

</details>

### Slack

Apidog supports sending notification events to a specific **Channel** in Slack by integrating Slack apps - **Incoming WebHooks** in the specified Channel and configuring the Webhook URL of Incoming WebHooks, which can send event messages to the Slack Channel.

**Configuration field description:**

| **Configuration Field** | Required | Description |
|------------------------|----------|-------------|
| **Notification Name** | No | Give a name to the third-party integrated notification to record its purpose. |
| **Trigger Events** | Yes | Supported events: API changes, schema changes, Document changes, Import data, Automation testing |
| **Service URL** | Yes | Webhook URL in "Incoming WebHooks - Integration Settings" |

#### Integrating Apidog Notification with Slack

Project admins can use third-party integration functions to associate Slack apps - **Incoming WebHooks** added in Slack - Channels with project notification events in Apidog to push related API changes, documentation changes, testing completions, etc. to the specified Channel in Slack.

<details>
<summary>📷 Step 1: Open channel details</summary>

In the Slack channel, click the "Open channel details" option in the top right corner.

<Background>
![CleanShot 2024-12-03 at 15.41.54@2x.png](https://api.apidog.com/api/v1/projects/544525/resources/348487/image-preview)
</Background>

</details>

<details>
<summary>📷 Step 2: Install Incoming WebHook</summary>

In the `Integrations - Apps` of the specific Channel, install and add `Incoming WebHook`.

<Background>
    <img style="background-color: transparent;" src="https://assets.apidog.com/uploads/help/2024/02/21/539e1f2eac9b4ba5ef1250ad2fcd2f0b.png" />

    <img style="background-color: transparent;" src="https://assets.apidog.com/uploads/help/2024/02/21/da4e1353dab1fd737235d40e3803ec5c.png" />
</Background>

</details>

<details>
<summary>📷 Step 3: View Incoming WebHooks</summary>

After installation is complete, click the button to the right of `Incoming WebHooks` - `View`.

<Background>
    <img style="background-color: transparent;" src="https://assets.apidog.com/uploads/help/2024/02/21/4da28e3a30b6967b62574c0d38da478b.png" />
</Background>

</details>

<details>
<summary>📷 Step 4: Configure Incoming WebHooks</summary>

This will open the description page of `Incoming WebHooks`, click `Configuration` to set up.

<Background>
    <img style="background-color: transparent;" src="https://assets.apidog.com/uploads/help/2024/02/21/74ceeba151fba888c02f5c51a05ec826.png" />
</Background>

</details>

<details>
<summary>📷 Step 5: Add to Slack</summary>

Click `Add to Slack`.

<Background>
    <img style="background-color: transparent;" src="https://assets.apidog.com/uploads/help/2024/02/21/f1f5b9f73c37ba0dc2bcba18451c8652.png" />
</Background>

</details>

<details>
<summary>📷 Step 6: Select Channel and Add Integration</summary>

Select the Channel to push Apidog notification event messages to, and click `Add Incoming WebHooks integration`.

<Background>
    <img style="background-color: transparent;" src="https://assets.apidog.com/uploads/help/2024/02/21/74647553e66678a41caa8e5d6a8e7ddc.png" />
</Background>

</details>

<details>
<summary>📷 Step 7: Get Webhook URL</summary>

Get and copy the Webhook URL.

<Background>
    <img style="background-color: transparent;" src="https://assets.apidog.com/uploads/help/2024/02/21/8f841fe5883fdbc8c347d149f57baa37.png" />
</Background>

</details>

<details>
<summary>📷 Step 8: Create notification target in Apidog</summary>

Click "Settings" > "Notifications" > "Notification Targets" > and create a new notification Target.

<Background>
![create-new-slack-notification-target.png](https://api.apidog.com/api/v1/projects/544525/resources/350632/image-preview)
</Background>

- Fill in the notification target name.
- Choose `Slack` as the notification channel.
- Paste the Webhook URL obtained from the Incoming WebHooks settings in the `Service URL`.

</details>

After clicking `Save`, the set-up is complete. You now can move on to [create a notification event](https://docs.apidog.com/notification-settings-616240m0.md#notification-events).

Once the notification event is set up and triggered, you will receive the message in your designated Slack channel.

<details>
<summary>📷 Visual Reference: Slack notification message</summary>

<Background>
    <img style="background-color: transparent;" src="https://assets.apidog.com/uploads/help/2024/02/21/5d80c034b973e463b55013e3864363f5.png" />
</Background>

</details>

### Teams

Support for sending notifications to Microsoft Teams allows [Workflows](https://support.microsoft.com/en-us/office/create-incoming-webhooks-with-workflows-for-microsoft-teams-8ae491c7-0394-4861-ba59-055e33f75498) in Teams to use these messages as triggers for further actions—such as automatically posting messages in a group or channel—helping teams stay informed about important events from Apidog.

Specifically, you can configure a Webhook Trigger within a Workflow. When certain notification events in Apidog are triggered (e.g., API changes, documentation updates, or automated test completions), Apidog will send a POST request to the specified HTTP POST URL of the trigger, carrying the event payload.

**Configuration Fields:**

| **Field** | **Required** | **Description** |
|-----------|--------------|-----------------|
| Name | Yes | A name that describes the purpose of this notification target |
| HTTP POST URL | Yes | The URL where the Webhook Trigger in the Workflow receives POST requests |

#### Integrating Apidog Notification with Teams Channels

<details>
<summary>📷 Step 1: Create a workflow in Teams</summary>

In **Microsoft Teams → Workflow**, click `Create`, and you can quickly get started by selecting the template `Post to a channel when a webhook request is received`.

<Background>
![image.png](https://api.apidog.com/api/v1/projects/544525/resources/356572/image-preview)
</Background>

</details>

<details>
<summary>📷 Step 2: Set flow name and account</summary>

Set a name for the flow, select the appropriate account, and click `Next`.

<Background>
![image.png](https://api.apidog.com/api/v1/projects/544525/resources/356573/image-preview)
</Background>

</details>

<details>
<summary>📷 Step 3: Choose group and channel</summary>

Choose the group and channel where you want to receive the notification, then click `Create flow`.

<Background>
![image.png](https://api.apidog.com/api/v1/projects/544525/resources/356574/image-preview)
</Background>

</details>

<details>
<summary>📷 Step 4: Get HTTP POST URL</summary>

Once the flow is created, the HTTP POST URL under the trigger step will be displayed. You can copy it directly or find it later within the trigger step of the flow.

<Background>
![image.png](https://api.apidog.com/api/v1/projects/544525/resources/356575/image-preview)

![image.png](https://api.apidog.com/api/v1/projects/544525/resources/356576/image-preview)
</Background>

</details>

<details>
<summary>📷 Step 5: Configure notification target in Apidog</summary>

Paste this HTTP POST URL into the notification target configuration in Apidog.

<Background>
![CleanShot 2025-06-10 at 11.55.15@2x.png](https://api.apidog.com/api/v1/projects/544525/resources/356577/image-preview)
</Background>

</details>

<details>
<summary>📷 Step 6: Create notification event</summary>

Create a notification event in Apidog and associate it with the configured Teams notification target.

<Background>
![CleanShot 2025-06-10 at 11.55.59@2x.png](https://api.apidog.com/api/v1/projects/544525/resources/356579/image-preview)
</Background>

</details>

<details>
<summary>📷 Step 7: Verify Teams notification</summary>

When this notification event is triggered, the previously created workflow will automatically post a message to the selected Teams channel.

<Background>
![image.png](https://api.apidog.com/api/v1/projects/544525/resources/356580/image-preview)
</Background>

</details>

### Webhook

Supports sending notification events to the HTTP Server. You can send event messages to the HTTP Server by specifying a URL address to receive POST requests.

**Configuration field description:**

| **Configuration Field** | Required | Description |
|------------------------|----------|-------------|
| **Notification Name** | No | Give a name to the third-party integrated notification to record the purpose of the notification. |
| **Trigger Event** | Yes | Supported events: API changes, Data model changes, Document changes, Import data, Automation testing |
| **Server URL** | Yes | URL address of the HTTP Server for receiving requests |
| **Signature Auth** | No | The sent content is encrypted by the [HMAC SHA1](https://en.wikipedia.org/wiki/Hash-based_message_authentication_code) encryption algorithm, using a token as the KEY to display the value in hexadecimal (requires a configured token), and contains the prefix sha1= |

#### Integrating Apidog Notification with Self-hosted HTTP Server

Project admins can use third-party integration to associate their self-hosted HTTP Server with project notification events in Apidog, to receive notifications for relevant API changes, document changes, and automation test completions in their HTTP Server.

To integrate Apidog notification with self-hosted HTTP server, click "Settings" > "Notifications" > "Notification Targets" > and create a new notification Target.

<details>
<summary>📷 Visual Reference</summary>

<Background>
![create-new-webhook-notification-target.png](https://api.apidog.com/api/v1/projects/544525/resources/350634/image-preview)
</Background>

</details>

1. Fill in the notification target name.
2. Choose `Webhook` as the channel.
3. Paste the URL of the self-hosted HTTP Server in the `Service URL` field. 
4. If the signature verification is enabled, copy and paste the key in the `Signature Key` field.

After clicking `Save`, the set-up is complete. You now can move on to [create a notification event](https://docs.apidog.com/notification-settings-616240m0.md#notification-events).

### Jenkins

It supports sending notification events to Jenkins service. By configuring Jenkins Webhook URL, event messages can be sent to Jenkins.

**Configuration field descriptions:**

| **Configuration Field** | **Required** | **Description** |
|------------------------|--------------|-----------------|
| **Notification Name** | No | Give a name to the third-party integration notification to record its purpose. |
| **Trigger Events** | Yes | API changes, Data model changes, Import data, Automation testing. Real-time notifications will be triggered when any of the above events occur. |
| **Service URL** | Yes | The URL is configured in the [Generic Webhook Trigger](https://plugins.jenkins.io/generic-webhook-trigger/) plugin. |
| **Signature Auth** | No | Sent to the [Generic Webhook Trigger](https://plugins.jenkins.io/generic-webhook-trigger/) plugin via the Authorization Bearer header. |

#### Integrating Apidog Notification with Jenkins Service

Project admins can use third-party integration functionality to associate the Webhook URL configured in the Jenkins [Generic Webhook Trigger](https://plugins.jenkins.io/generic-webhook-trigger/) plugin with project notification events in Apidog, to trigger a build action in Jenkins automatically when events such as API changes, document changes, and automation test completions are triggered, and view messages in the build history.

<details>
<summary>📷 Step 1: Webhook URL configured in Jenkins Generic Webhook Trigger plugin</summary>

Create a new view on the Jenkins Dashboard:

<Background>
    <img style="background-color: transparent;" src="https://assets.apidog.com/help/assets/images/webhook-10-704b7d013e426ac9f12b750f0aef1dcc.png" />
</Background>

Click on the view in the previous step to enter `Configure`>`Build Triggers`, and select `Generic Webhook Trigger`. Webhook URL is `"http://"+"your service address"+"/generic-webhook-trigger/invoke"`

<Background>
    <img style="background-color: transparent;" src="https://assets.apidog.com/help/assets/images/webhook-11-4c076ad1314d42d76a840b5de2f0ad83.png" />
</Background>

The custom token is supported:

<Background>
    <img style="background-color: transparent;" src="https://assets.apidog.com/help/assets/images/webhook-12-b83b2f9f817d3e3d6673b6ea8c829621.png" />
</Background>

</details>

<details>
<summary>📷 Step 2: Create a new notification target</summary>

Click "Settings" > "Notifications" > "Notification Targets" > and create a new notification Target.

<Background>
![notification-setting-jenkins.png](https://api.apidog.com/api/v1/projects/544525/resources/350635/image-preview)
</Background>

- Fill in the notification target name.
- Choose `Jenkins` as the channel
- Paste the Webhook URL configured in the [Generic Webhook Trigger](https://plugins.jenkins.io/generic-webhook-trigger/) plugin in the `Service URL` field
- If a custom token is used, copy and paste the `Token` into the `Signature Token` field.

</details>

After clicking `Save`, the set-up is complete. You now can move on to [create a notification event](https://docs.apidog.com/notification-settings-616240m0.md#notification-events).

Once the notification event is set up and triggered, Jenkins will automatically initiate a build action and you can view the message in the build history:

<details>
<summary>📷 Visual Reference: Jenkins Build History</summary>

<Background>
    <img style="background-color: transparent;" src="https://assets.apidog.com/help/assets/images/webhook-14-7b886e39ae1b2580280b5c9465467317.png" />
</Background>

</details>

### Email

Notifications can be sent via email to specified email addresses. Currently, email notifications are only available for the following events:

- Automated test completed/failed
- Continuous integration completed/failed
- Scheduled tasks completed/failed

**Configuration field description:**

| **Field** | **Required** | **Details** |
|-----------|--------------|-------------|
| **Name** | Yes | A descriptive name that highlights the purpose or characteristics of the notification target. |
| **Notification Email Address** | Yes | Enter the email address(es) to receive notifications. You can either select email addresses of project members or manually type in an address. Multiple email addresses are supported. |

#### Integrating Apidog Notification with Email

<details>
<summary>📷 Visual Reference</summary>

<Background>
![notification-setting-email.png](https://api.apidog.com/api/v1/projects/544525/resources/350636/image-preview)
</Background>

</details>

1. Fill in the notification target name.
2. Choose `Email` as the channel
3. Enter emails

After clicking `Save`, the set-up is complete. You now can move on to [create a notification event](https://docs.apidog.com/notification-settings-616240m0.md#notification-events).

## Notification Events

You can create notification events to specify which events will trigger notifications to designated recipients (notification targets). To set up a notification event, you need to configure:
- Notification Event Name
- Trigger Event
- Notification Targets

<details>
<summary>📷 Visual Reference</summary>

<Background>
![creating-notification-events.png](https://api.apidog.com/api/v1/projects/544525/resources/350637/image-preview)
</Background>

</details>

### Trigger Event

You can choose from the following notification events to trigger the notification:

| Trigger Event | Details |
|---------------|---------|
| **Endpoint Changed** | Endpoint Created<br> Endpoint Updated <br> Endpoint Deleted |
| **Schema Changed** | Schema Created<br> Schema Updated<br> Schema Deleted |
| **Document Changed** | Document Created<br> Document Updated<br> Document Deleted |
| **Data Import** | Import (Manual Import)<br> Import (Auto Sync) |
| **Response Component Changed** | Response Component Created<br> Response Component Updated<br> Response Component Deleted |
| **Sprint Branch Changed** | Sprint Branch Merged<br> Sprint Branch Created<br> Sprint Branch Archived<br> Sprint Branch Deleted<br> Sprint Branch Retrieved |
| **API Version Changed** | API Version Created<br> API Version Deleted |
| **Security Scheme Changed** | Security Scheme Created<br> Security Scheme Updated<br> Security Scheme Deleted |

:::tip
For notifications related to automated tests (e.g., automated test completed, continuous integration completed, scheduled task completed), you need to configure the settings individually for each test scenario. This approach is more flexible and better suits real-world use cases.
:::

### Notification Targets

Choose which notification targets will receive the notification when a trigger event happens. You can choose from the notification targets that have already been set up in the project and select multiple targets if needed.

However, email notifications are only supported for three specific events:

- Automated test completed/failed
- Continuous integration completed/failed
- Scheduled tasks completed/failed

<details>
<summary>📷 Visual Reference</summary>

<Background>
![creating-notification-events-setting-targets.png](https://api.apidog.com/api/v1/projects/544525/resources/350638/image-preview)
</Background>

</details>

