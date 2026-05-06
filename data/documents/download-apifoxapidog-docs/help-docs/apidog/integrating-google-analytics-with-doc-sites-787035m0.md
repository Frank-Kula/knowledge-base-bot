# Integrating Google Analytics with Doc Sites

> Apidog version 2.6.41 or later is required.

The Apidog doc sites now supports integration with Google Analytics. This allows you to track important metrics like page views, user behavior, and other key analytics directly through Google Analytics.


## How to Integrate Google Analytics with Apidog？

To get started, you'll need a Google Analytics account. If you don’t have one yet, you can easily sign up here: https://marketingplatform.google.com/about/analytics/

Once you’ve created your account, follow these steps to integrate Google Analytics with Apidog.

### Step 1: Create a Property

After registering, you can create a "Property" in the settings.

<Background>
![creating property at Apidog.png](https://api.apidog.com/api/v1/projects/544525/resources/348852/image-preview)
</Background>

When setting up a new property, you’ll need to create a "Web Stream" for your site. 

<Background>
![creating web stream.png](https://api.apidog.com/api/v1/projects/544525/resources/348853/image-preview)
</Background>

For the "Website URL", simply use the URL of your Apidog doc site. After entering the URL, click "Create & Continue".

<Background>
![entering Apidog doc site URL.png](https://api.apidog.com/api/v1/projects/544525/resources/348854/image-preview)
</Background>

### Step 2: Integrate Google Analytics with Apidog

Once the web stream is created, Google Analytics will usually prompt you to add a tracking code to your site. However, with Apidog, you don’t need to manually add any code. All you need to do is input your "Measurement ID" into the settings page of your Apidog doc site.

To find your "Measurement ID", return to the Google Analytics homepage and navigate to ："Settings" → "Data streams" in the left sidebar.

<Background>
![data stream settings at Google Analytics.png](https://api.apidog.com/api/v1/projects/544525/resources/348855/image-preview)
</Background>

From there, locate the Measurement ID for your site and copy it.

<Background>
![copy the measurement ID.png](https://api.apidog.com/api/v1/projects/544525/resources/348856/image-preview)
</Background>

Go to the settings page of your Apidog doc site. 

<Background>
![doc site setting page at Apidog.png](https://api.apidog.com/api/v1/projects/544525/resources/348857/image-preview)
</Background>   

Under the Google Analytics section, paste the "Measurement ID" (be sure to exclude the "G-" prefix).

<Background>
![entering measure ID into Apidog GA settings.png](https://api.apidog.com/api/v1/projects/544525/resources/348858/image-preview)
</Background>

Once you've entered the Measurement ID, save your settings. Your Google Analytics setup will now be connected to your Apidog doc site.

### Step 3: Verify the Integration

To check if everything is working, simply visit your doc site and interact with it —— browse, click around, etc. Then, go back to Google Analytics, click on "Reports" → "Realtime pages", and you should see live data reflecting the actions you just performed.

Now, you’ll be able to track and analyze real-time user data on your doc site with ease!

<Background>
![image.png](https://api.apidog.com/api/v1/projects/544525/resources/348859/image-preview)
</Background>



