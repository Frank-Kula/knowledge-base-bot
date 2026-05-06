# Public Scripts

Public Scripts allow you to write reusable code snippets that can be shared across multiple requests, preventing code duplication and making maintenance easier.

## Managing Public Scripts

To create and manage scripts, go to **Settings** > **Public Scripts**.

<Background>
  ![Manage Public Scripts](https://api.apidog.com/api/v1/projects/544525/resources/356626/image-preview)
</Background>

## Using Public Scripts

### 1. Adding to a Request
In the **Pre Processors** or **Post Processors** tab of any request, you can insert a Public Script.

<Background>
  ![Reference Public Script](https://api.apidog.com/api/v1/projects/544525/resources/356627/image-preview)
</Background>

:::tip[Execution Order]
*   Public scripts executes *before* custom scripts in the same processor list.
*   If multiple public scripts are added, they execute in the order they are listed.
:::

### 2. Calling Functions from Public Scripts
To use a function from a Public Script inside a Custom Script, the function must be declared as **global**.

**Bad Practice (Local Scope):**
```javascript
// This function is invisible to other scripts
function my_fun(name) {
    return "Hello " + name;
}
```

**Good Practice (Global Scope):**
```javascript
// Attach to global scope
my_fun = function(name) {
    return "Hello " + name;
};
```

**Implementation Workflow:**

<Steps>
  <Step>
    **Define Global Function**
    
    In your Public Script, define the function without `var`, `let`, or `const`, or explicitly attach it to `window`/`global` if needed (though direct assignment usually works in PM sandbox).
    
    ```javascript
    my_fun = function (name) {
      return "Hello, " + name + "!";
    };
    ```
    <Background>
      ![Define Global Function](https://api.apidog.com/api/v1/projects/544525/resources/356628/image-preview)
    </Background>
  </Step>
  <Step>
    **Call in Custom Script**
    
    Add the Public Script to your request **first**, then add a Custom Script **below it**. Call the function in the Custom Script.
    
    ```javascript
    // Call the global function
    const result = my_fun("Apidog");

    // Assert result
    pm.test("Greeting is correct", function () {
      pm.expect(result).to.eql("Hello, Apidog!");
    });
    ```
    <Background>
      ![Call Global Function](https://api.apidog.com/api/v1/projects/544525/resources/356629/image-preview)
    </Background>
  </Step>
</Steps>

