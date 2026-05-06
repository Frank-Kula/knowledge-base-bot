# Publishing Documentation Sites

Publishing a documentation site creates a permanent, fully customized home for your API documentation—distinct from the Quick Share feature, which is designed for temporary collaboration. While Quick Share generates shareable links for rapid internal and external communication, Publish Docs Sites provides comprehensive customization options including custom domains, branded design, navigation control, and advanced features. This makes it ideal for creating professional, public-facing API documentation that represents your brand.

## Prerequisites

Before publishing a documentation site, ensure you have:

- An Apidog account with a project containing API documentation
- Admin permissions for the project
- (Optional) A custom domain if you plan to use branded URLs

## Preliminary Configurations
### Publishing Your Documentation Site

To publish your documentation site, navigate to the Publish Docs module and click on the default main site, then click the `Publish` button.

<Background>
![image.png](https://api.apidog.com/api/v1/projects/544525/resources/371195/image-preview)
</Background>

### Documentation Site Visibility Settings

:::info[Version Requirement]
Apidog version must be ≥ 2.7.15 to access these visibility features.
:::

After clicking the `Publish` button, you can control the visibility of your published documentation site based on your security and access requirements. Click the `Publish right now` button to make your site live with your chosen visibility settings.

<Background>
![image.png](https://api.apidog.com/api/v1/projects/544525/resources/364847/image-preview)
</Background>


<AccordionGroup>
  <Accordion title="Public" defaultOpen>
    
Your doc sites will be accessible to all internet users. You can also choose to publish your API documentation on [API Hub](https://apidog.com/apihub/), a platform operated by Apidog that helps users discover and explore APIs.
  </Accordion>
  <Accordion title="Password protected">
   
If you prefer to secure your API documentations with passwords, enable`Password protected`and set a password — either by creating your own or generating a random one.

  </Accordion>
  <Accordion title="IP Allowlist">

Restrict access to your doc site to only the specific IP addresses or ranges that you configure.
  </Accordion>
    
    <Accordion title="Email Allowlist">
Only the emails on your configured email allowlist can access your doc sites by verifying their emails through verification codes. The email allowlist supports wildcards, making it easier to manage access for enterprise emails.
  </Accordion>
    
    <Accordion title="Custom Login Page">
    If you want users to authenticate through your own login system before accessing the online documentation site, you can enable the **Custom Login Page** feature. Navigate to the [Custom Login Page](https://docs.apidog.com/custom-login-page-1951815m0.md) for detailed instructions.
  </Accordion>
</AccordionGroup>



### Publishing Scope

By default, the scope for publishing documentation is set to all`Shared`resources. You can configure this in the`APIs`. For more details, please refer to [visibility settings](https://docs.apidog.com/visibility-settings-662939m0.md). 

## Advanced Configurations

### Try It
You can enable the **Try It** feature for your documentation pages, so that users can directly make API requests on the documentation page itself.
<Background>
![image.png](https://api.apidog.com/api/v1/projects/544525/resources/371313/image-preview)
</Background>

### Release Versions

You can create and publish multiple versions of your API documentation. [Learn more about publishing API versions.](https://docs.apidog.com/publishing-api-versions-645643m0.md)

<Background>
![release settings for API Documentations.jpg](https://api.apidog.com/api/v1/projects/544525/resources/349504/image-preview)
</Background>


:::tip[Related Resources]
- [How Can Document Users Modify the Base URL in Shared Docs?](https://docs.apidog.com/how-can-document-users-modify-the-base-url-in-shared-docs-984469m0.md)
- [How to Share Headers (e.g., Token) in Apidog Online Docs?](https://docs.apidog.com/how-to-share-headers-e-g-token-in-apidog-online-docs-1291962m0.md)
:::

### Domain Settings

- **Apidog provided domain**: Your document will have a default Apidog Subdomain, such as `https://vhh2uhkjv7.apidog.io`. You can also modify it manually. All Apidog documents use the `apidog.io` domain.

- **Custom Domain**: You can bind the Apidog document to your own domain. Learn more about [Custom domain](https://docs.apidog.com/custom-domain-631339m0.md).

<Background>
![domain settings for API documentations.jpg](https://api.apidog.com/api/v1/projects/544525/resources/349505/image-preview)
</Background>

### Visual Customization

You can customize appearance and layouts for API documentations.

<Background>
![image.png](https://api.apidog.com/api/v1/projects/544525/resources/364852/image-preview)
</Background>


You can preview your document in real time here and save it once you're satisfied with the result.

<Background>
![Apidog-01.gif](https://api.apidog.com/api/v1/projects/544525/resources/364853/image-preview)
</Background>


<Tabs>
<Tab title="Appearance">
Under Appearance Settings, you can configure various basic options for your API documentation, including **Title**, **Logo**, and **Favicon**.
<Background>
![image.png](https://api.apidog.com/api/v1/projects/544525/resources/364857/image-preview)
</Background>

Under **Display content**, you can customize which fields to display in API documentation, including: **Base URL**, **Maintainer**, and **Last Modified Time**.

<Background>
![image.png](https://api.apidog.com/api/v1/projects/544525/resources/371196/image-preview)
</Background>
</Tab>
<Tab title="Layout & Navigation">
You can customize the page layout with ease. Learn more about [Custom layouts](https://docs.apidog.com/custom-layouts-631390m0.md).

<Background>
![image.png](https://api.apidog.com/api/v1/projects/544525/resources/364859/image-preview)
</Background>
</Tab>
<Tab title="Custom Landing Page">
You can customize the homepage of your publish docs using either Markdown or HTML with CSS and JavaScript.

<Background>
![image.png](https://api.apidog.com/api/v1/projects/544525/resources/364862/image-preview)
</Background>
</Tab>
<Tab title="Custom CSS, JavaScript, and HTML">
You can configure global CSS, JavaScript, and footer HTML. For more details, see the [Custom CSS, JavaScript, HTML documentation](https://docs.apidog.com/custom-css-javascript-html-1275828m0.md).

<Background>
![image.png](https://api.apidog.com/api/v1/projects/544525/resources/364863/image-preview)
</Background>
</Tab>
</Tabs>

## SEO Settings

| Setting | Description |
| --- | --- |
| Global Metadata | Configures the default metadata for the entire site. |
| Robots File | The `robots.txt` file instructs search engines on which pages to crawl and display in search results. |
| Sitemap File | The `sitemap.xml` file provides search engines with a comprehensive list of all pages on your site for better indexing. |
| Docs Redirect Rules | Redirects users to the correct documentation page when a URL changes, preventing broken links. |
| URL & Slug Rules | Defines the URL structure and slug format for your documentation pages. |


## Advanced Settings

| Feature | Description |
| --- | --- |
| [Documentation Search](https://docs.apidog.com/documentation-search-746862m0.md) | Integrates with Algolia to provide enhanced search capabilities for your published API documentation. The **[Ask AI](https://docs.apidog.com/documentation-search-746862m0.md#ask-ai)** feature unlocks conversational, AI-powered Q&A directly within your documentation search.|
| [CORS Proxy](https://docs.apidog.com/cors-proxy-780225m0.md) | Specifies a CORS proxy to prevent cross-origin issues that can arise from browser security restrictions. |
| [Google Analytics](https://docs.apidog.com/integrating-google-analytics-787035m0.md) | Enables integration with Google Analytics to track and analyze traffic to your documentation site. |
| Publish to API Hub | Publishes your documentation to the [API Hub](https://apidog.com/apihub ), an open platform for sharing and discovering APIs. |
| Description | Sets the description that will be displayed on the API Hub if the project is published there. |
| Allow 'Export', 'Clone' Data | Permits users to export or clone the documentation data from the main branch. |


### Publish Multiple Docs Sites

To publish docs across different channels within the same project, you can create additional docs sites during publishing. For easier management, you can duplicate the main site’s configuration for each new site. Each sub-site can also have a unique custom domain name.

<Background>
![publishing-docs-sites-introduction-05.png](https://api.apidog.com/api/v1/projects/544525/resources/347928/image-preview)
</Background>

Only subsites let you set the visibility scope for published docs, allowing you to choose which resources are publicly accessible.

<Background>
![publishing-docs-sites-introduction-06.png](https://api.apidog.com/api/v1/projects/544525/resources/347929/image-preview)
</Background>

