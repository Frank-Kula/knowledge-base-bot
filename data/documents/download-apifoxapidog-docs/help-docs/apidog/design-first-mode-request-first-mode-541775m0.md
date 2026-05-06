# Design-first Mode & Request-first Mode

Apidog's APIs module features two modes that can be switched at the bottom left corner of the interface: `Design-first Mode` and `Request-first Mode`.

<p style="text-align: center">
    <img src="https://api.apidog.com/api/v1/projects/544525/resources/342735/image-preview" style="width: 640px" />
</p>

Both modes provide similar functionalities but with different interfaces, catering to different team workflows. 

**Design-first Mode** is Apidog's recommended mode, suitable for teams following the API-Design First approach. In this mode, teams spec the API first and then proceed with development and testing based on the API spec. 

On the other hand, **Request-first Mode** is ideal for teams that do not initially define the API specifications. These teams typically focus on backend development, finalize the code, and then produce the API spec for testing and client-side work to begin. 

If you need to call APIs developed by someone else but you don't have the documentation, you should also use Request-first Mode.

## Design-first Mode

In **Design-first Mode**, editing the API spec and sending requests are accessed through separate tabs. Users modify the API spec in the **Edit** tab and send requests in the **Run** tab. 

![image.png](https://api.apidog.com/api/v1/projects/544525/resources/342736/image-preview)

This separation suits teams following the API-Design First approach, where API architects and developers/consumers have distinct roles. API architects define the API spec without sending requests, while developers focus on API development and testing without altering the API spec. 

The divided tabs align with the usage habits of such teams. In the Edit tab, API architects can specify request examples, which are automatically set as default parameter values in the Run tab. API developers/consumers can further modify parameter values and request bodies in the Run tab.

## Request-first Mode

**Request-first Mode** is suitable for teams that do not specify APIs beforehand. Backend developers directly work on API development and may require calling APIs for debugging during development. 

In this mode, developers do not need to specify the API initially; instead, they can input a request directly, similar to creating a new request in Postman. In this interface, developers can easily modify parameter types, names, values, body components, and more without the need to separately tweak the API spec and request parameter values. 

![image.png](https://api.apidog.com/api/v1/projects/544525/resources/342737/image-preview)

Once debugging is completed and saved, the request is automatically **parsed** into an endpoint spec. Parameters are translated into spec parameters and example values, while the request/response body is parsed into a schema, and the body values are interpreted as request/response examples. Developers can further refine and enhance this endpoint spec based on their requirements.


## Differences between modes

The key difference between the two modes is that in Request-first Mode, the request body is used as the endpoint request body example. In contrast, in Design-first Mode, users can input an actual request body in the Run tab along with the request body example. Therefore, the body section in the **Run** tab is ONLY available in Design-first Mode and is not visible in Request-first Mode.

Another difference is that in Design-first Mode, you can add a pre/post-processor at the endpoint spec level or at the run/endpoint case level. Whereas, in Request-first Mode, since there is no Run tab, all pre/post-processors are considered to be at the endpoint spec level. The run/endpoint case level pre/post-processors are invisible in Request-first Mode.

