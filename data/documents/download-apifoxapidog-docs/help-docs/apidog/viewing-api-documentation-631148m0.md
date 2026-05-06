# Viewing API Documentation

Apidog's published API documentation provides an interactive, comprehensive view of your APIs. When users access your documentation URL, they'll see a well-structured presentation of each endpoint with multiple sections designed for easy understanding and testing.

## Documentation Structure

Each endpoint page includes the following sections:

- **Metadata**: Basic endpoint information
- **Try it out**: Interactive API testing
- **Request**: Parameters and body specifications
- **Request samples**: Code examples in various languages
- **Responses**: Response specifications and examples
<Background>
![image.png](https://api.apidog.com/api/v1/projects/544525/resources/344101/image-preview)
</Background>
## Metadata

This section displays essential endpoint information such as URL, HTTP method, modification time, and description. You can choose which fields to display when creating the documentation.

### Endpoint Status
Endpoints with "Released" status won't show a status tag. Endpoints with other statuses (like "Developing") will display a status tag after the endpoint name. Endpoints with "Deprecated" status appear as "~~endpoint name~~" in the left directory tree.
<Background>
<img src="https://api.apidog.com/api/v1/projects/544525/resources/344102/image-preview" style="width: 640px" />
</Background>
### Endpoint Description

Markdown content in the endpoint description is rendered and displayed at the end of the metadata section.

## Try It Out

Click "Try it out" to expand the interactive testing layer where you can send requests, modify parameters, and switch environments. Available environments are those selected when creating the documentation.

:::tip[Cloud Mock Environment]
If you select the [Cloud mock](https://docs.apidog.com/cloud-mock-621066m0.md) environment when creating the documentation, you're providing readers with a simple sandbox environment for testing APIs.
:::

After sending the request, you can see the response and the actual request on the page.
<Background>
<img src="https://api.apidog.com/api/v1/projects/544525/resources/344103/image-preview" style="width: 440px" />
</Background>
### Using Variables

If `{{variables}}` are used in request examples, readers must set variable values before sending requests.
<Background>
<img src="https://api.apidog.com/api/v1/projects/544525/resources/344104/image-preview" style="width: 440px" />
</Background>


### Using Credentials

You can configure authentication at the API or folder level within your project's Auth settings. Use [security schemes](https://docs.apidog.com/security-scheme-in-apidog-965336m0.md) or define settings manually.

<Background>
![image.png](https://api.apidog.com/api/v1/projects/544525/resources/369069/image-preview)
</Background>

After configuring the authentication settings—for example, using Bearer Token authentication—you will see an "Credentials" section at the top of the "Publish Documentation" panel, where you can directly enter the token value.

<Background>
![image.png](https://api.apidog.com/api/v1/projects/544525/resources/367455/image-preview)
</Background>

The major benefit of this configuration approach is that authentication information can be shared across different APIs. If multiple APIs reference the same security scheme or authentication type, you only need to enter the authentication information once, and other APIs can automatically reuse it.

<Background>
![04-apidog.gif](https://api.apidog.com/api/v1/projects/544525/resources/367457/image-preview)
</Background>

These credentials are encrypted and stored in the browser's LocalStorage, and are managed based on the browser session. Within the same session, they can be shared across multiple windows and tabs. Once the browser is closed and the session ends, these credentials automatically become invalid.

More specifically: the credentials stored in LocalStorage are encrypted, while the decryption key is stored in a session cookie. Although the data in LocalStorage persists long-term, the decryption key in the session cookie expires as soon as the browser is closed. As a result, the encrypted data can no longer be decrypted or accessed, and you'll need to re-enter the credentials the next time you visit.



## Request

This section displays parameters and body specifications. Apidog supports two parameter display styles—Modern or Classic—which you can choose in **Settings** → **Feature Settings** → **Endpoint Feature Settings**.
<Background>
![CleanShot 2025-12-29 at 17.24.55@2x.png](https://api.apidog.com/api/v1/projects/544525/resources/369070/image-preview)
</Background>

## Request Samples

Request code samples in various programming languages. You can choose whether to display this module when creating the share.
<Background>
![image.png](https://api.apidog.com/api/v1/projects/544525/resources/344105/image-preview)
</Background>
## Responses

Response specifications and examples, displayed the same as in the Apidog client.

## Export
If you selected "Allow exporting data" when creating the documentation, readers will see an Export option in the bottom right corner and at the very bottom of the document.
<Background>
![image.png](https://api.apidog.com/api/v1/projects/544525/resources/371192/image-preview)
</Background>



Readers can choose between "Clone" or "Export". "Export" supports exporting in OAS, HTML, Markdown, and Apidog formats.



