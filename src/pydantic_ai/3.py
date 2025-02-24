from .tools import clone_repo, ls, write_file, cat
from pydantic_ai import Agent, RunContext
import logfire
logfire.configure()

github_agent = Agent(
    model="anthropic:claude-3-5-sonnet-latest",
    tools=[clone_repo]
)

programming_agent = Agent(
    model="anthropic:claude-3-5-sonnet-latest",
    tools=[ls, write_file, cat]
)

async def github_agent_tool(ctx: RunContext, prompt: str):
    """An agent who can clone github repositories."""
    r = await github_agent.run(prompt, usage=ctx.usage)
    return r.data

async def programming_agent_tool(ctx: RunContext, prompt: str):
    """An agent who can interact with the filesystem. It can read, write and list files."""
    r = await programming_agent.run(prompt, usage=ctx.usage)
    return r.data

orchestrator_agent = Agent(
    model="anthropic:claude-3-5-sonnet-latest",
    tools=[github_agent_tool, programming_agent_tool]
)

print(orchestrator_agent.run_sync("""In the anforsm/helloworld github repo, change the backend url to backend.com instead.""").all_messages())
