# How to set the column width of a Markdown table?

You can use the `div` element in HTML and apply inline styles to adjust the column width. For example:

    ```
    | <div style="width: 130px;">Name</div> | Age | Gender | Email |  
    | --- | --- | --- | --- |  
    | John Doe | 25 | Male | [johndoe@example.com](mailto:johndoe@example.com) |  
    | Jane Smith | 30 | Female | [janesmith@example.com](mailto:janesmith@example.com) |  
    | Mike Johnson | 35 | Male | [mikejohnson@example.com](mailto:mikejohnson@example.com) |
    ```

Rendered table:

| <div style="width: 130px;">Name</div> | Age | Gender | Email |  
| --- | --- | --- | --- |  
| John Doe | 25 | Male | [johndoe@example.com](mailto:johndoe@example.com) |  
| Jane Smith | 30 | Female | [janesmith@example.com](mailto:janesmith@example.com) |  
| Mike Johnson | 35 | Male | [mikejohnson@example.com](mailto:mikejohnson@example.com) |
