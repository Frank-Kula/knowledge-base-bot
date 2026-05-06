# Why Am I Getting Error NJS-045 When Connecting to an Oracle Database in Apidog?

> “NJS-045: cannot load a node-oracledb binary for Node.js 18.18.2 (darwin arm64)”

This issue arises because Oracle currently has compatibility limitations with the ARM64 architecture. As a result, the `oracledb` driver does not support ARM64 at this time.
