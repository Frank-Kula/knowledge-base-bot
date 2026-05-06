# API Versions in Apidog

As APIs evolve to meet market demands and leverage technological advances, version management becomes essential. Open APIs serve as crucial channels for technical teams to deliver services and data externally. However, business evolution and technological progress inevitably lead to multiple version iterations of your endpoints. This change is natural and necessary as teams optimize functionalities, introduce new features, and address bugs.

Managing multiple API versions is crucial for serving different user groups while ensuring both compatibility and innovation. This approach allows teams to deliver stable, evolving services while maintaining version control, minimizing disruptions for existing users, and ensuring business continuity and reliability.

## Use Case

Teams may need to offer multiple API versions concurrently—such as the latest, stable, and long-term maintenance versions—to ensure minimal disruption for users on older versions.

## Highlights of API Version Feature

- **Full Version Creation**

  A new API version can be created based on an existing API version, containing copies of all endpoints from the original version. After creation, each endpoint within the version can be modified as needed. Alternatively, you can start from a blank API version and manually add endpoints.

- **Comprehensive Sharing**

  Select one or more API versions from your project to publish. All endpoints within the selected versions will be visible to users. When publishing, the API version's display name and slug settings can be configured to enhance reader experience.

- **One-Click Switching**

  If multiple API versions have been published, users can switch between them via a version selector located next to the project name on the public page. Clicking on a version will display all related endpoints and content for that specific version.

:::tip[Difference Between "API Version" and "Sprint Branch"]

- **API Version**: Designed for external release, especially when major changes cause significant incompatibilities between versions. Contains all endpoints, not just modified or newly added ones

- **Sprint Branch**: Used internally by development teams, aligning with the "sprint" concept in agile development. Each sprint typically creates a branch including only new or modified endpoints, excluding unchanged ones

:::
