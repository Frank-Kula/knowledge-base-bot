# Database Connection

You can configure database connection details in the project settings. Once configured, you can use these connections during endpoint debugging and testing by adding [database operations](https://docs.apidog.com/database-operations-in-apidog-588469m0.md) in the pre/post processors steps. This allows you to read from or write to the database seamlessly.

<details>
<summary>📷 Visual Reference</summary>

<Background>
![database-connection-settings.png](https://api.apidog.com/api/v1/projects/544525/resources/352336/image-preview)
</Background>

</details>

The free version of Apidog supports connecting to the following databases:

- MySQL
- SQL Server: Supports SQL Server 2014 and later versions
- Oracle (Connecting to an Oracle database requires installing [Oracle Client](https://docs.apidog.com/oracle-client-593551m0.md))
- Db2
- PostgreSQL

With an [upgrade](https://apidog.com/pricing/), you can also connect to:

- ClickHouse (Requires **Basic** plan)
- MongoDB (Requires **Basic** plan)
- Redis (Requires **Basic** plan)

## Configuring Database Connection

Follow these steps to set up a database connection in Apidog:

1. Open **Project Settings** → **Database Connections**.

<details>
<summary>📷 Visual Reference</summary>

<Background>
![project-database-connection-settings.png](https://api.apidog.com/api/v1/projects/544525/resources/352338/image-preview)
</Background>

</details>

2. Click **+ New** at the top right corner to create a database connection.

3. Select the database type from the available options, fill in the necessary connection information such as host, port, database name, user name, and password. It is recommended to use **variables** to fill in. Database connections filled entirely with variables can be saved in the cloud for collaboration.

:::danger
**Important!** When using variables for database connections, be mindful of [**data security implications**](#storage-mechanism-and-data-security).
:::

<details>
<summary>📷 Visual Reference</summary>

<Background>
![database-connection-details.png](https://api.apidog.com/api/v1/projects/544525/resources/352367/image-preview)
</Background>

</details>

4. In addition to the local connection method using username and password, you can also establish a more secure connection through SSH tunnel to better protect data transmission.

<details>
<summary>📷 Visual Reference</summary>

<Background>
![database-connection-via-ssh.png](https://api.apidog.com/api/v1/projects/544525/resources/352416/image-preview)
</Background>

</details>

5. Click **Save**, and this connection can be used in pre/post processors.

## Using Database Connection

You can add "Database Operations" in pre/post processors for an endpoint request to reference a database connection. After adding it, you can specify a database connection in "Database Operations".

<details>
<summary>📷 Visual Reference</summary>

<Background>
![database-connection-pre-post-processors.png](https://api.apidog.com/api/v1/projects/544525/resources/352418/image-preview)
</Background>

</details>

Below are the specific steps for database operations:

1. In the **Run** tab (*Design Mode*) or **Request** tab (*Request Mode*), navigate to pre/post processors.

2. Hover over **Add PreProcessor** or **Add PostProcessor** and select **Database Operation**.

<details>
<summary>📷 Visual Reference</summary>

<Background>
![adding-database-operation.png](https://api.apidog.com/api/v1/projects/544525/resources/352419/image-preview)
</Background>

</details>

3. Name the database operation and configure the database connection. Ensure the selected "Database Connection" is correctly set up. [Learn More.](#important-notes)

<details>
<summary>📷 Visual Reference</summary>

<Background>
![configuring databse connection.png](https://api.apidog.com/api/v1/projects/544525/resources/352422/image-preview)
</Background>

</details>

4. Enter the SQL command. Variables such as `{{variables}}` are supported in commands.

5. Enable **Extract Result To Variable** (supports JSONPath) and toggle **Console Log** if needed.

6. Click **Send** to execute the endpoint request, and check the result in the console.

<details>
<summary>📷 Visual Reference</summary>

<Background>
![image.png](https://api.apidog.com/api/v1/projects/544525/resources/352423/image-preview)
</Background>

</details>

If you use **Database Operation** in automated tests—either as a test step or in the pre/post-processors of endpoint requests—you can follow the same steps outlined above to set it up and use it.

:::info
Apidog supports standard SQL queries but does not support complex SQL operations such as stored procedures.
:::

## Important Notes

Before executing database operations via requests, ensure the configured database connection is properly saved:

- If your database connection uses variables and is stored in the cloud, make sure to set the actual database details (like host, username, password, etc.) in the **Current Value** field of the related variables. Alternatively, you can use the set variable method to configure these values dynamically.

<details>
<summary>📷 Visual Reference</summary>

<Background>
![configuring-variables-current-value.png](https://api.apidog.com/api/v1/projects/544525/resources/352424/image-preview)
</Background>

</details>

- If the database connection uses fixed text and is stored locally, you need to enter the actual database details (like host, username, password, etc.) in **Project Settings** → **Database Connection**.

<details>
<summary>📷 Visual Reference</summary>

<Background>
![entering-database-connection-credentials.png](https://api.apidog.com/api/v1/projects/544525/resources/352425/image-preview)
</Background>

</details>

- If you need to run test scenarios with a database connection via **CLI**, [click here for detailed notes](https://docs.apidog.com/installing-and-running-apidog-cli-605135m0.md)
- If you need to run test scenarios with a database connection via **Runner**, [click here for detailed notes](https://docs.apidog.com/general-runner-755233m0.md).

## Storage Mechanism and Data Security

Currently, Apidog offers two ways to store database connections:

- **Stored in Apidog Cloud**: If the database connection is configured entirely using variables, it will be stored as variables on Apidog's cloud server.
- **Stored Locally**: If the database connection is configured using fixed text, it will be stored as plain text in the local configuration file.

### Differences Between Storage Mechanisms

| Storage Mechanism | Storage Method | Advantages | Disadvantages |
|------------------|---------------|------------|---------------|
| Cloud | Use variables in configuration | 1. Enables more convenient collaboration with team members.<br>2. When running test scenarios via CI, Runner, etc., you can use variables to set the database connection details instead of maintaining local files. | ⚠️ When plaintext is used in the initial values of variables, data such as database names and passwords will be transmitted in plaintext to Apidog's cloud servers, posing a data security risk (using current values for variables keeps the data stored locally, eliminating this risk). It is recommended to use [vault variables](https://docs.apidog.com/vault-secret-in-apidog-778134m0.md) to avoid data security risks. |
| Local | Use fixed text in configuration | Locally stored with no security risk | 1. Poor collaboration; each team member must configure the database connection individually.<br>2. When running test scenarios through CI, Runner, or similar tools, you need to maintain a dedicated local file for database connections. |

:::warning
To balance a great user experience with data security, Apidog recommends saving database connections in the cloud and using Vault variables to ensure data safety. It is strongly discouraged to use plaintext in the initial values of variables related to database connections, as this can lead to significant data security risks.
:::

