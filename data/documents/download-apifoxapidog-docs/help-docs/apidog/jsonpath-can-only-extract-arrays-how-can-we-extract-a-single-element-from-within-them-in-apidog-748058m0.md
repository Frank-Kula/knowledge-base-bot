# JSONPath can only extract arrays. How can we extract a single element from within them in Apidog?

JSON is the most commonly used response data format, and JSONPath is a widely used syntax for data extraction within JSON structures. Apidog provides a visual JSONPath Extraction tool to simplify the process of crafting JSONPath expressions. Here is a guide on how to use this tool effectively:


<Steps>
  <Step>
Click on the <Icon icon="ph-bold-arrow-square-out"/> icon located to the right of the JSONPath input box.

![image.png](https://api.apidog.com/api/v1/projects/544525/resources/342819/image-preview)
      
  </Step>
  <Step>
In the JSONPath Extraction tool that pops up, the left section displays the JSON response. You can input your JSONPath expression in the JSONPath Expression field at the top right. The results section at the bottom will dynamically extract the corresponding data based on your expression.

![image.png](https://api.apidog.com/api/v1/projects/544525/resources/342817/image-preview)
  </Step>
  <Step>
If your JSONPath expression includes wildcard characters (*) or similar elements that may result in extracting multiple values, the results will be enclosed within square brackets ([]). If you wish to extract a specific value and **avoid the brackets**, you can toggle the "**Continue extracting**" switch and specify the index of the value you want to extract.
  </Step>
</Steps>


