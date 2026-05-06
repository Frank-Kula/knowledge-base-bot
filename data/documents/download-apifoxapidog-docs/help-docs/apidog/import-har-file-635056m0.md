# Import .har File

`.har` (HTTP Archive) is a JSON-formatted file used for logging a web browser's interaction with a site. It records web requests, responses, headers, and other data sent between the browser and server.
Apidog supports capturing these records to quickly generate API endpoints.

## Phase 1: Export .har File

You can use standard browser tools (Chrome, Edge, Firefox) to export traffic as a HAR file.

### Chrome / Edge
1.  Open Developer Tools: `F12` or `Ctrl+Shift+I` (Windows/Linux) / `Cmd+Opt+I` (Mac).
2.  Navigate to the **Network** tab.
3.  Refresh the page or perform actions to capture traffic.
4.  Right-click any request row (or the empty space) and select **Save all as HAR with content**.

<details>
<summary>📷 Visual Reference: Chrome DevTools</summary>
<Background>
![](https://api.apidog.com/api/v1/projects/544525/resources/369010/image-preview)
</Background>
<Background>
![](https://assets.apidog.com/uploads/help/2023/07/11/4f9200be66163413841e5ed0de6abc6d.png)
</Background>
</details>

## Phase 2: Import into Apidog

<Steps>
  <Step>
    **Upload File**

    Go to **Settings** > **Import Data** > **Manual**. Select **HAR** and upload your `.har` file.

    <details>
    <summary>📷 Visual Reference</summary>
    <Background>
    ![](https://assets.apidog.com/uploads/help/2023/07/11/7a7a6bf1a141b0ac6ada58e620753a22.png)
    </Background>
    </details>
  </Step>

  <Step>
    **Configure Import Options**
    
    Adjust the settings to match your needs:

    *   **BaseURL Handling**:
        *   **Hardcode**: Include the BaseURL in the specific endpoint path.
        *   **Remove**: Intelligent parsing removes the BaseURL so you can manage it globally via Environments (Recommended).
    
    *   **Static Resource**: Toggle **Exclude** to ignore captured images, CSS, and JS files.
      
    *   **Endpoint Case Generation**: Turn **ON** to automatically generate a default test case for each imported endpoint.
  </Step>
</Steps>

