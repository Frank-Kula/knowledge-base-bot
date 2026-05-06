# Finance

Module to generate finance and money related entries.

## Module Overview

For a random amount, use `{{$finance.amount}}`.

For traditional bank accounts, use: `{{$finance.accountNumber}}`, `{{$finance.accountName}}`, `{{$finance.bic}}`, `{{$finance.iban}}`, `{{$finance.pin}}` and `{{$finance.routingNumber}}`.

For credit card related methods, use: `{{$finance.creditCardNumber}}`, `{{$finance.creditCardCVV}}`, `{{$finance.creditCardIssuer}}`, `{{$finance.transactionDescription}}` and `{{$finance.transactionType}}`.

For blockchain related methods, use: `{{$finance.bitcoinAddress}}`, `{{$finance.ethereumAddress}}` and `{{$finance.litecoinAddress}}`.

---

## accountName

Generates a random account name.

**Returns**: string

**Examples**

```js
{{$finance.accountName}}  // 'Home Loan Account'
```
---

## accountNumber

Generates a random account number.

**Parameters**

| Name | Type | Default | Description |
| --- | --- |--- | --- |
| length | number | `8` | The length of the account number.|

**Returns**: string

**Examples**

```js
{{$finance.accountNumber}}  // '32765009'
{{$finance.accountNumber(length=5)}}  // '36908'
```
---

## amount

Generates a random amount between the given bounds (inclusive).

**Parameters**

| Name | Type | Default | Description |
| --- | --- |--- | --- |
| autoFormat | boolean	 | `false` | |
| dec | number | `2` | The number of decimal places for the amount.|
| max | number | `1000` | The upper bound for the amount.|
| min | number | `0` | The lower bound for the amount.|
| symbol | string| `''`| The symbol used to prefix the amount.|

**Returns**: string

**Examples**

```js
{{$finance.amount}}  // '400.29'

{{$finance.amount(min=5,max=10)}}  // '8.21'

{{$finance.amount(min=5,max=10,dec=0)}}  // '9'

{{$finance.amount(min=5,max=10,dec=2,symbol='$')}}  // '$7.29'

{{$finance.amount(min=5,max=10,dec=2,symbol='$',autoFormat=true)}}  // '$7.69'
```
---

## bic

Generates a random SWIFT/BIC code based on the ISO-9362 format.

**Parameters**

| Name | Type | Default | Description |
| --- | --- |--- | --- |
| includeBranchCode | boolean	 | `{{$datatype.boolean}}` | Whether to include a three-digit branch code at the end of the generated code.|

**Returns**: string

**Examples**

```js
{{$finance.bic}} // 'LPNACUB53ED'

{{$finance.bic(includeBranchCode=true)}}  // 'QSCPSJSGXXX'

{{$finance.bic(includeBranchCode=false)}}  // 'SAITKY56'
```
---

## bitcoinAddress

Generates a random Bitcoin address.

**Parameters**

| Name | Type | Default | Description |
| --- | --- |--- | --- |
| network | 'mainnet' \| 'testnet'| `mainnet` | The bitcoin network (`'mainnet'` or `'testnet'`).|
| type | 'legacy' \| 'segwit' \| 'bech32' \| 'taproot'\| `faker.helpers.arrayElement(['legacy','sewgit','bech32','taproot'])` | The bitcoin address type (`'legacy'`, `'sewgit'`, `'bech32'` or `'taproot'`).|

**Returns**: string

**Examples**

```js
{{$finance.bitcoinAddress}} // '1TZcCi8mttkfawi4bvwumBb3MuVdV6vcC'

{{$finance.bitcoinAddress(type='bech32')}}  // 'bc19a4f2kxzldwm5glsfkcagzc5smdx8rxk5uh5h84'

{{$finance.bitcoinAddress(type='bech32',network='testnet')}}  // 'tb18zkyajyvtarzscqxf02zjmh6y89j7s0ytdnzfzc'
```
---

## creditCardCVV

Generates a random credit card CVV.

