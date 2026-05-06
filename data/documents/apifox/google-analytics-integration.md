# 文档站接入 Google Analytics


> Apifox 版本需 ≥ 2.6.41

文档站支持上报网页信息到 Google Analytics，你可以在 Google Analytics 查看文档站的相关数据 *（比如浏览量、用户分析等等 Google Analytics 自带的能力）*

## Google Analytics 配置流程

1. 首先需要一个 Google Analytics 账号，可以在这个页面去注册：
   
   [https://marketingplatform.google.com/about/analytics/](https://marketingplatform.google.com/about/analytics/)


2. 注册账号之后，可在设置里创建一个 “媒体资源”。

    
    <Background>

    ![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/486110/image-preview)
    </Background>


    在创建媒体资源时需设置你的网站数据流，其中 “网站地址” 可以填入文档站顶部的地址，填入后点击 “创建并继续” 即可。

    
    <Background>

    ![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/486111/image-preview)
    
    
    ![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/486112/image-preview)
    </Background>



3. 数据流创建成功后，一般会要求填一段代码到网站中，不过在 Apifox 文档站中，我们不需要手动添加代码，只需要在 Apifox 文档站的设置页中填写 Measurement ID（衡量 ID） 即可。
   
   回到 Google Analytics 首页，点击左侧导航栏的 “设置 -> 数据流”，找到对应站点的 Measurement ID（衡量 ID），然后回填在 Apifox 文档站的设置页中。

    
    <Background>

    ![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/486113/image-preview)


    ![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/486114/image-preview)
    </Background>



4. 在 Apifox 文档站的设置页，点击 “Google Analytics”，然后填写 Measurement ID（衡量 ID）。

    
    <Background>

    ![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/486115/image-preview)
    
    </Background>


    <Background>

           <img width="460px" src="https://api.apifox.com/api/v1/projects/5097254/resources/486116/image-preview"/>
    </Background>




5. **要验证是否生效？**
   
   在配置完了以后，可以打开对应的文档站，做一些浏览和点击行为。回到 Google Analytics，点击 “报告 -> 页面实时浏览情况”，就可以看是否有实时的数据了。


    <Background>

    ![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/486117/image-preview)
    </Background>

