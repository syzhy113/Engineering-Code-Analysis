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
- **显式访问网络连接**：官方无法显式访问网页链接，对GitHub项目不友好，该工程可以对Github项目进行解析。
- **直接访问本地文件**：在您本地目录中运行，方便进行个性化文件目录操作，实时解析文件目录。
-  **数据安全**：代码在本地运行，无需将文件上至网络，提高了数据的安全性。
-  **模型支持**：使用API进行访问，无需```OpenAI plus```也可以使用```GPT4```。

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
1. 使用自己的```OpenAI API```替换 
```src/config.json ```
下的对应变量，以实现对模型的调用。<br>
2. 同时，如果需要使用对Github工程的访问功能，需要申请对应的```Github API KEY```。
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


