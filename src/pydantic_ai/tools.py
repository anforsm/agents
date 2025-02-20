from pydantic_ai import Agent, RunContext
from .. import tools as t


def clone_repo(ctx: RunContext, ssh_url: str) -> str:
    """Clone a repository from a given SSH URL."""
    return t.clone_repo(ssh_url)

def ls(ctx: RunContext, path: str) -> str:
    """List the contents of a directory, using the ls command."""
    return t.ls(path)
