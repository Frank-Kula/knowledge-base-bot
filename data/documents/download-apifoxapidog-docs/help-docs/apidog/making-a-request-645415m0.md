# Making a Request

This guide walks you through the process of sending API requests, from setting up environments to executing real requests. Whether you're testing endpoints or integrating with live services, follow these steps to get started.

## Prerequisites

Before sending requests, ensure you have:
- A project created in Apidog
- At least one [endpoint](https://docs.apidog.com/creating-an-endpoint-644726m0.md) defined or a URL ready for testing

## Step-by-Step Guide to Sending Requests
### 1. Create A Quick Request

Begin by clicking on the **Quick Request** button in a new tab or going to **Quick Requests** at the bottom of the directory tree and creating a new one. 

<Background>
<img src="https://api.apidog.com/api/v1/projects/544525/resources/369340/image-preview" alt="Quick Request Button"/>
</Background>

Then and enter the URL on the URL bar. Here's an example URL: `https://api.petstoreapi.com/v1/pets`


<Background>
![image.png](https://api.apidog.com/api/v1/projects/544525/resources/370056/image-preview)
</Background>

### 2. Send the Request

Click the **Send** button to execute your request. The system will process the request and provide the response form the API.

### 3. Review Response

Examine the response in the **Response** area, which displays:

- Status code
- Response headers
- Response body
- Response time

### 4. Inspect Actual Request Details

Switch to the **Actual Request** tab to view the complete HTTP request that was sent, including:

- Full URL
- Headers
- Request body
- Client Code

### 5. Save Request as Endpoint

Preserve your request configuration by clicking **Save as Endpoint** next to the Send button and giving it a name. This creates a reusable test case for future reference.

## Sending Requests From Saved Endpoints

If you are sending a request from a saved endpoint, you need to select the appropriate environment from the environment dropdown in the upper right corner. You can use any of the following options: 

- **Custom Environment**: customize your own environment using a your server base URL;
- **Local Mock**: for testing with simulated responses from your local machine;
-  **Cloud Mock**: use Apidog's dedicated mock server to fetch sample responses based on your response schema.

:::info[]
Learn more about **[Environments](https://docs.apidog.com/environments-variables-in-apidog-577823m0.md)** and how you can create one of your own.
:::


<CardGroup cols={2}>
  <Card title="Next Step" href="https://docs.apidog.com/adding-an-assertion-645440m0.md">
    Add Assertions to Validate Responses
  </Card>
</CardGroup>
