# Member Roles & Permission Settings

Member roles and permissions are divided into two categories: team and project.

## Team Roles and Permissions

### Default Roles and Permissions

Apidog offers built-in team roles with predefined permissions designed to cater to various needs. By assigning a role to a team member, you can effectively manage their permissions and access levels within the team.

The team-level permissions are structured around four primary roles: **Team Owner**, **Team Admin**, **Team Member**, and **Guest**. Below is a detailed breakdown of their respective permissions:

<table style="border-collapse: collapse;">
  <thead>
    <tr>
      <th>Resource Category</th>
      <th>Resource Name</th>
      <th>Permissions</th>
      <th>Team Owner</th>
      <th>Team Admin</th>
      <th>Team Member</th>
      <th>Guest</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="12"> Team Management </td>
      <td rowspan="5">Members/Roles</td>
      <td>View Team Member details</td>
      <td>✅</td>
      <td>✅</td>
      <td>✅</td>
      <td>❌</td>
    </tr>
    <tr>
      <td>Invite Team Members</td>
      <td>✅</td>
      <td>✅</td>
      <td>❌</td>
      <td>❌</td>
    </tr>
    <tr>
      <td>Assign/Remove Team Member Roles</td>
      <td>✅</td>
      <td>✅</td>
      <td>❌</td>
      <td>❌</td>
    </tr>
    <tr>
      <td>View Project Roles</td>
      <td>✅</td>
      <td>✅</td>
      <td>❌</td>
      <td>❌</td>
    </tr>
    <tr>
      <td>Add/Edit/Delete Project Roles</td>
      <td>✅</td>
      <td>✅</td>
      <td>❌</td>
      <td>❌</td>
    </tr>
    <tr>
      <td rowspan="3">Team Settings</td>
      <td>Edit Team Name</td>
      <td>✅</td>
      <td>✅</td>
      <td>❌</td>
      <td>❌</td>
    </tr>
    <tr>
      <td>Transfer Team</td>
      <td>✅</td>
      <td>❌</td>
      <td>❌</td>
      <td>❌</td>
    </tr>
    <tr>
      <td>Dismiss Team</td>
      <td>✅</td>
      <td>❌</td>
      <td>❌</td>
      <td>❌</td>
    </tr>
    <tr>
      <td rowspan="4">Project Operations</td>
      <td>Create New Projects</td>
      <td>✅</td>
      <td>✅</td>
      <td>❌</td>
      <td>❌</td>
    </tr>
    <tr>
      <td>Clone a Project</td>
      <td>✅</td>
      <td>✅</td>
      <td>❌</td>
      <td>❌</td>
    </tr>
    <tr>
      <td>Delete/Transfer a Project</td>
      <td>✅</td>
      <td>✅</td>
      <td>❌</td>
      <td>❌</td>
    </tr>
    <tr>
      <td>Edit Project Name</td>
      <td>✅</td>
      <td>✅</td>
      <td>❌</td>
      <td>❌</td>
    </tr>
  </tbody>
</table>

:::info[]
Custom permissions for team roles are **not yet supported**.
:::

### Guest

- Users from "Project invitations" but not "Team invitations" are considered Guests at the team level.
- Guests can only access projects they're invited to.
- Guests have similar team permissions as team members but are excluded from new project permission settings.
- Guests count towards user limits in plan selection.
- Guests are also counted as team members and will be billed according to the total number of team members.

### Setting Team Permissions

Set team-level permissions by assigning roles via My Team → Member page → Member Details → Role.

<details>
<summary>📷 Visual Reference</summary>

