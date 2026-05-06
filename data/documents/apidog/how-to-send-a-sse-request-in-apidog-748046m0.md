# How to send a SSE request in Apidog?

SSE is a real-time communication technology built upon the HTTP protocol. It enables a persistent, unidirectional connection between the client and server, allowing the server to push asynchronous messages to the client.

## Initiating an SSE Connection

To establish an SSE connection, create a new API within your HTTP project. Upon sending the request, if the response header `Content-Type` includes `text/event-stream`, Apidog will automatically parse the returned data as SSE events. The response content will be updated in real-time within a new timeline view, eliminating the need to wait for the server to close the connection.

<Background>
![](https://assets.apidog.com/help/assets/images/initiating-SSE-Connection-e82fd0e6dadbdb4337b44a3905054240.png)
</Background>

## Extracting Message Content with Post-Request Scripts

You can utilize custom scripts in the [Post processor scripts](https://docs.apidog.com/post-processor-scripts-593611m0.md) section of your API to extract specific field values from each SSE event and concatenate them into a complete string.

For instance, consider the API illustrated in the diagram above. Each message returned by this API contains a JSON structure. Our objective is to extract the `answer` field from the response and combine its parameter contents into a single text string.

<Background>
![](https://assets.apidog.com/help/assets/images/initiating-SSE-Connection-e82fd0e6dadbdb4337b44a3905054240.png)
</Background>

Insert the following example code into the custom script:

```js
// Get the response text
const text = pm.response.text()
// Split the text into lines
var lines = text.split('\n');
// Create an empty array to store the "content" parameter
var contents = [];
// Iterate through each line
for (var i = 0; i < lines.length; i++) {
    const line = lines[i];
    // Skip lines that do not start with "data:"
    if (!line.startsWith('data:')) {
        continue;
    }
    // Try to parse the JSON data
    try {
        var data = JSON.parse(line.substring(5).trim());  // Remove the leading "data: "
        // Get the "content" parameter from the "choices" array and add it to the array
        contents.push(data.choices[0].delta.content);
    } catch (e) {
        // Ignore the current line if it is not valid JSON data
    }
}
// Join the "content" parameters using the join() method
var result = contents.join('');
// Display the result in the "Visualize" tab of the body
pm.visualizer.set(result);
// Print the result to the console
console.log(result);
```

After sending the request, the concatenated text will be displayed in the `Visualize` section of the Body.

<Background>
![](https://assets.apidog.com/uploads/help/2023/08/29/8f786645f89b084e1da10ac68d2c866f.png)
</Background> 

