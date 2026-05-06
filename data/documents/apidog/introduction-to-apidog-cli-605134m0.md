# Introduction to Apidog CLI

![NPM Version](https://img.shields.io/npm/v/apidog-cli)

The Apidog CLI is a command-line utility designed for executing and testing your Apidog test scenarios. This tool is built with extensibility in mind, allowing you to seamlessly integrate it with your continuous integration (CI) servers and build systems.

Apidog CLI maintains feature parity with the Apidog platform, ensuring that you can run test scenarios in the same manner as they are executed within the Apidog platform.

When you orchestrated a test scenario in Apidog, you can choose to run it using the visual interface or the CLI, depending on your actual needs.

The differences between the two are:

| Item | Visual Run | Apidog CLI |
| --- | --- | --- |
| **Test Report** | Visual report | Command line report |
| **Running Speed** | Slower | Faster |
| **Compatibility** | Can only be run and viewed in the Apidog client | Can be run and viewed in the command line of any operating system, as well as in CI/CD platforms |
| **Multi-threading** | Supports multi-threading and performance testing | Does not support multi-threading and performance testing |
| **Online/Offline** | Only supports online running | Supports online/offline running |

## Getting Started

To get started, you need to install Node.js and Apidog CLI, after which you can proceed to run your test scenarios. Learn more about detailed information on [Installing and running Apidog CLI](https://docs.apidog.com/installing-and-running-apidog-cli-605135m0.md).

## Options

Apidog CLI offers a comprehensive set of options to customize your runs. Learn more about [Apidog CLI Options](https://docs.apidog.com/apidog-cli-options-609656m0.md).

## File Uploads

Apidog CLI supports file uploads, enabling you to use data files (e.g., text files) to fill in form data fields. Discover the details of [uploading files in Apidog CLI](https://docs.apidog.com/apidog-cli-options-609656m0.md).

## Integrate with CI/CD Platforms

Apidog provides integration with widely-used CI tools, enabling you to monitor API builds directly within the same platform where you design and test your APIs. Learn more about [Integrate with CI/CD](https://docs.apidog.com/cicd-in-apidog-609698m0.md).
