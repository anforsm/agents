from .tools import clone_repo

from smolagents import HfApiModel, ToolCallingAgent

tools = [clone_repo]

model = HfApiModel(
    max_tokens=2096,
    temperature=0.5,
    model_id='Qwen/Qwen2.5-Coder-32B-Instruct',
    custom_role_conversions=None,
)

agent = ToolCallingAgent(
    model=model,
    tools=[clone_repo],
    max_steps=6,
    verbosity_level=1,
    grammar=None,
    planning_interval=None,
    name=None,
    description=None,
)

if __name__ == "__main__":
    agent.run("Clone anforsm/helloworld")
