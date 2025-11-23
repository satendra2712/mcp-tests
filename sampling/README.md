# MCP Sampling Test

This directory contains a demonstration of MCP sampling, where the server requests an LLM completion from the client.

## Files

- `server.py`: A FastMCP server that defines a `trigger_sampling` tool.
- `client_ai.py`: An MCP client that connects to the server and handles sampling requests.

## How to Run

1. Ensure you have the `mcp` library installed.
2. Run the client:

```bash
python3 client_ai.py
```

## Expected Output

You should see the client connect, call the tool, receive a sampling request, and print the result:

```
[Client] Connected to server. Calling trigger_sampling tool...
Processing request of type ListToolsRequest
[Client] Available tools: ['trigger_sampling']
Processing request of type CallToolRequest
[Client] Server requested LLM completion. Prompt = 'Explain MCP sampling.'
[Client] Tool result:
...
```

## Browser Testing

You can also test the server using the MCP Inspector in your browser:

1.  Make sure you have the MCP CLI installed:
    ```bash
    pip install "mcp[cli]"
    ```
2.  Run the server in development mode:
    ```bash
    mcp dev server.py
    ```
3.  This will launch the MCP Inspector in your default browser (usually at `http://localhost:5173` or similar).
4.  You can use the Inspector to call the `trigger_sampling` tool and see the interaction.
