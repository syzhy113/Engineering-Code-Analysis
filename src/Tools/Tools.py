import warnings
warnings.filterwarnings("ignore")

from langchain.tools import StructuredTool
from .FileQATool import ask_docment
from .WriterTool import write
from .EmailTool import send_email
from .ExcelTool import get_first_n_rows
from .FileTool import list_files_in_directory, return_dict
from .FinishTool import finish
from .PythonTool import read_python
from .Python_structure_Tool import analyze_python_dict
from .githubTool import github_core

document_qa_tool = StructuredTool.from_function(
    func=ask_docment,
    name="AskDocument",
    description="根据一个Word或PDF文档的内容，回答一个问题。考虑上下文信息，确保问题对相关概念的定义表述完整。",
)

document_generation_tool = StructuredTool.from_function(
    func=write,
    name="GenerateDocument",
    description="根据需求描述生成一篇正式文档",
)

email_tool = StructuredTool.from_function(
    func=send_email,
    name="SendEmail",
    description="给指定的邮箱发送邮件。确保邮箱地址是xxx@xxx.xxx的格式。多个邮箱地址以';'分割。",
)

excel_inspection_tool = StructuredTool.from_function(
    func=get_first_n_rows,
    name="InspectExcel",
    description="探查表格文件的内容和结构，展示它的列名和前n行，n默认为3",
)

directory_inspection_tool = StructuredTool.from_function(
    func=list_files_in_directory,
    name="ListDirectory",
    description="探查文件夹的内容和结构，展示它的文件名和文件夹名",
)

finish_placeholder = StructuredTool.from_function(
    func=finish,
    name="FINISH",
    description="结束任务，将最终答案返回,最终答案需要明确答案是什么，比如 tool.py中的代码核心代码为xxx，起到了链接API的作用"
)

python_tool = StructuredTool.from_function(
    func=read_python,
    name="ReadPython",
    description="如果是github的工程，不要调用此工具 #### 读取python代码，以字符串形式返回代码, 可以一次访问不止一个文件,在访问的时候需要提供完整代码路径,"
                "如果你觉得提供给你的代码框架已经足够回答问题，可以不调用此工具"

)

return_dict_tool = StructuredTool.from_function(
    func=return_dict,
    name="return_file",
    description="探查文件夹的内容和结构，展示它的文件名和文件夹名"
)

get_python_structure = StructuredTool.from_function(
    func=analyze_python_dict,
    name="get_python_structure",
    description="获得python代码的机构，可以一次访问不止一个文件，在访问是需要提供完整的代码路径"
)


