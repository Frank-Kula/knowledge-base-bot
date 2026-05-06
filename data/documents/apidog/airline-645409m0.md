# Airline

Module to generate airline and airport related data.

## Module Overview

Several methods in this module return objects rather than strings. For example, you can use `{{$airline.airportIataCode}}` to pick out the specific property you need.

For a random airport, use `{{$airline.airportName}}` and `{{$airline.airportIataCode}}`.

For a random airline, use `{{$airline.airlineName}}` and `{{$airline.airlineIataCode}}`.

For a dummy booking, a passenger will generally book a flight on a specific `{{$airline.flightNumber}}`, `{{$airline.airplaneName}},` be allocated a `{{$airline.seat}} `and `{{$airline.recordLocator}}`.

**Related Modules**

To generate sample passenger data, you can use the methods of the [Person](https://docs.apidog.com/649475m0.md) module.

---

## aircraftType

Returns a random aircraft type.

**Returns**: 'narrowbody' | 'regional' | 'widebody'

**Examples**

```js
{{$airline.aircraftType}}  // 'Asiana Airlines'
```

---

## airline

:::info
The original `faker.airline.airline()` method has been refined into two more precise variables:

*  `{{$airline.airlineName}}`: Generates an airline name.
*  `{{$airline.airlineIataCode}}`: Generates an airline IATA code.
:::

Generates a random airline.

**Returns**: Airline

**Examples**

```js
{{$airline.airlineName}}  // 'Asiana Airlines'
{{$airline.airlineIataCode}}  // 'CX'
```
---

## airplane

:::info
The original `faker.airline.airplane()` method has been refined into two more precise variables:

*  `{{$airline.airplaneName}}`: Generates an airplane name.
*  `{{$airline.airplaneIataTypeCode}}`: Generates an airplane IATA code.
:::

Generates a random airplane.

**Returns**: airplane

**Examples**

```js
{{$airline.airplaneName}}  // 'ATupolev Tu-134'
{{$airline.airplaneIataTypeCode}}  // 'D3F'
```

---

## airport

:::info
The original `faker.airline.airport()` method has been refined into two more precise variables:

*  `{{$airline.airportName}}`: Generates an airport name.
*  `{{$airline.airportIataCode}}`: Generates an airport IATA code.
:::

Generates a random airport.

**Returns**: Airport

**Examples**

```js
{{$airline.airportName}}  // 'AHurgada International Airport'
{{$airline.airportIataCode}} // 'WUS'
```

---

## flightNumber

Returns a random flight number. Flight numbers are always 1 to 4 digits long. Sometimes they are used without leading zeros (e.g.: `American Airlines flight 425`) and sometimes with leading zeros, often with the airline code prepended (e.g.: `AA0425`).

To generate a flight number prepended with an airline code, combine this function with the `airline()` function and use template literals:

```js
{{$airline.airlineIataCode}}{{$airline.flightNumber(addLeadingZeros=true)}}  // 'CA0003'
```

**Parameters**

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| addLeadingZeros | boolean | `false` | Whether to pad the flight number up to 4 digits with leading zeros. |
| length | number \| `{ min: number; max: number; }` | `{ min: 1, max: 4 }` | The number or range of digits to generate. |

**Returns**: string

**Examples**

```js
{{$airline.flightNumber}}  // '6373'
{{$airline.flightNumber(addLeadingZeros=true)}}  // '0064'
{{$airline.flightNumber(length=2,addLeadingZeros=true)}}  // '0030'
{{$airline.flightNumber(length=2,min=2,max=3,addLeadingZeros=true)}}  // '0042'
{{$airline.flightNumber(length=3)}}  // '884'
{{$airline.flightNumber(min=2,max=3)}}  // '52'
```

---

## recordLocator

Generates a random record locator. Record locators are used by airlines to identify reservations. They're also known as booking reference numbers, locator codes, confirmation codes, or reservation codes.

**Parameters**

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| allowNumerics | boolean | `false` | Whether to allow numeric characters. |
| allowVisuallySimilarCharacters| boolean | `false`| Whether to allow visually similar characters such as '1' and 'I'. |

**Returns**: string

**Examples**

```js
{{$airline.recordLocator}}  // 'SYSQUW'
{{$airline.recordLocator(allowNumerics=true)}}  // 'CZY6RE'
{{$airline.recordLocator(allowVisuallySimilarCharacters=true)}}  // 'HBFFIB'
{{$airline.recordLocator(allowNumerics=true,allowVisuallySimilarCharacters=true)}}  // '0MELWZ'
```

---

## seat

Generates a random seat.

**Parameters**

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| aircraftType	 | 'narrowbody' \| 'regional' \| 'widebody' | `narrowbody` | The aircraft type. Can be one of `narrowbody`, `regional`, `widebody`.|

**Returns**: string

**Examples**

```js
{{$airline.seat}}  // '4F'
{{$airline.seat(aircraftType='narrowbody')}}  // '14B'
{{$airline.seat(aircraftType='regional')}} // '2D'
{{$airline.seat(aircraftType='widebody')}} // '23C'
```