<Background>
![setting-team-roles.png](https://api.apidog.com/api/v1/projects/544525/resources/349168/image-preview)
</Background>

</details>

## Project Roles and Permissions

### Default Roles and Permissions

Apidog offers built-in project roles with predefined permissions to streamline access management. The project roles are categorized into four types: **Admin**, **Editor**, **Read-only**, and **Forbidden**. Below is a detailed breakdown of the permissions for each role.

<details>
<summary> Default Roles and Permissions Table </summary>
<table style="border-collapse:collapse;width:100%;">
  <thead>
    <tr>
      <th>Resource Category</th>
      <th>Resource Name</th>
      <th>Permissions</th>
      <th>Admin</th>
      <th>Editor</th>
      <th>Read-only</th>
      <th>Forbidden</th>
    </tr>
  </thead>
  <tbody>
    <!-- Branch Management -->
    <tr>
      <td rowspan="5"><strong>Branch Management</strong></td>
      <td rowspan="4">Sprint Branch</td>
      <td>View, Switch Branches</td>
      <td>✅</td>
      <td>✅</td>
      <td>✅</td>
      <td>❌</td>
    </tr>
    <tr>
      <td>Merge Branches</td>
      <td>✅</td>
      <td>✅</td>
      <td>❌</td>
      <td>❌</td>
    </tr>
    <tr>
      <td>View/Submit Merge Request</td>
      <td>✅</td>
      <td>✅</td>
      <td>❌</td>
      <td>❌</td>
    </tr>
    <tr>
      <td>Add, Delete, Modify, Merge Protected Branch Content</td>
      <td>✅</td>
      <td>❌</td>
      <td>❌</td>
      <td>❌</td>
    </tr>
    <tr>
      <td>API Versions</td>
      <td>View, Switch API Versions</td>
      <td>✅</td>
      <td>✅</td>
      <td>✅</td>
      <td>❌</td>
    </tr>

    <!-- Endpoint Management -->
    <tr>
      <td rowspan="13"><strong>Endpoint Management</strong></td>
      <td rowspan="4">Endpoints (including Cases, Markdown, WebSocket, API Documentation, etc.)</td>
      <td>View, Run Endpoints</td>
      <td>✅</td>
      <td>✅</td>
      <td>✅</td>
      <td>❌</td>
    </tr>
    <tr>
      <td>Add, Delete, Modify Endpoints</td>
      <td>✅</td>
      <td>✅</td>
      <td>❌</td>
      <td>❌</td>
    </tr>
    <tr>
      <td>Generate Code</td>
      <td>✅</td>
      <td>✅</td>
      <td>❌</td>
      <td>❌</td>
    </tr>
    <tr>
      <td>Add, Delete, Modify Cases</td>
      <td>✅</td>
      <td>✅</td>
      <td>❌</td>
      <td>❌</td>
    </tr>
    <tr>
      <td rowspan="2">Schemas</td>
      <td>View, Reference Schemas</td>
      <td>✅</td>
      <td>✅</td>
      <td>✅</td>
      <td>❌</td>
    </tr>
    <tr>
      <td>Add, Delete, Modify Schemas</td>
      <td>✅</td>
      <td>✅</td>
      <td>❌</td>
      <td>❌</td>
    </tr>
    <tr>
      <td rowspan="2">Components</td>
      <td>View, Reference Components</td>
      <td>✅</td>
      <td>✅</td>
      <td>✅</td>
      <td>❌</td>
    </tr>
    <tr>
      <td>Add, Delete, Modify Components</td>
      <td>✅</td>
      <td>✅</td>
      <td>❌</td>
      <td>❌</td>
    </tr>
    <tr>
      <td rowspan="2">Requests</td>
      <td>View, Send Requests</td>
      <td>✅</td>
      <td>✅</td>
      <td>✅</td>
      <td>❌</td>
    </tr>
    <tr>
      <td>Add, Delete, Modify Requests</td>
      <td>✅</td>
      <td>✅</td>
      <td>❌</td>
      <td>❌</td>
    </tr>
    <tr>
      <td rowspan="3">Trash</td>
      <td>View</td>
      <td>✅</td>
      <td>✅</td>
      <td>❌</td>
      <td>❌</td>
    </tr>
    <tr>
      <td>Restore</td>
      <td>✅</td>
      <td>✅</td>
      <td>❌</td>
      <td>❌</td>
    </tr>
    <tr>
      <td>Permanently Delete</td>
      <td>✅</td>
      <td>❌</td>
      <td>❌</td>
      <td>❌</td>
    </tr>

    <!-- Automated Tests -->
    <tr>
      <td rowspan="7"><strong>Automated Tests</strong></td>
      <td rowspan="4">Test Scenarios</td>
      <td>View, Run Functional Tests</td>
      <td>✅</td>
      <td>✅</td>
      <td>✅</td>
      <td>❌</td>
    </tr>
    <tr>
      <td>Run Performance Tests</td>
      <td>✅</td>
      <td>✅</td>
      <td>✅</td>
      <td>❌</td>
    </tr>
    <tr>
      <td>Add, Delete, Modify</td>
      <td>✅</td>
      <td>✅</td>
      <td>❌</td>
      <td>❌</td>
    </tr>
    <tr>
      <td>Export to External Programs</td>
      <td>✅</td>
      <td>✅</td>
      <td>❌</td>
      <td>❌</td>
    </tr>
    <tr>
      <td rowspan="2">Scheduled Tasks</td>
      <td>View/Run Now</td>
      <td>✅</td>
      <td>✅</td>
      <td>✅</td>
      <td>❌</td>
    </tr>
    <tr>
      <td>Add, Delete, Modify</td>
      <td>✅</td>
      <td>✅</td>
      <td>❌</td>
      <td>❌</td>
    </tr>
    <tr>
      <td>Test Reports</td>
      <td>Delete</td>
      <td>✅</td>
      <td>✅</td>
      <td>❌</td>
      <td>❌</td>
    </tr>

    <!-- Environment Management -->
    <tr>
      <td rowspan="7"><strong>Environment Management</strong></td>
      <td rowspan="2">Global Variables</td>
      <td>View, Edit Current Values</td>
      <td>✅</td>
      <td>✅</td>
      <td>✅</td>
      <td>❌</td>
    </tr>
    <tr>
      <td>Add, Delete, Modify</td>
      <td>✅</td>
      <td>✅</td>
      <td>❌</td>
      <td>❌</td>
    </tr>
    <tr>
      <td rowspan="2">Global Params</td>
      <td>View</td>
      <td>✅</td>
      <td>✅</td>
      <td>✅</td>
      <td>❌</td>
    </tr>
    <tr>
      <td>Add, Delete, Modify</td>
      <td>✅</td>
      <td>✅</td>
      <td>❌</td>
      <td>❌</td>
    </tr>
    <tr>
      <td>Vault Secrets</td>
      <td>Add, Delete, Modify, Fetch</td>
      <td>✅</td>
      <td>✅</td>
      <td>❌</td>
      <td>❌</td>
    </tr>
    <tr>
      <td rowspan="2">Environments</td>
      <td>View, Edit Current Values</td>
      <td>✅</td>
      <td>✅</td>
      <td>✅</td>
      <td>❌</td>
    </tr>
    <tr>
      <td>Add, Delete, Modify</td>
      <td>✅</td>
      <td>✅</td>
      <td>❌</td>
      <td>❌</td>
    </tr>

    <!-- Documentation Sharing -->
    <tr>
      <td rowspan="4"><strong>Documentation Sharing</strong></td>
      <td rowspan="2">Quick Share</td>
      <td>View</td>
      <td>✅</td>
      <td>✅</td>
      <td>✅</td>
      <td>❌</td>
    </tr>
    <tr>
      <td>Add, Delete, Modify</td>
      <td>✅</td>
      <td>✅</td>
      <td>❌</td>
      <td>❌</td>
    </tr>
    <tr>
      <td rowspan="2">Publish Doc Sites</td>
      <td>View, Preview</td>
      <td>✅</td>
      <td>✅</td>
      <td>✅</td>
      <td>❌</td>
    </tr>
    <tr>
      <td>Publish Settings</td>
      <td>✅</td>
      <td>❌</td>
      <td>❌</td>
      <td>❌</td>
    </tr>

    <!-- Project Settings -->
    <tr>
      <td rowspan="28"><strong>Project Settings</strong></td>
      <td rowspan="3">Basic Settings</td>
      <td>View</td>
      <td>✅</td>
      <td>✅</td>
      <td>✅</td>
      <td>❌</td>
    </tr>
    <tr>
      <td>Modify</td>
      <td>✅</td>
      <td>❌</td>
      <td>❌</td>
      <td>❌</td>
    </tr>
    <tr>
      <td>Clone Project</td>
      <td>✅</td>
      <td>❌</td>
      <td>❌</td>
      <td>❌</td>
    </tr>
    <tr>
      <td rowspan="3">Member Management</td>
      <td>View</td>
      <td>✅</td>
      <td>❌</td>
      <td>❌</td>
      <td>❌</td>
    </tr>
    <tr>
      <td>Add</td>
      <td>✅</td>
      <td>❌</td>
      <td>❌</td>
      <td>❌</td>
    </tr>
    <tr>
      <td>Assign/Remove Member Roles</td>
      <td>✅</td>
      <td>❌</td>
      <td>❌</td>
      <td>❌</td>
    </tr>
    <tr>
      <td rowspan="2">Feature Settings</td>
      <td>View</td>
      <td>✅</td>
      <td>✅</td>
      <td>✅</td>
      <td>❌</td>
    </tr>
    <tr>
      <td>Add, Delete, Modify</td>
      <td>✅</td>
      <td>❌</td>
      <td>❌</td>
      <td>❌</td>
    </tr>
    <tr>
      <td rowspan="2">Notification Targets</td>
      <td>View</td>
      <td>✅</td>
      <td>✅</td>
      <td>✅</td>
      <td>❌</td>
    </tr>
    <tr>
      <td>Add, Delete, Modify</td>
      <td>✅</td>
      <td>✅</td>
      <td>❌</td>
      <td>❌</td>
    </tr>
    <tr>
      <td rowspan="2">Notification Events</td>
      <td>View</td>
      <td>✅</td>
      <td>✅</td>
      <td>✅</td>
      <td>❌</td>
    </tr>
    <tr>
      <td>Add, Delete, Modify</td>
      <td>✅</td>
      <td>✅</td>
      <td>❌</td>
      <td>❌</td>
    </tr>
    <tr>
      <td rowspan="2">Common Parameters</td>
      <td>View, Reference</td>
      <td>✅</td>
      <td>✅</td>
      <td>✅</td>
      <td>❌</td>
    </tr>
    <tr>
      <td>Add, Delete, Modify</td>
      <td>✅</td>
      <td>✅</td>
      <td>❌</td>
      <td>❌</td>
    </tr>
    <tr>
      <td rowspan="2">Sprint Branches</td>
      <td>View</td>
      <td>✅</td>
      <td>✅</td>
      <td>✅</td>
      <td>❌</td>
    </tr>
    <tr>
      <td>Add, Delete, Modify, Protect, Archive, Restore</td>
      <td>✅</td>
      <td>✅</td>
      <td>❌</td>
      <td>❌</td>
    </tr>
    <tr>
      <td rowspan="2">API Versions</td>
      <td>View</td>
      <td>✅</td>
      <td>✅</td>
      <td>✅</td>
      <td>❌</td>
    </tr>
    <tr>
      <td>Add, Delete, Modify</td>
      <td>✅</td>
      <td>✅</td>
      <td>❌</td>
      <td>❌</td>
    </tr>
    <tr>
      <td rowspan="2">Public Scripts</td>
      <td>View, Reference</td>
      <td>✅</td>
      <td>✅</td>
      <td>✅</td>
      <td>❌</td>
    </tr>
    <tr>
      <td>Add, Delete, Modify</td>
      <td>✅</td>
      <td>✅</td>
      <td>❌</td>
      <td>❌</td>
    </tr>
    <tr>
      <td rowspan="2">Database Connections</td>
      <td>View, Reference</td>
      <td>✅</td>
      <td>✅</td>
      <td>✅</td>
      <td>❌</td>
    </tr>
    <tr>
      <td>Add, Delete, Modify</td>
      <td>✅</td>
      <td>✅</td>
      <td>❌</td>
      <td>❌</td>
    </tr>
    <tr>
      <td rowspan="2">Custom Functions</td>
      <td>View, Reference</td>
      <td>✅</td>
      <td>✅</td>
      <td>✅</td>
      <td>❌</td>
    </tr>
    <tr>
      <td>Add, Delete, Modify</td>
      <td>✅</td>
      <td>✅</td>
      <td>❌</td>
      <td>❌</td>
    </tr>
    <tr>
      <td rowspan="3">Import Data</td>
      <td>Manual Import</td>
      <td>✅</td>
      <td>✅</td>
      <td>❌</td>
      <td>❌</td>
    </tr>
    <tr>
      <td>Scheduled Import (Manual Trigger)</td>
      <td>✅</td>
      <td>✅</td>
      <td>❌</td>
      <td>❌</td>
    </tr>
    <tr>
      <td>Scheduled Import Settings</td>
      <td>✅</td>
      <td>❌</td>
      <td>❌</td>
      <td>❌</td>
    </tr>
    <tr>
      <td>Export Data</td>
      <td>Export data</td>
      <td>✅</td>
      <td>✅</td>
      <td>❌</td>
      <td>❌</td>
    </tr>

    <!-- Request History -->
    <tr>
      <td rowspan="4"><strong>Request History</strong></td>
      <td rowspan="2">Local Request History</td>
      <td>View</td>
      <td>✅</td>
      <td>✅</td>
      <td>✅</td>
      <td>❌</td>
    </tr>
    <tr>
      <td>Share</td>
      <td>✅</td>
      <td>✅</td>
      <td>✅</td>
      <td>❌</td>
    </tr>
    <tr>
      <td rowspan="2">Shared Request History</td>
      <td>View</td>
      <td>✅</td>
      <td>✅</td>
      <td>✅</td>
      <td>❌</td>
    </tr>
    <tr>
      <td>Delete</td>
      <td>✅</td>
      <td>✅</td>
      <td>❌</td>
      <td>❌</td>
    </tr>
  </tbody>
</table>
    
</details>

### Setting Project Permissions

1. When sending an invitation, specify the project and set the invitee's permission level.

<details>
<summary>📷 Visual Reference</summary>

<Background>
<img src="https://api.apidog.com/api/v1/projects/544525/resources/343450/image-preview" style="width:400px" />
</Background>

</details>

2. Alternatively, set project-level permissions via My Team → Members → Project Role.

<details>
<summary>📷 Visual Reference</summary>

<Background>
![Team Permissions Settings](https://assets.apidog.com/uploads/help/2023/07/12/88ceafb35503323b0debd1b358ce8d1a.png)
</Background>
</details>


## Custom Roles and Permissions

The **Roles and permissions** feature allows you to customize permissions for specific roles, ensuring they align with the needs of users in various scenarios. Currently, this feature supports custom configurations for project roles only. Customization for team or organization roles is not yet available.

### Customizing Project Roles

If the built-in project roles in Apidog don't meet your specific needs for permission control, you can create custom project roles to address this gap.

:::info[]
This feature is available on [Apidog Enterprise plan](https://apidog.com/pricing/).
:::

To create a custom project role, navigate to the **Team → Members → Roles and permissions** or **Organization → Members → Roles and Permissions**. Click **+ Add** to start creating a custom project role.

<details>
<summary>📷 Visual Reference</summary>

<Background>
![add-team-members-project.png](https://api.apidog.com/api/v1/projects/544525/resources/349329/image-preview)
</Background>

</details>

You can freely set the custom role name, and then select the desired project permissions for it.

<details>
<summary>📷 Visual Reference</summary>

<Background>
![customizing-project-roles.png](https://api.apidog.com/api/v1/projects/544525/resources/349169/image-preview)
</Background>

</details>

**Important Notes:**

1. If you check the "All Permissions" option for a specific module, any new features added to that module will automatically be assigned to the custom role.
2. Default roles (such as Editor or Read-only) cannot be renamed or edited. However, you can copy these roles and modify them to quickly create a new custom role.

