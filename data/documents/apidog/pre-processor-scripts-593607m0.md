# Pre Processor Scripts

Pre-processor scripts are code snippets executed before a request is sent to the server. They are ideal for dynamic setup tasks, such as generating timestamps, calculating signatures, or setting random data.

## Example: Adding a Timestamp

You can generate a timestamp and store it in an environment variable to use in your request headers.

1.  **Add Script**: In the **Pre Processors** tab, add a Custom Script.
    
    ```javascript
    // Get current timestamp
    var timestamp = new Date().getTime();
    // Set to environment variable
    pm.environment.set("timestamp", timestamp);
    ```

    <Background>
      ![Set Timestamp Script](https://assets.apidog.com/uploads/help/2023/07/12/515f43fd4664f2284337c4b1503b09e0.png)
    </Background>

2.  **Use Variable**: In the **Headers** tab, reference the variable using `{{timestamp}}`.
    
    <Background>
      ![Use Timestamp Variable](https://assets.apidog.com/uploads/help/2023/07/12/46879417c23c56a63d1ed1ede57c429c.png)
    </Background>

When the request sends, `{{timestamp}}` will be replaced with the calculated value.

:::tip
Pre-processors function similarly to post-request scripts but do not have access to the `pm.response` object since the response has not yet been received.
:::

