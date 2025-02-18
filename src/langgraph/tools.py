#from .. import tools as t
from .. import tools as t
from langchain_core.tools import tool


@tool
def clone_repo(ssh_url: str) -> str:
    """Clone a repository from a given SSH URL. Returns the path to the cloned repository."""
    return t.clone_repo(ssh_url)

if __name__ == "__main__":
    print(clone_repo("git@github.com:anforsm/helloworld.git"))
