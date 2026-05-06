# Smart Mock

Smart mock automatically generates realistic API responses based on your API specifications without requiring additional configuration. This intelligent mocking system analyzes your schema and produces appropriate test data instantly.

## How Smart Mock Works

Smart mock generates data from three sources, applied in the following priority:

| Priority | Source | Description |
|----------|--------|-------------|
| 1 | **Mock Field** | Custom values or expressions in response spec properties |
| 2 | **Property Name Matching** | Automatic data generation based on property type and name |
| 3 | **JSON Schema** | Type-based defaults constrained by schema rules |

## Automatic Name-Based Mocking

Smart mock's intelligent algorithm matches property names to built-in rules, generating contextually appropriate data based on type and name.

### Built-in Matching Rules

View and manage built-in rules in **Settings** → **General Settings** → **Feature Settings** → **Mock Settings**.

These rules use wildcard or regular expression patterns to match property names:

<Background>
![image.png](https://api.apidog.com/api/v1/projects/544525/resources/343590/image-preview)
</Background>

### Creating Custom Rules

If built-in rules don't meet your needs, create custom matching rules:

<Steps>
  <Step>
    Navigate to **Settings** → **General Settings** → **Feature Settings** → **Mock Settings**
  </Step>
  <Step>
    Click **New** to create a custom rule
  </Step>
  <Step>
    Define condition details and specify the mock expression
  </Step>
</Steps>

Properties matching your custom conditions will generate data according to the specified mock expression.

<Background>
<img src="https://api.apidog.com/api/v1/projects/544525/resources/343593/image-preview" style="width: 640px" />
</Background>

:::info[Default Behavior]
If a property name doesn't match any rule, Smart mock generates a default value based on the property's data type.
:::

## Mock Field Priority

Values specified in the **mock field** of a response property override name-based matching.

You can enter either:
- **Fixed value**: A static value returned every time
- **Faker statement**: A dynamic value expression for varied data

<Background>
<img src="https://api.apidog.com/api/v1/projects/544525/resources/343594/image-preview" style="width: 640px" />
</Background>

## JSON Schema Constraints

All generated mock data respects JSON Schema constraints defined in your API specification.

### Schema Constraint Examples

| Schema Constraint | Example | Result |
|-------------------|---------|--------|
| **String Length** | Property `name` with length 3-5 | Auto-mocked "Richard" becomes "Richa" |
| **Enum Values** | Property `status` with enum ["sold", "pending", "available"] | Returns one of the three values |
| **Number Range** | Integer with min/max boundaries | Generated values stay within range |
| **Array Length** | Array with min/max element count | Generated arrays respect count limits |

:::tip[]
All property settings are reflected in the final mock data, ensuring responses always conform to your JSON schema specifications.
:::

## Localization Support

:::tip[Mock Locales]
Apidog supports customizable mock locales, allowing you to generate dynamic test data in different languages and formats that match your target region or audience. To learn more about configuring mock locales, visit [Mock language (Locales)](https://docs.apidog.com/mock-language-locales-965986m0.md).
:::

