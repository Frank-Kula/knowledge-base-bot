# Web Requests Work, But App Gets "read ECONNRESET"—Why?

1. #### **Apidog Version Issue**
    **Update Apidog** : Ensure you're using the the latest version of Apidog, as older versions may have compitibility issues.
    
2. #### **Apidog Configuration Issues**
    **Adjust Timeout Settings:** Increase the request time-out in Apidog's settings to prevent premature connection resets.

    **Check SSL Verification**: 
    -      If the server uses HTTPS, verify that SSL settings are correct.
    -      For testing, you can temporarily disable SSL verification (not recommanded for production).
    -      To configure certificate, you can read - [CA and client certificates](https://docs.apidog.com/ca-and-client-certificates-629101m0.md)
  
3. #### **Firewall or Proxy Issues:**
     **Check Firewall Rules:** Ensure your firewall isn’t blocking Apidog’s requests. Test by temporarily disabling it (use with caution).
 **Review Proxy Settings:**
    - Compare proxy settings between the web client and Apidog.
    - If the web client doesn’t use a proxy, disable it in Apidog’s settings.


4. #### **Unstable Network Connection**
    - Use `ping` to check server reachability.
    - Use `traceroute` (Linux/Mac) or `tracert` (Windows) to diagnose routing issues.
    - **Switch Networks:** Try switching from Wi-Fi to mobile data (or vice versa) to rule out local network problems.

5. #### **High Server Load**
    - Check Server Status: Contact the server admin to monitor CPU, memory, and bandwidth usage.
    - Reduce Request Frequency: Lower the request rate in Apidog to see if the issue persists.

6. **Server-Side Configuration Issues**
    - Compare Request Headers: Ensure Apidog’s request headers match those of the web client (check browser DevTools).
    - Review Server Logs: Ask the server admin to check logs for errors or blocks related to Apidog requests.

