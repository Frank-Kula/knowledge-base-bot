# Onboarding Guide

To get started using Apidog within your organization, you can follow through the following tasks to set your Apidog team up for success. It's recommended that you first collaborate with your Team Admins and your organization's IT team to set up, secure, and manage Apidog in your organization. Then you can set up your Apidog team by configuring relevant settings, inviting people to your team and assigning them roles, and creating resources related to your projects.

You can [download and install](https://apidog.com/download/) the Apidog desktop app for Windows, Mac, and Linux. You can also access Apidog on the web with the [Apidog Agent](https://app.apidog.com/main).

## Collaborate with Your IT Team

Contact your IT team to establish the procedure for adding a new piece of software, which varies from organization to organization. The following topics are common:

- Your IT team may need to add an exception to device policy allowing for Apidog to be installed on employee workstations. Provide a [Apidog download link](https://apidog.com/download/) to the IT team to help establish this exception.

- If your organization's network connection is behind a proxy, you may need to configure Apidog appropriately. Retrieve proxy connection details from your IT team and set them up within Apidog.

  :::info
  If you are already logged into Apidog, you can set up a proxy by navigating to the **⚙Settings → Proxy** option located in the top right corner of the Apidog interface. Alternatively, if you are not logged into Apidog yet, you can configure the proxy settings in the bottom left corner of the login screen in the Apidog client application.
  :::

- If your organization operates behind a firewall, your IT team may need to configure allowlists for Apidog's domains. This ensures Apidog data is synced with the cloud and all functionality works as expected.

  :::info
  Apidog's domains include:
  - *.apidog.com
  - *.apidog.io
  :::

## Set Up Apidog Team

First, you need to decide which member in your organization will be the Team Admin. The Team Admin can register an Apidog account, [create a new team](https://docs.apidog.com/managing-teams-612998m0.md), and automatically become the **Team Owner** of this new team.

The team owner has the following permissions:

- Modify team information
- Create new project
- Invite and remove members
- Set team permissions and project permissions for other members
- Manage subscriptions and payments
- Transfer and dissolve the team

A team can consist of multiple members and manage various projects. Administrators have the authority to determine which members have which permissions within specific projects.

In the Apidog free version, a team can have a maximum of 4 members. If your team exceeds 4 members, you will need to [upgrade to the paid plan of Apidog](https://apidog.com/pricing).

## Manage Team Members

The team owner can invite a few other members to be team admins, who will then be responsible for inviting and managing additional collaborative members within the team.

Team admins can [invite other members](https://docs.apidog.com/managing-team-members-613028m0.md) to join the team via email or invitation links. When inviting members to join, they can set the default permissions for the members regarding projects within the team. These permissions typically include Admin, Editor, Read-only, and Forbidden.

It is important to note that in Apidog, [Team permissions and Project permissions](https://docs.apidog.com/member-roles-permission-settings-616186m0.md) are distinct authorization levels. Team permissions are utilized for managing the team as a whole, encompassing Team settings, member management, and overall team governance. Team permissions include roles such as Team owner, Team Admin, Team member, and Guest.

On the other hand, Project permissions are specifically tailored for managing individual projects within the team. These permissions govern aspects related to project settings, access control, and collaboration within the project scope. Project permissions consist of roles such as Admin, Editor, Read-only or Forbidden, which dictate the level of control and access team members have within a particular project.

## Create Projects

Team owners and team admins can [create new projects](https://docs.apidog.com/managing-projects-613025m0.md) within the team. When creating a project, you can specify the project name and description, and select the appropriate project template based on your needs.

After creating a project, you can invite team members to join the project and assign them appropriate project permissions. This allows team members to collaborate on the project and access project resources based on their assigned permissions.

## Migrate Data

If you are [migrating](https://docs.apidog.com/migration-guide-overview-633036m0.md) from another API management tool to Apidog, you can import your existing API data into Apidog. Apidog supports importing data from various formats, including OpenAPI/Swagger, Postman, and more.

To import data, navigate to the project settings and select the **Import Data** option. Choose the appropriate import format and follow the on-screen instructions to complete the import process.

## Configure Initial Settings

After setting up your team and creating projects, you can configure initial settings to customize Apidog to your organization's needs. This includes:

- **Team Settings**: Configure team-level settings such as team name, description, and avatar.
- **Project Settings**: Configure project-level settings such as project name, description, and default environment.
- **Environment Variables**: Set up environment variables to manage different environments (e.g., development, staging, production).
- **Notification Settings**: Configure notification settings to receive alerts for important events.

By following these steps, you can set up Apidog within your organization and start collaborating on API design, development, and documentation with your team.

