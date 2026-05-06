# Fixing ECONNREFUSED Error

The `ECONNREFUSED` error indicates that when the Apidog client attempted to connect to the target server at the specified IP address and port, **the connection was refused**.


## Possible Causes

This error is typically not caused by Apidog itself but stems from issues with the target server, network configuration, or local settings. Major causes include:

### 1. Target service is not running  
The API service or application you are trying to reach is **not started** on the server or has crashed at the time of the request.

### 2. Incorrect address or port  
The IP address, hostname, or port specified in the Apidog request URL is incorrect; the server is not listening on that endpoint.

### 3. Server-side firewall blocking connections  
The server’s firewall or cloud security group is configured to block connections from the Apidog client. The server receives the connection attempt but actively refuses it.

### 4. Client-side firewall blocking connections  
Your local machine’s firewall or security software is preventing the Apidog application from making outbound network connections.

### 5. Proxy misconfiguration  
Apidog is configured with incorrect proxy settings, so requests fail to reach the target server.



## How to Troubleshoot and Fix

Follow these steps to identify and resolve the issue:

### 1. Install the browser extension or use the desktop app  
If you are using the web version, install the [browser extension](https://docs.apidog.com/installing-apidog-chrome-extension-821769m0) before resending requests.  
Alternatively, use the [Apidog desktop app](https://apidog.com/download/) (recommended for greater stability).


### 2. Verify the target service status
- **Start or restart the service:** Make sure the target API/service is up and running on the host (server or local machine).  
- **Check service logs:** Review the server application logs for errors or crashes around the time you attempted the connection.


### 3. Validate connection details
- **Check the port:** Confirm the port in your Apidog request URL (for example, `http://127.0.0.1:3000/api/users`) matches the port the service is actually listening on.  
- **Verify the address:** Ensure the IP address or domain name is correct. If using `localhost` or `127.0.0.1`, confirm the service is running locally.


### 4. Inspect firewall and security settings
- **Server firewall / security group:** If the API is hosted remotely, confirm the server firewall or cloud security group allows inbound connections to the target port (e.g., 80, 443, 3000). Contact the server administrator if necessary.  
- **Local firewall / antivirus:** Temporarily disable your local firewall or security software to see if the issue resolves. If it does, add Apidog to the allowlist rather than leaving protections disabled.


### 5. Check Apidog proxy settings

1. Open **Apidog → Settings → Network Proxy**.  
2. Actions to take:
   - If you **do not** need a proxy to reach the target service, ensure proxy is **disabled** or set to “No proxy”.  
   - If you **do** require a proxy, verify the proxy host, port, and authentication credentials are correct.

      <Frame>
        ![image.png](https://api.apidog.com/api/v1/projects/544525/resources/363376/image-preview)
      </Frame>


If, after all these checks, the issue persists, engage the server-side administrators or hosting provider and provide them with the request time, source IP (if applicable), and the attempted endpoint so they can inspect server/network logs and firewall rules.


