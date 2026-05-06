# Location

Module to generate addresses and locations.

## Module Overview

For a typical street address for a locale, use `{{$location.streetAddress}}`, `{{$location.city}}`, `{{$location.state}}`, and `{{$location.zipCode}}`. Most locales provide localized versions for a specific country.

If you need latitude and longitude coordinates, use `{{$location.latitude}}` and `{{$location.longitude}}`, or `{{$location.nearbyGPSCoordinateLatitude}}` for a latitude/longitude near a given location.

For a random country, you can use `{{$location.country}}` or `{{$location.countryCode}}`.

---

## buildingNumber

Generates a random building number.

**Returns**: string

**Examples**

```js
{{$location.buildingNumber}}  // '9954'
```
---

## cardinalDirection

Returns a random cardinal direction.

**Parameters**

| Name | Type | Default | Description |
| --- | --- |--- | --- |
| abbreviated | boolean| `false` |If true this will return abbreviated directions (N, E, etc). Otherwise this will return the long name.|

**Returns**: string

**Examples**

```js
{{$location.cardinalDirection}}  // 'East'

{{$location.cardinalDirection(abbreviated=true)}}  // 'E'
```
---

## city

Generates a random localized city name.

**Returns**: string

**Examples**

```js
{{$location.city}}  // '9954'
```
---

## country

Returns a random country name.

**Returns**: string

**Examples**

```js
{{$location.country}}  // 'Estonia'
```
---

## countryCode

Returns a random country name.

**Parameters**

| Name | Type | Default | Description |
| --- | --- |--- | --- |
| variant | 'alpha-2' \|'alpha-3' \| 'numeric'| `'alpha-2'` |The code to return. Can be either `'alpha-2'` (two-letter code), `'alpha-3'` (three-letter code) or `'numeric'` (numeric code).|

**Returns**: string

**Examples**

```js
{{$location.countryCode}}  // 'CZ'
{{$location.countryCode(variant='alpha-2')}}  // 'PL '
{{$location.countryCode(variant='alpha-3')}}  // 'SLE'
{{$location.countryCode(variant='numeric')}}  // '807'
```
---

## direction

Returns a random direction .

**Parameters**

| Name | Type | Default | Description |
| --- | --- |--- | --- |
| abbreviated | boolean| `false` |If true this will return abbreviated directions (NW, E, etc). Otherwise this will return the long name.|

**Returns**: string

**Examples**

```js
{{$location.direction}}  // 'East'
{{$location.direction(abbreviated=true)}}  // 'N'
```
---

## latitude

Generates a random latitude.

**Parameters**

| Name | Type | Default | Description |
| --- | --- |--- | --- |
| max | number| `90` |The upper bound for the latitude to generate.|
| min | number| `-90` |The lower bound for the latitude to generate.|
| precision | number| `4` |The number of decimal points of precision for the latitude.|

**Returns**: number

**Examples**

```js
{{$location.latitude}}  // '89.855'

{{$location.latitude(max=10)}}  // '-61.3305'

{{$location.latitude(min=-10,max=10)}}  // ‘9.3998’

{{$location.latitude(min=-10,max=10,precision=5)}}  // ‘7.46934’
```
---

## longitude

Generates a random longitude.

**Parameters**

| Name | Type | Default | Description |
| --- | --- |--- | --- |
| max | number| `90` |The upper bound for the longitude to generate.|
| min | number| `-90` |The lower bound for the longitude to generate.|
| precision | number| `4` |The number of decimal points of precision for the longitude.|

**Returns**: number

**Examples**

```js
{{$location.longitude}}  // '89.855'

{{$location.longitude(max=10)}}  // '-61.3305'

{{$location.longitude(min=-10,max=10)}}  // ‘9.3998’

{{$location.longitude(min=-10,max=10,precision=5)}}  // ‘7.46934’
```
---

## nearbyGPSCoordinate

Generates a random GPS coordinate within the specified radius from the given coordinate.

:::info
The original `faker.location.nearbyGPSCoordinate()` method has been refined into two more precise variables:

