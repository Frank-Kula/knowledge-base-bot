# How Can Document Users Modify the Base URL in Shared Docs?

In the published docs or quickly shared docs of Apidog, if you want the document users to be able to set and modify the Base URL, it can be easily achieved by setting variables. The specific operation steps are as follows:

<Steps>
  <Step title="Create and reference variables">
   In the Apidog project, go to a certain "Environment" page, click "Add Variable", and enter the variable name (for example, "BaseURL"). In the URL input box corresponding to the "Base URL" of the environment, use the variable reference (for example, `{{BaseURL}}`) to replace the specific URL address. This associates the Base URL with the created variable.
    <Background>

![image.png](https://api.apidog.com/api/v1/projects/544525/resources/365128/image-preview)
    </Background>

  </Step>
  <Step title="Select Environment">
    Choose the corresponding environment when publishing the documentation.
      
<Background>

![CleanShot 2025-10-31 at 14.02.11@2x.png](https://api.apidog.com/api/v1/projects/544525/resources/365129/image-preview)
</Background>

  </Step>
  <Step title="Access the document">
    
After the document is published and shared with users, the users can see the place where the variable is referenced on the endpoint. When the mouse hovers over the variable reference, it will prompt the user to set the variable value.
    <Background>
    
![CleanShot 2025-10-31 at 14.06.39@2x.png](https://api.apidog.com/api/v1/projects/544525/resources/365131/image-preview)
    </Background>
  </Step>
      <Step title="Modify the variable value">
 
          Click on the variable, and the variable setting window will pop up automatically. The user just needs to fill in the required actual value.
    <Background>
    
![image.png](https://api.apidog.com/api/v1/projects/544525/resources/365132/image-preview)
    </Background>
    After saving, the paths displayed on the document and the actual requests will automatically apply the updated variable value.

  </Step>
</Steps>



This method allows users to customize the Base URL to access their specific data.
