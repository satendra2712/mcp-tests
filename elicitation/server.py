from mcp.server.fastmcp import FastMCP
from mcp.types import TextContent, SamplingMessage

# Create a FastMCP server
mcp = FastMCP("elicitation-server")

@mcp.tool()
async def ask_user(question: str) -> str:
    """
    Asks the user a question and returns their answer using MCP sampling.
    """
    print(f"[Server] Asking user: {question}")

    try:
        # Get the request context to access sampling capabilities
        ctx = mcp.get_context()

        # Request sampling from the client
        result = await ctx.session.create_message(
            messages=[
                SamplingMessage(
                    role="user",
                    content=TextContent(type="text", text=question)
                )
            ],
            max_tokens=100,
            temperature=0.7
        )

        response_text = ""
        if result.content and isinstance(result.content, TextContent):
             response_text = result.content.text
        
        print(f"[Server] User answered: {response_text}")
        return f"User answered: {response_text}"

    except Exception as e:
        print(f"[Server] Failed to ask user: {e}")
        return f"Failed to ask user: {e}"

if __name__ == "__main__":
    mcp.run()
