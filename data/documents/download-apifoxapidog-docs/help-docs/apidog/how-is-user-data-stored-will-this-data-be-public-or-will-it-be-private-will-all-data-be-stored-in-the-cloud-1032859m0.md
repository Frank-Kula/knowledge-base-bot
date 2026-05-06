# How is user data stored? Will this data be public? Or will it be private? Will all data be stored in the cloud?

## Apidog SaaS

### Cloud Data

In the SaaS version of Apidog, most of your data, including API specifications and testing scenarios, are stored in the cloud. All user data is kept private and is only visible to team members, ensuring it is not publicly accessible. 

- The only exception is "publicly published" API documentation, which is visible to the public. However, you can [employ methods such as passwords and whitelists](https://docs.apidog.com/visibility-settings-662939m0) to prevent the API documentation from being publicly visible.
- We employ a variety of methods to ensure data security, and detailed information can be found at [Apidog Security Measures](https://legal.apidog.com/security-measures-645653m0).

### Local Data

[Current values](https://docs.apidog.com/using-variables-577908m0#initial-and-current-values) in environment/global variables are stored exclusively on the local computer and are not synchronized to the cloud.

- It is recommended to place sensitive data in **current values**.
- For credentials, like account passwords and similar sensitive information, utilizing [Vault Secrets](https://docs.apidog.com/vault-secret-in-apidog-778134m0) is advisable. Data within Vault Secrets will not be synchronized to the cloud.

## Apidog On-premises

In Apidog On-premises, all data resides on your own self-hosted servers and will not be stored on Apidog's cloud. 

No data will be sent to Apidog's server, ensuring complete control and privacy over your data.

## Related Questions

- [Where is Apidog's data stored, and how is data security ensured?](https://docs.apidog.com/where-is-apidogs-data-stored-and-how-is-data-security-ensured-1032941m0.md)
- [When sending requests, do they go through the Apidog server? Is data security ensured?](https://docs.apidog.com/when-sending-requests-do-they-go-through-the-apidog-server-is-data-security-ensured-1032926m0.md)
