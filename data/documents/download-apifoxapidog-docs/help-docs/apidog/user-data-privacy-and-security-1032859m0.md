# User Data Privacy and Security

Understanding how Apidog stores your data and maintains privacy is essential for secure API development and testing.

## Apidog SaaS

### Cloud Data

In the SaaS version of Apidog, most data is stored in the cloud, including:
- API specifications
- Testing scenarios
- Project configurations
- Team collaboration data

**Privacy and access:**
- All user data is kept private
- Only visible to team members
- Not publicly accessible by default

**Exception: Published API Documentation**

Publicly published API documentation is visible to the public. However, you can restrict access using:
- Password protection
- IP allowlists
- Other [visibility settings](https://docs.apidog.com/visibility-settings-662939m0.md)

**Security measures:**

Apidog employs various methods to ensure data security. For detailed information, see [Apidog Security Measures](https://legal.apidog.com/security-measures-645653m0).

### Local Data

Certain sensitive data is stored exclusively on your local computer and never synchronized to the cloud:

| Data Type | Storage Location | Cloud Sync |
|-----------|------------------|------------|
| [Current values](https://docs.apidog.com/using-variables-577908m0.md#initial-and-current-values) in environment/global variables | Local only | ❌ No |
| [Vault Secrets](https://docs.apidog.com/vault-secret-in-apidog-778134m0.md) | Local only | ❌ No |
| API specifications | Cloud | ✅ Yes |
| Testing scenarios | Cloud | ✅ Yes |

:::tip[Best Practice]
Store sensitive data such as passwords, API keys, and credentials in:
- **Current values** of environment/global variables
- **Vault Secrets**

This ensures sensitive information never leaves your local machine.
:::

## Apidog On-Premises

In Apidog On-Premises deployments:

**Complete data control:**
- All data resides on your own self-hosted servers
- No data stored on Apidog's cloud
- No data sent to Apidog servers

**Benefits:**
- Complete control over your data
- Full privacy and security
- Compliance with internal security policies
- Custom security implementations

## Related Topics

- [Data Storage and Security](https://docs.apidog.com/data-storage-and-security-1032941m0.md)
- [Request Routing and Data Security](https://docs.apidog.com/request-routing-and-data-security-1032926m0.md)

