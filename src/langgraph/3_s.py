from .tools import clone_repo, ls, cat, write_file
from .run_graph import run_graph, save_to_image

from typing import Annotated, Literal
from typing_extensions import TypedDict

from langchain_anthropic import ChatAnthropic
from langchain_core.messages.ai import AIMessage
from langchain_core.messages import ToolMessage

from langgraph.graph import StateGraph
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode, tools_condition
from langgraph.checkpoint.memory import MemorySaver

from langchain_core.tools import tool


class State(TypedDict):
    messages: Annotated[list, add_messages]

llm = ChatAnthropic(model_name="claude-3-5-sonnet-20241022", timeout=None, stop=None).bind_tools(tools)
def chatbot(state: State):
    return state | {"messages": [llm.invoke(state["messages"])]}

@tool
def programming_agent(prompt: str) -> str:
    """Access to a programming agent who can do programming tasks, including navigating filesystems, reading files and writing files."""

    programming_tools = ToolNode(tools=[ls, cat, write_file])
    programming_agent = StateGraph(State)
    programming_agent.add_node("chatbot", chatbot)
    programming_agent.add_node("tools", programming_tools)

    programming_agent.add_conditional_edges("chatbot", tools_condition)
    programming_agent.add_edge("tools", "chatbot")
    programming_agent.set_entry_point("chatbot")

    run_graph(programming_agent, prompt)
    return "Done"

@tool
def github_agent(prompt: str) -> str:
    """Access to a github agent who can do github tasks, including cloning repositories. (but cant push)"""

    github_tools = ToolNode(tools=[clone_repo])
    github_agent = StateGraph(State)
    github_agent.add_node("chatbot", chatbot)
    github_agent.add_node("tools", github_tools)

    github_agent.add_conditional_edges("chatbot", tools_condition)
    github_agent.add_edge("tools", "chatbot")
    github_agent.set_entry_point("chatbot")

    run_graph(github_agent, prompt)
    return "Done"


orchestrator = StateGraph(State)
orchestrator.add_node("chatbot", chatbot)
agents = ToolNode(tools=[programming_agent, github_agent])
orchestrator.add_node("tools", agents)

orchestrator.add_conditional_edges("chatbot", tools_condition)
orchestrator.add_edge("tools", "chatbot")
orchestrator.set_entry_point("chatbot")


memory = MemorySaver()
graph = orchestrator.compile(checkpointer=memory)

if __name__ == "__main__":
    run_graph(graph,
        """In the anforsm/helloworld github repo, change the backend url to backend.com instead."""
    )
