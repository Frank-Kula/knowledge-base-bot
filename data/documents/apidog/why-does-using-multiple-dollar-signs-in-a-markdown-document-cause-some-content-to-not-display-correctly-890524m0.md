# Why Does Using Multiple Dollar Signs in a Markdown Document Cause Some Content to Not Display Correctly?

The Markdown editor used by Apidog parses `$xxxxx$` into mathematical formulas. If your content isn't a math formula, but contains multiple `$`, it may fail to parse and not display correctly.
To avoid this, the following methods can be employed:

#### Method 1. Use inline code blocks
Include the code content in backticks', for example

<Container>

<Columns>
  
  <Column>
      Original
   ```js
Using {{$.stepid.element}} allows you to reference the value of a loop variable. When the step ID is 2, the current loop value would be {{$.2.element}}.
```
  </Column>
  <Column>
       Display effects
<Container>
  Use `{{$.step.element}}` to refer to the value of a loop variable. When step ID is 2, the value of the current loop is `{{$.2.element}}`
    </Container>
  </Column>
</Columns>

</Container>
#### Method 2. Use escape charecters
Add a backlash `\` before the `$` sign for escape, for example - 
<Container>

<Columns>
  
  <Column>
      Original
   ```js
Using `{{$.stepid.element}}` allows you to reference the value of a loop variable. When the step ID is 2, the current loop value would be `{{$.2.element}}`.
```
  </Column>
  <Column>
     Display effects
      
<Container>
Use `{{$.step id.element}}` to refer to the value of a loop variable. When step ID is 2, the value of the current loop is `{{$.2.element}}ment}}`.   
    </Container>
  </Column>
</Columns>

</Container>



