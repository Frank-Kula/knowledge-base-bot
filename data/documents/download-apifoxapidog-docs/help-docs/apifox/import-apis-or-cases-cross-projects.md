# 跨项目导入接口/用例

场景用例支持跨项目导入接口与接口用例。这意味着除了可以引用本项目中的接口导入作为步骤之外，还支持导入其它项目的接口作为步骤，共同组成一个完整的业务流程，这对于有着复杂业务流程的系统或架构而言非常重要。

## 导入接口

在弹出框中点击项目名称，选择其它项目的接口进行导入。导入其它项目中的接口时，仅支持 “手动同步” 方式，不影响原项目的接口用例数据。

> 有关于 “手动同步” 与 “自动同步” 模式间的区别，详细说明请参考[此文档](https://docs.apifox.com/sync-from-endpoint-or-test-case.md)。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/481675/image-preview)
</Background>


当你选择了某个其它项目并首次导入该项目的数据作为测试步骤时，为了确保这些步骤能够正常运行，避免出现不按预期使用服务（前置 URL）的问题发生，产品页面将引导你进行 **“环境关联”** 设置，将这个其它项目的环境，与当前项目的环境关联起来。详情请参考[管理其它项目接口的运行环境](https://docs.apifox.com/manage-cross-project-environments.md)。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/481676/image-preview)
</Background>


> 导入其它项目时，或者运行含有其它项目接口的场景用例时，至少需拥有该项目的只读权限。关于项目权限的详细说明，请参考阅读[此文档](https://docs.apifox.com/member-roles-and-permissions.md)。

## 导入接口用例

点击项目名称，选择其它项目的接口用例进行导入。导入其它项目的接口用例时，仅支持 “复制” 导入方式。即单向导入，不影响原项目的接口用例数据。

- **复制**

    将接口用例以 **“复制”** 方式导入，接口用例中的参数名、参数值会同时复制至测试步骤中，和原项目中的接口用例数据完全独立，各自改动后互不影响。若希望将测试步骤与原项目的接口文档进行关联，可以点击 “立即同步” 按钮同步接口文档中的各项参数名。

为确保数据的稳定和独立，这些由外部项目导入而来的接口、接口用例仅支持与原项目的接口文档使用 **“手动同步”** 方式同步数据。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/481678/image-preview)
</Background>


