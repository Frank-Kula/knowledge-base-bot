# Import from apiDoc

Apidog supports importing data from [apiDoc](https://apidocjs.com/). You can generate `api_data.json` or `api_data.js` files from your source code and import them directly.

## Phase 1: Generate Data

1.  Navigate to your project's root directory.
2.  Run the following command to parse your source code (`src`) and output the data to a distribution folder (`dist`).

    ```bash
    npx apidoc@0.29.0 -i src -o dist
    ```

    *   `src`: The directory containing your API source code annotations.
    *   `dist`: The output directory where the data files will be generated.

    <details>
    <summary>📷 Visual Reference: Output</summary>
    <img src="https://assets.apidog.com/uploads/help/2023/07/11/ad035ab81eee424783abc19ff534ceba.png" width="300px" />
    </details>

## Phase 2: Import into Apidog

<Steps>
  <Step>
    **Upload File**

    Go to **Settings** > **Import Data**. Select **apiDoc** and upload the `api_data.json` or `api_data.js` file from your `dist` folder.

  </Step>
</Steps>
