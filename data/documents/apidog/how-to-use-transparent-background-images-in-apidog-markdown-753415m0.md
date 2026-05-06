# How to use transparent background images in Apidog Markdown?

Since most transparent background PNGs do not display well in dark mode, Apidog Markdown's default behavior is to add a white background color to transparent PNGs when in dark mode.

For example:

![](https://api.apidog.com/api/v1/projects/544525/resources/348079/image-preview)

If you want to display the PNG with a transparent background, you can use the following syntax in your Markdown:

```html
<img src="https://api.apidog.com/api/v1/projects/544525/resources/348079/image-preview" style="background-color: transparent; width: 64px"/>
```

The provided HTML code for displaying a transparent background image in Apidog Markdown will result in the following:

<img src="https://api.apidog.com/api/v1/projects/544525/resources/348079/image-preview" style="background-color: transparent; width: 64px"/>

This approach allows you to display transparent PNG images in Apidog Markdown without the default white background color being applied in dark mode. The transparent background will be maintained, providing a consistent appearance across light and dark modes.

This will ensure that the image is displayed with a transparent background, regardless of the user's light or dark mode setting. The `style="background-color: transparent;"` attribute overrides Apidog Markdown's default behavior and allows the image to be displayed with its original transparent background.

You can also adjust the width of the image by adding the `width: 64px` style attribute, or any other desired width.