*  `{{$location.nearbyGPSCoordinateLatitude}}`: Generates an Latitude within the specified radius from the given coordinate.
*  `{{$location.nearbyGPSCoordinateLongitude}}`: Generates an Longitude within the specified radius from the given coordinate.
:::

**Parameters**

| Name | Type | Default | Description |
| --- | --- |--- | --- |
| isMetric | boolean| `false` |If `true` assume the radius to be in kilometers. If `false` for miles.|
| latitude | number||The original latitude to get a new coordinate close to.|
| longitude |number||The original longitude to get a new coordinate close to.|
| radius | number| `10` |The maximum distance from the given coordinate to the new coordinate.|

**Returns**:  [latitude: number, longitude: number]

**Examples**

```js
{{$location.nearbyGPSCoordinateLongitude}} // '76.1291'

{{$location.nearbyGPSCoordinateLongitude(latitude=33,longitude=178)}} // '178.07134671593099'

{{$location.nearbyGPSCoordinateLongitude(latitude=33,longitude=178,radius=1000,isMetric=true)}}  // ‘179.85715545348557’
```
---

## ordinalDirection

Returns a random ordinal direction (northwest, southeast, etc).

**Parameters**

| Name | Type | Default | Description |
| --- | --- |--- | --- |
| abbreviated | boolean| `false` |If true this will return abbreviated directions (NW, SE, etc). Otherwise this will return the long name.|

**Returns**: string

**Examples**

```js
{{$location.ordinalDirection}} // 'Southwest'

{{$location.ordinalDirection(abbreviated=true)}} // ‘NW’
```
---

## secondaryAddress

Generates a random localized secondary address. This refers to a specific location at a given address such as an apartment or room number.

**Returns**: string

**Examples**

```js
{{$location.secondaryAddress}} // ‘Suite 781’
```
---

## state

Returns a random localized state, or other equivalent first-level administrative entity for the locale's country such as a province or region. Generally, these are the ISO 3166-2 subdivisions for a country. If a locale doesn't correspond to one specific country, the method may return ISO 3166-2 subdivisions from one or more countries that uses that language. For example, the `ar` locale includes subdivisions from Arabic-speaking countries, such as Tunisia, Algeria, Syria, Lebanon, etc. For historical compatibility reasons, the default `en` locale only includes states in the United States (identical to `en_US`). However, you can use other English locales, such as `en_IN`, `en_GB`, and `en_AU`, if needed.

**Parameters**

| Name | Type | Default | Description |
| --- | --- |--- | --- |
| abbreviated | boolean| `false` |If true this will return abbreviated first-level administrative entity names. Otherwise this will return the long name.|

**Returns**: string

**Examples**

```js
{{$location.state}}  // 'Michigan'

{{$location.state(abbreviated=true)}} // ‘MD’
```
---

## street

Generates a random localized street name.

**Returns**: string

**Examples**

```js
{{$location.street}}  // ‘Jast Landing’
```
---

## streetAddress

Generates a random localized street address.

**Parameters**

| Name | Type | Default | Description |
| --- | --- |--- | --- |
| useFullAddress | boolean| |When true this will generate a full address. Otherwise it will just generate a street address.|


**Returns**: string

**Examples**

```js
{{$location.streetAddress}}  // ‘476 Forest Avenue’

{{$location.streetAddress(useFullAddress=true)}}  // ‘190 Jorge Trail Suite 352’
```
---

## timeZone

Returns a random IANA time zone relevant to this locale.

The returned time zone is tied to the current locale.

**Returns**: string

**Examples**

```js
{{$location.timeZone}}  // ‘America/Porto_Velho’
```
---

## zipCode

Generates random zip code from specified format. If format is not specified, the locale's zip format is used.

**Parameters**

| Name | Type | Default | Description |
| --- | --- |--- | --- |
| format | string| |WThe optional format used to generate the zip code. This won't be used if the state option is specified.|

**Returns**: string

**Examples**

```js
{{$location.zipCode}}  // ‘17711’

{{$location.zipCode(format='####')}}  // ‘0306’
```

