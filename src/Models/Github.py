from Tools.githubTool import github_core
from github import Github
from Tools.Python_structure_Tool import analyze_python_dict
import re
import os


g = Github(os.environ["GIT_KEY"])
core = github_core()


def parse_github_url(url):
    match = re.match(r"https://github.com/([^/]+)/([^/]+)", url)
    if match:
        owner, repo_name = match.groups()
        return f"{owner}/{repo_name}"
    else:
        return "无效的 GitHub URL，不存在该URL"


def directory_contents2str_github(contents, repo, branch_name, level=0):
    content_str = ""
    for content_file in contents:
        content_str += "  " * level + '--' + content_file.path + '\n'
        if content_file.type == "dir":
            content_str += directory_contents2str_github(repo.get_contents(content_file.path, ref=branch_name), repo,
                                                         branch_name, level + 1)
    return content_str


def directory_contents2str(directory, level=0):
    content_str = str(directory) + "文件夹下的路径为" + '\n'
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        content_str += "  " * level + '--' + item + '\n'
        if item_path.endswith('.py'):
            content_str += "  " * (level + 1) + analyze_python_dict([item_path]) + '\n'
        if os.path.isdir(item_path):
            content_str += directory_contents2str(item_path, level + 1)
    return content_str
