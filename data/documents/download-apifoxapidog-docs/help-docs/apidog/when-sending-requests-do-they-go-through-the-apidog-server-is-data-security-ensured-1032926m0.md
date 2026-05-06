# When sending requests, do they go through the Apidog server? Is data security ensured?

## Apidog Desktop Client
When you use the Apidog desktop client, requests are sent directly from your local computer to the target server, without passing through any Apidog servers. Sending requests from the Apidog client is the same as sending them from your own local code—ensuring a direct connection and maintaining your data privacy.

## Apidog Web

When using Apidog Web, due to the browser's cross-origin restrictions, you cannot directly send requests from the browser. Here are some options to overcome this limitation:

1. **Install the Apidog Browser Extension:** This allows you to send requests directly from your local computer.
2. **Use Apidog Cloud Agent:** This option sends requests from the Apidog agent server. 
3. **Install Apidog Self-hosted Request Proxy Agent:** This enables you to send requests from a server where you've deployed the agent.

For more information, you can refer to the detailed documentation at [Request Proxy in Apidog Web](https://docs.apidog.com/request-proxy-in-apidog-web-835152m0).

Only option 2 involves the requests going through the Apidog server. However, Apidog server will NOT keep any record of the requests.

If you wish for your requests to completely bypass Apidog’s servers, you can opt to use the Apidog Desktop Client, or when using the Apidog Web version, you can choose option 1 (installing the Apidog browser extension) or option 3 (installing the Apidog Self-hosted Request Proxy Agent).

Apidog take data security very seriously and ensure protection, as detailed in our [security measures](https://legal.apidog.com/security-measures-645653m0).

## Related Questions
- [Where is Apidog's data stored, and how is data security ensured?](https://docs.apidog.com/where-is-apidogs-data-stored-and-how-is-data-security-ensured-1032941m0.md)
- [How is user data stored? Will this data be public? Or will it be private? Will all data be stored in the cloud?](https://docs.apidog.com/how-is-user-data-stored-will-this-data-be-public-or-will-it-be-private-will-all-data-be-stored-in-the-cloud-1032859m0.md)
