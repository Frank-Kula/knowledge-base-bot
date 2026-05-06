# Kerberos

Kerberos is a network authentication protocol initially developed by the Massachusetts Institute of Technology (MIT) and widely used in modern computing systems, especially in enterprise environments. Kerberos utilizes symmetric encryption and a trusted third party, known as the Key Distribution Center (KDC), to securely authenticate users and services.

When using Windows Authentication in IIS (Internet Information Services), Kerberos will be used preferentially over NTLM when available, providing stronger security and better performance.

<Background>
![Kerberos Authentication](https://assets.apidog.com/uploads/help/2024/08/16/e7afc84de9c9207784752eca97d1111e.png)
</Background>

## Prerequisites

To use Apidog's Kerberos authentication feature, ensure your computer meets the following requirements:

| Operating System | Requirements |
|------------------|--------------|
| **Windows** | Successfully joined to a domain OR possesses a valid Kerberos credential |
| **macOS** | Possesses a valid Kerberos credential |
| **Linux** | Possesses a valid Kerberos credential |

:::warning[Client-Only Feature]
This feature is only supported in the **Apidog client version** and is not available in the web version. Kerberos authentication requires native OS integration that cannot be provided in a browser environment.
:::

## Configuration

Configure the Kerberos authentication parameter:

| Parameter | Description | Format | Example |
|-----------|-------------|--------|---------|
| **SPN** | Service Principal Name | `HTTP/hostname.domain.local@realm.name` | `HTTP/api.example.com@EXAMPLE.COM` |


