# Integrate with Gitlab

### Prerequisites

- A GitLab account and project
- An Apidog account with test scenarios created
- Access to generate Apidog access tokens

## Initialize Gitlab Pipeline

Access Gitlab and log in, click "Projects" in the left navigation bar, then click the "New project" button.

<Background>
![GitLab new project creation interface](https://api.apidog.com/api/v1/projects/544525/resources/343390/image-preview)
</Background>


After entering the project, in the "Build" section, click "Pipelines editor" to create a new pipeline.

## Get Gitlab Pipeline Code

In an Apidog Test scenario, switch to CI/CD tab. Specify the runtime environment, choose whether to enable test data, set iteration count, etc. 


<Background>
![Apidog CI/CD configuration tab with GitLab selected](https://api.apidog.com/api/v1/projects/544525/resources/343392/image-preview)
</Background>


Select Gitlab CI pipeline, then click "Copy Code" in the upper right corner.

Paste into Gitlab's Pipeline editor, then click "Commit changes" to trigger the pipeline. If your pipeline includes other built-in tasks, please modify as necessary to ensure the pipeline runs correctly.


<Background>
![GitLab pipeline editor with Apidog configuration](https://api.apidog.com/api/v1/projects/544525/resources/343413/image-preview)
</Background>


## Run the Pipeline

After the pipeline starts running, you will see the run logs in the terminal. At this point, you have integrated Apidog automated testing steps into your Gitlab CI pipeline.


<Background>
![GitLab pipeline execution logs showing test results](https://api.apidog.com/api/v1/projects/544525/resources/343414/image-preview)
</Background>

