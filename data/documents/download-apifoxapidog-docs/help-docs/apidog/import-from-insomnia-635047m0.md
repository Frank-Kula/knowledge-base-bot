# Import from Insomnia

Insomnia is an open-source API design and testing tool. Apidog supports importing data exported from Insomnia.

## Phase 1: Export Data from Insomnia

1.  Open Insomnia.
2.  Locate the export option based on your login status:
    *   **Not Logged In**: Click **Scratch Pad** > **Export**.
    *   **Logged In**: Click the **Collection Name** > **Export**.

3.  Select the data to export.
4.  Choose either **Insomnia** (latest version) or **HAR** (`.har`) format and save the file.


## Phase 2: Import into Apidog

<Steps>
  <Step>
    **Upload File**

    Go to **Settings** > **Import Data**. Based on your exported file, select either **Insomnia** or **HAR** and upload the file.
    
  </Step>

  <Step>
    **Configure Import Options**
    
    Adjust the following settings to match your needs:

    *   **BaseURL Handling**:
        *   **Hardcode**: Include the BaseURL in the specific endpoint path.
        *   **Remove**: Intelligent parsing removes the BaseURL so you can manage it globally via Environments (Recommended).
    
    *   **Static Resource**: Toggle to ignore or keep static resources.
      
    *   **Endpoint Case Generation**: Turn **ON** to automatically generate a default test case for each imported endpoint.

  </Step>
</Steps>
