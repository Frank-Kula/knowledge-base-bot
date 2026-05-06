# How to send a WebSocket request in Apidog?

WebSocket is an API technology that enables full-duplex communication over a single TCP connection. Compared to traditional HTTP requests, WebSocket offers lower latency and higher efficiency. It is well-suited for scenarios requiring persistent connections and real-time data transmission, such as online gaming, real-time chat, and more.

:::tip[]

WebSocket API management is supported in Apidog versions 2.2.34 and later.
  :::

## Creating a WebSocket endpoint

You can create a WebSocket endpoint within an HTTP project. 

1. Click the `+` button on the left and select `New WebSocket`.
2. Enter the WebSocket server URL, beginning with `ws` or `wss`.
3. Click `Connect`.
4. To disconnect the WebSocket endpoint, click `Disconnect`.

:::tip[]

For the best experience and to utilize the full feature set of the WebSocket API, we recommend using the Apidog client.
  :::

## Sending Messages

After establishing a WebSocket connection, you can compose messages under the `Message` tab.

<Background>
![](https://assets.apidog.com/help/assets/images/websocket-1-a610ef6cafff9ec207dd2daad67fc5b5.png)
</Background>
    
In addition to directly composing messages in text formats such as `Text`, `JSON`, `XML`, and `HTML`, you can also compose messages in binary formats using `Base64` or `Hexadecimal`.

The editor will apply syntax highlighting to the message content based on the selected message format. If the message is in `JSON`, `XML`, or `HTML` format, you can also format the input content.

## Viewing Messages 

The `Messages` section below displays the connection status, sent messages, and received messages in chronological order.

<Background>
![](https://assets.apidog.com/help/assets/images/websocket-2-384e88f9ecf503ba69e73fd1ae6320a4.png)
</Background>
    
Click a single message to view its details on the right:

- For text format messages, the formatted message will be displayed by default. You can manually switch the message format and encoding.

- For binary format messages, the message's `Hexdump` will be displayed by default. You can also view the message encoded with  `Base64` and the original message.

## Adding Handshake Request Parameters 

You can customize the parameters required during the WebSocket handshake, such as `Params`,`Headers`, and `Cookies`, to accommodate authentication or other complex scenarios.

<Background>
![](https://assets.apidog.com/help/assets/images/websocket-3-f2a3d0a20bccfe4764cc5c605462d015.png)
</Background>
    
:::tip[]
Handshake request parameters cannot be modified once the connection is established. They must be configured before establishing the connection or after disconnecting.
:::

## Using Variables 

You can use Apidog variables in the WebSocket connection's handshake and messages. Learn more about [Using variables](https://docs.apidog.com/using-variables-577908m0.md).

<Background>
![](https://assets.apidog.com/help/assets/images/websocket-4-a610ef6cafff9ec207dd2daad67fc5b5.png)
</Background>
    
## API Documentation

You can set the `status`, `responsible person`, and `tags` for the WebSocket API, and provide a detailed API description in `Markdown` format.

You can also share the WebSocket API documentation with external teams, who can view it directly in their browser.

## Saving the API 

After debugging is complete, click the `Save` button to save the WebSocket API to the directory tree of the `HTTP` project. This allows other team members to debug or view the API documentation.

<Background>
![](https://assets.apidog.com/uploads/help/2023/07/12/f6ff8b62d0f6df08eb4a34a9faa6ee11.png)
</Background>
    
## FAQ

**Q: Why is response validation not needed?**

A: For WebSocket requests, the HTTP status code must be `101` when establishing a connection, indicating a successful protocol upgrade. Therefore, validating the status code is typically not necessary.

**Q: There is no Auth tab. How can I authenticate the WebSocket API?**

A: Currently, two methods are recommended for WebSocket API authentication:

1. Pass the authentication information in a `Param`, `Header`, or `Cookie` field during the connection establishment.

2. Include the authentication information in a field within a message.

**Q: Does Apidog support pre-request/test scripts and assertions in WebSocket APIs?**

A: Not currently, but this feature will be evaluated for future iterations.

**Q: Are request and response examples supported?**

A: Not currently, but this feature will be evaluated for future iterations.

**Q: Why doesn't the WebSocket API support mocking?**

A: The current mocking library does not support WebSocket API definitions and therefore cannot generate message bodies based on the definition. 
