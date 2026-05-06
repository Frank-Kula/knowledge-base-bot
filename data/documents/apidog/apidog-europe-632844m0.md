# Apidog Europe

Apidog Europe is a dedicated European deployment of Apidog, designed to meet regional data residency and GDPR compliance requirements. This page explains the key differences between Apidog Europe and Apidog Global, how to access the European service, and how to migrate your data.

:::tip[]
User data is securely stored in the **AWS Ireland Region**, with backup data maintained in the **AWS Germany Region**.
:::

## What is Apidog Europe?

Apidog Europe offers the same comprehensive feature set as Apidog Global, with one critical difference: **data residency**. 

| Aspect | Apidog Europe | Apidog Global |
|--------|---------------|---------------|
| **Server Location** | AWS Ireland (Europe) | AWS USA (North America) |
| **Backup Location** | AWS Germany (Europe) | AWS USA (North America) |
| **Account System** | Separate European accounts | Separate global accounts |
| **GDPR Compliance** | Full GDPR compliance | Standard compliance |
| **Best For** | European teams | International teams |

:::important[]
Apidog Europe and Apidog Global use **completely separate account systems**. Users cannot collaborate or share data across regions.
:::

### Choosing the Right Service

- **Use Apidog Europe** if your team is based in Europe and requires GDPR-compliant data storage
- **Use Apidog Global** if you collaborate with colleagues outside Europe or don't have specific European data residency requirements

:::tip[]
Published API documentation can be accessed by readers anywhere in the world, regardless of which service you use, since reading documentation doesn't require an account.
:::

## Accessing Apidog Europe

### Web Application

Access Apidog Europe directly in your browser: [https://app.eu.apidog.com/](https://app.eu.apidog.com/)

### Desktop Client Downloads

Apidog Europe requires a dedicated client that connects exclusively to### Desktop Client Downloads

<table>
  <thead>
    <tr>
      <th>OS</th>
      <th>Architecture / Format</th>
      <th>Download Link</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Windows</td>
      <td>64-bit</td>
      <td><a href="https://file-assets.eu.apidog.com/download/Apidog%20Europe-windows-latest.zip">Download</a></td>
    </tr>
    <tr>
      <td rowspan="2">macOS</td>
      <td>Intel Chip</td>
      <td><a href="https://file-assets.eu.apidog.com/download/Apidog%20Europe-macOS-latest.zip">Download</a></td>
    </tr>
    <tr>
      <td>Apple Silicon (M1/M2/M3)</td>
      <td><a href="https://file-assets.eu.apidog.com/download/Apidog%20Europe-macOS-arm64-latest.zip">Download</a></td>
    </tr>
    <tr>
      <td rowspan="5">Linux</td>
      <td>amd64 (.AppImage)</td>
      <td><a href="https://file-assets.eu.apidog.com/download/Apidog%20Europe-linux-latest.zip">Download</a></td>
    </tr>
    <tr>
      <td>amd64 (.deb)</td>
      <td><a href="https://file-assets.eu.apidog.com/download/Apidog%20Europe-linux-deb-latest.zip">Download</a></td>
    </tr>
    <tr>
      <td>amd64 (.tar.gz)</td>
      <td><a href="https://file-assets.eu.apidog.com/download/Apidog%20Europe-linux-manual-latest.tar.gz">Download</a></td>
    </tr>
    <tr>
      <td>arm64 (.AppImage)</td>
      <td><a href="https://file-assets.eu.apidog.com/download/Apidog%20Europe-linux-arm64-latest.zip">Download</a></td>
    </tr>
    <tr>
      <td>arm64 (.deb)</td>
      <td><a href="https://file-assets.eu.apidog.com/download/Apidog%20Europe-linux-arm64-deb-latest.zip">Download</a></td>
    </tr>
  </tbody>
</table>

## GDPR Compliance

Apidog Europe adheres to the General Data Protection Regulation (GDPR), ensuring your data is handled with the highest standards of privacy and protection. Key compliance features include:

- **European data residency**: All data is stored exclusively within Europe
- **Enhanced privacy controls**: Greater control over personal and sensitive information
- **Regulatory alignment**: Full compliance with EU data protection requirements

For complete details, refer to our [Privacy Policy](https://legal.apidog.com/privacy-policy-645650m0).

## Migrating from Apidog Global to Apidog Europe

If you need to move your projects from Apidog Global to Apidog Europe, follow these steps:

### Step 1: Export Data from Apidog Global

1. In Apidog Global, navigate to **Settings** in the left menu
2. Click **Export Data**
3. Select **Apidog** as the export format
4. Choose the API scope you want to export
5. Click **Export**

<Background>
![Export data from Apidog Global](https://assets.apidog.com/uploads/help/2023/11/30/97cf626a36112974cd308f6df2c61ff0.png)
</Background>

### Step 2: Import Data to Apidog Europe

1. Open Apidog Europe
2. Click the **Settings** icon for your project
3. Navigate to the **Manual** tab
4. Select **Apidog Europe** as the data source
5. Import the exported file

<Background>
![Import data to Apidog Europe](https://assets.apidog.com/uploads/help/2023/11/30/77aedd0c487297babc8450febfba02c4.png)
</Background>

### Step 3: Review and Confirm Import

1. Review the import preview
2. Select the items to import:
   - APIs
   - Schemas
   - Environments
   - Test Scenarios
3. Click **Confirm**

<Background>
![Import preview and confirmation](https://assets.apidog.com/uploads/help/2023/11/30/77773352d41bc9e859b42e2827fb7c96.png)
</Background>

## Support

For questions or assistance with Apidog Europe, contact our support team at [support@apidog.com](mailto:support@eu.apidog.com).

