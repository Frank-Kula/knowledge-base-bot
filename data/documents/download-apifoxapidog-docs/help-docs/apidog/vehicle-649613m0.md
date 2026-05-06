# Vehicle

Module to generate vehicle related entries.

## Module Overview

Most methods are related to cars/automobiles: a `{{$vehicle.vehicle}}` name is comprised of a car `{{$vehicle.manufacturer}}` and `{{$vehicle.model}}`. You can also generate `{{$vehicle.fuel}}`, `{{$vehicle.type}}`, and `{{$vehicle.color}}`, as well as typical car registration IDs `{{$vehicle.vin}}` and `{{$vehicle.vrm}}`.

If you prefer two wheels, you can generate a `{{$vehicle.bicycle}}` type instead.

---

## bicycle

Returns a type of bicycle.

**Returns**: string

**Examples**

```js
{{$vehicle.bicycle}}  // 'City Bicycle'
```
---

## color

Returns a vehicle color.

**Returns**: string

**Examples**

```js
{{$vehicle.color}}  // 'teal'
```
---

## fuel

Returns a fuel type.

**Returns**: string

**Examples**

```js
{{$vehicle.fuel}}  // 'Gasoline'
```
---

## manufacturer

Returns a manufacturer name.

**Returns**: string

**Examples**

```js
{{$vehicle.manufacturer}}  // 'Jeep'
```
---

## model

Returns a vehicle model.

**Returns**: string

**Examples**

```js
{{$vehicle.model}}  // 'Prius'
```
---

## type

Returns a vehicle type.

**Returns**: string

**Examples**

```js
{{$vehicle.type}}  // 'Crew Cab Pickup'
```
---

## vehicle

Returns a random vehicle.

**Returns**: string

**Examples**

```js
{{$vehicle.vehicle}}  // 'BMW PT Cruiser'
```
---

## vin

Returns a vehicle identification number (VIN).

**Returns**: string

**Examples**

```js
{{$vehicle.vin}}  // 'E2AD154L2TK700685'
```
---
## vrm

Returns a vehicle registration number (Vehicle Registration Mark - VRM)

**Returns**: string

**Examples**

```js
{{$vehicle.vrm}}  // 'OT08HEE'
```

