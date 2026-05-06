# Data backup

At Apidog, we prioritize the security and availability of your data with robust backup measures, utilizing Amazon Web Services (AWS) data centers for secure storage. Continuous backups are performed every minute to ensure data integrity.

Additionally, you have the option to export your data in various formats such as OpenAPI Specification, HTML, Markdown, and more to be added in future updates. Regular backups and secure storage practices are recommended to safeguard your valuable information against unforeseen events.

## Export Data

Apidog supports comprehensive data export capabilities for individual APIs, API collections, or entire projects. Detailed steps can be found in our [Export Data guide](https://apidog.com/help/import/export-data).

1. Navigate to `Settings` and access the Export data tab on the left-hand side.

   ![](https://assets.apidog.com/uploads/help/2023/07/18/a5de9c1aeb6185c73a6f474730528fbe.png)

   Here, you will see various export parameters. For example, we suggest selecting version 3.2 for OpenAPI exports.

2. Choose the specific API or APIs you wish to export:

   - **Single API Export:** Click on "Export selected," select the desired API(s) via tags, then confirm.
   
     ![](https://assets.apidog.com/uploads/help/2023/07/18/9545ee7e36aad5b7356df3988c44a182.png)

   - **API Collection Export:** Click on "Export selected," choose the necessary folder(s), and confirm.

     ![](https://assets.apidog.com/uploads/help/2023/07/18/314aa999c0965f950a8d5a73835a0db5.png)

3. Specify the environment applicable for the export, like development or testing.

   ![](https://assets.apidog.com/uploads/help/2023/07/18/e6eb66c00782aad830331046e98a553a.png)

4. Opt to export as a JSON file or publish via an open URL, based on your needs.

   ![](https://assets.apidog.com/uploads/help/2023/07/18/669247a2bb8f9c983cbbfabc8faebe02.png)

## Restore Your Data

In case of accidental deletions or required rollbacks, Apidog provides multiple restoration options from both the trash and the change history records.

### Restore Data From Trash

1. Open the `APIs` screen and click on the Trash icon on the left.

   ![](https://assets.apidog.com/uploads/help/2023/07/18/b534128ad80a831c0d91bf9d87537420.png)

2. Choose the data to restore, supporting batch operations.

3. Hit the `Restore` button.

   ![](https://assets.apidog.com/uploads/help/2023/07/18/dca634ab614788becba6bad52fffec02.png)

### Restore Data From Change History

1. For an API with change history, open the API and click the history icon in the top right.

   ![](https://assets.apidog.com/uploads/help/2023/07/18/3e44b964f4ae3019e2b0f53b787e6df5.png)

2. Compare the pre and post-modification versions, then select the version you wish to restore.

3. Press the `Revert` button.

   ![](https://assets.apidog.com/uploads/help/2023/07/18/8b2b0be1a6b2ca9d58a7549c42541f5f.png)

:::tip
Restoring from the change history creates a new version of the data, while restoring from the trash reinstates the original version.
:::

Regular data backups are crucial to prevent loss and ensure accessibility to essential information in unexpected situations.

## Data Deletion Solutions

Mistakes happen, but we're here to assist. Our system maintains comprehensive backups, enabling us to restore a snapshot of your data from the past 30 days upon request. If you require data recovery assistance, please reach out to us at support@apidog.com.
