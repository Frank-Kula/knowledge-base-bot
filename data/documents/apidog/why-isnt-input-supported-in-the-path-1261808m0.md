# Why isn't "#" input supported in the path?

#### Why does the path input "#" prompt that is is not supported?

This is a design feature. The "#" (hash) in a URL is a [Fragment Identifier](https://en.wikipedia.org/wiki/URI_fragment) that instructs the browser to jump to a specific location within the page (e.g., an HTML element with a corresponding id).
According to the HTTP protocol specification, the "#" and subsequent content are not sent to the server, so the server cannot directly get the "#" part of the path. Therefore, when Apidog detects that the path contains a "#", it will prompt that the symbol is not supported to avoid invalid requests or logical errors.

#### How do I pass identity like "#"?

If the business needs to pass an identifier like "#", it is recommended to replace the `#` with `%23` (URL-encoded "#"), and then manually parse and restore the parameter after the server receives the parameters. Example: Change `path#value` to `path%23value`.
