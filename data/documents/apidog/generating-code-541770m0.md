# Generating Code

Based on the API spec, Apidog supports automatic generation of business code for various languages and frameworks, including but not limited to TypeScript, Java, Go, Swift, Objective-C, Kotlin, Dart, C++, C#, Rust, and over 130 other languages and frameworks.

Apidog offers three types of Code Generation: **Generate Server Stubs and Client SDKs**, **Generate Client Code**, and **Generate Data Model Code**.

- **Generate Server Stubs and Client SDKs**: Server Stubs are for API developers, while Client SDKs are for API consumers. This produces both server-side and client-side code. Server stubs are skeletal implementations of API endpoints on the server, while Client SDKs are pre-built libraries for different programming languages to interact with the API.
- **Generate Client Code**: For API consumers. Creates code for client applications to interact with an API.
- **Generate Data Model Code**: For API consumers. Generates code representations of the data structures used in the API. This includes classes or structs that define the shape of request and response objects, helping ensure type safety and consistency across the application.

## Generating Server Stubs and Client SDKs

The **Generate Server Stubs and Client SDKs** feature in Apidog empowers developers to streamline the process of implementing APIs by automatically generating server-side code stubs and client-side SDKs based on the API specifications defined within the platform.

Server Stubs are code templates that can be used to bootstrap server-side applications, providing a foundation for implementing the specified API endpoints, request handling, and response generation. On the other hand, Client SDKs offer pre-configured code snippets for interacting with the API from the client side, simplifying the integration of API functionality into various applications.

### How to Generate

**1. Install the code generation plugin**

Click **Generate Code** in the API spec, and select **Generate Server Stubs and Client SDKs**.

<Background>
<p style="text-align: center">
    <img src="https://api.apidog.com/api/v1/projects/544525/resources/348338/image-preview" style="width: 640px" />
</p>
</Background>

Click the **Download and Install** button in the business code generation page.

<Background>
<p style="text-align: center">
    <img src="https://assets.apidog.com/uploads/help/2023/07/12/aa61c60cf0b02f95b497aaca69f51504.png" style="width: 640px" />
</p>
</Background>

