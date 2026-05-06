# Quick Share

Effective API collaboration requires seamless documentation sharing. Quick Share eliminates the inefficiency of passing around Word or PDF files by providing instant, online documentation links. This feature enables rapid communication between teams, allowing you to share specific API endpoints with collaborators while maintaining control over access, visibility, and expiration.

### Prerequisites

Before creating a Quick Share, ensure you have:

- An Apidog account with access to a project
- API endpoints or documentation to share
- (Optional) Configured environments if you want readers to test endpoints

<Video src="https://www.youtube.com/watch?v=LRkuXCAXh3w"></Video>

## Creating a Quick Share

Switch to the **Publish Docs** module on the left sidebar.
<Background>
![CleanShot 2025-12-29 at 17.18.46@2x.png](https://api.apidog.com/api/v1/projects/544525/resources/369067/image-preview)
</Background>

Click `+New` to create a new Quick Share. A project supports multiple Quick Shares, which can be distributed to different collaborators. All team members can view Quick Shares created by anyone on the team.

<details>
<summary>📷 Visual Reference: New Share Dialog</summary>

<Background>
![image.png](https://api.apidog.com/api/v1/projects/544525/resources/360309/image-preview)
</Background>

</details>

### Configuration Options

In the New Share dialog, you can customize the following options:

- **Title**: The name of this share, only visible within the Apidog team, used for internal identification, not visible in the shared documentation.

- **Environments**: Choose the environments available in the online document. By default, no environment is selected. You can select multiple environments. The selected environments will be visible to readers in the documentation and can be used to send requests when using "Try it out".
:::tip[Cloud Mock Environment]
If you select the Cloud mock environment when creating the documentation, you're providing readers with a simple sandbox environment to test APIs without affecting production systems.
:::
- **Document content**: The document has two optional components: Base URL and Request samples. You can choose whether to display them in the document.
  - **Base URL**: This is the base URL set in the environment. If selected, each interface in the document will show the complete URL; if not selected, the URL in the document will start with "/".
  - **Owners**: Show oweners of this API documentation.
  - **Request samples**:  Whether to display example code for calling requests. See [request samples](#request-samples) for details.
  - Show 'Last Modified' time above endpoint description.
  - Show 'Last Modified' time at the end of the documentation.
 
- **Allow 'Export', 'Clone' Data**: Whether to allow readers to export & clone data in OAS/Markdown/HTML/Apidog format. 

- **Scope to share**: Choose which API endpoints and Markdown to include in this share. You can select by directory or filter and exclude by tag. You can also choose to [share the entire folder](#share-the-entire-folder).

- **Security**: You can set whether a password is required to access this document, and the expiration time of this document. If no expiration time is selected, it never expires.

- **Show API Fields**: You can set whether these fields are displayed in the document. Including: Owners, Update time, OperationId, Original link, Authorization Required.

- **Language**: The language setting here will affect the functional fixed text in the document, such as "Query Params" "Request samples", etc., but will not affect the text written in the API documentation content.

- **CORS Proxy**: You can deploy and configure the CORS proxy server to handle endpoint requests on API documentation. [Learn more](#cors-proxy).

- **Advanced Settings**: Configure options like Hide 'Try it out' Button and Hide 'Powered by Apidog'.

### Request Samples

You can choose whether to display request code samples when creating the share.
**How to customize request samples:**

1. In **Settings** → **Feature settings** → **Endpoint feature settings** → **Endpoint fields**, enable the Request samples field
2. In **Endpoint** → **Edit**, a Request samples module will appear at the end
3. Click **Custom Request Code Samples** to add samples in your preferred languages

<details>
<summary>📷 Visual Reference: Request Samples Configuration</summary>

<Background>
![CleanShot 2025-12-29 at 17.21.25@2x.png](https://api.apidog.com/api/v1/projects/544525/resources/369068/image-preview)
</Background>

</details>

### Share the Entire Folder

Quick Share supports `Share entire folder`, which is ideal for scenarios where you continue adding or removing documents after sharing. When enabled, collaborators automatically access all documentation in the folder without requiring you to adjust sharing settings for each new document. 

In the `Scope to Share` section, select `Manual Selection` to see the `Share entire folder` option. When enabled, collaborators automatically access all documentation in the folder.

<Background>
![sharing-03.png](https://api.apidog.com/api/v1/projects/544525/resources/348448/image-preview)
</Background>

## CORS Proxy Configuration

When sharing API documentation with external users, they may encounter [Cross-Origin Resource Sharing (CORS)](https://en.wikipedia.org/wiki/Cross-origin_resource_sharing) issues when testing endpoints directly in the browser. A CORS proxy solves this by routing requests through a designated proxy agent, bypassing browser CORS restrictions and enabling seamless API testing.

To configure the CORS proxy, click the setting option when creating a new shared documentation. By default, Apidog offers `Cloud Agent` to manage endpoint requests across all shared documentation.

<details>
<summary>📷 Visual Reference: CORS Proxy Settings</summary>

<Background>
![image.png](https://api.apidog.com/api/v1/projects/544525/resources/360310/image-preview)
</Background>

</details>

### CORS Proxy Options

Select the CORS proxy option that best suits your needs:

<details>
<summary>📷 Visual Reference: CORS Proxy Options</summary>

<Background>
![image.png](https://api.apidog.com/api/v1/projects/544525/resources/371190/image-preview)
</Background>

</details>

- **Cloud Proxy**: Uses Apidog's Cloud Agent to handle endpoint requests. Note: Cloud Agent cannot access endpoints on internal networks

- **Browser Extensions**: Uses a browser extension installed in the user's browser. Users without the extension will be prompted to install it before making requests

- **No Proxy**: Requests are sent directly from the user's browser. Ensure your endpoint server is configured to handle CORS properly

- **Self-hosted Request Proxy Agent**: Use a [Self-hosted Request Proxy Agent](https://docs.apidog.com/request-proxy-agent-780303m0.md) deployed within your infrastructure to handle endpoint requests


