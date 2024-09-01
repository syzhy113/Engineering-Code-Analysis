import ast
import os


def analyze_python_dict(file_paths):
    contents = ''
    for file_path in file_paths:
        contents += f'#######{file_path}#######' + '\n' + analyze_python_file(file_path)

    return contents


def analyze_python_file(file_path):
    if file_path.endswith('py'):
        with open(file_path, "r", encoding="utf-8") as file:
            code = file.read()
        contents = ""
        try:
            parsed_code = ast.parse(code)
            classes = [node for node in ast.walk(parsed_code) if isinstance(node, ast.ClassDef)]
            functions = [node for node in ast.walk(parsed_code) if isinstance(node, ast.FunctionDef)]

            print(f"\n解析文件: {file_path}")

            for cls in classes:
                contents += f"类名：{cls.name}" + '\n'
                for item in cls.body:
                    try:
                        functions.remove(item)
                    except:
                        pass
                    if isinstance(item, ast.FunctionDef):
                        contents += f"  方法名：{item.name}" + '\n'
                        contents += "  参数列表 " + str([arg.arg for arg in item.args.args]) + '\n'

            for func in functions:
                if func not in classes:
                    contents += "函数名：", func.name + '\n'
                    contents += "参数列表：" + str([arg.arg for arg in func.args.args])
                    # print("函数体：")
                    # for stmt in func.body:
                    #     print(f"  {ast.dump(stmt)}")

        except Exception as e:
            contents += f"解析文件 {file_path} 时出错: {e}"
        return contents

    elif file_path.endswith('m'):
        with open(file_path, "r", encoding="gbk") as file:
            code = file.read()

        print(f"\n解析文件: {file_path}")


if __name__ == "__main__":
    contents = analyze_python_file('../Agent/ReAct.py')
    contents = analyze_python_dict(['../Agent/ReAct.py', '../Agent/Action.py'])
    pass
