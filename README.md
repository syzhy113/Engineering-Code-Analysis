**更换阅读语言: [中文](README_CN.md)**

# Engineering-Code-Analysis
Automated and fast parsing of local project directories and GitHub directories, one-click deployment of local parsing with AutoGPT:

## Introduction

This project is an innovative localized AI assistant system designed to overcome the limitations of traditional online AI services. It supports direct access to local folders and can analyze the content of local project structures. With no file size limitations, it efficiently parses GitHub projects while ensuring that data is stored locally to enhance security.

### Workflow Framework
![工作流框架](image/image.png)

### Demo
![notebook_gif_demo](image/1.gif)

## Main Advantages

- **Increased File Size and Access Speed**:Say goodbye to the 100MB file size limit and internet speed issues. With the local version, everything is under your control.
- **Explicit Network Connection Access**:The official version cannot explicitly access web links and is not friendly to GitHub projects. This project can analyze GitHub projects.
- **Direct Access to Local Files**:Runs in your local directory, making it convenient for personalized file directory operations and real-time file directory analysis.
-  **Data Security**:The code runs locally, eliminating the need to upload files to the internet, which enhances data security.
-  **Model Support**:Access via API, allowing the use of ```GPT-4``` without needing an ```OpenAI Plus``` subscription.

## Precautions
AI-generated code executed on local devices, without human review, may pose security risks. You are responsible for any consequences arising from running such unreviewed programs.

## Usage

### Installation

1. Clone this repository:
   ```shell
   git clone https://github.com/syzhy113/Engineering-Code-Analysis.git
   cd Engineering-Code-Analys
   ```

2. Install dependencies. This program has been tested on Windows 11 and Ubuntu 18.04. Required libraries and versions:
   Create a conda environment:
      ```shell
   conda create -n env_name python=3.10
   conda activate env_name
   ```
   可以直接使用以下命令安装
   ```shell
   pip install -r requirements.txt
   ```

### API Configuration
1. Replace the corresponding variables in ```src/config.json``` with your own ```OpenAI API``` to enable model calls.<br>
2. Additionally, if you need to access GitHub projects, you'll need to obtain the corresponding ```Github API KEY```。
   ```shell
   {
     "GIT_KEY": "",
     "OPENAI_API_KEY": "",
     "OPENAI_BASE_URL": ""
   }
   ```

## Run

1. Navigate to the src directory:
   ```shell
   cd src
   ```

2. Run the following command:
   ```shell
   python main.py
   ```

3. To complete the conversation in the command line, use:
   ```shell
   🤖：有什么可以帮您？
   👨：
   ```


## Example

Here is an example of using this program for engineering task analysis:

1. ：
   ```shell
   🤖：有什么可以帮您？
   👨：Agent文件夹中的核心代码是什么，内容是什么，是干什么的，具体分析一下
   🤖：Agent文件夹中的核心代码包括两个文件：`Action.py`和`ReAct.py`。`Action.py`定义了一个`Action`类，用于描述一个动作。`ReAct.py`实
      现了一个基于Langchain的智能体框架，包括多个方法来格式化思维过程、提取动作、初始化智能体、查找工具、执行思考过程和运行智能体。
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
2. ：
   ```shell
   🤖：有什么可以帮您？
   👨：https://github.com/raghakot/keras-resnet解析一下这个工程
   🤖：## 工程基本信息
该工程是使用Keras实现的残差网络（ResNet），支持Theano和TensorFlow后端。主要目的是提供一种基于Keras的方便的ResNet实现。

安装和使用方法
1. 克隆本仓库：
   ```shell
   git clone https://github.com/raghakot/keras-resnet.git
   cd keras-resnet
   ```

2. 使用pip安装依赖：
   ```shell
   pip install -r requirements.txt
   ```

3. 使用方法：
   - 训练ResNet-18模型在CIFAR-10数据集上：
     ```shell
     THEANO_FLAGS=mode=FAST_RUN,device=gpu,floatX=float32 python cifar10.py
     ```

核心代码结构

cifar10.py
- 作用：训练ResNet-18模型在CIFAR-10数据集上。
  - 加载和预处理CIFAR-10数据。
  - 构建ResNet-18模型。
  - 使用数据增广（可选）。
  - 训练模型并保存训练日志。

resnet.py
- 作用：定义ResNet模型的构建逻辑。
  - _bn_relu：构建Batch Normalization和ReLU激活块。
  - _conv_bn_relu：构建卷积、Batch Normalization和ReLU激活块。
  - _bn_relu_conv：构建Batch Normalization、ReLU激活和卷积块。
  - _shortcut：构建残差块的shortcut连接。
  - _residual_block：构建残差块。
  - basic_block：定义基本残差块。
  - bottleneck：定义瓶颈残差块。
  - _handle_dim_ordering：处理不同的图像维度顺序。
  - ResnetBuilder：提供构建不同深度ResNet模型的方法，如ResNet-18、ResNet-34、ResNet-50等。

tests/test_resnet.py
- 作用：测试ResNet模型的构建和编译。
  - 定义了多个测试函数，测试不同深度的ResNet模型（如ResNet-18、ResNet-34、ResNet-50等）的构建和编译。
  - 使用pytest框架进行测试。

核心代码结构图
plaintext
── cifar10.py (训练ResNet-18模型在CIFAR-10数据集上)
    -- 加载和预处理数据
    -- 构建和训练模型

── resnet.py (定义ResNet模型的构建逻辑)
    -- class ResnetBuilder (提供构建ResNet模型的方法)
        -- function build (构建ResNet模型的核心方法)
        -- function build_resnet_18 (构建ResNet-18模型)
        -- function build_resnet_34 (构建ResNet-34模型)
        -- function build_resnet_50 (构建ResNet-50模型)
        -- function build_resnet_101 (构建ResNet-101模型)
        -- function build_resnet_152 (构建ResNet-152模型)

── tests/test_resnet.py (测试ResNet模型的构建和编译)
    -- function test_resnet18 (测试ResNet-18模型)
    -- function test_resnet34 (测试ResNet-34模型)
    -- function test_resnet50 (测试ResNet-50模型)
    -- function test_resnet101 (测试ResNet-101模型)
    -- function test_resnet152 (测试ResNet-152模型)
    -- function test_custom1 (自定义测试1)
    -- function test_custom2 (自定义测试2)

      ```


