from langchain.tools import StructuredTool


class github_core:
    def __init__(self, repo=None, branch_name=None):
        self.repo = repo
        self.branch_name = branch_name

    def set_repo_branch(self, repo, branch_name):
        self.repo = repo
        self.branch_name = branch_name

    def get_github_codes(self, file):
        if type(file) == str:
            return self.repo.get_contents(file, ref=self.branch_name).decoded_content.decode("utf-8")
        else:
            contents = ""
            for f in file:
                contents += f'#######{f}#######' + '\n' + \
                            self.repo.get_contents(f, ref=self.branch_name).decoded_content.decode("utf-8")
            return contents

    def as_tool(self):
        return StructuredTool.from_function(
            func=self.get_github_codes,
            name="get_github_code",
            description='如果在进行github任务，读取代码只能使用此工具，读取github上的代码和README，以字符串形式返回代码, 可以一次访问不止一个文件,'
                        '如果要访问不止一个文件，请用列表的形式返回，在访问的时候需要提供完整代码路径',
        )
