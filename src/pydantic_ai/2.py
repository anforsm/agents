from .tools import clone_repo, ls
from pydantic_ai import Agent, RunContext


agent = Agent(
    model="anthropic:claude-3-5-sonnet-latest",
    tools=[clone_repo, ls]
)

print(agent.run_sync("How many files are in the root of the anforsm/helloworld github repository?").all_messages())
