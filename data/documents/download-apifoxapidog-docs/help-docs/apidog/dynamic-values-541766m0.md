# Dynamic Values

When you are debugging an endpoint in Apidog, you often need to fabricate a value, a name, an address, or other data points in the request parameters, request body, etc. This is where the dynamic values feature comes in handy.

Dynamic values allow you to generate a new value based on a predefined rule every time you send a request. This helps streamline the debugging process and ensures that each request contains unique data.

## Getting Started

<Steps>
  <Step>
    In an endpoint, switch to the **Run** tab.
  </Step>
  <Step>
    For the parameter you want to dynamize, delete the original value, then click the <Icon icon="ph-bold-magic-wand"/> **magic wand** icon to the right of the value. In this example, I'll select the `name` parameter.

    <Background>
    <p style="text-align:center">
        <img src="https://api.apidog.com/api/v1/projects/544525/resources/344608/image-preview" style="width:640px" />
    </p>
    </Background>
  </Step>
  <Step>
    Click on **Data generator**, and choose the dynamic value type you need, such as `Person.firstName`.

    <Background>
    <p style="text-align:center">
        <img src="https://api.apidog.com/api/v1/projects/544525/resources/344605/image-preview" style="width:640px" />
    </p>
    </Background>
  </Step>
  <Step>
    Click **Insert** to insert the dynamic value into the parameter.

    <Background>
    <p style="text-align:center">
        <img src="https://api.apidog.com/api/v1/projects/544525/resources/344606/image-preview" style="width:640px" />
    </p>
    </Background>
  </Step>
  <Step>
    Click **Send**. You can see in the **Actual request** that the actual name sent is "Jennifer".

    <Background>
    <p style="text-align:center">
        <img src="https://api.apidog.com/api/v1/projects/544525/resources/344607/image-preview" style="width:640px" />
    </p>
    </Background>
  </Step>
  <Step>
    Send the request again, and a new first name will be generated dynamically.
  </Step>
</Steps>

## Using Dynamic Values in JSON Body

If you need to post a JSON body, and some values in the JSON need to be dynamically generated, you can also use dynamic values.

<Steps>
  <Step>
    Find a POST endpoint with a JSON body, and switch to the **Run** tab.
  </Step>
  <Step>
    In the JSON body, click **Generate automatically** -> **Generate field names**, and you will get the property names defined in the spec.

    <Background>
    <p style="text-align:center">
        <img src="https://api.apidog.com/api/v1/projects/544525/resources/344609/image-preview" style="width:640px" />
    </p>
    </Background>
  </Step>
  <Step>
    Position the cursor in the correct place, click <Icon icon="ph-bold-magic-wand"/> **Insert dynamic value**, and select **Data Generator**.

    <Background>
    <p style="text-align:center">
        <img src="https://api.apidog.com/api/v1/projects/544525/resources/344610/image-preview" style="width:640px" />
    </p>
    </Background>
  </Step>
  <Step>
    Choose the appropriate data type and click **Insert**.
  </Step>
  <Step>
    Add values for all the fields.
  </Step>
  <Step>
    Click **Send**. You can see the actual JSON body sent in the **Actual request** section.

    <Background>
    <p style="text-align:center">
        <img src="https://api.apidog.com/api/v1/projects/544525/resources/344620/image-preview" style="width:640px" />
    </p>
    </Background>
  </Step>
  <Step>
    If you send the request again, the dynamic values will generate a new JSON body.
  </Step>
</Steps>

## Using Dynamic Values in Custom Custom Expression

If you need to customize a string of information and there are some values in the information that need to be dynamically generated, you can also click on Custom expression and enter the dynamic value expression.

<Steps>
  <Step>
    Click on the dynamic expression to open the input box.

    <Background>
    <p style="text-align:center">
        <img src="https://api.apidog.com/api/v1/projects/544525/resources/344899/image-preview" style="width:640px" />
    </p>
    </Background>
  </Step>
  <Step>
    Generate expected content by inputting dynamic value expressions through methods such as concatenation. You can preview the generated information in real-time below.

    <Background>
    <p style="text-align:center">
        <img src="https://api.apidog.com/api/v1/projects/544525/resources/344902/image-preview" style="width:640px" />
    </p>
    </Background>
  </Step>
  <Step>
    Click on **Insert**. You can see custom expressions in the parameter values section.

    <Background>
    <p style="text-align:center">
        <img src="https://api.apidog.com/api/v1/projects/544525/resources/344901/image-preview" style="width:640px" />
    </p>
    </Background>
  </Step>
