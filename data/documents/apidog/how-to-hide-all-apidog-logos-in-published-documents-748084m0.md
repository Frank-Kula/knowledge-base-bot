# How to hide all Apidog logos in published documents?

<Steps>
  <Step title="Hide 'Build with Apidog'">
     The "Build with Apidog" mark is currently shown by default in published docs. To hide this mark, an [Enterprise plan](https://apidog.com/pricing/) is required.

  After upgrading to the Enterprise plan, please contact us via email at `support@apidog.com` and provide your custom domain and Docs Site ID.  
  
      After confirmation, our support team will help disable it for you manually.
  </Step>
  <Step title="Hide 'Run in Apidog'">
    Go to 'Share Docs', open Publish Docs Main Site, click 'Customize' - 'Appearance', and turn off the Hide 'Run in Apidog' Button.
      
    <Background>  
![image.png](https://api.apidog.com/api/v1/projects/544525/resources/359141/image-preview)
    </Background>
  </Step>
  <Step title="Request samples to hide'User-Agent: Apidog/1.0.0 (https://apidog.com) '">
    Update to version greater than or equal to 2.6.30, automatically remove 'User-Agent:Apidog' by default.
  </Step>
  <Step title="Auto-select Agent hides 'Apidog' logo">
:::tip[]
Issue view:
    <Background>

![image.png](https://api.apidog.com/api/v1/projects/544525/resources/348298/image-preview)
    </Background>
:::
   Go to 'Share Docs', open Publish Docs Main Site, click 'Customize' - 'Appearance', and turn off the Show'Try it out 'Button.
    <Background>  
   
![image.png](https://api.apidog.com/api/v1/projects/544525/resources/359142/image-preview)
    </Background>
  </Step>
</Steps>

