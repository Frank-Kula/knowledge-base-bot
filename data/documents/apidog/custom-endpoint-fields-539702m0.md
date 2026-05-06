# Custom Endpoint Fields

When collaborating on APIs, there may be a need for some custom additional fields to describe endpoints. For example, you could add fields such as "Authorization Required," "Response Format," or "Rate Limiting Policy" to provide more context to users consuming the API.

In Apidog, you can leverage **Customized Fields** to implement these additional fields seamlessly.

## Configuring Custom Fields

You can set up endpoint fields in Apidog by navigating to **Settings** > **General Settings** > **Feature Settings** > **Endpoint Feature Settings**. The customized fields that you configure here will apply project-wide in Apidog.

<Background>
<img src="https://api.apidog.com/api/v1/projects/544525/resources/341136/image-preview" style="width:640px" />
</Background>

Apidog provides three default built-in fields that you can manually enable or disable. If enabled, the field will appear in the endpoint metadata.

<Background>
<img src="https://api.apidog.com/api/v1/projects/544525/resources/341135/image-preview" style="width:640px" />
</Background>

### Adding New Fields

You also have the flexibility to add your custom fields as needed.

<Background>
<img src="https://api.apidog.com/api/v1/projects/544525/resources/341134/image-preview" style="width:440px" />
</Background>

**Supported field types:**

- Text
- Number
- Single select
- Multiple select
- Date
- Team member
- Link
- Email
- Single label
- Multiple label

### Showing Fields in API Documentation

In Quick Share, you have the option to choose whether to display these custom fields.

<Steps>
  <Step>
    When creating a Quick Share in Apidog, you can select the option **"Show API Fields"** to include the API fields you defined.

<Background>
<img src="https://api.apidog.com/api/v1/projects/544525/resources/341142/image-preview" style="width:540px" />
</Background>
  </Step>
  <Step>
    Select fields to be displayed.

<Background>
<img src="https://api.apidog.com/api/v1/projects/544525/resources/341143/image-preview" style="width:540px" />
</Background>     
  </Step>
  <Step>
    They will be displayed in the documentation.
  </Step>
</Steps>

When publishing documentation in Apidog, you can also choose which fields to display. In the **Publish Docs** section, under **Publish Docs Sites** > **Customize** > **Appearance & Display Content**, you have the option to select fields.

<Background>
![Publish docs field selection](https://api.apidog.com/api/v1/projects/544525/resources/369079/image-preview)
</Background>

