# Request History

Apidog automatically saves snapshots of your API requests and responses, making it easy to trace back, review, and resend previous requests. This feature is invaluable for debugging, comparing results over time, and collaborating with team members.

## View API Request History

When you send API requests, the request/response content of the API will be automatically saved as a snapshot on your local machine. You can view these snapshot data in the **History** → **Local** tab, which facilitates tracing back and reinitiating requests.

<Background>
![view-api-request-history-apidog.png](https://api.apidog.com/api/v1/projects/544525/resources/348134/image-preview)
</Background>

You can modify the parameters directly on this request history and click the **Send** button to debug this API again.

<Background>
![sending-request-apidog.png](https://api.apidog.com/api/v1/projects/544525/resources/348133/image-preview)
</Background>

:::tip
**Request History Storage Limits**

- Automatically generated and saved request history is stored on the **Local** tab and is only visible to yourself. If you need to share the results with other team members, you can use the **Share** feature.
- If your API request and response data exceeds 1MB, the request result will not be saved as a request history snapshot. However, you can click **Share** to save this request result to the cloud.
- When requesting on the client, the request history is saved locally with a limit of 500 entries.
- When requesting on the web, the request history is stored in the browser's storage with a limit of 500 entries.
- Request history data is independent between different platforms and devices.
:::

## Sharing Requested Results / Requested History

When you need to synchronize the results of an API request with other team members, such as when you need assistance in reviewing the API request results, you can click the **Share** button in the upper right corner of the returned results to create a sharing link and share this request result with other project members.

<Background>
![create-request-share-apidog.png](https://api.apidog.com/api/v1/projects/544525/resources/348130/image-preview)
</Background>

Other members in the project can access the shared request history by clicking on the generated sharing link. This will allow them to view the shared request results and initiate requesting. Alternatively, project members can manually navigate to the project's **History** → **Shared** section to view all the shared request histories within the project.

<Background>
![see-request-sharing-apidog.png](https://api.apidog.com/api/v1/projects/544525/resources/348131/image-preview)
</Background>

:::info[]
When sharing, the request results and local request history will be uploaded to the cloud for team collaboration purposes. This allows team members to access the exact request and response data you experienced.
:::

