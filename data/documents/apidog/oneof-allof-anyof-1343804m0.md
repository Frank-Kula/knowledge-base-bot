# OneOf, AllOf, AnyOf

`oneOf`, `anyOf`, and `allOf` are keywords in the JSON Schema specification used to define composite data structures. They are essentially logical operators applied to data validation. Apidog fully supports these JSON Schema features, helping you build more accurate API documentation and data validation rules.

## Basic Concepts

<AccordionGroup>
  <Accordion title="allOf" defaultOpen>
`allOf` means that data must **simultaneously satisfy** all subschema conditions, equivalent to the **AND** operation in logical operations. Like the expression "both... and..." in everyday language, all conditions must be met simultaneously for validation to pass.
  </Accordion>
  <Accordion title="anyOf">
`anyOf` means that data must **satisfy at least one** subschema condition, and can satisfy multiple simultaneously. This is equivalent to the **OR** operation in logical operations. Like the expression "either... or... or both" in everyday language, validation passes as long as one or more conditions are satisfied.
  </Accordion>
  <Accordion title="oneOf">
`oneOf` means that data must **satisfy exactly one** subschema condition - it cannot satisfy multiple conditions simultaneously, nor can it satisfy none at all. This is equivalent to the **XOR (exclusive or)** operation in logical operations. Like "either one or the other" in everyday language, exactly one condition must be chosen and satisfied.
  </Accordion>
</AccordionGroup>

## Logic Comparison Table

| Keyword | Logic Operation | Condition Requirement | Typical Use Case |
|---------|----------------|----------------------|------------------|
| `allOf` | AND | Must satisfy all conditions simultaneously | Inheritance, extension |
| `anyOf` | OR | Must satisfy at least one condition | Optional combinations |  
| `oneOf` | XOR | Must satisfy exactly one condition | Mutually exclusive choices |

## Usage in Apidog

### 1. Using the Visual Editor

<Steps>
  <Step title="Step 1: Create Data Schemas">
    In your project, click **"Schemas"**, then **"New Schema"**.
      
