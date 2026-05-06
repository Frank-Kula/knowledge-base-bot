# Sending Requests

Click **Send** in the **Run** tab of the endpoint to send a request.

The **Run** interface in Endpoint and the **Request** interface are very similar. The main difference is that **Run** is based on the endpoint, it can generate requests and validate responses based on the endpoint spec. When the endpoint spec changes, the **Run** interface will also be updated accordingly. On the other hand, **Requests** are independent and not related to the API spec.

<Video src="https://www.youtube.com/watch?v=4W3D2gHPp8c"></Video>

## Send Requests

When you send a request, Apidog displays the response received from the API server in a way that lets you examine, visualize, and troubleshoot it.

<Background>
<p style="text-align: center">
    <img src="https://api.apidog.com/api/v1/projects/544525/resources/341992/image-preview" style="width: 640px" />
</p>
</Background>

This interface is divided into two sections: the top half is where you input the request you want to send, and the bottom half displays the request you actually send, the response you receive, as well as the validation and assertion results for the response.

:::tip
You can hover over the **partition** button in the bottom right corner to adjust the layout of the Run interface. You can choose to split the interface horizontally, vertically, or no split.
<p style="text-align: center">
    <Background>
    <img src="https://api.apidog.com/api/v1/projects/544525/resources/342693/image-preview" style="width: 340px" />
    </Background>
 </p>
:::

### Actual Request

In the top half section, you may utilize variables, dynamic values, scripts, etc., to adjust the request you send. How to view the actual request being sent? You can see the complete actual request in the **Actual Request** tab in the bottom half.

<Background>
<p style="text-align: center">
    <img src="https://api.apidog.com/api/v1/projects/544525/resources/341995/image-preview" style="width: 440px" />
</p>
</Background>

### Validate the Response

Apidog automatically validates whether the response conforms to the schema based on the endpoint's specification. You can choose to enable or disable validation, as well as select which response to validate against.

:::tip
Learn more about [Validating Responses](https://docs.apidog.com/validating-responses-541768m0.md).
:::

### Extract the Response

Apidog supports extracting responses into the endpoint specification, which can be extracted as **response schema** or **response examples**.

<Background>
<p style="text-align: center">
    <img src="https://api.apidog.com/api/v1/projects/544525/resources/342694/image-preview" style="width: 400px" />
</p>
</Background>

## Modify Requests

You can modify requests in the **Run** tab. You can change parameter values or toggle the checkboxes in front of parameters to alter the request. These actions do not conflict with the endpoint specification.

Sometimes, you may need to modify the parameter types or add/remove parameters. In this case, the request deviates from the endpoint specification. In Apidog, these inconsistencies are highlighted in orange.

<Background>
![Inconsistent request](https://api.apidog.com/api/v1/projects/544525/resources/341998/image-preview)
</Background>

Hovering over these orange markers will display the differences between the specification and the current request. You can click **Revert** to restore it to the state that matches the specification, or click **Save to endpoint spec** to update the specification. You can also click the **Inconsistent** button in the top right corner to batch revert or save all differences to the endpoint specification.

## Save Requests

In the **Run** tab, there is no Save button. This is because, for an endpoint spec, it does not include the content of requests.

For debugging convenience, Apidog provides a **Stash** button. Clicking Stash will save the current content in the Run interface without affecting the endpoint spec, and the content will not be synchronized with others.

<Background>
<p style="text-align: center">
    <img src="https://api.apidog.com/api/v1/projects/544525/resources/342000/image-preview" style="width: 640px" />
</p>
</Background>

If you wish to persistently save a request, you can click **Save as case**. This request will be saved in the form of an endpoint case under the endpoint's hierarchy.

<Background>
<p style="text-align: center">
    <img src="https://api.apidog.com/api/v1/projects/544525/resources/342001/image-preview" style="width: 240px" />
</p>
</Background>

You can save each usage scenario of this endpoint as an endpoint case, facilitating developers' debugging and providing an easy way to import it into automated testing as a step.

:::tip
Learn more about [Debugging Cases](https://docs.apidog.com/debugging-cases-541771m0.md).
:::

:::tip
When importing a Postman Collection, each Postman request corresponds to an endpoint case in Apidog. Therefore, they will be displayed as a `success` case under the endpoint hierarchy, rather than within the endpoint specification.
Learn more about [migrate from Postman](https://apidog.com/blog/migrate-postman-enviornments-collection-to-apidog/).
:::

## Q&A

**Q: Why does the same request work correctly in other tools (such as Postman) but not in Apidog?**

A: If the requests are identical, then the responses should also be identical regardless of the tool used. If you are getting different responses, you can switch to the **Actual Request** tab and compare the request you sent in other tools to identify any differences.

