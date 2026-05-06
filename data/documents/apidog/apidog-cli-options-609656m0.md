# Apidog CLI Options

## Basic Apidog CLI Syntax

**Online execution:** when running real-time tests through the Apidog server, use the following command.

```bash
apidog run --access-token <value> [options]
```
Use the Apidog access token along with the ID of a specific test scenario or test scenario directory. For example:

```bash
apidog run --access-token $APIDOG_ACCESS_TOKEN -t 637132 -e 358171 -d 3497013 -r html,cli --database-connection ./database-connections.json
```
:::tip[]
If you're using Github Actions, you can store your access token under your repository's **Settings** --> **Secrets and Variables** --> **Actions** --> **Repository variables**. Then Use `${{ vars.APIDOG_ACCESS_TOKEN }}` to reference it.
:::

**Local execution:** when running offline tests using exported files use the following command.
```bash
apidog run <collection> [options]
```
Specify the URL or file path of the Apidog test scenario. For example:


```bash
apidog run examples/sample.apidog-cli.json -r cli,html
```

## Options

| Option | Description |
|--------|-------------|
| `--access-token <accessToken>` | Set authentication token for online execution |
| `-t, --test-scenario <testScenarioId>` | Specify test scenario ID to run |
| `-f, --test-scenario-folder <folderId>` | Specify test scenario directory ID to run |
| `-r, --reporters [reporters]` | Specify test report types (default: ["cli"]) |
| `--out-dir <outDir>` | Output directory for test reports (default: "./apidog-reports") |
| `--out-file <outFile>` | Output test report file name with no need to add a file extension (default: "apidog-report-{GENERATE_TIME}"). You can use special variables: `{FOLDER_NAME}` `{SCENARIO_NAME}` `{GENERATE_TIME}`|
| `--out-json-failures-separated <outJsonFailuresSeparated>` | Export failures as separate JSON file |
| `-e, --environment` | Specify runtime environment |
| `-n, --iteration-count <n>` | Set number of iterations |
| `-d, --iteration-data <path>` | Set data for case iterations (JSON or CSV) |
| `--variables <path>` | Environment/global variables using from files in the specified path, instead of use initial values of environment/global variables. |
| `--global-var <value>` | Set global variables (key=value format) |
| `--env-var <value>` | Set environment variables (key=value format) |
| `--external-program-path <path>` | Specify file path for external programs |
| `--database-connection <path>` | Specify file path for database configuration |
| `--ignore-redirects` | Prevent automatic redirects |
| `--silent` | Prevent console output |
| `--color <value>` | Enable/disable colored console output |
| `--delay-request [n]` | Specify delay between requests (ms) |
| `--timeout-request [n]` | Specify request timeout (ms) |
| `--timeout-script [n]` | Specify script execution timeout (ms) |
| `-k, --insecure` | Disable SSL verification |
| `--ssl-client-cert-list <path>` | Specify client certificate config path |
| `--ssl-client-cert <path>` | Specify client certificate path (PEM) |
| `--ssl-client-key <path>` | Specify client certificate private key path |
| `--ssl-client-passphrase <passphrase>` | Specify client certificate passphrase |
| `--ssl-extra-ca-certs <path>` | Specify additional trusted CA certificates |
| `-b, --bigint` | Enable bigint compatibility |
| `--upload-report [value]` | Upload test report overview to cloud |
| `--preferred-http-version <preferredHttpVersion>` | Set preferred HTTP protocol version |
| `--verbose` | Display detailed request and response information |
| `--lang <language>` | Set CLI language (en) |
| `-h, --help` | Display help information |

## Uploading Files in CLI

When working with APIs that require file uploads, accurately setting the path of the file to be uploaded is crucial. You should store the file in the same machine where the tests run and reference it using either its absolute or relative path. Follow these steps to reference a file to upload.

<Steps>
  <Step>
Copy the required file to the machine running the CLI beforehand. For example, if you're using Github Actions as your CI/CD pipeline, copy the required file to the same Github repository to that of your workflow.
  </Step>
  <Step>
