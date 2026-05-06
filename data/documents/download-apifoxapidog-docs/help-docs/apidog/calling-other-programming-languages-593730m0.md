# Calling Other Programming Languages

Apidog allows you to execute external programs (scripts, JARs, binaries) from your Javascript environment. This enables you to leverage existing code in languages like Java, Python, PHP, Go, Shell, etc.

:::warning[Security Notice]
External programs run outside the Apidog sandbox and have full access to your system. Ensure you trust the code you are executing.
:::

## Supported Languages
Apidog infers the execution command based on file extensions:

| Language | Extension | Command Prefix |
| :--- | :--- | :--- |
| **Java** | `.jar` | `java -jar` |
| **Python** | `.py` | `python` |
| **Node.js** | `.js` | `node` |
| **PHP** | `.php` | `php` |
| **Go** | `.go` | `go run` |
| **Shell** | `.sh` | `sh` |
| **Ruby** | `.rb` | `ruby` |
| **Lua** | `.lua` | `lua` |

## How to Call External Programs

1.  **Open External Program Directory**: Click the folder icon in the script editor to open the directory where your external scripts should be placed.
    
    <Background>
      ![External Program Directory](https://assets.apidog.com/uploads/help/2023/11/14/2bc81154adafd56e118cda73f9fae1be.png)
    </Background>

2.  **Execute via Script**: Use `pm.executeAsync` to call the program.

    ```javascript
    // Calls: java -jar "my-tool.jar" "arg1" "arg2"
    const result = await pm.executeAsync('my-tool.jar', ['arg1', 'arg2']);
    console.log(result);
    ```

## API Reference

### `pm.executeAsync`

- `filePath` _string_ External program path 
- `args` _string[]_ Parameters. When calling specified methods in a jar package, `JSON.stringify` will be used for conversion. Except for that, non-_string_ types will be implicitly converted to _string_.
- `options` _Object_
  - `command` _string_ The execution command of the external program, the first part of "command prefix" is the execution command. Optional, default value is inferred automatically (see "command prefix" table above), can be customized to any program.
  - `cwd` _string_ Working directory of the subprocess. Optional, default is "External Programs Directory".
  - `env` _Record&lt;string, string&gt;_ Environment variables of the subprocess. Optional, default is `{}`.
  - `windowsEncoding` _string_ Encoding used on Windows system. Optional, default is `"cp936"`.
  - `className` _string_ Specify the class name to call in the jar package, e.g. `"com.apidog.Utils"`. 
  - `method` _string_ Specify the method name to call in the jar package, e.g. `"add"`. 
  - `paramTypes` _string[]_ Specify the parameter types of the method to call in the jar package, e.g. `["int", "int"]`. 
- Return: _Promise&lt;string&gt;_

:::tip[Usage of `command` parameter]

By default Apidog uses `python` to execute `.py` files. If `python3` is already installed on the computer, `command` can be specified as `python3`.

```javascript
pm.executeAsync('./demo.py', [], { command: 'python3' }).then(res => {
   console.log('result: ', res);
});
```

:::

### `pm.execute`

:::tip[]
It is recommended to use `pm.executeAsync` instead.
:::

`pm.execute(filePath, args, options)`

- `filePath` _string_ External program path
- `args` _string[]_ Parameters. When calling specified methods in a jar package, `JSON.stringify` will be used for conversion. Except for that, non-_string_ types will be implicitly converted to _string_.
- `options` _Object_
  - `windowsEncoding` _string_ Encoding used on Windows system. Optional, default is `"cp936"`.
  - `className` _string_ Specify the class name to call in the jar package, e.g. `"com.apidog.Utils"`. 
  - `method` _string_ Specify the method name to call in the jar package, e.g. `"add"`. 
  - `paramTypes` _string[]_ Specify the parameter types of the method to call in the jar package, e.g. `["int", "int"]`.
- Return: _string_

## Execution and Logs 

When executing a program, the executed command will be printed in the console (for reference only). If the result does not meet expectations, you can copy the command and paste it in `Shell/CMD` to debug.

The console will also print the "standard output (stdout)" and "standard error output (stderr)" of the executed process. The stdout content (excluding the trailing newline character) will be the final result of the execution. 

:::tip
For historical reasons, `pm.execute` treats execution as failed when there is content in stderr. This causes some programs to fail when outputting warnings or error messages. `pm.executeAsync` changes to use the **exit code** of the process to determine if the execution failed.  
:::

<Background>
![](https://assets.apidog.com/uploads/help/2023/11/15/a069941be4890dbc6ca04cc498506ed9.png)
</Background>

## Input and Output of External Programs

### Parameters

Since the specified external program runs with command line execution, it can only get the passed in parameters through command line arguments.

For example, in script `pm.executeAsync('add.js', [2, 3])`, the actual executed command is `node add.js 2 3`. To get the parameters in the external script add.js: 

```js
let a = parseInt(process.argv[1]); // 2  
let b = parseInt(process.argv[2]); // 3
```

:::tip 

1. Different programming languages have different ways to get command line arguments, please refer to corresponding language docs.
2. The type of command line arguments is always _string_, need to convert based on actual types.
   :::

### Return Value

As mentioned above, Apidog uses the stdout content as the result of program execution. So printing content to stdout can return results.

For example, in script `const result = await pm.executeAsync('add.js', [2, 3])`, the result can be returned by:

```js 
console.log(parseInt(process.argv[1]) + parseInt(process.argv[2]));
```

:::tip[]

1. Different programming languages have different ways to print to stdout, refer to corresponding language docs.  
2. The return type is _string_, need to convert based on actual types.
3. The trailing newline character of the result will be trimmed.
4. When calling specified methods in jar packages, the return value of the called method will be used as the final return value.
   :::

### Throwing Errors

Throwing errors can fail the current task and stop execution. For example: 

```js
throw Error("Execution failed"); 
```

:::tip[]

1. Different programming languages have different ways to throw errors, refer to corresponding docs.
2. In JavaScript, `console.error('Error')` only prints to stderr instead of throwing an error. Consider this while using other languages too.
   :::

### Debug Information 

Since `pm.executeAsync` uses exit code instead of stderr to determine success, stderr can be used to print debug information without affecting execution.

For example:

```js
console.warn("debug info");
console.error("error info");
```

:::tip

1. Only `pm.executeAsync` supports this way of printing debug info.  
2. Different programming languages have different ways to print to stderr, refer to corresponding docs.
   :::

## Migrate From `pm.execute` to `pm.executeAsync`

Since the return value of `pm.executeAsync` is _Promise_ type, `execute` cannot be directly changed to `executeAsync`. But you can use `async`/`await` to migrate with minimal changes.

:::tip
Apidog version 2.3.24 or later(CLI version 1.2.38 or later) supports top-level await.
:::

Steps:

1. Change `execute` to `executeAsync`
2. Add `await` before function call


```js
// Before
const result = pm.execute("add.js", [3, 4]); 
pm.environment.set("result", result);
```

```js 
const result = await pm.executeAsync("add.js", [3, 4]);
pm.environment.set("result", result);
```

## Call Specified Methods in `.jar` Packages

:::tip
This feature requires Apidog version to be 2.1.39 or later. It only supports calling jars with reflection, not jars like Spring Boot using internal runtime reflection.
:::

By default, calling a jar will invoke the main method in the Main class. If `options.className` is specified, it will override the default behavior and call the specified method in the jar instead.

Calling specified methods in jars is different from other external programs. Apidog will use a built-in executor to find the method in the jar by reflection and call it. If the called method has a return value, it will be used as the final return value after converting to string. Otherwise, it works the same as other calls, using stdout content as return value.

For example:

```js
await pm.executeAsync('./scripts/jar-1.0-SNAPSHOT.jar', ['hello', 'world'], {
    className: 'com.apidog.Test', 
    method: 'combine',
    paramTypes: ['String', 'String']
})
```

The actually executed command is: 

```bash
java -jar "<app-dist>/assets/JarExecuter-1.1.0-jar-with-dependencies.jar" ./scripts/jar-1.0-SNAPSHOT.jar "com.apidog.Test.combine(String,String)" "\"hello\"" "\"world\""
```

Where `<app-dist>/assets/JarExecuter-1.1.0-jar-with-dependencies.jar` is the built-in executor, responsible for finding the method `com.apidog.Test.combine(String,String)` in the user program `./scripts/jar-1.0-SNAPSHOT.jar` through reflection, and calling it with parameters (JSON string) `"hello"` and `"world"`.

:::tip
`paramTypes` is optional. If not specified, types will be inferred automatically based on parameters. Integers are inferred as `"int"`, floats as `"double"`, booleans as `"boolean"`, strings as `"String"`, arrays are inferred based on the first element, e.g. `[3]` is inferred as `"int[]"`, `[3.14]` as `"double[]"`, etc.
If the inferred types do not match the actual parameter types of the called method, `paramTypes` needs to be specified manually.
Supported values in `paramTypes` array: `"Number"`、`"int"`、`"Integer"`、`"long"`、`"Long"`、`"short"`、`"Short"`、`"float"`、`"Float"`、`"double"`、`"Double"`、`"boolean"`、`"Boolean"`、`"String"`、`"Number[]"`、`"int[]"`、`"Integer[]"`、`"long[]"`、`"Long[]"`、`"short[]"`、`"Short[]"`、`"float[]"`、`"Float[]"`、`"double[]"`、`"Double[]"`、`"boolean[]"`、`"Boolean[]"`、`"String[]"`

So the `paramTypes` in the example above can be omitted:

```js 
await pm.executeAsync('./scripts/jar-1.0-SNAPSHOT.jar', ['hello', 'world'], {
    className: 'com.apidog.Test',
    method: 'combine' 
})
```

:::

## Examples

### 1. PHP Program

   Script:

   ```js
const param1 = { a: 1, b: 2 }
const resultString = await pm.executeAsync('test.php', [JSON.stringify(param1)])
const result = JSON.parse(resultString)
console.log('Result:', result) // Result: { a: 2, b: 4 }
   ```

   `test.php`:

   ```php
<?php
$param = json_decode($argv[1]);
$result = [];
foreach($param as $key=>$value)
{
    $result[$key] = $value * 2;
}
echo json_encode($result);
   ```

### 2. Jar Program

   Script:

   ```js
const result = await pm.executeAsync('com.apidog.utils.jar', [3, 5], {
   className: 'com.apidog.utils.Utils',  
   method: 'add',
   paramTypes: ['Integer', 'Integer']
})
console.log('Result:', result) // Result: 8
   ```

   com.apidog.utils.jar:

   ```java
   package com.apidog.utils;

   public class Utils {
       public Integer add(Integer a, Integer b) {
           return a + b;
       }
   };
   ```

## Common Issues

### 1. Some programs require project config files and will error if missing

**Rust and Go:**

Rust:  

```
could not find `Cargo.toml` in `<...>/ExternalPrograms` or any parent directory
```

Go: 

```
go.mod file not found in current directory or any parent directory; see 'go help modules'
```

Solution: Use pm.executeAsync and specify `cwd`.

### 2. MacOS has built-in Python 3 but no Python 2

Use pm.executeAsync and set `command` to `"python3"`.

### 3. Command xxx not found

Install corresponding program and add necessary directories to system PATH. See [docs](https://docs.apidog.com/installing-java-environment-645607m0.md) for Java installation.

### 4. Calling external scripts prints garbled on some Windows systems 

Set `windowsEncoding` to `'utf-8'`

```js 
var result = pm.execute(`hello.go`, [], { windowsEncoding: 'utf-8' })
```
