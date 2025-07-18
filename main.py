# Enable nested event loops (useful in Jupyter or environments where an event loop is already running)
import nest_asyncio
nest_asyncio.apply()

# Load the Ollama LLM wrapper from LlamaIndex
from llama_index.llms.ollama import Ollama
from llama_index.core import Settings

# Set the default LLM to use LLaMA 3.2 via Ollama with a 120-second timeout
llm = Ollama(model="llama3.2", request_timeout=120.0)
Settings.llm = llm

# Import MCP client and tool specification class
from llama_index.tools.mcp import BasicMCPClient, McpToolSpec

# Define the system prompt for the agent
SYSTEM_PROMPT = """\
You are an AI assistant for Tool Calling.

Before you help a user, you need to work with tools to interact with Our Database
"""

# Import the function-based agent class
from llama_index.core.agent.workflow import FunctionAgent

# ----------------------------
# Create and configure the agent
# ----------------------------
async def get_agent(tools: McpToolSpec) -> FunctionAgent:
    tools = await tools.to_tool_list_async()
    agent = FunctionAgent(
        name="Agent",
        description="An agent that can work with Our Database software.",
        tools=tools,
        llm=Ollama(model="llama3.2", request_timeout=120.0),
        system_prompt=SYSTEM_PROMPT,
    )
    return agent

# Import additional workflow types
from llama_index.core.agent.workflow import (
    FunctionAgent, 
    ToolCallResult, 
    ToolCall
)
from llama_index.core.workflow import Context

# ----------------------------
# Handle user input with agent
# ----------------------------
async def handle_user_message(
    message_content: str,
    agent: FunctionAgent,
    agent_context: Context,
    verbose: bool = False,
) -> str:
    handler = agent.run(message_content, ctx=agent_context)
    
    async for event in handler.stream_events():
        if verbose and isinstance(event, ToolCall):
            print(f"🔧 Calling tool '{event.tool_name}' with kwargs {event.tool_kwargs}")
        elif verbose and isinstance(event, ToolCallResult):
            print(f"✅ Tool '{event.tool_name}' returned: {event.tool_output}")

    response = await handler
    return str(response)

# Import asyncio to run asynchronous main loop
import asyncio

# ----------------------------
# Main function to run the interactive loop
# ----------------------------
async def main():
    # Initialize MCP client and tool specification
    mcp_client = BasicMCPClient("http://127.0.0.1:8000/sse")
    mcp_tool = McpToolSpec(client=mcp_client)

    # Get the tool-augmented agent
    agent = await get_agent(mcp_tool)

    # Create a context for the agent to manage tool calls and memory
    agent_context = Context(agent)

    # Interactive loop for user input
    while True:
        user_input = input("Enter your message: ")
        if user_input.strip().lower() == "exit":
            print("👋 Exiting...")
            break

        print("User:", user_input)
        response = await handle_user_message(user_input, agent, agent_context, verbose=True)
        print("Agent:", response)

# ----------------------------
# Entry point
# ----------------------------
if __name__ == "__main__":
    asyncio.run(main())
