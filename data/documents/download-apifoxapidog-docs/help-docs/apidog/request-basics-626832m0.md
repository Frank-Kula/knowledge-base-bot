# Request Basics

The Apidog client supports sending API requests with HTTP, GraphQL, SOAP, gRPC, and other popular protocols. You can create requests in Apidog, send them to observe the responses, and save them for team collaboration.

## Create a New Request

To create a request in Apidog, you only need to click **"+"** → **"New Request"**.

<Background>
![CleanShot 2025-11-05 at 17.18.55@2x.png](https://api.apidog.com/api/v1/projects/544525/resources/365356/image-preview)
</Background>

You can fill in the necessary parts of the request according to the API spec into the Apidog interface, such as the request method, URL, request parameters, authorization, and so on.

Using this method, you can create `HTTP`, `GraphQL`, and `SOAP` requests. Learn more about creating `WebSocket` and `gRPC` requests in the respective protocol documentation.

### Request URL

To make a request in Apidog, you need to specify the URL representing the API endpoint you're connecting to. Each operation you can perform using an API is typically associated with an endpoint, which has a particular URL.

- **If you're building an API**: The URL will usually consist of the base location plus a path. For instance, in the request URL `https://api.example.com/user/12`, `https://api.example.com` is the base URL, and `/user/12` is the endpoint path.

- **If you're using a public API**: Your API provider will provide the URLs you need in their developer documentation.

You can enter query parameters in the URL field, or you can enter them in the **Params** tab. If your request uses path parameters, you can enter them in the URL field.

:::tip[]
Apidog will automatically add `http://` to the beginning of your URL if you don't specify a protocol.
:::

## Request Methods

In Apidog, you can select which request method to use on the left side of the request URL. The default method is GET.

### Common HTTP Methods

| **Method** | **Purpose** | **Effect on Data** |
| --- | --- | --- |
| **GET** | Retrieve data from a specified resource | Read-only, no side effects |
| **POST** | Submit data to be processed to a specified resource | Creates new resources |
| **PUT** | Update existing resources | Replaces entire resource |
| **PATCH** | Apply partial modifications to a resource | Updates specific fields |
| **DELETE** | Request the removal of a resource | Removes resource |

In API design, the same URL can be requested with different methods, representing different operations on the same resource. For example, `GET /user/{id}` typically retrieves the user information for this id, while `PUT /user/{id}` updates the user information for this id.

## Send the Request

After you specify the request protocol, method, and URL, add any other details required by the API you're sending the request to:

- **Parameters and Body**: Provide any parameters, body data, or request headers that need to be sent with the request.
- **Authentication**: Set up any required authentication and authorization.
- **Cookies**: You also have the option to use cookies with your requests by selecting the Cookies tab.

Once you've entered all the request details, select **Send** to transmit the request to the API server. You can view the response from the server in the response pane.

:::info[]
You can view requests you've sent in **History** in the sidebar and send them again. This is useful for debugging and comparing responses over time.
:::

