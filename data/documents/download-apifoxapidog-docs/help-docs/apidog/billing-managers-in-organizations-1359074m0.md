# Billing Managers in Organizations

You can assign the "Billing Manager" role to your organization, allowing designated users to help upgrade the plan, purchase seats, and perform other billing-related actions.

If your team is not part of an organization, please refer to [Billing managers in a team](https://docs.apidog.com/managing-team-members-613028m0.md#billing-managers).

<details>
<summary>📷 Visual Reference</summary>

<Background>
![image.png](https://api.apidog.com/api/v1/projects/544525/resources/359830/image-preview)
</Background>

</details>

## Managing Billing Managers in an Organization

:::caution
Only the organization owners, admins, or current billing managers can invite other users to join the organization as "Billing Managers".
:::

At the bottom of the "Plans Management" page in your organization, you can view the current billing managers list and manage them.

Click the **Invite** button to open a pop-up window. Enter one or more email addresses. An invitation to become a billing manager in the organization will be sent to those emails. The invitee must log in to the Apidog account linked to the invitation email and accept the invitation to officially join the organization as a billing manager. Invitations are valid for 7 days and cannot be used after they expire.

<details>
<summary>📷 Visual Reference</summary>

<Background>
![image.png](https://api.apidog.com/api/v1/projects/544525/resources/359832/image-preview)
</Background>

</details>

From the billing managers list, you can remove a specific billing manager. Once you click **Remove** and confirm, that billing manager will no longer have access to the organization in this role.

<details>
<summary>📷 Visual Reference</summary>

<Background>
![image.png](https://api.apidog.com/api/v1/projects/544525/resources/359834/image-preview)
</Background>

</details>

## Billing Manager Permissions

Billing managers will **have the ability** to:

✅ View the usage dashboard  
✅ Upgrade, renew, expand, or change the paid plan  
✅ Add, update, or remove payment methods  
✅ View payment history  
✅ Request invoices  
✅ View a list of billing managers  
✅ Invite additional billing managers  
✅ Remove other existing billing managers

Billing managers will **not be able to**:

❌ Create, access, or modify projects, resources, activities, or settings within your organization  
❌ See members of your organization  
❌ Be seen in the list of organization members

In the product interface, when accessing an organization as a billing manager, you will only see the "Plans Management" page for that organization, as shown below:

<details>
<summary>📷 Visual Reference</summary>

<Background>
![image.png](https://api.apidog.com/api/v1/projects/544525/resources/359839/image-preview)
</Background>

</details>

You cannot view the list of teams under this organization either.

<details>
<summary>📷 Visual Reference</summary>

<Background>
![image.png](https://api.apidog.com/api/v1/projects/544525/resources/359841/image-preview)
</Background>

</details>

## Notes

1. To invite a user as a billing manager in an organization, you need an email address registered with an Apidog account:
   - If the email is already registered with Apidog, the user can log in and accept the invitation to join as a billing manager
   - If the email is not registered, the user will be prompted to sign up for an Apidog account, log in, and then join as a billing manager
   - If you log in with a different Apidog account (not linked to the invited email), you'll see an "Invalid Invitation Link" warning when accepting the invite. This helps prevent misuse and ensures security

2. An organization can have multiple billing managers. They can **remove each other** from the organization and invite new billing managers.

3. A user can be both a regular member (e.g., admin, member, etc.) and a billing manager in an organization. In that case, their permissions in the organization will be the combined set of both roles.

