# SEO 设置

> Apifox 版本号需 `>=2.7.15` 

Apifox 提供了完善的 SEO 设置功能，帮助你优化 API 文档在搜索引擎中的展示效果，吸引更多访问流量。你可以根据实际需求，在页面级或文档站级配置 SEO 信息。

目前提供两个配置入口：

* **页面级 SEO 设置**：用于设置接口文档、Markdown 文档等单个页面的 SEO 信息。
* **站点级 SEO 设置**：用于统一配置整个文档站的 SEO 元数据（Metadata）、搜索引擎爬虫规则（robots.txt）、站点地图（sitemap.xml）、重定向规则及 URL 设置等。



## 页面级 SEO 设置

你可以在接口文档或 Markdown 文档页面，点击右侧的 **“SEO 设置”** 图标，打开页面级 SEO 设置面板。

<Background>
<img src="https://api.apifox.com/api/v1/projects/5097254/resources/484885/image-preview" />
</Background>

在面板中，你可以设置以下内容：

* **自定义 URL**

  设置当前页面的访问路径，例如设置为 `get-user-info`，最终页面地址将为 `https://{your-domain.com}/get-user-info`。

* **Meta Title**

  页面在搜索引擎中的标题。

* **Meta Description**

  页面在搜索引擎结果中的简要描述。

* **Keywords**

  页面相关关键词，便于搜索引擎理解页面内容。

* **自定义 Metadata**

  以 JSON 格式添加任意 `<meta>` 标签键值对，例如：

  ```json
  [
    {"name": "robots", "content": "noindex"},
    {"name": "twitter:card", "content": "summary_large_image"}
  ]
  ```
  
  在页面最终渲染为 HTML 时，会自动转换为以下 `<meta>` 标签：
  
    ```html
    <meta name="robots" content="noindex" />
    <meta name="twitter:card" content="summary_large_image" />
    ```
    

## 站点级 SEO 设置

在发布在线文档站时，你可以通过 **“SEO 设置”** 模块统一配置文档站的 SEO 策略。


<Background>
  
![CleanShot 2025-06-06 at 17.48.44@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/531938/image-preview)
</Background>


### 全局 Metadata

全局 Metadata 是用于定义整站通用 `<meta>` 标签的配置方式，支持使用内置变量进行动态渲染，所有页面将继承该配置（但可以被页面级配置覆盖）。


<Background>

![CleanShot 2025-06-05 at 17.27.49@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/531467/image-preview)
</Background>


**配置格式：**

请使用合法的 JSON 数组格式。例如：


```json
[
  {"property": "og:title", "content": "{{PAGE_TITLE}} - {{SITE_NAME}}"},
  {"property": "og:description", "content": "{{DESCRIPTION}}"},
  {"property": "og:image", "content": "{{SITE_ICON}}"},
  {"name": "twitter:card", "content": "summary_large_image"},
  {"name": "description", "content": "全局描述信息"},
  {"name": "keywords", "content": "全局关键词"}
]
```

上述配置在页面中最终渲染为 HTML 时，会自动转为标准的 `<meta>` 标签，，例如：


```html
<meta property="og:title" content="页面标题 - 站点名称" />
<meta property="og:description" content="页面描述" />
<meta property="og:image" content="站点图标 URL" />
<meta name="twitter:card" content="summary_large_image" />
<meta name="description" content="全局描述信息" />
<meta name="keywords" content="全局关键词" />

```

**支持的内置变量：**

支持以下内置变量，填写时可作为内容字段中的占位符：

| 变量名               | 含义        |
| ----------------- | --------- |
| `{{PAGE_TITLE}}`  | 页面标题      |
| `{{PAGE_URL}}`    | 页面 URL 地址 |
| `{{SITE_NAME}}`   | 站点名称      |
| `{{SITE_ICON}}`   | 站点图标地址    |
| `{{DESCRIPTION}}` | 默认页面描述    |
| `{{KEYWORDS}}`    | 默认页面关键词   |


**优先级说明：**


:::info[]
`页面级配置（接口或 Markdown 页面）` **>** `全局 Metadata` **>** `系统默认值`
:::


