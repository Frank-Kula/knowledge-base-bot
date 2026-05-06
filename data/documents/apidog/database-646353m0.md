# Database

Module to generate database related entries.

## Module Overview

Traditional relational database tables have data organized in columns with specific types - `column()`, `type()`. The database usually has an `engine()` and a default `collation()` for sorting.

For the NoSQL database MongoDB, `mongodbObjectId()` provides a random ID.

---

## collation

Returns a random database collation.

**Returns**: string

**Examples**

```js
{{$database.collation}}  // 'utf8_unicode_ci'
```
---

## column

Returns a random database column name.

**Returns**: string

**Examples**

```js
{{$database.column}}  // 'phone'
```
---

## mongodbObjectId

Returns a MongoDB ObjectId string.

**Returns**: string

**Examples**

```js
{{$database.mongodbObjectId}}  // '32488b5ddc1de4fe5f74eff5'
```
---

## type

Returns a random database column type.

**Returns**: string

**Examples**

```js
{{$database.type}}  // 'time'
```

