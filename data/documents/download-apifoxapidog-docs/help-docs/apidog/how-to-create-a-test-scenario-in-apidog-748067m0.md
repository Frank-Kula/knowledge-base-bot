# How to create a test scenario in Apidog?

## Create a test scenario

Upon opening Apidog, navigate to “Tests” module, and then click the `+` next to the search bar to create a new test scenario. Select the appropriate directory for it, and set the priority to complete the creation.

<Background>
  ![](https://api.apidog.com/api/v1/projects/544525/resources/342962/image-preview)
</Background>

## Add test steps

Once you have set up your test scenario in Apidog, you can start populating it with requests. There are several ways to add requests, each tailored to different needs and flexibility:

1. **Requests linked to the API spec**—These requests could be updated as the API specification changes:
   - **a. Import from endpoint spec**: This method involves importing requests straight from the structured definition within the API spec. It ensures your tests align with the API's documented interface, although you may need to manually adjust request parameters to meet specific testing conditions.
   - **b. Import from endpoint case**: Utilize this option to pull requests from predetermined endpoint cases that already contain configured parameters. This is particularly useful for standardized tests that simulate real-world API usage, enabling consistency across test runs.

2. **Independent requests not associated with the API spec**—These requests do not update in response to changes in the API spec. They allow for greater customization:
   - **a. Add custom request**: Craft requests from scratch to tailor test scenarios to specific requirements. This approach offers maximum flexibility to explore beyond the bounds of the existing API specification.
   - **b. Add from cURL**: Leveraging cURL lets you import or sculpt customized requests efficiently. It's a handy way to quickly create requests that mimic complex or unique API interactions without being constrained by the API spec.

3. **Reference other test scenarios**:
   - **a. Include requests from other test scenarios**: This method allows you to import specific requests from different test scenarios already defined in your project. 
   - **b. Reference other test scenario**: For comprehensive testing, you might need to employ the entirety of another test scenario. This capability ensures that you can integrate all related tests and configurations, avoiding the need to duplicate setup efforts and fostering unified testing strategies.

<p style="text-align:center">
    <img src="https://api.apidog.com/api/v1/projects/544525/resources/342963/image-preview" style="width:440px" />
</p>

### Import from endpoint spec

You can import endpoint specs from the current project as steps in the test scenario. There are two modes when importing endpoints: "Manual" and "Automated." For more detailed instructions, please refer to [Sync Data from APIs/API Cases](/automated-testing/test-scenarios/sync-data-from-api-cases).

- **Manual**

  In "Manual" mode, modifications to the endpoint documentation within the project do not have an immediate impact on the endpoints in the test steps. Synchronization of test data only occurs when testers activate the "Manual" button. It is important to note that alterations made to the test step data will not update the endpoint documentation, even when clicking for "Manual Sync". Instead, clicking this button enables the test scenarios to retrieve information from the endpoint documentation for synchronization purposes.

- **Automated**

  In the "Automated" mode, any changes in the endpoint documentation within the project will be updated synchronously in the test steps.
<Background>
![](https://assets.apidog.com/uploads/help/2024/06/03/9d17cd43ffaa9c900adbee6909f69587.png)
</Background>
:::tip[]
If you need to test endpoints from other projects in one test scenario, please refer to [Import Endpoints/Cases from Other Projects to Test Steps](/automated-testing/test-scenarios/import-apis-cases-from-other-projects-to-test-steps).
:::


### Import from Endpoint Case

You can choose to import endpoint cases from the current project or other projects. There are two modes when importing endpoint cases: **"Copy"** and **"Reference"**.

- **Copy**

  When importing an endpoint case as **"Copy"**, the parameters in the endpoint case will also be copied into the test steps. They will be independent of each other, and changes in each will not affect the others. Manual sync can be selected.

- **Reference**

  When importing an endpoint case as **"Reference"**, it will directly use the endpoint case from the original project for the request.
<Background>
![](https://assets.apidog.com/uploads/help/2024/06/03/05273dbe9767dddcefec4ccc64462656.png)
</Background>
### Add Custom Request

In a working process, you may need to call an endpoint outside of the project, such as a third-party payment endpoint. 

You can add a custom API request in the test steps. The custom request can be any HTTP request, including common `GET`, `POST`, `PUT`, `DELETE`, etc.

<p style="text-align:center">
    <img src="https://assets.apidog.com/uploads/help/2024/06/03/4182058b8246800d3a70820ca6de742f.png" style="width:640px" />
</p>


### Add from cURL

In a real working processes, many endpoint requests are presented in the form of `cURL` command lines. You have the option of importing cURL requests into the test steps, with just a single click.

<p style="text-align:center">
    <img src="https://assets.apidog.com/uploads/help/2024/06/03/8b0f8582fb54e898d735820a0697e6ec.png" style="width:640px" />
</p>

### Include steps from Other Test Scenarios

You can clone the test steps or process control conditions by importing from other test scenarios within the same project.

<Background> 
    ![](https://assets.apidog.com/uploads/help/2024/06/03/a99162a148847c98c6efc48cbfdce069.png)
</Background>

### Reference Other Test Scenarios

You can reference other test scenarios as a test step. There are two use cases:

1. If your business process has some common, reusable API test steps, you can compile these steps into a small test scenario and then reference it directly in other wider test scenarios.
2. If you need to regress the mainstream process of the entire product, you can refer to the various sub-test scenarios in the test scenario for assembly, and complete the test regression work of all mainstream processes with one click.

:::tip[]
To prevent infinite loops and situations where the test scenario cannot stop running normally, the feature of referencing other test scenarios cannot reference the original test scenario itself.
:::

<p style="text-align:center">
    <img src="https://assets.apidog.com/uploads/help/2024/06/03/7c9d9e3bc62fd137993f8375ae607eb2.png" style="width:640px" />
</p>

## Orchestrate the test scenario

Clicking any test step will enter the orchestrate mode. In this mode, you have a larger operating page to better and more efficiently fill in the detailed content of each test step. The left side of the page is the overall flow of the test scenario, and the right side is the details of the selected test step. Endpoint requests and testing process control components will have different display panels.

You can adjust the order of the steps by dragging the `≡` in front of the step.

You can use the "⬆️" and "⬇️" keys to quickly switch between the selected test steps in this mode.
<Background>
![](https://assets.apidog.com/uploads/help/2024/06/03/ad0e33b01cc06604ec02c9565bcbb324.png)
</Background>
In the orchestrate mode, you can edit multiple steps and then click the "Save All" button in the top left corner to save all the changes.

If any step has unsaved changes, the step will be marked with a dot in the list bar on the left. Remember to always save the changes you have made.
<Background>
![](https://assets.apidog.com/uploads/help/2024/06/03/6f3150d2b83a2685e2b40d1c356782c7.png)
</Background>
