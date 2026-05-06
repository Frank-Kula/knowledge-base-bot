# Import WSDL

**WSDL** (Web Services Description Language) is an XML format for describing network services. Apidog supports importing `.wsdl` and `.xml` files to quickly debug WebServices.

## Import Workflow

<Steps>
  <Step>
    **Upload File**

    Go to **Settings** > **Import Data**. Select **WSDL** and upload your file.

  </Step>

  <Step>
    **Preview & Confirm**
    
    A preview of the API endpoints will appear.
    *   **Verify Base URL**: Check the "Environments" tab to ensure the service address is correct.
    *   Click **Confirm** to finish.
  </Step>

  <Step>
    **Debug API**
    
    The imported environment will be created automatically.
    *   Select the environment in the top-right corner.
    *   Send a request; the Base URL will be automatically applied.

  </Step>
</Steps>
