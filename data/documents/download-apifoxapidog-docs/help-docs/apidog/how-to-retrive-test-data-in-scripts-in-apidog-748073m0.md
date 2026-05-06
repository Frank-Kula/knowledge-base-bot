# How to retrive test data in scripts in Apidog?

You can access the test data variables in scripts as shown below:

`pm.iterationData.has(variableName:String)`: function → Boolean: Check whether a test variable exists.
`pm.iterationData.get(variableName:String)`: function → *: get a test variable.
`pm.iterationData.replaceIn(variableName:String)`: function: replace dynamic variables in a string with their actual values.
`pm.iterationData.toObject()`: function → Object: get all local variables as objects.
