# Commerce

Module to generate commerce and product related entries.

## Module Overview

For a long product name like `'Incredible Soft Gloves'`, use `productName()`. The product names are generated from a list of adjectives, materials, and products, which can each be accessed separately using `productAdjective()`, `productMaterial()`, and `product()`. You can also create a description using `productDescription()`.

For a department in a shop or product category, use `department()`.

You can also create a price using `price()`.

---

## department

Returns a department inside a shop.

**Returns**: string

**Examples**

```js
{{$commerce.department}}  // 'Computers'
```

---

## isbn

Returns a random ISBN identifier.

**Parameters**

| Name | Type | Default | Description |
| --- | --- |--- | --- |
| separator | string | `'-'` | The separator to use in the format.|
| variant | 10 \| 13 | `13` | The variant of the identifier to return. Can be either `10` (10-digit format) or `13` (13-digit format).|

**Returns**: string

**Examples**

```js
{{$commerce.isbn}}  // '978-1-991214-85-0'

{{$commerce.isbn(variant=10)}}  // '0-516-95754-6'

{{$commerce.isbn(variant=13)}}  // '978-0-427-90508-9'

{{$commerce.isbn(separator=' ')}}  / '978 0 7460 5098 9'

{{$commerce.isbn(variant=10,separator=' ')}}  // '1 384 05626 2'

{{$commerce.isbn(variant=13,separator=' ')}}  // '978 1 62560 828 4'
```

---

## price

Generates a price between min and max (inclusive).

To better represent real-world prices, when `options.dec` is greater than 0, the final decimal digit in the returned string will be generated as follows:

- 50% of the time: `9`
- 30% of the time: `5`
- 10% of the time: `0`
- 10% of the time: a random digit from `0` to `9`

**Parameters**

| Name | Type | Default | Description |
| --- | --- |--- | --- |
| dec | number | `2` | The number of decimal places.|
| max | number | `1000`	|The maximum price.|
| min | number | `1` | The minimum price.|
| symbol | string | `‘’`|The currency value to use.|

**Returns**: string

**Examples**

```js
{{$commerce.price}}  // '286.29'

{{$commerce.price(min=100)}} // '156.45'

{{$commerce.isbn(variant=13)}}  // '978-0-427-90508-9'

{{$commerce.price(min=100,max=200)}}  / '104.85'

{{$commerce.price(min=100,max=200,dec=0)}}  // '193'

{{$commerce.price(min=100,max=200,dec=0,symbol='$')}}  // '$184'
```

---

## product

Returns a short product name.

**Returns**: string

**Examples**

```js
{{$commerce.product}}  // 'Pizza'
```
---

## productAdjective

Returns an adjective describing a product.

**Returns**: string

**Examples**

```js
{{$commerce.productAdjective}}  // 'Refined'
```
---

## productDescription

Returns a product description.

**Returns**: string

**Examples**

```js
{{$commerce.productDescription}}  // 'Ergonomic executive chair upholstered in bonded black leather and PVC padded seat and back for all-day comfort and support'
```
---

## productMaterial

Returns a material of a product.

**Returns**: string

**Examples**

```js
{{$commerce.productMaterial}}  // 'Steel'
```

---

## productName

Generates a random descriptive product name.

**Returns**: string

**Examples**

```js
{{$commerce.productName}} // 'Fantastic Soft Chips'
```