<Background>
![Creating a new schema](https://api.apidog.com/api/v1/projects/544525/resources/359640/image-preview)
</Background>
  </Step>
  <Step title="Step 2: Add Schema Composition">
    In the data schema editing panel, when selecting the type, click **"Schema Composition"** and choose `oneOf`, `anyOf`, or `allOf`. Define specific data structures for each subschema.
      
<Background>
![Adding schema composition](https://api.apidog.com/api/v1/projects/544525/resources/359641/image-preview)
</Background>
  </Step>
</Steps>

### 2. Using JSON Schema Code Editor

You can also directly edit JSON Schema code in the data schema editing panel to define these logical composition patterns.

<Background>
![JSON Schema code editor](https://api.apidog.com/api/v1/projects/544525/resources/359642/image-preview)
</Background>

## Application in API Documentation

### Request Parameter Definition

When defining endpoint request parameters, you can use these composition patterns to describe complex parameter structures:

<Steps>
  <Step>
    Enter the API editing page.
  </Step>
  <Step>
    In the **"Request Parameters"** section, select Body and choose JSON type.
  </Step>
  <Step>
    In the data structure, click **"Reference Schema"**, or select the appropriate **"Schema Composition"** based on business logic, or define custom JSON Schema.
     
<Background>
![Request parameter schema composition](https://api.apidog.com/api/v1/projects/544525/resources/359644/image-preview)
</Background>
  </Step>
</Steps>

### Response Data Definition

Similarly, you can use these schema composition in response data:

<Steps>
  <Step>
    In the **"Response"** section, add response examples.
  </Step>
  <Step>
    Use schema composition to describe different response formats.
      
<Background>
![Response schema composition](https://api.apidog.com/api/v1/projects/544525/resources/359646/image-preview)
</Background>
  </Step>
</Steps>

## Practical Usage Examples

### allOf Example (AND Operation)

Using `allOf` allows you to combine multiple data schemas together, requiring data to satisfy all conditions simultaneously. This is like saying "<span style="color: #999">user information must include basic information</span> **AND** <span style="color: #999">contact information</span>":

```json
{
  "allOf": [
    {
      "description": "Basic user information",
      "type": "object",
      "properties": {
        "id": { "type": "integer" },
        "name": { "type": "string" }
      },
      "required": ["id", "name"]
    },
    {
      "description": "Contact information", 
      "type": "object",
      "properties": {
        "email": { "type": "string", "format": "email" },
        "phone": { "type": "string" }
      },
      "required": ["email"]
    }
  ]
}
```

**Result:** The final data must contain id, name, and email fields, with phone being optional. All constraints from subschemas are merged and executed, as shown below:

<Background>
![allOf example result](https://api.apidog.com/api/v1/projects/544525/resources/359649/image-preview)
</Background>

### anyOf Example (OR Operation)

Using `anyOf` provides multiple optional validation paths - users can choose any one or multiple methods. This is like saying "<span style="color: #999">users can log in through username/password</span> **OR** <span style="color: #999">email/password</span> **OR** <span style="color: #999">phone/verification code</span>":

```json
{
  "type": "object",
  "properties": {
    "login": {
      "anyOf": [
        {
          "description": "Username/password login",
          "properties": {
            "username": { "type": "string" },
            "password": { "type": "string" }
          },
          "required": ["username", "password"]
        },
        {
          "description": "Email/password login",
          "properties": {
            "email": { "type": "string", "format": "email" },
            "password": { "type": "string" }
          },
          "required": ["email", "password"]
        },
        {
          "description": "Phone/verification code login",
          "properties": {
            "phone": { "type": "string" },
            "verifyCode": { "type": "string" }
          },
          "required": ["phone", "verifyCode"]
        }
      ]
    }
  }
}
```

**Result:** Users can provide information for any one or multiple login methods, as long as at least one method satisfies the validation requirements, as shown below:

<Background>
![anyOf example result](https://api.apidog.com/api/v1/projects/544525/resources/359650/image-preview)
</Background>

### oneOf Example (XOR Operation)

Using `oneOf` ensures that users can only choose one payment method and cannot provide multiple methods simultaneously. This is like saying "<span style="color: #999">payment method must be credit card</span> **XOR** <span style="color: #999">PayPal</span> **XOR** <span style="color: #999">bank transfer - exactly one of these options</span>":

```json
{
  "type": "object", 
  "properties": {
    "payment": {
      "oneOf": [
        {
          "description": "Credit card payment",
          "type": "object",
          "properties": {
            "type": { "const": "credit_card" },
            "cardNumber": { "type": "string" },
            "expiryDate": { "type": "string" }
          },
          "required": ["type", "cardNumber", "expiryDate"],
          "additionalProperties": false
        },
        {
          "description": "PayPal payment", 
          "type": "object",
          "properties": {
            "type": { "const": "paypal" },
            "email": { "type": "string", "format": "email" }
          },
          "required": ["type", "email"],
          "additionalProperties": false
        },
        {
          "description": "Bank transfer",
          "type": "object", 
          "properties": {
            "type": { "const": "bank_transfer" },
            "accountNumber": { "type": "string" },
            "routingNumber": { "type": "string" }
          },
          "required": ["type", "accountNumber", "routingNumber"],
          "additionalProperties": false
        }
      ]
    }
  }
}
```

**Result:** Users must choose exactly one payment method - they cannot provide multiple methods simultaneously, nor can they provide none, as shown below:

<Background>
![oneOf example result](https://api.apidog.com/api/v1/projects/544525/resources/359652/image-preview)
</Background>

## Best Practices

When choosing composition patterns, first clarify your business logic:

- Need to **combine/inherit** multiple schemas → Use `allOf` (AND operation)
- Need flexible **optional** combinations → Use `anyOf` (OR operation)  
- Need strict **mutually exclusive** choices → Use `oneOf` (XOR operation)

