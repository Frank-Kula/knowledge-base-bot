# Navigating Apidog

The main interface of Apidog is divided into these key areas:

- **Header**: Top navigation with project management and user settings.
- **Sidebar**: Left panel for accessing core features.
- **Workbench**: Central area with directory tree, tabs, and environment selector.
- **Footer**: Bottom bar for status, tools, and community links.

<Background>
![image.png](https://api.apidog.com/api/v1/projects/544525/resources/369333/image-preview)
</Background>

This layout ensures efficient navigation for API development and testing.

## Header

The header provides quick access to essential functions.

<Background>
![image.png](https://api.apidog.com/api/v1/projects/544525/resources/344447/image-preview)
</Background>

| Feature | Description |
|---------|-------------|
| Home | Access your personal homepage with teams, projects, and API hub. <Icon icon="material-outline-home"/> |
| Project Tabs | Switch between projects. Click the button next to the name to open in a new window. |
| Upgrade/Plan | View your team's current plan. |
| Refresh | Reload project data. Note: This closes all open tabs. <Icon icon="ph-bold-arrows-clockwise"/> |
| Settings | Configure local settings like appearance and proxy. <Icon icon="material-outline-settings"/> |
| Notifications | Check team activity alerts. <Icon icon="ph-bold-bell"/> |
| Avatar | Manage account settings and access tokens. |

:::tip[]
To switch projects, click any project tab in the header.
:::

## Sidebar

The Sidebar organizes core Apidog features.

<Background>
<p style="text-align: center">
<img src="https://api.apidog.com/api/v1/projects/544525/resources/369334/image-preview" style="width: 80px" />
</p>
</Background>

| Feature | Description |
|---------|-------------|
| Project Icon | Jump to [teams and projects](https://docs.apidog.com/basic-concepts-612997m0.md) overview. |
| APIs | [Define](https://docs.apidog.com/design-apis-in-apidog-533969m0.md), [debug](https://docs.apidog.com/develop-and-debug-apis-in-apidog-541758m0.md), [send requests](https://docs.apidog.com/send-requests-in-apidog-626721m0.md), create [schemas](https://docs.apidog.com/introduction-to-schema-533975m0.md), and write docs. |
| Tests | Run batch requests, create [scenarios](https://docs.apidog.com/create-a-test-scenario-599311m0.md), view [reports](https://docs.apidog.com/test-reports-603898m0.md), and manage [CI/CD](https://docs.apidog.com/cicd-in-apidog-609698m0.md). |
| Share Docs | Share and publish API docs with [customization](https://docs.apidog.com/custom-layouts-631390m0.md) options. |
| History | View and resend sent requests. |
| Settings | Manage project settings, notifications, and data. |
| Invite | Invite users to the project. <Icon icon="ph-bold-user-plus"/> |

:::tip[]
Use the Sidebar to quickly access frequently used features like APIs and Tests.
:::

## Workbench

The Workbench is the central workspace for managing project elements.

### Directory Tree

The directory tree organizes project components hierarchically.

<Background>
<p style="text-align: center">
    <img src="https://api.apidog.com/api/v1/projects/544525/resources/369335/image-preview" style="width: 240px" />
</p>
</Background>


| Feature | Description |
|---------|-------------|
| Branches and Versions | Switch branches or manage versions. Default is main branch. <Icon icon="ph-bold-git-branch"/> |
| Search and Filter | Search endpoints (not folders or cases). <Icon icon="material-outline-search"/> |
| Create New | Add endpoints, requests, schemas, etc. <Icon icon="ph-bold-plus"/> |
| *\<Project Name\>* | High-level project view. |
| Endpoints | Organize endpoints and cases in folders. |
| [Schemas](https://docs.apidog.com/introduction-to-schema-533975m0.md) | Manage schemas in folders. |
| [Components](https://docs.apidog.com/components-533976m0.md) | Reusable response components. |
| Admin API | Contains tools for the admin to batch process data |
| [Quick Requests](https://docs.apidog.com/send-requests-in-apidog-626721m0.md) | Organizes quick requests made in this project |


:::tip[]
To create a new endpoint, click the Create New icon in the directory tree.
:::

### Tabs

Clicking an element opens a tab. Tabs support types like Endpoint, Schema, Request, and Markdown.

- **Browsing Mode:** Single-click opens italic tabs that overwrite on new clicks.
- **Editing Mode:** Double-click or edit to make tabs normal (prevents overwriting).

Right-side buttons:
- <Icon icon="ph-bold-plus"/> **New**: Create elements.
- <Icon icon="material-outline-more_horiz"/> **More**: Close tabs (all, current, or others).

:::tip[]
Use double-click for persistent tabs during multi-element editing.
:::

### Environment Selector

Select environments for testing APIs. Switch between dev, staging, or production to ensure requests use correct settings.

**Example:** Click the environment dropdown in the workbench to change contexts.

## Footer

The footer provides status and utility tools.

<Background>
![image.png](https://api.apidog.com/api/v1/projects/544525/resources/369336/image-preview)
</Background>


| Feature | Description |
|---------|-------------|
| Collapse/Expand | Toggle directory tree visibility. <Icon icon="ph-bold-arrow-line-left"/> |
| Online | Shows connection status. Offline affects sync. <Icon icon="ph-bold-check-circle"/> |
| [Agent](https://docs.apidog.com/request-proxy-agent-780303m0.md) | Select agent for requests (Apidog Web only). <Icon icon="ph-bold-network"/> |
| [Cookies](https://docs.apidog.com/managing-cookies-629770m0.md) | Manage cookies. <Icon icon="ph-bold-cookie"/> |
| Trash | View deleted items (auto-deleted after 30 days). <Icon icon="ph-bold-trash"/> |
| Community | Join Apidog community on [Discord](https://discord.gg/ZBxrzyXfbJ), [Slack](https://join.slack.com/t/apidogcommunity/shared_invite/zt-2sdxs1l9y-YBP~JWZxp81Zkhrn_3N3_g), [X](https://x.com/ApidogHQ), or [Email](mailto:support@apidog.com). <Icon icon="material-outline-groups"/> |


:::tip[]
Check Online status to ensure team synchronization.
:::

---
<CardGroup cols={2}>
  <Card title="Next Step" href="https://docs.apidog.com/basic-concepts-in-apidog-644342m0.md">
    Learn Basic Concepts in Apidog
  </Card>
</CardGroup>
