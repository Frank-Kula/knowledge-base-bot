# 安装 Java 环境

# 安装 Java 环境

Apifox 的生成业务代码功能依赖于 Java 环境，可以使用 OpenJDK 或 Oracle JDK，推荐使用 OpenJDK。

> JDK 版本需大于 `11`

## 下载安装 OpenJDK

推荐使用 Amazon Corretto：

* Windows (x64)：https://corretto.aws/downloads/latest/amazon-corretto-11-x64-windows-jdk.msi
* macOS (Intel)：https://corretto.aws/downloads/latest/amazon-corretto-11-x64-macos-jdk.pkg
* macOS (Apple silicon)：https://corretto.aws/downloads/latest/amazon-corretto-11-aarch64-macos-jdk.pkg
* Linux (.deb): https://corretto.aws/downloads/latest/amazon-corretto-11-x64-linux-jdk.deb
* Linux (.rpm): https://corretto.aws/downloads/latest/amazon-corretto-11-x64-linux-jdk.rpm

或者访问 [AdoptOpenJDK](https://adoptopenjdk.net/releases.html) 网站，选择其他 OpenJDK 发行版。

## 通过包管理器安装 OpenJDK

### macOS

推荐使用 Homebrew 安装 OpenJDK，需要先安装 [Homebrew](https://brew.sh/)。

```shell
brew install openjdk
```

### Linux

推荐使用系统内置的包管理器安装 OpenJDK。

如果使用 CentOS、Rocky Linux、RHEL 或 Fedora：

```shell
sudo yum install java
```

如果使用 Ubuntu、Debian：

```shell
sudo apt install openjdk-11-jdk
```

## 检查 Java 环境是否安装成功

在终端运行 `java -version` 命令，如能正确显示 Java 或 OpenJDK 的版本号，则表示安装成功。

# 常见问题

如果 Java 环境已经安装成功，但是 Apifox 没有检测到 Java 环境，请尝试以下方法：

* 关闭 Apifox，然后再重新打开
* 重启电脑

