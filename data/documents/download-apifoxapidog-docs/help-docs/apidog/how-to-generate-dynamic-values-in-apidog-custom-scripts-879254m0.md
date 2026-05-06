# How to Generate Dynamic Values in Apidog Custom Scripts?

[PM Script API](https://docs.apidog.com/postman-scripts-reference-593586m0.md) Apidog supports generating dynamic values in custom scripts, using the `pm.variables.replaceInAsync(variableName:String):function` method to replace the "dynamic value expression" in the string with the actual value. The function returns a Promise, and await must be added when calling it.

An example of generating a random name is as follows:

```js
// Define a string containing a dynamic value expression
let stringWithVariable = "Hello, {{$person.fullName}}";

// Use replaceInAsync method to replace the {{$person.fullName}} placeholder
let realValueString = await pm.variables.replaceInAsync(stringWithVariable);
console.log(realValueString)
```

________________________________________________________________________________



`{{$person.fullName}}`  A real value was generated during the script execution.
<Background> 
![image.png](https://api.apidog.com/api/v1/projects/544525/resources/352281/image-preview)
</Background>

:::info[]
More usage of pm.variables can be referred to in [PM Script API](https://docs.apidog.com/postman-scripts-reference-593586m0.md)


For more information on dynamic values, please refer to [Dynamic values](https://docs.apidog.com/dynamic-values-541766m0.md)
:::
