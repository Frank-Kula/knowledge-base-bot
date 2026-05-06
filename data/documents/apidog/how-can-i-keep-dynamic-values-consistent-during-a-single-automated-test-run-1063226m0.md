# How can I keep dynamic values consistent during a single automated test run?

Dynamic expressions (such as `{{$person.fullName}}`) generate a new value each time they are called. If you directly assign such expressions to variables multiple times within a test flow, it may lead to inconsistent data across steps.

**Recommended approach:**

Generate the dynamic value once, store it in a variable, and reference that variable throughout the test. Variables are evaluated only once when assigned, ensuring consistency across the entire test run.


**Steps:**

1.  Pre-generate and store the variable

Add the following script to the pre-script of your test flow:


```js
// Generate a value from the dynamic expression once
let realValueString = await pm.variables.replaceInAsync("{{$person.fullName}}");
pm.environment.set("fixedPerson", realValueString); // Save to environment variable

```


2.  Use the stored variable instead of the expression

In subsequent test steps, use `{{fixedPerson}}` to ensure the same value is used throughout the test process.