:::note
If your network cannot access the internet, please manually download `openapi-generator-cli-7.13.0.jar` from:
[`https://repo1.maven.org/maven2/org/openapitools/openapi-generator-cli/7.13.0/openapi-generator-cli-7.13.0.jar`](https://repo1.maven.org/maven2/org/openapitools/openapi-generator-cli/7.13.0/openapi-generator-cli-7.13.0.jar)
:::

Then place the JAR file in the following directory for your system:

- **macOS**: `~/Library/Application Support/apidog/`
- **Windows**: `C:\Users\<USERNAME>\AppData\Roaming\apidog\`
- **Linux**: `~/.config/apidog/`

The plugin will automatically detect and use the local JAR, so no internet connection is required.

<Background>
<img src="https://api.apidog.com/api/v1/projects/544525/resources/366853/image-preview" width="460px" />
</Background>

**2. Generate code**

Select the desired server or client code, and click **Generate Code**.

<Background>
<p style="text-align: center">
    <img src="https://api.apidog.com/api/v1/projects/544525/resources/342707/image-preview" style="width: 640px" />
</p>
</Background>

**3. Use custom template**

You can also use the **Custom Code Templates** feature to generate code that conforms to your team's architectural specifications to meet a variety of individual needs.

<Background>
<p style="text-align: center">
    <img src="https://api.apidog.com/api/v1/projects/544525/resources/342704/image-preview" style="width: 640px" />
</p>
</Background>

### Supported Languages/Frameworks

| Language | Server/Client | Frameworks |
| :--- | :--- | :--- |
| Java | Server | Spring, Inflector, Msf4j, Pkmst, Play Framework, Undertow Server, Vertx, Vertx Web, JAX-RS Cxf, JAX-RS Cxf Cdi, JAX-RS Cxf Extended, JAX-RS Jersey, JAX-RS Resteasy, JAX-RS Resteasy Eap, JAX-RS Spec |
| Java | Client | Android, Java |
| PHP | Server | Laravel, Lumen, Symfony, Ze Ph, Slim4, Slim (Deprecated), Silex (Deprecated) |
| PHP | Client | PHP |
| Swift | Client | Swift5, Swift4, Swift3 (Deprecated), Swift2 (Deprecated) |
| Kotlin | Server | Kotlin Server, Kotlin Spring, Kotlin Vertx |
| Kotlin | Client | Kotlin |
| JavaScript | Client | Apollo, Flowtyped, Closure Angular |
| Node.js | Server | Express, GraphQL Express |
| TypeScript | Client | Axios, Fetch, Redux Query, Angular, Angularjs, Jquery, Rxjs, Node, Aurelia, Inversify |
| C++ | Server | Pistache Server, Qt5 Qhttpengine Server, Restbed Server |
| C++ | Client | Qt5 Client, Restsdk, Tizen |
| C# | Server | C# Nancyfx |
| C# | Client | C#, C# Netcore, C# Dotnet2 |
| ASP.NET | Server | ASP.NET Core |
| Dart | Client | Dart, Dart Dio, Dart Jaguar |
| Go | Server | Go Server, Go Gin Server |
| Go | Client | Go, Go (Experimental) |
| C | Client | C |
| Objective-C | Client | Objective-C |
| Scala | Server | Scala Akka Http Server, Scala Finch, Scala Lagom Server, Scala Play Server |
| Scala | Client | Scala Akka, Scala Gatling, Scala Sttp, Scalaz, Scala Httpclient (Deprecated) |
| Clojure | Client | Clojure |
| Groovy | Client | Groovy |
| Python | Server | Python Aiohttp, Python Blueplanet, Python Flask |
| Python | Client | Python, Python (Experimental) |
| Rust | Server | Rust Server |
| Rust | Client | Rust |
| Ruby | Server | Ruby On Rails, Ruby Sinatra |
| Ruby | Client | Ruby |
| R | Client | R |
| Perl | Client | Perl |
| PowerShell | Client | PowerShell |
| JMeter | Client | JMeter |
| Bash | Client | Bash |
| Lua | Client | Lua |
| F# | Server | F# Functions, F# Giraffe Server |
| OCaml | Client | OCaml |
| Erlang | Server | Erlang Server |
| Erlang | Client | Erlang Client, Erlang Proper |
| Flash | Client | Flash |
| Elixir | Client | Elixir |
| Haskell | Server | Haskell |
| Haskell | Client | Haskell Http Client |
| Elm | Client | Elm |
| Nim | Client | Nim |
| Ada | Server | Ada Server |
| Ada | Client | Ada |
| Apex | Client | Apex |
| Eiffel | Client | Eiffel |

:::tip
The features of Apidog's code templates are based on OpenAPI Generator but simplified. You can refer to this [Youtube Video](https://www.youtube.com/watch?v=Jp2y15Xgk9g) to learn more about the rules of OpenAPI generator templates.
:::

## Generating Client Code

Client code is used to initiate API requests in various development environments. Click the **Generate Client Code** button on the right side of the Documentation tab in the API.

<Background>
<p style="text-align: center">
    <img src="https://api.apidog.com/api/v1/projects/544525/resources/342709/image-preview" style="width: 640px" />
</p>
</Background>

You can also generate code by clicking the code icon `</>` in the Run tab in the API.

<Background>
<p style="text-align: center">
    <img src="https://api.apidog.com/api/v1/projects/544525/resources/342724/image-preview" style="width: 640px" />
</p>
</Background>

:::note
The Client code generated using the mentioned methods will **ONLY** include the API specifications and **NOT** the request parameter values. If you want to generate Client code that includes the request parameter values, you need to first send the request, then switch to the **Actual Request** tab. Scroll down to find the Client code that includes the parameter values.
:::

<Background>
<p style="text-align: center">
    <img src="https://api.apidog.com/api/v1/projects/544525/resources/342723/image-preview" style="width: 640px" />
</p>
</Background>

### Supported Languages

| Language | Variant |
| :--- | :--- |
| Shell | cURL, cURL-Windows, Httpie, wget, PowerShell |
| JavaScript | Fetch, Axios, jQuery, XHR, Native, Request , Unirest |
| Java | Unirest, OkHttp |
| Swift | URLSession |
| Go | Native |
| PHP | cURL, Guzzle, pecl_http, HTTP_Request2 |
| Python | http.client, Requests |
| HTTP | HTTP |
| C | libcurl |
| C# | RestSharp |
| Objective-C | NSURLSession |
| Ruby | Net::HTTP |
| OCaml | Cohttp |
| Dart | http |
| R | httr, RCurl |

## Generating Data Model Code

Data model code is used to define schemas, and is commonly used for serialization when APIs send data and deserialization processing when data is received. After the SQL code type is generated, you can also define table creation statements in the database table creation scenario to create data tables in the database.

To access the data model, tap the **Generate Code** button in the Schema Editor.

<Background>
<p style="text-align: center">
    <img src="https://api.apidog.com/api/v1/projects/544525/resources/342725/image-preview" style="width: 640px" />
</p>
</Background>

Afterward, you can select the desired programming language for the generated code and configure specific code style preferences.

<Background>
<p style="text-align: center">
    <img src="https://api.apidog.com/api/v1/projects/544525/resources/342726/image-preview" style="width: 640px" />
</p>
</Background>

### Supported Languages

<Columns>
  <Column>
    C#
    C++
    Crystal
    Dart
    Elm
  </Column>
  <Column>
    Flow
    Go
    Haskell
    Java
    JavaScript
  </Column>
  <Column>
    Kotlin
    Objective-C
    Pike
    Python
    Ruby
  </Column>
  <Column>
    Rust
    SQL
    Swift
    TypeScript
  </Column>
</Columns>

## Generate Code in API Documentation

In the API documentation generated by Apidog, you can easily generate **Client Code** and **Data Model code**.

<Background>
![Generate Code in API Documentation](https://api.apidog.com/api/v1/projects/544525/resources/342727/image-preview)
</Background>

