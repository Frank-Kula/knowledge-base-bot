# Regular Expressions

Regular expressions (regex) are powerful patterns used for matching and manipulating text. In Apidog, regular expressions are used for data validation, response assertions, dynamic value extraction, and text pattern matching in API testing.

Apidog uses JavaScript-flavored regular expressions, which provide a comprehensive set of features for pattern matching and text processing.

:::info[External Reference]
This page provides a brief introduction to regular expressions. For complete syntax details, examples, and advanced features, refer to the official [Mozilla Developer Network (MDN) documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_Expressions).
:::

## What are Regular Expressions?

Regular expressions are sequences of characters that define search patterns. They are commonly used for:

- **Validating input formats** (email addresses, phone numbers, URLs)
- **Extracting data** from API responses
- **Searching and replacing** text patterns
- **Testing assertions** in automated API tests
- **Parsing** structured text data

## Common Use Cases

### Response Validation

Use regex to validate that API responses match expected patterns:
- Email format: `/^[^\s@]+@[^\s@]+\.[^\s@]+$/`
- UUID format: `/^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$/i`
- Date format (YYYY-MM-DD): `/^\d{4}-\d{2}-\d{2}$/`

### Data Extraction

Extract specific values from response strings using capture groups:
- Extract domain from URL: `/https?:\/\/([^\/]+)/`
- Extract numbers: `/\d+/g`

### Dynamic Values

Generate dynamic test data using regex patterns in mock data generator.

## Learn More

For detailed information about regular expression syntax, special characters, flags, and advanced features, view the [Mozilla Developer Network documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_Expressions).
