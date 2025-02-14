# deepseek_r1_Alibaba

# deepseek r1 满血版本 🙋

## _使用本教程可能会消费你的阿里云费用，请悉知！_ 相比其他同水平大模型，其价格仍可以算便宜。

- 由于官方 DeepSeek 网站因大量访问者而无法访问，现提供阿里云版 DeepSeek R1 作为临时解决方案
- 
- 阿里云提供了在代码行中使用或者网页端使用的方式，但缺少在一般计算机本地使用远程api的图形方法，因此本仓库使用第三方开源软件flask展示了如何在本地使用api

- 本地使用远程api与在网页端使用没有本质区别，但具有更高的api防止泄漏的风险，以及在响应速度方面的不同。你也可以自己修改聊天的图形界面大小和风格等。
     

## 阿里云版本部署的deepssek r1

官网访问紧张？别担心！阿里云版DeepSeek现已同步上线，**模型能力与官网完全一致**，轻松实现零门槛切换！即日起注册即享**免费API额度**，助您无忧体验顶尖AI技术。用量用尽后，可使用相同api继续付费以低价使用，性能不打折！立即前往阿里云平台，解锁稳定、高效、高性价比的智能服务，让创新永不停摆！

![image](https://github.com/user-attachments/assets/f9065245-8346-4b60-acca-fc43d0782403)


## Pre-requests

 1. [Opeai SDK](https://github.com/openai/openai-python) 或者 DashScope的Python SDK，此处我们选择openai sdk
 2. [阿里云百炼api key](https://help.aliyun.com/zh/model-studio/getting-started/first-api-call-to-qwen?spm=0.0.0.i2#688de734136xo)
 3. [Flask](https://github.com/pallets/flask) （本地图形化需要）
 4. python 最好为3.12或者以上，这个对linxu一般已经有了，windows如果没有请自行安装
--------------------------------------------------------------------------------------------------------------------------
⚡ *api key是敏感信息，使用不当可能会泄漏带来额外费用。请不要直接粘贴到代码中使用，而是保存在本地计算机，再通过环境变量引用到代码中即可*
--------------------------------------------------------------------------------------------------------------------------
## 设置步骤

1. 请在你的本地计算机按照[阿里云的文档](https://help.aliyun.com/zh/model-studio/developer-reference/configure-api-key-through-environment-variables#65bb6a945by1x) 安装openai SDK （`pip install openai`）
2. 获取阿里云的token (第一个一百万免费，后续4元人民币/百万)，
  ![image](https://github.com/user-attachments/assets/515233cd-98ca-4bac-b962-43ddf39c11cf)

   你只需要保持阿里云的充值费用有一定余额即可在免费额度用完后继续使用，可在阿里云后台监控使用情况。
   
   ![image](https://github.com/user-attachments/assets/5311a6ff-3e06-4fb4-94dd-284149229ba2)
   

4. 安装Flask，  `pip install flask`, 通过运行app.py 和index.html 用作提供图形界面在本机使用
5. 下载本仓库代码，并解压，然后进入主文件夹
6. **设置api环境变量，`export DASHSCOPE_API_KEY="YOUR_DASHSCOPE_API_KEY"`，具体方法仍参考阿里云链接。**
   注意你的计算机类型，如果是windows你需要找到环境变量面板, Mac 和Linux可在命令行设置
   ![image](https://github.com/user-attachments/assets/e87d40bd-5307-40d4-b1bc-dabfb7484703)

  🙋 注意：按照阿里云文档，我们可以有两种方式调用这个api，即本教程中的openai sdk，或者 DashScope的Python SDK， 但无论哪种，我们需要设置的环境变量都只有一个也就是`DASHSCOPE_API_KEY` 

6. 运行 `python app.py` 这个命令将在你的计算机后台开始一个Flask进程按照app.py来调用你的阿里云api key，同时将index.html定义的聊天窗口呈现到你本机的5000端口。（你可以随意修改端口到其他空闲端口）
7. 到你的浏览器通过`localhost:5000`即可使用deepseek r1 满血版本 🙋
--------------------------------------------------------------------------------------------------------------------------
提醒：

⚡ 回复速度可能一般被，这是因为阿里云设置了api调用的速率

⚡ 为了保持使用的稳定性，实时显示思考过程被取消，而是在输出结果后一并显示，不完美但简单稳定，容易运行成功。

## 改进 

- 图形界面的大小，风格还可以有较大提升

- 暂时还不可以实时显示思考过程，现在只是在结果输出后一并给出了曾经的思考过程。
  ![image](https://github.com/user-attachments/assets/35cc87d9-3f12-4bf2-8647-9e22d1f4fbc4)

