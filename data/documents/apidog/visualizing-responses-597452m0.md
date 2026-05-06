# Visualizing Responses

Apidog allows you to programmatically render API response data as HTML. This is useful for turning JSON data into tables, charts, or images directly within the **Visualize** tab of the response panel.

<Background>
  ![Visualizer Example](https://assets.apidog.com/uploads/help/2023/07/27/06605f110095a2ae2864dcd896d827b0.jpg)
</Background>

## How to Visualize Data

1.  **Add Script**: In the **Post Processors**, add a Custom Script.
2.  **Use `pm.visualizer.set()`**: Define an HTML template and pass data to it.

```javascript
// 1. Prepare Data
var resp = {
    response: pm.response.json()
};

// 2. Define Template (Handlebars)
var template = `
    <div style="text-align: center; margin-top: 20px;">
        <h3>{{response.title}}</h3>
        <img src="{{response.url}}" />
    </div>
`;

// 3. Render
pm.visualizer.set(template, resp);
```

3.  **View Result**: Send the request and switch to the **Visualize** tab in the response section.

<Background>
  ![Visualize Tab](https://assets.apidog.com/uploads/help/2023/07/27/1b9886ee7c830a28c5b8a11044ad2325.jpg)
</Background>

## API Reference

### `pm.visualizer.set(template, data, options)`
*   **template** (`string`): HTML string. Supports [Handlebars](https://handlebarsjs.com/) syntax. You can include `<style>` and `<script>` tags.
*   **data** (`object`, optional): Data object to bind to the template.
*   **options** (`object`, optional): Handlebars compilation options.

### `pm.getData(callback)`
This function is available **inside the template's `<script>` tag**. It retrieves the data passed from `pm.visualizer.set`.

```javascript
const template = `
    <div id="container"></div>
    <script>
        pm.getData(function(err, data){
            document.getElementById('container').innerText = data.name;
        })
    </script>
`;

pm.visualizer.set(template, { name: 'Apidog' });
```

