# CSV File Format

CSV (Comma-Separated Values) is a widely-used file format for importing and exporting data in Apidog. This reference guide outlines the CSV file format specification as defined in RFC 4180, which Apidog follows for data import/export operations.

:::info[]
The CSV format specification is defined in [RFC 4180](https://tools.ietf.org/html/rfc4180), which provides standardized rules for CSV file structure.
:::

## Format Specifications

### 1. Line Separation

Each record in the file must be on a different line, separated by a line feed `CRLF`.

**Example:**

```js
 aaa,bbb,ccc
 zzz,yyy,xxx
```

### 2. File Ending

The end of the last record does not include a line break.

**Example:**

```js
 aaa,bbb,ccc
 zzz,yyy,xxx
```

### 3. Field Names (Optional Header)

The first record in the file may be a field name (not required). If it does contain field names, the number of names and the storage rules must be consistent with the other records.

**Example:**

```js
field_name,field_name,field_name
aaa,bbb,ccc
zzz,yyy,xxx
```

### 4. Field Separation

Each record can contain one or more fields, each separated by a comma. All records in the file must have the same number of fields. Spaces in fields are field values and should not be ignored. The last field of each record should not be followed by a comma.

**Example:**

```js
aaa,bbb,ccc
```

:::warning[Field Consistency]
All records must have the same number of fields. Inconsistent field counts will cause import errors.
:::

### 5. Quoting Fields

Each field can be enclosed in double quotes (not always necessary). If the field is not enclosed in double quotes, double quotes should not appear in the fields.

**Example:**

```js
"aaa","bbb","ccc"
zzz,yyy,xxx
```

### 6. Special Characters in Fields

Fields containing line breaks, double quotes, or commas should be enclosed in double quotes.

**Example:**

```js
"aaa","b
bb","ccc"
zzz,yyy,xxx
```

### 7. Escaping Double Quotes

If a field is enclosed in double quotes and contains a double quote character, you need to add another double quote in front of it to escape it.

**Example:**

```js
"aaa","b""bb","ccc"
```

## Best Practices

- Always include a header row with field names for clarity
- Use double quotes for fields containing special characters
- Ensure consistent field counts across all records
- Test your CSV file with a small sample before importing large datasets

## References

- [RFC 4180 - Common Format and MIME Type for CSV Files](https://tools.ietf.org/html/rfc4180)

