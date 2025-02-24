from .tools import clone_repo, ls, cat, write_file
from .run_graph import run_graph, save_to_image

from dotenv import load_dotenv
import os
load_dotenv("/Users/anton/Documents/GitHub/agents/src/langgraph/.env")
from typing import Annotated
from typing_extensions import TypedDict

from langchain_anthropic import ChatAnthropic
from langchain_core.messages.ai import AIMessage
from langchain_core.messages import ToolMessage

from langgraph.graph import StateGraph
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode, tools_condition
from langgraph.checkpoint.memory import MemorySaver


tools = [clone_repo, ls, cat, write_file]

llm = ChatAnthropic(model_name="claude-3-5-sonnet-20241022", timeout=None, stop=None).bind_tools(tools)

class State(TypedDict):
    messages: Annotated[list, add_messages]

def chatbot(state: State):
    return state | {"messages": [llm.invoke(state["messages"])]}


tool_node = ToolNode(tools=tools)
graph_builder = StateGraph(State)
graph_builder.add_node("chatbot", chatbot)
graph_builder.add_node("tools", tool_node)

graph_builder.add_conditional_edges("chatbot", tools_condition)
graph_builder.add_edge("tools", "chatbot")
graph_builder.set_entry_point("chatbot")

memory = MemorySaver()
graph = graph_builder.compile(checkpointer=memory)

print(__name__)

if __name__ == "__main__":
    run_graph(graph,
        """In the anforsm/helloworld github repo, change the backend url to backend.com instead."""
    )

    save_to_image(graph)
