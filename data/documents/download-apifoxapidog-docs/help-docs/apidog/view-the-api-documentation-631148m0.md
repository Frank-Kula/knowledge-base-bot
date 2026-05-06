# View the API documentation

Opening the copied URL in a browser will show you Apidog's online API documentation.
Each endpoint is displayed as a page, including several sections:
- Metadata
- Try it out
- Request
- Request samples
- Responses
<Background>
![image.png](https://api.apidog.com/api/v1/projects/544525/resources/344101/image-preview)
</Background>
## Metadata
This section displays various basic information about the endpoint, such as URL, method, modification time, description, etc. You can choose which fields to display when creating the documentation.
- **Endpoint status**
Endpoints with "Released" status won't show a status tag; endpoints with other status (like "Developing") will display a status tag after the endpoint name. Endpoints with "Deprecated" status will be shown as "~~endpoint name~~" in the left directory tree.
<Background>
<p style="text-align: center">
    <img src="https://api.apidog.com/api/v1/projects/544525/resources/344102/image-preview" style="width: 640px" />
</p>
</Background>
- **Endpoint description**
The Markdown in the endpoint description will be displayed at the end of the metadata.

## Try it out
Clicking it will expand the Try it out layer, where you can send requests or modify parameters, and switch the environment for the request. The available environments here are those selected when creating the documentation.

:::tip[]
If you select the Cloud mock environment when creating the documentation, it's equivalent to enabling a simple sandbox environment for the readers of the documentation.
:::

After sending the request, you can see the response and the actual request on the page.
<Background>
<p style="text-align: center">
    <img src="https://api.apidog.com/api/v1/projects/544525/resources/344103/image-preview" style="width: 440px" />
</p>
</Background>
### Use variables
If `{{variables}}` are used in request examples of the spec, when using the "try it out" feature, readers need to first set the values for these variables before they can send the request.
<Background>
<p style="text-align: center">
    <img src="https://api.apidog.com/api/v1/projects/544525/resources/344104/image-preview" style="width: 440px" />
</p>
</Background>
## Request
Parameters and body Specification. Apidog supports two parameter display styles, you can choose Modern or Classic style in **Project Settings** - **feature settings** - **endpoint feature settings**.
<Background>
![image.png](https://api.apidog.com/api/v1/projects/544525/resources/344098/image-preview)
</Background>
## Request samples
Request samples in various languages. You can choose whether to display this module when creating the share.
<Background>
![image.png](https://api.apidog.com/api/v1/projects/544525/resources/344105/image-preview)
</Background>
## Responses
Response spec and Response example, same as in the Apidog client.

## Export
If you selected "Allow exporting data" when creating the documentation, readers will see an Export option in the bottom right corner and at the very bottom of the document.
<p style="text-align: center">
    <img src="https://api.apidog.com/api/v1/projects/544525/resources/344107/image-preview" style="width: 200px" />
</p>
Readers can choose between "Clone" or "Export". "Export" supports exporting in OAS, HTML, Markdown, and Apidog formats.



