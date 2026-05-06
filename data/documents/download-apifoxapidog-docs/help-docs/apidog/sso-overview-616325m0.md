# SSO Overview

:::info
SSO is available on [Apidog Enterprise plan](https://www.apidog.com/pricing).
:::

When using Apidog, you can configure SSO single sign-on by organization. Apidog's SSO supports identity providers (IdPs) that compatible with the SAML 2.0 protocol, such as Microsoft Entra ID (formerly Azure Active Directory).

After configuring SSO, members within the organization must regularly verify their identity through SSO when accessing internal resources, enhancing overall security.

At the same time, organization members can directly log into Apidog and join the organization via SSO using their work emails. This makes it easier for administrators to invite members and simplifies the login process for everyone in the organization.

## Advantages of Using SSO for Enterprises

- **Enhanced User Experience**: SSO allows users to access multiple applications or systems with a single set of credentials, eliminating the need to remember numerous passwords. This simplifies the login process and improves user satisfaction.

- **Increased Productivity**: By reducing the frequency of login-related interruptions, SSO enables users to access necessary resources quickly and seamlessly. This boosts productivity as less time is spent on managing login credentials and more on performing critical tasks.

- **Improved Security**: SSO reduces the risk of password fatigue, where users reuse the same password across different platforms or choose weak passwords. With SSO, security measures can be centralized, making it easier to enforce strong authentication policies like multi-factor authentication (MFA).

- **Simplified Account Management**: SSO aids in the efficient management of user accounts. Administrators can streamline user onboarding and offboarding procedures, enforce security policies consistently, and manage accesses from a single interface.

- **Reduced IT Support Costs**: Since users are less likely to forget their passwords, there's a decrease in the number of password reset requests and related help desk calls. This can significantly reduce IT support workload and costs.

## Prerequisites for SSO with Apidog

- The identity provider (IdP) must support the SAML 2.0 protocol.
- An organization has been set up using Apidog and is subscribed to the enterprise edition payment plan.

