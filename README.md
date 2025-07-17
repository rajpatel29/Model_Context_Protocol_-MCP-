# Model Context Protocol (MCP) Example

This project demonstrates a basic Model Context Protocol (MCP) server and a Python client/agent that can interact with it using [LlamaIndex](https://www.llamaindex.ai/) and [Ollama](https://ollama.com/).

## What is LlamaIndex?
[LlamaIndex](https://www.llamaindex.ai/) is a data framework for building context-augmented LLM (Large Language Model) applications. It provides tools to connect LLMs to external data sources, manage tool calling, and orchestrate agent workflows.

## What is Ollama?
[Ollama](https://ollama.com/) is a platform for running open-source large language models locally. It allows you to download, manage, and serve LLMs (like Llama 3) on your own machine, making it easy to integrate powerful models into your applications without relying on cloud APIs.

## Features
- **MCP Server**: Exposes tool endpoints (e.g., `read_data`, `add_data`) for agent use.
- **Agent Client**: Connects to the MCP server, discovers tools, and allows interactive tool calling via LlamaIndex and Ollama LLM.

---

## Setup Instructions

### 1. Clone the Repository
```
git clone <your-repo-url>
cd LLM/Model_Context_Protocol_(MCP)
```

### 2. Install Python Dependencies
Make sure you have Python 3.8+ and pip installed.

```
pip install -r requirements.txt
```

---

## Running the MCP Server

Start the MCP server (in one terminal):

```
python3 server.py --server_type sse
```

- The server will start and expose tool endpoints at `http://127.0.0.1:8000/sse`.
- Available tools:
  - `read_data`: Simulates reading data from a table.
  - `add_data`: Simulates adding data to a table.

---

## Running the Agent Client

In a **separate terminal**, run the agent client:

```
python3 main.py
```

- The agent will connect to the MCP server and list available tools.
- You can interactively enter messages. The agent will use the tools as needed.
- Type `exit` to quit the agent.

---

## Example Usage

1. **Start the server:**
   ```
   python3 server.py --server_type sse
   ```
2. **Start the agent:**
   ```
   python3 main.py
   ```
3. **Interact:**
   - Enter: `read data from the table`
   - Enter: `add data: Hello World!`
   - Enter: `exit` to quit

---

## Requirements
- Python 3.8+
- [Ollama](https://ollama.com/) running locally (for LlamaIndex Ollama integration)
- All Python dependencies in `requirements.txt`

---

## Notes
- The MCP server and agent are for demonstration and development purposes.
- You can add more tools to `server.py` using the `@mcp.tool()` decorator.
- The agent uses LlamaIndex's FunctionAgent and can be extended for more complex workflows.

---

## License
MIT License 