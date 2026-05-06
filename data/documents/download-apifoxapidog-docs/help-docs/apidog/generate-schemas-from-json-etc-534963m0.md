# Generate Schemas from JSON Etc

When creating a schema, Apidog offers a very useful tool that allows you to quickly identify and create a schema from existing data. By clicking on **Generate from JSON etc.**, you enter the data structure import tool.

<Background>
<img src="https://api.apidog.com/api/v1/projects/544525/resources/341044/image-preview" style="width: 640px" />
</Background>

Here, you can paste in your `JSON`, `XML`, `JSON Schema` and **Import from Database**, and Apidog will automatically generate a schema based on that data.

## Generating from JSON/XML

<Background>
<img src="https://api.apidog.com/api/v1/projects/544525/resources/341045/image-preview" style="width: 640px" />
</Background>

For JSON/XML, all you need to do is paste the existing JSON or XML into the designated area, and it will be automatically recognized and converted into the corresponding schema and data types.

:::info[Important Notes]
- JSON smart recognition serves to generate data structures based on the provided JSON, without saving the values contained within the JSON itself.
- All properties appearing in JSON/XML will be treated as `required`.
- Fields like description and mock will be left blank.
:::

### Overwrite Mode

When a schema is **Generated from JSON** for the second time, the newly imported data will overwrite the existing schema that has already been generated. In this scenario, there are two **Overwrite modes**:

- **Merge (Default)**: When a matching key is found, the mock and description from the original schema will be retained.
- **Overwrite**: All existing data will be discarded, and the new data will completely replace the old data.

### Naming Style

You can choose proper naming style:

- **Keep it as is**
- **camelCase**
- **PascalCase**
- **snake_case**

### Save as Example

When using **Generate from JSON** in the Request body or Response, enabling **Save as Example** will include the current JSON/XML as a Request/Response Example when generating the schema.

## Generating from JSON Schema

Simply pasting a JSON Schema allows for visual recognition of the data structure.

## Importing from Database

Apidog supports two methods of generating schemas from database tables. The first method involves directly connecting to the database to read the table structures, while the second method entails pasting SQL DDL to recognize the table structure.

### Database Connections

<Background>
<img src="https://api.apidog.com/api/v1/projects/544525/resources/341051/image-preview" style="width: 640px" />
</Background>

To import schema from databases, follow these steps:

<Steps>
  <Step>
    Set up the database connection. Learn more about [Manage Database Connection](https://docs.apidog.com/database-operations-in-apidog-588469m0.md).
      
:::info[Supported Databases]
Apidog Free supports `MySQL`, `SQL Server`, `Oracle`, and `PostgreSQL` databases, while the paid version also includes support for `ClickHouse`, `MongoDB`, and `Redis`.
:::
  </Step>
  <Step>
    Select the database connection in **Import from database**.
  </Step>
  <Step>
    Select the tables to import.
  </Step>
  <Step>
    Configure the import options. For specific configuration settings, refer to the previous sections on JSON/XML handling.
  </Step>
</Steps>

:::tip[Field Length Settings]
When the **Follow database field length** toggle is enabled, Apidog will set the minimum and maximum property length values based on the field lengths defined in the table.
:::

### Enter SQL (DDL)

<Background>
<img src="https://api.apidog.com/api/v1/projects/544525/resources/341052/image-preview" style="width: 640px" />
</Background>

Paste the database table `CREATE` statement (DDL) to generate the schema. Support SQL that Compatible with MySQL.

For specific configuration settings, refer to the previous sections on JSON/XML handling.

