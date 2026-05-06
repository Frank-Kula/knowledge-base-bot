# Request proxy in Apidog web

When you log into Apidog via the web app, navigate to a project, and attempt to send a request to an endpoint, you might face Cross-Origin Resource Sharing (CORS) restrictions. To help users overcome this challenge, Apidog offers several types of request proxy agents:

<table border="1">
    <tr>
        <th>Request Proxy</th>
        <th>Description</th>
    </tr>
    <tr>
        <td>**Cloud Agent**</td>
        <td>
            - No installation required<br>
            - Supports sending HTTPS requests<br>
            - Requires connection to the Apidog cloud<br>
            - Cannot access private or local network environments
        </td>
    </tr>
    <tr>
        <td>**Browser Extension**</td>
        <td>
            - Installed locally<br>
            - Supports sending HTTPS requests<br>
            - Requires downloading the Apidog [Browser Extension](https://docs.apidog.com/installing-apidog-chrome-extension-821769m0.md)
        </td>
    </tr>
    <tr>
        <td>**Self-hosted Request Proxy Agent**</td>
        <td>
            - Deployed on a self-hosted server<br>
            - Supports sending HTTPS requests<br>
            - Requires server deployment<br>
            - Restricted by the network environment of the deployment server, possibly unable to access local network environments
        </td>
    </tr>
</table>

To choose which request proxy agent to use, go to the`Request Proxy`section located at the bottom right of the project page. By default, the system selects`Auto`mode. In this mode, if the browser extension is installed, it will be used to send requests. If not, the cloud agent will be employed for sending requests.

<Background>
![request-proxy-apidog.jpg](https://api.apidog.com/api/v1/projects/544525/resources/350181/image-preview)
</Background>
