# Why published Share Docs is not showing the hostname?

### 1. Why hostname is not showing while I am try out brach API versions?
When using only one or multi-versions of API hosted site in Apidog (e.g., with separate environments for each version), the `Try it` feature doesn’t consistently display the environment’s hostname or variables. It many occur on the main version of the API as well unless you set **Environment** while publishing it.

### 2. How to resolve this issue?

To resolve the inconsistent hostname issue in Apidog’s `Try it` feature for the main or alternate versions, follow these steps provided by support:
#### Update the Share Doc Settings:
1. Open the "Share Docs" page in your Apidog project.page

<Background>
![image.png](https://api.apidog.com/api/v1/projects/544525/resources/352871/image-preview)
</Background>
If you have one one version od API, then you must confirm that the doc is configured with environment. you can find the setting on the same page.  Here you can also find that there is `No Environment` set for the API. So to avoid the issue, one should select the environment.

2. If you have multiple AI versions, select "Switch to multi-version mode" to manage versions explicitly.
<Background> 
![img_v3_02kt_4865798d-a4d9-4390-b013-b657048e87eg.png](https://api.apidog.com/api/v1/projects/544525/resources/352866/image-preview)
</Background>

3. Click "+Add" to configure the alternate version (As per the screenshots).
<Background>  
![img_v3_02kt_32176f1a-d668-4a3a-bb68-29c3ce51fcdg.png](https://api.apidog.com/api/v1/projects/544525/resources/352867/image-preview)
</Background>

4. In the new entry: Select the alternate API version (e.g., v0.9).

5. Input the version number.

6. Choose the environment you want to use.

7. Add a unique slug (e.g., alt-0-9).

<Background>
  
![img_v3_02kt_966de502-c0c6-4cd4-a896-e92246013e8g.jpg](https://api.apidog.com/api/v1/projects/544525/resources/352869/image-preview)
</Background>


9. Save the changes.

Reload the published documentation. Use `Try it` now on the alternate version’s endpoint. The issue is supposed to be resolved.









