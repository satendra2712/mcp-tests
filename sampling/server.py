# server.py
import asyncio
from mcp.server import Server
from mcp.client import Client
from mcp.server.stdio import StdioTransport
from mcp.types import Message, TextContent


server = Server("demo-server")


@server.tool()
async def trigger_sampling(client: Client):
    """
    This tool demonstrates server → client LLM sampling.
    """
    print("[Server] Calling sampling.complete on the client...")

    response = await client.sampling(
        model="demo-model",
        messages=[
            Message(
                role="user",
                content=[TextContent(type="text", text="Explain MCP sampling.")]
            )
        ],
        max_tokens=50,
        temperature=0.0
    )

    print("[Server] Got response from AI client:")
    for sample in response.samples:
        for c in sample.content:
            print(" →", c.text)

    return {"status": "done"}


async def main():
    transport = StdioTransport(server, client_command=["python", "client_ai.py"])
    await server.run(transport)


if __name__ == "__main__":
    asyncio.run(main())
