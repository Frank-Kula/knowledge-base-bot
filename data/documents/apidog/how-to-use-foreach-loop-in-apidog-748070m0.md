# How to use foreach loop in Apidog?

When you have an array containing multiple elements (a list of specific content or a list obtained from previous steps), and you need to perform the same operation on each item in the list (e.g., first obtaining a list of products, and then adding each product in the list to the shopping cart), you need to use a ForEach loop.

In a ForEach loop, the operations inside the loop will be executed for each element in the array. 

The difference from a For loop is that you don't need to worry about the number of iterations; you only need to focus on the content of the loop array.

- **Setting the loop array**: In a ForEach loop, you need to set an array as the loop object. You can use a variable or manually enter an array, such as `["a","b","c"]`.

- **Adding requests**: Within a ForEach loop, you can add one or more requests, or add other loops or conditional branches, etc.

- **Break If condition and On Error handling**: You can add Break if and On error to the ForEach loop, consistent with the for loop mentioned above.

<p style="text-align:center">
    <img src="https://api.apidog.com/api/v1/projects/544525/resources/343000/image-preview" style="width:640px" />
</p>

:::tip
In the ForEach Loop's advanced setting, you can can also customize exception handling options for Break If and On Error. For more information, see Judgment Rules.
:::

### ForEach usage example

Consider two endpoints: one for retrieving a list of pet information and another for fetching details of a single pet. If you need to fetch the details of a pet recently added to the list, you can set up this scenario using a ForEach loop in your automated testing.

1. The first step outside the ForEach loop would be to request the pet information list endpoint to retrieve the actual list data. Typically, the response of this interface contains an array with basic information about multiple pets, such as pet ID and name.
2. Set up a ForEach loop with the source array being a subset of the pet array from the response of the previous step. 
3. Within the loop, set up a request to the "Get Pet Information" endpoint and use the element value from the ForEach loop to populate the ID parameter in this request. 

### Using loop element in requests
 
The current element/index of the loop can be used as a local variable within requests to dynamically adjust parameters or request bodies. To utilize this:

<Steps>
  <Step>
Add a ForEach loop and include a request within the loop.
    </Step>
  <Step>
Click the <Icon icon="ph-bold-magic-wand"/> **magic wand** icon in the request param and select “Retrieve pre-step data.”
<p style="text-align:center">
    <img src="https://api.apidog.com/api/v1/projects/544525/resources/342997/image-preview" style="width:300px" />
</p>
    </Step>
  <Step>
Choose the loop option, usually labeled as “Loop each element in `{{array}}`.”
<p style="text-align:center">
    <img src="https://api.apidog.com/api/v1/projects/544525/resources/343001/image-preview" style="width:300px" />
</p>
    </Step>
  <Step>
Select “Current loop element.” You can utilize JSONPath to extract properties of the element.
<p style="text-align:center">
    <img src="https://api.apidog.com/api/v1/projects/544525/resources/343002/image-preview" style="width:300px" />
</p>
    </Step>
  <Step>
You'll obtain a dynamic variable like `{{$.17.element}}`. Click "Insert", and it will be replaced at runtime with the current loop's element, which is an element of the loop array.
    <p style="text-align:center">
    <img src="https://api.apidog.com/api/v1/projects/544525/resources/343003/image-preview" style="width:400px" />
</p>  
    </Step>
</Steps>

:::tip
**Current Loop Element**: The system automatically extracts elements from the array specified in the ForEach loop and stores them in the designated variable. At the start of each iteration, this variable is updated with the current element's value from the array. If the element is an object, you can use JSONPath to extract a specific subfield, such as `{{$.1.element.data.name}}`.

**Current Loop Index**: The index of the current loop is stored in this variable. It starts at 0 and increments by 1 at the beginning of each subsequent iteration, reflecting the current index.
:::
