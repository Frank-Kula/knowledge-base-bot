# Data-Driven Testing

Apidog supports data-driven testing, allowing you to import test data sets in CSV or JSON format and use them within your test requests.

## Getting Started

<Video src="https://www.youtube.com/watch?v=JfrqbV5OVbc"></Video>

<Steps>
  <Step>
Create a test scenario and add the necessary test steps.
  </Step>
  <Step>
Prepare the test data. A set of test data is a two-dimensional table, where each column represents a variable, and each row contains a set of values for those fields, to be used for a single test scenario iteration. For example, you can prepare a CSV file with the following data.
| Dataset Name | petType | petName  | age | price |
|--------------|---------|----------|-----|-------|
| Pet-1        | Dog     | Buddy    | 3   | 300   |
| Pet-2        | Cat     | Whiskers | 2   | 150   |
| Pet-3        | Bird    | Tweety   | 1   | 50    |
| Pet-4        | Rabbit  | Thumper  | 4   | 80    |
| Pet-5        | Dog     | Max      | 5   | 250   |
    </Step>
    <Step>
Switch to "Test Data" tab, click "New" to add a set of test data.
<Background>
<img src="https://api.apidog.com/api/v1/projects/544525/resources/343127/image-preview" style="width:640px" />
</Background>

    </Step>
    <Step>
Import the test data, add a name, and save it.
<Background>
<img src="https://api.apidog.com/api/v1/projects/544525/resources/343125/image-preview" style="width:640px" />
</Background>
  </Step>
  <Step>
Add the test data variables to your requests. The names of the test data variables should match the column names in the two-dimensional table.
<Background>
<img src="https://api.apidog.com/api/v1/projects/544525/resources/343128/image-preview" style="width:640px" />
</Background>
  </Step>
  <Step>
When running the test, select the desired data set.
<Background>
<img src="https://api.apidog.com/api/v1/projects/544525/resources/343130/image-preview" style="width:340px" />
</Background>
  </Step>
     <Step>
 
    click Run, and choose the dataset you want to use.
<Background>
<img src="https://api.apidog.com/api/v1/projects/544525/resources/343131/image-preview" style="width:640px" />
</Background>
  </Step>

         <Step>
The test report will show the results for each dataset.
      <Background>
<img src="https://api.apidog.com/api/v1/projects/544525/resources/343132/image-preview" style="width:640px" />
</Background>
  </Step>
</Steps>

## Test data

Each test scenario can maintain multiple sets of test data, and you can choose which data set to use when running the scenario.

The test data is stored in the cloud and synchronized across team members.

Test data can be configured per environment, so when you switch to a different environment, the corresponding test data set will be used.

For example, you can maintain a set of pet data for both the test environment and the develop environment, using the same variable names. When you switch environments, the variable values from the corresponding environment will be used.

<Background>
![image.png](https://api.apidog.com/api/v1/projects/544525/resources/343136/image-preview)
</Background>

### Editing test data

You can import/export test data in CSV or JSON format, or you can manually add and edit the test data.

<Background>
![image.png](https://api.apidog.com/api/v1/projects/544525/resources/343134/image-preview)
</Background>

### Using test data

You can use `{{variable}}` to insert test data variables into the request parameters, headers, body, and other locations. When running the test scenario, these variables will be replaced with the corresponding test data values.

The variable name may be the same as other variables. When there are duplicate variable names, the order of precedence is: Local variable > Test data variable > Environment variable > Global variable.

### Using test data in scripts

You can access the variables in scripts as shown below:

`pm.iterationData.has(variableName:String)`: function → Boolean: Check whether a test variable exists.
`pm.iterationData.get(variableName:String)`: function → *: get a test variable.
`pm.iterationData.replaceIn(variableName:String)`: function: replace dynamic variables in a string with their actual values.
`pm.iterationData.toObject()`: function → Object: get all local variables as objects.

## FAQ
**Q: How to handle garbled characters when importing test data?**

A: On Windows, Excel will automatically save CSV files using GBK encoding by default. This can cause garbled characters when viewing the CSV in other software. Also, old Excel versions (e.g. Excel 2016) typically won't save the BOM (byte order mark) when saving CSV as UTF-8, which can also lead to garbled characters. 

Solutions:

- On Windows, resave the CSV as `UTF-8` encoding.  
- On macOS, run `iconv -f GBK -t UTF-8 xxx.csv > utf-8.csv` to convert encoding.


