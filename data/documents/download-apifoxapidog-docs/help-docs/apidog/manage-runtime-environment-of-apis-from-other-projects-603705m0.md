# Manage Runtime Environment of APIs from Other Projects

## Associating the running environment with other projects

When you select another project and import its APIs as test steps for the first time, you need to ensure these steps can execute properly and avoid issues with service URLs (Base URL). The popup will guide you through an **"environment association"** setup, which links the environment of the other project with the current project's environment.

<Background>
![Environment Association](https://assets.apidog.com/uploads/help/2024/04/03/569b3cd5a2aca315e3f24e3c405aa0f2.png)
</Background>

## Managing the running environment for APIs from other projects

You can view and manage the environment associations between the current project and other projects whose APIs have been imported as test scenario steps in the environment association function.

- When importing APIs from other projects into test steps, click **"Environment association"** to manage these associations.

<Background>
![Manage Environment Association](https://assets.apidog.com/uploads/help/2024/04/03/5aedd313c2b909d996d836913eabed90.png)
</Background>

- If the current test scenario has already imported APIs from other projects, a prompt will appear in the running environment of the functional testing, allowing you to manage it.

<Background>
![Functional Testing Prompt](https://assets.apidog.com/uploads/help/2024/04/03/680569eb10caeb707ba46f1f6259afd1.png)
</Background>

Inside the environment association function, you can see all imported projects along with their environment associations with the current project and the specific services (Base URLs).

<Background>
![Imported Projects](https://assets.apidog.com/uploads/help/2024/04/03/2cb8d6a1afa3c9c6a6372dc4c5a78fa5.png)
</Background>

## Permission control for steps imported from other projects

Click the **"Members"** tab on the homepage to view or manage team members' permissions. If you do not have read or higher permissions for the target project, you cannot view or edit the APIs (test cases) imported from that project.

<Background>
![Manage Permissions](https://assets.apidog.com/uploads/help/2024/04/03/f43cc954decdfb30d4a3dbe048775046.png)
</Background>

### Viewing/editing step details of imported APIs

To view or edit APIs imported from other projects into test steps, the operator needs to have **"Read-Only"** or higher permissions for the target project.

<Background>
![View/Edit Imported APIs](https://assets.apidog.com/uploads/help/2024/04/03/e92a82ca9088e51cba30ab2d6c59360b.png)
</Background>

If you do not have the necessary permissions, you cannot view or edit the API.

<Background>
![Permission Denied](https://assets.apidog.com/uploads/help/2024/04/03/5adc83eec64c54c8e8010d5d932547de.png)
</Background>

### Running test scenarios containing APIs from other projects

To run test scenarios containing APIs from other projects, the operator needs to have "Read-Only" or higher permissions for all imported projects. If you do not have access permissions for a particular project, you cannot run the test scenario.

<Background>
![Run Test Scenarios](https://assets.apidog.com/uploads/help/2024/04/03/f9d5561b4d7aa70480807eccadc6be12.png)
</Background>

## Manually synchronizing environment association data from other projects

To ensure data consistency, if the APIs or running environments in other projects have been updated, you can click **"Check the running methods of these steps"** → **"Update"** button to refresh the cross-project data in the current test scenario.

<Background>
![Synchronize Data](https://assets.apidog.com/uploads/help/2024/04/03/b79ab50728dbb4a4e2eef9fa5e1b1059.png)
</Background>

This retouched version provides clearer headings, improved readability, and structured information to help users manage the runtime environment of APIs from other projects effectively.
