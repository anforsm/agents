from .tools import clone_repo as tclone_repo

from pydantic_ai import Agent, RunContext


agent = Agent(
    model="anthropic:claude-3-5-sonnet-latest"
)

@agent.tool
def clone_repo(ctx: RunContext, repo_url: str):
    return tclone_repo(repo_url)

print(agent.run_sync("Clone anforsm/helloworld").data)
