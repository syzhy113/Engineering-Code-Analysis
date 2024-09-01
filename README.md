# Engineering-Code-Analysis
使用Openai有关项目工程的代码解释器

## 简介

本项目是一款创新的本地化AI助手系统，
旨在突破传统在线AI服务的局限。它支持直接访问本地文件夹，对本地项目结构内容进行解析。
无文件大小限制，能高效解析GitHub项目，同时保证数据仅存储在本地以提高安全性。

### 工作流框架
![工作流框架](image/image.png)

### Demo
![notebook_gif_demo](image/1.gif)

## 优势

- **文件大小及访问速度提升**：告别100MB文件大小限制和网速问题。使用本地版，一切尽在掌控之中。
- **显式访问网络连接**：官方无法显式访问网页链接，对github项目不友好，该工程可以对github项目进行解析。
- **直接访问本地文件**：在您本地目录中运行，方便进行个性化文件目录操作，实时解析文件目录。
-  **数据安全**：代码在本地运行，无需将文件上至网络，提高了数据的安全性。
-  **模型支持**：使用API进行访问，无需OpenAI plus也可以使用GPT4。

## 注意事项
本地设备上执行AI生成但未经人工审核的代码可能存在安全风险。若未经审核运行程序所产生的所有后果，您需自行承担。

## 使用方法

### 安装

1. 克隆本仓库
   ```shell
   git clone https://github.com/syzhy113/Engineering-Code-Analysis.git
   cd Engineering-Code-Analys
   ```

2. 安装依赖。该程序已在Windows 11和ubuntu18.04测试。所需的库及版本：
   创建conda环境
      ```shell
   conda create -n env_name python=3.10
   conda activate env_name
   ```
   可以直接使用以下命令安装
   ```shell
   pip install -r requirements.txt
   ```

### API配置
1. 使用自己的OpenAI API替换 
```src/config.json ```
下的对应变量，以实现对模型的调用。<br>
2. 同时，如果需要使用对Github工程的访问功能，需要申请对应的Github API KEY。
   ```shell
   {
     "GIT_KEY": "",
     "OPENAI_API_KEY": "",
     "OPENAI_BASE_URL": ""
   }
   ```

## 使用

1. 进入`src`目录。
   ```shell
   cd src
   ```

2. 运行以下命令：
   ```shell
   python main.py
   ```

3. 在命令行中，完成对话使用
   ```shell
   🤖：有什么可以帮您？
   👨：
   ```


## 示例

以下是一个使用本程序进行工程任务分析的示例：

1. ：
      ```shell
   🤖：有什么可以帮您？
   👨：Agent文件夹中的核心代码是什么，内容是什么，是干什么的，具体分析一下
   🤖：
      ```Agent文件夹中的核心代码包括两个文件：`Action.py`和`ReAct.py`。`Action.py`定义了一个`Action`类，用于描述一个动作。`ReAct.py`实现了一个基于Langchain的智能体框架，包括多个方法来格式化思维过程、提取动作、初始化智能体、查找工具、执行思考过程和运行智能体。
   —Agent
      ——Action.py 文件作用是定义动作类
         --class Action 类的作用是描述一个动作
              -- function __str__ 函数的作用是生成动作的字符串表示
      ——ReAct.py 文件作用是实现基于Langchain的智能体
         --class ReActAgent 类的作用是实现智能体框架
              -- function __format_thought_observation 函数的作用是格式化思维过程和观察结果
              -- function __extract_json_action 函数的作用是从文本中提取JSON格式的动作
              -- function __init__ 函数的作用是初始化智能体
              -- function __init_prompt_templates 函数的作用是初始化提示模板
              -- function __init_chains 函数的作用是初始化主流程链
              -- function __find_tool 函数的作用是根据工具名称查找工具
              -- function __step 函数的作用是执行一步思考过程
              -- function __exec_action 函数的作用是执行动作并返回观察结果
              -- function extract_between_markers 函数的作用是从字符串中提取标记之间的子字符串
              -- function run 函数的作用是运行智能体
      ```
   ```


