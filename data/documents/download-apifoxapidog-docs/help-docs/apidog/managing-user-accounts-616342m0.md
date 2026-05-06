# Managing User Accounts

:::info
SSO is available on [Apidog Enterprise plan](https://www.apidog.com/pricing).
:::

## Joining Organizations via SSO

When a new user successfully logs in to Apidog via SSO, if there are available seats within the organization, the new user will automatically join the corresponding organization.

There are two ways to log in via SSO:

- Access the organization's SAML authentication page directly through a browser. The format of this URL is `https://apidog.com/orgs/{org-name}/sso`, please replace "{org-name}" with your real organization's name.
- If the organization's owner has configured the `allowed email domains`, users can click **Sign in with SSO** on the login page and enter their work email to access to the SAML authentication page.

<details>
<summary>📷 Visual Reference</summary>

<Background>
![](https://assets.apidog.com/help/assets/images/sign-in-with-sso-424262813c25c255c89651034620b9a1.png)
</Background>

</details>

When users join an organization automatically through SSO login, they are granted organization member permissions by default but are not assigned with any teams within the organization. The organization owner needs to manually assign these members to the corresponding teams to grant them access to projects.

## Adding Existing User Accounts

If someone already has an Apidog account, the organization owner can invite them to join a team within the organization. Once they accept the invitation, they become members of the organization and are assigned to the corresponding team.

<details>
<summary>📷 Visual Reference</summary>

<Background>
![](https://assets.apidog.com/help/assets/images/invite-members-8484e1cb712fbb8cb32287cea50be73d.png)
</Background>

</details>

## Managing Organization Members

Organization owners can view the profiles of organization members, including their linked SSO identities, and can also assign organization members to teams. Organization members can only access projects within teams they are assigned to.

<details>
<summary>📷 Visual Reference</summary>

<Background>
![](https://assets.apidog.com/help/assets/images/manage-member-permissions-09ed14bded0e9ea9fe76cfdec2db2ad6.png)
</Background>

</details>

