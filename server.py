import argparse  # Used to parse command-line arguments
from mcp.server.fastmcp import FastMCP  # Import FastMCP server from the MCP framework

# Initialize the MCP server with an application identifier
mcp = FastMCP("hello-world")

# ========================
# TOOL 1: Read Data
# ========================
@mcp.tool()
def read_data() -> str:
    """
    Simulates reading data from a table.

    Returns:
        str: A static response indicating a read operation.
    """
    return "Hello, there! I'm reading data from the table."

# ========================
# TOOL 2: Add Data
# ========================
@mcp.tool()
def add_data(message: str) -> str:
    """
    Simulates adding data to a table.

    Args:
        message (str): A message string representing the data to add.

    Returns:
        str: Confirmation message including the provided input.
    """
    return f"Data successfully added: {message}"

# ========================
# MAIN SERVER ENTRY POINT
# ========================
if __name__ == "__main__":
    print("🚀 Starting Hello World MCP Server...")

    # Set up the argument parser for server type selection
    parser = argparse.ArgumentParser()

    # Allow the user to specify server mode: SSE (default) or stdio
    parser.add_argument(
        "--server_type", type=str, default="sse", choices=["sse", "stdio"]
    )

    # Parse command-line arguments
    args = parser.parse_args()

    # Launch the MCP server using the selected mode
    mcp.run(args.server_type)
