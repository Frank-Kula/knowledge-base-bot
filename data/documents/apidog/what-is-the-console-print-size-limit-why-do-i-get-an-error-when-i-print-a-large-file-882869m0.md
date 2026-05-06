# What is the console print size limit? Why Do I Get an Error When I Print a Large File?

Apigog's console print size is `limited to 1024 * 1024` bytes (1MB). This is a limitation of Node.js, and currently Apidog does not support configuration modification of this limitation. If the content of the printed file is too large and exceeds this limit, an error will be reported.