**Returns**: string

**Examples**

```js
{{$finance.creditCardCVV}} // '259'
```
---

## creditCardIssuer

Returns a random credit card issuer.

**Returns**: string

**Examples**

```js
{{$finance.creditCardIssuer}}  // 'mastercard'
```
---

## creditCardNumber

Generates a random credit card number.

**Parameters**

| Name | Type | Default | Description |
| --- | --- |--- | --- |
| issuer | string| ` ` | The name of the issuer (case-insensitive) or the format used to generate one.|

**Returns**: string

**Examples**

```js
{{$finance.creditCardNumber}} // '3047-598444-5005'

{{$finance.creditCardNumber(issuer='visa')}} // '4085568219353'

{{$finance.creditCardNumber(issuer='63[7-9]#-####-####-###L')}} // '6399-9882-5790-6281'

```
---

## currencyCode

Returns a random currency code. (The short text/abbreviation for the currency (e.g. `US Dollar` -> `USD`))

**Returns**: string

**Examples**

```js
{{$finance.currencyCode}}  // 'PYG'
```
---

## currencyName

Returns a random currency name.


**Returns**: string

**Examples**

```js
{{$finance.currencyName}}  // 'Mexican Peso'
```
---

## currencySymbol

Returns a random currency symbol.

**Returns**: string

**Examples**

```js
{{$finance.currencySymbol}}  // '$'
```
---

## ethereumAddress

Creates a random, non-checksum Ethereum address.

To generate a checksummed Ethereum address (with specific per character casing), wrap this method in a custom method and use third-party libraries to transform the result.

**Returns**: string

**Examples**

```js
{{$finance.ethereumAddress}}  // '0xd56f94f53f3a6b5c22e2454fc5de6e6ed70405ed'
```
---

## iban

Generates a random iban.

**Parameters**

| Name | Type | Default | Description |
| --- | --- |--- | --- |
| countryCode | string|  | The country code from which you want to generate an IBAN, if none is provided a random country will be used.|
| formatted | boolean| `false`| Return a formatted version of the generated IBAN.|

**Returns**: string

**Examples**

```js
{{$finance.iban}} // 'TR736918640040966092800056'

{{$finance.iban(formatted=true)}} // 'PT52 2975 5818 3052 0105 2010 7'

{{$finance.iban(formatted=true,countryCode='DO')}} // 'DO63 OHAF 2006 0035 5087 4800 4001'

```
---

## maskedNumber

Generates a random masked number.

**Parameters**

| Name | Type | Default | Description |
| --- | --- |--- | --- |
| ellipsis | boolean|`true`| Whether to prefix the numbers with an ellipsis.|
| length | number| `4`| The length of the unmasked number.|
| parens | boolean| `true`| Whether to use surrounding parenthesis.|

**Returns**: string

**Examples**

```js
{{$finance.maskedNumber}} // '(...9829)'

{{$finance.maskedNumber(length=3)}} // '(...094)'

{{$finance.maskedNumber(length=3,parens=false)}} // '...250'

{{$finance.maskedNumber(length=3,parens=false,ellipsis=false)}} // '626'
```
---

## pin

Generates a random PIN number.

**Parameters**

| Name | Type | Default | Description |
| --- | --- |--- | --- |
| length | number| `4`| The length of the PIN to generate.|

**Returns**: string

**Examples**

```js
{{$finance.pin}} // '1293'
{{$finance.pin(length=6)}} // '781299'
```
---

## routingNumber

Generates a random routing number.

**Returns**: string

**Examples**

```js
{{$finance.routingNumber}} // '325585941'
```
---

## transactionDescription

Generates a random transaction description.

**Returns**: string

**Examples**

```js
{{$finance.transactionDescription}} // 'invoice transaction at Armstrong - Schneider using card ending with ***(...9040) for ANG 828.98 in account ***58526794'
```
---

## transactionType

Returns a random transaction type.

**Returns**: string

**Examples**

```js
{{$finance.transactionType}}  // 'withdrawal'
```

