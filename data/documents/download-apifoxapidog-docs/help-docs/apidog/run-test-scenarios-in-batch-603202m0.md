# Run Test Scenarios in Batch

Apidog supports the ability to run multiple configured test scenarios in a batch.

In the Tests module, click on a folder in the left-hand folder tree, and the right-side panel will display a list of all the test scenarios within that folder. In this list, you can see information about each test scenario, such as the environment and the most recent run result.

<Background>
<img src="https://api.apidog.com/api/v1/projects/544525/resources/343141/image-preview" style="width:640px" />
</Background>

You can select multiple test scenarios, then click the "Batch run" button in the top-right corner to execute these test scenarios in a batch.

By default, the test scenarios will run using the environments that were saved for each individual test scenario. However, you can also click the dropdown button next to the "Batch Run" button to specify a different environment to use for the batch run.

After the batch run is completed, you will see a batch run test report that lists the results for all the executed test scenarios.

<Background>
<img src="https://api.apidog.com/api/v1/projects/544525/resources/343138/image-preview" style="width:640px" />
</Background>

## FAQ
**Q: Can I run test scenarios in batches in CI/CD?**

A: Currently, Apidog does not support running test scenarios in batches in CI/CD using a single command. However, you can achieve this by adding the CI/CD commands for each test scenario to the pipeline, effectively running them in a batch.
