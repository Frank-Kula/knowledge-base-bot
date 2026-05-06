# Installing and Running Apidog CLI

Apidog CLI is designed to run Apidog test scenarios in the command line. To get started using Apidog CLI, install Node.js, then Apidog CLI. Then you can run your test scenarios.

### Prerequisites

- Node.js v16 or later installed on your system
- npm (Node Package Manager) installed
- An Apidog account with test scenarios created

## Installing Apidog CLI

Apidog CLI is built on Node.js. To run Apidog CLI, please [install Node.js](https://nodejs.org/en/download/package-manager/) before using it.

The Apidog CLI relies on Node.js version v16 or later. 

Install Apidog CLI from npm globally on your system, enabling you to run it from anywhere:

```bash
npm install -g apidog-cli
```

Here are some commands to verify if Apidog CLI is installed successfully. 

```bash
node -v && apidog -v && which node && which npm && which apidog
```

If installed successfully, it will directly print the version number and installation path after executing commands above.

<Background>
![Terminal output showing successful Apidog CLI installation with version numbers and paths](https://assets.apidog.com/uploads/help/2023/12/26/c9dd7e01651dfed2ff0853cfb8c95426.png)
</Background>

## Updating Apidog CLI

Use the command below to upgrade Apidog CLI.

```bash
npm install apidog-cli@latest -g
```

## Running Apidog CLI

To run test scenarios using the Apidog CLI, you first need to create and orchestrate a test scenario. Then, you can run the test scenario from the command line using the Apidog CLI, just like running it in the visual interface, and get a test report.

The Apidog CLI supports two ways of running:

1. **Running with online data**: This is suitable for live scenarios.
2. **Running with exported test scenarios**: This is suitable for offline scenarios.

### Run Online Data in Real Time

<Steps>
  <Step>
In a test scenario, switch to the CI/CD tab.
<Background>
![CI/CD tab in Apidog test scenario interface](https://api.apidog.com/api/v1/projects/544525/resources/343367/image-preview)
</Background>
  </Step>
  <Step>
Configure the environment, test data, iterations, delay, etc.
  </Step>
  <Step>
In the CI/CD provider section, select "Command line".
  </Step>
  <Step>
Click "Add access token" button and then "Generate token".

:::highlight purple 
Learn more about [access token](https://docs.apidog.com/api-access-token.md).
:::
  </Step>
  <Step>
Click the command to copy it.
  </Step>
  <Step>
Paste and run the command in the command line. And you'll get a test report in command line.
  </Step>
</Steps>

:::tip[]
In Step 2, the configurations you set will automatically determine the options and values utilized in the CLI:
- Environment: Maps to `-e <environmentId>`.
- Test data: Maps to `-d <testDataId>`.
- Iterations: Maps to `-n <n>`.
- Delay: Maps to `--delay-request <n>`.
- Environment/Global variables: If selecting`Export current value and use it`, you can find an export option below to export the current values of the environment/global variables from your project to a file. This affects`--variables <path>`. You will need to import this file onto the machine running the CLI and specify its path via`--variables <path>`. [Learn more about differences between "Use initial value" and "Export current value and use it" here.](https://docs.apidog.com/run-a-test-scenario-602063m0.md#rules-for-using-environmentglobal-variables-across-different-running-methods)
    
If your test scenario also uses locally stored database connection configurations, the product interface will guide you to export these configurations to a local file, which affects `--database-connection <path>`. You will then need to import this exported file onto the machine running the CLI and specify its path in`--database-connection <path>`.
:::

### Run Exported Data

This options allows you to run offline tests locally using exported files. 
<Steps>
  <Step>
In a test scenario, switch to the CI/CD tab.
  </Step>
  <Step>
Configure the environment, test data, iterations, delay, etc.
  </Step>
  <Step>
In the CI/CD provider, select "Command line" and then switch to "Run exported data".
<Background>
![Run exported data option in CI/CD configuration](https://api.apidog.com/api/v1/projects/544525/resources/343381/image-preview)
</Background>
  </Step>
  <Step>
Export the test scenario as a JSON file.
  </Step>
  <Step>
Copy the command displayed below.
  </Step>
  <Step>
Paste and run the command in the command line. You will get a command line test report.
  </Step>
</Steps>

:::tip[]
The settings in step 2 (such as "Run Online Data") will automatically affect the options and values used in the CLI below. Note that when running in this way, the environment/global variables use the values from the file exported along with the test scenario. [Learn more here](https://docs.apidog.com/run-a-test-scenario-602063m0.md#rules-for-using-environmentglobal-variables-across-different-running-methods).
:::

## CLI Test Report

After running the CLI, you will receive a command-line test report that includes execution statistics for test scenarios and validation and assertions for failed requests.

<Background>
![Example CLI test report showing test results and statistics](https://api.apidog.com/api/v1/projects/544525/resources/343373/image-preview)
</Background>

You can also find the /apidog-reports/ directory in the folder where you ran the CLI. This directory contains the CLI test report in HTML format.

## Options

Apidog CLI provides a rich set of options to customize a collection run. Learn more at [Apidog CLI Options](https://docs.apidog.com/apidog-cli-options-609656m0.md).

## Using Apidog CLI with CI/CD

Apidog CLI supports integration with various pipeline tools, such as Jenkins, GitLab, GitHub Actions, and more. Learn more about [integrating CI/CD](https://docs.apidog.com/cicd-in-apidog-609698m0.md).

