# JSONPath

JSONPath is a query language designed to extract information from JSON data structures, similar to how XPath functions for XML. In Apidog, JSONPath is used extensively for extracting values from API responses, validating data, and creating dynamic test assertions.

The version of JSONPath utilized in Apidog is based on [JSONPath Plus](https://github.com/JSONPath-Plus/JSONPath). For more detailed syntax explanations, you can follow the provided link.

:::tip[AI-Powered JSONPath Generator]
If you are not familiar with JSONPath, you can [use this free AI tool to generate expressions](https://app.anakin.ai/apps/21858?r=Mw4DLLke).
:::

## Quick Start

<Steps>
  <Step title="JSON Response Example">
    Suppose we have the following JSON response:
   
      ```json
      {
          "store": {
            "book": [
              { "category": "fiction", "author": "Author A", "title": "Book 1" },
              { "category": "reference", "author": "Author B", "title": "Book 2" },
              { "category": "fiction", "author": "Author C", "title": "Book 3" }
            ]
          }
      }

      ```
  </Step>
  <Step title="Extracting Data">
    To extract the `title` of the first `book` in the array, use this JSONPath expression:
      
     ```json
      $.store.book[0].title
      ```  
This expression returns "Book 1".
      
  </Step>
  <Step title="JSONPath Expression Explained">
    Let's break down the expression `$.store.book[0].title`:
    - `$`: Refers to the root node of the JSON document — essentially the entire structure.
    - `store`: Points to the `store` property, which is an object under the root node.
    - `book`: Accesses the `book` property under the `store` object, which is an array.
    - `[0]`: Selects the first element in the `book` array (indices start at 0).
    - `title`: Retrieves the `title` of the first book in the array.

In summary, the expression navigates from the root, finds the `store` object, accesses the `book` array, selects the first item, and extracts the `title` of that item.
  </Step>
</Steps>

:::info[Important Notes]
- JSONPath indices start from `0`.  
- Strings in JSONPath must use single quotes, for example: `$.store.book[?(@.category=='reference')]`.
:::

## Syntax Overview

### Basic Syntax

| Syntax            | Description                              |
| ----------------- | ---------------------------------------- |
| `$`               | Root node                                |
| `@`               | Current node                             |
| `.node` or `['node']` | Access child nodes                       |
| `[index]`         | Array indexing, supports counting from `0`|
| `[start:end:step]`| Array slicing                            |
| `*`               | Wildcard, matches all child nodes        |
| `..`              | Recursive wildcard, matches all descendants |
| `(<expr>)`        | Dynamic expression                       |
| `?(<boolean expr>)` | Filter condition                         |

### Extended Syntax

| Syntax                         | Description                                                 |
| ------------------------------ | ----------------------------------------------------------- |
| `^`                            | Access the parent of the matching item                                 |
| `~`                            | Get attribute names of the matching item (as an array)                         |
| `@null()`, `@boolean()`, `@number()`, `@string()`, `@array()`, `@object()` | Retrieve basic JSON types                                        |
| `@integer()`                   | Retrieve integer type                                            |
| `@scalar()`                    | Retrieve complex types, accepting `undefined` and non-finite numbers (when querying JavaScript objects) |
| `@other()`                     | Can be used with a user-defined `otherTypeCallback`          |
| `@undefined()`, `@function()`, `@nonFinite()` | Non-JSON types used when querying non-JSON JavaScript objects |
| `@path`, `@parent`, `@property`, `@parentProperty`, `@root` | Shorthand selectors in filters                             |
| `` ` ``                         | Escape remaining sequences                                  |
| `@['...']`, `?@['...']`         | Escape special characters in attribute names within filters |
| `$..`                           | Retrieve all parent components                                    |

## JSONPath Examples

Here are some common JSONPath expressions based on the example JSON data:

### Example JSON Data

```json
{
  "store": {
    "book": [
      {
        "category": "reference",
        "author": "Nigel Rees",
        "title": "Sayings of the Century",
        "price": 8.95
      },
      {
        "category": "fiction",
        "author": "Evelyn Waugh",
        "title": "Sword of Honour",
        "price": 12.99
      },
      {
        "category": "fiction",
        "author": "Herman Melville",
        "title": "Moby Dick",
        "isbn": "0-553-21311-3",
        "price": 8.99
      },
      {
        "category": "fiction",
        "author": "J. R. R. Tolkien",
        "title": "The Lord of the Rings",
        "isbn": "0-395-19395-8",
        "price": 22.99
      }
    ],
    "bicycle": {
      "color": "red",
      "price": 19.95
    }
  }
}
```

### Common Query Examples

| XPath                  | JSONPath                                   | Result                                         |
| ---------------------- | ------------------------------------------ | ---------------------------------------------- |
| `/store/book/author`   | `$.store.book[*].author`                   | Authors of all books                           |
| `//author`             | `$..author`                                | All authors                                    |
| `/store/*`             | `$.store.*`                                | All child nodes under `store`                  |
| `/store//price`        | `$.store..price`                           | All price fields                               |
| `//book[3]`            | `$..book[2]`                               | Third book (0-based index)                     |
| `//book[last()]`       | `$..book[(@.length-1)]` or `$..book[-1:]`  | Last book                                      |
| `//book[position()<3]` | `$..book[:2]` or `$..book[0,1]`           | First two books                                |
| `//book[isbn]`         | `$..book[?(@.isbn)]`                       | Books with an ISBN                             |
| `//book[price<10]`     | `$..book[?(@.price<10)]`                   | Books priced under 10                          |
| `//*`                  | `$..*`                                     | Recursively match all child nodes              |

:::tip[Testing JSONPath Expressions]
You can verify these expressions using a [JSONPath tester](http://jsonpath.com/). *Make sure to select **JSONPath Plus** for validation.*
:::

<Background>
![jsonpath-plus-validation.png](https://api.apidog.com/api/v1/projects/544525/resources/350622/image-preview)
</Background>

## Use Cases in Apidog

JSONPath is particularly useful in Apidog for:

- **Response Validation**: Extract specific values from API responses to verify correctness
- **Dynamic Variables**: Store extracted values for use in subsequent requests
- **Test Assertions**: Create powerful assertions based on response data
- **Data Extraction**: Pull specific fields from complex nested JSON structures

## References

- [JSONPath Plus](https://github.com/JSONPath-Plus/JSONPath)
- [JSONPath - XPath for JSON](https://goessner.net/articles/JsonPath/)
- [Querying JSON with SelectToken](https://www.newtonsoft.com/json/help/html/SelectToken.htm)

