# How to mock fixed API data in Apidog?

If you want an endpoint to return specific data, you can use mock expectations.

<Tabs>
  <Tab title="Design-first Mode">
In Design-first Mode, you can set expectations in the `Mock` tab of the endpoint.

      <Background>
![image.png](https://api.apidog.com/api/v1/projects/544525/resources/352097/image-preview)
</Background>
  </Tab>
  <Tab title="Request-first Mode">
In Request-first Mode, you can set expectations in the `Mock` tab.
<Background>
![image.png](https://api.apidog.com/api/v1/projects/544525/resources/352098/image-preview)
</Background>
    </Tab>

</Tabs>


You can add an unconditional expectation to return fixed data.


<Steps>
  <Step>
    Click "New expectation".
  </Step>
  <Step>
    Add an expectation name, leave the conditions blank.
      <p style="text-align: center">
    <img src="https://api.apidog.com/api/v1/projects/544525/resources/343601/image-preview" style="width: 640px" />
</p>
  </Step>
  <Step>
    Fill in the response you want to return in the Response data and save.
  </Step>
  <Step>
    Copy the mock URL to access this endpoint.
  </Step>
</Steps>
