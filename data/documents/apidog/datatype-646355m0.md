# Datatype

Module to generate boolean values.

## Module Overview

For a simple random true or false value, use `boolean()`.

---

## boolean

Returns the boolean value true or false.

Note: A probability of `0.75` results in `true` being returned `75%` of the calls; likewise `0.3` => `30%`. If the probability is` <= 0.0`, it will always return `false`. If the probability is `>= 1.0`, it will always return `true`. The probability is limited to two decimal places.

**Parameters**

| Name | Type | Default | Description |
| --- | --- |--- | --- |
| probability | number | `0.5` | The probability (`[0.00, 1.00]`) of returning `true`.|

**Returns**: boolean

**Examples**

```js
{{$datatype.boolean}}  // 'false'

{{$datatype.boolean(probability=0.1)}}  // ‘false’
```

:::note
The function `faker.datatype.boolean(0.9)` used a positional argument `0.9` to specify the probability of returning `True`.

This has been updated to use a named parameter `probability`.  The equivalent function call is now `{{ $datatype.boolean(probability=0.9) }}`.
:::

