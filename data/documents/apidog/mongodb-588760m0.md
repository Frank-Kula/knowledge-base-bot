# MongoDB

:::info
Connecting to MongoDB is a paid feature. Please check [Pricing](https://apidog.com/pricing/) for details.
:::

MongoDB is a popular NoSQL database that stores data in JSON-like documents. Apidog allows you to connect to MongoDB and perform operations using standard query syntax.

## Connecting to MongoDB

<Steps>
  <Step>
    **Create Connection**
    
    Go to **Settings** > **Database Connections** > **New**. Select **MongoDB**.
  </Step>
  <Step>
    **Configure Details**
    
    Enter the connection string or individual components (Host, Port, Database, etc.).
    
    <Background>
      ![MongoDB Connection Settings](https://assets.apidog.com/uploads/help/2023/12/01/e86e418e35b9811b43e43d4a386e37bb.png)
    </Background>
  </Step>
</Steps>

## Performing Operations

In the **Database Operation** processor, select **MongoDB**. You can perform standard CRUD operations or run advanced commands.

### Common CRUD Operations
Select an **Operation Type** (e.g., `Find`, `Insert`, `Update`, `Delete`) and specify the **Collection Name**.

**Query Example:**
In the **Query Condition** field, enter a JSON object:

```json
{
    "_id": "65486728456e79993a150f1c"
}
```

Apidog automatically handles `ObjectId` conversion for matching ID strings.

<Background>
  ![MongoDB Query Example](https://assets.apidog.com/uploads/help/2023/12/01/0aa793e9610aa0bfc0ba1e98b81be936.png)
</Background>

### Using BSON Types
You can use standard MongoDB BSON types in your queries:

```javascript
{
  "createdAt": ISODate("2023-11-15T00:00:00.000Z"),
  "price": NumberDecimal("19.99"),
  "active": true
}
```

**Supported Types:**

| Type | Syntax | Description |
| :--- | :--- | :--- |
| **Date** | `ISODate("...")` | Date/Time object |
| **ObjectId** | `ObjectId("...")` | Unique Document ID |
| **Decimal** | `NumberDecimal("...")` | High-precision decimal |
| **Long** | `NumberLong("...")` | 64-bit integer |

### Running Database Commands
For administrative tasks or complex aggregations, select **Run Database Command** as the Operation Type.

**Example: Count Documents**
```json
{
    "count": "users",
    "query": { "active": true }
}
```

<Background>
  ![Run Database Command](https://assets.apidog.com/uploads/help/2023/12/01/7d56893affe5eeea3a807b891745327e.png)
</Background>

