# Internet

Module to generate internet related entries.

## Module Overview

For user accounts, you may need an `{{$internet.email}}` and a `{{$internet.password}}`, as well as a ASCII `{{$internet.userName}}` or Unicode `{{$internet.displayName}}`. Since the emails generated could coincidentally be real email addresses, you should not use these for sending real email addresses. If this is a concern, use `{{$internet.exampleEmail}}` instead.

For websites, you can generate a `{{$internet.domainName}}` or a full `{{$internet.url}}`.

To make your data more 🔥, you can use `{{$internet.emoji}}`.

You also have access to a number of the more technical elements of web requests, such as `{{$internet.httpMethod}}`, `{{$internet.httpStatusCode}}`, `{{$internet.ip}}`, `{{$internet.mac}}`, `{{$internet.userAgent}}`, and `{{$internet.port}}`.

---

## color

Generates a random css hex color code in aesthetically pleasing color palette.

Based on http://stackoverflow.com/questions/43044/algorithm-to-randomly-generate-an-aesthetically-pleasing-color-palette

**Parameters**

| Name | Type | Default | Description |
| --- | --- |--- | --- |
| blueBase | number| `0` | The optional base blue in range between `0` and `255`.|
| greenBase | number| `0` | The optional base green in range between `0` and `255`.|
| redBase | number| `0` | The optional base red in range between `0` and `255`.|

**Returns**: string

**Examples**

```js
{{$internet.color}}  // '#6a7351'
{{$internet.color(redBase=100,greenBase=100,blueBase=100)}}  // '#a1719a'
```
---

## displayName

Generates a display name using the given person's name as base. The resulting display name may use one or both of the provided names. If the input names include Unicode characters, the resulting display name will contain Unicode characters. It will not contain spaces.

**Parameters**

| Name | Type | Default | Description |
| --- | --- |--- | --- |
| firstName | string| `{{$person.firstName}}` | The optional first name to use.|
| lastName | string| `{{$person.lastName}}` | The optional last name to use.|

**Returns**: string

**Examples**

```js
{{$internet.displayName}}  // 'Karli_Christiansen91'

{{$internet.color(redBase=100,greenBase=100,blueBase=100)}}  // '#a1719a'

{{$internet.displayName(firstName='Jeanne',lastName='lastName')}}  // 'Jeanne.lastName26'
```
---

## domainName

Generates a random domain name.

**Returns**: string

**Examples**

```js
{{$internet.domainName}}  // 'wilted-nephew.com'
```
---

## domainSuffix

Returns a random domain suffix.

**Returns**: string

**Examples**

```js
{{$internet.domainSuffix}}  // 'com'
```
---

## domainWord

Generates a random domain word.

**Returns**: string

**Examples**

```js
{{$internet.domainWord}}  // 'illustrious-lashes'
```
---

## email

Generates an email address using the given person's name as base.

**Parameters**

| Name | Type | Default | Description |
| --- | --- |--- | --- |
| allowSpecialCharacters | boolean| `false` | Whether special characters such as `.!#$%&'*+ `should be included in the email address.|
| firstName | string| `{{$person.firstName}}` | The optional first name to use.|
| lastName | string| `{{$person.lastName}}` | The optional last name to use.|
| provider | string| |The mail provider domain to use. If not specified, a random free mail provider will be chosen.|

**Returns**: string

**Examples**

```js
{{$internet.email}}  // 'Marcelle58@yahoo.com'

{{$internet.email(firstName='Jeanne')}}  // 'Jeanne.Mitchell@gmail.com'

{{$internet.email(firstName='Jeanne',lastName='Doe')}}  // 'Jeanne.Doe59@gmail.com'

{{$internet.email(firstName='Jeanne',lastName='Doe',provider='example.fakerjs.dev')}}  // 'Jeanne_Doe@example.fakerjs.dev'

{{$internet.email(firstName='Jeanne',lastName='Doe',provider='example.fakerjs.dev',allowSpecialCharacters=true)}}  // 'Jeanne_Doe@example.fakerjs.dev'
```
---

## emoji

Generates a random emoji.

**Returns**: string

**Examples**

```js
{{$internet.emoji}} // '👨🏻‍🔬'
{{$internet.emoji(types=['food','nature'])}}  // ‘🥔’
```
---

## exampleEmail

Generates an email address using an example mail provider using the given person's name as base.

**Parameters**

| Name | Type | Default | Description |
| --- | --- |--- | --- |
| allowSpecialCharacters | boolean| `false` | Whether special characters such as `.!#$%&'*+ `should be included in the email address.|
| firstName | string| `{{$person.firstName}}` | The optional first name to use.|
| lastName | string| `{{$person.lastName}}` | The optional last name to use.|

**Returns**: string

**Examples**

