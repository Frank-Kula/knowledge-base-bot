# Assertion

Assertions play a crucial role in API testing, allowing you to verify if the response meets your expectations. Apidog provides a visual interface for creating assertions, making it easy to define test conditions without writing scripts. For advanced scenarios, you can still use custom scripts with full Postman syntax compatibility.

## Adding an Assertion

<Steps>
  <Step>
    **Navigate to Post Processors**
    
    Open the **Run** tab (Design-first Mode) or **Request** tab (Request-first mode) and scroll to the **Post Processors** section.
    
    <Tabs>
      <Tab title="Design-first Mode">
        <Background>
          ![Post Processors in Design Mode](https://api.apidog.com/api/v1/projects/544525/resources/352194/image-preview)
        </Background>
      </Tab>
      <Tab title="Request-first Mode">
        <Background>
          ![Post Processors in Request Mode](https://api.apidog.com/api/v1/projects/544525/resources/352193/image-preview)
        </Background>
      </Tab>
    </Tabs>
  </Step>
  <Step>
    **Add Assertion Processor**
    
    Hover over **+ Add** and select **Assertion**.
    
    <Background>
      ![Add Assertion Menu](https://api.apidog.com/api/v1/projects/544525/resources/352195/image-preview)
    </Background>
  </Step>
  <Step>
    **Configure Assertion Rule**
    
    Select the validation target (e.g., headers, body, status code). Use `$` to represent the root object for JSON responses.
    
    *   **Example**: To specific checks `status` field in `data` object, use `$.data.status`.
    
    <Background>
      ![Configure Assertion Target](https://api.apidog.com/api/v1/projects/544525/resources/348239/image-preview)
    </Background>
  </Step>
  <Step>
    **Set Conditions**
    
    Define the criteria (e.g., `Equals`, `Contains`, `Is Null`). You can compare against static values or dynamic variables like `{{variable}}`.
  </Step>
  <Step>
    **Execute and Verify**
    
    Click **Send**. Results will appear in the **Assertion** tab of the response panel.
    
    <Background>
      ![Assertion Results](https://api.apidog.com/api/v1/projects/544525/resources/342854/image-preview)
    </Background>
  </Step>
</Steps>

:::tip
All data in visual assertions is automatically converted to **STRING** for comparison. For precise type checking (e.g., distinguishing `4` from `4.0`), consider using [Custom Scripts](https://docs.apidog.com/use-scripts-in-apidog-593582m0.md) instead.
:::

## Quick Assertions from Response

You can instantly create assertions based on the actual response data:

1.  Hover over any field in the response body or header.
2.  Click the **Assertion** button that appears.
3.  Modify the auto-generated rule if needed.

<Background>
  ![Quick Assertion from Response](https://api.apidog.com/api/v1/projects/544525/resources/348240/image-preview)
</Background>

## Script-Based Assertions

For advanced validation logic, you can use the `pm.test` syntax in Custom Scripts. Apidog is fully compatible with Postman scripts.

:::highlight purple
Learn more about [Scripting](https://docs.apidog.com/use-scripts-in-apidog-593582m0.md).
:::

