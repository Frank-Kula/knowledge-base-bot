# Generating Requests

After creating an endpoint specification or importing an API spec, you can generate and send requests for debugging and validation.

## Generate Request Parameters

<Tabs>
    <Tab title="Design-first Mode">
    In Apidog's **Design-first Mode**, once you have specified an endpoint in the **Edit** tab, you can click the **Run** tab to switch to the sending request interface. Here, the corresponding request is automatically generated based on the endpoint specifications that you have defined.

    For `path` parameters, `query` parameters, `headers`, and `body` of type `form-data` or `x-www-form-urlencoded`, if you have specified an `example` in the endpoint specification, this example will automatically populate the `value` field in the **Run** interface as the initial request parameter value.

    <Background>
    ![Param example 1](https://api.apidog.com/api/v1/projects/544525/resources/341188/image-preview)

    ![Param example 2](https://api.apidog.com/api/v1/projects/544525/resources/341189/image-preview)
    </Background>

:::tip
If the parameters such as param name, description, type, or example in the `endpoint specification` are modified and saved in the **Edit** tab, the corresponding fields in the **Run** tab will also be updated accordingly. Any changes made in the spec will reflect across the entire development process, maintaining consistency and accuracy.
:::
  </Tab>
  <Tab title="Request-first Mode">
    In **Request-first Mode**, you can directly input request parameters.
  </Tab>
</Tabs>

## Generate Request Body

If your request body is of `JSON` or `XML` type, you can automatically generate the request body within Apidog without manually constructing it.

### Request Body Examples and Initial Content

<Tabs>
  <Tab title="Design-first Mode">
    If your endpoint specification includes a defined body example, this example will appear in the **Run** tab as the initial body content.

    If there is no body example defined in the endpoint specification, the body field in the **Run** tab will be left blank. However, you can click on **Auto-generate** to create a body structure that fits your requirements.

    <Background>
    ![Auto-generate request body example](https://api.apidog.com/api/v1/projects/544525/resources/351686/image-preview)
    </Background>
  </Tab>
  <Tab title="Request-first Mode">
    In **Request-first Mode**, if you have already specified the Data Schema, you can click **Auto-generate** to create the JSON or XML body.

    <Background>
    ![Auto-generate in Request-first Mode 1](https://api.apidog.com/api/v1/projects/544525/resources/352070/image-preview)
    
    ![Auto-generate in Request-first Mode 2](https://api.apidog.com/api/v1/projects/544525/resources/352069/image-preview)
    </Background>
  </Tab>
</Tabs>

### Auto-Generate Options

> Apidog version 2.7.0 or later is required.

Apidog provides a variety of data auto-generation options to meet different needs. You can select from multiple generation methods in the **Auto-generate** dropdown menu:

<Background>
![Auto-generate data options](https://api.apidog.com/api/v1/projects/544525/resources/351687/image-preview)
</Background>

#### 1. Examples

- **Feature:** Manually selects a predefined request body example.
- **Use Case:** Manually switch between predefined examples for different business scenarios, such as normal requests, exception requests, or boundary value testing.

#### 2. Generate Each Time

- **Feature:** Regenerates data following [smart mock rules](https://docs.apidog.com/smart-mock-618190m0.md) each time a request is sent.
- **Use Case:** Ideal for dynamic data requirements.
- **Note:** When **Generate Each Time** is enabled, the body content becomes uneditable until this option is disabled.

<Background>
![Generate each time](https://api.apidog.com/api/v1/projects/544525/resources/351690/image-preview)
</Background>

#### 3. Auto-Generation Preference

Clicking **Auto-generation Preference** opens a pop-up window where you can select the rules you prefer for automatically generating data.

<Background>
![Auto-generation preference](https://api.apidog.com/api/v1/projects/544525/resources/351692/image-preview)
</Background>

- **Use Example Values First**
  - **Feature:** If example values are defined in the request data schema, they will be used for automatic generation. If no example values are configured, a random value will be generated based on the Mock rules.
  - **Use Case:** Ideal for scenarios where some fields require fixed values, while others can be dynamically generated.

  <Background>
  ![Field examples values](https://api.apidog.com/api/v1/projects/544525/resources/351700/image-preview)
  </Background>

- **Use Default Values First**
  - **Feature:** If default values are defined in the request data schema, they will be used for automatic generation. If no default values are configured, a random value will be generated based on the Mock rules.
  - **Use Case:** Suitable for debugging scenarios where preset values need to be retained.

  <Background>
  ![Field default value](https://api.apidog.com/api/v1/projects/544525/resources/351701/image-preview)
  </Background>

- **Use Mock Value**
    - **Feature:** Generates data based on Smart Mock rules.
    - **Use Case:** Quickly generate complete test data.

- **Generate Field Names Only**
    - **Feature:** Generate field names only using the request data schema, leaving values blank.
    - **Use Case:** Useful for testing scenarios where specific values need to be manually filled in.

- **Use Request Example**
    - **Feature:** Randomly selects a predefined request example.
    - **Use Case:** Quickly switch between different business scenarios, such as normal or exception requests.

## Insert Dynamic Value

You can use **Dynamic Values** to generate values for both request parameters and request body. This allows dynamic values to be automatically mocked and inserted into the request each time it is sent.

Next to the input box for each request parameter, you will see a <Icon icon="ph-bold-magic-wand"/> **magic wand** icon for dynamic variables—clicking this icon will insert a dynamic value.

<Background>
<p style="text-align: center">
    <img src="https://api.apidog.com/api/v1/projects/544525/resources/341888/image-preview" style="width: 640px" />
</p>
</Background>

Similarly, in the request body, you can click on the <Icon icon="ph-bold-magic-wand"/> **Insert Dynamic Value** button to insert dynamic values within JSON or XML bodies.

<Background>
<p style="text-align: center">
    <img src="https://api.apidog.com/api/v1/projects/544525/resources/341889/image-preview" style="width: 340px" />
</p>
</Background>

:::tip
Learn more about [Dynamic Values](https://docs.apidog.com/dynamic-values-541766m0.md).
:::

## Send Request

Click **Send** to send the request.

:::tip
Learn more about [Sending Requests](https://docs.apidog.com/sending-requests-548328m0.md).
:::

