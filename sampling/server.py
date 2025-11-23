# server.py
from mcp.server.fastmcp import FastMCP
from mcp.types import TextContent, SamplingMessage

# Create a FastMCP server
mcp = FastMCP("demo-server")

@mcp.tool()
async def trigger_sampling() -> str:
    """
    This tool demonstrates server -> client LLM sampling.
    """
    print("[Server] Calling sampling.createMessage on the client...")

    try:
        # Get the request context to access sampling capabilities
        ctx = mcp.get_context()

        # Request sampling from the client
        result = await ctx.session.create_message(
            messages=[
                SamplingMessage(
                    role="user",
                    content=TextContent(type="text", text="Explain MCP sampling.")
                )
            ],
            max_tokens=50,
            temperature=0.0
        )

        print("[Server] Got response from AI client:")
        print(f"  Model: {result.model}")
        print(f"  Role: {result.role}")
        
        response_text = ""
        if result.content and isinstance(result.content, TextContent):
             print(" ->", result.content.text)
             response_text = result.content.text
        
        return f"Sampling successful. Client responded: {response_text}"

    except Exception as e:
        print(f"[Server] Sampling failed: {e}")
        return f"Sampling failed: {e}"

if __name__ == "__main__":
    mcp.run()
