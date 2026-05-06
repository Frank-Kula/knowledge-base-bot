# AWS Secrets Manager

:::tip[]
Vault secrets is available on the [Apidog Enterprise plan](https://apidog.com/pricing).
:::

Apidog supports integration with AWS Secrets Manager via access key pairs for IAM users.

## Configure AWS

Create IAM users for individuals who need to access AWS Secrets Manager, and generate an access key pair (Access Key ID and Secret Access Key) for each user.

## Test Connection

1. In Apidog, enter the AWS [Region](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-regions) code, your **Access Key ID**, and **Secret Access Key**.
   
   :::note
   The access key pair is NOT uploaded to the server and is NOT shared with other team members.
   :::

2. Click **Test Connection**. If the configuration is correct, "Succeeded" will be displayed.

<Background>
![Test AWS connection](https://api.apidog.com/api/v1/projects/544525/resources/348729/image-preview)
</Background>

## Link Secrets

Assume there is a secret named `test/foo` in AWS Secrets Manager:

<Background>
![AWS Secrets Manager secret example](https://api.apidog.com/api/v1/projects/544525/resources/348730/image-preview)
</Background>

To link this secret in Apidog:

1. Enter the metadata as shown below.

<Background>
![Link AWS secret metadata](https://api.apidog.com/api/v1/projects/544525/resources/348731/image-preview)
</Background>

2. Click the **Fetch Secrets** button.
3. Click the eye icon on the right to view the retrieved secret value.

<Background>
![View fetched AWS secret](https://api.apidog.com/api/v1/projects/544525/resources/348732/image-preview)
</Background>

If you want to extract a specific value from a key-value pair secret:
1. Select **Key/Value** as the secret type.
2. Enter the name of the key you wish to retrieve.

<Background>
![Extract specific key from AWS secret](https://api.apidog.com/api/v1/projects/544525/resources/348733/image-preview)
</Background>

