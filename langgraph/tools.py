from .. import tools as t

from langchain_core.tools import tool


@tool
def clone_repo(ssh_url):

    return t.clone_repo(ssh_url)