# How to migrate environments from other tools to Apidog?

In Apidog, the Initial value of variables is synchronized within the team, while the Current value is only stored locally. This means that when you use Apidog on another computer, you won't have access to the previously used Current values.

Therefore, Apidog provides the functionality to migrate environments. You can export the services and variables in environments as a JSON file and then import it on another computer. Here are the steps:
<Steps>
  <Step>
    In the environment management, hover over the `...` next to the Environments list, click Export to obtain a JSON file.
<p style="text-align: center">
    <img src="https://api.apidog.com/api/v1/projects/544525/resources/342803/image-preview" style="width: 540px" />
</p>
  </Step>
  <Step>
On another computer, open environment management, hover over the `...` next to the Environments list, and click Import. Select the JSON file to import.
  </Step>
  <Step>
You can also import environments exported from Postman.
    </Step>
</Steps>

