# Science

Module to generate science related entries.

## Module Overview

Both methods in this module return objects rather than strings. For example, you can use `{{$science.chemicalElementName}}` to pick out the specific property you need.

---

## chemicalElement

Returns a random periodic table element.

:::info
The original `faker.science.chemicalElement()` method has been refined into three more precise variables:

*  `{{$science.chemicalElementSymbol}}`: Generates an chemicalElement Symbol.
*  `{{$science.chemicalElementName}}`: Generates an chemicalElement Name.
*  `{{$science.chemicalElementAtomicNumber}}`: Generates an chemicalElement AtomicNumber.
:::

**Returns**: string

**Examples**

```js
{{$science.chemicalElementAtomicNumber}} // '72'

{{$science.chemicalElementName}}  // 'Ytterbium'

{{$science.chemicalElementSymbol}}  // 'Fm'
```
---

## unit

Returns a random scientific unit.

:::info
The original `faker.science.unit()` method has been refined into two more precise variables:

*  `{{$science.unitName}}`: Generates an unit name.
*  `{{$science.unitSymbol}}`: Generates an unit Symbol.
:::

**Returns**: string

**Examples**

```js
{{$science.unitName}} // 'farad'

{{$science.unitSymbol}} // 'lm'
```

