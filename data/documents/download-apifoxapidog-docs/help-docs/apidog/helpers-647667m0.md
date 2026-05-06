# Helpers

Module with various helper methods providing basic (seed-dependent) operations useful for implementing faker methods.

## Module Overview

A particularly helpful method is `{{$helpers.arrayElement(['abc','123'])}}` which returns a random element from an array. This is useful when adding custom data that Faker doesn't contain.

A number of methods can generate strings according to various patterns: `{{$helpers.replaceSymbols('##??**')}}` and `{{$helpers.fromRegExp('[A-Z0-9]{4}-[A-Z0-9]{4}')}}`.

---

## arrayElement

Returns random element from the given array.

**Parameters**

| Name | Type | Default | Description |
| --- | --- |--- | --- |
| array | T[] | | The array to pick the value from.|

**Returns**: T

**Examples**

```js
{{$helpers.arrayElement(['cat','dog','mouse'])}}  // 'cat'
```
---

## arrayElements

Returns a subset with random elements of the given array in random order.

**Parameters**

| Name | Type | Default | Description |
| --- | --- |--- | --- |
| array | T[] | | The array to pick the value from.|
| max | number| | The maximum number of elements to pick.|
| min | number| | The minimum number of elements to pick.|


**Returns**: T

**Examples**

```js
{{$helpers.arrayElements(['cat','dog','mouse'])}}  // '["cat"]'

{{$helpers.arrayElements(['1','2','3','4'])}}  // '["4"]'
```
---

## fromRegExp

Generates a string matching the given regex like expressions.

This function doesn't provide full support of actual RegExp. Features such as grouping, anchors and character classes are not supported. If you are looking for a library that randomly generates strings based on RegExps, see [randexp.js](https://github.com/fent/randexp.js)

Supported patterns:

- `x{times}` => Repeat the `x` exactly `times` times.
- `x{min,max}` => Repeat the `x` `min` to `max` times.
- `[x-y]` => Randomly get a character between `x` and `y` (inclusive).
- `[x-y]{times}` => Randomly get a character between `x` and `y` (inclusive) and repeat it `times` times.
- `[x-y]{min,max}` => Randomly get a character between `x` and `y` (inclusive) and repeat it `min` to `max` times.
- `[^...] `=> Randomly get an ASCII number or letter character that is not in the given range. (e.g. `[^0-9]` will get a random non-numeric character).
- `[-...]` => Include dashes in the range. Must be placed after the negate character `^` and before any character sets if used (e.g. `[^-0-9]` will not get any numeric characters or dashes).
- `/[x-y]/i` => Randomly gets an uppercase or lowercase character between `x` and `y` (inclusive).
- `x?` => Randomly decide to include or not include `x`.
- `[x-y]?` => Randomly decide to include or not include characters between `x` and `y` (inclusive).
- `x*` => Repeat `x` 0 or more times.
- `[x-y]*` => Repeat characters between `x` and `y` (inclusive) 0 or more times.
- `x+` => Repeat `x` 1 or more times.
- `[x-y]+` => Repeat characters between `x` and `y` (inclusive) 1 or more times.
- `.` => returns a wildcard ASCII character that can be any number, character or symbol. Can be combined with quantifiers as well.

**Parameters**

| Name | Type | Default | Description |
| --- | --- |--- | --- |
| pattern |string \| RegExp| | The template string/RegExp to generate a matching string for.|

**Returns**: string

**Throws**: If min value is more than max value in quantifier, e.g. `#{10,5}`. If an invalid quantifier symbol is passed in.

**Examples**

```js
{{$helpers.fromRegExp('#{5}')}} // '#####'

{{$helpers.fromRegExp('#{2,9}')}} // '#######'

{{$helpers.fromRegExp('[1-7]')}} // '5'

{{$helpers.fromRegExp('#{3}test[1-5]')}} // '###test3'

{{$helpers.fromRegExp('[0-9a-dmno]')}} // '5'

{{$helpers.fromRegExp('[^a-zA-Z0-8]')}} // '9'

{{$helpers.fromRegExp('[a-d0-6]{2,8}')}} // 'a0dc45b0'

{{$helpers.fromRegExp('[-a-z]{5}')}} // 'a-zab'

{{$helpers.fromRegExp('/[A-Z0-9]{4}-[A-Z0-9]{4}/')}}// '/RUQN-KAVE/'

{{$helpers.fromRegExp('/[A-Z]{5}/i')}} // '/EJORS/i'

{{$helpers.fromRegExp('/.{5}/')}} // '/...../'

{{$helpers.fromRegExp('/Joh?n/')}} // '/Jon/'

{{$helpers.fromRegExp('/ABC*DE/')}} // '/ABCDE/'

{{$helpers.fromRegExp('/bee+p/')}} // '/beep/'
```
---

## rangeToNumber

Helper method that converts the given number or range to a number.

**Parameters**

| Name | Type | Default | Description |
| --- | --- |--- | --- |
| max | number|  | The maximum value for the range.|
| min | number|  | The minimum value for the range.|


**Returns**: number

**Examples**

```js
{{$helpers.rangeToNumber}}  // '6'
{{$helpers.rangeToNumber(min=1,max=10)}}  // '1'
```
---

## replaceCreditCardSymbols

Replaces the symbols and patterns in a credit card schema including Luhn checksum.

**Parameters**

| Name | Type | Default | Description |
| --- | --- |--- | --- |
| string | string| `'6453-####-####-####-###L'` | The credit card format pattern.|
| symbol | string| `'#'`| The symbol to replace with a digit.|

**Returns**: string

**Examples**

```js
{{$helpers.replaceCreditCardSymbols}}  // '6453-1529-4797-6717-3847'

{{$helpers.replaceCreditCardSymbols(string='1234-[4-9]-##!!-L')}}  // '1234-7-5096-4'
```
---

## replaceSymbols

Parses the given string symbol by symbols and replaces the placeholder appropriately.

- `#` will be replaced with a digit (`0` - `9`).
- `?` will be replaced with an upper letter ('A' - 'Z')
- and `*` will be replaced with either a digit or letter.

**Parameters**

| Name | Type | Default | Description |
| --- | --- |--- | --- |
| string | string| ` ` | The template string to parse.|

**Returns**: string

**Examples**

```js
{{$helpers.replaceSymbols('##??**')}}  // '24BTX6'

{{$helpers.replaceSymbols('#####')}}  // '17608'

{{$helpers.replaceSymbols('?????')}}  // 'SYJON'

{{$helpers.replaceSymbols('*****')}}  // 'CZ436'

{{$helpers.replaceSymbols('Your pin is: #?*#?*')}}  // 'Your pin is: 7UU5NK'
```
---

## slugify

Slugifies the given string. For that all spaces (` `) are replaced by hyphens (`-`) and most non word characters except for dots and hyphens will be removed.

**Parameters**

| Name | Type | Default | Description |
| --- | --- |--- | --- |
| string | string| ` ` |The input to slugify.|

**Returns**: string

**Examples**

```js
{{$helpers.slugify('abc 123')}}  // 'abc-123'

{{$helpers.slugify('Hello world!')}}  // 'Hello-world'
```

