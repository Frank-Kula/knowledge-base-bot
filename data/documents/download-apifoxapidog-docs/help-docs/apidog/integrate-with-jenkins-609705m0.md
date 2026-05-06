# Integrate with Jenkins

### Prerequisites

- Jenkins installed and running (v2.0 or later recommended)
- Node.js v16 or later installed on Jenkins host
- An Apidog account with test scenarios created
- Access to generate Apidog access tokens

## Install Jenkins

Jenkins is an automated build tool that helps developers automate building process, testing, and deploying applications during the software development process. Here's how to [install](https://www.jenkins.io/download/) it on a Linux system:

1. Add the Jenkins GPG public key:

```bash
wget -q -O - https://pkg.jenkins.io/debian/jenkins.io.key | sudo apt-key add -
```

2. Add the Jenkins source to the list of APT software sources:

```bash
sudo sh -c 'echo deb http://pkg.jenkins.io/debian-stable binary/ > /etc/apt/sources.list.d/jenkins.list'
```

3. Update the APT package list:

```bash
sudo apt-get update
```

4. Install Jenkins:

```bash
sudo apt-get install jenkins
```

5. Start the Jenkins service:

```bash
sudo systemctl start jenkins
```

After installation, open a web browser and enter `http://localhost:8080` or `http://{your_public_IP}:8080` to access the Jenkins dashboard. The console provides a web API for you to manage and configure Jenkins services.

For more information about Jenkins, please check the [Jenkins website](https://www.jenkins.io/).

## Configuring Node.js Environment for Jenkins

:::tip[]
Before running Apidog CLI, you need to ensure that the Node.js version number is v16 or later, so you need to configure NodeJS dependencies in the Jenkins environment first.
:::

1. Open the Jenkins plugin management and find the NodeJS plugin, install it and restart it.


<Background>
![Jenkins plugin management interface showing NodeJS plugin](https://api.apidog.com/api/v1/projects/544525/resources/357041/image-preview)
</Background>



2. Create a new NodeJS in the global tool configuration, configure the version number (requires v16 or later) and package name `apidog-cli` .


<Background>
![Jenkins global tool configuration for NodeJS](https://api.apidog.com/api/v1/projects/544525/resources/357043/image-preview)
</Background>



If apidog-cli has been installed on the Jenkins host and you want to run tasks directly in the Node environment, you can refer to the Node configuration in the figure below and fill in the Node path of the host.


<Background>
![Alternative NodeJS configuration using existing installation](https://api.apidog.com/api/v1/projects/544525/resources/357044/image-preview)
</Background>

You can trigger Apidog automated tests in Jenkins using the following two methods:  
1. Add the configuration in a visual pipeline (Freestyle Project)  
2. Integrate the embedded code into the pipeline (Pipeline)

## Run CLI Commands

### Configure Pipeline Visually

Open Apidog and retrieve the CLI command from the Continuous Integration details page. If your Jenkins environment has internet access, you can choose to use the "Run online data in real time" command. If internet access is not available, you need to first export the CLI JSON data file into the environment and then execute it via the CLI.


<Background>
![Apidog CI/CD tab showing Jenkins CLI command options](https://api.apidog.com/api/v1/projects/544525/resources/357045/image-preview)
</Background>


In the project configuration page, locate the **Build Environment** section, check the option **"Provide Node & npm bin/ folder to PATH"**, and select the NodeJS version (e.g., `nodejs18`) that you configured in the **Global Tool Configuration (Tools)** section.


<Background>
![Jenkins build environment configuration with NodeJS selected](https://api.apidog.com/api/v1/projects/544525/resources/357046/image-preview)
</Background>


After setting up the build environment, go to the **Build Steps** section, click **Add build step**, and select **Execute Shell** *(choose **Execute Windows Batch Command** if you're using a Windows system)*.


<Background>
![Jenkins build steps configuration showing Execute Shell option](https://api.apidog.com/api/v1/projects/544525/resources/357047/image-preview)
</Background>


Paste the Apidog CLI command into the **Command** input box and save the configuration.


<Background>
![Jenkins shell command configuration with Apidog CLI command](https://api.apidog.com/api/v1/projects/544525/resources/357048/image-preview)
</Background>


Click **Build Now** in the project to start the execution.


<Background>
![Jenkins build now button to trigger execution](https://api.apidog.com/api/v1/projects/544525/resources/357049/image-preview)
</Background>

You can check the build progress and results in the "Build History."

<br />

### Integrate Embedded Code into the Pipeline

Navigate to the **CI/CD** tab and copy the embedded code snippet, then paste it into your Jenkins configuration file.


<Background>
![Apidog CI/CD tab showing Jenkins pipeline code snippet](https://api.apidog.com/api/v1/projects/544525/resources/357050/image-preview)
</Background>


Simply paste the code directly into the Jenkins pipeline configuration to embed it into your existing CI/CD workflow.


<Background>
![Jenkins pipeline configuration editor with Apidog code](https://api.apidog.com/api/v1/projects/544525/resources/357051/image-preview)
</Background>


The `nodejs18` mentioned here refers to the NodeJS alias set earlier — please replace it with your actual alias. Also, make sure to replace the variable `$APIDOG_ACCESS_TOKEN` in the code with your actual Access Token. Alternatively, you can add an environment variable named `APIDOG_ACCESS_TOKEN` in Jenkins under **Dashboard → Manage Jenkins → System**, and set its value to your Access Token. This allows the pipeline to read your Access Token during execution.


<Background>
![Jenkins system configuration for environment variables](https://api.apidog.com/api/v1/projects/544525/resources/357052/image-preview)
</Background>


You can simplify the above code by removing the script for installing the Apidog CLI. This way, there's no need to reinstall `apidog-cli` every time a build is executed, which reduces both build time and resource consumption. This is possible because NodeJS and global npm packages (i.e., `apidog-cli`) have already been configured in advance under **Global Tool Configuration (Tools)**, ensuring that the required tools are readily available during the build process.


<Background>
![Simplified Jenkins pipeline code without CLI installation](https://api.apidog.com/api/v1/projects/544525/resources/357054/image-preview)
</Background>


Click **Build Now** in the project to start the execution.


<Background>
![Jenkins build execution in progress](https://api.apidog.com/api/v1/projects/544525/resources/357053/image-preview)
</Background>


## Publish Reports with Jenkins

Specify the generated report name `${JOB_NAME}_${BUILD_NUMBER}` (Jenkins built-in variable) in the command. Use the `HTML Publisher` plugin to view the report. 

```bash
apidog run https://api.apidog.com/api/v1/api-test/ci-config/XXX/detail?token=xxxxx -r html,cli --out-file ${JOB_NAME}_${BUILD_NUMBER}
```