In Apidog, navigate to your test scenario and locate the step that requires file upload. Click on **Bulk Edit** button as shown below.
<Background>
![Batch Edit button in test scenario step details](https://api.apidog.com/api/v1/projects/544525/resources/371836/image-preview)
</Background>
  </Step>
  <Step>
Copy the path of the file you copied to the CLI machine. Then replace the file field parameter value with the file path on the CLI machine. For example, if you put a `png` file under `data` folder in a Github repo, you can use `data/to-be-uploaded.png` to reference it.
        
<Background>
![File path configuration in batch edit mode](https://api.apidog.com/api/v1/projects/544525/resources/371835/image-preview)
</Background>

  </Step>  
</Steps>

After this configuration, the file can be correctly sent to Apidog through the CLI.

:::info[]
If you want to run this test scenario locally again, you'll need to modify the file path in the parameter value back to the path on your local machine.
:::

## Using Database Operations in CLI

When your test scenarios include database operations, you need to take a few extra steps because database configurations are saved locally, not in the cloud. This means you can't directly run the CLI in cloud mode for these scenarios. Here's how to handle this situation:

<Steps>
  <Step>
For test scenarios that include database operations, you'll see a prompt in the command line generation interface: "Download the database configuration file."  
    </Step>
  <Step>
Download this file and place it in the directory where you plan to run the Apidog CLI.
  </Step>
  <Step>
The automatically generated command line will include the `--database-connection` option. You can use this command line as is to run your tests.
  </Step>
</Steps>

## Uploading Local CLI Test Reports to the Cloud

To upload your local CLI test reports to the cloud, you can add the `--upload-report` parameter at the end of your CLI command. Here's how to do it:

<Steps>
  <Step>
Add the `--upload-report` parameter to your CLI command:

   ```bash
   apidog run --access-token $APIDOG_ACCESS_TOKEN -t 637132 -e 358171 -d 3497013 -r html,cli --upload-report detail
   ```  
    </Step>
  <Step>
This command will run your tests and automatically upload the test report to the cloud after completion.
</Step>
  <Step>
To view the uploaded report:
   - Go to the "Test Reports" section in your Apidog dashboard.
   - Look for the "Team Reports" column.
    </Step>
    <Step>
Note: For reports uploaded via CLI, the "Tester" field will be displayed as empty.
  </Step>  
</Steps>

## Using External Scripts/Programs in CLI

You can reference external scripts or programs when running the Apidog CLI by adding their path at the end of the command. Here's how to do it:

```bash
--external-program-path ./scripts
```

In this example, the CLI is instructed to reference programs located in the `./scripts` directory. If no hierarchy is specified, the default is the current CLI execution directory.

There are two main approaches to managing these external scripts:

### 1. Local Path

To avoid confusion in managing local scripts, it's recommended to:
- Organize all script files by category
- Place them in a specific directory
- Specify the corresponding local path in the CLI command

### 2. Cloud Code Repository

Alternatively, you can:
- Host script files in a cloud-based code repository
- Set up pull commands in your CI/CD workflow to fetch external scripts to the local environment
- Specify the actual path of the external scripts in the CLI command

## SSL

### Client Certificate

Apidog CLI supports passing in client certificates.


### Using Single SSL Client Certificate 

* `--ssl-client-cert` 
  Specify the path of the public SSL client certificate. 

* `--ssl-client-key` 
  Specify the path of the private SSL client certificate (optional). 
* `--ssl-client-passphrase `
  Specify SSL client passphrase (optional).

### Using SSL Client Certificates Configuration File (Supports Multiple Certificates)

* `--ssl-client-cert-list` 
  Specify the path of the JSON file of the SSL client certificate list. For example:`ssl-client-cert-list.json`

```json
[
    {
        "name": "domain1",
        "matches": ["https://test.domain1.com/*", "https://www.domain1/*"],
        "key": {"src": "/CI/client.domain1.key"},
        "cert": {"src": "/CI/client.domain1.crt"},
        "passphrase": "changeme"
    },
    {
        "name": "domain2",
        "matches": ["https://domain2.com/*"],
        "key": {"src": "/CI/client.domain2.key"},
        "cert": {"src": "/CI/client.domain2.crt"},
        "passphrase": "changeme"
    }
]
```

This option supports setting different SSL client certificates based on URL or hostname. It takes precedence over the `--ssl-client-cert`, `--ssl-client-key`, and `--ssl-client-passphrase` options. These options will be used as fallback options if there is no match for the URL in the list.

## HTTP/2

The CLI can be configured to use specific protocol versions for sending requests by using the `--preferred-http-version` parameter.

Protocol version parameter values:

1. "HTTP/2" - HTTP/2 Application-Layer Protocol Negotiation (ALPN), supported only for HTTPS requests.
2. "HTTP/2-with-prior-knowledge" - HTTP/2 with prior knowledge
3. "HTTP/1" - HTTP/1.1

The parameter supports the following configurations:

1. Setting different protocol versions for HTTPS and HTTP requests:
   ```bash
   --preferred-http-version="https=HTTP/2,http=HTTP/2-with-prior-knowledge"
   ```

2. Setting the same protocol version for both HTTPS and HTTP:
   ```bash
   --preferred-http-version="HTTP/1"
   ```

3. Setting HTTP/2 for both HTTPS and HTTP (unsupported values will be automatically ignored):
   ```bash
   --preferred-http-version="HTTP/2"
   ```

## FAQ

**Q: How to handle the error message `Invalid character in header content["Authorization"]`?**

A: If you're certain that running test scenarios in the Apidog client or web interface doesn't produce any errors, please check if you've set INITIAL values for variables in your environment.

