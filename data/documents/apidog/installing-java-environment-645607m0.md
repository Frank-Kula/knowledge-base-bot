# Installing Java Environment

Apidog requires a Java environment for certain advanced features, such as running custom scripts and executing automated tests with Java-based libraries. This guide provides step-by-step instructions for installing the Java Development Kit (JDK) on different operating systems.

### Prerequisites

Before installing Java, ensure you have:
- Administrator or sudo access on your system
- Knowledge of your operating system (Windows, macOS, or Linux)
- Knowledge of your system architecture (x64, ARM, etc.)

## Download and Install OpenJDK

Amazon Corretto is recommended for optimal compatibility with Apidog:

| Platform | Download Link |
|----------|--------------|
| Windows (x64) | [amazon-corretto-8-x64-windows-jdk.msi](https://corretto.aws/downloads/latest/amazon-corretto-8-x64-windows-jdk.msi) |
| macOS (Intel) | [amazon-corretto-8-x64-macos-jdk.pkg](https://corretto.aws/downloads/latest/amazon-corretto-8-x64-macos-jdk.pkg) |
| macOS (Apple silicon) | [amazon-corretto-8-aarch64-macos-jdk.pkg](https://corretto.aws/downloads/latest/amazon-corretto-8-aarch64-macos-jdk.pkg) |
| Linux (.deb) | [amazon-corretto-8-x64-linux-jdk.deb](https://corretto.aws/downloads/latest/amazon-corretto-8-x64-linux-jdk.deb) |
| Linux (.rpm) | [amazon-corretto-8-x64-linux-jdk.rpm](https://corretto.aws/downloads/latest/amazon-corretto-8-x64-linux-jdk.rpm) |

Alternatively, visit the [AdoptOpenJDK](https://adoptopenjdk.net/releases.html) website to choose another OpenJDK distribution.

:::tip[Recommended Version]
Apidog works best with Java 8 (JDK 8) or higher. Amazon Corretto 8 is recommended for stability and long-term support.
:::

## Install OpenJDK via Package Manager

### macOS

It is recommended to use Homebrew to install OpenJDK. You need to install [Homebrew](https://brew.sh/) first.

```shell
brew install openjdk
```

:::info[macOS Setup]
After installation, you may need to add OpenJDK to your PATH. Follow the instructions displayed by Homebrew after installation.
:::

### Linux

It is recommended to use the system's built-in package manager to install OpenJDK.

**For CentOS, Rocky Linux, RHEL, or Fedora:**

```shell
sudo yum install java
```

**For Ubuntu or Debian:**

```shell
sudo apt install openjdk-8-jdk
```

:::tip[Linux Distributions]
Most modern Linux distributions include OpenJDK in their default repositories, making installation straightforward.
:::

## Verify Installation

Run `java -version` in the terminal. If the Java or OpenJDK version number can be displayed correctly, the installation is successful.

**Expected output:**

```
openjdk version "1.8.0_xxx"
OpenJDK Runtime Environment (build 1.8.0_xxx)
OpenJDK 64-Bit Server VM (build 25.xxx, mixed mode)
```

## Troubleshooting

If the Java environment has been installed successfully but Apidog does not detect the Java environment, please try the following methods:

- Close Apidog and reopen it
- Restart the computer
- Verify that Java is in your system PATH by running `echo $PATH` (macOS/Linux) or `echo %PATH%` (Windows)

:::warning[Detection Issues]
If Apidog still cannot detect Java after restarting, ensure that the JAVA_HOME environment variable is properly configured on your system.
:::

## References

- [Amazon Corretto Documentation](https://docs.aws.amazon.com/corretto/)
- [AdoptOpenJDK](https://adoptopenjdk.net/)

