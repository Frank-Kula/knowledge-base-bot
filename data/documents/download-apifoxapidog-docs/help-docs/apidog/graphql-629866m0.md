# GraphQL

GraphQL is a query language for APIs and a server-side runtime for executing queries using a type system you define for your data. Unlike traditional REST APIs, GraphQL provides a flexible approach to data retrieval, allowing clients to request exactly the data they need. GraphQL is database-agnostic and integrates seamlessly with your existing code and data infrastructure.

## Creating a GraphQL Request

To create a new GraphQL request in Apidog:

1. Navigate to the request builder
2. Select **"Body"** → **"GraphQL"**

<Background>
![](https://assets.apidog.com/uploads/help/2024/05/31/36967607d601fbf4e50882ac32bbd276.png)
</Background>

## Executing GraphQL Queries

### Writing Queries

Enter your GraphQL query in the **Query** box on the "Run" tab. Apidog provides code completion to assist with query construction.

:::tip[Enable Code Completion]
Click the **"Fetch Schema"** button in the input box to enable code completion for GraphQL query expressions. This feature helps you write accurate query statements by suggesting available fields and types.
:::

<Background>
![](https://assets.apidog.com/uploads/help/2024/05/31/544fb2e4aa8ba78fa243f8933d9b6aa3.png)
</Background>

### Using Variables

GraphQL queries support variables for dynamic data injection. This enables you to reuse queries with different input values without modifying the query structure.

For detailed syntax and usage, refer to the official [GraphQL variables documentation](https://graphql.org/learn/queries/#using-variables-inside-fragments).

<Background>
![](https://assets.apidog.com/uploads/help/2024/05/31/23db61c1960df793ee8687bee901caa3.png)
</Background>

## Key Features

| Feature | Description |
|---------|-------------|
| **Schema Fetching** | Automatically retrieve API schema for code completion |
| **Variable Support** | Use dynamic variables in queries for flexible data requests |
| **Code Completion** | IntelliSense-style suggestions for fields and types |
| **Type Validation** | Real-time validation against the GraphQL schema |

