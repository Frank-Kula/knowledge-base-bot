# How to share APIs to collaborators in Apidog?

In API development, communication, and collaboration, API documentation is logically the standard, but in practice, there is the problem of passing around files in Word or PDF formats. For this reason, **online document** is advocated to improve the efficiency of communication between teams.

## Create a quick share

Switch to **Share Docs** module on the left side.

![](https://assets.apidog.com/uploads/help/2023/09/04/38afef894f87f5bbe7cc41579290c783.png)

Click "New" to create a new Quick share. A project supports multiple different Quick shares, which can be distributed to different collaborators. Every team member can see all Quick shares created by everyone.
<p style="text-align: center">
    <img src="https://api.apidog.com/api/v1/projects/544525/resources/344051/image-preview" style="width: 440px" />
</p>

In the New Share popup, you can customize the following options:

- **Title**: The name of this share, only visible within the Apidog team, used for internal identification, not visible in the shared documentation.

- **Environments**: Choose the environments available in the online document. By default, no environment is selected. You can select multiple environments. The selected environments will be visible to readers in the documentation and can be used to send requests when using "Try it out".
:::tip[]
If you select the Cloud mock environment when creating the documentation, it's equivalent to enabling a simple sandbox environment for the readers of the documentation.
:::
- **Document content**: The document has two optional components: Base URL and Request samples. You can choose whether to display them in the document.
  - **Base URL**: This is the base URL set in the environment. If selected, each interface in the document will show the complete URL; if not selected, the URL in the document will start with "/".
  - **Request samples**:  Whether to display example code for calling requests. See [Request Samples](#request-samples) for details.

- **Allow exporting data**: Whether to allow readers to export data in OAS/Markdown/HTML/Apidog format. 

- **Scope to share**: Choose which API endpoints and Markdown to include in this share. You can select by directory or filter and exclude by tag.

- **Security**: You can set whether a password is required to access this document, and the expiration time of this document. If no expiration time is selected, it never expires.

- **Show API Fields**: You can set whether these fields are displayed in the document. Including: Owners, Update time, OperationId, Original link, Authorization Required.

- **Language**: The language setting here will affect the functional fixed text in the document, such as "Query Params" "Request samples", etc., but will not affect the text written in the API documentation content.

- **Advanced settings**: You can set Hide 'Try it out' Button and Hide 'Powered by Apidog' here.

### Share entire folder

Quick share supports "share entire folder". This is suitable for scenarios where, after sharing the link, you may have added or removed documents in the folder, and you want collaborators to be able to see these changes synchronously. 

In the "Scope to share", when you select "Manual selection", you can see "share entire folder". If enabled, collaborators will always see all documents in the folder, without you needing to manually modify the sharing scope after adding documents.

<p style="text-align: center">
    <img src="https://api.apidog.com/api/v1/projects/544525/resources/344093/image-preview" style="width: 440px" />
</p>

### Request samples
You can choose whether to display this module when creating the share.
You can customize Request samples. Here's how:
1. In **Project settings** - **Feature settings** - **Endpoint feature settings** - **Endpoint fields**, enable the Request samples field.
2. Then in **Endpoint** - **Edit**, a Request samples module will appear at the end.
3. You can click **Add request sample** here to add samples in the languages you need. Then it will appear in the documentation.

![image.png](https://api.apidog.com/api/v1/projects/544525/resources/344099/image-preview)

## Share the link

After the setting is complete, copy the link to share with team members.

![](https://assets.apidog.com/uploads/help/2023/07/11/cc0b9a9eb05ee500489b03aa51e15ee9.png)

Visit the link to [View the API documentation](https://docs.apidog.com/viewing-api-documentation-631148m0.md).

