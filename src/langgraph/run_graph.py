from langgraph.utils.config import RunnableConfig
from langchain_core.runnables.graph import CurveStyle, MermaidDrawMethod, NodeStyles

def run_graph(graph, initial_input, print_output=True):
    config: RunnableConfig = {"configurable": {"thread_id": "1"}}
    events = graph.stream(
        {
            "messages": [
                {
                    "role": "system",
                    "content": """You are a helpful assistant :)"""
                },
                {
                    "role": "user",
                    "content": initial_input
                }
            ]
        },
        config=config,
        stream_mode="values",
    )
    for event in events:
        for value in event.values():
            message = value[-1]
            if print_output:
                message.pretty_print()

def save_to_image(graph):
    png = graph.get_graph().draw_mermaid_png(
            draw_method=MermaidDrawMethod.API,
    )
    # Save the graph png
    with open("graph.png", "wb") as f:
        f.write(png)
