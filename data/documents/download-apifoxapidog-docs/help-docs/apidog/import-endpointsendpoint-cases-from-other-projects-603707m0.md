# Import endpoints/endpoint cases from other projects

The test scenario supports cross-project importing of endpoints and endpoint cases. This means that in addition to referencing endpoints within the current project and importing them as steps, it also supports importing endpoints from other projects as steps to form a complete business process. This feature is crucial for systems or architectures with complex business processes.

## Importing endpoints

Click on the "+ Add Step" or any `+` button in any test step section and select an endpoint from another project to import. When importing endpoints from other projects, only the "Manual" mode is supported, and this action does not affect the endpoint cases data in the original project.


:::highlight purple
For the difference between the "Manual" and "Automated" modes, please refer to [here](https://docs.apidog.com/sync-data-from-endpointsendpoint-cases-603709m0.md).
:::

![Import Endpoint](https://assets.apidog.com/uploads/help/2024/04/03/3540ff734e0019ae84df6d40fce86f26.png)

When you select another project and import data from that project as test steps for the first time, the product page will guide you to perform an **"Environment association"** setting. This ensures that these steps can run normally and avoid unexpected issues with using the wrong service (base URL) by associating the environment of that other project with the current project's environment. For details, please refer to [Manage the runtime environment of APIs from other projects](https://docs.apidog.com/manage-the-runtime-environment-of-apis-from-other-projects-603705m0.md).

![Environment Association](https://assets.apidog.com/uploads/help/2024/04/03/ecdeb2abe38dde17078409f9c107d6a6.png)


:::tip[]
When importing from other projects or when running test scenarios containing endpoints from other projects, you must have at least `read-only` access to that project. For more details about project permissions, please refer to [member permissions settings](https://docs.apidog.com/member-roles-permission-settings-616186m0.md).

:::

## Importing endpoint cases

Click on the project name and select an endpoint case from another project to import. When importing endpoint cases from other projects, only the **"Reference"** mode is supported. This means it is a one-way import and does not affect the endpoint cases data in the original project.

- **Reference**

  The endpoint cases will be imported in the **"Reference"** mode. The parameter names and parameter values in the endpoint cases will be copied to the test steps, and the data will be completely independent from the endpoint cases in the original project. Any changes made on either side will not affect the other. If you want to associate the test steps with the endpoint documentation in the original project, you can click the "Sync Now" button to sync the parameter names from the endpoint documentation.

To ensure data stability and independence, these endpoints and endpoint cases imported from external projects only support the "Manual" mode for synchronizing data with the endpoint documentation in the original project.

![Import Endpoint Cases](https://assets.apidog.com/uploads/help/2024/04/03/191b623663723ceedf72fdebb80760ee.png)

:::important
Steps imported from other projects can only be manually synchronized to ensure the stability of test step data. Without that, you cannot reference them.
:::

This retouched version includes clearer headings, improved readability, and structured information to help users effectively import endpoints and endpoint cases from other projects into their test steps.
