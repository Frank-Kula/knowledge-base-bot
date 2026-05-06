# Send Requests in Apidog

Apidog enables you to send API requests for development, testing, and integration purposes. Whether you're building your own API or integrating with external services, you can fetch, add, or remove data while transmitting parameters and authorization information.

For example, when developing a shop application, you might send a login request, retrieve a product list, and create an order—all through Apidog's request interface.

## Sending a Request

<Video src="https://www.youtube.com/watch?v=_b-Z6mMHcGA"></Video>

<Steps>
  <Step>
In Apidog, click **"+"** → **"New Request"** to create a new request.

<Background>
![CleanShot 2025-11-05 at 17.15.25@2x.png](https://api.apidog.com/api/v1/projects/544525/resources/365353/image-preview)
</Background>

  </Step>
  <Step>
Fill in the request details according to the API specification, including:

- **Request method** (GET, POST, PUT, DELETE, etc.)
- **URL** (endpoint address)
- **Request parameters** (query, path, body)
- **Authorization** (if required)

<Background>
![image.png](https://api.apidog.com/api/v1/projects/544525/resources/343866/image-preview)
</Background>
  </Step>
  <Step>
Click **"Send"** to execute the request. The server's response appears in the lower half of the interface, enabling you to debug and develop based on the results.
  </Step>
</Steps>

## Next Steps

Explore the following topics to master API requests in Apidog:

| Topic | Description |
|-------|-------------|
| [Create and Send API Requests](https://docs.apidog.com/request-basics-626832m0.md) | Learn the basics of building requests—including parameters, headers, and body data |
| [Authentication and Authorization](https://docs.apidog.com/authentication-and-authorization-in-apidog-629096m0.md) | Configure identity verification and access control for secure API connections |
| [Response Data and Cookies](https://docs.apidog.com/response-and-cookies-in-apidog-629648m0.md) | View, visualize, and manage API response data and cookies |
| [Variables and Environments](https://docs.apidog.com/using-variables-577908m0.md) | Reuse data throughout requests and adapt values based on your working environment |

### Additional Protocols

Beyond HTTP requests, Apidog supports multiple protocols for diverse API communication needs:

- **[GraphQL](https://docs.apidog.com/graphql-629866m0.md)** - Query language for APIs with flexible data retrieval
- **[gRPC](https://docs.apidog.com/grpc-629868m0.md)** - High-performance RPC framework
- **[WebSocket](https://docs.apidog.com/websocket-629877m0.md)** - Full-duplex communication channels
- **[SSE](https://docs.apidog.com/sse-debugging-629889m0.md)** - Server-Sent Events for real-time updates
- **[SOAP/WebService](https://docs.apidog.com/soap-or-webservice-629910m0.md)** - XML-based messaging protocol

