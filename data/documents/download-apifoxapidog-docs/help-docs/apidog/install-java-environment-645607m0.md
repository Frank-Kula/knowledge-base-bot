# Install Java Environment

## Download and Install OpenJDK

Amazon Corretto is recommended:

* Windows (x64): https://corretto.aws/downloads/latest/amazon-corretto-8-x64-windows-jdk.msi
* macOS (Intel): https://corretto.aws/downloads/latest/amazon-corretto-8-x64-macos-jdk.pkg
* macOS (Apple silicon): https://corretto.aws/downloads/latest/amazon-corretto-8-aarch64-macos-jdk.pkg
* Linux (.deb): https://corretto.aws/downloads/latest/amazon-corretto-8-x64-linux-jdk.deb
* Linux (.rpm): https://corretto.aws/downloads/latest/amazon-corretto-8-x64-linux-jdk.rpm

Or visit the [AdoptOpenJDK](https://adoptopenjdk.net/releases.html) website to choose another OpenJDK distribution.

## Install OpenJDK via the package manager

### macOS

It is recommended to use Homebrew to install OpenJDK. You need to install [Homebrew](https://brew.sh/) first.

```shell
brew install openjdk
```

### Linux

It is recommended to use the system's built-in package manager to install OpenJDK.

If using CentOS, Rocky Linux, RHEL or Fedora:

```shell
sudo yum install java
```

If using Ubuntu、Debian:

```shell
sudo apt install openjdk-8-jdk
```

## Check whether the Java environment is installed successfully

Run `java -version` in the terminal. If the Java or OpenJDK version number can be displayed correctly, the installation is successful.

## FAQ

If the Java environment has been installed successfully but Apidog does not detect the Java environment, please try the following methods:

* Close Apidog and reopen it
* Restart the computer


