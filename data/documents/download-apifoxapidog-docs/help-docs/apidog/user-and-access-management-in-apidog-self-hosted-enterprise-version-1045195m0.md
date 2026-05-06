# User and Access Management in Apidog Self-Hosted (Enterprise) Version

### Q1: Why can’t I invite members to Teams via email or a public link in the enterprise/on-premise version of Apidog?
A: In the on-premise version of Apidog, team members cannot be invited via email or public links. This is expected behaviour.
 Instead, users must:
1. Manually register and activate their accounts within your Apidog organization.
2. Once registered, admins can find and invite them to teams or organizations via the Admin Platform.
 For more : [Self-hosting Environment Variables](https://self-hosting.apidog.io/405300m0) 

### Q2: What’s the default behavior when a new project is created — do existing team members automatically get access?
A: No, existing team members do not automatically get access to new projects. Their default role is usually set to “**Forbidden**”, meaning they cannot see or interact with the project until explicitly invited and assigned a role.

### Q3: Can I customize the default role of team members when new projects are created?
A: Yes! Customizing default project roles is supported in Apidog. Once your team has multiple members,(olo member cannot find the setting) you’ll have the option to set a default permission level when creating a new project.
<Background>
![image.png](https://api.apidog.com/api/v1/projects/544525/resources/355511/image-preview)
</Background>
By default, this permission is set to **Forbidden**, meaning team members won’t have access unless explicitly granted. However, you can easily adjust this to match your workflow — whether that’s Editor, Read-only, or Admin.





 
### Q4: How do I manage new users if I want to add to one of the projects in a Team?
A: As mentioned above, the users registered within your organization can be added to teams. 
To add users to a project:

1. Go to the **Team** window.
2. Click the **Members** tab
3. Select the user form the list

<Background>
 ![img_v3_02mm_3658fe7f-d157-4cce-9081-bc2fde088abg.png](https://api.apidog.com/api/v1/projects/544525/resources/355504/image-preview)
</Background>
4. Select the Project you want to add from the dropdown
5. Select access roles you want to assign to the user for the project.

Need help managing users in the Apidog Self-Hosted Enterprise version?
We’re here for you — reach out anytime via our Enterprise dedicated support channels.





