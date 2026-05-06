# Oracle Client

To connect to an Oracle database in Apidog, you must verify that the **Oracle Instant Client** is installed on your machine.

## Windows Installation

1.  **Download**: Visit the [Oracle Instant Client Downloads](https://www.oracle.com/database/technologies/instant-client/downloads.html) and download the **Basic Package (ZIP)** for Windows x64.
2.  **Extract**: Unzip the file to a directory, e.g., `C:\oracle\instantclient_19_3`.
3.  **Environment Variable**: Add this directory path to your system's `PATH` environment variable.
4.  **Restart**: Restart Apidog to apply changes.

## macOS Installation

1.  **Download**: Download the [macOS 64-bit Instant Client](https://www.oracle.com/database/technologies/instant-client/macos-intel-x86-downloads.html).
2.  **Extract**: Unzip to a directory, e.g., `~/oracle/instantclient_19_8/`.
3.  **Link Library**: Create a symbolic link for the library file to `/usr/local/lib`.
    ```bash
    ln -s ~/oracle/instantclient_19_8/libclntsh.dylib /usr/local/lib/
    ```
    *(If `/usr/local/lib` does not exist, create it first).*
4.  **Restart**: Restart Apidog.

## Linux Installation

1.  **Download**: Visit the [Oracle Instant Client for Linux](https://www.oracle.com/database/technologies/instant-client/linux-x86-64-downloads.html).
2.  **Install**: Follow the official installation instructions for your specific distribution (RPM or ZIP).
3.  **Restart**: Restart Apidog.

