from .. import tools as t


def clone_repo(ssh_url: str) -> str:
    """Clone a repository from a given SSH URL. Returns the path to the cloned repository."""
    return t.clone_repo(ssh_url)

def ls(path: str) -> str:
    """List the contents of the current directory."""
    return t.ls(path)

def cat(filename: str) -> str:
    """Read the contents of a file."""
    return t.cat(filename)

def write_file(filename: str, content: str) -> None:
    """Write content to a file."""
    t.write_file(filename, content)

if __name__ == "__main__":
    print(clone_repo("git@github.com:anforsm/helloworld.git"))
