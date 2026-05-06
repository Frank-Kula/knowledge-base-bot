# Download and Installation of Linux Desktop Version

## I. Preparations
1. Confirm System Architecture
First, you need to clarify the system architecture to avoid downloading the wrong version. Run the following command in the terminal to check:

```js
uname -a 
```

- If the output contains x86_64: 64-bit Intel/AMD processor
- If the output contains i386/i686/i586: 32-bit Intel/AMD processor
- If the output contains arm64/aarch64: 64-bit ARM processor (e.g., Raspberry Pi 4B, ARM cloud server)
- If the output contains armhf: 32-bit ARM processor

2. Selection of Installation Package Format

| Installation Package Format | Applicable Systems |Advantages|
| --- | --- | --- |
| .deb | Debian, Ubuntu, Linux Mint, Deepin, Kali, etc. | Natively compatible; supports system-level installation and uninstallation |
| .AppImage | All mainstream Linux distributions (Ubuntu, Fedora, CentOS, Arch, etc.) | No installation required; high portability; directly executable |
| .tar.gz | Almost all Linux distributions | Strong compatibility; supports custom installation directories |

## Ⅱ. Installation Steps

<Tabs>
  <Tab title=".deb installation">
<Steps>
  <Step title="Download the installation package">
Run commands in the terminal for quick download.
      
```
wget https://file-assets.apidog.com/download/Apidog-linux-deb-latest.zip
```
     
<Background>
<img src="https://api.apidog.com/api/v1/projects/544525/resources/368368/image-preview"  />
</Background>   
  </Step>
  <Step title="Unzip the installation package ">
Run the command to extract the file in the directory where the installation package is located.
```
unzip Apidog-linux-deb-latest.zip      
```      
<Background>
<img src="https://api.apidog.com/api/v1/projects/544525/resources/368369/image-preview"  />    
</Background>       
  </Step>
  <Step title="Installation File">
Run the command to complete the installation of Apidog.
```
sudo dpkg -i apidog_2.7.57_amd64.deb      
```  
<Background>
<img src="https://api.apidog.com/api/v1/projects/544525/resources/368370/image-preview"  />   
</Background>          
  </Step>
  <Step title="Open File">
After successful installation, find Apidog in the application bar and open it. 
<Background>
<img src="https://api.apidog.com/api/v1/projects/544525/resources/368371/image-preview"  />   
</Background>   
  </Step>
</Steps>

  </Tab>
  <Tab title=".AppImage installation">
<Steps>
  <Step title="Download the installation package">
Run commands in the terminal for quick download.
      
```
wget https://file-assets.apidog.com/download/Apidog-linux-latest.zip
```
     
<Background>
<img src="https://api.apidog.com/api/v1/projects/544525/resources/368373/image-preview"  />
</Background>   
  </Step>
  <Step title="Unzip the installation package">
Run the command to extract the file in the directory where the installation package is located.
```
unzip Apidog-linux-latest.zip    
```  
<Background>
<img src="https://api.apidog.com/api/v1/projects/544525/resources/368374/image-preview"  />   
</Background>          
  </Step>
<Step title="Run File">
Run the command to open Apidog.
```
chmod a+x Apidog.AppImage
./Apidog.AppImage
```  
<Background>
<img src="https://api.apidog.com/api/v1/projects/544525/resources/368375/image-preview"  />   
</Background>          
  </Step>
</Steps>

  </Tab>
  <Tab title=".tar.gz installation">
<Steps>
  <Step title="Download the installation package">
Run commands in the terminal for quick download.
      
```
wget https://file-assets.apidog.com/download/Apidog-linux-manual-latest.tar.gz
```
     
<Background>
<img src="https://api.apidog.com/api/v1/projects/544525/resources/368376/image-preview"  />
</Background>   
  </Step>
  <Step title="Unzip the installation package">
Run the command to extract the file in the directory where the installation package is located.
```
tar -zxvf Apidog-linux-manual-latest.tar.gz 
```  
<Background>
<img src="https://api.apidog.com/api/v1/projects/544525/resources/368377/image-preview"  />   
</Background>          
  </Step>    

  <Step title="Run File">
Run the command to open Apidog.
```
cd apidog-2.7.57/
./apidog  
```  
<Background>
<img src="https://api.apidog.com/api/v1/projects/544525/resources/368378/image-preview"  />   
</Background>          
  </Step>    
</Steps>

  </Tab>
</Tabs>

