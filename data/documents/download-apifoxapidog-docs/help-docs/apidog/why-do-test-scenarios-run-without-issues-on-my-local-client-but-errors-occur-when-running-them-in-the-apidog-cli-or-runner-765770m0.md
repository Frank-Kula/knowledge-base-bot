# Why do test scenarios run without issues on my local client, but errors occur when running them in the Apidog CLI or runner?

The most common problem involves the use of variables.

When running in the Apidog local client, the '**current value**' of variables, which is stored in your client, is used and does not sync to the server. However, when running in the CLI or runner, the '**initial value**' stored on the server is used.

To ensure smooth operation both locally and remotely, you need to set both the initial value and current value properly and keep them consistent.

<Background>
![image.png](https://api.apidog.com/api/v1/projects/544525/resources/348439/image-preview)
</Background>

