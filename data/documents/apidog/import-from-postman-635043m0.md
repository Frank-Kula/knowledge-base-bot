# Import from Postman

:::tip[] 
For a detailed feature-by-feature comparison of Apidog and Postman, please see this page: [Apidog vs. Postman](https://apidog.com/compare/apidog-vs-postman/).
:::

## Video Tutorial

<Video src="https://youtu.be/D86mzmChgIE?si=PuZmHWQOEWiywzd5"></Video>

## Conceptual Mapping

Understanding how Postman concepts map to Apidog is crucial for a smooth migration.

| Postman Concept | Apidog Equivalent | Notes |
| :--- | :--- | :--- |
| **Collection** | **Project** / **Module** | Can be imported as a full Project or an inner Module depending on import scope. |
| **Request** | **API Endpoint** | A standard HTTP request becomes a structured API documentation endpoint. |
| **Environment** | **Environment** | Works identically. Key-value pairs for different stages (Dev, Prod, etc.). |
| **Collection Variable** | **Module Variable** | Variables scoped to the collection map to Apidog's Module-level variables. |
| **Pre-request Script** | **Pre-processor** | Scripts running before the request. |
| **Post-response Script** | **Post-processor** | Scripts running after the request (assertions, variable setting). |


## Phase 1: Export Data from Postman

### 1. Exporting a Collection
1.  Open **Collections** in the left sidebar.
2.  Click the `...` icon next to the collection and select **Export**  under **More**.
3.  Choose **Collection v2.1** (Recommended) and save the JSON file.

:::info[Batch Exporting Multiple Collections]
You can batch export multiple Postman collections using the steps below:
- Click your **account avatar** in the top-right corner of Postman and select **Settings**.
- Under **Account Settings**, click **Export Data**.
- Create a new export request and select **Collections** and **Environments** as needed.
- Download the export file from the email Postman sends you.

Importing these collections is straightforward. Extract the folders from the `zip` file you received, then follow the same procedure described below to import your collections.
:::


### 2. Exporting an Environment (Optional)
If your collection uses environment variables, you should export the environment too.
1.  Go to **Environments** in the left sidebar.
2.  Click `...` next to your environment and select **Export**.
3.  Save the JSON file.


## Phase 2: Import Data into Apidog

### 1. Import the Collection
1.  Open **Settings** > **Import Data** in your Apidog project or click on **Import Project** button on the **Team Page**.
2.  Select **Postman** and upload your Collection JSON file (or folder, if you have both collection and environment files).


### 2. Match the Environment Variables
If you imported an Environment JSON along with the Collection:
- On the Import Preview screen, choose whether or not `baseURL` should be included with endpoint urls.
- If `baseURL` is not included in endpoint urls, make sure the environment `baseURL` is set properly. 


### 3. Verify Migration
Once imported, check that your variables are correctly mapped. You can then select the imported environment (or create a new one, if you didn't import) and make requests.


---

:::tip[Detailed Guide]
For a deeper dive into complex migration scenarios, check out our blog: [How to Migrate Postman Collections to Apidog](https://apidog.com/blog/migrate-postman-enviornments-collection-to-apidog/)
:::

