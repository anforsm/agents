import os
import asyncio
from autogen_agentchat.conditions import TextMentionTermination
from langgraph.pregel.algo import Call
from typing_extensions import Annotated

from autogen_core import CancellationToken

from autogen_agentchat.teams import MagenticOneGroupChat, RoundRobinGroupChat
from autogen_agentchat.messages import TextMessage
from autogen_agentchat.agents import AssistantAgent, UserProxyAgent
from autogen_agentchat.ui import Console

from autogen_ext.models.openai import OpenAIChatCompletionClient

from .tools import clone_repo, ls, cat, write_file

client = OpenAIChatCompletionClient(
    model="gpt-4o"
    #model="azure.gpt-4o",
    #api_key=os.environ["NL_OPENAI_API_KEY"],
    #base_url="https://chat.netlight.com/api",
    #model_info={
    #    "function_calling": True,
    #    "vision": False,
    #    "json_output": True,
    #    "family": "gpt-4o"
    #}
)

github_agent = AssistantAgent(
    name="github_agent",
    model_client=client,
    tools=[clone_repo],
    system_message="You are a helpful assistant. Use tools to solve tasks. When you are done, say TERMINATE.",
    description="A GitHub agent that can clone repositories."
)

programming_agent = AssistantAgent(
    name="programming_agent",
    model_client=client,
    tools=[ls, cat, write_file],
    system_message="You are a helpful assistant. Use tools to solve tasks. When you are done, say TERMINATE.",
    description="A programming agent that can perform file operations such as listing files, reading files, and writing files."
)

agent_team = MagenticOneGroupChat(
    participants=[github_agent, programming_agent],
    model_client=client,
    #termination_condition=TextMentionTermination("TERMINATE"),
    #max_turns=4
)

async def main():
        user_input = "In the anforsm/helloworld github repo, change the backend url to backend.com instead."
        stream = agent_team.run_stream(task=user_input)
        await Console(stream)

if __name__ == "__main__":
    asyncio.run(main())