```js
{{$internet.exampleEmail}} // ‘Melisa71@example.com’

{{$internet.exampleEmail(firstName='Jeanne')}}  // ‘Jeanne.Wunsch70@example.com’

{{$internet.exampleEmail(firstName='Jeanne',lastName='Doe')}}  // ‘Jeanne_Doe0@example.com’

{{$internet.exampleEmail(firstName='Jeanne',lastName='Doe',allowSpecialCharacters=true)}}  // ‘Jeanne_Doe18@example.org’
```
---

## httpMethod

Returns a random http method.

Can be either of the following:

- GET
- POST
- PUT
- DELETE
- PATCH

**Returns**: 'GET' | 'POST' | 'PUT' | 'DELETE' | 'PATCH'


**Examples**

```js
{{$internet.httpMethod}}  // ‘POST’
```
---

## httpStatusCode

Generates a random HTTP status code.

**Returns**: number

**Examples**

```js
{{$internet.httpStatusCode}}  // ‘404’
{{$internet.httpStatusCode(types=['success','serverError'])}}  // ‘505’
```
---

## ip

Generates a random IPv4 or IPv6 address.

**Returns**: string

**Examples**

```js
{{$internet.ip}} // ‘112.165.30.30’
```
---

## ip4

Generates a random IPv4 address.

**Returns**: string

**Examples**

```js
{{$internet.ipv4}} // ‘185.3.59.20’
```
---

## ip6

Generates a random IPv6 address.

**Returns**: string

**Examples**

```js
{{$internet.ipv6}} // ‘cf2d:5020:acfb:abd1:14a3:1af0:eac3:0eec’
```
---

## mac

Generates a random mac address.

**Parameters**

| Name | Type | Default | Description |
| --- | --- |--- | --- |
| separator | string| `:` | The optional separator to use. Can be either `':'`, `'-'` or `''`.|


**Returns**: string

**Examples**

```js
{{$internet.mac}} // ‘65:e4:37:2d:fa:e1’
```
---

## password

Generates a random password-like string. Do not use this method for generating actual passwords for users. Since the source of the randomness is not cryptographically secure, neither is this generator.

**Parameters**

| Name | Type | Default | Description |
| --- | --- |--- | --- |
| length | number| `15` |The length of the password to generate.|
| memorable | boolean| `false` |Whether the generated password should be memorable.|
| pattern | RegExp| `/\w/` |The pattern that all chars should match. This option will be ignored, if `memorable` is `true`.|
| prefix | string| ` ` |The prefix to use.|

**Returns**: string

**Examples**

```js
{{$internet.password}} // 'mgrAvW7pUjIebSR'
{{$internet.password(length=20)}}  // ‘fiumNIpNAcdLglbRLWuA’

{{$internet.password(length=20,memorable=true)}}  //  ‘pusuyakalusasohujono’

{{$internet.password(length=20,memorable=true,pattern='/[A-Z]/')}}  // ‘bohozucoyapobemusuti’

{{$internet.password(length=20,memorable=true,pattern='/[A-Z]/',prefix='Hello')}}  // ‘Hellojokoyaduhahamuv’
```
---

## port

Generates a random port number.

**Returns**: number

**Examples**

```js
{{$internet.port}}  // ‘41478’
```
---

## protocol

Returns a random web protocol. Either `http` or `https`.

**Returns**: 'http' | 'https'

**Examples**

```js
{{$internet.protocol}} // ‘https’
```
---

## url

Generates a random http(s) url.

**Parameters**

| Name | Type | Default | Description |
| --- | --- |--- | --- |
| appendSlash | boolean| `{{$datatype.boolean}}` | Whether to append a slash to the end of the url (path).|
| protocol | HTTPProtocolType	| `https` | The protocol to use. |

**Returns**: string

**Examples**

```js
{{$internet.url}} // ‘https://true-co-producer.name/’

{{$internet.url(appendSlash=true)}}  // 'https://pessimistic-order.net/'

{{$internet.url(appendSlash=true,protocol='http')}}  // 'http://warm-coast.info/'
```
---

## userAgent

Generates a random user agent string.

**Returns**: string

**Examples**

```js
{{$internet.userAgent}} // ‘Mozilla/5.0 (Windows; U; Windows NT 6.2)AppleWebKit/533.1.0 (KHTML, like Gecko) Version/4.0.3 Safari/533.1.0'
```
---

## userName

Generates a username using the given person's name as base. The resulting username may use neither, one or both of the names provided. This will always return a plain ASCII string. Some basic stripping of accents and transliteration of characters will be done.

**Parameters**

| Name | Type | Default | Description |
| --- | --- |--- | --- |
| firstName | string| `{{$person.firstName}}` | The optional first name to use.|
| lastName | string| `{{$person.lastName}}` | The optional last name to use.|

**Returns**: string

**Examples**

```js
{{$internet.userName}} // ‘Hiram25'
{{$internet.userName(firstName='Jeanne')}}  // 'Jeanne.Lockman35'
{{$internet.userName(firstName='Jeanne',lastName='Doe')}}  // 'Jeanne.Doe'
```

