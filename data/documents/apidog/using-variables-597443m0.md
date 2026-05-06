# Using Variables

You can use scripts to set, get, and unset variables at different scopes (Environment, Global, Local).

## Environment Variables

These variables persist in the currently selected environment.

```javascript
// Set variable
pm.environment.set("token", "123456");

// Get variable
var token = pm.environment.get("token");

// Unset variable
pm.environment.unset("token");
```

### Storing Objects/Arrays
Since variables only store strings, you must stringify objects or arrays before saving them.

```javascript
var user = { id: 1, name: "Apidog" };

// Save
pm.environment.set("user", JSON.stringify(user));

// Read
var savedUser = JSON.parse(pm.environment.get("user"));
```

## Global Variables

Global variables are accessible across the entire project (or team, depending on scope).

```javascript
// Set global variable
pm.globals.set("baseUrl", "https://api.example.com");

// Get global variable
var url = pm.globals.get("baseUrl");
```

## Local Variables

Temporary variables valid only for the current request execution.

```javascript
// Set temporary variable
pm.variables.set("tempId", "999");

// Get temporary variable
var id = pm.variables.get("tempId");
```

## Module Variables

Variables scoped to the current module (compatible with Postman Collection Variables).

```javascript
// Set module variable
pm.moduleVariables.set("moduleId", "m1");

// Get module variable
var modId = pm.moduleVariables.get("moduleId");
```

