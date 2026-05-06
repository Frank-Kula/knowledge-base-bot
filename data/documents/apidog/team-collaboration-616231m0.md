# Team Collaboration

## Multi-User Collaboration & Real-time Sync

The real-time collaboration capability of the API documentation helps improve work efficiency for R&D teams and reduces the cost of repeated communication. The HTTP API and data model modules in the API management support multi-user online real-time collaboration. When others save data, the current page will automatically update changes made by other team members.

<Video src="https://assets.apidog.com/uploads/help/2024/03/07/ef8842b967f932c4c388f3031680b4b3.mp4"></Video>

### Applicable Scenarios

In the following scenarios, the new API documentation will be automatically synced to team members without the need for manual global refresh:

- Modifying and saving an API within the App
- After periodically importing Swagger/OpenAPI files

### Highlights

Apidog's multi-user collaboration features include:

- Real-time display of editor avatars, clearly showing who is editing the same API
- Field-level collaboration, effectively avoiding content conflicts
- If there is a conflict, you'll know during editing so you can resolve it beforehand and continue editing
- Fine-grained conflict resolution, allowing preservation of partial content from both sides
- API documentation has version history and recycle bin, supporting rollback to old versions, no need to worry about accidental modifications
- Automatic import and the IDEA plugin are also part of real-time collaboration, data is automatically updated after import

## Collaboration Links

The "Collaboration Link" feature allows members of the team to quickly locate APIs and collaborate.

:::info
Collaboration links are only used for sharing within the team, and non-team members can't open the collaboration link.
:::

### Copying the Collaboration Link

Tap the **Copy Collaboration Link** button in the menu bar on the right side of the API to create a collaboration link. Send it to other team members, open the link, and you can directly locate the corresponding API in the web terminal.

<details>
<summary>📷 Visual Reference</summary>

<Background>
![](https://assets.apidog.com/uploads/help/2023/07/12/8b2b016d7acd0a2563d57be039899a3c.png)
</Background>

</details>

### Link URL Specification

Apidog links are composed of several key components:

1. **Project ID**
   - Example: https://apidog.com/web/project/{Project-ID}

2. **Specified Endpoint within the Project**
   - Example: https://apidog.com/web/project/{Project-ID}/apis/api-{API-ID}

3. **Specified Tab within an Endpoint**
   - Example: https://apidog.com/web/project/{Project-ID}/apis/api-{API-ID}-run

This URL structure allows users to access specific projects, APIs, and views within the Apidog platform.

## Embedding Parameter Values in URLs

When sharing Apidog endpoints, the default behavior is to only include the API specification without any parameter values. However, if you need to share the document with specific parameter or variable values included, you can embed them directly in the document URL.

### Passing Parameter Values

There are two approaches to embedding parameter values in the URL - the simple mode and the complex mode. The simple mode is more straightforward and does not require URL encoding, but it does not support bracket characters. The complex mode supports all characters but requires encoding the parameter data.

#### Simple Mode

In the simple mode, you can use the format `query[xxx]=yyy` to assign the value `yyy` to the parameter named `xxx`.

Example:
```
https://apidog.com/web/project/406014/apis/api-10061199-run?query[aaa]=yyy&query[bbb]=yyy&path[aaa]=yyy&body[aaa]=yyy&header[aaa]=yyy&cookie[aaa]=yyy&environment[aaa]=yyy
```

| Parameter Type | Parameter Value | Description |
|:---------------|:----------------|:------------|
| Query Parameters | `query[xxx]=yyy` | |
| Path Parameters | `path[xxx]=yyy` | |
| Body Parameters | `body[xxx]=yyy` | For form-data or x-www-urlencoded body types |
| Body Parameters | `body=yyy` | For other body types |
| Header Parameters | `header[xxx]=yyy` | |
| Cookie Parameters | `cookie[xxx]=yyy` | |
| Environment Variables | `environment[xxx]=yyy` | These will be saved to the default environment variables |

#### Complex Mode

The complex mode allows for more advanced parameter embedding by encoding a JSON object. The value of the `params` parameter is obtained by calling `encodeURIComponent` on the following JSON data:

```json
{
    "query": [
        ["id", "value1"], 
        ["id", "value2"], 
        ["key2", "value3"]
    ],
    "path": [
        ["key1", "value1"], 
        ["key2", "value2"]
    ],
    "body": [
        ["aaa", "value1"], 
        ["key2", "value2"]
    ],
    "header": [
        ["testHeader", "value1"], 
        ["key2", "value2"]
    ], 
    "cookie": [
        ["testCookie", "value1"], 
        ["key2", "value2"]
    ], 
    "environment": [
        ["key1", "value1"], 
        ["key2", "value2"]
    ]
}
```

The encoded URL would look like:
```
https://apidog.com/web/project/406014/apis/api-10061199-run?params={ "query"%3A{ "aaa"%3A"xxx"%2C "bbb"%3A"yyy" }%2C "body"%3A{ "aaa"%3A"xxx"%2C "bbb"%3A"yyy" }%2C "cookie"%3A{ "aaa"%3A"xxx"%2C "bbb"%3A"yyy" }%2C "environment"%3A{ "aaa"%3A"xxx"%2C "bbb"%3A"yyy" } }
```

| Parameters Type | Parameters Value | Description |
|:----------------|:-----------------|:------------|
| Query Parameters | `query` | |
| Path Parameters | `path` | |
| Body Parameters | `body` | If the body type is form-data or x-www-urlencoded, the value of body is JSON; otherwise the value of body is a string |
| Header Parameters | `header` | |
| Cookie Parameters | `cookie` | |
| Environment Variables | `environment` | These will be saved to the default environment variables |

### Passing Environment Variables

You can also use the URL to automatically set the user's "environment variables" by passing parameters. To do this, add URL parameters in the format `environment[variable name]=variable value`.

For example:

- https://apidog.com/web/project/406014?environment[aaa]=xxx&environment[bbb]=yyy
- https://apidog.com/web/project/406014/apis/api-10061199-run?environment[aaa]=xxx

## Changing the Opening Method

Collaboration links support opening in both the client and the web side. If you want to locate the API through the client, go to Apidog Web, tap the **Settings** ⚙, and turn on the **Always open collaboration links on desktop** option in **General**.

:::info
This option is only available on Apidog Web but not Apidog Client.
:::

<details>
<summary>📷 Visual Reference</summary>

<Background>
![](https://assets.apidog.com/help/assets/images/team-collaboration-2-46f5fd97c46681a7ea4101c236ede292.png)
</Background>

</details>

The client will be automatically evoked when the collaboration link is accessed.

