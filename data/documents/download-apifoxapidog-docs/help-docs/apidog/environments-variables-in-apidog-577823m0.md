# Environments & Variables in Apidog

In Apidog, a **variable** serves as a dynamic placeholder for values that can be utilized across multiple API requests and scripts. When executing a request or script, Apidog references the current value of the variable.

By grouping variables into **environments**, you can easily adapt your testing setup to different work scenarios (e.g., Development, Testing, Production).

## Getting Started with Variables

Here's a quick guide to creating and using variables in Apidog.

<Steps>
  <Step>
    **Open the PetStore Project**
    
    Open the default PetStore project, which is pre-installed in your Team space for every user.
  </Step>
  <Step>
    **Open Environment Management**
    
    Locate and click the environment icon `≡` at the top right in your interface.
  </Step>
  <Step>
    **Create a Variable**
    
    Find the **Global Variables** section. Create a new variable called `my_variable` with "123" as its initial value.
      
<Background>
![Create global variable](https://api.apidog.com/api/v1/projects/544525/resources/342742/image-preview)
</Background>
  </Step>
  <Step>
    **Save Changes**
    
    Click the **Save** button.
  </Step>
  <Step>
    **Use in an Endpoint**
    
    Open the "Find pet by ID" endpoint, and switch to the **Run** tab.
  </Step>
  <Step>
    **Insert Variable**
    
    Locate the path parameter "PetId", and add `{{my_variable}}` as the value.
  </Step>
  <Step>
    **View Value**
    
    Move your cursor over the variable name to view its current value and scope.
      
<Background>
![View variable value](https://api.apidog.com/api/v1/projects/544525/resources/342743/image-preview)
</Background>
  </Step>
  <Step>
    **Switch Environment**
    
    Click the Environments dropdown besides the `≡` icon, and switch to the **Local Mock** environment.
  </Step>
  <Step>
    **Send Request**
    
    Click **Send** to execute the request.
  </Step>
  <Step>
    **Verify Replacement**
    
    You will find the response displayed in the lower half of the interface. By switching to the **Actual Request** tab, you can view the request that was actually sent, with variables replaced by their respective actual values.
    
<Background>
<p style="text-align: center">
    <img src="https://api.apidog.com/api/v1/projects/544525/resources/342744/image-preview" style="width: 640px" />
</p>
</Background>

  </Step>
</Steps>

:::tip[]
For a deeper understanding of variables in Apidog, see [Using Variables](https://docs.apidog.com/using-variables-577908m0.md).
:::

## Create and Switch Environments

The term "environment" is commonly used in development teams to distinguish between "development," "testing," "production," and so on. Each environment encompasses one or a set of servers.

*   When the client is in a particular environment, all requests are sent to the servers in that environment.
*   Upon switching environments, requests are directed to a different set of servers.

Learn more about [Environment Management](https://docs.apidog.com/environment-management-584758m0.md).

