from .. import tools as t
from smolagents import tool


@tool
def clone_repo(ssh_url: str) -> str:
    """Clone a repository from a given SSH URL. Returns the path to the cloned repository.
    Args:
        ssh_url: The SSH URL of the repository to clone.
    """
    return t.clone_repo(ssh_url)

if __name__ == "__main__":
    print(clone_repo("git@github.com:anforsm/helloworld.git"))
