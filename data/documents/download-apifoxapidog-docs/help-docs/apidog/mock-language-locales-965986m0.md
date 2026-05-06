# Mock Language (Locales)

Apidog supports multiple languages for dynamic mock data generation through Faker.js locale features. This enables you to generate localized data—such as names, addresses, and phone numbers—that match your target region or culture.

## Default Locale Behavior

By default, Faker follows your project's language setting.

**Configuration:**
- Set your project language in **Project Settings** → **Basic Settings**
- This language serves as the default locale for all dynamically generated mock values

<Background>
![image.png](https://api.apidog.com/api/v1/projects/544525/resources/354049/image-preview)
</Background>

## Customizing Faker Locale

To set the Faker locale independently from your project language:

<Steps>
  <Step>
    Navigate to **Project Settings** → **Feature Settings** → **Mock Settings**
  </Step>
  <Step>
    Select your desired Faker locale from the dropdown
  </Step>
</Steps>

This setting overrides the default project language and generates mock data using the specified locale.

<Background>
![image.png](https://api.apidog.com/api/v1/projects/544525/resources/354050/image-preview)
</Background>

## Field-Level Locale Override

Override the locale for individual fields using the `locale` parameter in mock expressions:

**Syntax:**
```
{{$person.fullName(locale='ja')}}
```

**Example Result:**
```
田中 太郎
```

This flexibility allows you to mix different languages within the same mock response when needed.

**Use Cases:**
- Testing internationalization (i18n) features
- Simulating multi-language user bases
- Generating region-specific test data

## Time Zone Configuration

### Project-Level Time Zone

Set a default time zone for all dynamically generated date and time values:

<Steps>
  <Step>
    Navigate to **Project Settings** → **Feature Settings** → **Mock Settings**
  </Step>
  <Step>
    Select your desired time zone
  </Step>
</Steps>

All generated dates and times use this time zone unless overridden at the field level.

### Field-Level Time Zone Override

Override the time zone for individual date or time fields using the `timeZone` parameter.

**Examples:**

| Use Case | Expression | Sample Output |
|----------|------------|---------------|
| Recent date (Tokyo) | `{{$date.recent(days=1, timeZone='Asia/Tokyo')}}` | `2024-06-13T16:48:12+09:00` |
| Date range (London) | `{{$date.between(from='2024-01-01', to='2024-12-31', timeZone='Europe/London', format='yyyy-MM-dd HH:mm:ss')}}` | `2024-03-15 04:26:52` |

:::tip[]
Field-level time zone parameters provide precise control over date and time data, enabling accurate simulation of any region or time zone in your mock responses.
:::

