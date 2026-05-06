# Managing Organization



In Apidog, an organization is used to centrally manage multiple teams and members. With organizations, you can control permissions, assign roles, and ensure efficient collaboration across your company.

## Creating an Organization

You can create one or more organizations. To create a new organization:

1. In the main window, click **Organizations** from the left navigation panel to open the organization management page.

2. Click the **+ New Organization** button at the bottom left.

<details>
<summary>📷 Visual Reference</summary>

<Background>  
![image.png](https://api.apidog.com/api/v1/projects/544525/resources/362140/image-preview) 
</Background>

</details>

3. Enter the organization name.

<details>
<summary>📷 Visual Reference</summary>

<Background>  
<img src="https://api.apidog.com/api/v1/projects/544525/resources/362143/image-preview" width="460px"/>  
</Background>

</details>

4. Click **Create**. Your new organization is now set up.

## Organization Members and Roles

You can invite members into your organization and assign them different roles:

- **Org Admin**: Has the highest permissions (except the org owner). Can manage organization members, teams, and organization settings.
- **Org Member**: Can join the organization and its teams, and collaborate on projects. Cannot change organization settings.

### Inviting Members

To invite members into the organization:

1. Go to **Members** under your organization.

<details>
<summary>📷 Visual Reference</summary>

<Background>
<img src="https://api.apidog.com/api/v1/projects/544525/resources/362127/image-preview"/> 
</Background>

</details>

2. Click **Invite**, enter their emails to send an invitation, or share the invite link.

<details>
<summary>📷 Visual Reference</summary>

<Background>
<img src="https://api.apidog.com/api/v1/projects/544525/resources/362130/image-preview" width="460px"/> 
</Background>

</details>

### Custom Project Roles

With the [Enterprise](https://apidog.com/pricing) plan, you can also use [custom project roles](https://docs.apidog.com/member-roles-permission-settings-616186m0.md#custom-roles-and-permissions) to control what project members can do.

<details>
<summary>📷 Custom Roles Examples</summary>

<Background> 
<img src="https://api.apidog.com/api/v1/projects/544525/resources/362131/image-preview"/>  
</Background>

<Background>
<img src="https://api.apidog.com/api/v1/projects/544525/resources/362132/image-preview"/> 
</Background>

</details>

## Relation Between Organizations and Teams

- **Organization**: The highest-level management unit, representing a company or large group. It manages multiple teams.
- **Teams**: A sub-unit within an organization, usually a department or smaller group. It manages multiple projects.

## Organization vs. Team — Which Should You Choose?

When using Apidog, a common question is: should you manage everything directly under an **Organization**, or mainly rely on **Teams**? The answer really comes down to two things — team size and business scope.

### If Your Team is Small and Focused

Say you've got around ten people all working on the same product line. In that case, a single **Team** is more than enough. A Team can handle projects, APIs, and members in one place — simple and efficient, without the extra overhead of an Organization.

### If Your Company is Large and Spread Out

If you've got lots of people and multiple, unrelated business lines, it's best to create an **Organization** first, then set up separate **Teams** inside it for each business area. Each Team manages its own projects and members, with clear boundaries and no overlap.

## Updating Organization Info

Admins can update the organization's name or details from **Settings**. All members will see the updated info.

<details>
<summary>📷 Visual Reference</summary>

<Background>  
<img src="https://api.apidog.com/api/v1/projects/544525/resources/362133/image-preview"/> 
</Background>

</details>

## Transferring the Organization

The organization owner can transfer ownership to another member via **Organization Settings** → **Danger Zone** → **Transfer**.

<details>
<summary>📷 Visual Reference</summary>

<Background>  
<img src="https://api.apidog.com/api/v1/projects/544525/resources/362134/image-preview"/> 
</Background>

</details>

## Dismissing the Organization

The organization owner can permanently delete the organization under **Organization Settings** → **Danger Zone** → **Dismiss Organization**.

<details>
<summary>📷 Visual Reference</summary>

<Background>
<img src="https://api.apidog.com/api/v1/projects/544525/resources/362136/image-preview"/> 
</Background>

</details>

:::warning
Dismissing an organization is permanent and cannot be undone. All teams and projects within the organization will be deleted.
:::

