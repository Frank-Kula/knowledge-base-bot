# How to enable cloud mock in Apidog?

Cloud mock is an essential feature for teams that require a continuously available mock endpoint. Unlike local mocks, which are served from the user's machine and become unavailable when the computer is turned off, cloud mocks provide a persistent and accessible solution for teams. Here are some key aspects and use cases of cloud mocks:

1. Team-wide accessibility: All members of a team share the same cloud mock URL, promoting collaboration and consistency.
2. Continuous availability: Cloud mocks remain accessible 24/7, regardless of individual team members' computer status.
3. Ideal for public API documentation: Can be used to create sandbox environments for public-facing API documentation.
4. Non-production data source: Serves as a reliable data source for non-production environments.

## Enabling cloud mock

To enable cloud mocks for your project:

1. Navigate to "Project Settings"
2. Select "Mock Settings"
3. Toggle on the "Cloud Mock" feature

![image.png](https://api.apidog.com/api/v1/projects/544525/resources/343629/image-preview)

## Using cloud mocks

Once enabled, you can access and use cloud mocks in the following ways:

1. Visit the endpoint and click on the "Cloud Mock" button in the Mock tab to obtain the cloud mock URL.
2. Use the "Request" button to instantly retrieve response data.
3. For GET requests, you can directly access the cloud mock URL in a web browser to view the response data.

## Implementing access control

Cloud mocks support access control through token authentication:

1. Go to "Project Settings" - "Mock Settings"
2. Set the access permission to "Token Authentication"

To use the authenticated cloud mock:

1. Append the token to the request URL:
   ```
   https://mock.apidog.com/m1/2689726-0-default/users?apidogToken=GdfNrEm6lxM9nDGGIMCWC1OPSiZ6hGOi
   ```

2. For Quick Requests, add the `apidogToken` parameter to the Header parameters.

3. For form-data and x-www-form-urlencoded requests, add the `apidogToken` parameter to the Body parameters.

By implementing cloud mocks, teams can ensure consistent and always-available mock endpoints for their API development and testing processes. This approach streamlines collaboration, improves documentation, and provides a reliable data source for non-production environments.
