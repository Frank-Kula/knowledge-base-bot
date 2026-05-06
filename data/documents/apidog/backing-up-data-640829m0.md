# Backing Up Data

Apidog prioritizes data security and availability through robust backup infrastructure and flexible export options. Your data is continuously backed up every minute to Amazon Web Services (AWS) data centers, ensuring integrity and protection against data loss.

Beyond automated backups, you can export your API data in multiple formats (OpenAPI, HTML, Markdown) and restore deleted items from trash or change history. This guide covers data export, restoration methods, and recovery options.

:::info
Apidog automatically backs up your data every minute to AWS data centers. For additional protection, we recommend regularly exporting critical project data to your local system.
:::

## Export Data

Apidog supports comprehensive data export capabilities for individual APIs, API collections, or entire projects. For detailed information, see the [Export Data guide](https://docs.apidog.com/export-data-635117m0.md).

1. Navigate to **Settings** and access the **Export data** tab on the left-hand side.

<Background>
![](https://assets.apidog.com/uploads/help/2023/07/18/a5de9c1aeb6185c73a6f474730528fbe.png)
</Background>

Here, you will see various export parameters. For example, we suggest selecting version 3.2 for OpenAPI exports.

2. Choose the specific API or APIs you wish to export:

   - **Single API Export:** Click **Export selected**, select the desired API(s) via tags, then confirm.
   
<details>
<summary>📷 Visual Reference</summary>

<Background>
![](https://assets.apidog.com/uploads/help/2023/07/18/9545ee7e36aad5b7356df3988c44a182.png)
</Background>

</details>

   - **API Collection Export:** Click **Export selected**, choose the necessary folder(s), and confirm.

<details>
<summary>📷 Visual Reference</summary>

<Background>
![](https://assets.apidog.com/uploads/help/2023/07/18/314aa999c0965f950a8d5a73835a0db5.png)
</Background>

</details>

3. Specify the environment applicable for the export, like development or testing.

<details>
<summary>📷 Visual Reference</summary>

<Background>
![](https://assets.apidog.com/uploads/help/2023/07/18/e6eb66c00782aad830331046e98a553a.png)
</Background>

</details>

4. Opt to export as a JSON file or publish via an open URL, based on your needs.

<details>
<summary>📷 Visual Reference</summary>

<Background>
![](https://assets.apidog.com/uploads/help/2023/07/18/669247a2bb8f9c983cbbfabc8faebe02.png)
</Background>

</details>

## Restore Your Data

In case of accidental deletions or required rollbacks, Apidog provides multiple restoration options from both the trash and the change history records.

### Restore Data From Trash

1. Open the **APIs** screen and click on the **Trash** icon on the left.

<Background>
![](https://assets.apidog.com/uploads/help/2023/07/18/b534128ad80a831c0d91bf9d87537420.png)
</Background>

2. Choose the data to restore, supporting batch operations.

3. Hit the **Restore** button.

<details>
<summary>📷 Visual Reference</summary>

<Background>
![](https://assets.apidog.com/uploads/help/2023/07/18/dca634ab614788becba6bad52fffec02.png)
</Background>

</details>

### Restore Data From Change History

1. For an API with change history, open the API and click the history icon in the top right.

<Background>
![](https://assets.apidog.com/uploads/help/2023/07/18/3e44b964f4ae3019e2b0f53b787e6df5.png)
</Background>

2. Compare the pre and post-modification versions, then select the version you wish to restore.

3. Press the **Revert** button.

<details>
<summary>📷 Visual Reference</summary>

<Background>
![](https://assets.apidog.com/uploads/help/2023/07/18/8b2b0be1a6b2ca9d58a7549c42541f5f.png)
</Background>

</details>

:::tip
Restoring from the change history creates a new version of the data, while restoring from the trash reinstates the original version.
:::

## Data Deletion Solutions

If you've accidentally deleted data and need to recover information beyond the 30-day trash retention period, our system maintains comprehensive backups. We can restore a snapshot of your data from the past 30 days upon request.

For data recovery assistance, please contact us at support@apidog.com.

