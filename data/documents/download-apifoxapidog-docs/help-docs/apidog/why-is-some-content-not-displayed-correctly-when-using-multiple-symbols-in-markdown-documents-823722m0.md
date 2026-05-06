# Why is some content not displayed correctly when using multiple $ symbols in Markdown documents?

Apidog's Markdown editor interprets `$xxxxx$` as mathematical formulas. If your content is not a mathematical formula but contains multiple $, it may cause parsing failures and thus fail to display correctly.
To avoid this situation, you can adopt the following methods:
#### Method One: Use Inline Code Blocks
Enclose the code content with backticks, for example:

<Container>

<Columns>
  
  <Column>
      Original Text
   ```js
Using `{{$.stepId.element}}` can reference the value of the loop variable. When the setpID is 2, the current value of the loop is `{{$.2.element}}`. 
```
  </Column>
  <Column>
       Display
      
<Container>
Using `{{$.stepId.element}}` can reference the value of the loop variable. When the setpID is 2, the current value of the loop is `{{$.2.element}}`. 
    </Container>
  </Column>
</Columns>

</Container>

#### Method Two: Use Escape Characters
Add a backslash `\` before the `$` symbol to escape it, for example:
<Container>

<Columns>
  
  <Column>
      Original Text
   ```js
Using {{\$.stepId.element}} can reference the value of the loop variable. When the setpID is 2, the current value of the loop is {{\$.2.element}}.  
```
  </Column>
  <Column>
      Display
      
<Container>
Using {{\$.stepId.element}} can reference the value of the loop variable. When the setpID is 2, the current value of the loop is {{\$.2.element}}.
    </Container>
  </Column>
</Columns>

</Container>




