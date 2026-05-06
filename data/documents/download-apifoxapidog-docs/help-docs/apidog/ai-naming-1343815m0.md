# AI naming

:::tip[About AI features]
- You need to manually [enable the AI feature](https://docs.apidog.com/enable-ai-features-1225685m0) to access AI-related functionalities (available in version 2.7.37 and above).
- Please note that you need to [add your own AI model key (Claude, OpenAI, Gemini, etc.)](https://docs.apidog.com/enable-ai-features-1225685m0#configure-model-providers) to utilize Apidog's AI capabilities. Apidog's AI functions are **FREE** and do not provide a native AI model; they will only use your own AI model to process your data.
:::

AI can generate standardized, professional, and easy-to-read field names based on your description of a specific field in the current API documentation, in accordance with the [APl design guidelines](https://docs.apidog.com/apl-design-guidelines-1343750m0.md).

You’ll see the AI naming icon next to each field in the:

- API Documentation
- Schemas
- Components

Click the icon to begin the AI naming process.

<Background>
![image.png](https://api.apidog.com/api/v1/projects/544525/resources/359661/image-preview)
</Background>

After clicking the AI naming icon, a prompt will appear. Enter a short description of the field to guide the AI to generate a suitable field name. You can also choose a different AI model. If you’ve already filled in the field description, it will automatically be used.

<Background>

![image.png](https://api.apidog.com/api/v1/projects/544525/resources/359677/image-preview)
</Background>

Click `Send` and the AI will generate multiple field names based on the API design guidelines, current document context, and the field description. It will also provide an explanation and rating for each name.

<Background>
![image.png](https://api.apidog.com/api/v1/projects/544525/resources/359664/image-preview)
</Background>

You can select one of the AI-generated field names and click `Adopt` to apply it directly to the documentation.

<Background>
![Generate field names using AI](https://assets.apidog.com/uploads/help/2025/07/28/o9kay-ed.gif)
</Background>
