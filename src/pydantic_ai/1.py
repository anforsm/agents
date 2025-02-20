from .tools import clone_repo
from pydantic_ai import Agent

agent = Agent(
    model="anthropic:claude-3-5-sonnet-latest",
    tools=[clone_repo]
)

print(agent.run_sync("Clone anforsm/helloworld").all_messages())
