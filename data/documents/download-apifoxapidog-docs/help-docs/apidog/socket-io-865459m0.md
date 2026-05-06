# Socket.IO

Socket.IO is a library that enables low-latency, bidirectional, and event-based communication between clients and servers. It provides real-time, two-way communication channels over WebSocket connections with automatic fallback to HTTP long-polling when WebSocket is unavailable.

## Prerequisites

- Apidog version 2.7.0 or later
- A Socket.IO server endpoint (supports `ws://` and `wss://` protocols)

## Creating a Socket.IO Endpoint

<Steps>
  <Step title="Create a new Socket.IO endpoint">
  - Hover over the **"+"** button on the left panel of your project
  - Click on **"New Socket.IO"**
      
<Background>
![CleanShot 2025-11-05 at 17.17.02@2x.png](https://api.apidog.com/api/v1/projects/544525/resources/365354/image-preview)
</Background>

  </Step>
  <Step title="Enter the server address">
  - Input the server address (e.g., `ws://localhost:3000`)
  - Supports both `ws://` and `wss://` protocols
<Background>
![enter-server-address.png](https://api.apidog.com/api/v1/projects/544525/resources/351707/image-preview)
</Background>

  </Step>
  <Step title="Establish connection">
  - Click the **"Connect"** button to connect to the server
<Background>
![connecting-socket-io-endpoint.png](https://api.apidog.com/api/v1/projects/544525/resources/351708/image-preview)
</Background> 
  </Step>
</Steps>

## Listening to Events

Open the **Events** tab and enter the event name you want to listen to (e.g., `new message`). Disable **Listen** for a specific event to stop receiving messages for that event.

<Background>
![adding-listening-events.png](https://api.apidog.com/api/v1/projects/544525/resources/351709/image-preview)
</Background>

### Event Listening Rules

| Rule | Description |
|------|-------------|
| **Default Event** | System listens to the `message` event by default |
| **Dynamic Changes** | Adding or removing events does not affect existing connections |
| **Event Name Changes** | Changing an event name automatically stops listening to the original event |

## Sending Messages

### Events & Arguments

<Steps>
  <Step title="Set up events and arguments">
  - **Event:** Defaults to `message`, but you can customize it (e.g., `new message`)
  - **Argument:** Supports JSON, text, and Binary formats
  </Step>
  <Step title="Send the message">
 Click the **"Send"** button
  </Step>
  <Step title="View records">
  Check the timeline for sending records with event tags
  </Step>
</Steps>

<Background>
![viewing-sending-records.png](https://api.apidog.com/api/v1/projects/544525/resources/351711/image-preview)
</Background>

### Acknowledgment (Ack)

When you enable the **Ack** option, the server sends back a callback message after receiving and processing the request.

<Background>
![message-status.png](https://api.apidog.com/api/v1/projects/544525/resources/351716/image-preview)
</Background>

### Multiple Arguments

Click **"+ Add Argument"** to include additional arguments.

<Background>
![adding-multiple-arguments.png](https://api.apidog.com/api/v1/projects/544525/resources/351719/image-preview)
</Background>

When you send a message with multiple arguments, the timeline displays a label like **"x Args"**. Click on it to expand and view all arguments. Switch between tabs on the right for more details.

<Background>
![sending-messages-with-multiple-arguments.png](https://api.apidog.com/api/v1/projects/544525/resources/351718/image-preview)
</Background>

## Handshake Request Parameters

You can include request parameters in the **URL**, **Params**, **Headers**, or **Cookies**.

<Background>
![handshake-request-parameters.png](https://api.apidog.com/api/v1/projects/544525/resources/351720/image-preview)
</Background>

## Client Version and Handshake Path

<Steps>
  <Step title="Configuration Entry">
 Go to **Settings** under **Request**
<Background>
![handshake-path-configuration.png](https://api.apidog.com/api/v1/projects/544525/resources/351721/image-preview)
</Background>

  </Step>
  <Step title="Client Version">
 The default is **v4**. If the server uses an older version (e.g., v2/v3), manually switch the client version
  </Step>
  <Step title="Handshake Path">
 The default is `/socket.io`. If the server uses a custom path (e.g., `/custom`), update the path accordingly
  </Step>
</Steps>

## Using Variables

Apidog enables you to include variables in your arguments. When you send a message, these variables are automatically replaced with their real values.

<Background>
![using-variables-in-argument.png](https://api.apidog.com/api/v1/projects/544525/resources/351722/image-preview)
</Background>

## Saving the Endpoint

Once debugging is complete, click the **"Save"** button to store the Socket.IO endpoint in the HTTP project's folder tree. This makes it easy for team members to access, debug, and view the endpoint documentation, improving collaboration and efficiency.

## Generating Endpoint Documentation

Easily manage your Socket.IO endpoint by setting its **status**, assigning a **maintainer**, and adding relevant **tags**. You can also write detailed descriptions using **Markdown**. With Apidog, you can generate online API documentation and share the URL with your team for seamless collaboration.

<Background>
![socket-io-endpoint-documentation.png](https://api.apidog.com/api/v1/projects/544525/resources/351724/image-preview)
</Background>

## FAQs

<Accordion title="What to do if the connection fails?" defaultOpen>

**Checklist:**
- Make sure the server is running
- Verify that the client version is compatible with the server
- Ensure the firewall isn't blocking the required port
</Accordion>

<Accordion title="Not receiving all arguments?" defaultOpen={false}>
**Possible Fixes:**

1. Review the server's argument handling logic. Example:
    
```js
socket.on('event', (...args) => {
  const callback = typeof args[args.length - 1] === 'function' 
    ? args.pop() 
    : null;
  //   // Process the args  
});
```
2. Double-check the argument order and types
</Accordion>

<Accordion title="ACK Not Triggered?" defaultOpen={false}>
Ensure that the server is calling `callback()`.
</Accordion>

