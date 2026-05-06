# Apifox Linux 桌面版下载安装


:::tip[]
👉 [Mac 桌面版、Windows 桌面版下载安装](https://docs.apifox.com/download)
:::

## 一、前置准备
1. 确认系统架构
首先需明确系统架构，避免下载错误版本，终端执行以下命令查看：

```js
uname -a 
```
- 若输出含 x86_64：64 位 Intel/AMD 处理器
- 若输出含 i386/i686/i586：32 位 Intel/AMD 处理器
- 若输出含 arm64/aarch64：64 位 ARM 处理器（如树莓派 4B、ARM 云服务器）
- 若输出含 armhf：32 位 ARM 处理器

2. 安装包格式选择

| 安装包格式 | 适用系统 | 优势 |
| --- | --- |--- |
| .deb | Debian、Ubuntu、Linux Mint、Deepin、Kali 等 | 原生适配，支持系统级安装 / 卸载 |
| .AppImage | 所有主流 Linux 发行版（Ubuntu、Fedora、CentOS、Arch 等） | 免安装、便携性强，解压即可运行 |
| .tar.gz | 几乎所有 Linux 发行版 | 兼容性强，可自定义安装路径 |

点击跳转下载安装包：[Linux 桌面版下载](https://docs.apifox.com/download.md)

## 二、安装步骤
<Tabs>
<Tab title=".deb 安装">
<Steps>
  <Step title="下载安装包">
在终端运行命令进行快捷下载      
```
wget https://file-assets.apifox.com/download/Apifox-linux-deb-latest.zip
```
<Background>
<img src="https://api.apifox.com/api/v1/projects/5097254/resources/593990/image-preview"  />
</Background>   
  </Step>
  <Step title="解压安装包">
在安装包的所在目录运行命令解压文件
```
unzip Apifox-linux-deb-latest.zip      
```
<Background>
<img src="https://api.apifox.com/api/v1/projects/5097254/resources/597238/image-preview"  />    
</Background>      
  </Step>
  <Step title="安装文件">
运行命令完成 Apifox 的安装
```
sudo dpkg -i apifox_2.7.49_amd64.deb      
```
<Background>
<img src="https://api.apifox.com/api/v1/projects/5097254/resources/597239/image-preview"  />   
</Background>        
  </Step>
   <Step title="打开文件">
安装成功后，在应用栏中找到 Apifox 并打开。
<Background>
<img src="https://api.apifox.com/api/v1/projects/5097254/resources/593997/image-preview"  width="600px"/>
</Background>              
  </Step>   
</Steps>
  </Tab>

    
  <Tab title=".AppImage 安装">
 <Steps>
  <Step title="下载压缩包">
在终端运行命令进行快捷下载
```
wget https://file-assets.apifox.com/download/Apifox-linux-latest.zip
```
<Background>
<img src="https://api.apifox.com/api/v1/projects/5097254/resources/593999/image-preview"  />
</Background>   
  </Step>
     
  <Step title="解压文件">
在安装包的所在目录运行命令解压文件
```
unzip Apifox-linux-latest.zip
```
<Background>
<img src="https://api.apifox.com/api/v1/projects/5097254/resources/597240/image-preview"  />    
</Background>        
  </Step>
     
  <Step title="运行文件">
运行命令打开 Apifox

```
chmod a+x Apifox.AppImage
./Apifox.AppImage
```
<Background>
<img src="https://api.apifox.com/api/v1/projects/5097254/resources/594001/image-preview"  />
</Background>         
  </Step>   
</Steps>
  </Tab>
    
    
  <Tab title=".tar.gz 安装">
<Steps>
 <Step title="下载压缩包">
在终端运行命令进行快捷下载      
```
wget https://file-assets.apifox.com/download/Apifox-linux-manual-latest.tar.gz
```
<Background>
<img src="https://api.apifox.com/api/v1/projects/5097254/resources/594003/image-preview"  />
</Background>   
     </Step>   
<Step title="解压文件">
运行命令打开 Apifox
```
tar -zxvf Apifox-linux-manual-latest.tar.gz
cd apifox-2.x.x/
./apifox
```
<Background>
<img src="https://api.apifox.com/api/v1/projects/5097254/resources/594004/image-preview"  />
</Background>   
<Background>
<img src="https://api.apifox.com/api/v1/projects/5097254/resources/594005/image-preview"  />
</Background>      
    
  </Step>    
</Steps>
  </Tab>
    
</Tabs>
