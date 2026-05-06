# What is the size limit for console printing?Why do I get an error when printing large files?

Apidog's console printing has a size limit of `1024 * 1024` bytes (1MB). This is a limitation of Node.js, and currently, Apidog does not support configuring this limit. If the printed file content exceeds this limit, an error will occur.
