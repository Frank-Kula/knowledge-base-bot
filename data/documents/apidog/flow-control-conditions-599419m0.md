# Flow Control Conditions

You can add flow control conditions (loops, conditions, waits, grouping, etc.) to your testing scenarios. This enhances the utilization of more complex testing scenarios/process configurations, ultimately resolving the testing challenges of intricate scenarios through automated testing features.

<Background>
![Flow control conditions](https://api.apidog.com/api/v1/projects/544525/resources/342966/image-preview)
</Background>

## For Loops

When you need to send a single request multiple times consecutively, using a `for` loop is an efficient approach. Here's how to effectively use for loops in your Apidog test scenarios:

<Background>
<img src="https://api.apidog.com/api/v1/projects/544525/resources/342994/image-preview" style="width:640px" />
</Background>

- **Setting the iterations count**: Decide how many times the loop should run. This can be a fixed number or a `{{variable}}`.

- **Adding requests**: Within a for loop, you can include one or more requests, as well as other loops or conditional branches. This flexibility allows for complex test scenarios where multiple actions need to be tested in sequence.
- **Break If condition**: You can add a `Break if` condition to a for loop. This will immediately terminate the loop if the condition is satisfied. You can drag and adjust the position of `Break if` or even add multiple `Break if` conditions to handle different scenarios.
- **On Error handling**: Manage errors by adding `On Error` conditions to the loop. If an error occurs, specified actions will be triggered:
    - **Ignore**: The loop continues with the next request.
    - **Continue**: Skips the remaining requests in the current cycle and moves to the next iteration.
    - **Break execution**: Stops the loop and proceeds with subsequent requests outside the loop.
    - **End execution**: Completely halts the entire test scenario.
  The `On Error` condition is fixed at the start of the loop and cannot be moved.

### Using Loop Index in Requests
 
The current index of the loop can be used as a local variable within requests to dynamically adjust parameters or request bodies. To utilize this:

<Steps>
  <Step>
Add a for loop and include a request within the loop.
    </Step>
  <Step>
Click the magic wand icon `🪄` in the request param and select "Retrieve pre-step data."
<Background>
<img src="https://api.apidog.com/api/v1/projects/544525/resources/342997/image-preview" style="width:300px" />
</Background>
      
:::tip[]
- The feature of "Retrieve pre-step data" is only available in the "Tests" module and not in the "APIs" module. 
- When using "Retrieve pre-step data", the value can only be obtained when the entire test scenario is run together; it cannot be accessed when running individual steps.
:::
    </Step>
  <Step>
Choose the loop option, usually labeled as "Loop n times."
<Background>
<img src="https://api.apidog.com/api/v1/projects/544525/resources/342998/image-preview" style="width:300px" />
</Background>
    </Step>
  <Step>
Select "Current loop index."
<Background>
<img src="https://api.apidog.com/api/v1/projects/544525/resources/342993/image-preview" style="width:300px" />
</Background>

    </Step>
  <Step>
You'll obtain a dynamic variable like `{{$.5.index}}`. Click "Insert", and it will be replaced at runtime with the current loop's index like `0` or `5`.
<Background>
<img src="https://api.apidog.com/api/v1/projects/544525/resources/342999/image-preview" style="width:400px" />
</Background> 

:::tip[]
The index of loop always starts from `0`.
:::
  </Step>
</Steps>

## ForEach Loops

When you have an array containing multiple elements (a list of specific content or a list obtained from previous steps), and you need to perform the same operation on each item in the list (e.g., first obtaining a list of products, and then adding each product in the list to the shopping cart), you need to use a ForEach loop.

In a ForEach loop, the operations inside the loop will be executed for each element in the array. 

The difference from a For loop is that you don't need to worry about the number of iterations; you only need to focus on the content of the loop array.

- **Setting the loop array**: In a ForEach loop, you need to set an array as the loop object. You can use a variable or manually enter an array, such as `["a","b","c"]`.

- **Adding requests**: Within a ForEach loop, you can add one or more requests, or add other loops or conditional branches, etc.

- **Break If condition and On Error handling**: You can add Break if and On error to the ForEach loop, consistent with the for loop mentioned above.

<Background>
<img src="https://api.apidog.com/api/v1/projects/544525/resources/343000/image-preview" style="width:640px" />
</Background>

:::tip
In the ForEach Loop's advanced setting, you can can also customize exception handling options for Break If and On Error. For more information, see Judgment Rules.
:::

### ForEach Usage Example

Consider two endpoints: one for retrieving a list of pet information and another for fetching details of a single pet. If you need to fetch the details of a pet recently added to the list, you can set up this scenario using a ForEach loop in your automated testing.

1. The first step outside the ForEach loop would be to request the pet information list endpoint to retrieve the actual list data. Typically, the response of this interface contains an array with basic information about multiple pets, such as pet ID and name.
2. Set up a ForEach loop with the source array being a subset of the pet array from the response of the previous step. 
3. Within the loop, set up a request to the "Get Pet Information" endpoint and use the element value from the ForEach loop to populate the ID parameter in this request. 

### Using Loop Element in Requests
 
The current element/index of the loop can be used as a local variable within requests to dynamically adjust parameters or request bodies. To utilize this:

<Steps>
  <Step>
Add a ForEach loop and include a request within the loop.
    </Step>
  <Step>
Click the <Icon icon="ph-bold-magic-wand"/> **magic wand** icon in the request param and select "Retrieve pre-step data."
<Background>
<img src="https://api.apidog.com/api/v1/projects/544525/resources/342997/image-preview" style="width:300px" />
</Background>
    </Step>
  <Step>
Choose the loop option, usually labeled as "Loop each element in `{{array}}`."
<Background>
<img src="https://api.apidog.com/api/v1/projects/544525/resources/343001/image-preview" style="width:300px" />
</Background>
    </Step>
  <Step>
Select "Current loop element." You can utilize JSONPath to extract properties of the element.
<Background>
<img src="https://api.apidog.com/api/v1/projects/544525/resources/343002/image-preview" style="width:300px" />
</Background>
    </Step>
  <Step>
You'll obtain a dynamic variable like `{{$.17.element}}`. Click "Insert", and it will be replaced at runtime with the current loop's element, which is an element of the loop array.
<Background>
<img src="https://api.apidog.com/api/v1/projects/544525/resources/343003/image-preview" style="width:400px" />
</Background> 
    </Step>
</Steps>

:::tip
**Current Loop Element**: The system automatically extracts elements from the array specified in the ForEach loop and stores them in the designated variable. At the start of each iteration, this variable is updated with the current element's value from the array. If the element is an object, you can use JSONPath to extract a specific subfield, such as `{{$.1.element.data.name}}`.

**Current Loop Index**: The index of the current loop is stored in this variable. It starts at 0 and increments by 1 at the beginning of each subsequent iteration, reflecting the current index.
:::

## If

When you need to send different requests based on different scenarios, you can use an If statement to add conditional branches. When the specified conditions are met, the corresponding step will be executed; otherwise, it will be skipped. For more specific details, please refer to Judgment Rules.

<Background>
<img src="https://api.apidog.com/api/v1/projects/544525/resources/343027/image-preview" style="width:640px" />
</Background>

- **Setting If statement**: If statement supports various conditions such as equal to, not equal to, contains, not contains, etc. Both constants and variables can be used on either side of the condition.
- **Add requests**: Multiple requests can be added within a conditional branch, as well as other loops or conditional branches.
- **Execute conditional branches**: If the conditions set in the configuration are met, the test step will be executed, otherwise, it will be skipped.
- **Else statement**: An Else statement can be added within a conditional branch to handle scenarios when the If condition is not met.

### If Usage Example

A pet shop owner, based on the sales status of pets from the previous day, needs to change the sales status of a pet to "Sold" if it was sold. Otherwise (else), they need to check the list of pets still for sale.

1. Click the "Add Step" button at the bottom and select "Conditional Branching."
2. Enter the variable `saleStatus` obtained from the API request response into the input box after "If" and select the condition "equals." Finally, input `true` as the comparison value. 
3. Hover over the conditional branching operation to see the " + Else" option. Click it to add the step "List of Pets for Sale" (in case the condition is not met, i.e., to query the list of pets still for sale).

## Judgment Rules

When using the `If` statement in a test scenario, you can define conditional rules to control test execution. If the conditions are met, the corresponding step will run; otherwise, it will be skipped. Likewise, in the `Break If` settings for `ForEach` and `For` loops, you can set judgment rules to control the execution flow more flexibly.

| Rule | Description |
|------|-------------|
| **Equals** | Checks if two values are equal. |
| **Does not equal** | Checks if two values are not equal. |
| **Exists** | Checks if a field or variable exists. |
| **Does not exist** | Checks if a field or variable does not exist. |
| **Less than** | Checks if one value is less than another. |
| **Less than or equal** | Checks if one value is less than or equal to another. |
| **Greater than** | Checks if one value is greater than another. |
| **Greater than or equal** | Checks if one value is greater than or equal to another. |
| **Matches with Regex** | Checks if a string matches the specified regular expression. |
| **Contains** | Checks if a string or array contains the specified value. |
| **Does not contain** | Checks if a string or array does not contain the specified value. |
| **Is empty** | Checks if a field, array, or variable is empty. |
| **Is not Empty** | Checks if a field, array, or variable is not empty. |
| **In List** | Checks if a value belongs to a specified List. |
| **Not in List** | Checks if a value does not belong to a specified List. |

When performing conditional checks (such as greater than, greater than or equal, equals, or not equals), if the values being compared are integers or strings, the system will **automatically convert strings to numbers** for accurate comparison. For example, if you compare a string `"18"` with the number `18`, the system will convert the string `"18"` to the number `18` before comparing.

### Equals

Checks if two values are equal. If they are equal, the condition is met and the test step will be executed; otherwise, it will be skipped.

- **Example**:  
  - **Scenario**: Check if user age extracted from pre-step is equal to 18. 
  - **Condition Example**: `{{$.5.response.body.data.age}} Equals 18`
  - **Actual Execution Effect**: If the extracted age value from pre-step is 18 (the string will be automatically converted to a number), the step will be executed, such as displaying specific information or performing certain actions.

### Does not equal

Checks if two values are not equal. If they are not equal, the condition is met and the test step will be executed; otherwise, it will be skipped.

- **Example**:  
  - **Scenario**: Check if the order status extracted from pre-step is not equal to "Paid".  
  - **Condition Example**: `{{$.4.response.body.data.status}} Does not equal Paid`  
  - **Actual Execution Effect**: If the order status extracted from pre-step is another value (such as "Pending" or "Shipped"), the step will be executed.

### Exists

Checks if a certain field or variable exists. If it exists, the condition is met and the step will be executed; otherwise, it will be skipped.

- **Example**:  
  - **Scenario**: Check if the `email` field exists in the user data extracted from pre-step.  
  - **Condition Example**: `{{$.3.response.body.data.email}} Exists`  
  - **Actual Execution Effect**: If the `email` field is present in the user data extracted from pre-step, the step will be executed.

### Does not exist

Checks if a certain field or variable does not exist. If it does not exist, the condition is met and the step will be executed; otherwise, it will be skipped.

- **Example**:  
  - **Scenario**: Check if the `phone` field does not exist in the user data extracted from pre-step.  
  - **Condition Example**: `{{$.2.response.body.data.phone}} Does not exist`  
  - **Actual Execution Effect**: If the `phone` field is absent in the user data extracted from pre-step, the step will be executed.

### Less Than

Checks if one value is less than another. If it is, the condition is met and the step will be executed; otherwise, it will be skipped.

- **Example**:  
  - **Scenario**: Check if the product stock extracted from pre-step is less than 10.  
  - **Condition Example**: `{{$.1.response.body.data.stock}} Less Than 10`  
  - **Actual Execution Effect**: If the stock value extracted from the pre-step is 8, the condition is met and the step will be executed.

### Less than or equal

Checks if one value is less than or equal to another. If it is, the condition is met and the step will be executed; otherwise, it will be skipped.

- **Example**:  
  - **Scenario**: Check if the age extracted from pre-step is less than or equal to 12.  
  - **Condition Example**: `{{$.2.response.body.data.age}} Less than or equal 12`  
  - **Actual Execution Effect**: If the age value extracted from pre-step is 10, the condition is met and the step will be executed.

### Greater than

Checks if one value is greater than another. If it is, the condition is met and the step will be executed; otherwise, it will be skipped.

- **Example**:  
  - **Scenario**: Check if the order amount extracted from pre-step is greater than 1000.  
  - **Condition Example**: `{{$.1.response.body.data.amount}} Greater than 1000`  
  - **Actual Execution Effect**: If the order amount value extracted from pre-step is 1105, the condition is met and the step will be executed.

### Greater than or equal

Checks if one value is greater than or equal to another. If it is, the condition is met and the step will be executed; otherwise, it will be skipped.

- **Example**:  
  - **Scenario**: Check if the user points extracted from pre-step are greater than or equal to 500.  
  - **Condition Example**: `{{$.3.response.body.data.points}} Greater than or equal 500`  
  - **Actual Execution Effect**: If the points' value extracted from pre-step is 600, the condition is met and the step will be executed.

### Matches with Regex

Checks if a string matches a specified regular expression. If it matches, the condition is met and the step will be executed; otherwise, it will be skipped.

- **Example**:  
  - **Scenario**: Check if the email format extracted from pre-step is correct.  
  - **Condition Example**: `{{$.2.response.body.data.email}} Matches with Regex /^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$/i`  
  - **Actual Execution Effect**: If the extracted email format from pre-step matches the regular expression (for example, `test@gmail.com`), the step will be executed.

:::tip
Regular expressions should be written using "literal" syntax, where the pattern is enclosed in /, with optional modifiers (e.g., g for global matching, i for case-insensitive) appended at the end. For more information on writing regular expressions, you can refer to the [MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions).
:::

### Contains

Checks if a string or array contains a specified value. If it does, the condition is met and the step will be executed; otherwise, it will be skipped.

- **Example**:  
  - **Scenario**: Check if the user role list extracted from pre-step contains the "admin" role.  
  - **Condition Example**: `{{$.3.response.body.data.roles}} Contains admin`  
  - **Actual Execution Effect**: If the extracted role list from pre-step contains "admin", the step will be executed.

### Does not contain

Checks if a string or array does not contain a specified value. If it does not, the condition is met and the step will be executed; otherwise, it will be skipped.

- **Example**:  
  - **Scenario**: Check if the user's shopping cart extracted from pre-step does not contain a certain product.  
  - **Condition Example**: `{{$.4.response.body.data.cartItems}} Does not contain productId123`  
  - **Actual Execution Effect**: If the extracted cart array from pre-step does not contain the product `productId123`, the step will be executed.

### Is empty

Checks if a field, array, or variable is empty. If it is, the condition is met and the step will be executed; otherwise, it will be skipped.

- **Example**:  
  - **Scenario**: Check if the remarks field extracted from pre-step is empty.  
  - **Condition Example**: `{{$.2.response.body.data.remarks}} Is empty`  
  - **Actual Execution Effect**: If the extracted remarks field from pre-step is empty, the step will be executed.

### Is not Empty

Checks if a field, array, or variable is not empty. If it is not empty, the condition is met and the step will be executed; otherwise, it will be skipped.

- **Example**:  
  - **Scenario**: Check if the order remarks extracted from pre-step are filled out.  
  - **Condition Example**: `{{$.1.response.body.data.orderRemarks}} Is not Empty`  
  - **Actual Execution Effect**: If the extracted order remarks from pre-step are not empty, the step will be executed.

### In List

Checks if a value belongs to a specified list. If it does, the condition is met and the step will be executed; otherwise, it will be skipped.

- **Example**:  
  - **Scenario**: Check if the product selected by the user extracted from pre-step is in the recommended product list.  
  - **Condition Example**: `{{$.3.response.body.data.productId}} In List ["prod123", "prod456", "prod789"]`  
  - **Actual Execution Effect**: If the product ID extracted from pre-step is "prod456", the step will be executed.

:::tip
In Apidog, when entering a list, each element should be entered separately and separated by pressing the Enter key.
:::

### Not in List

Checks if a value does not belong to a specified list. If it does not belong, the condition is met and the step will be executed; otherwise, it will be skipped.

- **Example**:  
  - **Scenario**: Check if the promo code entered by the user extracted from pre-step is not in the list of used promo codes.  
  - **Condition Example**: `{{$.4.response.body.data.promoCode}} Not in List ["usedCode1", "usedCode2"]`  
  - **Actual Execution Effect**: If the extracted promo code from pre-step is "newPromo", the condition is met and the step will be executed; otherwise, it will be skipped.

## Grouping

When multiple steps in the testing process are interrelated, they can be grouped together for classification. By grouping testing steps, you enhance the readability and operability of the testing scenario.

<Background>
<img src="https://api.apidog.com/api/v1/projects/544525/resources/342979/image-preview" style="width:340px" />
</Background>

## Wait

When a certain step in the testing process requires waiting for a period before execution, you can add a wait condition to resolve this.

### Wait Usage Example

Simulate a user viewing pet details and updating the browsing status of the pet information after browsing for 1000ms.

1. Click the "Add Step" button at the bottom and select "Wait."
2. Input the time to wait, 1000 (in milliseconds).


:::tip[]
When you use test flow control, the test report will not display the steps like If, for, etc., but will only show the actual requests executed, listed linearly in the order of execution.
:::

