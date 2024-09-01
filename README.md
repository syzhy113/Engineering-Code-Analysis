**更换阅读语言: [中文](README_CN.md)**

# Engineering-Code-Analysis
Here's the translated version of your content while preserving the original formatting:

## Introduction

This project is an innovative localized AI assistant system designed to overcome the limitations of traditional online AI services. It supports direct access to local folders and can analyze the content of local project structures. With no file size limitations, it efficiently parses GitHub projects while ensuring that data is stored locally to enhance security.

### Workflow Framework
![工作流框架](image/image.png)

### Demo
![notebook_gif_demo](image/1.gif)

## Main Advantages

- **Increased File Size and Access Speed**：Say goodbye to the 100MB file size limit and internet speed issues. With the local version, everything is under your control.
- **Explicit Network Connection Access**：The official version cannot explicitly access web links and is not friendly to GitHub projects. This project can analyze GitHub projects.
- **Direct Access to Local Files**：Runs in your local directory, making it convenient for personalized file directory operations and real-time file directory analysis.
-  **Data Security**：The code runs locally, eliminating the need to upload files to the internet, which enhances data security.
-  **Model Support**：Access via API, allowing the use of ```GPT-4``` without needing an ```OpenAI Plus``` subscription.

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
   🤖：该工程实现了基于Keras的残差网络，支持theano和tensorflow后端。核心代码结构如下：
      ——resnet.py 文件作用是实现ResNet模型
         --class ResnetBuilder 类的作用是构建各种版本的ResNet模型
              -- function build 函数的作用是构建自定义的ResNet架构
              -- function build_resnet_18 函数的作用是构建ResNet18模型
              -- function build_resnet_34 函数的作用是构建ResNet34模型
              -- function build_resnet_50 函数的作用是构建ResNet50模型
              -- function build_resnet_101 函数的作用是构建ResNet101模型
              -- function build_resnet_152 函数的作用是构建ResNet152模型
         -- function _bn_relu 函数的作用是构建一个BN -> ReLU块
         -- function _conv_bn_relu 函数的作用是构建一个Conv -> BN -> ReLU块
         -- function _bn_relu_conv 函数的作用是构建一个BN -> ReLU -> Conv块
         -- function _shortcut 函数的作用是在输入和残差块之间添加捷径并将它们合并
         -- function _residual_block 函数的作用是构建一个带有重复瓶颈块的残差块
         -- function basic_block 函数的作用是用于构建层数≤34的ResNet的基本3×3卷积块
         -- function bottleneck 函数的作用是用于构建层数>34的ResNet的瓶颈架构
         -- function _handle_dim_ordering 函数的作用是处理图像维度顺序
         -- function _get_block 函数的作用是获取块函数（basic_block或bottleneck）
      
      ——cifar10.py 文件作用是实现Cifar10数据集的训练示例
         -- 函数和全局变量的作用是定义训练参数、数据预处理和模型训练
      
      ——tests/test_resnet.py 文件作用是实现ResNet模型的单元测试
         -- function _test_model_compile 函数的作用是测试模型的编译
         -- function test_resnet18 函数的作用是测试ResNet18模型
         -- function test_resnet34 函数的作用是测试ResNet34模型
         -- function test_resnet50 函数的作用是测试ResNet50模型
         -- function test_resnet101 函数的作用是测试ResNet101模型
         -- function test_resnet152 函数的作用是测试ResNet152模型
         -- function test_custom1 函数的作用是测试自定义的ResNet模型
         -- function test_custom2 函数的作用是测试自定义的ResNet模型

      ```