### Robots 文件（robots.txt）

该文件用于规范搜索引擎爬虫的访问行为，启用后可通过 `https://{your-domain.com}/robots.txt` 访问。


**默认生成内容：**

```xml
User-Agent: *
Allow: /

Sitemap: {{SITEMAP_URL}}
```

`{{SITEMAP_URL}}` 变量会自动替换为当前文档站的 `sitemap.xml` 地址（前提是 sitemap 功能开启）。

若关闭 sitemap 功能，系统将自动移除该行的最终输出。


**阻止页面被索引的方法（禁止搜索引擎收录）：**


<AccordionGroup>
  <Accordion title="阻止整个文档站被索引" defaultOpen>
    在「全局 Metadata」中添加：
    ```json
    {"name": "robots", "content": "noindex"}
    ```
    或在站点根目录的 `robots.txt` 中禁止搜索引擎抓取：
    
    ```js
    User-agent: *
    Disallow: /
    ```
    
<Frame>
<img src="https://api.apifox.com/api/v1/projects/5097254/resources/595769/image-preview" width="360px" />
</Frame>

  </Accordion>
  <Accordion title="阻止单个页面被索引" defaultOpen={true}>
    在对应页面的「自定义 Metadata」中添加相同内容：

    ```json
    {"name": "robots", "content": "noindex"}
    ```
  </Accordion>
</AccordionGroup>




### Sitemap 文件（sitemap.xml）

启用后，系统将自动生成 `sitemap.xml` 文件（站点地图），列出站点下所有页面的索引，方便搜索引擎更高效地抓取站点内容，文件可通过 `https://{your-domain.com}/sitemap.xml` 访问。

- 默认状态：已启用。

- 若关闭，将不再提供 `sitemap.xml` 文件，同时 `robots.txt` 输出中会自动去除 `Sitemap: {{SITEMAP_URL}}` 所在行。


### 文档重定向规则

如果你需要对已发布文档的 URL 进行修改，可通过设置重定向规则，避免用户访问旧地址时报错。

<Background>

![CleanShot 2025-06-06 at 14.42.33@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/531775/image-preview)
</Background>

你可以手动添加多个重定向规则，系统会将访问旧 URL 的用户自动跳转到新 URL：

<Background>
<img src="https://api.apifox.com/api/v1/projects/5097254/resources/484900/image-preview" />
</Background>



### URL 和 Slug 规则

点击 “项目设置” 可跳转查看当前站点页面的默认 URL 命名规则。

<Background>
![CleanShot 2025-06-06 at 14.43.13@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/531777/image-preview)
</Background>

URL 命名规则有两种，根据是否在页面中设置了自定义 Slug（URL）而有所不同：


<Background>
<img src="https://api.apifox.com/api/v1/projects/5097254/resources/484896/image-preview" />
</Background>


<AccordionGroup>
  <Accordion title="当设置了自定义 URL（Slug）时" defaultOpen>
    系统将直接使用你填写的 Slug 作为访问路径。

    ```js
    https://your-domain.com/{slug}
    ```

    例如：你在某个 Markdown 文档中填写了 Slug 为 `api-overview`，那它的地址将是：

    ```js
    https://your-domain.com/api-overview
    ```
  </Accordion>
  <Accordion title="当没有设置自定义 URL（Slug）时">
    
系统将按照预设规则自动生成 URL，可选规则如下：

**规则一（默认推荐）:**

```js
https://your-domain.com/{slugify(resourceName)}-{resourceKey}
```

- `resourceName`：资源标题（如接口名称、文档标题）

- `slugify(...)`：将标题转为 URL 友好的形式（例如空格转为连字符）

- `resourceKey`：唯一标识 ID

**示例：**

```js
https://docs.apifox.com/SEO-设置-5702007m0
```

**规则二（更简洁）:**


```js
https://your-domain.com/{resourceKey}
```

仅保留唯一 ID，更简短但不具备语义信息。

**示例：**

```js
https://docs.apifox.com/5702007m0
```
  </Accordion>
</AccordionGroup>


你可以根据团队的 SEO 习惯或文档管理方式选择适合的默认规则。

## 常用 Metadata 参考


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
