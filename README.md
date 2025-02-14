# deepseek_r1_Alibaba

# deepseek r1 16 B 版本 🙋 

## _使用本教程可能会消费你的阿里云费用，请悉知！_ 相比其他同水平大模型，其价格仍可以算便宜。

(我无法确定其可靠参数范围，但根据模型自己回答为16B）

![image](https://github.com/user-attachments/assets/021ade79-1d09-4001-b3a7-50d8dd94180c)

通过huggingface查询，确实有16.5B的开源模型，因此很可能是阿里云自己部署了这个水平的模型，又发售了api给大众使用， 其中新用户注册可以拿到第一个免费百万token
![image](https://github.com/user-attachments/assets/b83d6159-5cd7-45c6-8bb6-0bf6c2a137ff)

```
### 实际场景示例**
- **单次对话输入**：
如果每次输入约 **1000 字**（约 500~700 token），则 100 万 token 可支持 **约 1400~2000 次对话**（仅计算输入，不包含输出）。
- **包含输出**：
如果每次对话输入 + 输出共消耗 **2000 token**，则 100 万 token 可支持约 **500 次完整对话**。
```



- 由于官方 DeepSeek 网站因大量访问者而无法访问，现提供阿里云版 DeepSeek R1 作为临时解决方案
- 阿里云提供了在代码行中使用或者网页端使用的方式，但缺少在一般计算机本地使用远程api的图形方法，因此本仓库使用第三方开源软件flask展示了如何在本地使用api
- 本地使用远程api与在网页端使用没有本质区别，但具有更高的api防止泄漏的风险，以及在响应速度方面的不同。你也可以自己修改聊天的图形界面大小和风格等。
     

## 阿里云版本部署的deepssek r1

官网访问紧张？别担心！阿里云版DeepSeek现已同步上线

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
## 提醒：

⚡ 回复速度可能一般，这是因为阿里云设置了api调用的速率


⚡ 为了保持使用的稳定性，实时显示思考过程被取消，而是在输出结果后一并显示，不完美但简单稳定，容易运行成功。

![image](https://github.com/user-attachments/assets/01bb06c5-b446-4a8a-b9a1-b235c296e3e3)

⚡ 本着能运行起来就不要在去动代码的精神，我放弃了继续加入其他feature，如点击回车自动发送，和左侧显示历史聊天记录等（可以加入，但app.py文件将因这些不太重要的功能变得特别长），因此你需要手动点击发送按钮开始聊天
![image](https://github.com/user-attachments/assets/fb4c8c06-cf18-47d1-8097-12216c8c08a8)


## 改进, 如果你想在此基础上继续改进，你可以从以下方面着手

- 图形界面的大小，风格还可以有较大提升

- 暂时还不可以实时显示思考过程，现在只是在结果输出后一并给出了曾经的思考过程。
  ![image](https://github.com/user-attachments/assets/35cc87d9-3f12-4bf2-8647-9e22d1f4fbc4)

