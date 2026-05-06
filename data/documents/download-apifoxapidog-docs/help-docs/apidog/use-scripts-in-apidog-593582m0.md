# Use Scripts in Apidog

Apidog includes a powerful JavaScript-based scripting engine that allows you to add dynamic behavior to your API requests and tests. This engine is fully compatible with Postman scripts.

## Capabilities

With custom scripts, you can:
1.  **Validate Responses**: Write assertions to verify status codes, headers, and body content (Post-processor).
2.  **Modify Requests**: Dynamically set URL parameters, headers, or body data (Pre-processor).
3.  **Manage Variables**: Pass data between requests by setting and retrieving variables.
4.  **External Integration**: Call programs written in other languages (Java, Python, PHP, Go, etc.).

:::highlight purple
**New to Scripting?** Use the **[Apidog Script Generator](https://app.anakin.ai/apps/21857)** to generate scripts from natural language descriptions.
:::

## Usage

Scripts can be executed at two stages of the request lifecycle:

*   **Pre Processors**: Executed *before* the request is sent.
*   **Post Processors**: Executed *after* the response is received.

<Background>
  ![Script Execution Flow](https://assets.apidog.com/uploads/help/2023/07/12/ce9ebf6278b2bf4a3a3c67b1d969af89.png)
</Background>

## Debugging

You can print messages to the **Console** using `pm.console.log()` or `console.log()` for debugging purposes.

```javascript
pm.console.log("This works");
```

## Examples

*   **[Assertion Scripts](https://docs.apidog.com/assertion-scripts-593739m0.md)**
*   **[Using Variables](https://docs.apidog.com/using-variables-597443m0.md)**
*   **[Modifying Requests](https://docs.apidog.com/modifying-requests-597445m0.md)**
*   **[Other Examples](https://docs.apidog.com/other-examples-597448m0.md)**


## FAQ

**Q: Does Apidog support `pm.nextRequest()`?**

A: No. Apidog uses **Test Scenarios** for workflow orchestration instead of the "Run Collection" feature found in Postman. In a Test Scenario, you can use **Condition** steps (If-Else) to control the flow of execution based on logic, removing the need for `pm.nextRequest()`.

