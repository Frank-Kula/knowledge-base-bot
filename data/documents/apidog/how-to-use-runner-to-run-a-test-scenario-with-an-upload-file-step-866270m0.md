# How to use Runner to run a test scenario with an upload file step?

In Apidog, the file parameters within an endpoint request actually only save the **file path** (not the file itself). When sending a request, Apidog will look for the actual file based on the file path and then send it. Therefore, you need to ensure that:


<Steps>
  <Step title="Put your file in host machine">
    Copy the files to the host directory that is mounted to the Runner's volume. The Runner's volume is specified by yourself using `-v` when [deploying the Runner](https://docs.apidog.com/general-runner-755233m0.md).
  </Step>
  <Step title="Open the test step that requires using files in Apidog">
    In the Apidog test scenario, locate the step details for the file upload request and click the "Batch Edit" button in top-right corner.
      <Background>

    ![image.png](https://api.apidog.com/api/v1/projects/544525/resources/352026/image-preview)

    </Background>
  </Step>
  <Step title="Change the file path in the request parameters">
    Replace the file field parameter value with the file path in the Runner's directory (e.g., `/opt/runner/yourfilename.jpg`).
      <Background>


    ![image.png](https://api.apidog.com/api/v1/projects/544525/resources/352027/image-preview)
    </Background>
  </Step>
</Steps>


