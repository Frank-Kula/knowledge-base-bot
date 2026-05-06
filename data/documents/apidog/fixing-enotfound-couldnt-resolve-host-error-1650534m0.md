# Fixing ENOTFOUND: Couldn't resolve host Error

The `ENOTFOUND: Couldn't resolve host` error indicates that the system failed to resolve the domain name or hostname in your request to its corresponding IP address. In other words, the **DNS lookup failed** — the very first step of a network request.



## Possible Causes

This error is primarily related to the **DNS (Domain Name System)**, not to whether the target server is running.

### 1. Typo or Malformed Domain
* **Misspelled domain:** The domain in your request URL is incorrect, missing a `/`, or contains an extra `/`, causing DNS lookup to fail.
* **Invalid URL format:** The URL might be missing the protocol prefix, such as `http://` or `https://`.

### 2. Local DNS or Hosts File Issues
* **Corrupted DNS cache:** Your computer or router may have cached incorrect DNS records.
* **Incorrect hosts file entry:** Your local `hosts` file (used to override DNS resolution) might contain outdated or invalid entries for the requested domain.

### 3. Network or Firewall Restrictions
* **Disconnected or unstable network:** Your device is offline or has an unstable internet connection.
* **Faulty DNS server:** The DNS server configured on your network (e.g., router or ISP DNS) is malfunctioning or unreachable.
* **VPN/proxy interference:** A misconfigured VPN or proxy is blocking or altering normal DNS lookups.
* **Firewall restrictions:** Your local firewall or security software may be blocking DNS requests (usually UDP port 53).



## How to Fix It

Follow these steps to troubleshoot and fix the `ENOTFOUND: Couldn't resolve host` error.

### 1. Install the Extension or Use the Desktop App

If you’re using the web version, install the [browser extension](https://docs.apidog.com/installing-apidog-chrome-extension-821769m0) before sending requests, or use the [desktop app](https://apidog.com/download/) instead (recommended).

### 2. Verify and Correct the Domain/URL

* **Double-check the domain:** Carefully review the full **URL** or **Base URL** you are using in Apidog. Ensure the domain name is spelled correctly and formatted properly (no missing or extra `/`).
  * Example: make sure it’s `api.example.com` rather than `api.exampel.com`.
* **Check URL format:** Ensure the URL starts with `http://` or `https://`.
* If your Base URL uses environment variables, confirm that the variable values are correct.

### 3. Refresh Local DNS Resolution

* **Test in browser:** Try opening the same URL directly in your browser.  
  If the browser can’t reach it either, the issue is likely local (your computer or network).

* **Flush DNS cache:**
  * **Windows:** Run `ipconfig /flushdns` in Command Prompt (CMD).
  * **macOS:** Run `sudo dscacheutil -flushcache; sudo killall -HUP mDNSResponder` in Terminal.

* **Check your hosts file:**
  * **Windows:** `C:\Windows\System32\drivers\etc\hosts`
  * **macOS/Linux:** `/etc/hosts`
  * Remove or comment out (add `#` at the beginning of the line) any entries related to the domain you’re testing.

### 4. Check Network and Proxy Configuration

* **Change DNS servers:** Temporarily switch to public DNS servers such as Google DNS (`8.8.8.8`), then try again.
* **Inspect VPN/proxy settings:**
  * Try disabling your VPN or proxy and send the request again.
  * If a proxy is required, go to **Settings → Network Proxy** in Apidog and verify that the proxy configuration is correct.
  
      <Frame>
    ![image.png](https://api.apidog.com/api/v1/projects/544525/resources/363376/image-preview)
      </Frame>

* **Restart network devices:** Restart your router or modem to clear potential network or DNS issues.


By following these steps, you should be able to identify and resolve the root cause of the `ENOTFOUND: Couldn't resolve host` error in Apidog.


