# Shared Test Data

In automated test, many test scenarios may need to use the same test data, such as user login information, product data, or configuration parameters. Apidog supports creating **Shared Test Data** that can be used across multiple scenarios. This reduces repetitive work, ensures data consistency, and makes test resource management more efficient.

### Main Advantages of Shared Test Data:

1. **Cross-Scenario Sharing**: Maintain one set of test data at the project level for multiple scenarios to reference.
  
2. **Unified Management**: Centralized test data storage; modifying in one place updates all scenarios that referenced the data.
  
3. **Consistency Guarantee**: Ensures different scenarios use the same base data to avoid deviations in results.
  
4. **Standardized Workflow**: Establishes test data standards to improve team collaboration and maintainability of the testing workflow.

---

## Creating Shared Test Data

### Method 1: Static Test Data

<Steps>
  <Step>
In your project, click `Tests` in the left menu, then select the `Test Data` tab.

<Background>
![image.png](https://api.apidog.com/api/v1/projects/544525/resources/372729/image-preview)
</Background>

  </Step>
  <Step>
Click the `Create Test Data (Static)` button and enter a name.

<Background>
![image.png](https://api.apidog.com/api/v1/projects/544525/resources/372731/image-preview)
</Background>

  </Step>
  <Step>
Import or manually edit the data. It supports **CSV** and **JSON** imports, manual table editing, or bulk generation.

<Background>
![bulk-test-data-generation.gif](https://api.apidog.com/api/v1/projects/544525/resources/372734/image-preview)
</Background>

  </Step>
  <Step>
Click `Save` to create a shared test data.
     
  </Step>
</Steps>
  

### Method 2: Database Connection

This allows you to pull data dynamically from a database, ideal for staying consistent with real-world data.
  
<Steps>
  <Step>
In the `Test Data` tab, click `Create Test Data (Database)`.
      
<Background>
![image.png](https://api.apidog.com/api/v1/projects/544525/resources/372737/image-preview)
</Background>
  </Step>

  <Step>
If currently no database connection is configured, click `Set Data Source Config` to add or select a database.
  </Step>

  <Step>

Write a SQL query to get the test data. You can also use variables in the SQL. For example:

```sql
SELECT id, name, email FROM pets;
````

<Background>

![creating-shared-data-using-database-connection.gif](https://api.apidog.com/api/v1/projects/544525/resources/372743/image-preview)
</Background>

  </Step>

  <Step>
Click `Save` to create a shared test data.
  
:::tip[]
Once data is pulled, it remains static until you manually refresh it.

<Background>
![img_v3_02v9_77e7ef9f-11e8-4d44-9816-cede3a69d97g.jpg](https://api.apidog.com/api/v1/projects/544525/resources/372748/image-preview)
</Background>
:::      

  </Step>
</Steps>

---

## Using Shared Test Data in Scenarios
Once you create shared test data, you can reference it in any test scenarios.
  
<Steps>
  <Step>
Go to a `Test Scenario`, and in the run configuration panel, click the `Test Data` dropdown to select your shared data.
      
<Background>
![image.png](https://api.apidog.com/api/v1/projects/544525/resources/372749/image-preview)
</Background>

  </Step>
  <Step>
Once referenced, you can use the data in test steps using the `{{variable_name}}` syntax.

<Background>
![image.png](https://api.apidog.com/api/v1/projects/544525/resources/372750/image-preview)
</Background>

  </Step>
</Steps>

---

## Managing Shared Test Data

### Editing Shared Test Data

In the "Shared Test Data" list, click a data name to open the edit screen. You can:

- Change the data name
- Add, delete, or edit data rows
- Add or remove data columns (variables)
- Import new data to overwrite existing data
- Export the current data as CSV or JSON

:::tip[]
After you update shared test data, all scenario cases that reference that data automatically use the latest values — no manual sync needed.
:::


**Editing limits for database-type shared test data:**

- Data content is **read-only**; you cannot edit individual values directly
- Manual refresh is supported: data is fetched again from the linked database and overwrites the current set
- You can change the test data name
- You can change the database connection settings or the SQL query


### Configuring Data by Environment

Shared test data can be configured per environment. You can maintain a separate dataset for development, testing, and other environments; when you switch environments, the data for that environment is used automatically.

<Background>
![image.png](https://api.apidog.com/api/v1/projects/544525/resources/372752/image-preview)
</Background>


## Using Shared Test Data in Scripts

You can access shared test data in pre or post processor scripts:

```js
// Check if a shared test data variable exists
pm.iterationData.has("variable_name")

// Get the value of a shared test data variable
pm.iterationData.get("variable_name")

// Convert all shared test data variables to an object
pm.iterationData.toObject()
```

The variable name must match the column name in the shared test data.

## Shared Test Data vs Scenario Test Data

| Comparison | Shared Test Data | Scenario Test Data |
|------------|-----------------|---------------------|
| Data scope | Project-level; can be used by multiple test scenarios | Only the current test scenario |
| Data sync | Changes automatically apply to all scenarios that reference it | Affects only the current scenario |
| Use case | Common base data, e.g. user info, product data | Data specific to one scenario |
| Maintenance | Low; managed in one place | Higher; maintained per scenario |


## Best Practices

**1. Use the right data granularity**

Use shared test data for highly reusable base data; keep scenario-specific data inside the scenario.

**2. Use clear naming**

Give shared test data descriptive names (e.g. "User login data", "Product list data") so the team can understand and choose them easily.

**3. Clean up unused data regularly**

Periodically check which shared test data is still referenced and remove data that is no longer used to keep the list tidy.

**4. Use with environment variables**

Keep environment-related settings (e.g. URLs, keys) in environment variables and business data in shared test data for clear separation of concerns.


## FAQs

<Accordion title="What's the difference between shared test data and environment variables?" defaultOpen>
Environment variables are best for configuration (e.g. API base URL, keys), usually one value per variable. Shared test data is best for business data and supports multiple rows for data-driven tests. You can use both together.
</Accordion>

<Accordion title="Does changing shared test data affect tests that are already running?">
No. A running test uses a snapshot of the data from when the run started. Your changes only affect new test runs you start after that.
</Accordion>

<Accordion title="How many records can shared test data hold?">
Shared test data supports a large number of records; the exact limit depends on your team plan. Keeping each dataset to a reasonable size (e.g. under 1000 rows) is recommended for best performance.
</Accordion>


