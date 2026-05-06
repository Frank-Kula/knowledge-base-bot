# Using Variables

In Apidog, **variables** allow you to save and reuse values easily. Storing a value as a variable enables you to access it across various environments, requests, scripts, and test scenarios. Utilizing variables increases productivity and promotes teamwork among colleagues.

## What are Variables?

A variable is a symbolic representation of data that allows you to retrieve a value without manually inputting it every time it's needed. This is beneficial for reusing the same values across different locations.

**Example:**
If you have the same token in multiple requests and anticipate changes, save the token as a variable named `{{my_token}}`. Use `{{my_token}}` in the request parameter value. When the token changes, updating the variable value updates it everywhere.

<Background>
![Variable example](https://api.apidog.com/api/v1/projects/544525/resources/342746/image-preview)
</Background>

Variables can take effect in parameter values, bodies, URLs, or headers.

:::tip[]
In Apidog's **Tests** module, variables can be used to [pass data between requests](https://docs.apidog.com/pass-data-between-requests-601617m0.md).
:::

## Variable Scopes

Apidog supports variables in various scopes to adjust to different development, testing, and collaboration requirements.

Priority (from lowest to highest): **Global < Module < Environment < Data < Local**

When a variable with the same name is defined in different scopes, the value from the **narrowest scope** takes precedence.

1.  **Global Variables**
    *   **Shared within Project**: Accessible across an entire project. Useful for sharing data between endpoints (e.g., login token).
    *   **Shared within Team**: Shared throughout the entire team across different projects (e.g., a token shared between a login project and a finance project).

<Background>
![Global project variables](https://api.apidog.com/api/v1/projects/544525/resources/371865/image-preview)


![Global team variables](https://api.apidog.com/api/v1/projects/544525/resources/371863/image-preview)
</Background>

:::note
*   **Permissions**: To manage team variables, you need team admin permissions. Go to **Team Resources > Variables**.
*   **Scripts**: You can use `pm.globals.set` to update local values in scripts, but cannot change names or shared values.
:::

2.  **Module Variables**
    *   Defined within a module. Importing from Postman "Collection variables" maps to Module variables.

3.  **Environment Variables**
    *   Tied to specific environments (Development, Testing, Production). Only the active environment's variables are effective.

4.  **Data Variables**
    *   Sourced from external CSV or JSON files in **Test Scenarios** or **CLI**. Values do not persist after the run.

5.  **Local Variables**
    *   Temporary variables confined to a single request or test scenario run. Disappear once completed.

:::tip
Variables in Apidog are stored as **strings**. When saving objects or arrays, use `JSON.stringify()` to store and `JSON.parse()` to retrieve them.
:::

## Shared and Local Values

Each variable has two states:

*   **Shared Value**: Sychronized with Apidog servers and shared with the team.
*   **Local Value**: Stored LOCALLY in your browser or client cache. **Not shared.**

<Background>
![Initial vs Current value](https://api.apidog.com/api/v1/projects/544525/resources/371869/image-preview)
</Background>

**Best Practices:**
*   Use **Local Value** for sensitive data (tokens, passwords) so they stay on your machine.
*   Leave Local Value empty to fall back to the Shared Value.
*   Click the link icon `🔗` to sync Local Value with Shared Value.

:::warning
*   Cleaning Apidog cache will delete Local Values.
*   Local Values do NOT migrate automatically when switching devices (use Environment Export/Import).
:::

### Using Variables in Apidog CLI

When running in the **CLI**, the **Shared Value** is used by default, whereas the Client uses the Local Value. This is a common cause for discrepancies between Client and CLI runs.

:::tip
Learn more about the [Apidog CLI](https://docs.apidog.com/introduction-to-apidog-cli-605134m0.md).
:::

## Defining Variables

### 1. Environment Management (Preset)
Values for Global and Environment variables can be preset manually.

<Steps>
  <Step>
    Click the **Environment Management** icon `≡`.
  </Step>
  <Step>
    Select **Global Variables** or a specific environment.
  </Step>
  <Step>
    Add the variable name, shared value, and local value.
  </Step>
  <Step>
    Click **Save**.
  </Step>
</Steps>

### 2. Extract Variables
Visually extract values from API responses into variables without writing code.

<Steps>
  <Step>
    In the **Run** tab (Design Mode), go to **Post Processors**.
  </Step>
  <Step>
    Select **Extract Variable**.
    <Background>
    ![Add extraction](https://api.apidog.com/api/v1/projects/544525/resources/342755/image-preview)
    </Background>
  </Step>
  <Step>
    Configure extraction source (JSON, XML, Header, etc.) and JSONPath.
    <Background>
    ![Configure extraction](https://api.apidog.com/api/v1/projects/544525/resources/342756/image-preview)
    </Background>
  </Step>
  <Step>
    Send the request to execute and verify in the **Console**.
    <Background>
    ![Console verification](https://api.apidog.com/api/v1/projects/544525/resources/342758/image-preview)
    </Background>
  </Step>
</Steps>

:::tip
Learn more about [Extract Variable](https://docs.apidog.com/extract-variable-588468m0.md).
:::

### 3. Scripts

Use the `pm` object in Pre/Post-processors.

**Syntax for `set`:**

```javascript
// Environment Variable
pm.environment.set('key', 'value');

// Global Variable (Project)
pm.globals.set('key', 'value');

// Local Variable
pm.variables.set('key', 'value');

// Module Variable
pm.moduleVariables.set('key', 'value');
```

**Storing Objects/Arrays:**

```javascript
var obj = { id: 1, name: "test" };
pm.environment.set('user', JSON.stringify(obj));
```

:::tip
Learn more about [Script Syntax](https://docs.apidog.com/postman-scripts-reference-593586m0.md).
:::

### 4. Database Operations
Connect to a database to retrieve data and set it as a variable.

<Steps>
  <Step>
    Add **Database Operation** in Post Processors.
    <Background>
    ![Add DB op](https://api.apidog.com/api/v1/projects/544525/resources/342780/image-preview)
    </Background>
  </Step>
  <Step>
    Configure database connection.
    <Background>
    ![Configure DB](https://api.apidog.com/api/v1/projects/544525/resources/342782/image-preview)
    </Background>
  </Step>
  <Step>
    Enter SQL command (supports `{{variable}}`).
  </Step>
  <Step>
    Set **Extract Result To Variable**.
  </Step>
</Steps>

:::tip
Learn more about [Database Operations](https://docs.apidog.com/database-operations-in-apidog-588469m0.md).
:::

## Using Variables

### Request Parameters
Use double curly braces `{{variable}}` in URL, parameters, headers, or body.

**Example URL:**
`http://127.0.0.1/pet/findByStatus?status={{CurrentStatus}}`

**Example JSON Body:**
```json
{
    "status": "{{CurrentStatus}}",
    "quantity": {{TotalPet}}
}
```

:::warning
*   **Strings**: Add double quotes `""` around the variable for strings (e.g., `"{{name}}"`).
*   **Numbers/Booleans**: Do NOT add quotes (e.g., `{{count}}`).
:::

### Accessing Sub-elements
If a variable contains a JSON object/array, access properties via dot notation using [JSONPath](https://docs.apidog.com/jsonpath-645606m0.md).

**Object in `{{user}}`:**
```json
{ "id": 1, "name": "Jack" }
```
*   Request: `{{user.name}}`
*   Script: `pm.variables.get("user.name")`

**Array in `{{users}}`:**
```json
[ { "name": "Jack" } ]
```
*   Request: `{{users[0].name}}`
*   Script: `pm.variables.get("users[0].name")`

### Using Variables in Scripts
In scripts, use `pm.*.get()` instead of `{{}}`.

```javascript
// Get environment variable
var val = pm.environment.get("variable");

// Get global variable
var val = pm.globals.get("variable");

// Get local variable
var val = pm.variables.get("variable");
```

**Logging:**
```javascript
console.log(pm.variables.get("my_var"));
```
Check the **Console** tab to see output.

### Using Data Variables
In **Test Scenarios**, importing a CSV/JSON file creates "Data Variables". Use `{{column_name}}` to reference them. Each row in the file triggers a separate iteration.

:::tip
Learn more about [Data Driven Testing](https://docs.apidog.com/data-driven-testing-602987m0.md).
:::

## FAQ

**Q: Can I use variables in Mocks?**
*   **No.** Variables are resolved when a *request is sent*. Mocks are static definitions or run on the mock server without a client-side "sending" context in the same way.

**Q: How do I get the base URL in a script?**
*   Use `pm.request.getBaseUrl()`.
*   Avoid `pm.environment.get('BASE_URL')` as it might be inaccurate for non-default server endpoints.

