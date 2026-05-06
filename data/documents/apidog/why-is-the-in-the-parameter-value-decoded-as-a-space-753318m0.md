# Why is the "+" in the parameter value decoded as a space?

In URL encoding rules, within form data, the space character (' ') needs to be encoded as a '+' sign, because using spaces directly in URLs is unsafe, and '%20' (the URL encoded form of a space) is longer and harder to read. Therefore, when URLs or form data are received and decoded by a web server, the '+' sign is decoded as a space. This is because in the application/x-www-form-urlencoded MIME type data, '+' is used as a substitute for spaces.

![image.png](https://api.apidog.com/api/v1/projects/544525/resources/348294/image-preview)

![image.png](https://api.apidog.com/api/v1/projects/544525/resources/348295/image-preview)


### How to Encode "+" in value:

If you want to encode "+" in value, you can easily do so using the auto-encode function. Here's how:

1. Select the Text: Highlight the text that contains spaces.
2. Right-Click: Click the right mouse button.
3. Choose Auto-Encode: Select the Encode option from the context menu.
![image.png](https://api.apidog.com/api/v1/projects/544525/resources/349182/image-preview)
4. View the Encoded Result: After selecting the Encode option, the text will be automatically converted. You will see the encoded result displayed, where special characters are replaced with their encoded equivalents.
![image.png](https://api.apidog.com/api/v1/projects/544525/resources/349327/image-preview)


