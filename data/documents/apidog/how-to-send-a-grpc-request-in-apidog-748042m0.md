# How to send a gRPC request in Apidog?

gRPC is an efficient, fast, and reliable Remote Procedure Call (RPC) framework widely used in various scenarios. In microservices architecture, Apidog facilitates efficient communication across services. For scenarios involving substantial data transfer, Apidog utilizes streaming capabilities to reduce network latency and bandwidth consumption.

:::tip[]
The gRPC API debugging functionality is currently in the Beta testing phase. Apidog version must be equal to or greater than 2.3.0 to use the gRPC API debugging feature.
:::

## Create a New gRPC Project

Click the "New Project" button on the Apidog homepage and select "gRPC Project (Beta)."
<Background>
![](https://assets.apidog.com/uploads/help/2023/12/28/4aaf1f823ba81c7b6ee50f2c3ed0454a.png)
</Background>

## Import Proto

gRPC follows an API-First approach, meaning that before development, services, methods, and messages must be defined through `.proto` files. Therefore, before debugging gRPC APIs using Apidog, you need to import the `.proto` file that serves as the API definition.

### Initial Import

Currently, there are two ways to import `.proto` files:

- Local file
- URL hosting the `.proto` file

<Background>
![](https://assets.apidog.com/uploads/help/2023/12/28/10b18c1027ee564bdce395caadcfe8b1.jpg)
</Background>
    
The selected `.proto` file will be imported as one Proto, where the service will be imported as a service, and rpc will be imported as methods.

If the chosen `.proto` file depends on other `.proto` files, you need to manually add the dependency directory.

Services from other `.proto` files that the selected `.proto` file depends on will also be imported into the same Proto if their package belongs to the same package as the selected `.proto` file.

### Reimport

If the imported `.proto` file undergoes changes, it can be reimported in Apidog: right-click on Proto, then click the "Reimport" button.

<Background>
![](https://assets.apidog.com/uploads/help/2023/12/28/6704d5b1d889fdf60303a0e18abddcfc.png)
</Background>
    
## Invocation Methods

When defining gRPC methods using `.proto` files, Apidog supports four types:

- Unary: One-way call
- Server Streaming: Server-side streaming
- Client Streaming: Client-side streaming
- Bidirectional Streaming: Bidirectional streaming

Apidog supports all four method types.

### Unary Call

Unary calls are similar to HTTP requests. Enter the URL in the address bar, input the message content in JSON format under the Message tab, click the "Invoke" button, and the unary call will be initiated.

<Background>
![](https://assets.apidog.com/uploads/help/2023/12/28/cfd111bf9783babdcfcc1a8c8ccf1338.png)
</Background>
    
Additionally, you can manually fill in Metadata and Auth information to meet authentication or other complex scenarios.

### Streaming Call

Streaming calls are similar to WebSocket connections. After initiating the call, you can write and send messages under the Message tab. Server streaming, client streaming, and bidirectional streaming fall under the streaming call types.

Apidog provides a timeline view that centrally displays the call status, sent messages, and received messages in chronological order. Clicking on a message allows easy viewing of message details.

<Background>
![](https://assets.apidog.com/uploads/help/2023/12/28/e94c4b468304e5f7674f87148bb88b5b.png)
</Background>
    
## Advanced Usage

### Auto-generate Dynamic Values

Apidog can recognize the content in `.proto` files, allowing you to click the "Auto-generate" button to generate the message body. For more flexible dynamic data, you can configure and generate expressions using the "Dynamic Values" feature.

Refer to the *["Dynamic Values"](/environments-and-variables/dynamic-variables)* for more detailed instructions.

<Background>
![](https://assets.apidog.com/uploads/help/2023/12/28/c2f48ec33377ced7c42679dab38f3b4d.png)
</Background>
    
### Use Variables

You can use Apidog variables in gRPC messages and Metadata.Refer to the *"[Environment Variable Types](/environments-and-variables/variables)"* documentation for detailed instructions.

<Background>
![](https://assets.apidog.com/uploads/help/2024/01/08/364e76da810fed9543090fedb9604f45.png)
</Background>
    
### Enable TLS

gRPC APIs support establishing secure connections through TLS.

Using Apidog, you can click on the protocol selector in front of the URL to quickly toggle the TLS status.

Additionally, Apidog is compatible with using `grpcs://` in the URL to enable TLS for the connection. Conversely, `grpc://` indicates TLS is not enabled.

<Background>
![](https://assets.apidog.com/uploads/help/2023/12/28/c695a4d4159b5269f828dffe4d1e3dc0.png)
</Background>
    
## Manage Server Addresses and Environments

Click the plus icon on the right side of the URL address bar to add the currently used server address to an environment.

<Background>
![](https://assets.apidog.com/uploads/help/2023/12/28/8b005fffb7b4dfbb7d23105dfc559fd9.png)
</Background>
    
Then, select the environment and server address in the upper right corner, and choose "Follow Default" in the URL address bar to use a unified server address for debugging all methods.

<Background>
![](https://assets.apidog.com/uploads/help/2023/12/28/d5a88aa851642916a87f32f64791db45.png)
</Background>
    
## View Proto Files and API Parameters

### View Proto File Content

In Apidog, clicking on the Proto in the left directory tree allows you to view the raw content of the `.proto` file.

<Background>
![](https://assets.apidog.com/uploads/help/2023/12/28/b1bcefb50b8e31c51fc3108fe9ea18bd.png)
</Background>
    
### View Request and Response Parameters

gRPC uses ProtoBuf as the serialization format, meaning that each message is transmitted in ProtoBuf format when sending or receiving messages. Unlike other text-based serialization formats (JSON, XML), ProtoBuf is a binary format not suitable for human writing and reading. Therefore, when calling gRPC APIs In Apidog, all messages are written and displayed in JSON format.

You can view the request and response parameters represented in JSON format on the API information page.

<Background>
![](https://assets.apidog.com/uploads/help/2023/12/28/b00a98d53096e20a246e2e909eb15b6c.png)
</Background>
    
ProtoBuf and JSON have a mapping relationship for data types, as shown in the table below:

| ProtoBuf 3             | JSON          | JSON Example                       |
| ---------------------- | ------------- | ---------------------------------- |
| message                | object        | `{"fooBar": v, "g": null, …}`      |
| enum                   | string        | `"FOO_BAR"`                        |
| map\<K,V\>               | object        | `{"k": v, …}`                      |
| repeated V             | array         | `[v, …]`                           |
| bool                   | boolean       | `true, false`                      |
| string                 | string        | `"Hello World!"`                   |
| bytes                  | base64 string | `"YWJjMTIzIT8kKiYoKSctPUB+"`       |
| int32, fixed32, uint32 | number        | `1, -10, 0`                        |
| int64, fixed64, uint64 | string        | `"1", "-10"`                       |
| float, double          | number        | `1.1, -10.0, 0, "NaN", "Infinity"` |

## Save Debugging Information

After completing debugging, click the "Save" button to save server URL, messages, Metadata, etc., in the current method for other team members to debug.
