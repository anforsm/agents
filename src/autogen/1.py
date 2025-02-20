import os
import asyncio
from autogen_agentchat.conditions import TextMentionTermination
from langgraph.pregel.algo import Call
from typing_extensions import Annotated

from autogen_core import CancellationToken

from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.messages import TextMessage
from autogen_agentchat.agents import AssistantAgent, UserProxyAgent
from autogen_agentchat.ui import Console

from autogen_ext.models.openai import OpenAIChatCompletionClient

from .tools import clone_repo

client = OpenAIChatCompletionClient(
    model="gpt-4o"
)

agent = AssistantAgent(
    name="github_agent",
    model_client=client,
    tools=[clone_repo],
    system_message="You are a helpful assistant. Use tools to solve tasks.",
)

async def simple_test() -> None:
    prompt = "clone the repo anforsm/helloworld"
    response = await agent.on_messages([TextMessage(content=prompt, source="user")], CancellationToken())
    print(response)

user_proxy = UserProxyAgent("user_proxy")
agent_team = RoundRobinGroupChat(
    participants=[user_proxy, agent],
    termination_condition=TextMentionTermination("TERMINATE")
)

if __name__ == "__main__":
    config = agent_team.dump_component()
    with open("config.json", "w") as f:
        f.write(config.model_dump_json())

    #asyncio.run(simple_test())
    #asyncio.run(agent_team.run())
