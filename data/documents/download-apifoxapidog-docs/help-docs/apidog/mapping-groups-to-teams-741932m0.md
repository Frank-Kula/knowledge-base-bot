# Mapping Groups to Teams

Apidog does not support creating or deleting groups using SCIM. However, mapping an identity provider (IdP)'s group to a team within your Apidog organization via SAML is supported.

Updated Text: Here is a step-by-step video tutorial on how to enable Apidog SAML Group Mapping using Microsoft Entra ID (Azure AD) as an IdP.

<Video src="https://www.youtube.com/watch?v=kjcyQmA8sLw"></Video>


## Modifying Claim of SSO

To support group mapping via SAML, you should add a group claim of SSO:

1. Open your Microsoft Entra ID management portal in a browser.
2. Go to **Enterprise applications** and open your enterprise application.
3. On the application's **Overview** page, click **Set up single sign on**, and edit **Attributes & Claims**.

<details>
<summary>📷 Visual Reference</summary>

<Background>
![mapping-groups-step-1.png](https://api.apidog.com/api/v1/projects/544525/resources/347379/image-preview)
</Background>

</details>

4. Click **Add a group claim**, select **All groups**, check **Customize the name of the group claim**, and set "Name" to "groups".

<details>
<summary>📷 Visual Reference</summary>

<Background>
![mapping-groups-step-2.png](https://api.apidog.com/api/v1/projects/544525/resources/347380/image-preview)
</Background>

</details>

After this setting, when a user signs in with SSO, Apidog can obtain the unique identifier (object id) of the group to which the user belongs. In addition, Apidog will NOT obtain any information about any groups in Azure.

## Configuring Mapping

Next, we can configure the mapping between group and team:

1. Open the **Groups** page of Microsoft EntraID, you can find that each group has a **Name** and **Object Id**.

<details>
<summary>📷 Visual Reference</summary>

<Background>
![mapping-groups-step-3.png](https://api.apidog.com/api/v1/projects/544525/resources/347381/image-preview)
</Background>

</details>

2. Open the SAML Group page in the organization settings of Apidog, then you can paste the name and id of the Azure group.
3. Set the permissions of members of this Azure group on each Apidog team.

<details>
<summary>📷 Visual Reference</summary>

<Background>
![mapping-groups-step-4.png](https://api.apidog.com/api/v1/projects/544525/resources/347382/image-preview)
</Background>

</details>

When a user signs in with SSO, the corresponding team access permissions will be granted according to the configuration.

