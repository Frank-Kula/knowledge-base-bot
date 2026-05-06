# Apifox CLI

![NPM Version](https://img.shields.io/npm/v/apifox-cli)

Apifox CLI 是一个命令行工具，旨在执行和测试你的场景用例。它经过优化，具备高度的扩展性，可以轻松集成到你的持续集成 *（CI）* 服务器和构建系统中。

Apifox CLI 与 Apifox 端内功能完全一致，确保你能够以相同的方式运行场景用例。

在 Apifox 中编排好场景用例后，你可以根据实际需求选择使用可视化界面或 CLI 来执行测试。

两者的区别如下：

项目 | 端内可视化运行 | Apifox CLI
--- | --- | ---
测试报告 | 可视化报告 | 命令行报告
运行速度 | 相对较慢 | 相对较快
兼容性 | 只能在 Apifox 客户端中运行和查看 | 可以在任何操作系统的命令行以及 CI/CD 平台中运行和查看
多线程 | 支持多线程和性能测试 | 不支持多线程和性能测试
在线/离线 | 仅支持在线运行 | 支持在线/离线运行

## 快速开始

首先需要安装 Node.js 和 Apifox CLI，安装完成后就可以开始运行场景用例了。更多详细信息可以查看[安装和运行 Apifox CLI](https://docs.apifox.com/install-and-run-cli.md)。

## 配置选项

Apifox CLI 提供了一系列选项来自定义运行方式。可以查看 [CLI 命令选项](https://docs.apifox.com/cli-command-options.md)了解更多信息。

## 文件上传

Apifox CLI 支持文件上传，你可以使用数据文件 *（比如文本文件）* 来填充表单数据字段。详细了解[在 Apifox CLI 中上传文件](https://docs.apifox.com/cli-command-options.md)。

## 集成 CI/CD 平台

Apifox 提供了与主流 CI 工具的集成，让你可以在设计和测试 API 的同一个平台上直接监控 API 的构建。查看[集成 CI/CD](https://docs.apifox.com/cicd.md)了解更多信息。
