# 常见编程语言对应的数据类型


Apifox 的 HTTP 项目的接口文档遵循 Swagger/OpenAPI 规范，其数据类型基于 JSON Schema 规范草案 2020-12。

JSON Schema 与编程语言无关，任何可以被转换为 JSON 的数据结构，都可以使用  JSON Schema 来描述。常见的编程语言的数据类型，都与 JSON Schema 的数据类型存在着映射关系，详见下面的表格。

## JavaScript

| JavaScript | JSON Schema | JSON 示例           |
| ---------- | ----------- | --------------------- |
| number     | number      | `1.1`, `-10.0`, `0` |
| number     | integer     | `1`, `-10`, `0`       |
| string     | string      | `"Hello World!"`        |
| boolean    | boolean | `true`, `false` |
| undefined  | null        | `null` |
| null       | null        | `null` |
| object     | object      | `{"k": v, …}` |
| array      | array       | `[v, …]` |

## Python

| Python           | JSON Schema | JSON 示例           |
| :--------------- | :---------- | :------------------ |
| int              | integer     | `1`, `-10`, `0`     |
| float            | number      | `1.1`, `-10.0`, `0` |
| str              | string      | `"Hello World!"`    |
| bool             | boolean     | `True`, `False`     |
| dict             | object      | `{"k": v, …}`       |
| list, set, tuple | array       | `[v, …]`            |

## Java

| Java                                                         | JSON Schema | JSON 示例                |
| :----------------------------------------------------------- | :---------- | :----------------------- |
| boolean, java.lang.Boolean                                   | boolean     | `true`, `false`            |
| char, java.lang.Character                                    | string      | `"\u0066"`, `"f"`          |
| java.lang.String                                             | string      | `"Hello World!"`         |
| byte, java.lang.Byte, short, java.lang.Short, int, java.lang.Integer, long, java.lang.Long | integer     | `1`, `-10`, `0`           |
| float, java.lang.Float, double, java.lang.Double             | number | `1.1`, `-10.0`, `0`        |
| java.util.List&lt;V>, java.util.Set&lt;V>, dataType[]              | array       | `[v, …]`                 |
| java.util.Map&lt;K,V>, DTO, POJO                                | object      | `{"k": v, …}`            |
| enum                                                         | string      | `"ENUM_VALUE"` |
| java.util.Date, java.sql.Date, java.sql.Timestamp, java.sql.Time | string      | `"2020-01-01 00:00:00"`  |
| java.time.LocalDateTime, java.time.LocalTime                 | string      | `"2020-01-01T00:00:00"`  |
| java.time.LocalDate                                          | string      | `"2020-01-01"`           |

## PHP

| PHP              | JSON Schema | JSON 示例           |
| :--------------- | :---------- | :------------------ |
| boolean          | boolean     | `true`, `false`     |
| integer          | integer     | `1`, `-10`, `0`     |
| float            | number      | `1.1`, `-10.0`, `0` |
| string           | string      | `"Hello World!"`    |
| array            | array       | `[v, …]`            |
| object           | object      | `{"k": v, …}`       |
| NULL             | null        | `null`              |

## Go

| Go               | JSON Schema | JSON 示例           |
| :--------------- | :---------- | :------------------ |
| bool             | boolean     | `true`, `false`     |
| string           | string      | `"Hello World!"`    |
| int, int8, int16, int32, int64 | integer | `1`, `-10`, `0`     |
| float32, float64 | number      | `1.1`, `-10.0`, `0` |
| array, slice     | array       | `[v, …]`            |
| struct, map      | object      | `{"k": v, …}`       |

## Ruby

| Ruby             | JSON Schema | JSON 示例           |
| :--------------- | :---------- | :------------------ |
| TrueClass, FalseClass | boolean | `true`, `false`     |
| String           | string      | `"Hello World!"`    |
| Fixnum, Bignum   | integer     | `1`, `-10`, `0`     |
| Float            | number      | `1.1`, `-10.0`, `0` |
| Array            | array       | `[v, …]`            |
| Hash             | object      | `{"k": v, …}`       |

