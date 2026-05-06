# 批量运行场景用例

批量运行场景用例能够为测试人员节省大量的手动执行时间，你可以通过以下方法在 Apifox 中执行批量运行场景用例。

## 批量运行场景用例

点击场景用例下的 **“目录”**，在目录页中可以看到当前目录下的全部场景用例。批量勾选需要执行测试的场景，然后点击右上角的 **“批量运行”** 按钮，运行时将使用场景用例中的默认运行配置。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/528340/image-preview)
</Background>

可以根据实际需求设置是否在测试运行完成后发送通知。

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/528344/image-preview)
</Background>


批量运行完成后，你将看到批量运行测试报告，其中列出了所有执行的场景用例的结果，点击相应的场景用例，可以查看更详细的测试报告。

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/481817/image-preview)
</Background>

## 常见问题


<Accordion title="我可以在 CI/CD 中批量运行场景用例吗？" defaultOpen>
可以。在 CLI 中使用 `-f <folderId>` 命令，指定一个目录，来批量运行这个目录中的所有场景用例。如果你不同时使用 `-e` `-d` 等命令指定运行配置，则这些场景用例将使用自己保存的默认运行配置发起运行。[了解更多](https://docs.apifox.com/cli-command-options.md)
</Accordion>



