# SEO Settings

Optimize your API documentation's search engine visibility to attract more developers and users. Apidog provides comprehensive SEO features that help your documentation rank higher in search results, making it easier for potential users to discover your APIs.

:::info[Version Requirement]
Apidog version must be ≥ 2.7.15 to access these SEO features.
:::

You can configure SEO settings at two levels based on your needs.

1. **Page-Level SEO Settings**: Configure SEO for individual pages such as endpoint documentation or Markdown files.
2. **Site-wide SEO Settings**: Configure global SEO metadata, robots.txt, sitemap.xml, redirect rules, and URL settings for the entire documentation site.


## Page-Level SEO Settings

Access page-level SEO settings by clicking the `SEO Settings` icon on the right side of any endpoint documentation or Markdown page. 

<Background>
![page-level seo settings.png](https://api.apidog.com/api/v1/projects/544525/resources/356625/image-preview)
</Background>

### Configuration Options

In the SEO settings panel, you can configure:

- **URL Slug:** Define the path for the current page. For example, set it to `find-by-id`, then the final page URL becomes: `https://{your-domain.com}/find-by-id`.
- **Meta Title:** The title of the webpage that will appear in search engine results.
- **Meta Description:** A brief description of the webpage shown in search engine results.
- **Keywords:** Keywords to help improve search engine understanding.
- **Custom Metadata:** Add extra `<meta>` tags in JSON format. Example:

  ```json
  [
    {"name": "robots", "content": "noindex"},
    {"name": "twitter:card", "content": "summary_large_image"}
  ]
  ```
  
  These will render in HTML as:
  
    ```html
    <meta name="robots" content="noindex" />
    <meta name="twitter:card" content="summary_large_image" />
    ```

## Site-wide Level SEO Settings

When publishing online docs sites, go to "**SEO Settings**" to apply site-wide SEO configurations.

<Background>
![CleanShot 2025-12-29 at 17.34.15@2x.png](https://api.apidog.com/api/v1/projects/544525/resources/369076/image-preview)
</Background>

### Global Metadata

This sets default `<meta>` tags for every page in the docs site. You can use built-in variables to generate dynamic content. All pages inherit this configuration unless overridden by page-level seo settings.

<Background>
![global-metadata.png](https://api.apidog.com/api/v1/projects/544525/resources/356631/image-preview)
</Background>


**Configuration Format:**

Please use a valid JSON array, e.g.:

```json
[
  {"property": "og:title", "content": "{{PAGE_TITLE}} - {{SITE_NAME}}"},
  {"property": "og:description", "content": "{{DESCRIPTION}}"},
  {"property": "og:image", "content": "{{SITE_ICON}}"},
  {"name": "twitter:card", "content": "summary_large_image"},
  {"name": "description", "content": "global description information"},
  {"name": "keywords", "content": "global keywords"}
]
```

These will render in HTML as:

```html
<meta property="og:title" content="{{PAGE_TITLE}} - {{SITE_NAME}}" />
<meta property="og:description" content="{{DESCRIPTION}}" />
<meta property="og:image" content="{{SITE_ICON}}" />
<meta name="twitter:card" content="summary_large_image" />
<meta name="description" content="global description information" />
<meta name="keywords" content="global keywords" />

```

**Supported Built-in Variables:**

The following built-in variables are supported and can be used as placeholders in the content field when filled in:

| Variable  | Meaning|
| ----------------- | --------- |
| `{{PAGE_TITLE}}`  | Title of the current page|
| `{{PAGE_URL}}`    | Page's full URL|
| `{{SITE_NAME}}`   | Your documentation site name|
| `{{SITE_ICON}}`   | URL of your site icon   |
| `{{DESCRIPTION}}` | Default page description|
| `{{KEYWORDS}}`    | Default page keywords   |


**Priority:**

:::info[Priority Order]
`Page-Level SEO Settings (endpoint or Markdown page)` **>** `Global Metadata` **>** `System defaults`
:::


### Robots File(robots.txt)

This file controls crawler behavior and is accessible at `https://{your-domain.com}/robots.txt`.


**Default content:**

```xml
User-Agent: *
Allow: /

Sitemap: {{SITEMAP_URL}}
```

`{{SITEMAP_URL}}` is automatically replaced with the actual `sitemap.xml`URL, provided the sitemap feature is enabled. 

If disabled, this line is removed automatically.


**How to prevent pages from being indexed:**

<AccordionGroup>
  <Accordion title="Block the entire site from indexing" defaultOpen>
   Add the following to **Global Metadata**:
    ```json
    {"name": "robots", "content": "noindex"}
    ```
    
    Or prevent search engines from crawling the site by adding the following to the root-level `robots.txt`:
      
    ```js
    User-agent: *
    Disallow: /
    ```
      
<Frame>
<Background>
<img src="https://api.apidog.com/api/v1/projects/544525/resources/366274/image-preview" width="360px" />
</Background>
</Frame>
  </Accordion>
  <Accordion title="Block a single page from indexing" defaultOpen={true}>
    Add the following to the **Custom Metadata** of the specific page:    
    ```json
    {"name": "robots", "content": "noindex"}
    ```
  </Accordion>
</AccordionGroup>


### Sitemap File(sitemap.xml)

When enabled, the system automatically generates a `sitemap.xml` listing all pages on the site to help search engines crawl more effectively. You can access the sitemap via `https://{your-domain.com}/sitemap.xml`.

- Default status: Enabled.

- If disabled, `sitemap.xml` will no longer be available and `Sitemap: {{SITEMAP_URL}}` will also be removed from `robots.txt`.

### Docs Redirect Rules

If you modify published documentation URLs, you can set redirect rules to avoid 404 errors when users visit old URLs.

<Background>
![image.png](https://api.apidog.com/api/v1/projects/544525/resources/369077/image-preview)
</Background>

You can manually add multiple redirect rules to automatically forward users from old URLs to new ones:

<Background>
![image.png](https://api.apidog.com/api/v1/projects/544525/resources/356633/image-preview)
</Background>

### URL & Slug Rules

Click the`project settings`to view the default URL rules for your site pages.

<Background>
![image.png](https://api.apidog.com/api/v1/projects/544525/resources/369078/image-preview)
</Background>

There are two types of URL naming rules, depending on whether a custom slug (URL) is set on the page.

<Background>
![image.png](https://api.apidog.com/api/v1/projects/544525/resources/356635/image-preview)
</Background>

<AccordionGroup>
  <Accordion title="When the URL Slug is set" defaultOpen>
    The system uses the provided slug as the access path:

    ```js
    https://your-domain.com/{slug}
    ```

   For example, if the slug in a Markdown file is `api-overview`, the address will be:

    ```js
    https://your-domain.com/api-overview
    ```
  </Accordion>
  <Accordion title="When the URL Slug is blank">
    
The system auto-generates the URL using one of the following rules:

**Rule 1(default and recommended):**

```js
https://your-domain.com/{slugify(resourceName)}-{resourceKey}
```

- `resourceName`: The resource title (such as the endpoint name or documentation title)

- `slugify(...)`: Converts the title into a URL-friendly format (e.g., spaces become hyphens)

- `resourceKey`: Unique ID

**Example:**

```js
https://docs.apidog.com/5702007m0.md
```

**Rule 2(more concise):**


```js
https://your-domain.com/{resourceKey}
```

This keeps only the unique ID—shorter but lacks semantic context.

**Example:**

```js
https://docs.apidog.com/5702007m0.md
```
  </Accordion>
</AccordionGroup>


Choose the rule that best fits your team’s SEO preferences and documentation workflow.

## Common Metadata Reference


<details> 
<summary> Metadata Reference </summary>

```json
[
  {
    "name": "robots",
    "content": "noindex"
  },
  {
    "name": "charset",
    "content": "UTF-8"
  },
  {
    "name": "viewport",
    "content": "width=device-width, initial-scale=1.0"
  },
  {
    "name": "description",
    "content": "Page description"
  },
  {
    "name": "keywords",
    "content": "keyword1, keyword2, keyword3"
  },
  {
    "name": "author",
    "content": "Author Name"
  },
  {
    "name": "googlebot",
    "content": "index, follow"
  },
  {
    "name": "google",
    "content": "notranslate"
  },
  {
    "name": "google-site-verification",
    "content": "verification_token"
  },
  {
    "name": "generator",
    "content": "Mintlify"
  },
  {
    "name": "theme-color",
    "content": "#000000"
  },
  {
    "name": "color-scheme",
    "content": "light dark"
  },
  {
    "name": "format-detection",
    "content": "telephone=no"
  },
  {
    "name": "referrer",
    "content": "origin"
  },
  {
    "name": "refresh",
    "content": "30"
  },
  {
    "name": "rating",
    "content": "general"
  },
  {
    "name": "revisit-after",
    "content": "7 days"
  },
  {
    "name": "language",
    "content": "en"
  },
  {
    "name": "copyright",
    "content": "Copyright 2024"
  },
  {
    "name": "reply-to",
    "content": "email@example.com"
  },
  {
    "name": "distribution",
    "content": "global"
  },
  {
    "name": "coverage",
    "content": "Worldwide"
  },
  {
    "name": "category",
    "content": "Technology"
  },
  {
    "name": "target",
    "content": "all"
  },
  {
    "name": "HandheldFriendly",
    "content": "True"
  },
  {
    "name": "MobileOptimized",
    "content": "320"
  },
  {
    "name": "apple-mobile-web-app-capable",
    "content": "yes"
  },
  {
    "name": "apple-mobile-web-app-status-bar-style",
    "content": "black"
  },
  {
    "name": "apple-mobile-web-app-title",
    "content": "App Title"
  },
  {
    "name": "application-name",
    "content": "App Name"
  },
  {
    "name": "msapplication-TileColor",
    "content": "#000000"
  },
  {
    "name": "msapplication-TileImage",
    "content": "path/to/tile.png"
  },
  {
    "name": "msapplication-config",
    "content": "path/to/browserconfig.xml"
  },
  {
    "name": "og:title",
    "content": "Open Graph Title"
  },
  {
    "name": "og:type",
    "content": "website"
  },
  {
    "name": "og:url",
    "content": "https://example.com"
  },
  {
    "name": "og:image",
    "content": "https://example.com/image.jpg"
  },
  {
    "name": "og:description",
    "content": "Open Graph Description"
  },
  {
    "name": "og:site_name",
    "content": "Site Name"
  },
  {
    "name": "og:locale",
    "content": "en_US"
  },
  {
    "name": "og:video",
    "content": "https://example.com/video.mp4"
  },
  {
    "name": "og:audio",
    "content": "https://example.com/audio.mp3"
  },
  {
    "name": "twitter:card",
    "content": "summary"
  },
  {
    "name": "twitter:site",
    "content": "@username"
  },
  {
    "name": "twitter:creator",
    "content": "@username"
  },
  {
    "name": "twitter:title",
    "content": "Twitter Title"
  },
  {
    "name": "twitter:description",
    "content": "Twitter Description"
  },
  {
    "name": "twitter:image",
    "content": "https://example.com/image.jpg"
  },
  {
    "name": "twitter:image:alt",
    "content": "Image Description"
  },
  {
    "name": "twitter:player",
    "content": "https://example.com/player"
  },
  {
    "name": "twitter:player:width",
    "content": "480"
  },
  {
    "name": "twitter:player:height",
    "content": "480"
  },
  {
    "name": "twitter:app:name:iphone",
    "content": "App Name"
  },
  {
    "name": "twitter:app:id:iphone",
    "content": "12345"
  },
  {
    "name": "twitter:app:url:iphone",
    "content": "app://"
  },
  {
    "name": "article:published_time",
    "content": "2024-01-01T00:00:00+00:00"
  },
  {
    "name": "article:modified_time",
    "content": "2024-01-02T00:00:00+00:00"
  },
  {
    "name": "article:expiration_time",
    "content": "2024-12-31T00:00:00+00:00"
  },
  {
    "name": "article:author",
    "content": "Author Name"
  },
  {
    "name": "article:section",
    "content": "Technology"
  },
  {
    "name": "article:tag",
    "content": "tag1, tag2, tag3"
  },
  {
    "name": "book:author",
    "content": "Author Name"
  },
  {
    "name": "book:isbn",
    "content": "1234567890"
  },
  {
    "name": "book:release_date",
    "content": "2024-01-01"
  },
  {
    "name": "book:tag",
    "content": "tag1, tag2, tag3"
  },
  {
    "name": "profile:first_name",
    "content": "John"
  },
  {
    "name": "profile:last_name",
    "content": "Doe"
  },
  {
    "name": "profile:username",
    "content": "johndoe"
  },
  {
    "name": "profile:gender",
    "content": "male"
  },
  {
    "name": "music:duration",
    "content": "205"
  },
  {
    "name": "music:album",
    "content": "Album Name"
  },
  {
    "name": "music:album:disc",
    "content": "1"
  },
  {
    "name": "music:album:track",
    "content": "1"
  },
  {
    "name": "music:musician",
    "content": "Artist Name"
  },
  {
    "name": "music:song",
    "content": "Song Name"
  },
  {
    "name": "music:song:disc",
    "content": "1"
  },
  {
    "name": "music:song:track",
    "content": "1"
  },
  {
    "name": "video:actor",
    "content": "Actor Name"
  },
  {
    "name": "video:actor:role",
    "content": "Role Name"
  },
  {
    "name": "video:director",
    "content": "Director Name"
  },
  {
    "name": "video:writer",
    "content": "Writer Name"
  },
  {
    "name": "video:duration",
    "content": "120"
  },
  {
    "name": "video:release_date",
    "content": "2024-01-01"
  },
  {
    "name": "video:tag",
    "content": "tag1, tag2, tag3"
  },
  {
    "name": "video:series",
    "content": "Series Name"
  }
]
```
</details>
