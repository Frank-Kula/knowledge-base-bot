# Offline Space

Apidog Offline Space is a feature designed for developers who need to debug endpoints without an internet connection or want complete control over their data privacy. Whether you're working in restricted network environments, handling sensitive data, or simply prefer local-first workflows, Offline Space provides a fully offline debugging environment with all data stored locally on your device.


## Feature Highlights

| Feature | Description |
|---------|-------------|
| **Offline Debugging** | Debug endpoints without an internet connection, perfect for restricted network environments |
| **Local Data Storage** | All data is saved on your local device, ensuring complete data security and privacy |
| **Simple and Fast** | Easy to use with a minimal learning curve, even for first-time users |


## How to Use Offline Space

### Prerequisites

Before using Offline Space, ensure you have:
- The latest version of the Apidog desktop app installed
- Basic familiarity with API endpoint debugging in Apidog

### 1. Launch Offline Space

<Steps>
  <Step>
    Launch the Apidog desktop app.
  </Step>
  <Step>
    Click the `...` menu in the top bar.
  </Step>
  <Step>
    Choose "Offline Space" from the dropdown.
        
<Background>
![Accessing Offline Space from the menu](https://api.apidog.com/api/v1/projects/544525/resources/359243/image-preview)
</Background>

  </Step>
</Steps>

### 2. Work with Offline Space

Once you enter Offline Space, you have access to core debugging capabilities:

- **Create, open, or import collections** to organize your endpoints
- **Debug and test endpoints** with full request/response functionality
- **View endpoint response results** including headers, body, and status codes
- **Manage local data** with complete control over storage

<details>
<summary>📷 Visual Reference</summary>

<Background>
![Offline Space interface showing collection management](https://api.apidog.com/api/v1/projects/544525/resources/359244/image-preview)
</Background>

</details>


## FAQs

<Accordion title="Where is Offline Space data stored?" defaultOpen>
All data is stored on your local device and is never uploaded to the cloud. This ensures complete privacy and security for sensitive API data. You can manage your Offline Space data locally using version control systems like Git, allowing you to track changes, collaborate with team members, or back up your work as needed.
</Accordion>

<Accordion title="What features are supported in Offline Space?" defaultOpen={false}>
Currently, Offline Space supports core endpoint debugging functionality, including creating and managing collections, sending requests, viewing responses, and managing local data. As Offline Space is in beta, additional features may be added based on user feedback and development priorities. Check the Apidog release notes for updates on new capabilities.
</Accordion>

<Accordion title="Can I sync Offline Space data with my online projects?" defaultOpen={false}>
Offline Space is designed to operate independently from cloud-based projects. Data remains local to ensure privacy and offline functionality. If you need to share work between Offline Space and online projects, you can export and import collections manually.
</Accordion>

