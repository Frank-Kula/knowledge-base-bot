# Import cURL

## Utilizing Traffic Capture Tools

You can capture HTTP traffic using standard tools and import it into Apidog via `cURL`. This workflow consists of two phases: **Capturing** the request and **Importing** it.

## Phase 1: Capture Traffic (Copy as cURL)

Use your preferred proxy or browser tool to capture the request.

### Chrome DevTools
1.  Open Developer Tools: `F12` or `Ctrl+Shift+I` (Windows/Linux) / `Cmd+Opt+I` (Mac).
2.  Go to the **Network** tab and trigger the request.
3.  Right-click the request > **Copy** > **Copy as cURL**.


### Charles Proxy
1.  Locate the request in the session list.
2.  Right-click the request > **Copy cURL Request**.


### Fiddler
1.  Select **File** > **Export Sessions** > **Selected Sessions**.
2.  Choose **cURL Script** format.
3.  Save and open the `.bat` file to copy the script content.

## Phase 2: Import into Apidog

Once you have the `cURL` command on your clipboard:

<Steps>
  <Step>
    **Open Import Dialog**
    
    Click the `+` button next to the search bar and select **Import cURL** (Shortcut: `Ctrl/Cmd + I`).

  </Step>

  <Step>
    **Paste Command**
    
    Paste the cURL command into the text box.

  </Step>

  <Step>
    **Debug / verify**
    
    The request will open in the "Quick Debugging" tab. You can test it immediately.

  </Step>

  <Step>
    **Save as API**
    
    Click **Save** to permanently add the endpoint to your project for documentation and testing.

  </Step>
</Steps>
