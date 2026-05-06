# Notification

Apidog's notification feature is divided into two main sections: **Personal Account Notifications** and **Project-Level Notifications**.

Personal Account Notifications (found in the account settings at the top right) focus on interactions directly related to you, such as `@` mentions or replies in endpoint [comments](https://docs.apidog.com/comments-1604291m0.md). These appear as inbox messages and email alerts to keep you updated.

Project-Level Notifications (found in project settings) are designed for team collaboration. They can automatically push important events such as endpoint changes or test results to third-party platforms (e.g., Slack, Teams), enabling automated team-wide information syncing.

This documentation introduces **Personal Account Notifications**. For **Project-Level Notifications**, please refer to [this doc](https://docs.apidog.com/notification-settings-616240m0.md).

## How to Enable Notifications

### Step 1: Access Notification Settings

Click the **Settings** icon in the top-right corner of the interface and select **Notifications**.

<details>
<summary>📷 Visual Reference</summary>

<Background>
<img style="width: 460px;" src="https://api.apidog.com/api/v1/projects/544525/resources/361452/image-preview" />
</Background>

</details>

### Step 2: Configure Notification Preferences

Configure notification preferences for both **Inbox** and **Email**:

- Use the checkboxes to select which event types you want to receive notifications for
- Click **Select all** to enable all events at once
- Uncheck an option if you no longer want to receive notifications for that event type

<details>
<summary>📷 Visual Reference</summary>

<Background>
<img style="width: 460px;" src="https://api.apidog.com/api/v1/projects/544525/resources/361460/image-preview" />
</Background>

</details>

## Notification Types

### Inbox

When a specified event is triggered, the system sends you a new inbox message.

<details>
<summary>📷 Example</summary>

<Background>
<img style="width: 460px;" src="https://api.apidog.com/api/v1/projects/544525/resources/361455/image-preview" />
</Background>

</details>

### Email

When a specified event is triggered, the system sends a notification email to your registered address.

<details>
<summary>📷 Example</summary>

<Background>
<img style="width: 460px;" src="https://api.apidog.com/api/v1/projects/544525/resources/361454/image-preview" />
</Background>

</details>

## Notification Events

You can choose to receive notifications for the following events:

| Event | Description |
|-------|-------------|
| **New comments on resource I maintained** | When an endpoint, documentation, or other resource you're in charge of receives a new comment |
| **New comments on resources I created** | When an endpoint, documentation, or other resource you created receives a new comment |
| **Mentioned** | When another user `@` mentions you in a comment |
| **Replied** | When another user replies to your comment |
| **Resolved** | When an issue you raised is marked as resolved |

:::tip
It's recommended to enable at least one notification method to avoid missing important updates. For critical events that require quick responses (e.g., being mentioned), it's best to enable both inbox and email notifications.
:::

