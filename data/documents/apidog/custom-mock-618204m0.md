# Custom Mock

Apidog provides powerful mock customization features that give you fine-grained control over API responses. This document introduces two approaches to customize mock data:

1. **Field-Level Customization**: Control specific fields while using smart mock for others
2. **Full Response Customization**: Define complete mock responses with expectations (fixed, conditional, or dynamic)

## Field-Level Customization

Sometimes you need to define specific values for certain fields while letting Apidog automatically generate the rest. Apidog offers flexible methods for field-level control.

### Setting Custom Field Values

#### 1. Fixed Values

Specify a static value in the endpoint spec's mock field. Apidog will always return this exact value for that field, while using smart mock for unspecified fields.

**Example:**

<Frame>
<Background>
![image.png](https://api.apidog.com/api/v1/projects/544525/resources/353916/image-preview)
</Background>
</Frame>

#### 2. Dynamic Values with Faker.js

Generate realistic random data using Apidog's dynamic values (based on Faker.js). Use the syntax:

```
{{$category.method}}
```

**Common Examples:**

| Expression | Example Result |
|------------|----------------|
| `{{$person.fullName}}` | Rachel Wheeler |
| `{{$internet.email}}` | Arno.Huels33@yahoo.com |
| `{{$commerce.productName}}` | Elegant Plastic Bike |

Select dynamic values directly from the dropdown menu:

<Frame>
<Background>
![image.png](https://api.apidog.com/api/v1/projects/544525/resources/353921/image-preview)
</Background>
</Frame>

#### 3. Parameterized Faker Methods

Pass parameters to dynamic value methods for specialized data generation using Apidog's enhanced Faker.js syntax.

**Examples:**

| Use Case | Expression | Description |
|----------|------------|-------------|
| Integer range | `{{$number.int(min=0,max=10000)}}` | Random integer between 0 and 10,000 |
| Readable phone | `{{$phone.number(style='human')}}` | Human-readable phone format |
| Multiple of N | `{{$number.int(multipleOf=3)}}` | Integer divisible by 3 |
| Array element | `{{$helpers.arrayElement(['red','blue','green'])}}` | Random color from array |
| Date range | `{{$date.between(from='2024-01-01',to='2024-12-31',format='yyyy-MM-dd')}}` | Date between specified range |

:::tip[]
Explore the complete list of modules, methods, and parameters in the [Dynamic Values Modules documentation](https://docs.apidog.com/1938252m0.md).
:::

#### 4. Concatenating Multiple Expressions

Combine static text and multiple dynamic expressions to generate complex field values.

**Example: Full Address Generation**

```
{{$location.streetAddress}}, {{$location.city}}, {{$location.state}}, {{$location.zipCode}}, {{$location.country}}
```

**Sample Output:**
```
8507 Hudson Alley, Rochester, Wisconsin, 96512, United States
```

Each component is dynamically generated, creating unique, realistic addresses for every mock API call.

:::tip[Mock Locales]
Apidog supports customizable mock locales, allowing you to generate dynamic test data in different languages and formats that match your target region or audience. To learn more about configuring mock locales, visit [Mock language (Locales)](https://docs.apidog.com/mock-language-locales-965986m0.md).
:::

## Full Response Customization (Mock Expectations)

For complete control over mock responses, use **mock expectations**. This feature allows you to define fixed, conditional, or dynamic responses.

### Creating Mock Expectations

<Background>
![image.png](https://api.apidog.com/api/v1/projects/544525/resources/352097/image-preview)
</Background>

### Fixed Responses

Return the same data for every request by creating an unconditional expectation.

**Steps:**

<Steps>
  <Step>
    Click **New expectation**
  </Step>
  <Step>
    Add an expectation name and leave conditions blank
    <Background>
<img src="https://api.apidog.com/api/v1/projects/544525/resources/343601/image-preview" style="width: 640px" />
</Background>
  </Step>
  <Step>
    Fill in the response data you want to return, then save
  </Step>
  <Step>
    Copy and use the provided mock URL to access this endpoint
  </Step>
</Steps>

### Conditional Responses

Return different mock data based on request parameters. The mock engine evaluates conditions from top to bottom, returning the first matching expectation.

**Supported Condition Types:**

| Parameter Type | Description |
|----------------|-------------|
| Query parameters | URL query strings |
| Path parameters | Dynamic URL segments |
| Header parameters | HTTP headers |
| Cookie parameters | Cookie values |
| Body parameters | JSON body fields (via JSON path) |

:::info[Condition Behavior]
- Multiple conditions are combined with AND logic (all must match)
- If no conditions match, Apidog falls back to the Mock method priority in **Project Settings** → **Feature Settings** → **Mock Settings**
:::

:::caution[Limitations]
- Body parameters support **JSON only**, not XML
- Parameter conditions cannot use `{{variables}}`
- Request body format must match the API spec (e.g., form-data, JSON)
- IP address conditions can restrict responses to specific IPs
:::

<Background>
<img src="https://api.apidog.com/api/v1/projects/544525/resources/343619/image-preview" style="width: 640px" />
</Background>

### Dynamic Mock Data

Mock expectations support dynamic, randomized data using [Faker.js](https://fakerjs.dev/) and [Nunjucks](https://mozilla.github.io/nunjucks/) template syntax.

**Example:**

```json
{
    "data": [
        {% for i in range(0, 20) %}
        {% if i>1 %},{% endif %}
        {
            "id": {{i}},
            "firstname": "{{$person.firstName}}",
            "lastname": "{{$person.lastName}}"
        }
        {% endfor %}
    ],
    "success": true
}
```

**This generates:**
- Array of 20 user objects (id from 0 to 19)
- Each with randomly generated first and last names
- A constant `"success": true` field

**Syntax Notes:**

| Syntax | Purpose |
|--------|---------|
| `{{$...}}` | Invokes Faker.js for random values |
| `{% for ... %}` | Nunjucks loop structure |
| `{{i}}` | Nunjucks loop variable (not an Apidog variable) |

:::warning[Important Differences]
- **Apidog uses** `{{$person.firstName}}` instead of native Faker.js `faker.person.firstName()`
- Apidog project/environment variables (`{{variable}}`) are **not available** in mock expectations
- Consult [Faker.js](https://fakerjs.dev/) and [Nunjucks](https://mozilla.github.io/nunjucks/) documentation for full syntax
:::

## Advanced Features

### Custom Response Headers

Add custom headers to mock expectations to simulate authentication, pagination, or other API behaviors.

<Background>
<img src="https://api.apidog.com/api/v1/projects/544525/resources/343623/image-preview" style="width: 640px" />
</Background>

### Advanced Response Properties

Configure additional response properties in the **More** tab:

| Property | Purpose | Default |
|----------|---------|---------|
| **HTTP Status Code** | Simulate errors or special cases | 200 |
| **Response Delay** | Simulate network latency (milliseconds) | 0 |

<Background>
<img src="https://api.apidog.com/api/v1/projects/544525/resources/343624/image-preview" style="width: 640px" />
</Background>

### Enable/Disable Expectations

Toggle expectations on or off independently for local and cloud mock environments from the expectation list.

## Summary

Apidog's custom mock features provide:
- **Flexible field customization** with fixed or dynamic values
- **Full response control** through mock expectations
- **Conditional logic** for parameter-based responses
- **Dynamic data generation** using Faker.js and Nunjucks
- **Advanced simulation** with custom headers, delays, and status codes

These features enable you to create robust, high-fidelity API simulations that accurately mirror production behavior!

