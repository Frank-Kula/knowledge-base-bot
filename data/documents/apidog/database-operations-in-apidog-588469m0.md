# Database Operations in Apidog

Apidog supports direct integration with databases, allowing you to perform CRUD operations within your API workflows. You can execute SQL queries in Pre/Post processors, assert the results, or extract data as variables for use in subsequent requests.

## Getting Started

<Steps>
  <Step>
    **Add Database Processor**
    
    Navigate to the **Pre Processors** or **Post Processors** section of your request and select **Database Operation**.
    
    <Tabs>
      <Tab title="Design-first Mode">
        <Background>
          ![Add Database Processor Design Mode](https://api.apidog.com/api/v1/projects/544525/resources/352194/image-preview)
        </Background>
      </Tab>
      <Tab title="Request-first Mode">
         <Background>
          ![Add Database Processor Request Mode](https://api.apidog.com/api/v1/projects/544525/resources/352193/image-preview)
        </Background>
      </Tab>
    </Tabs>
  </Step>
  <Step>
    **Configure Operation**
    
    Name the operation and select a **Database Connection**.
    
    <Background>
      <p style="text-align: center">
        <img src="https://api.apidog.com/api/v1/projects/544525/resources/342782/image-preview" style="width: 640px" />
      </p>
    </Background>
  </Step>
  <Step>
    **Enter SQL Command**
    
    Input your SQL query. You can use variables like `{{variable}}` within the query.
    
    ```sql
    SELECT * FROM User where username = '{{name}}'
    ```
  </Step>
  <Step>
    **Extract Results (Optional)**
    
    Enable **Extract Result To Variable** to save query results.
    *   **Variable Name**: Name of the variable.
    *   **JSONPath Expression**: Use `$[0].uid` to get the `uid` from the first row.
  </Step>
  <Step>
    **Execute**
    
    Click **Send**. Results are displayed in the **Console**.
    
    <Background>
      <p style="text-align: center">
        <img src="https://api.apidog.com/api/v1/projects/544525/resources/342783/image-preview" style="width: 640px" />
      </p>
    </Background>
  </Step>
</Steps>

:::tip
Apidog supports standard SQL queries but does not currently support complex operations like stored procedures via the visual interface.
:::

## Database Connections

### Supported Databases

| Tier | Supported Databases |
| :--- | :--- |
| **Free** | MySQL, SQL Server (2014+), PostgreSQL, Oracle |
| **Paid** | ClickHouse, MongoDB, Redis |

:::tip
Connecting to an **Oracle** database requires installing the **[Oracle Client](https://docs.apidog.com/oracle-client-593551m0.md)** separately.
:::

### Setting Up a Connection

<Steps>
  <Step>
    Go to **Settings** > **Database Connections**.
    <Background>
    ![Database Settings](https://api.apidog.com/api/v1/projects/544525/resources/342821/image-preview)
    </Background>
  </Step>
  <Step>
    Click **+ New** at the top right.
  </Step>
  <Step>
    Select the database type and enter connection details (Host, Port, Username, Password, Database Name).
    
    <Background>
      <p style="text-align: center">
        <img src="https://api.apidog.com/api/v1/projects/544525/resources/342822/image-preview" style="width: 640px" />
      </p>
    </Background>
  </Step>
  <Step>
    (Optional) Configure **SSH Tunnel** for secure connections.
    
    <Background>
      <p style="text-align: center">
        <img src="https://api.apidog.com/api/v1/projects/544525/resources/342823/image-preview" style="width: 640px" />
      </p>
    </Background>
  </Step>
  <Step>
    Click **Save**.
  </Step>
</Steps>

:::security
**Data Privacy**: Database credentials (address, port, username, password) are stored **locally** on your client and are **not synced** to the cloud. Each team member must configure their own database connections.
:::

## Multi-Environment Configuration

When working with different environments (e.g., Dev, Test, Prod), you can configure environment-specific database connections.

1.  In **Database Connections**, create separate connections for each environment.
2.  Enable **Environment Specific** settings if available or simply name them clearly.
3.  When executing requests, Apidog will use the connection corresponding to the currently selected environment.

<Background>
  <p style="text-align: center">
    <img src="https://api.apidog.com/api/v1/projects/544525/resources/342824/image-preview" style="width: 640px" />
  </p>
</Background>

## Database Access in Scripts

For advanced logic, you can connect to databases using custom JavaScript scripts.

```javascript
var dbConfig = {
    type: 'mysql',
    host: '127.0.0.1',
    port: '3306',
    username: 'root',
    password: 'password',
    database: 'test'
};

pm.dataSource(dbConfig).query('SELECT * FROM pets', (err, results) => {
    if (err) {
        console.log(err);
    } else {
        console.log(results);
        pm.environment.set('pet_name', results[0].name);
    }
});
```


## CLI Support

Apidog CLI supports running test scenarios with database operations. However, since database configs are local, you must export the database configuration file and place it on the machine running the CLI.

See **[Apidog CLI](https://docs.apidog.com/introduction-to-apidog-cli-605134m0.md)** for instructions.

