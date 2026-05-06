# Company

Module to generate company related entries.

## Module Overview

To generate a random company name, use `name()`. This is localized in many locales.

To generate jargon-filled company catchphrases and buzzwords, use `catchPhrase()` or `buzzPhrase()`.

**Related Modules**
- For products and commerce, use [Commerce](https://docs.apidog.com/646336m0.md).
- For finance-related entries, use [Finance](https://docs.apidog.com/finance-647562m0.md).

---

## buzzAdjective

Returns a random buzz adjective that can be used to demonstrate data being viewed by a manager.

**Returns**: string

**Examples**

```js
{{$company.buzzAdjective}}  // 'back-end'
```

---

## buzzNoun

Returns a random buzz noun that can be used to demonstrate data being viewed by a manager.

**Returns**: string

**Examples**

```js
{{$company.buzzNoun}}  // 'lifetime value'
```

---

## buzzPhrase

Generates a random buzz phrase that can be used to demonstrate data being viewed by a manager.


**Returns**: string

**Examples**

```js
{{$company.buzzPhrase}}  // 'implement intuitive metrics'
```

---

## buzzVerb

Returns a random buzz verb that can be used to demonstrate data being viewed by a manager.

**Returns**: string

**Examples**

```js
{{$company.buzzVerb}}  // 'engage'
```

---

## catchPhrase

Generates a random catch phrase that can be displayed to an end user.

**Returns**: string

**Examples**

```js
{{$company.catchPhrase}}  // 'Expanded dedicated core'
```

---

## catchPhraseAdjective

Returns a random catch phrase adjective that can be displayed to an end user.

**Returns**: string

**Examples**

```js
{{$company.catchPhraseAdjective}}  // 'Triple-buffered'
```

---

## catchPhraseDescriptor

Returns a random catch phrase descriptor that can be displayed to an end user.

**Returns**: string

**Examples**

```js
{{$company.catchPhraseDescriptor}}  // 'non-volatile'
```

---

## catchPhraseNoun

Returns a random catch phrase noun that can be displayed to an end user.

**Returns**: string

**Examples**

```js
{{$company.catchPhraseNoun}}  // 'installation'
```

---

## name

Returns a random company name.

**Returns**: string

**Examples**

```js
{{$company.name}}  // 'Torphy - Gleason'
```

