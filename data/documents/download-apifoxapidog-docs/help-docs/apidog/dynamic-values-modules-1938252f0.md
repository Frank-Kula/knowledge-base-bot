# Dynamic values Modules

Apidog Dynamic Values leverages [Faker.js v9.0.0-rc.1](https://v9.fakerjs.dev/) to deliver deterministic, locale-aware test data that can be generated once and reused across requests, eliminating scripting overhead while preserving full compatibility with existing Faker expressions.

## Comprehensive Dynamic Value Library

For easy reference, Apidog provides documentation with examples for each dynamic value category, mirroring the structure of Faker.js:

- [Airline](https://docs.apidog.com/airline-645409m0.md)
- [Animal](https://docs.apidog.com/645417m0.md)
- [Color](https://docs.apidog.com/645425m0.md)
- [Commerce](https://docs.apidog.com/646336m0.md)
- [Company](https://docs.apidog.com/company-646345m0.md)
- [Database](https://docs.apidog.com/646350m0.md)
- [Datatype](https://docs.apidog.com/datatype-646355m0.md)
- [Date](https://docs.apidog.com/647552m0.md)
- [Finance](https://docs.apidog.com/finance-647562m0.md)
- [Food](https://docs.apidog.com/food-647645m0.md)
- [Git](https://docs.apidog.com/647573m0.md)
- [Hacker](https://docs.apidog.com/647580m0.md)
- [Helpers](https://docs.apidog.com/helpers-647667m0.md)
- [Image](https://docs.apidog.com/647682m0.md)
- [Internet](https://docs.apidog.com/internet-647754m0.md)
- [Location](https://docs.apidog.com/location-647839m0.md)
- [Lorem](https://docs.apidog.com/649396m0.md)
- [Music](https://docs.apidog.com/649435m0.md)
- [Number](https://docs.apidog.com/number-649453m0.md)
- [Person](https://docs.apidog.com/649475m0.md)
- [Phone](https://docs.apidog.com/phone-649511m0.md)
- [Science](https://docs.apidog.com/649524m0.md)
- [String](https://docs.apidog.com/string-649530m0.md)
- [System](https://docs.apidog.com/649537m0.md)
- [Vehicle](https://docs.apidog.com/649549m0.md)
- [Word](https://docs.apidog.com/649558m0.md)

## Key Enhancements in Apidog Dynamic Values

Here are the key changes that make Apidog Dynamic Values even more powerful and user-friendly:

### 1. Simplified Expression Syntax for Easy Access

Apidog uses a concise and intuitive syntax for calling dynamic values:

- **Faker.js:** `faker.finance.accountName()`
- **Apidog:** `{{$finance.accountName}}`

Simply type `{{%` within Apidog to trigger auto-completion and effortlessly explore the available dynamic values.

### 2. Optimized Output for Objects and Arrays

Apidog simplifies data handling by returning JSON strings for methods that originally returned objects or arrays in Faker.js, enabling direct access to specific values.

#### Example 1: Extracting Airport Data

**Faker.js:** `faker.airline.airport()` returns an object:

```js
faker.airline.airport() // { name: 'Dallas Fort Worth International Airport', iataCode: 'DFW' } 
```

**Apidog:** Access specific fields directly:

```js
`{{$airline.airportName}}`  //'Dallas Fort Worth International Airport'
`{{$airline.airportIataCode}}`  // 'DFW'
```

#### Example 2: Handling Multiple Dates

**Faker.js:** `faker.date.betweens()` returns an array:

```js
faker.date.betweens({ from: '2020-01-01T00:00:00.000Z', to: '2030-01-01T00:00:00.000Z', count: { min: 2, max: 5 }})
// [
//   2021-12-19T06:35:40.191Z,
//   2022-09-10T08:03:51.351Z,
//   2023-04-19T11:41:17.501Z
// ]
```

**Apidog:** Returns a JSON stringified array for straightforward data processing:

```js
{{$date.betweens(from='2020-01-01T00:00:00',to='2030-01-01',min=2,max=5)}}  // ["2020-10-14 00:48:27","2021-10-25 22:46:34","2027-03-06 02:33:22","2028-04-22 20:13:40","2029-12-31 14:45:59"]
```

:::tip
For a comprehensive overview of adjusted methods and their parameters, refer to the Apidog documentation.
:::

### 3. Enhanced Locale Control

Apidog provides enhanced control over Locale settings for generating region-specific data:

- **Function-Level Settings:** Define Locale settings individually for each dynamic value function.
- **Project-Level Defaults:** Set a default Locale for your entire Apidog project.
- **Date Formatting Overrides:** Utilize the `format` method within date-related functions to apply Locale-specific formatting overrides.

### 4. Preset Parameters for Common Use Cases

Apidog boosts your efficiency by providing preset parameters for frequently used methods (customizable as needed):

- `{{$helpers.fromRegExp('[A-Z0-9]{4}-[A-Z0-9]{4}')}}`  // Generates strings matching a regular expression
- `{{$helpers.arrayElement(['abc','123'])}}`  // Randomly selects an element from an array
- `{{$helpers.arrayElements(['abc','123'])}}`  // Selects multiple random elements from an array
- `{{$helpers.replaceSymbols('##??**')}}`  // Replaces special symbols with random characters
- `{{$helpers.slugify('abc 123')}}`  //  Generates a URL-friendly slug

### 5. Expanded Dynamic Value Library

Apidog enriches your data generation capabilities with new categories and methods:

- **New Category: `food`** for generating diverse food-related data. Example: `{{$food.vegetable}}` 
- **New Methods:**
    - `{{$date.timeZone}}` for generating time zone data.
    - `{{$music.album}}` for creating realistic music album names.
    - `{{$music.artist}}` for generating artist names.
- **Enhanced Method Parameters:**
   -   `{{$phone.number(style='human')}}` for generating human-readable phone numbers, such as: (555) 123-4567.
   -   `{{$number.int(multipleOf=3)}}` for generating integers divisible by a specified number.

### 6. Unlimited Concatenation

Apidog provides ultimate flexibility by allowing you to seamlessly combine Mock data and dynamic values without limitations, enabling the creation of rich and realistic test scenarios.

### 7. Expanded Date Functionality

Apidog extends date-related functions with new parameters for formatting, offset calculation, and more, catering to diverse and complex testing requirements.

