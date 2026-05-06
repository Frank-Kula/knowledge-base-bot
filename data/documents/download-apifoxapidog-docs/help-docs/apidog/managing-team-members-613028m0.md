# Managing Team Members

The member management feature in Apidog enables you to manage user collaboration within your team by assigning specific permissions. Only team owner and admins have the authority to manage these settings. Other team members can view the list of team members and their basic information but cannot make any changes.

When you need to collaborate on an API project, you can invite team members or external collaborators to work together.

## Inviting Users to Join the Team

To invite members, go to **Members** and click on **Invite** at the top right.

:::tip[]
Only team admins and team owner can send invitations. Project admins, even if they manage a specific project, cannot invite members to the team.
:::


<Background>
![inviting-users-to-teams.jpg](https://api.apidog.com/api/v1/projects/544525/resources/349124/image-preview)
</Background>


### Invitation Methods

There are two methods to invite members to the team:

- **Invite via Link**: Copy the invitation link and share it with users to join the team. When joining through this link:
  - The user's team role is automatically set to `Team Member`.
  - Their permissions for all team projects are determined by the project role you assign during the invitation.

- **Invite via Email**: Enter one or more email addresses and send an invitation.
  - Apidog will email the recipients, prompting them to register (if they are not Apidog users yet) and join the team.
  - Their permissions for all team projects are determined by the project role you assign during the invitation.

## Inviting Users to Join Specific Projects

Users with invitation permissions can invite external collaborators to edit specific projects without granting access to other team projects. To do so, click on **Invite** on the left side of the project page.


<Background>
![invite-team-users-join-specific-projects.jpg](https://api.apidog.com/api/v1/projects/544525/resources/372065/image-preview)
</Background>


There are three ways to invite other users to join the current project. While the two methods are similar to the ones used to invite members to teams, the third method allows selecting users from the team.

:::note[Note]
- Invitations sent from a project are limited to that project only.
- For other projects in the team, permissions default to `Forbidden`, meaning the invited member cannot view them.
:::

<details>
<summary>📷 Visual Reference</summary>

<Background>
![inviting-users-join-project.jpg](https://api.apidog.com/api/v1/projects/544525/resources/372066/image-preview)
</Background>

</details>

### Guests

Users who gain project access through "Project Invitations" are considered **guests** at the team level.

Guests can only see the projects they're invited to. Use "Project Invitations" to allow external collaborators to edit specific projects without accessing other team projects.

Guests have the same team permissions as team members, but are excluded from permission settings for newly created team projects.

:::info[]
**Guests** are also counted as team members and will be billed according to the total number of team members.
:::

## Managing Team Member Details & Permissions

Click the settings button on the right of a member's name to open the member details page.


<Background>
![member-setting-page-entry.jpg](https://api.apidog.com/api/v1/projects/544525/resources/349131/image-preview)
</Background>


There, you can configure more advanced settings.

<details>
<summary>📷 Visual Reference</summary>

<Background>
![manage-member-details.jpg](https://api.apidog.com/api/v1/projects/544525/resources/349130/image-preview)
</Background>

</details>

1. **Nickname**: Assign a nickname for easier identification. The member can also change it.
2. **Role**: Set a member's **team role** to control their access to team functions, such as inviting or removing members and creating projects.
   - New members are assigned the "Team Member" role by default.
   - Be cautious when assigning "Team Admin" roles, as it can impact data security.
3. **Project Role**: Set the member's role for each project in the team, defining what they can do in each project. [Check out member roles & permission settings.](https://docs.apidog.com/member-roles-permission-settings-616186m0.md#project-roles-and-permissions)
4. **Remove Member**: You can remove members from the team. Once removed, they will no longer have access to your team's data.

## Billing Managers

If your team is not part of an organization, you can assign the "Billing Manager" role to certain users so they can help your team upgrade plans, purchase seats, and manage other billing activities.

:::tip[]
For instructions on setting a billing manager in an organization, see [Billing managers in organization](https://docs.apidog.com/billing-managers-in-organizations-1359074m0.md).
:::

### Managing Billing Managers in a Team

:::caution[]
Only team owners, admins, or current billing managers can invite other users to join the team as a "Billing Manager".
:::

At the bottom of the "Plans Management" page in your team, you can view the current billing managers list and manage them.

<Background>
![image.png](https://api.apidog.com/api/v1/projects/544525/resources/372067/image-preview)
</Background>


Click the **Invite** button to open a pop-up window. Enter one or more email addresses. An invitation to become a billing manager will be sent to those emails. The invitee must log in to the Apidog account linked to the invitation email and accept the invitation to officially join the team as a billing manager. Invitations are valid for 7 days and cannot be used after they expire.

<details>
<summary>📷 Visual Reference</summary>

<Background>
![image.png](https://api.apidog.com/api/v1/projects/544525/resources/359816/image-preview)
</Background>

</details>

From the billing managers list, you can remove a specific billing manager. Once you click **Remove** and confirm, that billing manager will no longer have access to the team in this role.

<details>
<summary>📷 Visual Reference</summary>

<Background>
![image.png](https://api.apidog.com/api/v1/projects/544525/resources/359817/image-preview)
</Background>

</details>

### Billing Manager Permissions

Billing managers will **have the ability** to:

✅ View the usage dashboard  
✅ Upgrade, renew, expand, or change the paid plan  
✅ Add, update, or remove payment methods  
✅ View payment history  
✅ Request invoices  
✅ View a list of billing managers  
✅ Invite additional billing managers  
✅ Remove other existing billing managers

Billing managers **will *not* be able to**:

❌ Create, access, or modify projects, resources, activities, or settings within your team  
❌ See members of your team  
❌ Be seen in the list of team members

In the product interface, if you access a team as a billing manager, you will only see the "Plans Management" page for that team, as shown below:

<details>
<summary>📷 Visual Reference</summary>

<Background>
![image.png](https://api.apidog.com/api/v1/projects/544525/resources/359822/image-preview)
</Background>

</details>

### Notes

1. To invite a user as a billing manager, you need an email address registered with an Apidog account:
   - If the email is already registered with Apidog, the user can log in and accept the invitation to join as a billing manager
   - If the email is not registered, the user will be prompted to sign up for an Apidog account, log in, and then join as a billing manager
   - If you log in with a different Apidog account (not linked to the invited email), you'll see an "Invalid Invitation Link" warning when accepting the invite. This helps prevent misuse and ensures security

2. A team can have multiple billing managers. They can **remove each other** from the team and invite new billing managers.

3. A user can be both a regular team member (e.g., admin, member, etc.) and a billing manager. In that case, their permissions in the team will be the combined set of both roles.

