# Fixing ETIMEDOUT Error

**`ETIMEDOUT`** indicates that your request **exceeded the configured time limit** while waiting for a response from the target server.



## Possible Causes

There are three primary causes:

### 1. Network or firewall blocking

Your local firewall, antivirus software, or corporate network restrictions are preventing Apidog from establishing outbound connections.

### 2. Server or address issues

* The target server is not running, is unreachable, or the target port is blocked by a firewall.
* The requested URL or IP address is incorrect.

### 3. Apidog configuration issues

* The request timeout is set too short and the server has not yet responded.
* Proxy settings are incorrect, preventing the request from being sent.



## How to Fix

### 1. Install the browser extension or use the desktop app

If you are using the web version, install the [browser extension](https://docs.apidog.com/installing-apidog-chrome-extension-821769m0) before sending requests. Alternatively, use the [Apidog desktop app](https://apidog.com/download/) — **recommended** for greater stability.


### 2. Increase the timeout (most common)

In Apidog, go to **Settings → General** and increase the **Request timeout** value.

<Frame>

![image.png](https://api.apidog.com/api/v1/projects/544525/resources/363377/image-preview)

</Frame>



### 3. Check network and firewall

* **Local check:** Temporarily **disable** your firewall or antivirus to verify whether they are causing the timeout.
* **Network test:** Try a different network (for example, a mobile hotspot) to rule out corporate network restrictions.



### 4. Verify the server and address

* **Confirm service availability:** Ensure the target server is running and can be reached from other environments (for example, open the URL in a browser).
* **Validate the URL:** Double-check the request URL/IP and port for typos.



### 5. Check proxy settings

1. Open **Apidog → Settings → Network Proxy**.
2. Take the appropriate action:

   * If you **do not** need a proxy to reach the target service, ensure proxy is **disabled** or set to **No proxy**.
   * If you **do** require a proxy, verify the proxy host, port, and authentication credentials are correct.

      <Frame>
        ![image.png](https://api.apidog.com/api/v1/projects/544525/resources/363376/image-preview)
      </Frame>



If the timeout persists after these checks, consult the target service owner or administrator and provide request timestamps and the endpoint used so they can inspect server logs and network configurations.