</Steps>

Here are some common custom dynamic value examples. You can also click [Dynamic Values Modules](https://docs.apidog.com/dynamic-values-modules-1938252f0.md) to see more dynamic value methods.

| Desired Custom Content | Custom Expression | Example Return Value | Method Concatenation and Meaning |
| :--- | :--- | :--- | :--- |
| Random username with timestamp | `{{$internet.userName}}_{{$date.now}}` | "Kattie_Rice64_2024-09-04T05:51:42.413Z" | Use `{{$internet.userName}}` to generate a random username, use `{{$date.now}}` to get the current time, and concatenate them using template literals. |
| Random email address with company domain | `{{$person.firstName}}.{{$person.lastName}}@{{$company.name | lower}}.com` | "Kole.Haag@schmidt-schoen.com" | Use `{{$person.firstName}}`, `{{$person.lastName}}` to generate a random name, use `{{$company.name | lower}}` to generate a company name, convert it to lowercase, and concatenate them to form an email address. |
| Random address with street number and apartment number | `{{$location.buildingNumber}} {{$location.street}}, Apt. {{$number.int(min=1,max=1000)}}, {{$location.city}}, {{$location.state(abbreviated=true)}} {{$location.zipCode}}` | "723 Klein Inlet, Apt. 814, North Myron, DE 67605" | Use multiple methods to generate a detailed address, including street number, street name, apartment number, city, state, and zip code. |
| Random company name with industry and company type | `{{$company.buzzAdjective}} {{$company.buzzNoun}} {{$company.name}}` | "web-enabled architectures Fay Inc" | Use the `company` method to generate a company name with industry description and company type. |
| Random date within the past year | `{{$date.past(years=1)}}` | "2023-10-24T09:25:24.109Z" | Use the `{{$date.past(years=1)}}` method to generate a random date within the past year. |
| Random price with currency symbol | `{{$finance.currencySymbol}}{{$commerce.price}}` | "KM12.89" | Use `{{$finance.currencySymbol}}` to generate a random currency symbol, use `{{$commerce.price}}` to generate a random price, and concatenate them. |
| Random product description | `{{$commerce.productAdjective}} {{$commerce.productMaterial}} {{$commerce.product}} - {{$lorem.sentences(min=2,max=4)}}` | "Small Wooden Pizza - Thema copiose dens adinventitias a. Causa uxor terreo defleo vitiosus animi. Ademptio possimus decet considero absorbeo sursum rem circumvenio antiquus curatio. Adipisci addo tredecim carbo." | Use `{{$commerce.productAdjective}}` and `{{$lorem.sentences(min=2,max=4)}}` methods to generate text containing product features and descriptions. |
| Random sentence with hashtag | `#{{$lorem.slug(min=1,max=3)}} {{$lorem.sentence(min=1,max=3)}}` | "#provident-quidem-tempore Vita comprehendo id." | Use `{{$lorem.slug(min=1,max=3)}}` to generate a random hashtag and concatenate it before the sentence. |
| Random IP address with port number | `{{$internet.ipv4}}::{{$number.int(min=1024,max=65535)}}` | "246.222.133.63::56332" | Use `{{$internet.ipv4}}` to generate a random IP address, use `{{$number.int(min=1024,max=65535)}}` to generate a port number, and concatenate them. |
| Random URL with query parameters | `{{$internet.url}}?{{$lorem.slug}}={{$lorem.word}}` | "https://nippy-bob.name/?nemo-provident-clementia=blandior" | Use `{{$internet.url}}`, `{{$lorem.slug}}`, and `{{$lorem.word}}` to generate a random URL with query parameters. |
| Random file path | `/path/to/{{$lorem.slug}}/{{$system.fileName}}` | "/path/to/caritas-solio-vilicus/across.img" | Use `{{$lorem.slug}}`, `{{$system.fileName}}`, and string concatenation to generate a random file path. |
| Random database table name | `table_{{$string.alphanumeric(length=5)|lower}}` | "table_brxlr" | Use `{{$string.alphanumeric(length=5)|lower}}` to generate a random string and concatenate it to form a database table name. |
| Random HTML code snippet | `<p>{{$lorem.sentence}} <a href="{{$internet.url}}">{{$lorem.word}}</a></p>` | `<p>Calamitas velociter una succurro depopulo. <a href="https://feline-king.name/">comminor</a></p>` | Use `{{$lorem.sentence}}` and `{{$internet.url}}` to generate a random HTML code snippet containing a link. |
| Random HTTP request header | `{ "User-Agent": {{$internet.userAgent}}, "Referer": {{$internet.url}} }` | `{ "User-Agent": Opera/13.25 (Macintosh; Intel Mac OS X 10.7.9 U; HE Presto/2.9.171 Version/12.00), "Referer": https://queasy-dusk.info/ }` | Use `{{$internet.userAgent}}` and `{{$internet.url}}` to generate a random HTTP request header containing User-Agent and Referer. |

## Use Cases for Dynamic Variables

Dynamic variables have a wide range of applications in API testing. Here are a few typical examples:

- **Simulating Real-World Data**: You need to test how your API handles different types of data, such as usernames, addresses, or email addresses in various formats. Using dynamic variables, you can easily generate large amounts of test data that resemble real-world scenarios, improving test coverage.
- **Generating Unique Values**: In certain test scenarios, you need to ensure data uniqueness, such as generating order numbers, user IDs, or transaction IDs. Dynamic variables can generate unique values based on timestamps or random numbers, preventing data conflicts and ensuring accurate test results.
- **Streamlining Data Handling**: Instead of manually modifying data for each test run, use dynamic variables to automatically generate the required data. This saves you significant time and effort, boosting your testing efficiency.

## Insert Dynamic Value Manually

In the input field where you need to insert a dynamic variable, you can type `{{$` to trigger the dynamic variable list.

<Background>
<p style="text-align: center">
    <img src="https://api-r2.apidog.com/api/v1/projects/544525/resources/344853/image-preview" style="width: 640px" />
</p>
</Background>

You can quickly locate the desired variable using one of these methods:

- **Full Input**: Enter the complete dynamic variable name accurately, for example, `$timestamp`.
- **Fuzzy Matching**: Enter partial keywords, such as `time`, and the system will automatically filter and display matching dynamic variables.

Select the target dynamic variable to insert it into the input field.

:::tip
This method does not support directly adding parameters or functions to the dynamic variable.
:::

## Data Generator

Use the data generator, you can generate any custom data as you need.

Hover on the parameter input field and click the magic wand icon that appears to open the more powerful **Data Generator** panel.

<Background>
<p style="text-align: center">
    <img src="https://api-r2.apidog.com/api/v1/projects/544525/resources/344852/image-preview" style="width: 640px" />
</p>
</Background>

You can find the desired dynamic variable in the panel using two methods:

- **Search by Variable Type**: Quickly locate the desired variable scope by selecting a dynamic variable type, such as "Date", "String", "Number", etc., for higher search efficiency.

<Background>
<p style="text-align: center">
    <img src="https://api-r2.apidog.com/api/v1/projects/544525/resources/344858/image-preview" style="width: 640px" />
</p>
</Background>

- **Search by Keyword**: Enter keywords in the "Type" input box at the top, such as "time," and the system will automatically filter and display matching dynamic variables, making it easier for you to locate them quickly.

<Background>
<p style="text-align: center">
    <img src="https://api-r2.apidog.com/api/v1/projects/544525/resources/344859/image-preview" style="width: 640px" />
</p>
</Background>

Once you have selected the desired dynamic variable, you can further refine it with the following operations to meet more granular data generation needs:

- **Add Methods**: Some dynamic variables support additional methods, such as `{{$date.now}}`, which can use the `addDays` method to add days to generate data for a specific date.

<Background>
<p style="text-align: center">
    <img src="https://api-r2.apidog.com/api/v1/projects/544525/resources/344860/image-preview" style="width: 640px" />
</p>
</Background>

- **Add Processing Functions**: All dynamic variable results can be processed with functions, for example, using the `md5` function to encrypt a string and generate test data that meets security requirements.

<Background>
<p style="text-align: center">
    <img src="https://api-r2.apidog.com/api/v1/projects/544525/resources/344861/image-preview" style="width: 640px" />
</p>
</Background>

The **Expression** area clearly displays your currently selected dynamic variables, methods, and functions, making it easy for you to check and modify them.

The **Preview** area displays sample data generated by the dynamic variable in real-time. Click the **Refresh** button at the end of the **Preview** area to generate new sample data, allowing you to easily view the effects of data generation.

Click on the sample data in the **Preview** area to automatically copy the content, which is convenient for you to paste where it is needed.

## Constant

You can use **Constant** to wrap a piece of static text in the **Dynamic Value** syntax, allowing you to add processing functions afterward. Common use cases include applying **MD5 hashing**, **Base64 encoding**, or **changing letter case**.

When using a constant, enter the original value and manually add the required processing functions in the syntax. The system will automatically handle the encryption or conversion during execution.

<Background>
<img src="https://api.apidog.com/api/v1/projects/544525/resources/363371/image-preview" style="width: 360px;" />
</Background>

If the value is purely static and does not require any processing, you can enter it directly as plain text without using Constant.

## Setting the Data Language/Country

Apidog's dynamic variables support generating sample data in different languages to meet your testing needs in multilingual environments. Here's how:

1. Open the **Data Generator** panel.
2. For dynamic variable types other than date and time, click the settings button in the upper right corner of the dynamic variable and select the target language.

<Background>
<p style="text-align: center">
    <img src="https://api-r2.apidog.com/api/v1/projects/544525/resources/344862/image-preview" style="width: 640px" />
</p>
</Background>

3. For date and time dynamic variable types, you can specify the language and format using the `format` and `locale` methods.

<Background>
<p style="text-align: center">
    <img src="https://api-r2.apidog.com/api/v1/projects/544525/resources/344863/image-preview" style="width: 640px" />
</p>
</Background>

## Powerful Date Operations and Formatting

Apidog goes beyond providing abundant date and time dynamic values, it is committed to simplifying your development process. Here are some of the features you can easily achieve:

- **Flexible Time Adjustment**: Using the `add` method, you can easily add or subtract time units based on the current time. For example, `{{$date.now|addHours(-3)}}` will return the date 3 hours earlier than the current time.

<Background>
<p style="text-align: center">
    <img src="https://api-r2.apidog.com/api/v1/projects/544525/resources/344864/image-preview" style="width: 640px" />
</p>
</Background>

- **Diverse Date Formatting**: With the `format` method, you can format dates into different formats as needed. For example, `{{$date.now|formatISO}}` will format the date according to the ISO 8601 standard.

<Background>
<p style="text-align: center">
    <img src="https://api-r2.apidog.com/api/v1/projects/544525/resources/344865/image-preview" style="width: 640px" />
</p>
</Background>

- **Precise Time Zone Control**: By setting the `timezone` parameter, you can easily control the time zone of the date. For example, `{{$date.now|format('yyyy-MM-dd HH:mm:ss',timezone='America/Port-au-Prince')}}` will return the date corresponding to the current time in the UTC+8:00 time zone.

<Background>
<p style="text-align: center">
    <img src="https://api-r2.apidog.com/api/v1/projects/544525/resources/344866/image-preview" style="width: 600px" />
</p>
</Background>

## Common Dynamic Variables

To help you get the most out of Apidog Dynamic Values, we've compiled a comprehensive list of available values along with clear examples. You can click [Dynamic Values Modules](https://docs.apidog.com/dynamic-values-modules-1938252f0.md) to quickly find the values you need and learn how to use them effectively.

:::tip
You can also hover your mouse over a Dynamic Value expression within the Apidog application to view a brief description and examples.
:::

